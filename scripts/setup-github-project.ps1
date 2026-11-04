#Requires -Version 5.1
<#
.SYNOPSIS
  Verifica e completa a configuração do GitHub Project V2 BETTY SNYDER (#40).
.NOTES
  Requer gh autenticado com escopos: project, read:project, repo.
  Uso: .\scripts\setup-github-project.ps1
#>
$ErrorActionPreference = "Stop"
$gh = Get-Command gh -ErrorAction SilentlyContinue
if (-not $gh) { throw "Instale e autentique o GitHub CLI (gh)." }
$ghExe = $gh.Source

$owner = "FCTE-Qualidade-de-Software-1"
$repoName = "2026-2_T01_BETTY_SNYDER"
$projectNumber = 40
$projectTitle = "BETTY SNYDER"

function Invoke-GQL([string]$Query, [hashtable]$Variables = @{}) {
  $body = @{ query = $Query; variables = $Variables }
  $tmp = Join-Path $env:TEMP ("gql-" + [guid]::NewGuid().ToString() + ".json")
  try {
    [System.IO.File]::WriteAllText(
      $tmp,
      ($body | ConvertTo-Json -Depth 8 -Compress),
      (New-Object System.Text.UTF8Encoding($false))
    )
    $out = & $ghExe api graphql --input $tmp
    if ($LASTEXITCODE -ne 0) { throw "GraphQL falhou: $out" }
    $response = $out | ConvertFrom-Json
    if ($response.errors) {
      throw "GraphQL retornou erro: $(($response.errors | ForEach-Object { $_.message }) -join '; ')"
    }
    return $response.data
  } finally {
    if (Test-Path $tmp) { Remove-Item -LiteralPath $tmp }
  }
}

Write-Host "Verificando autenticação e escopos..."
$authStatus = & $ghExe auth status 2>&1
if ($LASTEXITCODE -ne 0) { throw "Autentique o GitHub CLI com gh auth login." }
$authText = $authStatus -join "`n"
foreach ($scope in @("'project'", "'read:project'", "'repo'")) {
  if ($authText -notmatch [regex]::Escape($scope)) {
    throw "O token precisa do escopo $scope. Execute: gh auth refresh -h github.com -s project,read:project,repo"
  }
}
Write-Host $authStatus

$projectQuery = @'
query($owner:String!,$number:Int!,$repoOwner:String!,$repoName:String!){
  organization(login:$owner){
    projectV2(number:$number){
      id title number url
      repositories(first:100){nodes{nameWithOwner}}
      items(first:100){
        nodes{id content{... on Issue{id}}}
        pageInfo{hasNextPage}
      }
      fields(first:100){
        nodes{
          ... on ProjectV2FieldCommon{id name dataType}
        }
      }
    }
  }
  repository(owner:$repoOwner,name:$repoName){id}
}
'@
$data = Invoke-GQL $projectQuery @{
  owner = $owner
  number = $projectNumber
  repoOwner = $owner
  repoName = $repoName
}
$project = $data.organization.projectV2
$repository = $data.repository
if (-not $project) { throw "Project da organização #$projectNumber não foi encontrado." }
if ($project.items.pageInfo.hasNextPage) {
  throw "O Project tem mais de 100 itens; a paginação do inventário precisa ser expandida antes de provisionar."
}
if ($project.title -cne $projectTitle) {
  throw "O Project #$projectNumber tem nome '$($project.title)', esperado '$projectTitle'. Nada foi alterado."
}
if (-not $repository) { throw "Repositório $owner/$repoName não foi encontrado." }

Write-Host "Project confirmado: $($project.url)"

$isLinked = @($project.repositories.nodes | Where-Object {
  $_.nameWithOwner -eq "$owner/$repoName"
}).Count -gt 0
if (-not $isLinked) {
  $linkQuery = @'
mutation($projectId:ID!,$repositoryId:ID!){
  linkProjectV2ToRepository(input:{projectId:$projectId,repositoryId:$repositoryId}){
    repository{nameWithOwner}
  }
}
'@
  Invoke-GQL $linkQuery @{ projectId = $project.id; repositoryId = $repository.id } | Out-Null
  Write-Host "Repositório vinculado: $owner/$repoName"
} else {
  Write-Host "Repositório já vinculado: $owner/$repoName"
}

$requiredFields = @(
  @{ Name = "Esforço planejado (horas)"; DataType = "NUMBER" },
  @{ Name = "Esforço real (horas)"; DataType = "NUMBER" },
  @{ Name = "Data início planejada"; DataType = "DATE" },
  @{ Name = "Data fim planejada"; DataType = "DATE" },
  @{ Name = "Data fim real"; DataType = "DATE" },
  @{ Name = "Progresso (%)"; DataType = "NUMBER" },
  @{ Name = "Evidência (link)"; DataType = "TEXT" }
)
$createFieldQuery = @'
mutation($projectId:ID!,$name:String!,$dataType:ProjectV2CustomFieldType!){
  createProjectV2Field(input:{projectId:$projectId,name:$name,dataType:$dataType}){
    projectV2Field{
      ... on ProjectV2FieldCommon{id name dataType}
    }
  }
}
'@

foreach ($required in $requiredFields) {
  $existing = @($project.fields.nodes | Where-Object { $_.name -ceq $required.Name })
  if ($existing.Count -gt 1) {
    throw "Há mais de um campo '$($required.Name)' no Project #$projectNumber."
  }
  if ($existing.Count -eq 1) {
    if ($existing[0].dataType -cne $required.DataType) {
      throw "O campo '$($required.Name)' tem tipo '$($existing[0].dataType)', esperado '$($required.DataType)'."
    }
    Write-Host "Campo OK: $($required.Name) ($($required.DataType))"
    continue
  }

  $created = Invoke-GQL $createFieldQuery @{
    projectId = $project.id
    name = $required.Name
    dataType = $required.DataType
  }
  $field = $created.createProjectV2Field.projectV2Field
  if (-not $field) { throw "A API não confirmou a criação do campo '$($required.Name)'." }
  Write-Host "Campo criado: $($field.name) ($($field.dataType))"
}

$issues = & $ghExe api --paginate "repos/$owner/$repoName/issues?state=all&per_page=100" --jq '.[] | select(.pull_request == null) | .node_id'
if ($LASTEXITCODE -ne 0) { throw "Não foi possível listar as Issues de $owner/$repoName." }

$addQuery = @'
mutation($projectId:ID!,$contentId:ID!){
  addProjectV2ItemById(input:{projectId:$projectId,contentId:$contentId}){
    item{id}
  }
}
'@
$linkedIssueIds = @{}
foreach ($item in $project.items.nodes) {
  if ($item.content.id) { $linkedIssueIds[$item.content.id] = $true }
}

$added = 0
$checked = 0
foreach ($nodeId in $issues) {
  if (-not $nodeId) { continue }
  $checked++
  if ($linkedIssueIds.ContainsKey($nodeId)) { continue }
  Invoke-GQL $addQuery @{ projectId = $project.id; contentId = $nodeId } | Out-Null
  $linkedIssueIds[$nodeId] = $true
  $added++
}

Write-Host "Concluído: $added Issues adicionadas; $checked verificadas no Project #$projectNumber."
Write-Host "Views configuráveis na interface do Project: Kanban e Tabela PSM."
