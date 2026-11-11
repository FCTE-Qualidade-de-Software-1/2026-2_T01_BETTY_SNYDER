# Eficiência de desempenho

## 1. Definições

Esta página descreve a coleta **instrumentada** de Eficiência de desempenho (G2), executada pela Dupla B (Karolina Vieira Barbosa e Mateus de Siqueira Silva). As definições formais das métricas e as faixas de julgamento estão na [Fase 2](../../fase2.md). O bloco de eficiência percebida, elaborado pela Dupla B, é aplicado pela Dupla A na [entrevista](entrevista.md) e no [Pré-entrevista com participante](pre-entrevista-participante.md).

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

### 2.1 Orientações por sistema operacional

#### Windows 10/11

1. Tomada; em *Configurações → Sistema → Energia e bateria*, modo **Melhor desempenho** quando disponível.
2. Encerrar processos (`Ctrl + Shift + Esc`).
3. Confirmar CPU basal &lt; 2% no Gerenciador de Tarefas.
4. Durante a medição, acompanhar o processo do Anki (Detalhes / `resmon`).
5. Coletor: `py -3 coletor.py --cenario repouso --duracao 300` (ou `estresse` / `cold_start`). Se `py` faltar, usar `python`.
6. *Cold start:* reinício entre baterias ou RAMMap (**Empty → Empty Standby List**); registrar o método e manter consistente.
7. Registrar edição/versão do Windows e o hardware.

#### macOS

1. Tomada; desativar Modo de Pouca Energia se ativo.
2. Encerrar processos; Monitor de Atividade.
3. Confirmar CPU basal &lt; 2%.
4. Acompanhar % CPU e Memória do Anki.
5. Coletor: `python3 coletor.py --cenario ...`.
6. *Cold start:* `sudo purge` ou reinício; registrar o método.
7. Registrar versão do macOS e hardware.

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

## 4. Registro de dados

Pasta: `avaliacao/dados/desempenho/bruto/`, padrão `<métrica>_<cenário>_<execução>` (ver [Dados](../../dados.md)). Exemplos: `T_ini_coldstart_01.csv`, `CPU_repouso_win11_01.csv`.

Enquadramento nas faixas (matriz usada neste protocolo de medição):

| Métrica | Insatisfatório | Mínimo | Alvo | Excelente |
| --- | --- | --- | --- | --- |
| $T_{\text{inicializacao}}$ (cold start) | &gt; 9 s | 6 s &lt; T ≤ 9 s | 3 s &lt; T ≤ 6 s | ≤ 3 s |
| $T_{\text{revisao}}$ | &gt; 3 s | 2 s &lt; T ≤ 3 s | 1 s &lt; T ≤ 2 s | ≤ 1 s |
| RAM em repouso | &gt; 800 MB | 400 a 800 MB | 250 a 400 MB | ≤ 250 MB |
| CPU em repouso (média) | &gt; 10% | 5% a 10% | 2% a 5% | ≤ 2% |
| Pico de RAM sob estresse | &gt; 1,5 GB | 1,0 a 1,5 GB | 600 MB a 1,0 GB | ≤ 600 MB |
| CPU da Main Thread sob carga | &gt; 50% | 30% a 50% | 15% a 30% | ≤ 15% |
| Vazão | &lt; 10.000 cards/min | 10.000 a 30.000 | 30.000 a 60.000 | ≥ 60.000 |

## 5. Critérios de invalidação

Descartar e reiniciar a rodada se:

- Intervenção do SO alheia ao teste (Windows Update, Spotlight, `unattended-upgrades` consumindo &gt; 5% de CPU).
- Queda ou oscilação severa de rede na sincronização.
- Interação manual com a interface durante os 5 minutos de repouso.

## 6. Relação com o instrumento e com os dados

A dimensão humana (observação, perguntas pós-tarefa e Likert LIK-PERF) foi elaborada pela Dupla B e é aplicada pela Dupla A em todas as sessões com participantes, conforme a [Entrevista](entrevista.md) e o [Pré-entrevista com participante](pre-entrevista-participante.md). Esta página cobre apenas a medição instrumentada de laboratório. A visão das três frentes está em [Protocolos](index.md).
