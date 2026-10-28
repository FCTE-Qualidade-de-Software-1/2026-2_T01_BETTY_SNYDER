# Organização no GitHub — Betty Snyder (PSM/CID)

Referência ao padrão em `padrao_documentacao_github.md` (pasta do projeto acadêmico), adaptado ao repositório `2026-2_T01_BETTY_SNYDER`.

Atualização de status das tarefas: **25/10/2026**.

## Project

**Nome previsto:** `Anki Quality Assessment — PSM/CID`

A criação do Project (Projects V2) exige o escopo OAuth `project` / `read:project`. Em 25/10/2026 a autorização device-flow do GitHub CLI com esses escopos foi **bloqueada** pela interface (“You can’t perform that action at this time” / falha de user code). Issues e milestones já foram criadas com o escopo `repo`.

Para concluir o Project (quando a autorização estiver disponível):

1. Autenticar o GitHub CLI com escopos de projeto:
   ```powershell
   $env:Path += ";C:\Users\pedro.rodrigues\AppData\Local\Temp\gh-cli\bin"
   gh auth login -h github.com -p https -w -s "repo,workflow,project,read:project,read:org"
   ```
2. Executar `scripts/setup-github-project.ps1` (cria o Project, campos e vincula as Issues).

Alternativa na UI: criar o Project `Anki Quality Assessment — PSM/CID` em Projects da organização ou do repositório e adicionar as Issues abertas.

Campos personalizados previstos (padrão §4.1): Status, Priority, PSM Category, Quality Attribute, Activity Type, Platform, Planned/Actual Effort (h), Estimated/Actual Cost (BRL), Planned Start/End, Actual Completion, Progress (%), Metric ID, Measurement Status, Evidence.

## Milestones

| # | Título | Due | Estado em 25/10 |
|---|---|---|---|
| 1 | PC1 | 19/10/2026 | **closed** (apresentação realizada) |
| 2 | F1 \| Plano de Medição e Preparação | 26/10/2026 | open — Issues da Entrega 1 / Fases 1–2 |
| 3 | F2 \| Execução e Análise das Medições | 11/11/2026 | open — coleta futura |
| 4 | E2 \| Relatório e Recomendações de Melhoria | 18/11/2026 | open — entrega final |

## Labels

Labels do padrão (`psm:*`, `quality:*`, `type:*`, `environment:*`, `priority:*`) mais `status:on-time`, `status:late`, `status:partial`, `status:pending` para o corte de 25/10.

Labels legadas (Usabilidade/Portabilidade etc.) permanecem no repositório; novas Issues usam o vocabulário ISO 25010:2023 do padrão.

## Issues (corte 25/10)

Foram criadas **46 Issues** a partir de `gestao-psm/calendario-progresso.csv`, milestone **F1**, com status no corpo e nas labels.

### Abertas (pendente ou parcial)

| Issue | ID | Status 25/10 |
|---|---|---|
| #11 | R01-C-REPO | parcial (issues/milestones criados; Project pendente de escopo OAuth) |
| #32 | E1-COMUM | pendente |
| #39 | E1-B2 | pendente |
| #40 | E1-B3 | pendente |
| #41 | E1-B4 | pendente |
| #42 | E1-B5 | pendente |
| #43 | E1-C1 | pendente |
| #44 | E1-C2 | parcial |
| #45 | E1-C3 | pendente |
| #46 | E1-C4 | pendente |

### Concluídas (closed)

As demais 36 Issues do calendário (R01-*, P2-*, E1-A1…A5, E1-B1) estão **closed**, com label `status:on-time` ou `status:late` conforme `concluida_no_prazo` no CSV.

## Templates de Issue

Arquivos locais (ainda sem commit, se não solicitados):

- `.github/ISSUE_TEMPLATE/01-activity.yml`
- `.github/ISSUE_TEMPLATE/02-measurement.yml`
- `.github/ISSUE_TEMPLATE/03-improvement.yml`
- `.github/ISSUE_TEMPLATE/config.yml`

## Links

- Issues: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/issues
- Milestones: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/milestones
