# Fase 2 — Especificar a avaliação

Esta página reproduz a Seção IV do [artigo da Entrega 1](artigo.md), entregue em 26/10/2026.

> As referências entre colchetes seguem a numeração do [artigo](artigo.md#referencias).


Esta seção especifica a avaliação por meio do GQM [4]. Para cada característica priorizada na Fase 1, apresentam-se o objetivo de medição, as questões e hipóteses, os fatores de variação, as métricas e os níveis de pontuação com os critérios de julgamento. Os níveis seguem quatro faixas comuns às três características: *insatisfatório*, *mínimo*, *alvo* e *excelente*. O [Diagrama GQM](#diagrama-gqm) reúne a hierarquia completa, e a seção [Coerência entre as Fases 1 e 2](#coerencia-entre-as-fases-1-e-2) explicita a ligação entre as fases.

## Capacidade de Interação

A equipe selecionou três subcaracterísticas: **reconhecibilidade da adequação**, porque o Anki usa conceitos próprios (nota, tipo de nota, card e baralho) e o estudante precisa perceber quais funções atendem ao que quer fazer; **facilidade de aprendizado**, porque a Fase 1 definiu o uso sem treinamento nem suporte; e **operabilidade**, porque quem já usa o Anki repete as mesmas tarefas diariamente. Os testes envolvem dois grupos definidos por triagem (ver [Grupos de participantes e triagem](#grupos-de-participantes-e-triagem)): iniciantes (Grupo A), que respondem principalmente a Q1 e Q2, e usuários frequentes (Grupo B), que respondem a Q3 e servem de comparação em H3.

### Objetivo de Medição

O objetivo G1 segue o template do GQM [4] e as decisões comuns da equipe. O propósito de entender o produto serve para identificar pontos de melhoria, conforme o objetivo da avaliação definido na Fase 1.

| Template GQM | G1 — Capacidade de interação |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 e o fluxo de criação de conta, login e sincronização do AnkiWeb |
| **para o propósito de** | entender, identificando pontos de melhoria |
| **com respeito a** | reconhecibilidade da adequação, facilidade de aprendizado e operabilidade |
| **do ponto de vista do** | estudante, usuário final (iniciante e usuário frequente) |
| **no contexto de** | uso individual em computador pessoal, sem treinamento formal |

### Grupos de participantes e triagem

**Grupo A — Usuários iniciantes.** Participantes que nunca utilizaram o Anki antes do estudo. Não devem ter experiência prática anterior com as tarefas avaliadas no Anki Desktop ou no AnkiWeb. O uso de outros aplicativos de flashcards é registrado separadamente, pois pode influenciar a aprendizagem.

**Grupo B — Usuários frequentes.** Participantes que utilizaram o Anki regularmente durante as últimas quatro semanas, preferencialmente em pelo menos três dias por semana, e que já realizaram as tarefas centrais avaliadas: criar baralhos e cartões, revisar cartões e sincronizar com o AnkiWeb.

Antes da entrevista ou do preenchimento do formulário de avaliação, a pessoa responde ao formulário de triagem: (1) já utilizou o Anki (nunca / experimentou uma ou duas vezes / já utilizou regularmente); (2) nos últimos 7 dias, em quantos dias utilizou (nenhum / 1–2 / 3–4 / 5–7); (3) há quanto tempo utiliza regularmente (nunca / menos de 4 semanas / 4 semanas a 3 meses / mais de 3 meses); (4)–(6) já criou baralhos e cartões, já revisou e já sincronizou Desktop–AnkiWeb (sim/não); (7) já utilizou outros aplicativos de flashcards (sim/não); (8) familiaridade geral com informática (baixa/média/alta). A classificação no Grupo A ou B segue essas respostas.

### Questões e Hipóteses

*Tabela III. Questões e hipóteses de Capacidade de interação*

| Questão | Hipótese |
|---|---|
| **Q1** (Reconhecibilidade da adequação): um estudante que nunca usou o Anki consegue identificar, pela interface, quais funções usar para criar seus cards e estudar? | **H1:** no Grupo A, T<sub>rf</sub> das funções principais (criar baralho, adicionar cards e estudar) fica em *alvo* ou *excelente*; nota, tipo de nota e card ficam em *mínimo* ou *insatisfatório*. |
| **Q2** (Facilidade de aprendizado): um estudante iniciante consegue aprender, sem ajuda, a criar uma conta no AnkiWeb, criar um baralho, adicionar cards, revisá-los e sincronizar a coleção? | **H2:** no Grupo A, T<sub>sa</sub> e T<sub>aprend</sub> em baralho, cards e revisão ficam em *alvo* ou *excelente*; conta e primeira sincronização ficam em *mínimo* ou *insatisfatório*. |
| **Q3** (Operabilidade): as tarefas do estudo diário podem ser executadas com pouco esforço por quem já usa o Anki? | **H3:** no Grupo B, T<sub>ct</sub> e T<sub>exec</sub> em revisar e adicionar cards ficam em *alvo* ou *excelente*; a diferença \|Δ\| entre Grupos A e B (médias de T<sub>ct</sub> e T<sub>exec</sub>) é maior em conta e sincronização do que em revisar e adicionar cards. |

### Fatores de Variação

Três fatores, obtidos na triagem e no perfil, podem influenciar os resultados: **familiaridade com informática** (ordinal: baixa, média ou alta) afeta H2 e H3 via tempos e ajudas em conta e sincronização; **experiência prévia com aplicativos de flashcards** (nominal) afeta H1 (reconhecimento de funções); e **sistema operacional** (nominal) afeta H2 e H3 via T<sub>exec</sub>.

### Métricas

A Tabela IV resume as cinco métricas do escopo (Plano de Medição, Aula 08). Todas são de escala de razão e coletadas em sessões observadas com consentimento registrado, nas tarefas da Fase 1 (criar baralho, adicionar cards, revisar, criar conta no AnkiWeb, login e sincronizar). Cada métrica indica a referência acadêmica de origem; T<sub>rf</sub> tem operacionalização própria, relacionada à referência citada.

*Tabela IV. Métricas de Capacidade de interação: definição, cálculo, referência e interpretação*

| Métrica | Q | Definição / cálculo | Referência de origem | Interpretação |
|---|:---:|---|---|---|
| Taxa de reconhecimento de funções (T<sub>rf</sub>) | Q1 | Porcentagem de iniciantes que indicam a função correta; N<sub>reconh.</sub> / N<sub>part.</sub> × 100% (operacionalização própria) | Adaptada de Sellier et al. [12] | Maior é melhor; 0–100% |
| Tempo de aprendizagem (T<sub>aprend</sub>) | Q2 | Média do tempo total do Grupo A no roteiro completo | Vogel et al. [13] | Menor é melhor; > 0 min |
| Taxa de sucesso após aprendizagem (T<sub>sa</sub>) | Q2 | Tentativas concluídas com sucesso ÷ tentativas realizadas × 100% | Bird et al. [14] | Maior é melhor; 0–100% |
| Taxa de conclusão de tarefas (T<sub>ct</sub>) | Q3 | Porcentagem de tarefas concluídas por grupo; N<sub>concluídas</sub> / N<sub>propostas</sub> × 100% | Bird et al. [14] | Maior é melhor; 0–100% |
| Tempo de execução da tarefa (T<sub>exec</sub>) | Q3 | Média do tempo da pessoa do recebimento da tarefa até o sucesso (também mediana), por tarefa e grupo | Bird et al. [14] | Menor é melhor; > 0 min |

### Níveis de Pontuação e Critérios de Julgamento

Os níveis da Tabela V foram fixados antes da coleta. Os limites de T<sub>exec</sub> medem o tempo da pessoa para concluir a tarefa e foram definidos por acordo da equipe (os limiares de 3, 9 e 12 s de Hoxmeier e DiCesare [11] aplicam-se ao tempo de resposta do sistema na Eficiência de desempenho, não a estas tarefas). Os demais limites também foram definidos por acordo da equipe, por falta de dados históricos do Anki.

*Tabela V. Níveis de pontuação das métricas de Capacidade de interação*

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| T<sub>rf</sub> (Q1) | T<sub>rf</sub> < 60% | 60% ≤ T<sub>rf</sub> < 75% | 75% ≤ T<sub>rf</sub> < 90% | T<sub>rf</sub> ≥ 90% |
| T<sub>aprend</sub> (Q2) | t > 40 min ou abandono | 25 ≤ t ≤ 40 min | 15 ≤ t < 25 min | t < 15 min |
| T<sub>sa</sub> (Q2) | T<sub>sa</sub> < 60% ou intervenção recorrente | 60% ≤ T<sub>sa</sub> < 75% | 75% ≤ T<sub>sa</sub> < 90% sem ajuda, ou T<sub>sa</sub> ≥ 90% com uma ajuda | T<sub>sa</sub> ≥ 90% sem ajuda |
| T<sub>ct</sub>, frequentes (Q3) | T<sub>ct</sub> < 80% ou abandono | 80% ≤ T<sub>ct</sub> < 90%, ou 100% com uma ajuda | 90% ≤ T<sub>ct</sub> < 100% sem ajuda | 100% sem ajuda |
| T<sub>exec</sub> (Q3) | t > 10 min ou falha | 5 ≤ t ≤ 10 min | 2 ≤ t < 5 min | t < 2 min |

**Regra de julgamento.** O julgamento procede de baixo para cima [4]: cada métrica é classificada em uma faixa, as faixas são agregadas por questão e as questões respondem ao G1. Uma questão é atendida quando suas métricas essenciais (T<sub>rf</sub> em Q1; T<sub>sa</sub> e T<sub>aprend</sub> em Q2; T<sub>ct</sub> e T<sub>exec</sub> em Q3) estão no alvo ou acima; havendo divergência, prevalece a faixa mais baixa. H1–H3 são julgadas pelos valores esperados da Tabela III. Os fatores de variação não alteram os limites, mas são reportados na interpretação. As faixas mínimo e insatisfatório tornam-se recomendações priorizadas, e a mais relevante alimenta a ação de melhoria da Entrega 2.

## Eficiência de Desempenho

A equipe avalia as três subcaracterísticas de Eficiência de Desempenho da ISO/IEC 25010:2023: **comportamento no tempo**, para verificar a prontidão do aplicativo nas tarefas de estudo; **utilização de recursos**, para mensurar a pegada de CPU e memória em computadores pessoais modestos; e **capacidade**, para avaliar a estabilidade do sistema sob coleções volumosas (até 100 mil cards). A investigação da arquitetura concorrente (Q4) desdobra simultaneamente comportamento no tempo e utilização de recursos, analisando se o isolamento de tarefas intensivas no backend em Rust evita a degradação da interface gráfica em PyQt.

### Objetivo de Medição

O objetivo G2 segue o template do GQM [4] e as decisões comuns da equipe. O propósito de entender o produto serve para identificar pontos de melhoria, conforme o objetivo da avaliação definido na Fase 1:

| Template GQM | G2 — Eficiência de desempenho |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 e o fluxo de conta, login e sincronização do AnkiWeb |
| **para o propósito de** | entender |
| **com respeito a** | comportamento no tempo, utilização de recursos e capacidade |
| **do ponto de vista do** | estudante, usuário final (operador) |
| **no contexto de** | uso individual em computador pessoal com Windows, macOS ou Ubuntu |

### Questões e Hipóteses

As quatro questões e suas respectivas hipóteses de baseline constam na Tabela VI. As hipóteses expressam as expectativas quantitativas da equipe fundamentadas nas faixas de pontuação preestabelecidas.

*Tabela VI. Questões e hipóteses de Eficiência de desempenho*

| Questão | Hipótese |
|---|---|
| **Q1** (Comportamento no tempo): quais ações do estudante no Anki Desktop demandam maior tempo de resposta: inicialização, abertura da revisão, carregamento da coleção ou sincronização? | **H1:** o tempo de sincronização situa-se na faixa *alvo* (3 ≤ t < 9 s) devido à latência de rede; o tempo de inicialização (*cold start*) e o tempo para iniciar a revisão situam-se na faixa *excelente* (t < 3 s). |
| **Q2** (Utilização de recursos): como o consumo médio e de pico de CPU e de memória RAM varia entre o cenário de repouso e o cenário de estresse operacional? | **H2:** em repouso, o uso médio de CPU fica entre 2% e 5% e a RAM entre 150 e 250 MB (*alvo*); sob estresse operacional, o pico de CPU fica entre 40% e 70% e a RAM estabiliza-se entre 350 e 500 MB (*alvo*). |
| **Q3** (Capacidade): qual o impacto do aumento volumétrico da coleção (10k, 50k e 100k cards) sobre o tempo de processamento e a vazão do banco de dados SQLite? | **H3:** com 100 mil cards, a degradação temporal do carregamento situa-se entre 15% e 35% (*alvo*), com tempo total inferior a 9 s e vazão superior a 15.000 cards/min na verificação do banco. |
| **Q4** (Comportamento concorrente): durante operações intensivas de banco e sincronização, as *Worker Threads* em Rust isolam o processamento pesado sem reter a *Main Thread* (UI Qt)? | **H4:** as *Worker Threads* absorvem a sobrecarga de I/O, limitando o consumo de CPU da *Main Thread* entre 15% e 35% (*alvo*), com preempções involuntárias (`nvcswch/s`) < 10 e sem congelamento perceptível da interface gráfica. |

### Fatores de Variação

Antes da execução dos testes, registram-se as condições de controle: todas as aplicações concorrentes e navegadores devem ser encerrados, mantendo apenas os serviços essenciais do sistema operacional. Os fatores de variação identificados e seu mapeamento de impacto são:

- **Configuração de Hardware (CPU, núcleos e tipo de disco SSD/HDD):** afeta diretamente H1 (tempos de leitura), H2 (picos de CPU) e H3 (I/O do banco de dados).
- **Sistema Operacional e Servidor Gráfico (Windows 11, macOS, Ubuntu com X11 ou Wayland):** afeta H2 e H4 devido às diferenças no gerenciamento de memória do PyQt e escalonamento de threads [7].
- **Latência e Largura de Banda da Conexão:** afeta estritamente a sincronização em H1.
- **Volume da Coleção de Cards (10k, 50k e 100k cards sintéticos):** afeta a escala de degradação em H3 e consumo de RAM em H2.

### Métricas

As dez métricas de Eficiência de Desempenho estão detalhadas na Tabela VII. Por restrição das ferramentas instrumentadas de baixo nível (`pidstat` e `perf`), as métricas de análise granular por thread associadas à Q4 são coletadas prioritariamente no ambiente Ubuntu Linux; nos sistemas Windows e macOS, a observação concorrente apoia-se nos monitores nativos de desempenho (*Performance Monitor* e *Activity Monitor*).

*Tabela VII. Métricas de Eficiência de Desempenho: definição, cálculo, coleta e interpretação*

| Métrica | Q | Definição | Função de cálculo | Procedimento e meio de coleta | Critério de interpretação |
|---|:---:|---|---|---|---|
| Tempo de inicialização (T<sub>ini</sub>) | Q1 | Intervalo entre o comando de disparo e a renderização da tela inicial | t<sub>janela pronta</sub> − t<sub>execução</sub> | Script automatizado (`time` / `perf stat`); média de 5 execuções frias (*cold*) | Menor é melhor; limiares baseados em Hoxmeier e DiCesare [11] |
| Tempo para iniciar revisão (T<sub>rev</sub>) | Q1, Q3 | Duração entre o clique em "Estudar Agora" e a exibição do primeiro card | t<sub>card visível</sub> − t<sub>clique</sub> | Registro de eventos de UI e instrumentação via `perf trace` | Menor é melhor; tempo de resposta perceptivo do estudante |
| Tempo de sincronização (T<sub>sinc</sub>) | Q1 | Tempo total de transferência e conciliação da coleção com o AnkiWeb | t<sub>fim sinc</sub> − t<sub>início sinc</sub> | Cronometragem em rede controlada com coleção padronizada | Menor é melhor; depende da latência de rede |
| Tempo de carga da coleção (T<sub>carga</sub>) | Q1, Q3 | Tempo de leitura e indexação do banco SQLite (`.anki2`) | t<sub>banco carregado</sub> − t<sub>abertura coleção</sub> | Medição instrumentada do encerramento das consultas de abertura | Menor é melhor; indicador direto de eficiência de armazenamento |
| Consumo de CPU (CPU<sub>med</sub>, CPU<sub>pico</sub>) | Q2 | Percentual de utilização dos núcleos de processamento pelo processo do Anki | Média e valor máximo amostrados no intervalo | Amostragem em intervalos de 1 s via `pidstat -u 1` (Linux) ou equivalente no Windows/macOS | Menor é melhor; reflete a pegada computacional sobre a máquina |
| Consumo de RAM (RAM<sub>med</sub>, RAM<sub>pico</sub>) | Q2, Q3 | Memória física residente (*Resident Set Size*, RSS) alocada | Média e pico de RSS (em MB) durante a sessão estabilizada | Amostragem com `pidstat -r 1` e biblioteca `psutil` após 5 min de uso | Menor é melhor; estabilidade sem vazamentos de memória (*leaks*) |
| Vazão de processamento (Vaz<sub>proc</sub>) | Q3 | Quantidade de cards validados por unidade de tempo no banco de dados | Cards processados ÷ tempo de processamento (cards/min) | Script em Python utilizando o pacote oficial `anki` (*Check Database*) | Maior é melhor; capacidade de processamento em lote |
| Uso de CPU na Main Thread (CPU<sub>main</sub>) | Q4 | Carga de processamento consumida pela thread de interface Qt | Percentual médio de CPU atribuído ao TID da thread principal | Coleta isolada via `pidstat -t -u 1` identificando a thread de UI | Menor é melhor; valores baixos asseguram ausência de travamentos |
| Trocas de contexto involuntárias (Ctx<sub>invol</sub>) | Q4 | Frequência de preempções forçadas do escalonador nas threads | Taxa média de trocas de contexto involuntárias (`nvcswch/s`) | Amostragem por thread via `pidstat -t -w 1` no ambiente Ubuntu Linux | Menor é melhor; alta taxa indica disputa excessiva por recursos |
| Taxa de I/O em disco (IO<sub>disco</sub>) | Q3, Q4 | Volume de leitura e escrita física no banco de dados SQLite | Taxa instantânea e média de transferência em kB/s (bytes ÷ tempo) | Monitoramento de descritores de arquivo e disco via `pidstat -t -d 1` | Menor em repouso é melhor; sob estresse, compatível com a taxa do disco |

### Níveis de Pontuação e Critérios de Julgamento

Os critérios de julgamento da Tabela VIII foram fixados antes da coleta. Os limiares de tempo de resposta apoiam-se no estudo experimental de Hoxmeier e DiCesare [11], validado na literatura de avaliação com a ISO/IEC 25010 [8], [9], delimitando faixas sem sobreposição de borda no formato a ≤ x < b. A escala de memória e CPU contempla o comportamento típico da interface PyQt/QtWebEngine sob computação heterogênea [7], [6].

*Tabela VIII. Níveis de pontuação das métricas de Eficiência de desempenho*

| Métrica / agrupamento | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Tempos de resposta (T<sub>ini</sub>, T<sub>rev</sub>, T<sub>sinc</sub>, T<sub>carga</sub>) | t ≥ 12 s ou falha | 9 ≤ t < 12 s | 3 ≤ t < 9 s | t < 3 s |
| Memória RAM em repouso (RAM<sub>rep</sub>) | RAM ≥ 400 MB | 250 ≤ RAM < 400 MB | 150 ≤ RAM < 250 MB | RAM < 150 MB |
| Memória RAM sob estresse (RAM<sub>estresse</sub>) | RAM ≥ 800 MB ou *leak* | 500 ≤ RAM < 800 MB | 350 ≤ RAM < 500 MB | RAM < 350 MB |
| CPU em repouso (CPU<sub>rep</sub>) | CPU ≥ 10% | 5% ≤ CPU < 10% | 2% ≤ CPU < 5% | CPU < 2% |
| Pico de CPU sob estresse (CPU<sub>pico</sub>) | CPU ≥ 90% sustentado | 70% ≤ CPU < 90% | 40% ≤ CPU < 70% | CPU < 40% |
| Degradação com 100k cards (Deg<sub>carga</sub>) | Δt ≥ 60% ou falha | 35% ≤ Δt < 60% | 15% ≤ Δt < 35% | Δt < 15% |
| Vazão de banco (Vaz<sub>proc</sub>, cards/min) | Vaz < 5.000 | 5.000 ≤ Vaz < 10.000 | 10.000 ≤ Vaz < 20.000 | Vaz ≥ 20.000 |
| CPU da Main Thread (CPU<sub>main</sub>) | CPU ≥ 60% ou trava > 1 s | 35% ≤ CPU < 60% | 15% ≤ CPU < 35% | CPU < 15% |
| Preempção involuntária (Ctx<sub>invol</sub>, `nvcswch/s`) | Ctx ≥ 50 | 20 ≤ Ctx < 50 | 10 ≤ Ctx < 20 | Ctx < 10 |
| Taxa de I/O em disco em repouso (IO<sub>rep</sub>) | IO ≥ 500 kB/s | 100 ≤ IO < 500 kB/s | 10 ≤ IO < 100 kB/s | IO < 10 kB/s |

**Regra de julgamento e plano de medição.** A consolidação ocorre de forma ascendente: cada métrica coletada é enquadrada na respectiva faixa de pontuação, gerando o julgamento de cada questão (Q1–Q4) e respondendo ao objetivo G2. O plano de medição detalhado (responsáveis, cronograma exato de amostragem, massa de dados sintética e scripts de automação) e o plano de análise ficam postergados para o Plano de Avaliação (Fase 3, a ser entregue no Ponto de Controle 2).

## Flexibilidade (antiga Portabilidade)

A equipe avalia as três subcaracterísticas de Flexibilidade da ISO/IEC 25010:2023: **instalabilidade**, que mede o esforço e a taxa de sucesso da instalação nas três plataformas; **adaptabilidade**, que verifica a integração do aplicativo com atalhos, tema escuro, bandeja e associação de arquivos; e **substituibilidade**, que mede a preservação de dados e o tempo de migração entre máquinas. A desinstalação é verificada apenas qualitativamente durante os testes (o usuário deve conseguir remover o Anki pelos mecanismos padrão do sistema operacional), sem métrica própria.

### Objetivo de Medição

O objetivo G3 segue o template do GQM [4], com o ponto de vista definido na Fase 1 e as decisões comuns da equipe. O propósito é identificar pontos de melhoria, e o ponto de vista é o do estudante, usuário final.

| Template GQM | G3 — Flexibilidade |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 e o fluxo de conta, login e sincronização do AnkiWeb |
| **para o propósito de** | entender |
| **com respeito a** | adaptabilidade, instalabilidade e substituibilidade |
| **do ponto de vista do** | estudante, usuário final |
| **no contexto de** | uso individual em computador pessoal, nas plataformas Windows, macOS e Ubuntu |

### Questões e Hipóteses

A Tabela IX apresenta as questões e as hipóteses de baseline, com os valores esperados ligados às métricas e às faixas de pontuação da Tabela XI.

*Tabela IX. Questões e hipóteses de Flexibilidade*

| Questão | Hipótese |
|---|---|
| **Q1** (Instalabilidade): o processo de instalação do Anki Desktop ocorre de forma simples e livre de erros nas três plataformas? | **H1:** no Windows e no macOS, a instalação tem 100% de sucesso, nenhuma intervenção manual e menos de 2 min; no Ubuntu, leva de 2 a 5 min e exige pelo menos uma intervenção manual. |
| **Q2** (Adaptabilidade): o Anki Desktop se adapta às características nativas de cada sistema operacional (atalhos, tema escuro, bandeja)? | **H2:** o checklist de integração atinge 10/10 no macOS e 9/10 no Windows e no Ubuntu, com falha pontual de tema escuro ou de associação de arquivos `.apkg` no Ubuntu. |
| **Q3** (Substituibilidade): a migração de dados (exportação, importação e sincronização) preserva a integridade das informações ao trocar de máquina? | **H3:** a migração via arquivos `.apkg` e AnkiWeb preserva 100% dos dados, com tempo de substituição inferior a 1 min. |

### Fatores de Variação

São registrados três fatores que podem influenciar os resultados: o **sistema operacional** (Windows, macOS ou Ubuntu), com maior tempo esperado no Ubuntu por causa de dependências como o `zstd`, que afeta H1 (tempo e intervenções de instalação) e H2 (integração com o sistema); a **arquitetura do processador** (x64 ou ARM), que afeta H1 (tempo de instalação); e a **permissão de administrador** (sim ou não), cuja ausência pode inviabilizar a instalação ou exigir intervenções e, portanto, afeta H1.

### Métricas

A Tabela X detalha as seis métricas do escopo, cada uma ligada a uma questão de pesquisa. A integração com o sistema operacional usa o checklist de 10 critérios derivado de Milichiewicz e Badurowicz [7]: (1) ícone na bandeja do sistema; (2) atalhos globais de teclado; (3) associação de arquivos `.apkg`; (4) diálogos nativos de abrir e salvar; (5) tema escuro sincronizado com o SO; (6) notificações nativas; (7) integração com a área de transferência; (8) menu contextual nativo; (9) arrastar e soltar arquivos `.apkg`; e (10) compatibilidade com recursos de acessibilidade do SO. As demais métricas são de escala de razão.

*Tabela X. Métricas de Flexibilidade: questão, definição, cálculo e interpretação*

| Métrica | Q | Definição | Cálculo | Critério de interpretação |
|---|:---:|---|---|---|
| Taxa de instalação bem-sucedida (T<sub>inst</sub>) | Q1 | Percentual de tentativas de instalação concluídas sem falha em cada plataforma | N<sub>sucesso</sub> / N<sub>tentativas</sub> × 100% | Maior é melhor; 0–100% |
| Tempo de instalação (T<sub>inst_t</sub>) | Q1 | Tempo entre o início e a conclusão do processo de instalação | t<sub>fim</sub> − t<sub>início</sub> (min) | Menor é melhor; > 0 min |
| Número de intervenções (N<sub>int</sub>) | Q1 | Quantidade de ações manuais extras exigidas para concluir a instalação | Contagem inteira | Menor é melhor; inteiro ≥ 0 |
| Pontuação no checklist de integração (P<sub>int</sub>) | Q2 | Soma dos critérios de integração com o SO atendidos (10 itens) | Soma de c<sub>i</sub>, com c<sub>i</sub> ∈ {0, 1}, para i = 1 a 10 | Maior é melhor; 0–10 |
| Taxa de preservação de dados (T<sub>pd</sub>) | Q3 | Percentual de itens da coleção preservados após a migração | N<sub>preservados</sub> / N<sub>totais</sub> × 100% | Maior é melhor; 0–100% |
| Tempo de substituição (T<sub>sub</sub>) | Q3 | Tempo entre o início e a conclusão da migração com verificação de integridade | t<sub>fim</sub> − t<sub>início</sub> (min) | Menor é melhor; > 0 min |

### Níveis de Pontuação e Critérios de Julgamento

Os níveis da Tabela XI foram definidos por acordo da equipe, com base nas metas de aceitação do projeto e nas referências da literatura. A faixa *Mínimo* da Substituibilidade foi preenchida com a exigência de intervenção manual, que separa a migração automática (alvo/excelente) da migração que exige correção.

*Tabela XI. Níveis de pontuação das métricas de Flexibilidade*

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Taxa de instalação T<sub>inst</sub> (Q1) | < 100% (falha) | 100% com uma intervenção manual | 100% sem intervenção | 100% sem intervenção e T<sub>inst_t</sub> < 2 min |
| Tempo de instalação T<sub>inst_t</sub> (Q1) | > 10 min | 5 a 10 min | 2 a 5 min | < 2 min |
| Número de intervenções N<sub>int</sub> (Q1) | > 2 | 2 | 1 | 0 |
| Pontuação no checklist P<sub>int</sub> (Q2) | < 6/10 | 6 ou 7/10 | 8 ou 9/10 | 10/10 |
| Taxa de preservação T<sub>pd</sub> (Q3) | Perda de dados | 100% com intervenção manual | 100% automática em até 1 min | 100% automática em menos de 1 min |
| Tempo de substituição T<sub>sub</sub> (Q3) | > 5 min | 2 a 5 min | 1 a 2 min | < 1 min |

**Regra de julgamento.** O julgamento procede de baixo para cima [4]: cada métrica é classificada em uma faixa, as faixas são agregadas por questão e as questões respondem ao G3. Uma questão é atendida quando suas métricas essenciais (T<sub>inst</sub> e T<sub>inst_t</sub> em Q1; P<sub>int</sub> em Q2; T<sub>pd</sub> e T<sub>sub</sub> em Q3) estão no alvo ou acima; havendo divergência, prevalece a faixa mais baixa. As faixas mínimo e insatisfatório tornam-se recomendações priorizadas, e a mais relevante alimenta a ação de melhoria da Entrega 2. O plano de medição detalhado (quem coleta, quando e como), o número de participantes e o caminho mínimo das tarefas ficam para o plano de avaliação (Fase 3, PC2).

## Diagrama GQM

A Figura 2 apresenta a hierarquia GQM da avaliação: os três objetivos no nível conceitual, as questões no nível operacional e as métricas no nível quantitativo, cada uma acompanhada da questão que responde.

![Hierarquia GQM da avaliação](assets/diagrama-gqm.png)

*Figura 2. Hierarquia GQM da avaliação: objetivos, questões e métricas de Capacidade de interação, Eficiência de desempenho e Flexibilidade.*

## Coerência entre as Fases 1 e 2

A Fase 1 delimitou o escopo, sob o ponto de vista do estudante, em quatro componentes: a interface do Anki Desktop, sua execução em Windows, macOS e Ubuntu, a instalação e o fluxo de conta e sincronização do AnkiWeb. A Fase 2 mantém nos três objetivos esse ponto de vista e a priorização da Fase 1 (Capacidade de interação com ênfase 5, as demais com 3): as questões de **Capacidade de interação** avaliam a interação com a interface e com o fluxo de conta e sincronização; as métricas de **Eficiência de desempenho** medem a execução e a fluidez do estudo; e as de **Flexibilidade** cobrem a instalação e a migração entre as três plataformas.
