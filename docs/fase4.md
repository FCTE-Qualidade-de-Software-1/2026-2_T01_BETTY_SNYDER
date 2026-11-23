# Fase 4: Executar a avaliação e julgar

Esta página registra a obtenção dos dados, a organização dos arquivos no repositório, a análise GQM (Goal-Question-Metric: método que liga objetivos a perguntas e a medidas) frente às questões e hipóteses da [Fase 2](fase2.md), o julgamento frente ao propósito da [Fase 1](fase1.md), as relações entre características, as sugestões priorizadas e a ação de melhoria obrigatória. As análises detalhadas estão em [interacao.md](avaliacao/analise/interacao.md), [desempenho.md](avaliacao/analise/desempenho.md) e [flexibilidade.md](avaliacao/analise/flexibilidade.md).

## Organização dos dados

Os dados do **produto** (avaliação do Anki) ficam em [`avaliacao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao). Não confundir com [`gestao-psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/gestao-psm), que acompanha o projeto acadêmico (esforço e progresso da equipe).

```text
avaliacao/
  protocolos/     Como conduzir entrevistas e ensaios
  scripts/        Programas de coleta e consolidação
  dados/
    interacao/      {bruto, consolidado}  Capacidade de interação (facilidade de uso)
    desempenho/     {bruto, consolidado}  Eficiência de desempenho (tempo e recursos)
    flexibilidade/  {bruto, consolidado}  Flexibilidade (instalação, integração e migração)
  analise/        Interpretação das métricas frente ao GQM
```

**Rastreabilidade** (caminho do arquivo bruto até o número publicado): protocolo → dado bruto → consolidado → análise e esta Fase 4. Nomes preferenciais: `<métrica>_<cenário>_<execução>` (exemplo: `T_ini_coldstart_ubuntu_01.csv`). Exceção: `sessoes.csv` indexa entrevistas (data, formato e ata), sem apontar mídia.

| Frente | Bruto principal | Consolidado / análise |
| --- | --- | --- |
| Capacidade de interação | [`M-INT-01_reconhecimento.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/M-INT-01_reconhecimento.csv), [`M-INT_tarefas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/M-INT_tarefas.csv), [`Entrevistas/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/interacao/bruto/Entrevistas), [`sessoes.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/sessoes.csv) | [`M-INT_metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/consolidado/M-INT_metricas.csv); [análise](avaliacao/analise/interacao.md) |
| Eficiência de desempenho | CSV em `docs/avaliacao/dados/desempenho/bruto/` (espelho usado na GitPage); canônico previsto em `avaliacao/dados/desempenho/` | [análise de desempenho](avaliacao/analise/desempenho.md) |
| Flexibilidade | Consolidados de instalação, checklist e migração em [`flexibilidade/consolidado/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/flexibilidade/consolidado) | [análise de Flexibilidade](avaliacao/analise/flexibilidade.md) |

**Participantes.** Códigos públicos: PA01 (Grupo A, iniciante); PB01, PB02 (piloto) e PB03 (Grupo B, frequentes). A tabela código → pessoa e os termos de consentimento ficam fora do repositório. Gravações de tela e áudio não são versionadas; a evidência pública da sessão são as atas, as fichas anonimizadas e `sessoes.csv`.

## Visão geral da coleta

| Frente | Dados brutos | Métricas e análise | Situação objetiva |
| --- | --- | --- | --- |
| Capacidade de interação | [`Entrevistas/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/interacao/bruto/Entrevistas) (PA01, PB01, PB02, PB03), atas, CSV `M-INT-*` | [`M-INT_metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/consolidado/M-INT_metricas.csv); [análise](avaliacao/analise/interacao.md) | Quatro participantes; um iniciante (PA01); três frequentes (PB02 piloto); métricas T<sub>rf</sub>, T<sub>aprend</sub>, T<sub>sa</sub>, T<sub>ct</sub> e T<sub>exec</sub> calculadas |
| Eficiência de desempenho | CSV e gráficos em `docs/avaliacao/dados/desempenho/bruto/` e `docs/avaliacao/dados/` | [análise de desempenho](avaliacao/analise/desempenho.md) | Triangulação concluída em Ubuntu, Windows 11 e macOS; limitações específicas da API do Windows NT documentadas como variação controlada de plataforma |
| Flexibilidade | [`flexibilidade-instalacao-tempo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-instalacao-tempo.csv), [`flexibilidade-checklist-registro.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-checklist-registro.csv), [`flexibilidade-migracao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-migracao.csv), gráficos de instalação e checklist | [análise de Flexibilidade](avaliacao/analise/flexibilidade.md); seção abaixo | Q1 e Q2 no alvo/excelente; Q3 com T<sub>pd</sub> = 100% e T<sub>sub</sub> na faixa mínimo |

---

## Capacidade de interação

### Coleta e notas de cálculo

Quatro sessões com consentimento (TCLE, o Termo de Consentimento Livre e Esclarecido). A evidência pública no repositório são as fichas anonimizadas e as atas; as gravações de tela e áudio permanecem em diretório privado.

| Código | Data | Modalidade / SO | Grupo e etapas | Evidência |
| --- | --- | --- | --- | --- |
| PA01 | 14/11/2026 | Presencial, Windows 11 | A (iniciante): Etapas 1 a 3 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PA01_2026-11-14.md); [ata](avaliacao/atas/sessao-PA01_2026-11-14.md) |
| PB01 | 13/11/2026 | Online, macOS | B (frequente): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB01_2026-11-13.md); [ata](avaliacao/atas/sessao-PB01_2026-11-13.md) |
| PB02 | 13/11/2026 | Online, Windows 10 | B (frequente / piloto): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB02_2026-11-13.md); [ata](avaliacao/atas/sessao-PB02_2026-11-13.md) |
| PB03 | 21/11/2026 | Online, Windows 10 | B (frequente): Etapas 1, 4 e 5 | [ficha](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/Entrevistas/PB03_2026-11-21.md); [ata](avaliacao/atas/sessao-PB03_2026-11-21.md) |

**Notas de cálculo.** O Grupo A executa Etapas 1 a 3 e 5. O Grupo B não executa Etapas 2 e 3. Em PB01, os tempos da seção Etapa 2 da ficha foram contabilizados como Etapa 4. Em PB02, os tempos da seção Etapa 3 foram contabilizados como Etapa 4. Em PB03, quatro tarefas da Etapa 4 têm tempo; B2 Revisar não foi coletada. A sessão **PB02** (piloto) permanece na avaliação geral como linha de base e dado consolidado. Detalhe em [interacao.md](avaliacao/analise/interacao.md).

### Resultados

| Métrica | PA01 | Faixa | PB01 | Faixa | PB02 | Faixa | PB03 | Faixa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T<sub>rf</sub> | 16,7% (1/6) | Insatisfatório | 66,7% | Mínimo | 83,3% | Alvo | 66,7% | Mínimo |
| T<sub>aprend</sub> | 7 min 36 s (456,05 s) | Excelente | n/a | - | n/a | - | n/a | - |
| T<sub>sa</sub> | 100% (4/4 sem ajuda) | Excelente | n/a | - | n/a | - | n/a | - |
| T<sub>ct</sub> | 80% → 100% (rodadas 1-2) | Mínimo → Excelente | 100% (Etapa 4) | Excelente | 100% (Etapa 4) | Excelente | 100% (4/4) | Excelente |
| T<sub>exec</sub> mediana | 50 s | Excelente | 39,31 s | Excelente | 25 s | Excelente | 27,285 s | Excelente |

**Agregados do Grupo B.** Média de T<sub>rf</sub> = 72,2% (faixa mínimo). T<sub>ct</sub> = 100% nos três frequentes. Mediana aproximada de T<sub>exec</sub> ≈ 30,5 s (faixa excelente).

![Tempo por tarefa (T_exec): Grupo A (PA01) e Grupo B, com faixa alvo de 2 a 5 min](assets/grafico_texec_tarefas_interacao.png)

*Figura. Tempo por tarefa alinhado semanticamente. Grupo A: PA01, rodada 1. Grupo B: Etapa 4 (fonte canônica `M-INT_tarefas.csv`, com PB03). A figura pode ainda mostrar a média anterior só de PB01 e PB02. A faixa sombreada é o alvo da Fase 2 (2 a 5 min).*

### Análise

| Questão | Evidência | Resposta |
| --- | --- | --- |
| **Q1** (reconhecibilidade) | T<sub>rf</sub> de PA01 = 16,7%, abaixo de 75% (alvo) | Não atendida |
| **Q2** (aprendizagem) | T<sub>aprend</sub> = 7 min 36 s e T<sub>sa</sub> = 100% em PA01, ambos na faixa excelente | Atendida em PA01 (n = 1 iniciante) |
| **Q3** (operabilidade) | T<sub>ct</sub> = 100% e T<sub>exec</sub> mediana &lt; 2 min em PB01, PB02 e PB03 | Atendida no escopo da Etapa 4 (com ressalvas) |

| Hipótese | Julgamento |
| --- | --- |
| **H1** | Rejeitada no iniciante (T<sub>rf</sub> 16,7%). PB02 só acertou R1 após três tentativas. PB03 errou R4 e R6. |
| **H2** | Sustentada em PA01 para o roteiro de aprendizagem. |
| **H3** | Sustentada no agregado de frequentes (T<sub>ct</sub> e T<sub>exec</sub> em alvo ou excelente), com remapeamento documental em PB01/PB02 e B2 não coletada em PB03. |

**Evidência qualitativa (Etapa 5).** PA01 falhou em localizar “Criar baralho” e pediu botões autoexplicativos. PB01 confundiu “nota” com “cartão” e pediu tutorial prático. PB02 descreveu “Criar baralho” como pouco intuitivo na parte inferior. PB03 apontou clareza dos botões iniciais, confusão em “nota” e desejo de interface e termos menos técnicos.

**Limitações.** Amostra de quatro participantes, com um único iniciante para Q1 e Q2. Em PB01/PB02, a Etapa 4 foi remapeada a partir de seções erradas da ficha. Em PB03, B2 Revisar não foi coletada. O julgamento preserva a ênfase 5 da Fase 1.

---

## Eficiência de desempenho

### Coleta

A Dupla B instrumentou o Anki Desktop 26.09.3 em três máquinas de referência ([Ambiente](avaliacao/protocolos/ambiente.md)):

| Avaliador | SO | Arquitetura | Hardware |
| --- | --- | --- | --- |
| Mateus de Siqueira | Ubuntu 24.04 LTS | x86_64 | Intel Core i7-1185G7, 8 GB RAM |
| Karolina Vieira | Windows 11 | x86_64 | Intel Core i7-1165G7, 16 GB RAM |
| Davi Severiano | macOS Sequoia | ARM64 | Apple Silicon M4, 16 GB unificada |

Os CSV e gráficos usados nesta página estão em `docs/avaliacao/dados/desempenho/bruto/` e `docs/avaliacao/dados/` (gráficos de threads). O diretório canônico `avaliacao/dados/desempenho/` contém apenas README e `.gitkeep` nesta entrega.

**Ressalvas de medição.** No Windows e no macOS, o cold start registrado é o tempo de criação do processo (*launcher*), não o tempo até a interface pronta (TTI, tempo até a tela ficar utilizável); no Ubuntu, o coletor mediu até a ativação dos subprocessos QtWebEngine (TTI ≈ 1,018 s). A RAM do Windows (73,40 MB em repouso; 26,35 MB no estresse) enumera só o processo pai, sem a árvore de renderizadores. T<sub>sinc</sub> foi retirado dos ensaios de laboratório (risco de *rate limit* no AnkiWeb e dependência de rede externa); a sincronização permanece nas entrevistas (Capacidade de interação) e no cenário M2 de migração (Flexibilidade).

### Resultados

Valores tomados de [desempenho.md](avaliacao/analise/desempenho.md). As faixas abaixo seguem a Tabela VIII da [Fase 2](fase2.md), salvo quando a análise de desempenho registra enquadramento próprio e isso é indicado no texto.

| Métrica | Ubuntu 24.04 | Windows 11 | macOS Sequoia | Enquadramento |
| --- | --- | --- | --- | --- |
| Cold start (Q1) | 1,018 s (TTI) | 0,152 s (*launcher*) | 0,021 s (*launcher*) | Excelente (&lt; 3 s) nos três |
| CPU em repouso (Q2) | 0,04% | 0,00% | 0,10% | Excelente |
| RAM em repouso (Q2) | 783,89 MB | 73,40 MB (só processo pai) | 950,77 MB | Insatisfatório em Ubuntu e macOS (≥ 400 MB; QtWebEngine) |
| Threads em repouso | 56 (6 filhos) | 13–16 (1 filho) | 85–88 (5 filhos) | Contagem observada |
| RAM pico 100k cards (Q2) | 1.328,13 MB (1,33 GB) | 26,35 MB (*stub*) | 1.512,06 MB (1,51 GB) | Insatisfatório em Ubuntu e macOS (≥ 800 MB) |
| CPU pico sob carga (Q2) | 100,6% (1 núcleo) | 98,4% (1 núcleo) | 100,8% (1 núcleo) | Um núcleo saturado; demais livres |
| Main thread sob estresse (Q4) | 2,35% | 98,44% (TID #0) | 1,30% | Excelente em Ubuntu e macOS; Windows: limitação controlada da API NT |
| Vazão Check Database 100k (Q3) | ≈ 2.000.000 cards/min (~3 s) | Ação manual sem timer | ≈ 3.000.000 cards/min (~2 s) | Excelente em Ubuntu e macOS |

### Análise

| Questão / hipótese | Evidência | Julgamento |
| --- | --- | --- |
| **Q1 / H1** (comportamento no tempo) | Cold start &lt; 1,5 s em todos os SOs; T<sub>sinc</sub> fora do laboratório | H1 confirmada para cold start (faixa excelente). T<sub>sinc</sub> não julgado nestes ensaios. |
| **Q2 / H2** (CPU) | CPU em repouso ≤ 0,10% | H2 para CPU superada (faixa excelente; abaixo do alvo 2–5% previsto). |
| **Q2 / H2** (RAM) | 783,89 MB e 950,77 MB em repouso; 1,33 GB e 1,51 GB sob 100k cards | H2 para RAM refutada: faixa insatisfatório (Tabela VIII: ≥ 400 MB repouso / ≥ 800 MB estresse). Pegada do QtWebEngine/Chromium e índices SQLite sob 100k cards. |
| **Q3 / H3** (capacidade e vazão) | Check Database em ~2–3 s; vazão ≫ 15.000 cards/min | H3 confirmada e superada (faixa excelente). |
| **Q4 / H4** (threads / UI) | Main thread 2,35% (Ubuntu) e 1,30% (macOS); Windows 98,44% no TID #0 | H4 confirmada em Unix (faixa excelente). No Windows, o pico no índice #0 é registrado como limitação controlada da API NT (ausência de garantia de ordem cronológica em `proc.threads()`). |

**Limitação controlada de plataforma (Windows 11).** A triangulação multiplataforma — destacada positivamente no [feedback do PC2](avaliacao/atas/feedback-PC2_2026-11-16.md) — evidencia que, sem privilégios elevados no Windows NT, a biblioteca `psutil` isola apenas o processo raiz (`anki.exe`, omitindo os renderizadores `QtWebEngineProcess`) e não garante que o índice `#0` de `proc.threads()` corresponda à thread de interface gráfica. Da mesma forma, o disparo de *cold start* no Windows e no macOS registra o *process creation time* (*launcher*), enquanto no Ubuntu registra o *Time-to-Interactive* completo (1,018 s). Por rigor metodológico, o julgamento quantitativo comparável 1:1 de Q2 (árvore completa de RAM), Q3 (vazão cronometrada) e Q4 (isolamento determinístico de *Main Thread*) adota Ubuntu 24.04 e macOS Sequoia como linha de base primária, preservando os registros brutos do Windows 11 para transparência da avaliação.

---

## Flexibilidade

Detalhamento: [análise de Flexibilidade](avaliacao/analise/flexibilidade.md).

### Coleta (F4-C1 / F4-C2)

Os protocolos de [instalação](avaliacao/protocolos/flexibilidade-instalacao.md), [checklist](avaliacao/protocolos/flexibilidade-checklist.md) e [migração](avaliacao/protocolos/flexibilidade-migracao.md) preveem, em laboratório (Dupla C), as métricas T<sub>inst</sub>, T<sub>inst_t</sub>, N<sub>int</sub>, P<sub>int</sub>, T<sub>pd</sub> e T<sub>sub</sub> nas máquinas de referência Windows, macOS e Ubuntu ([Ambiente](avaliacao/protocolos/ambiente.md)).

Publicados em [`avaliacao/dados/flexibilidade/consolidado/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/flexibilidade/consolidado): tempos de instalação, checklist de integração (P<sub>int</sub>), migração M1/M2 (T<sub>pd</sub>, T<sub>sub</sub>) e dois gráficos. A pasta `bruto/` ainda não espelha os arquivos `diff_m*_rep*.csv` citados no consolidado.

### Resultados (Q1, Q2 e Q3)

Fontes: [`flexibilidade-instalacao-tempo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-instalacao-tempo.csv), [`flexibilidade-checklist-registro.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-checklist-registro.csv) e [`flexibilidade-migracao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/flexibilidade/consolidado/flexibilidade-migracao.csv). Faixas da Tabela XI da [Fase 2](fase2.md).

| Sistema | T<sub>inst</sub> | T<sub>inst_t</sub> | N<sub>int</sub> | Faixas (T<sub>inst</sub> / T<sub>inst_t</sub> / N<sub>int</sub>) | P<sub>int</sub> | Faixa P<sub>int</sub> |
| --- | --- | --- | --- | --- | --- | --- |
| Windows 11 | 100% (1/1) | 3,82 min | 0 | Alvo / alvo / excelente | 10/10 | Excelente |
| macOS 27 (ARM) | 100% (1/1) | 0,55 min | 0 | Excelente / excelente / excelente | 10/10 | Excelente |
| Ubuntu 26.04.1 | 100% (1/1) | 0,97 min | 0 | Excelente / excelente / excelente | 10/10 | Excelente |

![Tempo de instalação nos três sistemas operacionais](assets/grafico_flexibilidade_tempo_instalacao_3so.png)

*Figura. Tempo de instalação (T<sub>inst_t</sub>) em Windows, macOS e Ubuntu.*

![Checklist de integração (P_int) nos três sistemas](assets/grafico-flexibilidade-checklist.png)

*Figura. Pontuação do checklist de integração (P<sub>int</sub>) por sistema operacional.*

**Migração (Q3).** Seis ensaios em 20/11/2026 (M1 `.apkg` e M2 AnkiWeb, três pares de SO cada): T<sub>pd</sub> = 100% (0 diferenças em 10.000 cartões; sem intervenção); T<sub>sub</sub> entre 2,33 e 2,66 min (média 2,51 min), faixa **mínimo**. Detalhamento: [análise de Flexibilidade](avaliacao/analise/flexibilidade.md).

**Qualitativos (Parte C das entrevistas; complementam o laboratório).**

| Participante | Relato sobre instalação |
| --- | --- |
| PB01 (macOS) | Instalação “tranquila”; precisou autorizar a abertura do aplicativo baixado da internet (Gatekeeper). |
| PB02 (Windows) | Instalação “tranquila” e “intuitiva”; sem passo além do instalador. |
| PB03 (Windows) | Instalação “um pouco confusa” no site (extensões externas); precisou de passo além do instalador. |
| PA01 (Grupo A) | Anki já instalado pela equipe antes da sessão; perguntas de instalabilidade do Grupo B marcadas N/A. |

### Análise (F4-C3)

| Questão / hipótese (Fase 2) | Situação nesta página |
| --- | --- |
| **Q1 / H1** (instalabilidade) | Atendida nos três sistemas (T<sub>inst</sub> e T<sub>inst_t</sub> no alvo ou excelente; N<sub>int</sub> = 0). H1 parcial: no Ubuntu o tempo ficou abaixo de 2 min e sem intervenção, diferente da expectativa de 2 a 5 min com intervenção. |
| **Q2 / H2** (adaptabilidade) | Atendida: P<sub>int</sub> = 10/10 nos três sistemas (faixa excelente). |
| **Q3 / H3** (substituibilidade) | T<sub>pd</sub> = 100% (preservação confirmada); T<sub>sub</sub> média 2,51 min (faixa mínimo). Q3 não atendida no alvo. H3 parcial: preservação sim; tempo &lt; 1 min não. |
| **Objetivo G (Flexibilidade)** | Q1 e Q2 atendidas; Q3 com evidência completa na faixa mínimo (tempo de migração). |

Arquivos opcionais remanescentes: espelhar `diff_m*_rep*.csv` em `avaliacao/dados/flexibilidade/bruto/migracao/`.

---

## Coerência com o propósito da Fase 1 (F4-C4)

O [propósito da avaliação](fase1.md#propósito-da-avaliação-e-uso-pretendido) é **indicar pontos de melhoria** no Anki, sob o ponto de vista do estudante, para a requisitante (professora), com recomendações priorizadas para mantenedores e estudantes.

| Expectativa da Fase 1 | Resultado da Fase 4 | Atende? |
| --- | --- | --- |
| Identificar barreiras de uso na interface (ênfase 5) | Q1 de Capacidade de interação não atendida (T<sub>rf</sub> do iniciante 16,7%); Q2 e Q3 atendidas no escopo amostral | Sim, com limitação de n = 4 (1 iniciante) |
| Informar comportamento de desempenho em estudo prolongado | Cold start e vazão excelentes; RAM na faixa mínimo; Windows parcial | Parcial |
| Informar instalabilidade e migração entre SO | Instalação, checklist e migração publicados; T<sub>sub</sub> na faixa mínimo | Sim, com ressalva de tempo de migração acima de 1 min |
| Fundamentar uma ação de melhoria | Protótipo de alta fidelidade para “Criar baralho” | Sim |

O julgamento cumpre o uso pretendido na característica priorizada (Capacidade de interação), cobre instalabilidade, adaptabilidade e migração com dados de laboratório, e deixa explícitas a faixa mínimo de T<sub>sub</sub> e a incompletude de desempenho no Windows.

## Relações entre características (Premissa 1)

- **Capacidade de interação × Eficiência de desempenho.** Falhas de reconhecibilidade (T<sub>rf</sub> de PA01 = 16,7%; R1 falhou) elevam o esforço cognitivo na primeira sessão, mesmo com cold start e vazão de banco na faixa excelente. Evidência: [interacao.md](avaliacao/analise/interacao.md) e [desempenho.md](avaliacao/analise/desempenho.md).
- **Eficiência de desempenho × uso em notebook.** RAM em repouso na faixa mínimo (≈ 780–950 MB em Ubuntu e macOS) e picos de 1,33–1,51 GB sob 100k cards podem afetar a fluidez percebida em máquinas de 8 GB (perfil Ubuntu da avaliação). Limitação: RAM do Windows ainda incompleta (só processo pai).
- **Flexibilidade × Capacidade de interação.** Com T<sub>inst_t</sub> excelente ou alvo e N<sub>int</sub> = 0 nos três sistemas, a barreira de primeiro uso observada nas entrevistas concentra-se na interface (vocabulário e “Criar baralho”), não no tempo de instalação em laboratório. A migração preserva 100% dos dados, mas leva em média 2,51 min (faixa mínimo), o que ainda pode somar esforço no primeiro uso ao trocar de máquina. Evidência: [flexibilidade.md](avaliacao/analise/flexibilidade.md).

Onde os dados não permitem relação: afirmação causal entre o tempo de migração M1/M2 e T<sub>exec</sub> das sessões de entrevista (amostras e contextos distintos).

## Sugestões priorizadas (F4-C5)

| Prioridade | Sugestão (ação concreta) | Base |
| --- | --- | --- |
| 1 | Destacar **Criar baralho** na tela inicial (lista de baralhos como home) | T<sub>rf</sub> R1; PA01 e PB02 |
| 2 | Incluir glossário ou tooltips para nota, tipo de nota e cartão | Q1; respostas da Etapa 5 |
| 3 | Revisar footprint de memória do QtWebEngine sob coleções grandes | RAM na faixa mínimo (Ubuntu 1,33 GB; macOS 1,51 GB com 100k cards) |
| 4 | Reduzir o tempo de migração (T<sub>sub</sub> hoje ≈ 2,5 min) e fechar itens “refazer” no Windows | Q3 na faixa mínimo; desempenho parcial no Windows |

## Ação de melhoria

**Problema.** “Criar baralho” não é reconhecido de imediato (T<sub>rf</sub> do iniciante 16,7%; PB02 só após três tentativas).

**Justificativa.** Prioridade 1 da tabela acima; ênfase 5 da Fase 1; evidência direta de Q1/H1.

**Ação.** Protótipo de alta fidelidade com a lista de baralhos como tela inicial e destaque para **Criar Baralho**, além de tutorial introdutório guiado. Artefato: [Protótipo da ação de melhoria](prototipo-acao-melhoria.md) ([abrir interativo](prototipo-interativo/index.html)).

**Validação proposta.** Nova sessão com iniciante: R1 correto e T<sub>rf</sub> ≥ 75% (alvo), ou localização espontânea em no máximo 10 s sem ajuda.

**O que a ação não cobre.** Não reduz T<sub>sub</sub> da migração (Q3 de Flexibilidade) nem fecha as medições de desempenho no Windows.
