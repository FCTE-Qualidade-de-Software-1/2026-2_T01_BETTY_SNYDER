#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
FCTE / UnB - Qualidade de Software 1 (2026-2)
Grupo 01: Betty Snyder | Dupla B: Eficiência de Desempenho
Script: analisador_threads.py (Atendimento à Questão Q4 - Issue #56 / E2-21)
Autores: Karolina Vieira Barbosa e Mateus de Siqueira Silva
===============================================================================
Finalidade:
  Monitorar e auditar o isolamento entre a Main Thread (interface gráfica PyQt)
  e as Worker Threads de segundo plano (motor SQLite / backend em Rust) do Anki,
  atendendo rigorosamente aos critérios da Questão Q4:
    - docs/avaliacao/protocolos/desempenho.md (Seção 3, Cenário 2B e Seção 4)

Critérios de Julgamento GQM (Q4 - CPU da Main Thread sob Carga de 100k):
  - Excelente:      CPU_Main <= 15.0%
  - Alvo:           15.0% < CPU_Main <= 30.0%
  - Mínimo:         30.0% < CPU_Main <= 50.0%
  - Insatisfatório: CPU_Main > 50.0%

Modos de Operação:
  1. Tempo Real (--modo realtime):
     Inspeciona periodicamente os TIDs do Anki via /proc/<PID>/task/
     calculando CPU individual da Main Thread e das Worker Threads.
     Exemplo:
       python3 analisador_threads.py --modo realtime --duracao 180 --cenario estresse

  2. Parser de Dump pidstat (--modo parse):
     Processa um arquivo gerado previamente pelo utilitário do Linux:
       pidstat -t -u -w -p $(pgrep anki) 1 180 > threads_estresse.txt
     Exemplo:
       python3 analisador_threads.py --modo parse --arquivo threads_estresse.txt
===============================================================================
"""

import sys
import os
import time
import argparse
import re
import csv
from datetime import datetime
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None


# =============================================================================
# Constantes & Critérios GQM (Questão Q4)
# =============================================================================
GQM_Q4_THRESHOLDS = {
    "excelente": (0.0, 15.0),
    "alvo": (15.0, 30.0),
    "minimo": (30.0, 50.0),
    "insatisfatorio": (50.0, float("inf")),
}


def classificar_gqm_q4(cpu_main_pct: float) -> str:
    """Enquadra a taxa de uso da Main Thread nas faixas oficiais do GQM."""
    for nivel, (lim_inf, lim_sup) in GQM_Q4_THRESHOLDS.items():
        if lim_inf <= cpu_main_pct <= lim_sup:
            return nivel.capitalize()
    return "N/D"


def obter_caminho_saida_padrao(cenario: str) -> Path:
    """Retorna o caminho padronizado na pasta docs/avaliacao/dados/."""
    base_dir = Path(__file__).resolve().parent.parent / "dados"
    base_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_dir / f"threads_{cenario}_ubuntu_{timestamp}.csv"


def encontrar_pid_anki(pid_informado: int = None) -> int:
    """Localiza o PID principal do Anki."""
    if pid_informado:
        return pid_informado

    if psutil is None:
        # Fallback via /proc
        for entry in os.listdir("/proc"):
            if entry.isdigit():
                try:
                    with open(f"/proc/{entry}/cmdline", "rb") as f:
                        cmd = f.read().decode("utf-8", errors="ignore").lower()
                        if "anki" in cmd and "analisador_threads.py" not in cmd:
                            return int(entry)
                except (IOError, PermissionError):
                    continue
        return None

    candidatos = []
    for p in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            cmdline = " ".join(p.info["cmdline"] or []).lower()
            nome = (p.info["name"] or "").lower()
            if ("anki" in nome or "anki" in cmdline) and "analisador_threads.py" not in cmdline:
                candidatos.append(p.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return sorted(candidatos)[0] if candidatos else None


def ler_nome_thread(pid: int, tid: int) -> str:
    """Lê o nome descritivo da thread em /proc/[pid]/task/[tid]/comm."""
    caminho = f"/proc/{pid}/task/{tid}/comm"
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read().strip()
    except (IOError, PermissionError):
        return f"thread_{tid}"


# =============================================================================
# Modo 1: Monitoramento em Tempo Real via /proc e psutil
# =============================================================================
def executar_modo_realtime(pid: int, duracao: int, intervalo: float, saida_csv: Path, cenario: str):
    """Amostra periodicamente o consumo de CPU da Main Thread e Workers."""
    print("=" * 72)
    print("🔬 ANÁLISE DE THREADS EM TEMPO REAL (QUESTÃO Q4 - ISO/IEC 25010)")
    print(f"📌 PID Alvo: {pid} | Duração: {duracao}s | Taxa de Amostragem: {intervalo}s")
    print("=" * 72)

    if psutil is None:
        print("[ERRO CRÍTICO] psutil não está instalado. Execute: pip install psutil")
        sys.exit(1)

    try:
        proc = psutil.Process(pid)
    except psutil.NoSuchProcess:
        print(f"[ERRO] Processo com PID {pid} não encontrado.")
        sys.exit(1)

    print(f"✅ Anki detectado: PID {pid} ({proc.name()})")
    print(f"📁 Destino CSV: {saida_csv}")
    print("Iniciando amostragem... Pressione Ctrl+C para finalizar.\n")

    tempos_anteriores = {}
    tempo_clock_anterior = time.time()

    def coletar_tempos_tids():
        dados = {}
        task_dir = f"/proc/{pid}/task"
        if not os.path.exists(task_dir):
            return dados
        for tid_str in os.listdir(task_dir):
            if not tid_str.isdigit():
                continue
            tid = int(tid_str)
            stat_path = f"{task_dir}/{tid_str}/stat"
            try:
                with open(stat_path, "r") as f:
                    conteudo = f.read()
                partes = conteudo.rsplit(")", 1)[-1].split()
                utime = int(partes[11])
                stime = int(partes[12])
                dados[tid] = utime + stime
            except (IOError, IndexError, ValueError):
                continue
        return dados

    clock_ticks = os.sysconf(os.sysconf_names.get("SC_CLK_TCK", 100))
    tempos_anteriores = coletar_tempos_tids()
    time.sleep(intervalo)

    amostras = []
    segundo = 0

    cabecalho = [
        "segundo",
        "timestamp_iso",
        "cpu_main_thread_pct",
        "cpu_workers_total_pct",
        "cpu_processo_total_pct",
        "qtd_threads_ativas",
        "nome_main_thread",
        "classificacao_gqm_q4",
    ]

    try:
        with open(saida_csv, mode="w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerow(cabecalho)

            while segundo < duracao or duracao <= 0:
                t_atual = time.time()
                dt = t_atual - tempo_clock_anterior
                if dt <= 0:
                    dt = intervalo

                if not proc.is_running():
                    print("\n[ALERTA] Processo do Anki finalizou durante a coleta.")
                    break

                tempos_atuais = coletar_tempos_tids()
                cpu_main = 0.0
                cpu_workers = 0.0

                for tid, ticks_total in tempos_atuais.items():
                    if tid in tempos_anteriores:
                        delta_ticks = max(0, ticks_total - tempos_anteriores[tid])
                        cpu_tid = (delta_ticks / clock_ticks / dt) * 100.0
                        if tid == pid:
                            cpu_main += cpu_tid
                        else:
                            cpu_workers += cpu_tid

                cpu_proc_total = cpu_main + cpu_workers
                qtd_threads = len(tempos_atuais)
                nome_main = ler_nome_thread(pid, pid)
                nivel_gqm = classificar_gqm_q4(cpu_main)

                linha = [
                    segundo,
                    datetime.now().isoformat(),
                    round(cpu_main, 2),
                    round(cpu_workers, 2),
                    round(cpu_proc_total, 2),
                    qtd_threads,
                    nome_main,
                    nivel_gqm,
                ]
                writer.writerow(linha)
                f_out.flush()

                amostras.append({
                    "cpu_main": cpu_main,
                    "cpu_workers": cpu_workers,
                    "cpu_total": cpu_proc_total,
                })

                print(
                    f"[{segundo:03d}s] Main Thread (UI): {cpu_main:5.1f}% | "
                    f"Workers: {cpu_workers:5.1f}% | "
                    f"Total: {cpu_proc_total:5.1f}% | "
                    f"Threads: {qtd_threads:2d} | GQM: [{nivel_gqm.upper()}]"
                )

                tempos_anteriores = tempos_atuais
                tempo_clock_anterior = t_atual
                segundo += int(intervalo)
                time.sleep(intervalo)

    except KeyboardInterrupt:
        print("\n[INFO] Coleta interrompida pelo operador.")

    imprimir_resumo_q4(amostras, saida_csv)


# =============================================================================
# Modo 2: Parser de Dump gerado pelo comando `pidstat -t`
# =============================================================================
def executar_modo_parse(caminho_arquivo: Path, saida_csv: Path):
    """
    Processa arquivos gerados por:
      pidstat -t -u -w -p <PID> 1 <DURACAO> > threads.txt
    """
    print("=" * 72)
    print("📄 PROCESSAMENTO DE LOG PIDSTAT (QUESTÃO Q4 - ISO/IEC 25010)")
    print(f"📁 Arquivo de entrada: {caminho_arquivo}")
    print("=" * 72)

    if not caminho_arquivo.exists():
        print(f"[ERRO] O arquivo informado não existe: {caminho_arquivo}")
        sys.exit(1)

    amostras_por_segundo = {}
    padrao_linha = re.compile(
        r"^\s*(\d{2}:\d{2}:\d{2})\s+\d+\s+(\d+|-)\s+(\d+)\s+([\d\.]+)\s+([\d\.]+)\s+[\d\.]*\s*[\d\.]*\s+([\d\.]+)\s+\d+\s+(.*)$"
    )

    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            match = padrao_linha.match(linha.strip())
            if not match:
                continue

            hora, tgid, tid_str, usr, sys_cpu, cpu_str, cmd = match.groups()
            tid = int(tid_str)
            cpu_val = float(cpu_str.replace(",", "."))

            if hora not in amostras_por_segundo:
                amostras_por_segundo[hora] = {"main": 0.0, "workers": 0.0, "tids": {}}

            is_main = (tgid != "-" and tgid == tid_str) or cmd.strip() in ["anki", "python3"]

            if is_main:
                amostras_por_segundo[hora]["main"] += cpu_val
            else:
                amostras_por_segundo[hora]["workers"] += cpu_val

            amostras_por_segundo[hora]["tids"][tid] = cpu_val

    if not amostras_por_segundo:
        print("[ERRO] Nenhuma linha válida de métrica encontrada no log do pidstat.")
        sys.exit(1)

    amostras = []
    with open(saida_csv, mode="w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow([
            "timestamp",
            "cpu_main_thread_pct",
            "cpu_workers_total_pct",
            "cpu_processo_total_pct",
            "qtd_threads",
            "classificacao_gqm_q4",
        ])

        for hora, dados in amostras_por_segundo.items():
            cpu_main = dados["main"]
            cpu_workers = dados["workers"]
            cpu_total = cpu_main + cpu_workers
            nivel_gqm = classificar_gqm_q4(cpu_main)

            writer.writerow([
                hora,
                round(cpu_main, 2),
                round(cpu_workers, 2),
                round(cpu_total, 2),
                len(dados["tids"]),
                nivel_gqm,
            ])

            amostras.append({
                "cpu_main": cpu_main,
                "cpu_workers": cpu_workers,
                "cpu_total": cpu_total,
            })

    imprimir_resumo_q4(amostras, saida_csv)


def imprimir_resumo_q4(amostras: list, saida_csv: Path):
    """Exibe o sumário com auditoria formal GQM para a Questão Q4."""
    if not amostras:
        return

    mains = [a["cpu_main"] for a in amostras]
    workers = [a["cpu_workers"] for a in amostras]
    totais = [a["cpu_total"] for a in amostras]

    media_main = sum(mains) / len(mains)
    pico_main = max(mains)
    media_workers = sum(workers) / len(workers)
    media_total = sum(totais) / len(totais)

    razao_main_total = (media_main / media_total * 100.0) if media_total > 0 else 0.0
    nivel_final = classificar_gqm_q4(media_main)

    print("\n" + "=" * 72)
    print("📊 RESULTADO CONSOLIDADO DA AUDITORIA DE THREADS (QUESTÃO Q4)")
    print("=" * 72)
    print(f"Total de Janelas Avaliadas: {len(amostras)} segundos")
    print(f"CPU Média da Main Thread (UI):      {media_main:5.2f}% (Pico: {pico_main:5.2f}%)")
    print(f"CPU Média das Worker Threads (Back): {media_workers:5.2f}%")
    print(f"Consumo Médio Agregado do Anki:     {media_total:5.2f}%")
    print(f"Sobrecarga da UI sobre Carga Total: {razao_main_total:5.1f}%")
    print("-" * 72)
    print("🎯 ENQUADRAMENTO GQM (ISO/IEC 25010 / QUESTÃO Q4):")
    print(f"  • Nível Conquistado: [{nivel_final.upper()}]")
    print("  • Faixas Oficiais do Protocolo:")
    print("      - Excelente:      <= 15.0% (Interface totalmente responsiva)")
    print("      - Alvo:           15.0% a 30.0%")
    print("      - Mínimo:         30.0% a 50.0%")
    print("      - Insatisfatório: > 50.0% (Risco severo de engasgo/bloqueio de UI)")
    print("-" * 72)
    print(f"💾 Relatório CSV salvo em:\n   {saida_csv}")
    print("=" * 72)


# =============================================================================
# 🎨 TODO (Karolina Vieira Barbosa - Dupla B): Geração de Gráficos para o PC2
# =============================================================================
# Tarefa delegada para os slides do Ponto de Controle 2 (16/11):
#
# Requisitos:
#   1. Ler o arquivo CSV gerado (caminho_csv).
#   2. Utilizar 'matplotlib' (ou 'seaborn') para plotar:
#      - Eixo X: 'segundo' (tempo de esforço do teste).
#      - Eixo Y: 'cpu_main_thread_pct' e 'cpu_workers_total_pct'.
#      - Linha de Referência GQM (Horizontal Vermelha Tracejada em 15.0%):
#        Indica o teto da faixa 'Excelente' da Questão Q4 (ISO/IEC 25010).
#   3. Adicionar título, legenda e anotação do enquadramento conquistado.
#   4. Salvar o gráfico em alta resolução (300 DPI) em:
#      'docs/avaliacao/dados/grafico_threads_<cenario>.png'.
# =============================================================================
def gerar_grafico_threads(caminho_csv: Path, saida_png: Path = None):
    """
    TODO (Karolina): Implementar a renderização visual com matplotlib.
    Exemplo de esqueleto sugerido:
    
    try:
        import matplotlib.pyplot as plt
        import csv
        
        segundos, cpu_main, cpu_workers = [], [], []
        with open(caminho_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                segundos.append(int(row["segundo"]))
                cpu_main.append(float(row["cpu_main_thread_pct"]))
                cpu_workers.append(float(row["cpu_workers_total_pct"]))
                
        plt.figure(figsize=(10, 5))
        plt.plot(segundos, cpu_main, label="Main Thread (PyQt UI)", color="#2563eb", linewidth=2)
        plt.plot(segundos, cpu_workers, label="Worker Threads (Rust/SQLite)", color="#10b981", linewidth=1.5, linestyle="--")
        plt.axhline(y=15.0, color="#ef4444", linestyle=":", label="Teto GQM Excelente (15%)")
        
        plt.title("Isolamento de Threads no Anki sob Carga (Questão Q4 - ISO/IEC 25010)")
        plt.xlabel("Tempo de Execução (s)")
        plt.ylabel("Uso de CPU (%)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if not saida_png:
            saida_png = caminho_csv.with_suffix(".png")
        plt.savefig(saida_png, dpi=300, bbox_inches="tight")
        print(f"📊 Gráfico gerado com sucesso em: {saida_png}")
        
    except ImportError:
        print("[AVISO] matplotlib não instalado. Instale com: pip install matplotlib")
    """
    pass


def main():
    parser = argparse.ArgumentParser(
        description="Auditor de Isolamento de Threads do Anki (Questão Q4 - Betty Snyder / Dupla B)"
    )
    parser.add_argument(
        "--modo",
        choices=["realtime", "parse"],
        default="realtime",
        help="Modo de operação: 'realtime' para monitorar processo ativo ou 'parse' para analisar arquivo pidstat.",
    )
    parser.add_argument(
        "--cenario",
        choices=["repouso", "estresse"],
        default="estresse",
        help="Cenário de medição (repouso ou estresse).",
    )
    parser.add_argument(
        "--duracao",
        type=int,
        default=180,
        help="Duração em segundos para o modo realtime (Padrão: 180s para estresse).",
    )
    parser.add_argument(
        "--intervalo",
        type=float,
        default=1.0,
        help="Intervalo de amostragem em segundos (Padrão: 1.0s).",
    )
    parser.add_argument(
        "--pid",
        type=int,
        default=None,
        help="PID específico do processo Anki a ser auditado.",
    )
    parser.add_argument(
        "--arquivo",
        type=str,
        default=None,
        help="Caminho do arquivo txt gerado pelo pidstat para o modo 'parse'.",
    )
    parser.add_argument(
        "--saida",
        type=str,
        default=None,
        help="Caminho de saída personalizado para o arquivo CSV de métricas.",
    )
    parser.add_argument(
        "--grafico",
        action="store_true",
        default=False,
        help="Gera automaticamente a imagem PNG com as curvas das threads para o PC2 (TODO Karolina).",
    )

    args = parser.parse_args()

    saida_csv = Path(args.saida) if args.saida else obter_caminho_saida_padrao(args.cenario)

    if args.modo == "parse":
        if not args.arquivo:
            print("[ERRO] No modo 'parse', forneça o caminho do arquivo com --arquivo <caminho.txt>")
            sys.exit(1)
        executar_modo_parse(Path(args.arquivo), saida_csv)
    else:
        pid = encontrar_pid_anki(args.pid)
        if not pid:
            print("[ERRO] Processo do Anki não localizado em execução.")
            print("Abra o Anki antes de executar no modo realtime ou informe o PID com --pid <NUM>.")
            sys.exit(1)
        executar_modo_realtime(
            pid=pid,
            duracao=args.duracao,
            intervalo=args.intervalo,
            saida_csv=saida_csv,
            cenario=args.cenario,
        )

    if args.grafico:
        gerar_grafico_threads(saida_csv)


if __name__ == "__main__":
    main()
