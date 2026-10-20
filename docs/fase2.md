# Fase 2 — Especificar a avaliação

Nesta fase, cada característica priorizada na [Fase 1](fase1.md) foi desdobrada pela abordagem *Goal-Question-Metric* (GQM), de Basili, Caldiera e Rombach (1994): um **objetivo de medição** (nível conceitual), **questões** com **hipóteses** (nível operacional) e **métricas** (nível quantitativo). Para cada métrica foram definidos cálculo, fonte, procedimento de coleta, critério de interpretação, faixa de valores e meio de coleta, além de **níveis de pontuação** e **critérios de julgamento**, fixados antes da coleta.

As três características usam as mesmas quatro faixas de pontuação: **insatisfatório**, **mínimo**, **alvo** e **excelente**.

| Característica | Responsáveis | Subcaracterísticas avaliadas |
|---|---|---|
| [Usabilidade](#usabilidade) | Dupla A (Davi e Pedro) | Reconhecibilidade da adequação, facilidade de aprendizado e operabilidade |
| [Eficiência de desempenho](#eficiencia-de-desempenho) | Dupla B (Karolina e Mateus) | Comportamento no tempo, utilização de recursos e capacidade |
| [Portabilidade](#portabilidade) | Dupla C (Bryan e Dante) | Adaptabilidade, instalabilidade e substituibilidade |

---

## Usabilidade

### Subcaracterísticas escolhidas

- **Reconhecibilidade da adequação:** o Anki usa conceitos próprios, como nota, tipo de nota, card e baralho, e o estudante precisa perceber, pela interface, quais funções atendem ao que ele quer fazer.
- **Facilidade de aprendizado:** a Fase 1 definiu que o estudante usa o Anki sozinho, sem treinamento nem suporte, e por isso importa se ele aprende as tarefas essenciais por conta própria.
- **Operabilidade:** quem já usa o Anki repete as mesmas tarefas todos os dias, como revisar, adicionar cards e sincronizar, e o esforço para executá-las afeta o uso contínuo.

Os testes envolvem dois grupos de estudantes. Os **iniciantes**, que nunca usaram o Anki, respondem principalmente às questões de reconhecibilidade e aprendizado. Os **usuários frequentes** respondem à questão de operabilidade e servem de comparação com os iniciantes.

### Objetivo de medição

| Template GQM | Usabilidade |
|---|---|
| Analisar | o Anki Desktop 26.09.3 e o fluxo de criação de conta, login e sincronização do AnkiWeb |
| para o propósito de | entender, identificando pontos de melhoria |
| com respeito a | reconhecibilidade da adequação, facilidade de aprendizado e operabilidade |
| do ponto de vista do | estudante, usuário final (iniciante e usuário frequente) |
| no contexto de | uso individual em computador pessoal, sem treinamento formal |

### Questões e hipóteses

| Questão | Hipótese |
|---|---|
| **Q1** (Reconhecibilidade da adequação): um estudante que nunca usou o Anki consegue identificar, pela interface, quais funções usar para criar seus cards e estudar? | **H1:** a maioria dos iniciantes identifica as funções principais (criar baralho, adicionar cards e estudar), mas confunde conceitos próprios do Anki, como nota, tipo de nota e card. |
| **Q2** (Facilidade de aprendizado): um estudante iniciante consegue aprender, sem ajuda, a criar uma conta no AnkiWeb, criar um baralho, adicionar cards, revisá-los e sincronizar a coleção? | **H2:** os iniciantes concluem sem ajuda as tarefas de criar baralho, adicionar cards e revisar, mas precisam de mais tempo ou de ajuda na criação de conta e na primeira sincronização, que exigem alternar entre o site e o aplicativo. |
| **Q3** (Operabilidade): as tarefas do estudo diário podem ser executadas com pouco esforço por quem já usa o Anki? | **H3:** usuários frequentes revisam e adicionam cards rapidamente e com poucas ações; a maior diferença entre iniciantes e frequentes aparece nas tarefas de conta e sincronização. |

### Fatores de variação

Registrados por um questionário de perfil aplicado antes dos testes:

| Fator | Escala | Efeito esperado |
|---|---|---|
| Familiaridade com informática | Ordinal (baixa, média ou alta) | Participantes com baixa familiaridade levam mais tempo nas tarefas de conta e sincronização |
| Experiência prévia com aplicativos de flashcards | Nominal | Facilita o reconhecimento das funções de criação e revisão de cards (Q1) |
| Sistema operacional usado | Nominal (Windows, macOS ou Ubuntu) | Pode alterar o tempo e o número de ações das tarefas (Q2 e Q3) |

### Métricas

Todas as métricas são de escala de razão e coletadas em sessões observadas, com consentimento registrado, nas tarefas da Fase 1 (criar baralho, adicionar cards, revisar, criar conta no AnkiWeb, login e sincronizar).

| Métrica | Questão | Cálculo | Fonte e procedimento de coleta | Interpretação e faixa |
|---|---|---|---|---|
| Taxa de reconhecimento de funções | Q1 | Participantes que identificam a função ÷ participantes × 100%, por tarefa | O avaliador descreve a tarefa sem o jargão do Anki; o participante indica a função; o acerto é registrado antes de qualquer ajuda (formulário de observação) | Maior é melhor; 0 a 100% |
| Taxa de identificação de propósito | Q1 | Respostas corretas ÷ (itens × participantes) × 100% | O participante explica o propósito de uma função ou tela; a resposta é classificada por gabarito alinhado ao manual do Anki | Maior é melhor; 0 a 100% |
| Tempo de aprendizagem | Q2 | Média do tempo total dos iniciantes no roteiro completo | Cronômetro do início da primeira tarefa à conclusão da última (ou ao abandono); ajudas registradas à parte | Menor é melhor; acima de 0 min |
| Taxa de sucesso após aprendizagem inicial | Q2 | Tarefas corretas ÷ tarefas propostas × 100%, marcando "sem ajuda" e "com ajuda" | Checklist de sucesso por tarefa, verificando o estado do produto ao final de cada tarefa | Maior é melhor; 0 a 100% |
| Redução do tempo de execução | Q2 | (tempo da 1ª execução − tempo da 2ª execução) ÷ tempo da 1ª execução × 100% | A mesma tarefa é repetida na sessão, sem nova instrução; registro pareado dos dois tempos | Maior é melhor; pode ser negativa |
| Taxa de conclusão de tarefas | Q3 | Tarefas concluídas ÷ tarefas propostas × 100%, por grupo | Roteiro de operabilidade; conclusão, abandono ou falha marcados no formulário | Maior é melhor; 0 a 100% |
| Tempo de execução da tarefa | Q3 | Média dos tempos por tarefa e por grupo (também a mediana) | Cronômetro do recebimento da tarefa até o estado de sucesso; sistema operacional registrado | Menor é melhor; acima de 0 s |
| Número médio de ações | Q3 | Média de cliques, atalhos e entradas por tarefa | Contagem pelo avaliador, incluindo ações de correção de erro | Menor é melhor; inteiro maior ou igual a 0 |

### Níveis de pontuação

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Taxa de reconhecimento de funções (Q1) | abaixo de 60% | 60% a 75% | 75% a 90% | 90% ou mais |
| Taxa de identificação de propósito (Q1) | abaixo de 55% | 55% a 70% | 70% a 85% | 85% ou mais |
| Tempo de aprendizagem (Q2) | acima de 40 min ou abandono | 25 a 40 min | 15 a 25 min | menos de 15 min |
| Taxa de sucesso após aprendizagem inicial (Q2) | abaixo de 60% ou intervenção recorrente | 60% a 75% | 75% a 90% sem ajuda, ou 90% ou mais com uma ajuda | 90% ou mais sem ajuda |
| Redução do tempo de execução (Q2) | abaixo de 5% ou negativa | 5% a 20% | 20% a 40% | 40% ou mais |
| Taxa de conclusão, usuários frequentes (Q3) | abaixo de 80% ou abandono | 80% a 90%, ou 100% com uma ajuda | 90% ou mais sem ajuda | 100% sem ajuda |
| Tempo de execução da tarefa (Q3) | acima de 12 s ou falha | 9 a 12 s | 3 a 9 s | menos de 3 s |
| Número médio de ações (Q3) | mais de 3 vezes o caminho mínimo | até 3 vezes | até 2 vezes | até 1,5 vez |

**Origem dos limites:** os limites de tempo por tarefa seguem os limiares de satisfação de Hoxmeier e DiCesare (2000), já usados em avaliações ISO/IEC 25010 (Sukmandari e Sukardiyono, 2017; Jayanto e Jati, 2017). Os demais foram definidos por acordo da equipe, na ausência de dados históricos do Anki. O caminho mínimo de cada tarefa, usado no número de ações, será fixado no plano de avaliação (Fase 3).

### Critérios de julgamento

O julgamento procede de baixo para cima: cada métrica é classificada em uma faixa, as faixas são agregadas por questão e as questões respondem ao objetivo.

- **Q1** é atendida quando a taxa de reconhecimento e a taxa de identificação estão, em média, no alvo ou acima nas funções principais. Se nota, tipo de nota e card caírem em mínimo ou insatisfatório, H1 é sustentada, e o ponto de melhoria prioriza a clareza desses conceitos.
- **Q2** é atendida quando a taxa de sucesso está no alvo ou acima, o tempo de aprendizagem não é insatisfatório e a redução do tempo atinge pelo menos o mínimo. Se conta e sincronização ficarem abaixo das demais tarefas, H2 é sustentada.
- **Q3** é atendida quando, entre os usuários frequentes, a taxa de conclusão, o tempo de execução e o número de ações estão no alvo ou acima nas tarefas diárias. A maior diferença em conta e sincronização sustenta H3.

Havendo divergência dentro de uma questão, prevalece a faixa mais baixa entre as métricas essenciais (reconhecimento e identificação em Q1; sucesso e tempo de aprendizagem em Q2; conclusão e tempo de execução em Q3). Os fatores de variação não alteram os limites, mas são reportados na interpretação. As faixas mínimo e insatisfatório tornam-se recomendações priorizadas, e a mais relevante alimenta a ação de melhoria da Entrega 2.

---

## Eficiência de desempenho

### Objetivo de medição

| Template GQM | Eficiência de desempenho |
|---|---|
| Analisar | o Anki Desktop 26.09.3 e a sincronização com o AnkiWeb |
| para o propósito de | entender, identificando pontos de melhoria |
| com respeito a | comportamento no tempo, utilização de recursos, capacidade e eficiência a nível de threads |
| do ponto de vista do | estudante, usuário final (operador) |
| no contexto de | uso individual em computador pessoal com Windows, macOS ou Ubuntu |

### Questões e hipóteses

| Questão | Hipótese |
|---|---|
| **Q1** (Comportamento no tempo): quais ações do estudante no Anki Desktop levam mais tempo para responder: abrir o aplicativo, iniciar a revisão ou sincronizar? | **H1:** a sincronização é a ação mais demorada, e abrir o aplicativo e iniciar a revisão respondem em menos de 3 segundos. |
| **Q2** (Utilização de recursos): como o uso de CPU e de memória RAM varia entre o cenário de repouso e o cenário de estresse? | **H2:** o consumo de CPU e de RAM é maior no estresse do que no repouso, mantendo-se dentro da faixa esperada para aplicações PyQt. |
| **Q3** (Capacidade): como o aumento da quantidade de cards influencia o tempo de processamento e a resposta do Anki Desktop? | **H3:** o aumento de cards eleva gradualmente o tempo de carregamento e o consumo de memória, sem tornar o estudo perceptivelmente lento. |
| **Q4** (Eficiência a nível de threads): durante operações intensivas de banco de dados e sincronização, o processamento pesado permanece nas *Worker Threads* (Rust) sem bloquear a *Main Thread* (interface Qt)? | **H4:** o backend em Rust absorve a carga de I/O e de CPU, mantendo a *Main Thread* livre de contenção e evitando o congelamento da interface. |

### Fatores de variação

| Fator | Escala | Efeito esperado |
|---|---|---|
| Configuração de hardware (processador, núcleos, RAM e tipo de disco) | Nominal e razão | Máquinas com menos núcleos ou disco mais lento tendem a tempos maiores e mais disputa entre threads (Q1 a Q4) |
| Sistema operacional e servidor gráfico (Windows 11, macOS ou Ubuntu com X11/Wayland) | Nominal | Alteram memória, CPU e comportamento das threads de renderização (Q1, Q2 e Q4) |
| Porte da coleção (10, 50 e 100 mil cards) | Razão | Coleções maiores exigem mais memória e elevam leitura e escrita no SQLite (Q2 a Q4) |
| Condições de rede e processos em segundo plano | Razão | Afetam o tempo de sincronização (Q1) e as preempções involuntárias (Q2 e Q4) |

### Métricas

Todas as métricas são de escala de razão.

| Métrica | Questão | Faixa de valores | Meio de coleta |
|---|---|---|---|
| Tempo de inicialização (*cold* e *warm start*) | Q1 | acima de 0 s | Script automatizado (`time` / `perf stat`) até abrir a janela principal |
| Tempo para iniciar a revisão e exibir a resposta | Q1, Q3 | acima de 0 s | `perf trace` e registro de eventos da interface |
| Tempo de sincronização | Q1 | acima de 0 s | Cronometragem do início ao fim da sincronização com o AnkiWeb |
| Tempo de carregamento da coleção | Q1, Q3 | acima de 0 s | Tempo de leitura do banco `.anki2` (SQLite) |
| Uso médio e de pico de CPU | Q2 | 0 a 100% | `pidstat -u 1` (Linux), Monitor de Atividade (macOS) e Gerenciador de Tarefas (Windows) |
| Uso médio e de pico de RAM | Q2, Q3 | acima de 0 MB | Memória residente estabilizada após 5 min, via `pidstat -r 1` ou `psutil` |
| Vazão de processamento | Q3 | acima de 0 cards/min (10, 50 e 100 mil cards) | Script em Python com o pacote `anki` e a rotina *Check Database* |
| Uso de CPU por thread | Q4 | 0 a 100% por thread | `pidstat -t -u 1` no Linux (*Main Qt*, *Worker Rust* e *WebEngine*) |
| Trocas de contexto por thread | Q4 | 0 ou mais trocas/s | `pidstat -t -w 1` no Linux (`cswch/s` e `nvcswch/s`) |
| Taxa de I/O em disco por thread | Q3, Q4 | 0 ou mais kB/s | `pidstat -t -d 1` no Linux (leitura e escrita no SQLite) |

### Níveis de pontuação

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Tempos de resposta (Q1) | acima de 12 s, falha ou *timeout* | 9 a 12 s | 3 a 9 s | menos de 3 s |
| Memória RAM (Q2) | acima de 800 MB ou crescimento contínuo | 500 a 800 MB no estresse | 150 a 250 MB em repouso; até 500 MB no estresse | até 150 MB em repouso; até 350 MB no estresse |
| CPU (Q2) | acima de 5% em repouso | picos de 70% a 90% | até 5% em repouso; 40% a 70% no estresse | até 2% em repouso; até 40% no estresse |
| Capacidade com 100 mil cards (Q3) | acima de 12 s, degradação acima de 60% ou falha no SQLite | 9 a 12 s; degradação de 35% a 60% | 3 a 9 s; degradação de 15% a 35% | menos de 3 s; degradação abaixo de 15% |
| Threads (Q4) | *Main Thread* com 80% de CPU ou mais, ou congelamento | *Main Thread* até 60%; 10 a 50 trocas involuntárias/s; travamento de até 1 s | *Main Thread* de 15% a 35%, sem atraso perceptível | *Main Thread* abaixo de 15%; menos de 10 trocas involuntárias/s; sem congelamento |

**Origem dos limites:** limiares de tempo de resposta de Hoxmeier e DiCesare (2000), adotados em avaliações ISO/IEC 25010 (Sukmandari e Sukardiyono, 2017; Jayanto e Jati, 2017); perfil de recursos de aplicações PyQt (Milichiewicz e Badurowicz, 2025); e estudos de eficiência sob carga (Pereira et al., 2023; Rojas et al., 2025).

---

## Portabilidade

### Objetivo de medição

| Template GQM | Portabilidade |
|---|---|
| Analisar | o Anki Desktop 26.09.3 (instalação, adaptação e substituição de dados) |
| para o propósito de | entender, identificando pontos de melhoria |
| com respeito a | adaptabilidade, instalabilidade e substituibilidade |
| do ponto de vista do | estudante, usuário final |
| no contexto de | uso individual em computador pessoal, nas plataformas Windows, macOS e Ubuntu |

### Questões e hipóteses

| Questão | Hipótese |
|---|---|
| **Q1** (Instalabilidade): o processo de instalação e desinstalação do Anki Desktop ocorre de forma simples e livre de erros nas três plataformas? | **H1:** as instalações via pacote (Windows e macOS) são rápidas e intuitivas, enquanto a instalação no Ubuntu, via script, pode exigir mais intervenções e apresentar maior taxa de falha. |
| **Q2** (Adaptabilidade): o Anki Desktop se adapta às características nativas de cada sistema operacional (atalhos, tema escuro, bandeja)? | **H2:** a adaptação é excelente no macOS e no Windows, mas apresenta falhas pontuais de integração visual (tema escuro) e de associação de arquivos no Ubuntu. |
| **Q3** (Substituibilidade): a migração de dados (exportação, importação e sincronização) preserva a integridade das informações ao trocar de máquina ou versão? | **H3:** a migração via arquivos `.apkg` e AnkiWeb preserva 100% da integridade dos dados. |

### Fatores de variação

| Fator | Escala | Efeito esperado |
|---|---|---|
| Sistema operacional (Windows, macOS ou Ubuntu) | Nominal | Maior tempo de adaptação no Ubuntu, por dependências como o `zstd` |
| Arquitetura do processador (x64 ou ARM) | Nominal | Pode alterar o tempo de instalação |
| Permissão de administrador (sim ou não) | Nominal | Sua ausência pode inviabilizar a instalação ou exigir intervenções |

### Métricas

A integração com o sistema operacional usa um checklist de 10 critérios derivado de Milichiewicz e Badurowicz (2025), como bandeja do sistema, atalhos globais, associação de arquivos `.apkg`, diálogos nativos e tema escuro. É a única métrica de escala ordinal; as demais são de escala de razão.

| Métrica | Faixa | Meio de coleta |
|---|---|---|
| Taxa de execução multiplataforma (%) | 0 a 100 | Registro da execução das funcionalidades nas três plataformas |
| Taxa de preservação funcional (%) | 0 a 100 | Comparação das funcionalidades nos ambientes de origem e destino |
| Taxa de preservação de dados (%) | 0 a 100 | Inspeção do banco SQLite (DB Browser) |
| Tempo de adaptação e configuração (min) | acima de 0 | Medição do tempo de adaptação e configuração |
| Taxa de instalação bem-sucedida (%) | 0 a 100 | Formulário de observação do avaliador |
| Tempo de instalação (min) | acima de 0 | Cronômetro |
| Número de intervenções necessárias | inteiro maior ou igual a 0 | Formulário de observação |
| Taxa de falhas de instalação (%) | 0 a 100 | Registro das tentativas de instalação |
| Taxa de substituição bem-sucedida (%) | 0 a 100 | Verificação do funcionamento após a substituição |
| Tempo de substituição (min) | acima de 0 | Medição do tempo de substituição |
| Integridade pós-substituição (%) | 0 a 100 | Inspeção do banco SQLite (DB Browser) |
| Integração com o sistema (pontos) | 0 a 10 | Checklist de 10 critérios |

### Níveis de pontuação

| Subcaracterística | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Instalabilidade (Q1) | Falha na instalação | Sucesso após uma intervenção | 100% de sucesso, entre 2 e 5 min | 100% de sucesso, em menos de 2 min |
| Adaptabilidade (Q2) | Menos de 6/10 no checklist | 6 ou 7/10 | 8 ou 9/10 | 10/10 |
| Substituibilidade (Q3) | Perda de dados | não se aplica | 100% de integridade, em mais de 1 min | 100% de integridade, em menos de 1 min |

**Origem dos limites:** acordo da equipe, com base nas metas de aceitação do projeto.

---

## Diagrama GQM

O diagrama reúne a hierarquia completa da avaliação: os três objetivos no nível conceitual, as questões no nível operacional e as métricas no nível quantitativo, cada uma acompanhada da questão que responde.

![Hierarquia GQM da avaliação](assets/diagrama-gqm.png)

*Figura 2. Hierarquia GQM: objetivos, questões e métricas de Usabilidade, Eficiência de desempenho e Portabilidade.*

## Coerência entre as Fases 1 e 2

A Fase 1 delimitou o escopo, sob o ponto de vista do estudante, em quatro componentes: a interface do Anki Desktop, sua execução em Windows, macOS e Ubuntu, a instalação e o fluxo de conta e sincronização do AnkiWeb. A Fase 2 mantém nos três objetivos esse mesmo ponto de vista e a priorização da Fase 1 (Usabilidade com ênfase 5; Eficiência de desempenho e Portabilidade com ênfase 3).

| Componente da Fase 1 | Onde é avaliado na Fase 2 |
|---|---|
| Interface do usuário do Anki Desktop | Usabilidade: Q1, Q2 e Q3 |
| Criação de conta no AnkiWeb, login e sincronização | Usabilidade: Q2 e Q3; Eficiência de desempenho: Q1 e Q4; Portabilidade: Q3 |
| Execução em Windows, macOS e Ubuntu | Eficiência de desempenho: Q1 a Q4; Portabilidade: Q2 |
| Instalação e desinstalação | Portabilidade: Q1 |

## Referências

- Basili, V. R., Caldiera, G. e Rombach, H. D. (1994). The Goal Question Metric approach. *Encyclopedia of Software Engineering*, p. 528–532. John Wiley & Sons.
- Hoxmeier, J. A. e DiCesare, C. (2000). System response time and user satisfaction: an experimental study of browser-based applications. *Proceedings of AMCIS 2000*.
- ISO/IEC (2011). *ISO/IEC 25010: Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*.
- Jayanto, R. D. e Jati, H. (2017). Evaluasi kualitas aplikasi mobile kamus istilah jaringan pada platform android dengan standar ISO/IEC 25010. *Elinvo*, 2(2):178–183.
- Milichiewicz, R. e Badurowicz, M. (2025). Comparative analysis of cross-platform application development tools in terms of operating system integration. *Journal of Computer Science Institute*, 36:357–364.
- Pereira, D. S. et al. (2023). Performance efficiency evaluation based on ISO/IEC 25010:2011 applied to a case study on load balance and resilient. *Anais do WPerformance / CSBC*. SBC.
- Rojas, H., Renteria, R. e Martinez, V. (2025). Understanding performance efficiency in ISO/IEC 25000: a systematic literature review. *JOIV*, 9(6):2405–2417.
- Sukmandari, D. G. e Sukardiyono, T. (2017). Analisis aplikasi jadwal perkuliahan berbasis android berdasarkan standar ISO 25010. *Elinvo*, 2(1):80–84.