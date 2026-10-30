# Organização no GitHub (PSM / CID)

Esta página descreve a configuração do repositório `2026-2_T01_BETTY_SNYDER` como suporte à coleta e ao rastreamento das medidas PSM/CID. O padrão de referência é o documento `padrao_documentacao_github.md` (pasta do projeto acadêmico), adaptado ao contexto da equipe Betty Snyder.

Atualização de status das tarefas: **25/10/2026**.

No modelo de informação do PSM (RAMOS, 2026), Project, milestones, labels e issues constituem **entidades e atributos** a partir dos quais se aplicam métodos de medição (contagens, esforço, prazo). A Parte 1 do *framework* CID orienta o que medir (JONES et al., 2021a); a Parte 2 especifica como operacionalizar as medidas (JONES et al., 2021b). A relação com cada categoria consta em [Calendário e progresso](calendario-e-progresso.md), [Recursos e custos](recursos-e-custos.md) e [Procedimentos e lacunas](procedimentos-e-lacunas.md).

## Project

**Nome previsto:** `Anki Quality Assessment — PSM/CID`

A criação do Project (Projects V2) exige o escopo OAuth `project` / `read:project`. Em 25/10/2026 a autorização *device-flow* do GitHub CLI com esses escopos foi **bloqueada** pela interface (“You can’t perform that action at this time” / falha de *user code*). Issues e milestones já foram criadas com o escopo `repo`.

Para concluir o Project (quando a autorização estiver disponível):

1. Autenticar o GitHub CLI com escopos de projeto:
   ```powershell
   $env:Path += ";C:\Users\pedro.rodrigues\AppData\Local\Temp\gh-cli\bin"
   gh auth login -h github.com -p https -w -s "repo,workflow,project,read:project,read:org"
   ```
2. Executar `scripts/setup-github-project.ps1` (cria o Project, campos e vincula as Issues).

Alternativa na UI: criar o Project `Anki Quality Assessment — PSM/CID` em Projects da organização ou do repositório e adicionar as Issues abertas.

### Campos personalizados previstos (padrão §4.1)

| Campo | Uso PSM / CID |
|---|---|
| Status | Estados de fluxo (A Fazer, Em Andamento, Concluído) |
| Priority | Priorização gerencial do item |
| PSM Category | Recursos e custos; Calendário e progresso; Desempenho dos processos |
| Quality Attribute | Atributo GQM do produto (quando a issue for de medição do Anki) |
| Activity Type | Tipo de atividade do projeto |
| Platform | Ambiente de execução (medições de produto) |
| Planned / Actual Effort (h) | Medidas básicas de esforço (Recursos e custos) |
| Estimated / Actual Cost (BRL) | Extensão financeira (ainda não operacionalizada) |
| Planned Start / End | Compromisso de calendário |
| Actual Completion | Conclusão real (base para ICP e *cycle time*) |
| Progress (%) | Proxy de progresso da unidade de trabalho |
| Metric ID | Identificador da métrica (PSM ou GQM) |
| Measurement Status | Situação do dado coletado |
| Evidence | Evidência bruta ou caminho no repositório |

Enquanto o Project V2 não estiver ativo, a fonte canônica de calendário permanece o CSV `gestao-psm/calendario-progresso.csv`, e os campos de esforço monetário e de transição de estado configuram **lacunas** documentadas em [Procedimentos e lacunas](procedimentos-e-lacunas.md).

## Milestones

Os milestones aproximam os marcos (*releases*) do mapeamento CID para contagem de *work items* comprometidos e concluídos.

| # | Título | Due | Estado em 25/10 |
|---|---|---|---|
| 1 | PC1 | 19/10/2026 | **closed** (apresentação realizada) |
| 2 | F1 \| Plano de Medição e Preparação | 26/10/2026 | open — Issues da Entrega 1 / Fases 1–2 |
| 3 | F2 \| Execução e Análise das Medições | 11/11/2026 | open — coleta futura |
| 4 | E2 \| Relatório e Recomendações de Melhoria | 18/11/2026 | open — entrega final |

## Labels

Labels do padrão (`psm:*`, `quality:*`, `type:*`, `environment:*`, `priority:*`) mais `status:on-time`, `status:late`, `status:partial`, `status:pending` para o corte de 25/10.

As labels `status:*` alimentam a análise de conformidade de prazos (ICP) em [Calendário e progresso](calendario-e-progresso.md). Elas **não** substituem os estados de fluxo To Do / In Progress / Done necessários a *Cycle Time*, *Throughput* e WIP.

Labels legadas (Usabilidade/Portabilidade etc.) permanecem no repositório; novas Issues usam o vocabulário ISO 25010:2023 do padrão.

## Issues (corte 25/10)

Foram criadas **46 Issues** a partir de `gestao-psm/calendario-progresso.csv`, milestone **F1**, com status no corpo e nas labels. Na Entrega 1 as issues **não** foram fonte primária de medição; após o Ponto de Controle 1 passaram a materializar o compromisso de trabalho.

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

Arquivos em `.github/ISSUE_TEMPLATE/`:

| Template | Papel |
|---|---|
| `01-activity.yml` | Atividades do **projeto** (candidatas a medidas PSM de calendário e esforço) |
| `02-measurement.yml` | Observações de métricas **GQM do produto Anki** (não confundir com PSM) |
| `03-improvement.yml` | Ações de melhoria |
| `config.yml` | Configuração dos templates |

## Links

- Issues: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/issues
- Milestones: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/milestones

## Referências

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 1: concepts, definitions, principles, and measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021a. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 2: measurement specifications and enterprise measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021b. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

RAMOS, Cristiane Soares. **Medição prática de software e sistemas**: PSM – Practical Software and System Measurement. Notas de aula. Brasília: Faculdade do Gama, Universidade de Brasília, 2026. Material didático da disciplina Qualidade de Software 1 (FGA0315).

Voltar à [visão geral do PSM](../gestao-psm.md).
