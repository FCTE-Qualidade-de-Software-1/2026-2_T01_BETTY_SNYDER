# Análise de Flexibilidade

Esta página registra o estado da execução da frente de Flexibilidade (Dupla C) frente ao GQM da [Fase 2](../../fase2.md) e aos protocolos da [Fase 3](../../fase3.md). Não inventa valores de métrica: até existirem CSV em `avaliacao/dados/flexibilidade/`, o julgamento quantitativo permanece **não aplicável**.

## Escopo GQM

| Questão | Métricas (Fase 2) | Protocolo |
| --- | --- | --- |
| Q1 instalabilidade | T<sub>inst</sub>, T<sub>inst_t</sub>, N<sub>int</sub> | [Instalação](../protocolos/flexibilidade-instalacao.md) |
| Q2 adaptabilidade | P<sub>int</sub> (10 critérios) | [Checklist](../protocolos/flexibilidade-checklist.md) |
| Q3 substituibilidade | T<sub>pd</sub>, T<sub>sub</sub> | [Migração](../protocolos/flexibilidade-migracao.md) |

Máquinas de referência: [Ambiente](../protocolos/ambiente.md) (Windows: Bryan; macOS: Davi; Ubuntu: Dante).

## Evidências no repositório

| Artefato esperado | Situação em 20/11/2026 |
| --- | --- |
| CSV bruto (`T_inst_*`, `P_int_*`, `T_pd_*`, `T_sub_*`, …) | Ausentes; pastas com README e `.gitkeep` |
| Consolidado com faixas da Tabela XI | Ausente |
| Gráficos de instalação | Ausentes |
| Relatos qualitativos (Parte C das entrevistas) | Disponíveis nas fichas PA01, PB01, PB02 e PB03; ver [Fase 4](../../fase4.md) |

## Julgamento

| Questão / hipótese | Julgamento quantitativo | Observação |
| --- | --- | --- |
| Q1 / H1 | Não realizado | Sem medições de laboratório publicadas |
| Q2 / H2 | Não realizado | Sem checklist pontuado por SO |
| Q3 / H3 | Não realizado | Sem CSV de migração M1/M2 |

**Impacto no objetivo G de Flexibilidade.** O objetivo da Fase 2 não recebe resposta numérica nesta entrega. A evidência qualitativa das entrevistas (PB01/PB02/PB03; Gatekeeper no macOS; site confuso em PB03) **não substitui** T<sub>inst</sub>, P<sub>int</sub> ou T<sub>pd</sub>.

## Limitações e próximo passo da equipe

- Sem CSV, F4-C1 e F4-C3 ficam incompletos para esta característica.
- A ação de melhoria publicada (protótipo de “Criar baralho”) responde a Capacidade de interação, não a Flexibilidade.
- Próximo passo operacional da Dupla C: executar os três protocolos nas máquinas de referência, versionar CSV em `avaliacao/dados/flexibilidade/` e atualizar esta página e a [Fase 4](../../fase4.md).
