# Eficiência de desempenho

## 1. Definições

Esta página descreve a coleta **instrumentada** de Eficiência de desempenho (Eficiência de desempenho), executada pela Dupla B (Karolina Vieira Barbosa e Mateus de Siqueira Silva). As definições formais das métricas e as faixas de julgamento estão na [Fase 2](../../fase2.md). O bloco de eficiência percebida, elaborado pela Dupla B, é aplicado pela Dupla A na [entrevista](entrevista.md) e no [Pré-entrevista com participante](pre-entrevista-participante.md).

Escopo operacional desta frente:

- Q1 (comportamento no tempo): inicialização a frio (*cold start*), transição para revisão e sincronização com o AnkiWeb.
- Q2 (utilização de recursos): CPU e memória RAM médios e de pico em repouso e sob carga.
- Q3 (capacidade): degradação e vazão em cards por minuto com coleções de 10 mil, 50 mil e 100 mil cartões.
- Q4 (threads no Ubuntu): isolamento entre a Main Thread (PyQt) e as Worker Threads (Rust), observado com `pidstat -t`.

## 2. Pré-requisitos e condições de controle

Máquinas de referência: [Ambiente](ambiente.md).

Antes de cada medição:

1. **Alimentação elétrica:** computador na tomada; plano de energia em alto desempenho (evitar *throttling*).
2. **Isolamento de processos:** encerrar navegadores, IDEs, comunicadores e players. Uso basal de CPU do sistema **abaixo de 2%** antes de abrir o Anki.
3. **Rede (sincronização):** Wi-Fi ou cabo estável; registrar ping e download/upload.
4. **Registro de hardware:** SO e build, processador (modelo, clock, núcleos), RAM, armazenamento (SSD/HDD).

### 2.1 Orientações e execução por sistema operacional

A automação das coletas pode ser feita via menu interativo interplataforma ou por comandos diretos no terminal.

#### Windows 10/11
1. **Condições prévias:** Notebook na tomada; modo *Melhor desempenho* em *Configurações → Sistema → Energia e bateria*; encerrar processos em segundo plano (`Ctrl + Shift + Esc`) até CPU basal < 2%.
2. **Execução automatizada (Menu CMD):**
   ```cmd
   docs\avaliacao\scripts\executar_testes.cmd
   ```
3. **Execução direta (Prompt de Comando ou PowerShell):**
   - *Cold start:* Encerrar o Anki; esvaziar a Standby List no RAMMap (*Empty → Empty Standby List*) ou reiniciar; executar:
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario cold_start --saida docs\avaliacao\dados\desempenho\bruto\T_ini_coldstart_windows_01.csv
     ```
   - *Repouso basal (300 s):*
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario repouso --duracao 300 --saida docs\avaliacao\dados\desempenho\bruto\CPU_repouso_windows_01.csv
     py -3 docs\avaliacao\scripts\analisador_threads.py --modo realtime --duracao 300 --cenario repouso --saida docs\avaliacao\dados\desempenho\bruto\threads_repouso_windows_01.csv
     ```
   - *Estresse (180 s com 100k cards):*
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario estresse --duracao 180 --saida docs\avaliacao\dados\desempenho\bruto\metricas_estresse_windows_01.csv
     py -3 docs\avaliacao\scripts\analisador_threads.py --modo realtime --duracao 180 --cenario estresse --saida docs\avaliacao\dados\desempenho\bruto\threads_estresse_windows_01.csv --grafico
     ```

#### macOS
1. **Condições prévias:** Tomada conectada; desativar *Modo de Pouca Energia*; confirmar CPU basal < 2% no *Monitor de Atividade*.
2. **Execução automatizada (Shell):**
   ```bash
   chmod +x docs/avaliacao/scripts/executar_testes.sh
   ./docs/avaliacao/scripts/executar_testes.sh
   ```
3. **Execução direta (Terminal):**
   - *Cold start:* Fechar Anki (`pkill -f Anki`); limpar cache de disco (`sudo purge`); executar:
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario cold_start --saida docs/avaliacao/dados/desempenho/bruto/T_ini_coldstart_macos_01.csv
     ```
   - *Repouso basal (300 s):*
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario repouso --duracao 300 --saida docs/avaliacao/dados/desempenho/bruto/CPU_repouso_macos_01.csv
     ```
   - *Estresse (180 s):*
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario estresse --duracao 180 --saida docs/avaliacao/dados/desempenho/bruto/metricas_estresse_macos_01.csv
     ```

#### Linux (Ubuntu 24.04 LTS)
1. **Condições prévias:** Encerrar softwares em background; verificar CPU basal < 2%.
2. **Execução automatizada (Shell):**
   ```bash
   ./docs/avaliacao/scripts/executar_testes.sh
   ```
3. **Execução direta (Konsole / Bash):**
   - *Cold start:* `pkill -f anki && sync && echo 3 | sudo tee /proc/sys/vm/drop_caches` seguido de:
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario cold_start --saida docs/avaliacao/dados/desempenho/bruto/T_ini_coldstart_ubuntu_01.csv
     ```
   - *Repouso basal (300 s):*
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario repouso --duracao 300 --saida docs/avaliacao/dados/desempenho/bruto/CPU_repouso_ubuntu_01.csv
     python3 docs/avaliacao/scripts/analisador_threads.py --modo realtime --duracao 300 --cenario repouso --saida docs/avaliacao/dados/desempenho/bruto/threads_repouso_ubuntu_01.csv
     ```
   - *Estresse (180 s com 100k cards):*
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario estresse --duracao 180 --saida docs/avaliacao/dados/desempenho/bruto/metricas_estresse_ubuntu_01.csv
     python3 docs/avaliacao/scripts/analisador_threads.py --modo realtime --duracao 180 --cenario estresse --saida docs/avaliacao/dados/desempenho/bruto/threads_estresse_ubuntu_01.csv --grafico
     ```

#### Observação sobre comparação entre sistemas

O coletor `psutil` é a fonte oficial de CPU, RSS e I/O nos três SOs. Utilitários nativos são conferência visual. A análise por thread (Q4) permanece específica do Ubuntu (`pidstat`).

## 3. Procedimento passo a passo

### Cenário 1: Cold start e tempos de transição (Q1)

- **Objetivo:** tempo de carga sem cache de páginas do SO.
- **Repetições:** 5; descartar maior e menor; média das 3 centrais.

1. Fechar o Anki.
2. Limpar cache: Ubuntu `sync && echo 3 | sudo tee /proc/sys/vm/drop_caches`; macOS `sudo purge`; Windows reinício ou RAMMap.
3. `coletor.py --cenario cold_start` (`py -3` no Windows; `python3` no macOS/Ubuntu).
4. Script marca $T_0$ no disparo do executável; add-on marca $T_{\text{render}}$ em `deck_browser_did_render`.
5. $T_{\text{inicializacao}} = T_{\text{render}} - T_0$.
6. Transição para revisão: clique no baralho; add-on marca até `reviewer_did_show_question` ($T_{\text{revisao}}$).
7. Salvar em `resultados_cenario1_<SO>.csv`.

### Cenário 2: Repouso vs. estresse (Q2 e Q4)

#### A. Repouso basal (5 minutos)

1. Abrir o Anki com coleção padrão limpa.
2. Não tocar no teclado/mouse por 5 minutos.
3. `coletor.py --cenario repouso --duracao 300` (amostragem 1 s): CPU total, RSS (MB), I/O (KB/s).
4. No Ubuntu, em paralelo: `pidstat -t -u -p $(pgrep anki) 1 300 > threads_repouso.txt`.

#### B. Estresse (coleção 100k cards)

1. Carregar `colecao_100k.anki2`.
2. `coletor.py --cenario estresse`.
3. Sequência: Browse → Todos os cartões → ordenar por Modificado → busca `card:*` → Verificar banco de dados.
4. No Ubuntu: `pidstat -t -u -w -p $(pgrep anki) 1 > threads_estresse.txt`. Avaliar se a Main Thread (Qt) manteve &lt; 15% de CPU sem bloqueio da UI.

### Cenário 3: Capacidade e vazão (Q3)

Massas: 10k, 50k e 100k cards.

1. Carregar a coleção; rodar *Check Database*; cronometrar $T_{\text{exec}}$.
2. Vazão = $N_{\text{cards}} / T_{\text{exec}}$ (em minutos).
3. Repetir para 50k e 100k.
4. Degradação = $(\text{Vazão}_{100k} - \text{Vazão}_{10k}) / \text{Vazão}_{10k} \times 100$.
5. Salvar em `resultados_capacidade_<SO>.csv`.

## 4. Registro de dados e resultados empíricos

Pasta oficial de evidências: `avaliacao/dados/desempenho/bruto/`, com padrão de nomenclatura `<métrica>_<cenário>_<SO>_<execução>.csv` (ver [Fase 4](../../fase4.md#organizacao-dos-dados)).

### 4.1 Matriz de faixas de julgamento GQM

| Métrica / Questão GQM | Insatisfatório | Mínimo | Alvo | Excelente |
| :--- | :---: | :---: | :---: | :---: |
| $T_{\text{inicializacao}}$ (cold start - Q1) | &gt; 9 s | 6 s &lt; T ≤ 9 s | 3 s &lt; T ≤ 6 s | ≤ 3 s |
| $T_{\text{revisao}}$ (tempo de transição) | &gt; 3 s | 2 s &lt; T ≤ 3 s | 1 s &lt; T ≤ 2 s | ≤ 1 s |
| RAM em repouso basal (Q2) | &gt; 800 MB | 400 a 800 MB | 250 a 400 MB | ≤ 250 MB |
| CPU em repouso basal (média - Q2) | &gt; 10% | 5% a 10% | 2% a 5% | ≤ 2% |
| Pico de RAM sob estresse (100k cards - Q2) | &gt; 1,5 GB | 1,0 a 1,5 GB | 600 MB a 1,0 GB | ≤ 600 MB |
| CPU da Main Thread sob carga (Q4) | &gt; 50% | 30% a 50% | 15% a 30% | ≤ 15% |
| Vazão de processamento (Q3) | &lt; 10.000 cards/min | 10.000 a 30.000 | 30.000 a 60.000 | ≥ 60.000 |

### 4.2 Resultados consolidados de laboratório (Ubuntu 24.04 LTS / Anki 26.09.3)

A bateria completa de testes instrumentados executada no ambiente Linux de referência gerou os seguintes resultados:

| Métrica / Questão GQM | Valor Empírico Coletado | Faixa no Protocolo | Julgamento GQM | Arquivo de Origem (Bruto) |
| :--- | :---: | :---: | :---: | :--- |
| **$T_{\text{inicialização}}$ (Cold Start - Q1)** | **`1.018 s`** | $\le 3\text{ s}$ | 🟢 **Excelente** | [`T_ini_coldstart_ubuntu_01.csv`](../dados/desempenho/bruto/T_ini_coldstart_ubuntu_01.csv) |
| **CPU em Repouso Basal (Q2)** | **`0.04%`** | $\le 2.0\%$ | 🟢 **Excelente** | [`CPU_repouso_ubuntu_01.csv`](../dados/desempenho/bruto/CPU_repouso_ubuntu_01.csv) |
| **RAM RSS em Repouso Basal (Q2)** | **`783.89 MB`** | $400\text{ a }800\text{ MB}$ | 🟡 **Mínimo** | [`CPU_repouso_ubuntu_01.csv`](../dados/desempenho/bruto/CPU_repouso_ubuntu_01.csv) |
| **Isolamento de Threads / UI (Q4)** | **`2.35%`** (Pico: $21.0\%$) | $\le 15.0\%$ | 🟢 **Excelente** | [`threads_estresse_ubuntu_01.csv`](../dados/desempenho/bruto/threads_estresse_ubuntu_01.csv) |
| **Pico de RAM sob Estresse (100k - Q2)** | **`1.328,13 MB`** ($1.33\text{ GB}$) | $1.0\text{ a }1.5\text{ GB}$ | 🟡 **Mínimo** | [`metricas_estresse_ubuntu_01.csv`](../dados/desempenho/bruto/metricas_estresse_ubuntu_01.csv) |
| **Pico de Escrita no SSD (I/O)** | **`228.4 MB/s`** ($228.416\text{ KB/s}$) | Capacidade NVMe | 🟢 **Nominal** | [`metricas_estresse_ubuntu_01.csv`](../dados/desempenho/bruto/metricas_estresse_ubuntu_01.csv) |
| **Vazão Check Database (Q3)** | **$\approx 2.000.000\text{ cards/min}$** ($3.0\text{s}$) | $\ge 60.000\text{ cards/min}$ | 🟢 **Excelente** | [`metricas_estresse_ubuntu_01.csv`](../dados/desempenho/bruto/metricas_estresse_ubuntu_01.csv) |

*(Nota de Rastreabilidade: Os dados coletados em ambiente Windows 11 pela integrante Karolina Vieira Barbosa estão versionados sob o padrão `threads_*windows*.csv` conforme catalogado na [Fase 4](../../fase4.md#organizacao-dos-dados)).*

### 4.3 Análise técnica aprofundada: consumo de RAM em repouso basal (783,89 MB - Q2)

O registro de **783,89 MB** de RSS em repouso basal (classificado como **Mínimo** no GQM) decorre da arquitetura interna moderna do Anki Desktop (versões 24 a 26) e da semântica de medição de memória do kernel Linux:

1. **Arquitetura Multi-Processo (QtWebEngine/Chromium):** O Anki não é uma aplicação puramente nativa; sua interface com o usuário (navegador de baralhos, barras de ferramentas e visualizador de cartões) é renderizada em instâncias integradas do Chromium via `PyQt6.QtWebEngineCore`.
2. **Decomposição da Árvore de Processos:** Uma inspeção detalhada da árvore de processos do Anki em repouso revela como o consumo se distribui:

| Processo / PID | Função Arquitetural | Memória Real (RSS) |
| :--- | :--- | :---: |
| `anki` (Processo Pai) | Runtime Python 3.13, motor Rust (`anki_rs`), SQLite | **~370 MB** |
| `QtWebEngineProcess` (Zygote 1) | Gerenciador de processos do Chromium | **~52 MB** |
| `QtWebEngineProcess` (Zygote 2) | Sandbox de segurança e IPC | **~53 MB** |
| `QtWebEngineProcess` (Renderer 1) | WebView do *Deck Browser* (HTML/CSS/JS) | **~99 MB** |
| `QtWebEngineProcess` (Renderer 2) | WebView da barra superior e menus | **~98 MB** |
| `QtWebEngineProcess` (Renderer 3) | WebView auxiliar / cache do *Reviewer* | **~106 MB** |
| **Soma Total da Árvore** | **Consumo agregado medido pelo coletor oficial** | **`~778 MB`** |

3. **Sobreposição de Bibliotecas Compartilhadas no RSS:** O *Resident Set Size* (RSS) computado para cada subprocesso contabiliza as páginas de memória física mapeadas, incluindo bibliotecas dinâmicas compartilhadas pesadas (como `libQt6WebEngineCore.so.6`, com mais de 200 MB em disco, drivers gráficos Mesa/Vulkan e fontes). Ao somar o RSS individual de cada filho da árvore, ocorre sobreposição de memória compartilhada.
4. **Alinhamento com o GQM:** Caso fosse computado unicamente o processo pai (`anki`), o consumo ficaria em ~370 MB (faixa **Alvo**). Ao medir a **árvore completa real** necessária para o software funcionar, o Anki situa-se estavelmente na faixa **Mínimo** (400 a 800 MB). Durante os 300 segundos de amostragem basal, o RSS variou menos de 0,5 MB, comprovando **ausência de vazamento de memória (Memory Leak)**.

### 4.4 Auditoria de isolamento de threads sob carga real (Q4)

A análise refinada com `analisador_threads.py` e `pidstat` comprovou a eficácia do isolamento entre a Main Thread (UI PyQt) e as Worker Threads (Rust/SQLite):
- **Em repouso:** Main Thread média de `0.03%` CPU; Workers média de `0.02%` CPU; 56 threads ativas.
- **Sob estresse (100k cards):** Durante o pico de verificação de integridade (*Check Database*), os Workers atingiram **`100.0%` de utilização da CPU** e I/O de escrita de **`228.4 MB/s`**, enquanto a Main Thread permaneceu em **`1.0%`** (média de `2.35%` e pico isolado de 21% apenas na exibição do modal conclusivo).
- O comportamento comprova que a interface gráfica não sofre congelamento perceptível pelo usuário mesmo sob estresse severo, atendendo plenamente à meta de $\le 15\%$ da faixa **Excelente**. O gráfico gerado está versionado em [`docs/avaliacao/dados/grafico_threads_estresse.png`](../dados/grafico_threads_estresse.png).

### 4.5 Avaliação de capacidade e vazão com 100.000 cards (Q3)

No Cenário 3, a rotina *Check Database* processou o baralho sintético de 100.000 notas em **$\approx 3,0\text{ segundos}$** ($T_{\text{exec}} \approx 0,05\text{ min}$):
$$\text{Vazão} = \frac{100.000\text{ cards}}{0,05\text{ min}} \approx 2.000.000\text{ cards/min}$$
O valor supera em mais de 30 vezes o limiar de $\ge 60.000\text{ cards/min}$, posicionando o motor Rust/SQLite na faixa **Excelente**.

## 5. Critérios de invalidação

Descartar e reiniciar a rodada se:

- Intervenção do SO alheia ao teste (Windows Update, Spotlight, `unattended-upgrades` consumindo &gt; 5% de CPU).
- Queda ou oscilação severa de rede na sincronização.
- Interação manual com a interface durante os 5 minutos de repouso.

## 6. Relação com o instrumento e com os dados

A dimensão humana (observação, perguntas pós-tarefa e Likert LIK-PERF) foi elaborada pela Dupla B e é aplicada pela Dupla A em todas as sessões com participantes, conforme a [Entrevista](entrevista.md) e o [Pré-entrevista com participante](pre-entrevista-participante.md). Esta página cobre apenas a medição instrumentada de laboratório. A visão das três frentes está em [Fase 3](../../fase3.md).
