# Planejamento da Entrega 2 (Fases 3 e 4)

Equipe Betty Snyder · FGA0315 · Versão 1.0 de 04/11/2026 · Responsável: Davi Severiano Freitas

Este planejamento organiza o trabalho entre a Entrega 1 e a Entrega 2: o plano de avaliação (Fase 3), a execução e o julgamento (Fase 4), a ação de melhoria obrigatória e a segunda versão do artigo. Cada atividade corresponde a uma issue com responsável, esforço planejado e datas, para alimentar as três categorias do PSM.

## 1. Premissas

O Ponto de Controle 2 é em **16/11/2026**, com slides e andamento do artigo, e a recomendação é chegar a ele com tudo pronto. A entrega final é em **22/11/2026**; o intervalo entre as duas datas serve para incorporar o feedback do PC2 e revisar o artigo. Por isso o plano trata o PC2 como o prazo real das Fases 3 e 4 e da ação de melhoria.

A ação de melhoria depende da avaliação: ela só pode ser escolhida depois que os dados mostrarem qual métrica ficou em mínimo ou insatisfatório. A ordem é, portanto, plano (Fase 3) → coleta e julgamento (Fase 4) → ação de melhoria.

As três características e o GQM da Fase 2 não mudam, e os nomes usados em todos os artefatos são os da ISO/IEC 25010:2023 (Capacidade de interação, Eficiência de desempenho e Flexibilidade). A Fase 3 apenas operacionaliza o que a Fase 2 especificou; quando precisar esclarecer uma definição (por exemplo, o que conta como "ajuda"), o esclarecimento é registrado como operacionalização, sem alterar limites de pontuação já fixados.

## 2. Cronograma

| Período | O que acontece | Marco (milestone) |
| :---- | :---- | :---- |
| Qua 04/11 a Sex 06/11 | Limpeza da E1; inventário das máquinas; estrutura de dados; protocolos das três características; massa sintética; instrumentação; recrutamento | Reunião 04 na Qui 05/11: revisão cruzada dos protocolos |
| Sáb 07/11 | Pilotos: uma sessão de usuário, uma rodada de medição por SO, uma instalação | Ajustes dos protocolos |
| Dom 08/11 | Fase 3 no artigo e na GitPage com protocolos, recursos e cronograma; corte PSM 1 | **F3: plano de avaliação pronto** |
| Seg 09/11 a Sex 13/11 | Coleta da Fase 4: sessões com participantes (Dupla A) até 13/11; medições (Dupla B) e testes de instalação, checklist e migração (Dupla C) até 12/11 | Reunião 05 na Qui 12/11: situação da coleta |
| Qui 12/11 a Sáb 14/11 | Consolidação, cálculo das métricas e enquadramento nas faixas: Duplas B e C em 12 e 13/11; Dupla A em 13 e 14/11 (manhã) | **F2: dados brutos e planilhas calculadas no repositório (14/11)** |
| Sáb 14/11 (tarde) | Julgamento integrado; recomendações priorizadas; escolha da ação de melhoria | Reunião 06 (online) |
| Sáb 14/11 a Dom 15/11 | Ação de melhoria; artigo v2 completo; slides; corte PSM 2; ensaio em 15/11 | - |
| Seg 16/11 | Apresentação do PC2 | **PC2** |
| Ter 17/11 a Sáb 21/11 | Feedback do PC2 transformado em tarefas; refinamento da ação; revisão cruzada do artigo; GitPage final; corte PSM 3 (publicado em 22/11); release em 21/11 | Reunião 07 logo após o PC2 |
| Dom 22/11 | Margem de segurança e submissão no Moodle | **E2** |

A coleta é o caminho crítico. As sessões com participantes vão de 09/11 a 13/11, e depois disso não há data extra antes do julgamento de 14/11. Por isso o recrutamento começa já, em paralelo aos protocolos, as sessões são marcadas o mais cedo possível dentro da janela, e os tempos e acertos de cada sessão são lançados na planilha no mesmo dia.

## 3. Divisão por dupla

| Dupla | Integrantes | Característica (ISO/IEC 25010:2023) | Categoria PSM | Outras responsabilidades |
| :---- | :---- | :---- | :---- | :---- |
| A | Davi Severiano Freitas (@Davi-UnB) e Pedro Henrique Freire Rodrigues (@Pedro-Henrique3) | Capacidade de interação (antiga Usabilidade) | Recursos e custos | Consolidação do artigo e da Fase 3, atas, estrutura de dados, release |
| B | Karolina Vieira Barbosa (@Karolina91) e Mateus de Siqueira Silva (@siqueira-prog) | Eficiência de desempenho | Desempenho dos processos | Massa sintética (usada também pela Dupla C), GitPage |
| C | Bryan Smith Rodrigues Cavalcante (@Bryan70897) e Dante Fernandes Scarpati (@dantescarpati) | Flexibilidade (antiga Portabilidade) | Calendário e progresso | Limpeza das issues da E1, apoio ao recrutamento e, se preciso, como observadores nas sessões |

Capacidade de interação tem ênfase 5 e exige sessões com pessoas, então é a frente que mais depende de agenda externa. A Dupla C apoia o recrutamento e, se algum horário coincidir com aula de alguém da Dupla A, assume o papel de observadora (cronometragem e anotação).

No PC2, cada dupla faz e apresenta os slides da sua característica. A Dupla A cuida também da abertura, do julgamento integrado, da ação de melhoria e da unificação visual do arquivo.

## 4. Issues e ordem de execução

### 4.1 Como as issues estão organizadas

As 34 issues têm o identificador no título (`[TASK] E2-xx`), e o número indica o grupo: **E2-0x** são tarefas de organização, **E2-1x, E2-2x e E2-3x** preparam a avaliação de Capacidade de interação, Eficiência de desempenho e Flexibilidade, respectivamente, **E2-4x** consolidam o plano e os slides, **E2-5x, E2-6x e E2-7x** são a coleta e a análise de cada característica, **E2-8x** são o julgamento e a ação de melhoria, **E2-9x** são o artigo, a GitPage e a entrega, e **E2-Px** são as medições do PSM e as atas.

Elas estão distribuídas em quatro milestones, que correspondem aos marcos do cronograma: **F3** (plano de avaliação, até 08/11), **F2** (coleta e análise, até 14/11), **PC2** (julgamento, ação de melhoria, artigo e slides, até 16/11) e **E2** (revisão final e entrega, até 22/11).

Cada issue traz o objetivo, uma lista de tarefas marcáveis, o entregável esperado, as métricas envolvidas, as horas planejadas, as datas de início e de conclusão, os critérios de conclusão e as dependências. As horas planejadas somam 156,5 h, entre 21 e 32 h por pessoa. Com o valor de R\$ 35,00 por hora adotado pela equipe no PSM de Recursos e custos, o custo planejado da Entrega 2 é de R\$ 5.477,50; cada issue mostra o seu custo planejado ao lado das horas.

### 4.2 Como trabalhar em uma issue

Ao começar, o responsável move a issue para **Em andamento** no Project. Durante o trabalho, marca as tarefas da lista e salva os arquivos nos caminhos indicados no entregável. Ao terminar, registra as horas reais e a data de conclusão nos campos do Project, comenta na issue com o link da evidência (arquivo, commit ou página) e a fecha. Se o prazo não for cumprido, a issue recebe a label `status:late` e um comentário explicando o motivo e a nova data. Esses registros são a fonte dos cortes de Recursos e custos e de Calendário e progresso, então uma issue fechada sem horas e sem data atrapalha a medição da equipe inteira.

As horas também continuam na planilha de horas, como na E1.

### 4.3 Ordem de execução

A sequência abaixo vale para a equipe toda. Dentro de cada etapa, as duplas trabalham em paralelo; a seta indica que uma issue só começa quando a anterior estiver pronta.

**Etapa 0: arranque (04/11 a 05/11).** São tarefas curtas e independentes, que destravam o resto. E2-00 limpa as pendências da E1. E2-01 ajusta a coerência da Fase 2, para que a numeração das questões já entre certa no plano. E2-02 levanta as máquinas da equipe, e sem ele nenhuma dupla sabe em que sistema vai medir. E2-03 cria a estrutura de pastas onde todos os dados vão ser salvos. A ata da Reunião 04 (E2-P4) registra a revisão dos protocolos.

**Etapa 1: preparação de cada característica (04/11 a 07/11).**

- **Dupla A:** E2-10 (protocolo) → E2-12 (piloto em 07/11). O recrutamento (E2-11) começa no mesmo dia que o protocolo, porque é o item mais demorado e não pode esperar.  
- **Dupla B:** E2-20 (massa de dados) → E2-21 (instrumentação) → E2-22 (protocolo e piloto em 07/11).  
- **Dupla C:** E2-30 (instalação) e E2-31 (checklist) em paralelo → E2-32 (migração), que depende da coleção padrão gerada pela Dupla B em E2-20.

**Etapa 2: plano de avaliação (05/11 a 08/11).** E2-40: cada dupla envia o resumo do seu protocolo até 07/11, e a Dupla A consolida a Fase 3 no artigo e na GitPage até 08/11. No mesmo dia é feito o primeiro corte do PSM (E2-P1, E2-P2 e E2-P3).

**Etapa 3: coleta (09/11 a 13/11).**

- **Dupla A:** E2-50 e E2-51 (sessões dos dois grupos), entre 09/11 e 13/11, conforme a agenda de cada participante.  
- **Dupla B:** E2-60 (medições nos três sistemas).  
- **Dupla C:** E2-70 (instalações) → E2-71 (checklist e migrações).

**Etapa 4: análise por característica (12/11 a 14/11).** E2-61 e E2-72 em 12 e 13/11; E2-52 em 13 e 14/11, porque as sessões vão até sexta. Em todas: cada dupla calcula suas métricas, enquadra nas faixas da Fase 2, responde às suas questões e hipóteses e abre uma issue `[IMPROVE]` (template 03) para cada resultado em mínimo ou insatisfatório.

**Etapa 5: julgamento e ação de melhoria (14/11 a 16/11).** E2-80 (reunião de 14/11 à tarde) → E2-81. O julgamento integrado prioriza as issues `[IMPROVE]` e escolhe a ação de melhoria. A ação passa para a dupla da característica do problema escolhido, que a executa até o PC2.

**Etapa 6: artigo e slides para o PC2 (13/11 a 16/11).** E2-90 (artigo completo) e E2-41 (slides) andam juntos: cada dupla escreve a seção de resultados e faz os slides da sua característica assim que termina a Etapa 4. A GitPage da issue E2-91 entra aqui com as páginas das Fases 3 e 4 já publicadas e os dados brutos linkados. Segundo corte do PSM em 15/11 e ensaio na mesma noite.

**Etapa 7: depois do PC2 (17/11 a 22/11).** E2-95 transforma o feedback em tarefas e faz a revisão cruzada do artigo. E2-91 finaliza a GitPage. Terceiro corte do PSM, previsto para 21/11 e publicado em **22/11/2026**, que alimenta a tabela de contribuição. E2-92 publica a release em 21/11 e submete no Moodle, deixando 22/11 como margem. E2-93 prepara a apresentação final.

### 4.4 Resumo por dupla

| Etapa | Dupla A (Davi, Pedro) | Dupla B (Karolina, Mateus) | Dupla C (Bryan, Dante) |
| :---- | :---- | :---- | :---- |
| 0 | E2-01, E2-03, ata da Reunião 04 | E2-02 | E2-00 |
| 1 | E2-10 → E2-12; E2-11 em paralelo | E2-20 → E2-21 → E2-22 | E2-30, E2-31 → E2-32 |
| 2 | Consolida E2-40; corte E2-P1 | Parte da E2-40; corte E2-P3 | Parte da E2-40; corte E2-P2 |
| 3 | E2-50, E2-51 | E2-60 | E2-70 → E2-71; apoia sessões da Dupla A se preciso |
| 4 | E2-52 | E2-61 | E2-72 |
| 5 | Conduz E2-80 | Participa de E2-80 | Participa de E2-80 |
| 5 e 6 | E2-81 (se a ação for de interação); abertura, julgamento e fechamento dos slides; consolida E2-90 | Slides e resultados de desempenho; E2-91 parcial | Slides e resultados de flexibilidade |
| 7 | E2-95, E2-92, atas | E2-91 final, revisão cruzada | Revisão cruzada, corte E2-P2 |

## 5. Decisões de método que o plano precisa registrar

Esta seção resume o que cada protocolo deve fixar para atender ao critério F3-C1 (instruções repetíveis). O texto final de cada protocolo é produzido nas issues da Fase 3.

### 5.1 Capacidade de interação

**Entrevista já combinada.** A sessão com o estudante que usa o Anki entra como participante do Grupo B, se a triagem confirmar o uso regular. A Fase 2 especificou métricas de desempenho em tarefas (Tct e Texec para o Grupo B), e elas só existem se ele executar as tarefas enquanto é observado e gravado. A sessão segue então três partes: triagem, tarefas observadas (de onde saem as métricas) e, ao final, o questionário. As respostas do questionário entram como evidência qualitativa, útil para explicar resultados e para fundamentar a ação de melhoria, sem criar uma métrica pontuada nova, que não foi especificada na Fase 2.

**Participantes.** A meta é de dois participantes no Grupo A (iniciantes) e três no Grupo B (frequentes), com mínimo aceitável de um iniciante e dois frequentes, todos classificados pelo formulário de triagem da Seção IV-A2. Integrantes da equipe não participam como usuários, porque conhecem o roteiro e o produto.

Esse número é definido pelas restrições da Fase 1: prazo curto, nenhum custo e participação voluntária com consentimento registrado. Ele é compatível com o propósito da avaliação, que é indicar pontos de melhoria, e não certificar o produto. Com essa amostra, os resultados descrevem onde os participantes tiveram dificuldade e não permitem generalizar para todos os estudantes nem fazer inferência estatística. Isso é declarado como limitação no artigo, e o questionário ao final de cada sessão ajuda a explicar cada dificuldade observada.

O Grupo A sustenta as questões Q1 e Q2 de Capacidade de interação, que pesam mais por causa da ênfase 5. Por isso o recrutamento de iniciantes é a prioridade da semana; mesmo um único iniciante já permite observar o primeiro contato com o Anki.

**Como os números são tratados com amostra pequena.** Os limites da Tabela V não mudam. O que muda é a forma de apresentar e calcular, para que os valores façam sentido com poucas pessoas:

- As taxas são calculadas sobre o total de tentativas ou indicações, não sobre o número de pessoas. Com dois iniciantes e seis itens no teste de reconhecimento, Trf passa a ter 12 indicações, o que dá uma resolução bem melhor do que 0%, 50% ou 100%. O valor por item também é reportado.  
- Todo resultado aparece também como contagem ("5 de 6 tarefas"), ao lado da porcentagem.  
- Os tempos (Taprend e Texec) são apresentados por participante e pela mediana, sem média de grupo, que com dois ou três valores seria enganosa.  
- A comparação entre grupos da hipótese H3 de Capacidade de interação é feita entre as medianas e tratada como indício, não como diferença comprovada.  
- O julgamento de cada questão declara a amostra (número de participantes) e o artigo explica o limite de generalização.

Cada sessão tem um facilitador, que lê os enunciados e aplica as regras de ajuda, e um observador, que cronometra e preenche a ficha. A sessão é gravada (tela e áudio, sem câmera) após a assinatura do termo de consentimento. Participantes são identificados apenas por código (PA01 e PA02 para iniciantes, PB01 a PB03 para frequentes). Com poucas sessões, a mesma dupla conduz todas, o que reduz a variação entre facilitadores.

Regras que precisam estar escritas no protocolo, porque os níveis da Tabela V dependem delas:

- **Ajuda.** Uma ajuda é qualquer intervenção do facilitador. Ela só ocorre quando o participante pede ou fica três minutos sem progresso, e segue dicas padronizadas em dois níveis (primeiro aponta a área da tela, depois indica o comando). Cada ajuda é registrada com horário e nível.  
- **Abandono.** A tarefa é encerrada como falha aos 10 minutos (limite insatisfatório de Texec) ou quando o participante desiste. A sessão do Grupo A é encerrada aos 40 minutos (limite insatisfatório de Taprend).  
- **Início e fim do cronômetro.** Começa quando o facilitador termina de ler o enunciado e termina quando o critério de sucesso da tarefa é visível na tela (por exemplo, o baralho aparece na lista).  
- **Trf (Q1).** Antes de qualquer uso, o participante do Grupo A vê a janela principal e a janela Adicionar e indica onde faria cada uma de seis ações ou onde está cada conceito (criar baralho, adicionar cards, estudar, nota, tipo de nota, card). Trf é calculada sobre o total de indicações e também por item.  
- **Taprend e Tsa (Q2).** O Grupo A faz o roteiro completo (criar conta no AnkiWeb, criar baralho, adicionar cards, revisar, sincronizar); o tempo total é Taprend. Em seguida faz uma segunda rodada curta das mesmas tarefas, sem ajuda; a taxa de sucesso dessa rodada é Tsa. Essa é a operacionalização de "sucesso após aprendizagem" e precisa ser explicitada no artigo.  
- **Tct e Texec (Q3).** Os dois grupos fazem as tarefas diárias (revisar, adicionar cards, sincronizar). O Grupo B usa uma conta de teste da equipe, para não mexer na coleção pessoal do participante.

Conta no AnkiWeb: a criação exige e-mail e confirmação. O protocolo define se o participante usa o próprio e-mail (e apaga a conta depois) ou um e-mail descartável fornecido pela equipe.

### 5.2 Eficiência de desempenho

Uma máquina por sistema, de preferência com o sistema instalado diretamente (máquina virtual distorce CPU e disco; se o Ubuntu precisar ser em VM, isso é registrado como fator de variação). Condições de controle da Seção IV-B3: outros aplicativos fechados e a máquina ligada na tomada.

Massa de dados: coleções sintéticas de 10 mil, 50 mil e 100 mil cards geradas por script com o pacote `anki`, com semente fixa e histórico de revisões, para que qualquer pessoa gere exatamente a mesma coleção. A coleção de 10 mil também é a coleção padrão de sincronização e de migração.

Instrumentação proposta (os nomes de hooks foram conferidos no código do Anki):

- **Add-on de medição.** Registra carimbos de tempo nos hooks `main_window_did_init`, `deck_browser_did_render`, `state_did_change`, `reviewer_did_show_question`, `sync_will_start` e `sync_did_finish`. Assim, Trev é o intervalo entre a mudança para o estado `review` e a exibição do primeiro card, e Tsinc é o intervalo entre o início e o fim da sincronização. O add-on também mantém um temporizador de 100 ms na thread principal e registra atrasos acima de 1 s, que é o critério de "trava" da Tabela VIII.  
- **Script lançador.** Anota o instante de disparo e abre o Anki; Tini vai do disparo até o primeiro `deck_browser_did_render`.  
- **Scripts com o pacote `anki`.** Tcarga é o tempo para abrir a coleção e executar a primeira consulta. Vazproc é o número de cards dividido pelo tempo de `fix_integrity()` (Verificar banco de dados), em cards por minuto.  
- **Coletor de recursos.** Um script com `psutil`, igual nos três sistemas, amostra CPU, RSS e I/O a cada 1 s, somando os processos filhos (o lançador do Anki inicia um processo Python separado). No Ubuntu, `pidstat -t -u -w -d 1` complementa com os dados por thread da Q4.

Cenários: **repouso** são 5 minutos parado na lista de baralhos, depois de 5 minutos de estabilização. **Estresse** é uma sequência fixa sobre a coleção de 100 mil cards: verificar banco de dados, abrir o navegador com todos os cards, ordenar por data e sincronizar. Cada medição de tempo é repetida 5 vezes; o cold start limpa o cache de disco antes de cada repetição (`drop_caches` no Ubuntu, `purge` no macOS, reinicialização no Windows). Para a sincronização, registram-se a latência até o AnkiWeb e a velocidade da conexão em cada rodada.

Pontos a confirmar no piloto: o tamanho máximo de coleção aceito pelo AnkiWeb (se 100 mil não sincronizar, a sincronização usa só a coleção de 10 mil e isso é declarado) e se o add-on carrega corretamente na versão 26.09.3.

### 5.3 Flexibilidade

**Instalação (Q1).** Três tentativas por sistema, feitas por integrantes diferentes, sempre em estado limpo (novo usuário do sistema ou VM restaurada a partir de snapshot), seguindo apenas o guia oficial em docs.ankiweb.net. O cronômetro começa ao abrir o instalador já baixado (o download fica de fora, por depender da rede) e termina quando a janela principal do Anki abre pela primeira vez. Intervenção é toda ação além do caminho padrão do instalador: instalar o `zstd`, liberar o app no Gatekeeper ou no SmartScreen, mudar permissões. A desinstalação é verificada em cada sistema, com registro de sim/não e de arquivos remanescentes.

**Checklist de integração (Q2).** Cada um dos 10 critérios recebe um procedimento de teste e um critério de aprovação escritos antes da coleta, com captura de tela como evidência. Cada sistema é avaliado por um integrante e conferido por outro.

**Migração (Q3).** Dois cenários com a coleção padrão de 10 mil cards, incluindo mídia e histórico de revisões: exportação e importação de `.apkg` entre máquinas de sistemas diferentes, e envio e baixa pelo AnkiWeb. Um script compara antes e depois as contagens de notas, cards, baralhos, revisões e mídia, e um hash do conteúdo dos campos e do agendamento. Tpd é a porcentagem de itens preservados; Tsub vai do início da exportação ou sincronização até o fim da verificação. Três repetições por cenário.

## 6. Dicionário de IDs das métricas

Os IDs abaixo são usados nas issues, nos nomes dos arquivos de dados e nas tabelas de resultados.

| ID | Métrica | Questão |
| :---- | :---- | :---- |
| M-INT-01 | Taxa de reconhecimento de funções (Trf) | Q1 de Capacidade de interação |
| M-INT-02 | Tempo de aprendizagem (Taprend) | Q2 de Capacidade de interação |
| M-INT-03 | Taxa de sucesso após aprendizagem (Tsa) | Q2 de Capacidade de interação |
| M-INT-04 | Taxa de conclusão de tarefas (Tct) | Q3 de Capacidade de interação |
| M-INT-05 | Tempo de execução da tarefa (Texec) | Q3 de Capacidade de interação |
| M-PERF-01 | Tempo de inicialização (Tini) | Q1 de Eficiência de desempenho |
| M-PERF-02 | Tempo para iniciar revisão (Trev) | Q1 de Eficiência de desempenho, Q3 de Eficiência de desempenho |
| M-PERF-03 | Tempo de sincronização (Tsinc) | Q1 de Eficiência de desempenho |
| M-PERF-04 | Tempo de carga da coleção (Tcarga) | Q1 de Eficiência de desempenho, Q3 de Eficiência de desempenho |
| M-PERF-05 | Consumo de CPU | Q2 de Eficiência de desempenho |
| M-PERF-06 | Consumo de RAM | Q2 de Eficiência de desempenho, Q3 de Eficiência de desempenho |
| M-PERF-07 | Vazão de processamento (Vazproc) | Q3 de Eficiência de desempenho |
| M-PERF-08 | CPU da Main Thread | Q4 de Eficiência de desempenho |
| M-PERF-09 | Trocas de contexto involuntárias | Q4 de Eficiência de desempenho |
| M-PERF-10 | Taxa de I/O em disco | Q3 de Eficiência de desempenho, Q4 de Eficiência de desempenho |
| M-FLEX-01 | Taxa de instalação bem-sucedida (Tinst) | Q1 de Flexibilidade |
| M-FLEX-02 | Tempo de instalação (Tinst\_t) | Q1 de Flexibilidade |
| M-FLEX-03 | Número de intervenções (Nint) | Q1 de Flexibilidade |
| M-FLEX-04 | Pontuação no checklist de integração (Pint) | Q2 de Flexibilidade |
| M-FLEX-05 | Taxa de preservação de dados (Tpd) | Q3 de Flexibilidade |
| M-FLEX-06 | Tempo de substituição (Tsub) | Q3 de Flexibilidade |

## 7. Estrutura de dados no repositório

```
avaliacao/
  protocolos/            protocolo de cada característica, roteiros, fichas, termo
  scripts/               geração de massa, add-on, coletores, verificação de integridade
  dados/
    interacao/
      bruto/             fichas, formulários de triagem, índice das gravações
      consolidado/       uma planilha por métrica (M-INT-xx.csv)
    desempenho/
      bruto/             logs do add-on, psutil e pidstat por SO e execução
      consolidado/
    flexibilidade/
      bruto/             registros de instalação, capturas do checklist, relatórios de integridade
      consolidado/
  analise/               notebooks ou scripts que geram tabelas e gráficos do artigo
```

Nome dos arquivos brutos: `<métrica>_<SO>_<cenário>_<execução>_<data>`, por exemplo `M-PERF-01_ubuntu_100k_r3_2026-11-10.csv`. Cada pasta `consolidado/` traz um README dizendo de quais arquivos brutos e de qual script cada número saiu, o que atende ao critério F4-C2 (ligação direta entre dado bruto e métrica).

Gravações: o termo de consentimento define onde ficam. Se ele autoriza manter as gravações no repositório, elas são comprimidas (720p, abaixo de 100 MB por arquivo, o limite do GitHub sem LFS). Se o acesso deve ser restrito, ficam numa pasta compartilhada com acesso apenas da equipe e da professora, e o repositório guarda o índice com código do participante, data e link.

## 8. Onde cada critério da rubrica é atendido

| Critério | Como é atendido | Issues |
| :---- | :---- | :---- |
| F3-C1 Método e repetibilidade | Protocolos com passos, regras de ajuda e abandono, início e fim do cronômetro, repetições | E2-10, E2-21, E2-22, E2-30, E2-31, E2-32 |
| F3-C2 Recursos e ambiente | Inventário de hardware e software; massa de dados justificada; perfil exigido dos participantes | E2-02, E2-11, E2-20 |
| F3-C3 Cronograma | Seção 2 deste plano, refletida nas datas e nos milestones das issues | E2-40 |
| F3-C7 / AG-C4 GitPage | Páginas Fase 3 e Fase 4, dados, versão e data no rodapé, links cruzados | E2-40, E2-91 |
| F3-C8 Consistência 2→3 | Tabela métrica → método → instrumento → ambiente → responsável → data | E2-40 |
| F4-C1 / F4-C2 Coleta e dados brutos | Estrutura da Seção 7; dados brutos ligados às métricas | E2-03, E2-50 a E2-72 |
| F4-C3 Análise GQM | Cada métrica na faixa, cada questão e cada hipótese respondida, gráficos e tabelas | E2-52, E2-61, E2-72 |
| F4-C4 / F4-C5 Propósito e julgamento | Recomendações priorizadas para mantenedores e estudantes, ligadas ao propósito da Fase 1 | E2-80 |
| Ação de melhoria | Seleção justificada pela evidência, execução e validação | E2-81 |
| Premissa 1 Relações entre características | Seção de discussão com evidências, limitações e casos sem dados suficientes | E2-80, E2-90 |
| Premissa 3 PSM | Cortes de 08/11, 15/11 e 22/11 (corte 3 oficial) com interpretação e decisão registrada | E2-P1, E2-P2, E2-P3 |
| AG-C1, AG-C2, AG-C3 Artigo | Versão completa no PC2 e revisão final após o feedback, limite de 15 páginas, declaração de IA atualizada | E2-90, E2-95 |
| AG-C5 Contribuição | Tabela com porcentagens que somam 100%, a partir do corte PSM de 22/11 | E2-95, E2-P1 |

## 9. Riscos e contingências

| Risco | Efeito | Resposta planejada |
| :---- | :---- | :---- |
| Nenhum iniciante confirmado até 10/11 | Q1 e Q2 de Capacidade de interação sem dados | Todos indicam contatos desde 04/11 (calouros, colegas de outros cursos, familiares); se ainda assim não houver ninguém, Q1 e Q2 de Capacidade de interação são reportadas como não respondidas, com a justificativa |
| Participante desmarca | Menos dados no Grupo A ou B | Marcar as sessões no início da janela (09 e 10/11), para que uma remarcação ainda caiba até 13/11, e manter uma reserva na lista de contatos |
| Nenhuma máquina com Ubuntu nativo | Q4 de Eficiência de desempenho medida em VM | Medir em VM e registrar como fator de variação; não comparar valores absolutos de CPU entre SO |
| Add-on não funciona na 26.09.3 | Sem Tini, Trev e Tsinc instrumentados | Plano B: gravação de tela a 60 fps e contagem de quadros |
| AnkiWeb recusa a coleção de 100 mil | Sem Tsinc em escala | Tsinc só com 10 mil, declarado no artigo |
| Atraso na coleta | Julgamento e ação de melhoria incompletos no PC2 | Reunião 05 (12/11) decide cortes de escopo, registrados como decisão de gestão no PSM; o que faltar é apresentado no PC2 como plano e concluído até 21/11 |
| Artigo passa de 15 páginas | Rejeição | Orçamento da Seção 10 e conferência na revisão final (E2-95) |

## 10. Orçamento de páginas do artigo v2

O artigo da E1 já ocupa cerca de 10 páginas sem o apêndice. Para caber em 15 com referências, a meta é: Fase 3 com até 1,5 página (a tabela de rastreabilidade carrega a maior parte), Fase 4 com até 3 páginas (uma tabela de resultados por característica e dois ou três gráficos), discussão, ação de melhoria e conclusão com até 1,5 página. Isso exige enxugar cerca de 1 página das seções II a IV, por exemplo levando para a GitPage o detalhe dos procedimentos de coleta da Tabela VII, que passa a ser coberto pela Fase 3.