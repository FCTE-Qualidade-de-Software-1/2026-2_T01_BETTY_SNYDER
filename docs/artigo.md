# Avaliação da Qualidade do Anki Desktop e do AnkiWeb segundo a ISO/IEC 25010:2023

**Bryan Smith Rodrigues Cavalcante, Dante Fernandes Scarpati, Davi Severiano Freitas, Karolina Vieira Barbosa, Mateus de Siqueira Silva e Pedro Henrique Freire Rodrigues**

Faculdade de Ciências e Tecnologias em Engenharia (FCTE) / Faculdade UnB Gama (FGA), Universidade de Brasília (UnB), Brasília, DF, Brasil. Disciplina FGA0315 Qualidade de Software 1, Profa. Dra. Cristiane Ramos. Equipe Betty Snyder.

`{bryan.cavalcante, dante.scarpati, davi.freitas, karolina.barbosa, mateus.siqueira, pedro.rodrigues}@aluno.unb.br`

*Versão da Entrega 1 (Fases 1 e 2), 26/10/2026.*

---

**Resumo.** Este artigo especifica a avaliação da qualidade do Anki Desktop 26.09.3 e do fluxo de conta, login e sincronização do AnkiWeb, com base na ISO/IEC 25010:2023. Na Fase 1, definem-se o requisitante, o propósito de indicar pontos de melhoria do ponto de vista do estudante, o modelo de qualidade adaptado e o escopo. Na Fase 2, o GQM deriva objetivos, questões, hipóteses, métricas, níveis de pontuação e critérios de julgamento para Capacidade de interação, Eficiência de desempenho e Flexibilidade. A gestão do projeto é acompanhada pelo PSM.

**Abstract.** This paper specifies the quality evaluation of Anki Desktop 26.09.3 and of the AnkiWeb account, login and synchronization flow, based on ISO/IEC 25010:2023. Phase 1 defines the requester, the purpose of identifying improvement points from the student's point of view, the adapted quality model and the scope. Phase 2 uses the Goal-Question-Metric approach to derive goals, questions, hypotheses, metrics, scoring levels and judgment criteria for Interaction Capability, Performance Efficiency and Flexibility. Project management is monitored with Practical Software Measurement (PSM).

---

## 1. Introdução

O processo de garantia da qualidade de software consolidou-se como disciplina nuclear da Engenharia de Software moderna, estabelecendo critérios objetivos para que produtos atendam tanto às expectativas funcionais dos usuários quanto a restrições de engenharia e desempenho [Galin 2018]. No contexto de ferramentas educacionais, o **Anki Desktop** ([github.com/ankitects/anki](https://github.com/ankitects/anki)) é uma plataforma de memorização ativa por repetição espaçada (*Spaced Repetition System*, SRS), construída com Python, Rust e a interface gráfica PyQt/QtWebEngine, que funciona em diferentes sistemas operacionais e armazena as coleções localmente em SQLite.

O presente trabalho, conduzido pela **Equipe Betty Snyder** na disciplina de Qualidade de Software 1 da Universidade de Brasília (FGA/FCTE-UnB), tem como objetivo avaliar a qualidade de produto do Anki Desktop (versão 26.09.3) e do fluxo de conta, login e sincronização do AnkiWeb, para indicar pontos de melhoria do ponto de vista do estudante. A avaliação segue a ISO/IEC 25010:2023 [ISO/IEC 2023a] e o processo de avaliação de produto [ISO/IEC 2023b], e a gestão do projeto é acompanhada pelo *Practical Software Measurement* (PSM) [McGarry et al. 2002].

## 2. Fundamentação Teórica e Trabalhos Relacionados

### 2.1. O Modelo de Qualidade de Produto ISO/IEC 25010:2023

A família de normas ISO/IEC 25000 (SQuaRE) estrutura a qualidade do produto de software em nove características principais [ISO/IEC 2023a]: adequação funcional, eficiência de desempenho, compatibilidade, capacidade de interação (antiga usabilidade), confiabilidade, segurança, manutenibilidade, flexibilidade (antiga portabilidade) e *safety* (segurança operacional). A **capacidade de interação** compreende reconhecibilidade da adequação, facilidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, inclusividade, assistência ao usuário e autodescritividade; a **flexibilidade** compreende adaptabilidade, escalabilidade, instalabilidade e substituibilidade. No escopo deste projeto, foram selecionadas três características: **Capacidade de interação**, **Eficiência de desempenho** e **Flexibilidade**. As subcaracterísticas efetivamente avaliadas constam na Figura 1 e são detalhadas na Fase 2 (Seção 5).

### 2.2. Processo de Avaliação de Produto

O processo de avaliação de produto de software é organizado em quatro fases. Na **Fase 1, estabelecer requisitos de avaliação**, definem-se o propósito da avaliação, o tipo de produto e o modelo de qualidade, com base no interesse do requisitante. Na **Fase 2, especificar a avaliação**, as subcaracterísticas são desdobradas em métricas, e definem-se níveis de pontuação e critérios de julgamento antes da coleta. Na **Fase 3, projetar a avaliação**, produz-se o plano de avaliação, com método, recursos e cronograma. Na **Fase 4, executar a avaliação**, obtêm-se as medidas, comparam-se com os critérios e julgam-se os resultados.

### 2.3. Goal-Question-Metric (GQM)

A abordagem *Goal-Question-Metric* (GQM), proposta por Basili, Caldiera e Rombach [Basili et al. 1994], define medições a partir de objetivos, em três níveis. No **nível conceitual**, o objetivo descreve um objeto de medição, um foco de qualidade, um ponto de vista e um contexto, segundo o template: *Analisar* (o objeto) *para o propósito de* (entender, melhorar ou controlar) *com respeito a* (foco de qualidade) *do ponto de vista de* (ator interessado) *no contexto de* (ambiente). No **nível operacional**, o objetivo é desdobrado em questões, associadas a hipóteses. No **nível quantitativo**, cada questão recebe as métricas que a respondem. O processo compreende planejamento, definição, coleta de dados e interpretação; a definição ocorre de cima para baixo e a interpretação, de baixo para cima [Basili et al. 1994].

### 2.4. Practical Software Measurement (PSM)

Proposto por McGarry et al. [McGarry et al. 2002] e alinhado à norma ISO/IEC 15939, o PSM fundamenta-se no Modelo de Informação de Medição, que conecta os atributos mensuráveis do projeto à tomada de decisão. Um **atributo** é quantificado por um método de medição para gerar uma **medida básica**; medidas básicas combinadas por uma função compõem uma **medida derivada**; com um modelo de análise e critérios de decisão, obtém-se um **indicador**, cuja interpretação atende à **necessidade de informação**. O *PSM Continuous Iterative Development (CID) Measurement Framework* [PSM 2021] atualiza esse modelo, e o projeto o aplica nas categorias *Recursos e Custos*, *Desempenho dos Processos* e *Calendário e Progresso*.

### 2.5. Trabalhos Relacionados

Rojas et al. [Rojas et al. 2025] mapeiam, em revisão sistemática, 68 métricas e 46 ferramentas de eficiência de desempenho na ISO/IEC 25010, com predominância de comportamento no tempo e utilização de recursos. Pereira et al. [Pereira et al. 2023] medem vazão, tempo de resposta e consumo de CPU e RAM em cenários de estresse. Milichiewicz e Badurowicz [Milichiewicz e Badurowicz 2025] comparam a pegada de memória e a integração com o sistema operacional de aplicações multiplataforma, incluindo PyQt, base do Anki Desktop. Sukmandari e Sukardiyono [Sukmandari e Sukardiyono 2017] e Jayanto e Jati [Jayanto e Jati 2017] aplicam a ISO/IEC 25010 com o *USE Questionnaire* [Lund 2001] e os limiares de tempo de resposta de Hoxmeier e DiCesare [Hoxmeier e DiCesare 2000].

## 3. Metodologia de Desenvolvimento do Projeto

### 3.1. Processo e Organização da Equipe

O trabalho segue as quatro fases descritas na Seção 2.2: as Fases 1 e 2 compõem a Entrega 1; a Fase 3, com o plano de avaliação, está prevista para o Ponto de Controle 2; e a Fase 4, com a execução, o julgamento e a ação de melhoria, para a Entrega 2.

A equipe, de seis integrantes, organiza-se em três duplas para distribuir as atividades da Entrega 1. As decisões são tomadas em reuniões registradas em ata; o artigo é escrito no Overleaf; o repositório no GitHub guarda documentos, atas, dados das medições e a GitPage; e as horas são registradas em planilha compartilhada. Na Entrega 1, as tarefas são acompanhadas pelos planejamentos, pelas atas e pelo documento de pendências da equipe. Até o momento da consolidação deste registro, **não haviam sido criadas *issues* no GitHub** para esse acompanhamento (a criação de *issues* permanece como possibilidade para a Entrega 2).

### 3.2. Sistema de Medição PSM

#### 3.2.1. Construtos de Medição

Os construtos seguem o Modelo de Informação de Medição de McGarry et al. [McGarry et al. 2002] e o template de instância do modelo de informação (*measurement construct*) do PSM [PSM 2021]. Os três realizam análise de performance: com o projeto em andamento, avaliam se o planejado está sendo cumprido (Tabela 1). Os limites dos critérios de decisão foram definidos pela equipe em 18/10/2026, por acordo, por não haver dados históricos de projetos anteriores.

*Tabela 1. Construtos de medição do PSM*

| Campo | Recursos e Custos | Desempenho dos Processos | Calendário e Progresso |
|---|---|---|---|
| Necessidade de informação | O esforço da equipe está dentro do planejado e equilibrado entre os integrantes? | As revisões encontram problemas antes da entrega, e o artigo melhora de uma revisão para a outra? | A equipe cumpre os prazos necessários para a Entrega 1? |
| Conceito mensurável | Esforço da equipe | Eficácia das revisões | Progresso das unidades de trabalho |
| Entidades relevantes | Trabalho dos integrantes; planejamento de horas | Revisões do artigo; seções do artigo | Tarefas planejadas |
| Atributos | Registros de horas na planilha; horas declaradas como planejadas | Defeitos registrados; seções revisadas; correções feitas | Prazo e situação de cada tarefa |
| Medidas básicas | (1) Horas reais por integrante; (2) horas planejadas por integrante | (1) Defeitos confirmados; (2) seções revisadas; (3) defeitos corrigidos | (1) Tarefas com prazo até a data; (2) tarefas concluídas no prazo |
| Método de medição (tipo) | Somar os registros da planilha e as horas declaradas por integrante (objetivo) | Contar os defeitos confirmados pelo responsável (não houve reunião em 18/10 nem 21/10), as seções revisadas e as correções (objetivo) | Contar as tarefas com prazo até a data e as concluídas, confirmadas pelo responsável e consolidadas pelo responsável da categoria (objetivo) |
| Escala, tipo e unidade | Reais maiores ou iguais a 0; razão; hora | Inteiros maiores ou iguais a 0; razão; defeito e seção | Inteiros maiores ou iguais a 0; razão; tarefa |
| Medidas derivadas e função de medição | Desvio = (reais − planejadas) ÷ planejadas; participação = horas do integrante ÷ horas totais | Densidade = defeitos confirmados ÷ seções revisadas; taxa de correção = corrigidos ÷ confirmados | Conformidade = tarefas concluídas no prazo ÷ tarefas com prazo até a data |
| Indicador | Desvio total da equipe e participação de cada integrante | Densidade de defeitos por revisão e taxa de correção acumulada | Percentual de conformidade e lista das tarefas atrasadas |
| Modelo de análise | Comparar o desvio e as participações com os limites | Comparar a densidade entre revisões consecutivas | Comparar a conformidade com o limite |
| Critério de decisão | Desvio acima de 30% (indicador da equipe) leva a replanejar a carga; participação abaixo de 10% leva a redistribuir tarefas | Se a densidade não cair entre revisões, as seções com defeito passam por nova revisão antes da Entrega 1 | Conformidade abaixo de 70% leva a redistribuir as tarefas atrasadas |

As fontes de dados na Entrega 1 são a planilha de horas, as atas e os documentos de planejamento. Os dados de cada medição são salvos no repositório, na pasta [`gestao-psm`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/gestao-psm).

#### 3.2.2. Registro das Medições, Interpretação e Decisões

O processo de medição do PSM na Entrega 1 segue cortes semanais em **11/10, 18/10 e 25/10/2026**. Em cada categoria há um **coletor** (levanta os dados e grava o CSV em [`gestao-psm`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/gestao-psm)) e um **redator** (calcula o indicador, propõe interpretação e decisão e registra no artigo). As decisões constam nesta seção; não houve reunião em 18/10 nem em 21/10, de modo que confirmações pontuais de tarefas ou defeitos são feitas pelo responsável. Ainda não há *issues* no GitHub como fonte de dados.

| Categoria | Data do corte | Medidas básicas | Indicador | Critério | Decisão | Arquivo |
|---|---|---|---|---|---|---|
| Recursos e Custos | 11/10/2026 | \(H_{\mathrm{plan}}=20{,}67\) h; \(H_{\mathrm{real}}=11{,}98\) h | Desvio −42,0%; menor participação 2,8% | Desvio da **equipe** > 30% (sobrecarga) ou participação < 10% | Redistribuir (participação); corte julgado retrospectivamente com critérios de 18/10 | `gestao-psm/2026-10-11_recursos-custos.csv` |
| Recursos e Custos | 18/10/2026 | \(H_{\mathrm{plan}}=49{,}37\) h; \(H_{\mathrm{real}}=39{,}50\) h | Desvio −20,0%; menor participação 11,0% | Idem | Manter a carga; acompanhar desvios individuais < −30% (Mateus e Dante) | `gestao-psm/2026-10-18_recursos-custos.csv` |
| Recursos e Custos | 25/10/2026 | \(H_{\mathrm{plan}}=78{,}10\) h; \(H_{\mathrm{real}}=42{,}17\) h | Desvio −46,0%; menor participação 10,3% | Idem | Limiar de sobrecarga da equipe não acionado; acompanhar subutilização (Mateus −68,8%; Dante −64,7%) | `gestao-psm/2026-10-25_recursos-custos.csv` |
| Desempenho dos Processos | Revisão 1 | 13 defeitos; 9 seções; 8 corrigidos | \(D_1=1{,}44\) defeitos/seção; taxa de correção 61,5% | Densidade deve cair entre revisões antes da Entrega 1 | Revisão 2 com dados reais (sem inventar densidade) | Contagem da Revisão 1 |
| Calendário e Progresso | 11/10/2026 | \(T_p=16\); \(T_c=9\) | \(ICP=56{,}3\%\) | Conformidade < 70% | Redistribuir atrasos (inclui issues/milestones não criadas) | `gestao-psm/calendario-progresso.csv` |
| Calendário e Progresso | 18/10/2026 | \(T_p=14\); \(T_c=3\) | \(ICP=21{,}4\%\) | Conformidade < 70% | Redistribuir atrasos do Plano da Fase 2 | `gestao-psm/calendario-progresso.csv` |
| Calendário e Progresso | 25/10/2026 | \(T_p=15\); \(T_c=6\) | \(ICP=40{,}0\%\) | Conformidade < 70% | Redistribuir as 9 tarefas restantes | `gestao-psm/calendario-progresso.csv`; `gestao-psm/2026-10-25_calendario-progresso.csv` |

- **Recursos e Custos.** As medidas básicas foram extraídas da planilha de esforço. Conferiu-se o lançamento da Karolina em 07/10 (reunião, 0,33 h) e em 08/10 (GitPage, 1,75 h): atividades distintas, **sem duplicata indevida**. Nos cortes de 11/10, 18/10 e 25/10, o desvio da equipe foi de −42,0%, −20,0% e **−46,0%** (\(H_{\mathrm{plan}}=78{,}10\) h e \(H_{\mathrm{real}}=42{,}17\) h em 25/10), e a menor participação passou de 2,8% para 11,0% e 10,3%. O critério de desvio de 30% aplica-se ao indicador da *equipe* (sobrecarga); o corte de 11/10 foi julgado retrospectivamente com os critérios de 18/10. **Interpretação:** o desvio de −46,0% em 25/10 indica subutilização do esforço planejado, sem acionar o limiar de sobrecarga (+30%). **Decisão:** manter o acompanhamento da carga e dos desvios individuais inferiores a −30% (em especial Mateus e Dante).

- **Desempenho dos Processos.** Na Revisão 1 foram inspecionadas 9 seções e confirmados 13 defeitos (\(D_1=13/9=1{,}44\) defeitos/seção); 8 foram corrigidos (taxa 61,5%), restando 5. Conta-se como defeito informação incorreta ou sem fonte, divergência com decisão da equipe ou item da rubrica ausente, confirmado pelo responsável (não houve reunião em 18/10 nem 21/10). **Não se inventa densidade da Revisão 2** até a contagem da Revisão 2. **Decisão:** executar a Revisão 2 com dados reais antes da Entrega 1.

- **Calendário e Progresso.** As medidas \(T_p\) e \(T_c\) cruzam atribuições pós-reunião 01, Plano da Fase 2, documento de pendências da Entrega 1, planilha e atas. Quem confirma a conclusão é o responsável da tarefa, consolidado pelo responsável da categoria. A tarefa de criar repositório/*issues*/*milestones* conta como **fora do prazo**: o repositório existe, mas a API do GitHub registrou **0 issues** em 25/10/2026. Nos cortes de 11/10, 18/10 e 25/10 obteve-se \(ICP=56{,}3\%\), \(21{,}4\%\) e \(40{,}0\%\) — todos abaixo de 70%. Em 25/10, \(T_c=6\) (B1 formato IEEE; A1 ISO 2023; A2 GQM Capacidade de interação; A3 Recursos; A4 rastreamento; A5 Apêndice/GitPage). **Decisão:** redistribuir as 9 tarefas ainda pendentes até a Entrega 1.

### 3.3. Declaração de Uso de Inteligência Artificial

A equipe utilizou ferramentas de Inteligência Artificial (IA) como apoio durante a Entrega 1: na estruturação e formatação do código LaTeX no template da SBC; na revisão textual e na tradução de termos técnicos e de artigos científicos; na análise do repositório do Anki; na redação de rascunhos das seções da Fase 1, dos objetivos GQM e dos construtos do PSM; e na produção das atas a partir das transcrições das reuniões. Todo o conteúdo gerado foi revisado pela equipe em reunião e conferido com os materiais da disciplina (aulas sobre processo de avaliação, GQM e PSM); as decisões de escopo, a escolha das métricas e os critérios de julgamento foram tomados pela equipe.

## 4. Fase 1 — Estabelecer os Requisitos de Avaliação

### 4.1. Propósito da Avaliação e Uso Pretendido

A avaliação foi solicitada pela professora da disciplina de Qualidade de Software 1, que atua como requisitante. O objetivo da avaliação é indicar pontos de melhoria no produto, sob o ponto de vista do estudante, usuário final do Anki.

Os pontos de melhoria identificados serão usados pela professora para avaliar a capacidade da equipe de fundamentar tecnicamente uma avaliação de produto. Serão também registrados como recomendações priorizadas para dois públicos: os mantenedores do Anki, que podem usá-los para decidir correções, e os estudantes, que podem usá-los como orientação de uso. O ponto de melhoria mais relevante será a base da ação de melhoria da Entrega 2.

### 4.2. Requisitante e Partes Interessadas

A Tabela 2 apresenta as partes interessadas, suas necessidades e a influência de cada uma nas escolhas da avaliação.

*Tabela 2. Partes interessadas na avaliação*

| Parte interessada | Papel | Necessidade | Influência na avaliação |
|---|---|---|---|
| Professora da disciplina | Requisitante | Uma avaliação fundamentada e rastreável | Acordou as características avaliadas e define prazos e formato |
| Estudante | Usuário final (operador) | Usar o Anki sozinho, sem lentidão, em qualquer sistema | Define o ponto de vista, as tarefas dos testes e os critérios de julgamento |
| Mantenedores do Anki | Desenvolvedor e fornecedor | Problemas descritos de forma reproduzível e priorizada | Limitam o escopo ao que é observável e ao código aberto; o AnkiWeb é de código fechado |
| Equipe avaliadora | Avaliador | Um escopo viável no prazo | Define as plataformas e a profundidade da avaliação |

### 4.3. Tipo de Produto e Descrição do Software

O produto avaliado é o Anki Desktop, versão 26.09.3, e o AnkiWeb, na versão em produção na data da avaliação, com a data de acesso registrada; o AnkiWeb é avaliado apenas na criação de conta, no login e na sincronização. O domínio é a educação, com estudo por repetição espaçada. Na classificação de Pressman, o Anki é um software de computador pessoal; na IEEE 1062, é um produto COTS, gratuito e de código aberto, e o AnkiWeb é um serviço gratuito de código fechado. Os principais usuários são estudantes universitários e autodidatas; o uso exige conhecimento básico de informática e nenhum conhecimento prévio de repetição espaçada. O uso é individual, em computador pessoal com Windows, macOS ou Ubuntu, sem treinamento formal nem suporte técnico; o estudo funciona sem internet, mas conta, login e sincronização exigem conexão.

O Anki Desktop possui oito funções principais: login na conta AnkiWeb; criação de baralhos; escrita de cards; revisão de cards, na qual o estudante avalia a própria resposta e o agendamento define quando o card volta; busca e edição no navegador de cards; importação e exportação; sincronização; e configuração das opções de estudo. A avaliação dedica-se principalmente à criação de baralhos, à escrita e à revisão de cards, ao login e à sincronização. A interface possui 16 janelas principais, como a janela principal, Adicionar, Navegador de cards, Opções do baralho, Importar, Exportar e Login de sincronização.

Há massa de dados de duas fontes: coleções sintéticas geradas com o pacote `anki` (por exemplo, 10 mil, 50 mil e 100 mil cards), para Eficiência de desempenho e Flexibilidade; e baralhos compartilhados no AnkiWeb, para os testes de Capacidade de interação. Os requisitos de software declarados pelo fabricante (apps.ankiweb.net e docs.ankiweb.net, consultados em 14/10/2026) são: Windows 10 versão 1703 ou posterior (x64) ou Windows 11 (ARM); macOS 13 ou posterior, em Apple Silicon ou Intel; distribuição Linux de 2022 ou posterior (x64, glibc 2.35+) ou de 2024 ou posterior (ARM, glibc 2.39+), com o pacote `zstd`; e, para o AnkiWeb, navegador atualizado e internet. Não há requisitos mínimos de memória ou processador.

### 4.4. Modelo de Qualidade

O modelo de qualidade da ISO/IEC 25010:2023 foi adaptado ao Anki a partir dos componentes do produto submetidos à avaliação (Figura 1). A adaptação mapeia as características da norma, que são abstratas, para os componentes com os quais o estudante interage e restringe o escopo às subcaracterísticas mostradas na figura: a instalação e desinstalação, para a **Flexibilidade** (adaptabilidade, instalabilidade e substituibilidade); a interface gráfica e a revisão de cards, para a **Capacidade de interação** (reconhecibilidade da adequação, facilidade de aprendizado e operabilidade); a execução nos diferentes sistemas operacionais, para a **Eficiência de desempenho** e a **Flexibilidade**; e o fluxo de conta e sincronização do AnkiWeb, para as três características.

![Modelo de qualidade adaptado ao Anki Desktop e ao AnkiWeb](assets/modelo-qualidade.png)

*Figura 1. Modelo de qualidade adaptado ao Anki Desktop e ao AnkiWeb, a partir da ISO/IEC 25010:2023 [ISO/IEC 2023a]. De cima para baixo: componentes avaliados, características e subcaracterísticas.*

### 4.5. Seleção e Priorização das Características

A ênfase de cada característica foi definida pela combinação do impacto para o estudante (quanto uma falha atrapalha o uso) com a viabilidade de medição com os recursos e o prazo da equipe (Tabela 3). A escolha de Capacidade de interação foi acordada com a requisitante, e as seis características não escolhidas ficam fora do escopo por acordo com ela.

*Tabela 3. Priorização das características avaliadas*

| Característica | Impacto para o estudante | Viabilidade de medição | Ênfase |
|---|---|---|---:|
| Capacidade de interação | Alto: todo estudante usa a interface sem treinamento | Média: exige testes com participantes | 5 |
| Eficiência de desempenho | Médio: notebooks variados e coleções que crescem | Alta: medições instrumentadas | 3 |
| Flexibilidade | Médio: estudantes usam sistemas diferentes e trocam de computador | Alta: instalação e migração controladas | 3 |

### 4.6. Escopo, Profundidade e Objetos da Avaliação

**Objetos e abrangência.** Instalação e desinstalação, interface do usuário e execução do Anki Desktop 26.09.3, e criação de conta, login e sincronização no AnkiWeb; três características da ISO/IEC 25010:2023 (Capacidade de interação, Eficiência de desempenho e Flexibilidade), nas plataformas Windows, macOS e Ubuntu. As subcaracterísticas avaliadas são as da Figura 1: reconhecibilidade da adequação, facilidade de aprendizado e operabilidade; comportamento no tempo, utilização de recursos e capacidade; adaptabilidade, instalabilidade e substituibilidade.

**Profundidade.** Avaliação externa, do ponto de vista do estudante, baseada no comportamento observável, por meio de testes com usuários, medições instrumentadas e inspeção da interface. O código-fonte do Anki Desktop serve apenas como apoio; o AnkiWeb, de código fechado, é avaliado só pelo comportamento. Não se trata de certificação nem de laudo de conformidade.

**Relacionamento e restrições.** Avaliação independente, com a documentação oficial como referência; prazo até 18/11/2026, seis avaliadores, sem custo, apenas computadores da equipe e participantes com consentimento registrado.

**Fora do escopo.** AnkiDroid e AnkiMobile (produtos e bases de código separados); o algoritmo de agendamento (exigiria acompanhar usuários por semanas); as demais funções do AnkiWeb; as demais subcaracterísticas das três características escolhidas que não aparecem na Figura 1; e as seis características não escolhidas, por acordo com a requisitante.

### 4.7. Relação com os Objetivos de Desenvolvimento Sustentável

A avaliação se relaciona ao ODS 4, Educação de Qualidade. Na **meta 4.3** (acesso igualitário à educação superior de qualidade, a preços acessíveis), o Anki Desktop é gratuito e apoia o estudo autônomo. Na **meta 4.4** (jovens e adultos com habilidades relevantes), o indicador 4.4.1, sobre habilidades em tecnologias da informação e comunicação, relaciona-se à facilidade de aprendizado avaliada em Capacidade de interação. Na **meta 4.5** (eliminar disparidades e garantir acesso a pessoas em situação de vulnerabilidade), relaciona-se à Flexibilidade e aos aspectos de inclusão da interface. Pontos de melhoria que reduzem barreiras de uso ampliam o alcance de uma ferramenta gratuita de estudo.

## 5. Fase 2 — Especificar a Avaliação

Esta seção especifica a avaliação por meio do GQM [Basili et al. 1994]. Para cada característica priorizada na Fase 1, apresentam-se o objetivo de medição, as questões e hipóteses, os fatores de variação, as métricas e os níveis de pontuação com os critérios de julgamento. Os níveis seguem quatro faixas comuns às três características: *insatisfatório*, *mínimo*, *alvo* e *excelente*. A Seção 5.4 reúne a hierarquia GQM completa, e a Seção 5.5 explicita a ligação entre as Fases 1 e 2.

### 5.1. Capacidade de interação (antiga Usabilidade)

A equipe selecionou três subcaracterísticas: **reconhecibilidade da adequação**, porque o Anki usa conceitos próprios (nota, tipo de nota, card e baralho) e o estudante precisa perceber quais funções atendem ao que quer fazer; **facilidade de aprendizado**, porque a Fase 1 definiu o uso sem treinamento nem suporte; e **operabilidade**, porque quem já usa o Anki repete as mesmas tarefas diariamente. Os testes envolvem dois grupos definidos por triagem: iniciantes (Grupo A), que respondem principalmente a Q1 e Q2, e usuários frequentes (Grupo B), que respondem a Q3 e servem de comparação em H3.

#### 5.1.1. Objetivo de Medição

O objetivo G1 segue o template do GQM [Basili et al. 1994], com as decisões comuns da equipe (ISO/IEC 25010:2023, GQM, faixas insatisfatório/mínimo/alvo/excelente e ponto de vista do estudante da Fase 1).

| Template GQM | Capacidade de interação |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 e o fluxo de criação de conta, login e sincronização do AnkiWeb |
| **para o propósito de** | entender, identificando pontos de melhoria |
| **com respeito a** | reconhecibilidade da adequação, facilidade de aprendizado e operabilidade |
| **do ponto de vista do** | estudante, usuário final (iniciante e usuário frequente) |
| **no contexto de** | uso individual em computador pessoal, sem treinamento formal |

#### 5.1.2. Grupos de participantes e triagem

**Grupo A — Usuários iniciantes.** Participantes que nunca utilizaram o Anki antes do estudo. Não devem ter experiência prática anterior com as tarefas avaliadas no Anki Desktop ou no AnkiWeb. O uso de outros aplicativos de flashcards é registrado separadamente, pois pode influenciar a aprendizagem.

**Grupo B — Usuários frequentes.** Participantes que utilizaram o Anki regularmente durante as últimas quatro semanas, preferencialmente em pelo menos três dias por semana, e que já realizaram as tarefas centrais avaliadas: criar baralhos e cartões, revisar cartões e sincronizar com o AnkiWeb.

Antes da entrevista ou do preenchimento do formulário de avaliação, a pessoa responde ao formulário de triagem: (1) já utilizou o Anki (nunca / experimentou uma ou duas vezes / já utilizou regularmente); (2) nos últimos 7 dias, em quantos dias utilizou (nenhum / 1–2 / 3–4 / 5–7); (3) há quanto tempo utiliza regularmente (nunca / menos de 4 semanas / 4 semanas a 3 meses / mais de 3 meses); (4)–(6) já criou baralhos e cartões, já revisou e já sincronizou Desktop–AnkiWeb (sim/não); (7) já utilizou outros aplicativos de flashcards (sim/não); (8) familiaridade geral com informática (baixa/média/alta). A classificação no Grupo A ou B segue essas respostas.

#### 5.1.3. Questões e Hipóteses

*Tabela 4. Questões e hipóteses de Capacidade de interação*

| Questão | Hipótese |
|---|---|
| **Q1** (Reconhecibilidade da adequação): um estudante que nunca usou o Anki consegue identificar, pela interface, quais funções usar para criar seus cards e estudar? | **H1:** no Grupo A, \(T_{rf}\) das funções principais (criar baralho, adicionar cards e estudar) fica em *alvo* ou *excelente*; nota, tipo de nota e card ficam em *mínimo* ou *insatisfatório*. |
| **Q2** (Facilidade de aprendizado): um estudante iniciante consegue aprender, sem ajuda, a criar uma conta no AnkiWeb, criar um baralho, adicionar cards, revisá-los e sincronizar a coleção? | **H2:** no Grupo A, \(T_{sa}\) e \(T_{\mathrm{aprend}}\) em baralho, cards e revisão ficam em *alvo* ou *excelente*; conta e primeira sincronização ficam em *mínimo* ou *insatisfatório*. |
| **Q3** (Operabilidade): as tarefas do estudo diário podem ser executadas com pouco esforço por quem já usa o Anki? | **H3:** no Grupo B, \(T_{ct}\) e \(T_{\mathrm{exec}}\) em revisar e adicionar cards ficam em *alvo* ou *excelente*; a diferença \(\lvert\Delta\rvert\) entre Grupos A e B (médias de \(T_{ct}\) e \(T_{\mathrm{exec}}\)) é maior em conta e sincronização do que em revisar e adicionar cards. |

#### 5.1.4. Fatores de Variação

Três fatores, obtidos na triagem e no perfil, podem influenciar os resultados: **familiaridade com informática** (ordinal: baixa, média ou alta) afeta H2 e H3 via tempos e ajudas em conta e sincronização; **experiência prévia com aplicativos de flashcards** (nominal) afeta H1 (reconhecimento de funções); e **sistema operacional** (nominal) afeta H2 e H3 via \(T_{\mathrm{exec}}\).

#### 5.1.5. Métricas

A Tabela 5 resume as seis métricas do escopo (Plano de Medição, Aula 08). Todas são de escala de razão e coletadas em sessões observadas com consentimento registrado. Cada métrica indica a referência acadêmica de origem; \(T_{rf}\) e \(R_t\) têm operacionalização própria, relacionada às referências citadas.

*Tabela 5. Métricas de Capacidade de interação: definição, cálculo, referência e faixa*

| Métrica | Q | Definição / cálculo | Referência de origem | Faixa |
|---|---|---|---|---|
| Taxa de reconhecimento de funções (\(T_{rf}\)) | Q1 | % de iniciantes que indicam a função correta; \(N_{\mathrm{reconh.}}/N_{\mathrm{part.}} \times 100\%\) (operacionalização própria) | Relacionada a Sellier et al. [Sellier et al. 2024] | 0–100% |
| Tempo de aprendizagem (\(T_{\mathrm{aprend}}\)) | Q2 | Média do tempo total do Grupo A no roteiro completo | Vogel et al. [Vogel et al. 2021] | > 0 min |
| Taxa de sucesso após aprendizagem (\(T_{sa}\)) | Q2 | \(\displaystyle T_{sa}=\frac{N_{\text{tentativas concluídas com sucesso}}}{N_{\text{tentativas realizadas}}}\times 100\%\) | Bird et al. [Bird et al. 2022] | 0–100% |
| Redução do tempo de execução (\(R_t\)) | Q2 | \((t_1 - t_2)/t_1 \times 100\%\) (operacionalização própria) | Relacionada a Marrella e Catarci [Marrella e Catarci 2018] | pode ser < 0 |
| Taxa de conclusão de tarefas (\(T_{ct}\)) | Q3 | % concluídas por grupo; \(N_{\mathrm{concluídas}}/N_{\mathrm{propostas}} \times 100\%\) | Bird et al. [Bird et al. 2022] | 0–100% |
| Tempo de execução da tarefa (\(T_{\mathrm{exec}}\)) | Q3 | Média do tempo da pessoa do recebimento da tarefa até o sucesso (também mediana), por tarefa e grupo | Bird et al. [Bird et al. 2022] | > 0 min |

#### 5.1.6. Níveis de Pontuação e Critérios de Julgamento

Os níveis da Tabela 6 foram fixados antes da coleta. Os limites de \(T_{\mathrm{exec}}\) medem o tempo da pessoa para concluir a tarefa e foram definidos por acordo da equipe (os limiares de 3, 9 e 12 s de Hoxmeier e DiCesare [Hoxmeier e DiCesare 2000] aplicam-se ao tempo de resposta do sistema na Eficiência de desempenho, não a estas tarefas). Os demais limites também foram definidos por acordo da equipe, por falta de dados históricos do Anki.

*Tabela 6. Níveis de pontuação das métricas de Capacidade de interação*

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| \(T_{rf}\) (Q1) | abaixo de 60% | 60% a 75% | 75% a 90% | 90% ou mais |
| \(T_{\mathrm{aprend}}\) (Q2) | acima de 40 min ou abandono | 25 a 40 min | 15 a 25 min | menos de 15 min |
| \(T_{sa}\) (Q2) | abaixo de 60% ou intervenção recorrente | 60% a 75% | 75% a 90% sem ajuda, ou 90% ou mais com uma ajuda | 90% ou mais sem ajuda |
| \(R_t\) (Q2) | abaixo de 5% ou negativa | 5% a 20% | 20% a 40% | 40% ou mais |
| \(T_{ct}\), frequentes (Q3) | abaixo de 80% ou abandono | 80% a 90%, ou 100% com uma ajuda | 90% ou mais sem ajuda | 100% sem ajuda |
| \(T_{\mathrm{exec}}\) (Q3) | acima de 10 min ou falha | 5 a 10 min | 2 a 5 min | menos de 2 min |

**Regra de julgamento.** O julgamento procede de baixo para cima [Basili et al. 1994]: cada métrica é classificada em uma faixa, as faixas são agregadas por questão e as questões respondem ao G1. Uma questão é atendida quando suas métricas essenciais (\(T_{rf}\) em Q1; \(T_{sa}\) e \(T_{\mathrm{aprend}}\) em Q2; \(T_{ct}\) e \(T_{\mathrm{exec}}\) em Q3) estão no alvo ou acima; havendo divergência, prevalece a faixa mais baixa, e \(R_t\) serve de evidência de apoio. H1–H3 são julgadas pelos valores esperados da Tabela 4. Os fatores de variação não alteram os limites, mas são reportados na interpretação. As faixas mínimo e insatisfatório tornam-se recomendações priorizadas, e a mais relevante alimenta a ação de melhoria da Entrega 2.

### 5.2. Eficiência de Desempenho

#### 5.2.1. Objetivo de Medição

O objetivo segue o template do GQM [Basili et al. 1994], com o ponto de vista definido na Fase 1.

| Template GQM | Eficiência de desempenho |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 e a sincronização com o AnkiWeb |
| **para o propósito de** | entender, identificando pontos de melhoria |
| **com respeito a** | comportamento no tempo, utilização de recursos, capacidade e eficiência a nível de threads |
| **do ponto de vista do** | estudante, usuário final (operador) |
| **no contexto de** | uso individual em computador pessoal com Windows, macOS ou Ubuntu |

#### 5.2.2. Questões e Hipóteses

*Tabela 7. Questões e hipóteses de Eficiência de desempenho*

| Questão | Hipótese |
|---|---|
| **Q1** (Comportamento no tempo): quais ações do estudante no Anki Desktop levam mais tempo para responder: abrir o aplicativo, iniciar a revisão ou sincronizar? | **H1:** a sincronização é a ação mais demorada, e abrir o aplicativo e iniciar a revisão respondem em menos de 3 segundos. |
| **Q2** (Utilização de recursos): como o uso de CPU e de memória RAM varia entre o cenário de repouso e o cenário de estresse? | **H2:** o consumo de CPU e de RAM é maior no estresse do que no repouso, mantendo-se dentro da faixa esperada para aplicações PyQt. |
| **Q3** (Capacidade): como o aumento da quantidade de cards influencia o tempo de processamento e a resposta do Anki Desktop? | **H3:** o aumento de cards eleva gradualmente o tempo de carregamento e o consumo de memória, sem tornar o estudo perceptivelmente lento. |
| **Q4** (Eficiência a nível de threads): durante operações intensivas de banco de dados e sincronização, o processamento pesado permanece nas *Worker Threads* (Rust) sem bloquear a *Main Thread* (UI Qt)? | **H4:** o backend em Rust absorve a carga de I/O e de CPU, mantendo a *Main Thread* livre de contenção e evitando o congelamento da interface. |

#### 5.2.3. Métricas

As métricas que respondem a Q1 a Q4 estão na Tabela 8; todas são de escala de razão, e os procedimentos seguem Hoxmeier e DiCesare [Hoxmeier e DiCesare 2000], Pereira et al. [Pereira et al. 2023], Rojas et al. [Rojas et al. 2025] e Milichiewicz e Badurowicz [Milichiewicz e Badurowicz 2025].

*Tabela 8. Métricas de Eficiência de desempenho: faixas e meios de coleta*

| Métrica | Questão | Faixa de valores | Meio de coleta |
|---|---|---|---|
| Tempo de inicialização (*cold* e *warm start*) | Q1 | acima de 0 s | Script automatizado (`time` / `perf stat`) até abrir a janela principal |
| Tempo para iniciar revisão e exibir resposta | Q1, Q3 | acima de 0 s | `perf trace` e registro de eventos de UI |
| Tempo de sincronização | Q1 | acima de 0 s | Cronometragem do início ao fim da sincronização com o AnkiWeb |
| Tempo de carregamento da coleção | Q1, Q3 | acima de 0 s | Tempo de leitura do banco `.anki2` (SQLite) |
| Uso médio e de pico de CPU | Q2 | 0 a 100% | `pidstat -u 1`, Monitor de Atividade e Gerenciador de Tarefas |
| Uso médio e de pico de RAM | Q2, Q3 | acima de 0 MB | RSS estabilizada após 5 min via `pidstat -r 1` / `psutil` |
| Vazão de processamento | Q3 | acima de 0 cards/min (10k, 50k e 100k) | Script em Python com o pacote `anki` e *Check Database* |
| Uso de CPU por thread | Q4 | 0 a 100% | `pidstat -t -u 1` no Linux (*Main Qt*, *Worker Rust* e *WebEngine*) |
| Trocas de contexto por thread | Q4 | 0 ou mais trocas/s | `pidstat -t -w 1` no Linux (`cswch/s` e `nvcswch/s`) |
| Taxa de I/O em disco por thread | Q3, Q4 | 0 ou mais kB/s | `pidstat -t -d 1` no Linux (leitura e escrita no SQLite) |

#### 5.2.4. Fatores de Variação

São registrados antes dos testes: a **configuração de hardware** (processador, núcleos, RAM e tipo de disco), que afeta tempos e disputa entre threads (Q1 a Q4); o **sistema operacional e o servidor gráfico** (Windows 11, macOS ou Ubuntu com X11/Wayland), que alteram memória, CPU e renderização [Milichiewicz e Badurowicz 2025]; o **porte da coleção** (10, 50 e 100 mil cards), que eleva memória e I/O (Q2 a Q4); e as **condições de rede e processos em segundo plano**, que afetam a sincronização (Q1) e as preempções involuntárias (Q2 e Q4).

#### 5.2.5. Níveis de Pontuação e Critérios de Julgamento

Os níveis da Tabela 9 baseiam-se nos limiares de tempo de resposta de Hoxmeier e DiCesare [Hoxmeier e DiCesare 2000], adotados em avaliações ISO/IEC 25010 [Sukmandari e Sukardiyono 2017; Jayanto e Jati 2017], no perfil de recursos de aplicações PyQt [Milichiewicz e Badurowicz 2025] e em estudos de eficiência sob carga [Pereira et al. 2023; Rojas et al. 2025].

*Tabela 9. Níveis de pontuação de Eficiência de desempenho*

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Tempos de resposta (Q1) | acima de 12 s, falha ou *timeout* | 9 a 12 s | 3 a 9 s | menos de 3 s |
| Memória RAM (Q2) | acima de 800 MB ou crescimento contínuo | 500 a 800 MB no estresse | 150 a 250 MB em repouso; até 500 MB no estresse | até 150 MB em repouso; até 350 MB no estresse |
| CPU (Q2) | acima de 5% em repouso | picos de 70% a 90% | até 5% em repouso; 40% a 70% no estresse | até 2% em repouso; até 40% no estresse |
| Capacidade com 100 mil cards (Q3) | acima de 12 s, degradação acima de 60% ou falha no SQLite | 9 a 12 s; degradação de 35% a 60% | 3 a 9 s; degradação de 15% a 35% | menos de 3 s; degradação abaixo de 15% |
| Threads (Q4) | *Main Thread* com 80% de CPU ou mais, ou congelamento | *Main Thread* até 60%; 10 a 50 trocas involuntárias/s; travamento até 1 s | *Main Thread* de 15% a 35%, sem atraso perceptível | *Main Thread* abaixo de 15%; menos de 10 trocas involuntárias/s; sem congelamento |

### 5.3. Flexibilidade (antiga Portabilidade)

#### 5.3.1. Objetivo de Medição

O objetivo segue o template do GQM [Basili et al. 1994], com o ponto de vista definido na Fase 1.

| Template GQM | Flexibilidade |
|---|---|
| **Analisar** | o Anki Desktop 26.09.3 (instalação, adaptação e substituição de dados) |
| **para o propósito de** | entender, identificando pontos de melhoria |
| **com respeito a** | adaptabilidade, instalabilidade e substituibilidade |
| **do ponto de vista do** | estudante, usuário final |
| **no contexto de** | uso individual em computador pessoal, nas plataformas Windows, macOS e Ubuntu |

#### 5.3.2. Questões e Hipóteses

*Tabela 10. Questões e hipóteses de Flexibilidade*

| Questão | Hipótese |
|---|---|
| **Q1** (Instalabilidade): o processo de instalação e desinstalação do Anki Desktop ocorre de forma simples e livre de erros nas três plataformas? | **H1:** as instalações via pacote (Windows e macOS) são rápidas e intuitivas, enquanto a instalação no Ubuntu, via script, pode exigir mais intervenções e apresentar maior taxa de falha. |
| **Q2** (Adaptabilidade): o Anki Desktop se adapta às características nativas de cada sistema operacional (atalhos, tema escuro, bandeja)? | **H2:** a adaptação é excelente no macOS e no Windows, mas apresenta falhas pontuais de integração visual (tema escuro) e de associação de arquivos no Ubuntu. |
| **Q3** (Substituibilidade): a migração de dados (exportação, importação e sincronização) preserva a integridade das informações ao trocar de máquina ou versão? | **H3:** a migração via arquivos `.apkg` e AnkiWeb preserva 100% da integridade dos dados. |

#### 5.3.3. Fatores de Variação

São registrados: o **sistema operacional** (Windows, macOS ou Ubuntu), com maior tempo esperado no Ubuntu por causa de dependências como o `zstd`; a **arquitetura do processador** (x64 ou ARM); e a **permissão de administrador** (sim ou não), cuja ausência pode inviabilizar a instalação ou exigir intervenções.

#### 5.3.4. Métricas

As métricas estão na Tabela 11. A integração com o sistema operacional usa um checklist de 10 critérios derivado de Milichiewicz e Badurowicz [Milichiewicz e Badurowicz 2025] (bandeja do sistema, atalhos globais, associação de arquivos `.apkg`, diálogos nativos e tema escuro), de escala ordinal; as demais métricas são de escala de razão.

*Tabela 11. Métricas de Flexibilidade: faixas e meios de coleta*

| Métrica | Faixa | Meio de coleta |
|---|---|---|
| Taxa de execução multiplataforma (%) | 0 a 100 | Registro da execução das funcionalidades nas três plataformas |
| Taxa de preservação funcional (%) | 0 a 100 | Comparação das funcionalidades nos ambientes de origem e destino |
| Taxa de preservação de dados (%) | 0 a 100 | Inspeção do banco SQLite (DB Browser) |
| Tempo de adaptação/configuração (min) | acima de 0 | Medição do tempo de adaptação e configuração |
| Taxa de instalação bem-sucedida (%) | 0 a 100 | Formulário de observação do avaliador |
| Tempo de instalação (min) | acima de 0 | Cronômetro |
| Número de intervenções necessárias | inteiro maior ou igual a 0 | Formulário de observação |
| Taxa de falhas de instalação (%) | 0 a 100 | Registro das tentativas de instalação |
| Taxa de substituição bem-sucedida (%) | 0 a 100 | Verificação do funcionamento após a substituição |
| Tempo de substituição (min) | acima de 0 | Medição do tempo de substituição |
| Integridade pós-substituição (%) | 0 a 100 | Inspeção do banco SQLite (DB Browser) |
| Integração com o sistema (pontos) | 0 a 10 | Checklist de 10 critérios |

#### 5.3.5. Níveis de Pontuação e Critérios de Julgamento

Os níveis da Tabela 12 foram definidos por acordo da equipe, com base nas metas de aceitação do projeto.

*Tabela 12. Níveis de pontuação de Flexibilidade*

| Subcaracterística | Insatisfatório | Mínimo | Alvo | Excelente |
|---|---|---|---|---|
| Instalabilidade (Q1) | Falha na instalação | Sucesso após uma intervenção | 100% de sucesso, entre 2 e 5 min | 100% de sucesso, em menos de 2 min |
| Adaptabilidade (Q2) | Menos de 6/10 no checklist | 6 ou 7/10 | 8 ou 9/10 | 10/10 |
| Substituibilidade (Q3) | Perda de dados | — | 100% de integridade, em mais de 1 min | 100% de integridade, em menos de 1 min |

### 5.4. Diagrama GQM

A Figura 2 apresenta a hierarquia GQM da avaliação: os três objetivos no nível conceitual, as questões no nível operacional e as métricas no nível quantitativo, cada uma acompanhada da questão que responde.

![Hierarquia GQM da avaliação](assets/diagrama-gqm.png)

*Figura 2. Hierarquia GQM da avaliação: objetivos, questões e métricas de Capacidade de interação, Eficiência de desempenho e Flexibilidade.*

### 5.5. Coerência entre as Fases 1 e 2

A Fase 1 delimitou o escopo, sob o ponto de vista do estudante, em quatro componentes: a interface do Anki Desktop, sua execução em Windows, macOS e Ubuntu, a instalação e o fluxo de conta e sincronização do AnkiWeb. A Fase 2 mantém nos três objetivos esse ponto de vista e a priorização da Fase 1 (Capacidade de interação com ênfase 5, as demais com 3): as questões de **Capacidade de interação** avaliam a interação com a interface e com o fluxo de conta e sincronização; as métricas de **Eficiência de desempenho** medem a execução e a fluidez do estudo; e as de **Flexibilidade** cobrem a instalação e a migração entre as três plataformas.

## 6. Considerações Finais e Próximos Passos

Este artigo apresentou as Fases 1 e 2 da avaliação do Anki Desktop e do AnkiWeb: os requisitos da avaliação, sob o ponto de vista do estudante, e a especificação por meio do GQM, com métricas, níveis de pontuação e critérios de julgamento para Capacidade de interação, Eficiência de desempenho e Flexibilidade, além da gestão do projeto com o PSM. Após a revisão do Ponto de Controle 1, as Fases 1 e 2 serão consolidadas na Entrega 1 (26/10/2026); o plano de avaliação (Fase 3) será apresentado no Ponto de Controle 2 (04/11/2026); e a execução, o julgamento e a ação de melhoria, na Entrega 2 (18/11/2026).

## Referências

Basili, V. R., Caldiera, G. e Rombach, H. D. (1994). The Goal Question Metric approach. In Marciniak, J. J., editor, *Encyclopedia of Software Engineering*, p. 528–532. John Wiley & Sons.

Bird, M., Carter, N., Lim, A., Kazmie, N., Fajardo, C., Reaume, S. e McGillion, M. H. (2022). A novel hospital-to-home system for children with medical complexities: Usability testing study. *JMIR Formative Research*, 6(8):e34572.

Galin, D. (2018). *Software Quality: Concepts and Practice*. John Wiley & Sons, IEEE Press, New York, NY.

Hoxmeier, J. A. e DiCesare, C. (2000). System response time and user satisfaction: An experimental study of browser-based applications. In *Proceedings of AMCIS 2000*, p. 1–6.

ISO/IEC (2023a). *ISO/IEC 25010:2023: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. International Organization for Standardization, Geneva.

ISO/IEC (2023b). *ISO/IEC 25040:2023: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*. International Organization for Standardization, Geneva.

Jayanto, R. D. e Jati, H. (2017). Evaluasi kualitas aplikasi mobile kamus istilah jaringan pada platform android dengan standar ISO/IEC 25010. *Elinvo (Electronics, Informatics, and Vocational Education)*, 2(2):178–183.

Lund, A. M. (2001). Measuring usability with the USE Questionnaire. *Usability Interface*, 8(2):3–6.

Marrella, A. e Catarci, T. (2018). Measuring the learnability of interactive systems using a Petri net based approach. In *Proceedings of the 2018 Designing Interactive Systems Conference (DIS '18)*, p. 1309–1319. ACM, New York, NY.

McGarry, J., Card, D., Jones, C., Layman, B., Clark, E., Dean, J. e Hall, F. (2002). *Practical Software Measurement: Objective Information for Decision Makers*. Addison-Wesley, Boston, MA.

Milichiewicz, R. e Badurowicz, M. (2025). Comparative analysis of cross-platform application development tools in terms of operating system integration. *Journal of Computer Science Institute*, 36:357–364.

Pereira, D. S., Bezerra, L. F. V., Nunes, J. S., Barroca Filho, I. M. e Lopes, F. A. S. (2023). Performance efficiency evaluation based on ISO/IEC 25010:2011 applied to a case study on load balance and resilient. In *Anais do Workshop de Desempenho (WPerformance / CSBC)*, p. 1–13. SBC.

Practical Software and Systems Measurement (2021). *PSM Continuous Iterative Development Measurement Framework*, Partes 1, 2 e 3.

Rojas, H., Renteria, R. e Martinez, V. (2025). Understanding performance efficiency in ISO/IEC 25000: A systematic literature review. *International Journal on Informatics Visualization (JOIV)*, 9(6):2405–2417.

Sellier, Q., Sluÿters, A., Vanderdonckt, J. e Poncin, I. (2024). Evaluating gesture user interfaces: Quantitative measures, qualitative scales, and method. *International Journal of Human-Computer Studies*, 186:103245.

Sukmandari, D. G. e Sukardiyono, T. (2017). Analisis aplikasi jadwal perkuliahan berbasis android berdasarkan standar ISO 25010. *Elinvo (Electronics, Informatics, and Vocational Education)*, 2(1):80–84.

Vogel, M., Knapik, P., Cohrs, M., Szyperrek, B., Pueschel, W., Etzel, H., Fiebig, D., Rausch, A. e Kuhrmann, M. (2021). Metrics in automotive software development: A systematic literature review. *Journal of Software: Evolution and Process*, 33(2):e2296.

## Apêndice A. Tabela de Contribuição da Equipe

*Tabela 13. Contribuição de cada integrante para a Entrega 1 (planilha de horas, registros até 25/10/2026; total de 42,17 horas reais)*

| Integrante | Dupla | Atividades realizadas | Esforço (%) |
|---|---|---|---:|
| Bryan Smith Rodrigues Cavalcante | C | Reuniões; tabela GQM de Flexibilidade, fatores de variação e detalhamento das métricas | 10,3 |
| Dante Fernandes Scarpati | C | Reuniões; diagramas do modelo de qualidade e do GQM; métricas de Flexibilidade; slides | 12,6 |
| Davi Severiano Freitas | A | Reuniões, atas e organização do trabalho; Fase 1; slides 1 a 5; revisão do artigo; PSM Recursos (corte 25/10) | 30,0 |
| Karolina Vieira Barbosa | B | Reuniões; estrutura e atualizações da GitPage; estudo de Desempenho dos Processos; ajustes no Overleaf | 18,4 |
| Mateus de Siqueira Silva | B | Layout e textos iniciais do artigo; estudo de Desempenho dos Processos; busca de artigos de referência | 11,9 |
| Pedro Henrique Freire Rodrigues | A | Reuniões; termo de consentimento; métricas e níveis de Capacidade de interação; slides 9 e 10; rastreamento PSM | 16,9 |
| **Total** | | | **100** |