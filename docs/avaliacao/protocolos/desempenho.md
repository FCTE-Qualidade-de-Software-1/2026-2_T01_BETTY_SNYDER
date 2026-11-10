# 🧪 Protocolo de Avaliação de Eficiência de Desempenho (Dupla B)

> **Equipe:** Betty Snyder (FGA0315 - Qualidade de Software 1)  
> **Responsáveis:** Karolina Vieira Barbosa e Mateus de Siqueira Silva  
> **Artefato:** Protocolo de Medição da Fase 3 (Issue #57 — E2-22)  
> **Alvo:** Anki Desktop 26.09.3 (Windows, macOS e Ubuntu)  
> **Norma de Referência:** ISO/IEC 25010:2023 & ISO/IEC 25040 (Fase 3: Projetar a Avaliação)

---

## 🎯 1. Objetivo & Escopo Metodológico

Este protocolo define os procedimentos padronizados e reprodutíveis para coleta das métricas da característica **Eficiência de Desempenho** (Subcaracterísticas: *Comportamento no Tempo*, *Utilização de Recursos* e *Capacidade*), respondendo às 4 Questões do GQM (G2):
- **Q1 (Comportamento no Tempo):** Medição de tempos de inicialização (*Cold Start*), transição para revisão e sincronização com o AnkiWeb.
- **Q2 (Utilização de Recursos):** Consumo médio e pico de CPU (%) e Memória RAM (MB) em repouso e sob carga pesada.
- **Q3 (Capacidade & Escalabilidade):** Degradação de desempenho e vazão ($\text{cards/min}$) operando sobre coleções escalonadas ($10\text{k}$, $50\text{k}$ e $100\text{k}$ cards).
- **Q4 (Desempenho de Threads - Específico Ubuntu):** Verificação de isolamento entre a Main Thread (interface PyQt) e as Worker Threads de background (backend Rust via `pidstat -t`).

---

## 🛡️ 2. Condições de Controle Rigoroso (Pré-requisitos Ambientais)

Antes de iniciar qualquer medição, o avaliador deve garantir que o ambiente atenda aos seguintes critérios:
1. **Alimentação Elétrica:** O computador/notebook deve estar **conectado à tomada** (alimentação externa ativa, plano de energia configurado em *Alto Desempenho* para evitar *throttling* térmico ou economia de clock).
2. **Isolamento de Processos Concorrentes:**
   - Todos os navegadores web (Chrome, Firefox), IDEs (VS Code, JetBrains), comunicadores (Discord, Teams, Telegram) e players de música/vídeo devem ser **completamente encerrados**.
   - O uso basal de CPU do sistema antes de abrir o Anki deve estar **abaixo de 2%**.
3. **Condição de Rede (para testes de Sincronização):**
   - Conexão Wi-Fi ou cabo estável. Registrar a latência média (ping) e velocidade de download/upload antes da sessão.
4. **Registro de Hardware:**
   - Preencher a tabela de identificação do equipamento:
     - Sistema Operacional e Versão exata do Kernel/Build.
     - Processador (Modelo, Clock base e contagem de núcleos físicos/lógicos).
     - Memória RAM instalada (Capacidade e Tecnologia DDR).
     - Armazenamento (SSD NVMe, SSD SATA ou HDD).


### 2.1. Orientações específicas por sistema operacional

As condições de controle desta seção devem ser aplicadas em todos os cenários. Os nomes dos menus podem variar conforme a versão do sistema.

#### Windows 10/11

1. **Alimentação:** conectar o computador à tomada. Em *Configurações → Sistema → Energia e bateria*, selecionar o modo de energia **Melhor desempenho** (quando disponível).
2. **Encerrar processos:** fechar navegadores, IDEs, comunicadores e players. Usar `Ctrl + Shift + Esc` para abrir o **Gerenciador de Tarefas** e conferir se há processos em segundo plano consumindo CPU ou disco.
3. **Verificar uso basal:** na aba **Processos** do Gerenciador de Tarefas, observar a utilização da CPU antes de abrir o Anki. Registrar o valor e confirmar que está abaixo de 2%.
4. **Monitorar o Anki:** durante as medições, abrir o Gerenciador de Tarefas e localizar o processo do Anki. Na aba **Detalhes**, conferir CPU e memória; para acompanhamento mais detalhado, usar o **Monitor de Recursos** (`resmon` no menu Iniciar).
5. **Coleta automatizada:** executar o coletor Python no PowerShell ou no Prompt de Comando, a partir da pasta em que o arquivo `coletor.py` está localizado:
   - `py -3 coletor.py --cenario repouso --duracao 300`
   - `py -3 coletor.py --cenario estresse`
   - `py -3 coletor.py --cenario cold_start`

   Se o comando `py` não estiver disponível, tentar `python` no lugar de `py -3`.
6. **Cold Start:** para reduzir a influência do cache, reiniciar o Windows antes de cada rodada ou bateria de rodadas. Como alternativa, utilizar o RAMMap, da Microsoft Sysinternals, com a opção **Empty → Empty Standby List**. Registrar qual método foi utilizado e aplicá-lo de forma consistente em todas as repetições.
7. **Registro:** anotar a edição e a versão do Windows (`Configurações → Sistema → Sobre`) e o modelo do processador, a RAM e o tipo de armazenamento.

#### macOS

1. **Alimentação:** conectar o Mac à tomada. Em notebooks, desativar o **Modo de Pouca Energia** durante os testes, se estiver ativo.
2. **Encerrar processos:** fechar navegadores, IDEs, comunicadores e players. Abrir o **Monitor de Atividade** (`Aplicativos → Utilitários → Monitor de Atividade`) e verificar se não há processos concorrentes consumindo recursos.
3. **Verificar uso basal:** no Monitor de Atividade, selecionar a aba **CPU** e observar o uso do sistema antes de abrir o Anki. Registrar o valor e confirmar que está abaixo de 2%.
4. **Monitorar o Anki:** no Monitor de Atividade, localizar o processo do Anki e acompanhar as colunas **% CPU** e **Memória**. Na aba **Disco**, observar a atividade de leitura e escrita quando necessário.
5. **Coleta automatizada:** abrir o Terminal, acessar a pasta do `coletor.py` com `cd` e executar:
   - `python3 coletor.py --cenario repouso --duracao 300`
   - `python3 coletor.py --cenario estresse`
   - `python3 coletor.py --cenario cold_start`
6. **Cold Start:** fechar o Anki e executar `sudo purge` no Terminal, caso o comando esteja disponível na versão do macOS utilizada. Se não estiver disponível ou não produzir o efeito esperado, reiniciar o Mac antes da rodada. Registrar o método utilizado e mantê-lo igual em todas as repetições.
7. **Registro:** anotar a versão do macOS em `Menu Apple → Sobre Este Mac`, além do modelo do processador/chip, memória instalada e tipo de armazenamento.

#### Observação sobre a comparação entre sistemas

O coletor baseado em `psutil` deve ser utilizado nos três sistemas para manter a coleta de CPU, memória RSS e I/O padronizada. O Gerenciador de Tarefas/Monitor de Recursos do Windows e o Monitor de Atividade do macOS servem como acompanhamento visual e conferência complementar; seus valores não devem substituir os dados do CSV. A análise detalhada de Main Thread e Worker Threads descrita em Q4 permanece específica do Ubuntu neste protocolo, pois os comandos `pidstat` apresentados não se aplicam diretamente ao Windows ou ao macOS.

---

## ⚙️ 3. Procedimento Operacional Passo a Passo

### 🧊 Cenário 1: Inicialização a Frio (*Cold Start*) & Tempos de Transição (Q1)

* **Objetivo:** Medir o tempo de carregamento da aplicação sem influência de dados em cache de disco do sistema operacional.
* **Repetições:** 5 rodadas completas (descartando a maior e a menor; calcula-se a média das 3 centrais).
* **Procedimento:**
  1. Fechar o Anki se estiver aberto.
  2. Limpar o cache de páginas do sistema operacional:
     - **Ubuntu / Linux:** Executar `sync && echo 3 | sudo tee /proc/sys/vm/drop_caches`
     - **macOS:** Executar `sudo purge`
     - **Windows:** Reiniciar a máquina entre as baterias ou utilizar script de liberação de standby memory via RAMMap.
  3. Iniciar o script de disparo automatizado (`coletor.py --cenario cold_start`). No Windows, usar `py -3 coletor.py --cenario cold_start` (ou `python`); no macOS e Ubuntu, usar `python3 coletor.py --cenario cold_start`.
  4. O script registra o carimbo de tempo $T_0$ no instante exato do disparo do executável do Anki.
  5. O add-on de instrumentação registra o carimbo $T_{\text{render}}$ no hook `deck_browser_did_render`.
  6. $T_{\text{inicializacao}} = T_{\text{render}} - T_0$.
  7. **Transição para Revisão:** O avaliador clica no baralho padrão e o add-on anota o intervalo até o evento `reviewer_did_show_question` ($T_{\text{revisao}}$).
  8. Registrar os valores no arquivo `resultados_cenario1_<SO>.csv`.

---

### 🧘 Cenário 2: Perfilamento de Repouso vs. Estresse (Q2 e Q4)

#### A. Repouso Basal (5 Minutos)
1. Abrir o Anki com uma coleção padrão limpa.
2. Não tocar no teclado ou mouse durante **5 minutos** (fase de estabilização térmica e encerramento de threads secundárias).
3. Iniciar o coletor `psutil` com amostragem de **1 segundo** (`coletor.py --cenario repouso --duracao 300`).
4. Durante 300 segundos, o coletor monitora o processo pai do Anki e todos os seus subprocessos filhos:
   - CPU Total (%)
   - Memória RSS (Resident Set Size em MB)
   - Taxa de I/O de Leitura/Escrita (KB/s)
5. No **Ubuntu**, rodar em paralelo: `pidstat -t -u -p $(pgrep anki) 1 300 > threads_repouso.txt`.

#### B. Estresse e Carga Máxima (Coleção de 100k Cards)
1. Carregar a coleção sintética de **100.000 cards** (`colecao_100k.anki2`).
2. Disparar o coletor de recursos (`coletor.py --cenario estresse`).
3. Executar em sequência contínua a seguinte bateria de esforço:
   - Abrir o Painel do Navegador de Cards (*Browse*).
   - Clicar em "Todos os Cartões" ($100.000$ registros carregados no grid).
   - Clicar no cabeçalho da coluna "Modificado" para forçar **ordenação total em memória**.
   - Realizar uma busca por expressão regular ampla (ex.: `card:*`).
   - Fechar o navegador e acionar a ferramenta **Verificar Banco de Dados** (*Tools ➔ Check Database*).
4. No **Ubuntu**, capturar a divisão de carga por thread (no Windows e no macOS, acompanhar CPU e memória pelos utilitários descritos na Seção 2.1; a separação por thread não faz parte deste protocolo nesses sistemas):
   - `pidstat -t -u -w -p $(pgrep anki) 1 > threads_estresse.txt`
   - Avaliar se a Main Thread (Qt) manteve $< 15\%$ de CPU e ausência de bloqueio de interface enquanto as Worker Threads executaram a verificação do SQLite.

---

### 📈 Cenário 3: Capacidade & Vazão Escalonada (Q3)

* **Objetivo:** Mensurar o tempo de processamento e a vazão quando o volume de dados escala em ordens de grandeza.
* **Massas Utilizadas:** $10.000$ cards, $50.000$ cards e $100.000$ cards.
* **Procedimento:**
  1. Carregar a coleção de $10\text{k}$ cards.
  2. Disparar a rotina *Check Database* e cronometrar o tempo exato de execução ($T_{\text{exec}}$).
  3. Calcular a vazão:
     $$\text{Vazão} = \frac{N_{\text{cards}}}{T_{\text{exec}} \text{ (em minutos)}}$$
  4. Repetir o procedimento idêntico para a coleção de $50\text{k}$ cards.
  5. Repetir o procedimento idêntico para a coleção de $100\text{k}$ cards.
  6. Calcular a **taxa de degradação percentual**:
     $$\text{Degradação} = \frac{\text{Vazão}_{100k} - \text{Vazão}_{10k}}{\text{Vazão}_{10k}} \times 100$$
  7. Salvar os resultados em `resultados_capacidade_<SO>.csv`.

---

## 📊 4. Planilha de Enquadramento nas Faixas GQM (Critérios de Julgamento)

Os dados brutos coletados nos CSVs serão enquadrados na matriz oficial de níveis acordada na Fase 2:

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
| :--- | :---: | :---: | :---: | :---: |
| **$T_{\text{inicializacao}}$ (Cold Start)** | $> 9\text{ s}$ | $6\text{ s} < T \le 9\text{ s}$ | $3\text{ s} < T \le 6\text{ s}$ | $\le 3\text{ s}$ |
| **$T_{\text{revisao}}$ (Abrir Card)** | $> 3\text{ s}$ | $2\text{ s} < T \le 3\text{ s}$ | $1\text{ s} < T \le 2\text{ s}$ | $\le 1\text{ s}$ |
| **RAM em Repouso** | $> 800\text{ MB}$ | $400\text{ MB} < RAM \le 800\text{ MB}$ | $250\text{ MB} < RAM \le 400\text{ MB}$ | $\le 250\text{ MB}$ |
| **CPU em Repouso (Média)** | $> 10\%$ | $5\% < CPU \le 10\%$ | $2\% < CPU \le 5\%$ | $\le 2\%$ |
| **Pico de RAM sob Estresse** | $> 1.5\text{ GB}$ | $1.0\text{ GB} < RAM \le 1.5\text{ GB}$ | $600\text{ MB} < RAM \le 1.0\text{ GB}$ | $\le 600\text{ MB}$ |
| **CPU da Main Thread sob Carga** | $> 50\%$ | $30\% < CPU \le 50\%$ | $15\% < CPU \le 30\%$ | $\le 15\%$ |
| **Vazão de Processamento** | $< 10.000\text{ cards/min}$ | $10.000 \le V < 30.000$ | $30.000 \le V < 60.000$ | $\ge 60.000\text{ cards/min}$ |

---

## 🚨 5. Critérios de Invalidação da Rodada de Teste

A medição deve ser sumariamente descartada e reiniciada se:
- Ocorrer intervenção do sistema operacional alheia ao teste (ex.: Windows Update disparado, indexação do Spotlight no macOS ou `apt/unattended-upgrades` no Linux consumindo $> 5\%$ de CPU).
- Queda ou oscilação severa de rede no teste de sincronização com o AnkiWeb.
- O operador interagir manualmente com a interface durante a janela de 5 minutos de repouso.

---

## 👥 6. Roteiro de Eficiência Percebida: Entrevistas & Formulário Online (A Dimensão Humana)

Para atender à decisão da Reunião 04 (construção do **Instrumento Único de Entrevista e Formulário** compartilhado entre todas as duplas), a Dupla B integra a coleta da **Eficiência Percebida** (tempo de resposta e fluidez sob a perspectiva do usuário final, conforme Hoxmeier & DiCesare, 2000).

Este módulo compõe a contribuição da Dupla B que será consolidada pelo Pedro no roteiro geral de entrevistas.

---

### 🎙️ 6.1. Bloco de Entrevista Presencial / Remota Observada

Durante a realização das tarefas padrão (criação de baralhos, adição de notas e revisão de cards):

1. **Observação Comportamental do Entrevistador (Ficha de Anotação):**
   - O participante demonstrou impaciência ou hesitação durante o carregamento inicial (*Cold Start*)? `[ ] Sim  [ ] Não`
   - Ocorreram cliques repetidos (*rage clicks*) por impressão de que a interface havia congelado? `[ ] Sim  [ ] Não`
   - A transição entre a exibição da pergunta e da resposta do flashcard ocorreu de forma instantânea? `[ ] Sim  [ ] Não`

2. **Perguntas Qualitativas Pós-Tarefa (Roteiro Semi-Estruturado):**
   - *"Durante o uso, em algum momento você teve a sensação de que o Anki estava lento, travado ou demorando para responder aos seus comandos?"*
   - *"Como você avalia o tempo que o Anki leva para sincronizar com a nuvem (AnkiWeb)? Isso interfere no seu fluxo de estudo?"*
   - *(Para usuários frequentes com grandes coleções):* *"Você nota diferença de velocidade quando pesquisa cards no painel Navegador (*Browse*) ou adiciona muitos cartões de uma vez?"*

---

### 📝 6.2. Bloco para Formulário Online & Triagem (Escala Likert de 1 a 5)

Perguntas prontas para inclusão no formulário do Google Forms / Microsoft Forms distribuído à comunidade de estudantes (grupos de Telegram/WhatsApp da UnB):

> **Instruções ao Participante:** Indique seu grau de concordância com as afirmações abaixo:  
> *(1 = Discordo Totalmente | 2 = Discordo | 3 = Neutro | 4 = Concordo | 5 = Concordo Totalmente)*

| Código | Item de Avaliação (Eficiência Percebida) | Escala |
| :---: | :--- | :---: |
| **LIK-PERF-01** | *"O Anki abre e fica pronto para uso rapidamente no meu computador."* | 1 - 2 - 3 - 4 - 5 |
| **LIK-PERF-02** | *"A navegação entre os cartões e a exibição das respostas ocorrem de forma fluida e sem atrasos."* | 1 - 2 - 3 - 4 - 5 |
| **LIK-PERF-03** | *"A sincronização com o AnkiWeb é rápida o suficiente para não atrapalhar minha rotina de estudos."* | 1 - 2 - 3 - 4 - 5 |
| **LIK-PERF-04** | *"O aplicativo responde instantaneamente quando realizo buscas ou filtro tags no Navegador de cards."* | 1 - 2 - 3 - 4 - 5 |

#### Dados de Contexto de Hardware (Coletados no Formulário):
- Sistema Operacional principal: `( ) Windows 10/11  ( ) macOS  ( ) Linux (Ubuntu/Debian/Fedora/Outro)`
- Tipo de unidade de armazenamento onde o Anki está instalado: `( ) SSD (rápido)  ( ) HDD / Disco Rígido (antigo)  ( ) Não sei informar`
- Tamanho aproximado da coleção de cards: `( ) Menos de 1.000  ( ) 1.000 a 10.000  ( ) Mais de 10.000 cards`
