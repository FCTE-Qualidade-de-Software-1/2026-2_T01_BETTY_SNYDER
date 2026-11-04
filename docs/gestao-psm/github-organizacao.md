# Organização no GitHub (PSM / CID)

Esta página documenta a infraestrutura do repositório `2026-2_T01_BETTY_SNYDER` empregada na coleta e no rastreamento das medidas PSM/CID. O padrão de referência é o documento `padrao_documentacao_github.md` (pasta do projeto acadêmico), adaptado ao contexto da equipe Betty Snyder. Atualização: **03/11/2026**.

No modelo de informação do PSM (RAMOS, 2026), Project, milestones, labels e issues correspondem a **entidades** e aos respectivos **atributos** sobre os quais se aplicam métodos de medição (contagens, esforço, prazo e estado de fluxo). A Parte 1 do *framework* CID orienta a seleção do que medir (JONES et al., 2021a); a Parte 2 especifica os procedimentos de coleta, cálculo e análise (JONES et al., 2021b). O detalhamento por categoria consta em [Recursos e custos](recursos-e-custos.md), [Calendário e progresso](calendario-e-progresso.md) e [Desempenho dos processos](desempenho-dos-processos.md).

## Project

- **Nome:** `BETTY SNYDER`
- **Tipo:** GitHub Projects V2 da organização, com o repositório padrão `FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER`.
- **URL:** https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/40
- **Script de provisionamento:** `scripts/setup-github-project.ps1` (completa o Project #40 existente; não cria outro).

O nome, o repositório padrão e os sete campos foram conferidos nas configurações do Project e pela API GraphQL em **03/11/2026**. O campo nativo Status usa os estados **A Fazer** (*Todo*), **Em Andamento** (*In Progress*) e **Concluído** (*Done*), alinhados ao mapeamento CID. Na mesma conferência, o Project continha **4 itens**, enquanto o repositório tinha 46 Issues; o script de provisionamento verifica campos, vínculo e inclui Issues ainda ausentes. Para executar mutações, autentique `gh` com os escopos `project` e `repo`. Os custos são derivados do esforço, sem campo dedicado de categoria PSM ou de custo.

### Campos padrão do Project

Os sete campos personalizados do Project #40 e seus tipos:

| Campo | Tipo | Uso PSM / CID |
|---|---|---|
| Esforço planejado (horas) | Número | Esforço de referência da atividade (\(H_p\)) |
| Esforço real (horas) | Número | Esforço realizado (\(H_r\)) |
| Data início planejada | Data | Início previsto para a atividade |
| Data fim planejada | Data | Prazo previsto; referência para o ICP |
| Data fim real | Data | Data de conclusão efetiva; base para o ICP |
| Progresso (%) | Número | Acompanhamento do avanço da atividade |
| Evidência (link) | Texto | Rastreabilidade para entregáveis e registros |

O campo nativo **Status** acompanha o fluxo e não faz parte desses sete campos personalizados. O *Cycle Time* deve ser obtido do histórico de transições de Status (início real até conclusão), não calculado com Data início planejada. Os custos são derivados dos esforços pela taxa definida em [Recursos e custos](recursos-e-custos.md); não são campos do Project.

A série histórica da Entrega 1 permanece nos CSV em `gestao-psm/`. Nos cortes seguintes, medidas de calendário e esforço podem ser obtidas dos campos nativos depois de preenchidos; medidas de fluxo usam o histórico de Status das Issues já incluídas no quadro.

## Milestones

Os milestones aproximam os marcos (*releases*) do mapeamento CID para contagem de *work items* comprometidos e concluídos.

| # | Título | Due | Estado em 25/10 |
|---|---|---|---|
| 1 | PC1 | 19/10/2026 | **closed** (apresentação realizada) |
| 2 | F1 \| Plano de Medição e Preparação | 26/10/2026 | open: Issues da Entrega 1 / Fases 1–2 |
| 3 | F2 \| Execução e Análise das Medições | 11/11/2026 | open: coleta futura |
| 4 | E2 \| Relatório e Recomendações de Melhoria | 18/11/2026 | open: entrega final |

## Labels

Labels do padrão (`psm:*`, `quality:*`, `type:*`, `environment:*`, `priority:*`) mais `status:on-time`, `status:late`, `status:partial`, `status:pending` para o corte de 25/10.

As labels `status:*` alimentam a análise de conformidade de prazos (ICP) em [Calendário e progresso](calendario-e-progresso.md). Os estados de fluxo To Do / In Progress / Done no Project complementam essas labels para *Cycle Time*, *Throughput* e WIP.

Labels legadas (Usabilidade/Portabilidade etc.) permanecem no repositório; novas Issues usam o vocabulário ISO 25010:2023 do padrão.

## Issues (corte 25/10)

Foram criadas **46 Issues** a partir de `gestao-psm/calendario-progresso.csv`, milestone **F1**, com status no corpo e nas labels. Na Entrega 1 as issues **não** foram fonte primária de medição. Na conferência de 03/11/2026, 4 das 46 Issues constavam como itens do Project #40; execute `gh auth refresh -h github.com -s project,repo` e depois `scripts/setup-github-project.ps1` para incluir as demais.

### Abertas (pendente ou parcial)

| Issue | ID | Status 25/10 |
|---|---|---|
| #11 | R01-C-REPO | parcial (issues, milestones e Project constituídos) |
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

## Guia da equipe (PDF)

Passo a passo de abertura e fechamento de Issues e relação com as categorias PSM:

- [padrao-abertura-fechamento-issues-psm.pdf](padrao-abertura-fechamento-issues-psm.pdf)
- Script de sincronização do bloco de campos no corpo das Issues: `scripts/sync-issue-fields.py`
- Mapeamento gerado: [mapeamento-campos-issues.csv](mapeamento-campos-issues.csv)

O formulário 01 coleta os sete valores no corpo da Issue. `scripts/sync-issue-fields.py` atualiza o bloco espelhado no corpo, as labels e o CSV de mapeamento; ele **não** altera os campos nativos do Project. Após sincronizar, confira/atualize os valores correspondentes no quadro. Para executar o provisionamento, o GitHub CLI precisa dos escopos `project` e `repo`.

## Links

- Issues: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/issues
- Milestones: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/milestones
- Projects: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/projects

## Referências

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 1: concepts, definitions, principles, and measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021a. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 2: measurement specifications and enterprise measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021b. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

RAMOS, Cristiane Soares. **Medição prática de software e sistemas**: PSM: Practical Software and System Measurement. Notas de aula. Brasília: Faculdade do Gama, Universidade de Brasília, 2026. Material didático da disciplina Qualidade de Software 1 (FGA0315).

Voltar à [visão geral do PSM](../gestao-psm.md).
