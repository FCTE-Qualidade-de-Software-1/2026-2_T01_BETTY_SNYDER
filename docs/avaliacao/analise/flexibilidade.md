# Análise de Flexibilidade

Esta página interpreta as medidas de Flexibilidade (Dupla C) frente ao GQM da [Fase 2](../../fase2.md) e aos protocolos da [Fase 3](../../fase3.md). Os valores vêm dos CSV publicados em `avaliacao/dados/flexibilidade/consolidado/`. A migração entre sistemas operacionais (Q3) ainda não tem CSV; para T<sub>pd</sub> e T<sub>sub</sub> o julgamento quantitativo permanece **não aplicável**.

## Escopo GQM

| Questão | Métricas (Fase 2) | Protocolo |
| --- | --- | --- |
| Q1 instalabilidade | T<sub>inst</sub> (taxa de sucesso), T<sub>inst_t</sub> (tempo), N<sub>int</sub> (intervenções manuais extras) | [Instalação](../protocolos/flexibilidade-instalacao.md) |
| Q2 adaptabilidade | P<sub>int</sub> (checklist de 10 critérios de integração com o sistema) | [Checklist](../protocolos/flexibilidade-checklist.md) |
| Q3 substituibilidade | T<sub>pd</sub>, T<sub>sub</sub> | [Migração](../protocolos/flexibilidade-migracao.md) |

Máquinas de referência: [Ambiente](../protocolos/ambiente.md) (Windows: Bryan; macOS: Davi; Ubuntu: Dante).

## Evidências no repositório

| Artefato | Situação em 22/11/2026 |
| --- | --- |
| Tempos de instalação | [`flexibilidade-instalacao-tempo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-instalacao-tempo.csv) |
| Checklist P<sub>int</sub> | [`flexibilidade-checklist-registro.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-checklist-registro.csv) |
| Gráficos | `grafico_flexibilidade_tempo_instalacao_3so.png`; `grafico-flexibilidade-checklist.png` (cópias em `docs/assets/` para a GitPage) |
| CSV bruto no padrão `<métrica>_<cenário>_<execução>` | Ainda não espelhados em `bruto/` |
| Migração (T<sub>pd</sub>, T<sub>sub</sub>) | Ausente |
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

## Julgamento

| Questão / hipótese | Julgamento quantitativo | Observação |
| --- | --- | --- |
| Q1 / H1 | Atendida (alvo ou excelente) | H1 parcial no Ubuntu: o tempo ficou abaixo de 2 min e sem intervenção, ao contrário da expectativa de 2 a 5 min com intervenção |
| Q2 / H2 | Atendida (excelente) | P<sub>int</sub> = 10/10 nos três sistemas |
| Q3 / H3 | Não realizado | Sem CSV de migração M1/M2 |

**Impacto no objetivo G de Flexibilidade.** Q1 e Q2 recebem resposta numérica. Q3 permanece aberta. Os relatos das entrevistas (instalação no site, Gatekeeper, Obsidian) **complementam** o laboratório, mas não substituem T<sub>pd</sub> nem T<sub>sub</sub>.

## Limitações e próximo passo da equipe

- F4-C1 e F4-C2 ficam parciais enquanto a migração e o espelhamento bruto no padrão de nomes não forem publicados.
- A ação de melhoria (protótipo de “Criar baralho”) responde a Capacidade de interação, não a Flexibilidade.
- Próximo passo operacional da Dupla C: versionar CSV de migração (T<sub>pd</sub>, T<sub>sub</sub>) e, se possível, alinhar `bruto/` ao padrão `<métrica>_<cenário>_<execução>`. Atualizar esta página e a [Fase 4](../../fase4.md).
