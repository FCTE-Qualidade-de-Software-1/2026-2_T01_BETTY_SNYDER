# Scripts de Avaliação de Desempenho (ISO/IEC 25010)

Este diretório contém o ferramental automatizado desenvolvido pela **Dupla B (Karolina Vieira Barbosa e Mateus de Siqueira Silva)** para a coleta e análise de Eficiência de Desempenho (G2) do **Anki Desktop 26.09.3**, em conformidade com o método **GQM (Goal-Question-Metric)** e o modelo **PSM (Practical Software Measurement)** da disciplina Qualidade de Software 1 (FCTE/UnB).

---

## 📁 Estrutura de Ferramentas

| Script | Função Principal | Sistemas Suportados |
| :--- | :--- | :--- |
| [`coletor.py`](coletor.py) | Coleta de CPU, RAM (RSS/VMS), I/O de disco e medição de Cold Start | Ubuntu, Windows, macOS |
| [`analisador_threads.py`](analisador_threads.py) | Auditoria de isolamento entre Main Thread (UI PyQt) e Worker Threads (Rust/SQLite) com geração de gráficos | Ubuntu (`pidstat` / `/proc`), Windows (`psutil`), macOS (`psutil`) |
| [`gerar_colecoes.py`](gerar_colecoes.py) | Gerador de massas sintéticas de teste (10k, 50k, 100k cartões) nos formatos `.txt` e `.apkg` | Multiplataforma |
| [`coletar_ambiente.py`](coletar_ambiente.py) | Detecção e caracterização do hardware e sistema operacional da máquina de teste | Multiplataforma |
| [`executar_testes.sh`](executar_testes.sh) | Menu interativo de automação dos testes de laboratório | Linux (Ubuntu) e macOS |
| [`executar_testes.cmd`](executar_testes.cmd) | Menu interativo de automação dos testes de laboratório | Windows (CMD / Batch) |

---

## 🚀 Como Executar os Scripts por Sistema Operacional

### 1. Windows 10 / 11

#### Opção A: Via Menu Interativo (`executar_testes.cmd`)
1. Abra o **Prompt de Comando (CMD)** ou **PowerShell**.
2. Navegue até a pasta do repositório:
   ```cmd
   cd C:\caminho\para\2026-2_T01_BETTY_SNYDER
   docs\avaliacao\scripts\executar_testes.cmd
   ```
3. Escolha o cenário desejado no menu de [1] a [6].

#### Opção B: Comandos Diretos no Terminal
* **Pré-requisito:** Instalar dependências necessárias:
  ```cmd
  py -3 -m pip install psutil matplotlib
  ```
* **Cenário 1: Cold Start:**
  1. Feche o Anki (`Ctrl + Shift + Esc`).
  2. Esvazie a lista de espera no RAMMap (*Empty → Empty Standby List*) ou reinicie a máquina.
  3. Execute:
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario cold_start --saida docs\avaliacao\dados\desempenho\bruto\T_ini_coldstart_windows_01.csv
     ```
* **Cenário 2A: Repouso Basal (5 minutos):**
  1. Abra o Anki com coleção limpa e deixe sem mexer.
  2. Execute:
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario repouso --duracao 300 --saida docs\avaliacao\dados\desempenho\bruto\CPU_repouso_windows_01.csv
     ```
* **Cenário 2B: Estresse de Recursos (100k cards):**
  1. Abra a coleção sintética de 100k.
  2. Dispare o coletor e execute as operações no Anki (*Browse → Ordenar por Modificado → Verificar Banco de Dados*):
     ```cmd
     py -3 docs\avaliacao\scripts\coletor.py --cenario estresse --duracao 180 --saida docs\avaliacao\dados\desempenho\bruto\metricas_estresse_windows_01.csv
     ```
* **Auditoria de Threads (Q4):**
  ```cmd
  py -3 docs\avaliacao\scripts\analisador_threads.py --modo realtime --duracao 180 --cenario estresse --saida docs\avaliacao\dados\desempenho\bruto\threads_estresse_windows_01.csv --grafico
  ```

---

### 2. macOS

#### Opção A: Via Menu Interativo (`executar_testes.sh`)
1. Abra o **Terminal**.
2. Dê permissão de execução (se necessário) e inicie:
   ```bash
   cd /caminho/para/2026-2_T01_BETTY_SNYDER
   chmod +x docs/avaliacao/scripts/executar_testes.sh
   ./docs/avaliacao/scripts/executar_testes.sh
   ```

#### Opção B: Comandos Diretos no Terminal
* **Instalação das dependências:**
  ```bash
  python3 -m pip install psutil matplotlib
  ```
* **Cenário 1: Cold Start:**
  1. Feche o Anki (`pkill -f Anki` ou `Cmd + Q`).
  2. Limpe os caches de disco do macOS:
     ```bash
     sudo purge
     ```
  3. Execute o coletor:
     ```bash
     python3 docs/avaliacao/scripts/coletor.py --cenario cold_start --saida docs/avaliacao/dados/desempenho/bruto/T_ini_coldstart_macos_01.csv
     ```
* **Cenário 2A: Repouso Basal:**
  ```bash
  python3 docs/avaliacao/scripts/coletor.py --cenario repouso --duracao 300 --saida docs/avaliacao/dados/desempenho/bruto/CPU_repouso_macos_01.csv
  ```
* **Cenário 2B: Estresse de Recursos:**
  ```bash
  python3 docs/avaliacao/scripts/coletor.py --cenario estresse --duracao 180 --saida docs/avaliacao/dados/desempenho/bruto/metricas_estresse_macos_01.csv
  ```

---

### 3. Linux (Ubuntu 24.04 LTS)

#### Opção A: Via Menu Interativo (`executar_testes.sh`)
```bash
cd /home/siqueira-prog/2026-2_T01_BETTY_SNYDER
./docs/avaliacao/scripts/executar_testes.sh
```

#### Opção B: Comandos Diretos
* **Cenário 1: Cold Start:**
  ```bash
  pkill -f anki
  sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
  python3 docs/avaliacao/scripts/coletor.py --cenario cold_start --saida docs/avaliacao/dados/desempenho/bruto/T_ini_coldstart_ubuntu_01.csv
  ```
* **Cenário 2A: Repouso Basal (300s):**
  ```bash
  python3 docs/avaliacao/scripts/coletor.py --cenario repouso --duracao 300 --saida docs/avaliacao/dados/desempenho/bruto/CPU_repouso_ubuntu_01.csv
  ```
* **Cenário 2B: Estresse com Gráfico de Threads:**
  ```bash
  python3 docs/avaliacao/scripts/coletor.py --cenario estresse --duracao 180 --saida docs/avaliacao/dados/desempenho/bruto/metricas_estresse_ubuntu_01.csv
  python3 docs/avaliacao/scripts/analisador_threads.py --modo realtime --duracao 180 --cenario estresse --saida docs/avaliacao/dados/desempenho/bruto/threads_estresse_ubuntu_01.csv --grafico
  ```

---

## 🎯 Padrão de Nomenclatura dos Arquivos de Saída

Conforme a convenção estabelecida em [Dados](../../dados.md):
- `<métrica>_<cenário>_<sistema_operacional>_<rodada>.csv`
- Exemplo: `CPU_repouso_ubuntu_01.csv`, `T_ini_coldstart_windows_01.csv`.
- **Regra de Governança:** Arquivos contendo `windows` pertencem às rodadas em Windows 11 e **não devem ser sobrescritos** por execuções em outros sistemas operacionais.
