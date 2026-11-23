# Análise de Flexibilidade

Esta página interpreta as medidas de Flexibilidade (Dupla C) frente ao GQM da [Fase 2](../../fase2.md) e aos protocolos da [Fase 3](../../fase3.md). Os valores vêm dos CSV publicados em `avaliacao/dados/flexibilidade/consolidado/`, incluindo a migração M1/M2 publicada por Bryan70897 em 23/11/2026.

## Escopo GQM

| Questão | Métricas (Fase 2) | Protocolo |
| --- | --- | --- |
| Q1 instalabilidade | T<sub>inst</sub> (taxa de sucesso), T<sub>inst_t</sub> (tempo), N<sub>int</sub> (intervenções manuais extras) | [Instalação](../protocolos/flexibilidade-instalacao.md) |
| Q2 adaptabilidade | P<sub>int</sub> (checklist de 10 critérios de integração com o sistema) | [Checklist](../protocolos/flexibilidade-checklist.md) |
| Q3 substituibilidade | T<sub>pd</sub>, T<sub>sub</sub> | [Migração](../protocolos/flexibilidade-migracao.md) |

Máquinas de referência: [Ambiente](../protocolos/ambiente.md) (Windows: Bryan; macOS: Davi; Ubuntu: Dante).

## Evidências no repositório

| Artefato | Situação em 23/11/2026 |
| --- | --- |
| Tempos de instalação | [`flexibilidade-instalacao-tempo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-instalacao-tempo.csv) |
| Checklist P<sub>int</sub> | [`flexibilidade-checklist-registro.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-checklist-registro.csv) |
| Migração (T<sub>pd</sub>, T<sub>sub</sub>) | [`flexibilidade-migracao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-migracao.csv) (6 ensaios em 20/11/2026: M1 `.apkg` e M2 AnkiWeb, 3 repetições cada) |
| Gráficos | `grafico_flexibilidade_tempo_instalacao_3so.png`; `grafico-flexibilidade-checklist.png` (cópias em `docs/assets/` para a GitPage) |
| CSV bruto no padrão `<métrica>_<cenário>_<execução>` | Ainda não espelhados em `bruto/` (os nomes `diff_m*_rep*.csv` constam no consolidado) |
| Relatos qualitativos (Parte C) | Fichas PA01, PB01, PB02 e PB03; ver [Fase 4](../../fase4.md) |

## Resultados de instalação (Q1)

| Sistema | Sucesso | T<sub>inst_t</sub> | N<sub>int</sub> | Observação do avaliador |
| --- | --- | --- | --- | --- |
| Windows 11 (x64) | Sim | 3,82 min (229 s) | 0 | Instalador demorou mais de 1 min na etapa de status/extração |
| macOS 27 (ARM) | Sim | 0,55 min (33 s) | 0 | Instalação rápida via `.dmg` |
| Ubuntu 26.04.1 (x64, Wayland) | Sim | 0,97 min (58 s) | 0 | Instalação via terminal (`sudo ./install.sh`); desinstalação via `apt` |

Faixas (Tabela XI): nos três sistemas, T<sub>inst</sub> = 100% sem intervenção. Em macOS e Ubuntu, T<sub>inst_t</sub> &lt; 2 min (excelente) e, portanto, T<sub>inst</sub> na faixa excelente. No Windows, T<sub>inst_t</sub> entre 2 e 5 min (alvo); T<sub>inst</sub> na faixa alvo. N<sub>int</sub> = 0 (excelente) nos três.

## Resultados do checklist (Q2)

P<sub>int</sub> = 10/10 em Windows, macOS e Ubuntu (critérios C1 a C10 todos atendidos). Faixa: **excelente**. Avaliadores: Bryan (Windows), Davi (macOS), Dante (Ubuntu); conferente Bryan.

## Resultados de migração (Q3)

Fonte: [`flexibilidade-migracao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-migracao.csv). Coleção padrão de 10 mil cartões; verificação de integridade com `n_diferentes = 0` em todas as linhas; intervenções: nenhuma.

| Cenário | Repetições | T<sub>pd</sub> | T<sub>sub</sub> (min) | Faixa T<sub>sub</sub> |
| --- | --- | --- | --- | --- |
| M1 (`.apkg`) | 3 (Win→Ubuntu, Ubuntu→macOS, macOS→Win) | 100% (0 diferenças / 10.000) | 2,33; 2,50; 2,66 (média 2,50) | Mínimo (2 a 5 min) |
| M2 (AnkiWeb) | 3 (mesmos pares de SO) | 100% (0 diferenças / 10.000) | 2,41; 2,50; 2,66 (média 2,52) | Mínimo (2 a 5 min) |
| **Agregado** | **6** | **100%** | **média 2,51 min** (mín. 2,33; máx. 2,66) | **Mínimo** |

**Leitura das faixas.** A definição de T<sub>pd</sub> é a taxa de preservação (100% em todos os ensaios, sem perda e sem intervenção). Na Tabela XI, as faixas alvo e excelente de T<sub>pd</sub> acoplam preservação a tempo ≤ 1 min; esse tempo não foi atingido. T<sub>sub</sub> cai na faixa **mínimo** (2 a 5 min). Pela regra de julgamento (prevalece a faixa mais baixa), **Q3 não é atendida no alvo**.

## Julgamento

| Questão / hipótese | Julgamento quantitativo | Observação |
| --- | --- | --- |
| Q1 / H1 | Atendida (alvo ou excelente) | H1 parcial no Ubuntu: o tempo ficou abaixo de 2 min e sem intervenção, ao contrário da expectativa de 2 a 5 min com intervenção |
| Q2 / H2 | Atendida (excelente) | P<sub>int</sub> = 10/10 nos três sistemas |
| Q3 / H3 | Q3 não atendida no alvo; H3 parcial | Preservação 100% confirmada (parte de H3); tempo de substituição &lt; 1 min **não** confirmado (T<sub>sub</sub> média 2,51 min) |

**Impacto no objetivo G de Flexibilidade.** Q1 e Q2 recebem resposta numérica no alvo ou excelente. Q3 tem evidência completa, mas o tempo de migração fica na faixa mínimo: o estudante consegue trocar de máquina sem perda de dados, porém acima do limiar de 1 min da hipótese.

## Limitações e próximo passo da equipe

- Uma instalação por SO não permite desvio padrão de T<sub>inst_t</sub>.
- Os arquivos `diff_m*_rep*.csv` citados no consolidado ainda não estão versionados em `bruto/migracao/`.
- A ação de melhoria (protótipo de “Criar baralho”) responde a Capacidade de interação, não a Flexibilidade.
- Encaminhamento opcional: reduzir T<sub>sub</sub> (otimizar exportação/importação ou sincronização) se a equipe priorizar elevar Q3 ao alvo; espelhar os diffs em `bruto/`.
