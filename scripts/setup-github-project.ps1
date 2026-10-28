#Requires -Version 5.1
<#
.SYNOPSIS
  Cria o GitHub Project V2 "Anki Quality Assessment — PSM/CID" e vincula Issues do repositório.
.NOTES
  Requer gh autenticado com escopos: project, read:project, repo.
  Uso: .\scripts\setup-github-project.ps1
#>
$ErrorActionPreference = "Stop"
$gh = Get-Command gh -ErrorAction SilentlyContinue
if (-not $gh) {
  $fallback = "C:\Users\pedro.rodrigues\AppData\Local\Temp\gh-cli\bin\gh.exe"
  if (Test-Path $fallback) { $ghExe = $fallback } else { throw "Instale o GitHub CLI (gh)." }
} else { $ghExe = $gh.Source }

function Invoke-GQL([string]$Query, [hashtable]$Variables = $null) {
  $body = @{ query = $Query }
  if ($Variables) { $body.variables = $Variables }
  $tmp = Join-Path $env:TEMP ("gql-" + [guid]::NewGuid().ToString() + ".json")
  [System.IO.File]::WriteAllText($tmp, ($body | ConvertTo-Json -Depth 8 -Compress))
  $out = & $ghExe api graphql --input $tmp
  if ($LASTEXITCODE -ne 0) { throw "GraphQL falhou: $out" }
  return ($out | ConvertFrom-Json)
}

Write-Host "Verificando escopos..."
& $ghExe auth status

$owner = "FCTE-Qualidade-de-Software-1"
$repoName = "2026-2_T01_BETTY_SNYDER"
$title = "Anki Quality Assessment — PSM/CID"

$repoQ = @'
query($o:String!,$n:String!){
  repository(owner:$o,name:$n){ id }
  viewer { id }
}
'@
$ids = Invoke-GQL $repoQ @{ o = $owner; n = $repoName }
$ownerId = $ids.data.viewer.id
$repoId = $ids.data.repository.id
Write-Host "ownerId=$ownerId repoId=$repoId"

$createQ = @'
mutation($ownerId:ID!,$title:String!,$repoId:ID!){
  createProjectV2(input:{ownerId:$ownerId,title:$title,repositoryId:$repoId}){
    projectV2 { id title number url }
  }
}
'@
try {
  $created = Invoke-GQL $createQ @{ ownerId = $ownerId; title = $title; repoId = $repoId }
  $project = $created.data.createProjectV2.projectV2
} catch {
  Write-Host "createProjectV2 com repositoryId falhou; tentando só owner+title..."
  $createQ2 = @'
mutation($ownerId:ID!,$title:String!){
  createProjectV2(input:{ownerId:$ownerId,title:$title}){
    projectV2 { id title number url }
  }
}
'@
  $created = Invoke-GQL $createQ2 @{ ownerId = $ownerId; title = $title }
  $project = $created.data.createProjectV2.projectV2
  $linkQ = @'
mutation($projectId:ID!,$repositoryId:ID!){
  linkProjectV2ToRepository(input:{projectId:$projectId,repositoryId:$repositoryId}){
    repository { name }
  }
}
'@
  Invoke-GQL $linkQ @{ projectId = $project.id; repositoryId = $repoId } | Out-Null
}

Write-Host "Project: $($project.url)"

# Campos single-select / number / date / text conforme padrão §4.1
function Add-SelectField($projectId, $name, [string[]]$options) {
  $opts = ($options | ForEach-Object { "{ name: `"$_`" }" }) -join ", "
  $q = @"
mutation {
  createProjectV2Field(input: {
    projectId: `"$projectId`"
    dataType: SINGLE_SELECT
    name: `"$name`"
    singleSelectOptions: [$opts]
  }) {
    projectV2Field { ... on ProjectV2SingleSelectField { id name } }
  }
}
"@
  try { Invoke-GQL $q | Out-Null; Write-Host "campo $name" } catch { Write-Host "aviso campo $name : $_" }
}

function Add-SimpleField($projectId, $name, $dataType) {
  $q = @"
mutation {
  createProjectV2Field(input: {
    projectId: `"$projectId`"
    dataType: $dataType
    name: `"$name`"
  }) {
    projectV2Field { ... on ProjectV2FieldCommon { id name } }
  }
}
"@
  try { Invoke-GQL $q | Out-Null; Write-Host "campo $name ($dataType)" } catch { Write-Host "aviso campo $name : $_" }
}

Add-SelectField $project.id "Priority" @("High","Medium","Low")
Add-SelectField $project.id "PSM Category" @("Process Performance","Resources & Costs","Schedule & Progress")
Add-SelectField $project.id "Quality Attribute" @("Interaction Capability","Performance Efficiency","Flexibility","Cross-cutting")
Add-SelectField $project.id "Activity Type" @("Planning","Execution","Measurement","Analysis","Documentation","Improvement")
Add-SelectField $project.id "Platform" @("Desktop Windows","Desktop macOS","Desktop Ubuntu","AnkiWeb","Cross-platform")
Add-SelectField $project.id "Measurement Status" @("Not Started","Collected","Validated","Analyzed")
Add-SimpleField $project.id "Planned Effort (h)" "NUMBER"
Add-SimpleField $project.id "Actual Effort (h)" "NUMBER"
Add-SimpleField $project.id "Estimated Cost (BRL)" "NUMBER"
Add-SimpleField $project.id "Actual Cost (BRL)" "NUMBER"
Add-SimpleField $project.id "Planned Start" "DATE"
Add-SimpleField $project.id "Planned End" "DATE"
Add-SimpleField $project.id "Actual Completion" "DATE"
Add-SimpleField $project.id "Progress (%)" "NUMBER"
Add-SimpleField $project.id "Metric ID" "TEXT"
Add-SimpleField $project.id "Evidence" "TEXT"

# Vincular todas as issues do repositório
$issues = & $ghExe api "repos/$owner/$repoName/issues?state=all&per_page=100" --jq ".[].node_id"
foreach ($nodeId in $issues) {
  if (-not $nodeId) { continue }
  $addQ = @'
mutation($projectId:ID!,$contentId:ID!){
  addProjectV2ItemById(input:{projectId:$projectId,contentId:$contentId}){
    item { id }
  }
}
'@
  try {
    Invoke-GQL $addQ @{ projectId = $project.id; contentId = $nodeId } | Out-Null
    Write-Host "item $nodeId"
  } catch {
    Write-Host "aviso item $nodeId : $_"
  }
}

Write-Host "Concluído. Abra: $($project.url)"
Write-Host "Configure as Views (Board, Table PSM, Medições, Cronograma) na UI do Project."
