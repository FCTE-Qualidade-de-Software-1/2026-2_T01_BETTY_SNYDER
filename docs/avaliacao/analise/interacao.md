# Avaliação de Capacidade de interação

Esta página consolida as métricas de Capacidade de interação a partir das fichas anonimizadas `PA01`, `PB01`, `PB02` e `PB03`, das atas de sessão, dos CSV e das faixas da [Fase 2](../../fase2.md). As gravações de tela e áudio não são versionadas no repositório (diretório privado). O julgamento é **indicativo** (n = 4; um iniciante).

## 1. Fontes e decisões de consolidação

| Código | Sessão | Grupo | Evidência |
| --- | --- | --- | --- |
| PA01 | 14/11/2026, presencial, Windows 11 | A (iniciante): Etapas 1 a 3 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PA01_2026-11-14.md); [ata](../atas/sessao-PA01_2026-11-14.md) |
| PB01 | 13/11/2026, online, macOS | B (frequente): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB01_2026-11-13.md); [ata](../atas/sessao-PB01_2026-11-13.md) |
| PB02 | 13/11/2026, online, Windows 10 | B (frequente / piloto): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB02_2026-11-13.md); [ata](../atas/sessao-PB02_2026-11-13.md) |
| PB03 | 21/11/2026, online, Windows 10 | B (frequente): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB03_2026-11-21.md); [ata](../atas/sessao-PB03_2026-11-21.md) |

**Regras de roteiro**

1. O Grupo A (iniciantes) executa Etapas 1 a 3 e 5 (reconhecimento, aprendizagem e segunda passagem).
2. O Grupo B (frequentes) **não** executa Etapas 2 e 3: não necessita de roteiro adicional de aprendizagem. Executa Etapas 1, 4 e 5.
3. Em PB02, os tempos preenchidos na seção “Etapa 3” da ficha correspondem à **Etapa 4** (uso diário) e são consolidados como tal.
4. Em PB01, os tempos preenchidos na seção “Etapa 2” da ficha seguem a mesma lógica documental e são consolidados como **Etapa 4**.
5. PA01 é Grupo A (iniciante). Marcação “B” residual na ficha, se houver, trata-se de erro de digitação e foi corrigida.
6. **Entrevista piloto (PB02).** No escopo deste projeto da disciplina, a sessão piloto é considerada parte da avaliação geral resultante: além de linha de base de comparação entre usuários frequentes, seus dados entram nas métricas consolidadas, no julgamento das questões GQM e nas recomendações de melhoria.
7. Em PB03, a tarefa rotulada como B2 Revisar constou como **não coletada**; T<sub>ct</sub> e T<sub>exec</sub> usam as quatro tarefas com tempo registrado.

## 2. Cálculo das métricas

### PA01 (Grupo A)

| Métrica | Cálculo | Valor | Faixa |
| --- | --- | --- | --- |
| T<sub>rf</sub> | 1/6 (R2) | 16,7% | Insatisfatório |
| T<sub>aprend</sub> | total da ficha na Etapa 2 | 7 min 36 s (456,05 s) | Excelente |
| T<sub>sa</sub> | 4/4 na Etapa 3 sem ajuda | 100% | Excelente |
| T<sub>ct</sub> rodada 1 | 4/5 (A3 sem S) | 80% | Mínimo |
| T<sub>ct</sub> rodada 2 | 4/4 | 100% | Excelente |
| T<sub>exec</sub> mediana (rodada 1) | mediana dos tempos A1 a A5 | 50 s | Excelente |

### PB01, PB02 e PB03 (Grupo B, Etapa 4)

| Participante | T<sub>rf</sub> | Faixa | T<sub>ct</sub> Etapa 4 | T<sub>exec</sub> mediana | Faixa T<sub>exec</sub> |
| --- | --- | --- | --- | --- | --- |
| PB01 | 66,7% | Mínimo | 100% (excelente) | 39,31 s | Excelente |
| PB02 | 83,3% | Alvo | 100% (excelente) | 25 s | Excelente |
| PB03 | 66,7% | Mínimo | 100% (4/4 coletadas) | 27,285 s | Excelente |
| Agregado B | 72,2% (média T<sub>rf</sub>) | Mínimo | 100% | ~30,5 s | Excelente |

### Tempo por tarefa (T<sub>exec</sub>)

![Tempo por tarefa (T_exec): Grupo A (PA01) e Grupo B](../../assets/grafico_texec_tarefas_interacao.png)

Barras agrupadas com a faixa alvo de 2 a 5 min da Fase 2. Grupo A: PA01, rodada 1 (A1 a A5). Grupo B: tempos da Etapa 4 (ver `M-INT_tarefas.csv`, incluindo PB03). A figura publicada pode ainda refletir a média anterior de PB01 e PB02; os valores canônicos estão na tabela acima e no consolidado. Cópia também em `docs/avaliacao/dados/grafico_texec_tarefas_interacao.png`.

## 3. Respostas a Q1 a Q3 e hipóteses

| Questão | Evidência | Resposta indicativa |
| --- | --- | --- |
| **Q1** | T<sub>rf</sub> PA01 = 16,7% | **Não atendida** |
| **Q2** | T<sub>aprend</sub> e T<sub>sa</sub> excelentes em PA01 | **Atendida** (n = 1) |
| **Q3** | T<sub>ct</sub> 100% e T<sub>exec</sub> excelentes em PB01, PB02 e PB03 | **Atendida** no escopo da Etapa 4 (com ressalvas documentais) |

| Hipótese | Julgamento |
| --- | --- |
| **H1** | Rejeitada no iniciante (T<sub>rf</sub> 16,7%). PB02 só acertou R1 após três tentativas. PB03 errou R4 e R6 (vocabulário nota/cartão). |
| **H2** | Sustentada em PA01 para o roteiro de aprendizagem. |
| **H3** | Sustentada no agregado de frequentes (T<sub>ct</sub> e T<sub>exec</sub> em alvo/excelente), com ressalva do remapeamento documental em PB01/PB02 e da tarefa B2 não coletada em PB03. |

## 4. Evidência qualitativa

- PA01: falhou em localizar **Criar baralho**; sugeriu botões autoexplicativos.
- PB01: confundiu “nota” com “cartão”; pediu tutorial prático.
- PB02: descreveu **Criar baralho** como pouco intuitivo na parte inferior e sugeriu reposicioná-lo.
- PB03: botões da tela inicial claros; maior confusão em “nota”; pediu interface e termos menos técnicos.

## 5. Limitações

- Um iniciante na amostra de Q1 e Q2.
- Em PB01 e PB02, a Etapa 4 foi registrada em seções erradas da ficha (2 ou 3) e remapeada na consolidação.
- Em PB03, B2 Revisar não foi coletada.
- Julgamento **indicativo** (n = 4).
- PB02 é sessão piloto; sua inclusão na avaliação geral e como linha de base está explícita na regra 6 da seção 1, conforme orientação do feedback do [Ponto de Controle 2](../atas/feedback-PC2_2026-11-16.md).

## 6. Ação de melhoria

Prioridade: protótipo reposicionando **Criar baralho**, com validação T<sub>rf</sub>(R1) ≥ 75%. Ver [Fase 4](../../fase4.md).
