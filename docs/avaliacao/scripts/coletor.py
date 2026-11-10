#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
FCTE / UnB - Qualidade de Software 1 (2026-2)
Grupo 01: Betty Snyder
Instrumentação de Eficiência de Desempenho (ISO/IEC 25010)
Script: coletor.py (Issue #56 / E2-21)
===============================================================================
Finalidade:
  Monitorar e coletar métricas de consumo de recursos do software Anki
  (CPU total, Memória RSS/VMS, Taxa de I/O de disco e contagem de threads)
  de forma padronizada e multiplataforma (Linux/Ubuntu, Windows 10/11 e macOS),
  atendendo rigorosamente ao protocolo oficial:
  'docs/avaliacao/protocolos/desempenho.md'.

Uso:
  # Repouso basal (5 minutos = 300 segundos com amostragem de 1s)
  python3 coletor.py --cenario repouso --duracao 300

  # Estresse com carga máxima (100k cards)
  python3 coletor.py --cenario estresse --duracao 180

  # Inicialização a Frio (Cold Start)
  python3 coletor.py --cenario cold_start

Requisitos:
  pip install psutil
===============================================================================
"""

import sys
import os
import time
import argparse
import platform
import csv
import subprocess
from datetime import datetime
from pathlib import Path

try:
    import psutil
except ImportError:
    print("\n[ERRO CRÍTICO] A biblioteca 'psutil' é necessária para a execução do coletor.")
    print("Instale-a executando:")
    print("    pip install psutil\n")
    sys.exit(1)


# =============================================================================
# Constantes & Critérios GQM (docs/avaliacao/protocolos/desempenho.md)
# =============================================================================
GQM_THRESHOLDS = {
    "repouso_ram_mb": {
        "excelente": (0, 250),
        "alvo": (250, 400),
        "minimo": (400, 800),
        "insatisfatorio": (800, float("inf")),
    },
    "repouso_cpu_pct": {
        "excelente": (0, 2.0),
        "alvo": (2.0, 5.0),
        "minimo": (5.0, 10.0),
        "insatisfatorio": (10.0, float("inf")),
    },
    "estresse_pico_ram_mb": {
        "excelente": (0, 600),
        "alvo": (600, 1000),
        "minimo": (1000, 1500),
        "insatisfatorio": (1500, float("inf")),
    },
    "cold_start_seg": {
        "excelente": (0, 3.0),
        "alvo": (3.0, 6.0),
        "minimo": (6.0, 9.0),
        "insatisfatorio": (9.0, float("inf")),
    },
}


def identificar_so() -> str:
    """Retorna o identificador amigável do sistema operacional."""
    sistema = platform.system().lower()
    if "linux" in sistema:
        return "ubuntu"
    elif "darwin" in sistema:
        return "macos"
    elif "windows" in sistema:
        return "windows"
    return "desconhecido"


def obter_caminho_saida_padrao(cenario: str, so: str) -> Path:
    """Calcula o caminho padrão para gravação dos resultados."""
    base_dir = Path(__file__).resolve().parent.parent / "dados"
    base_dir.mkdir(parents=True, exist_ok=True)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_dir / f"metricas_{cenario}_{so}_{timestamp_str}.csv"


def encontrar_processo_anki(pid_informado: int = None) -> psutil.Process:
    """Localiza o processo principal do Anki em execução."""
    if pid_informado:
        try:
            p = psutil.Process(pid_informado)
            if p.is_running():
                return p
        except psutil.NoSuchProcess:
            print(f"[AVISO] PID {pid_informado} informado não foi encontrado.")

    candidatos = []
    for p in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            nome = (p.info["name"] or "").lower()
            cmdline = " ".join(p.info["cmdline"] or []).lower()
            if "anki" in nome or "anki" in cmdline:
                # Evita selecionar este próprio script de coleta
                if "coletor.py" in cmdline:
                    continue
                candidatos.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not candidatos:
        return None

    # Se houver múltiplos, escolhe o de menor PID ou o que não for subprocesso do anki
    # Normalmente o processo pai é o launcher do Anki
    candidatos.sort(key=lambda proc: proc.pid)
    return candidatos[0]


def coletar_metricas_arvore(processo_pai: psutil.Process) -> dict:
    """
    Coleta dados agregados do processo pai e de todos os subprocessos filhos
    (ex.: renderizadores QtWebEngine, workers de áudio/sync).
    """
    processos = [processo_pai]
    try:
        filhos = processo_pai.children(recursive=True)
        processos.extend(filhos)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

    total_cpu = 0.0
    total_rss_bytes = 0
    total_vms_bytes = 0
    total_threads = 0
    read_bytes = 0
    write_bytes = 0

    processos_vivos = 0
    for p in processos:
        try:
            if not p.is_running():
                continue
            # cpu_percent com intervalo 0.0 pega a última medição acumulada
            cpu = p.cpu_percent(interval=None)
            total_cpu += cpu

            mem = p.memory_info()
            total_rss_bytes += mem.rss
            total_vms_bytes += getattr(mem, "vms", 0)

            total_threads += p.num_threads()

            # I/O counters (pode requerer privilégios ou não estar disponível em certas plataformas)
            try:
                io = p.io_counters()
                read_bytes += io.read_bytes
                write_bytes += io.write_bytes
            except (psutil.AccessDenied, AttributeError):
                pass

            processos_vivos += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return {
        "processos_vivos": processos_vivos,
        "cpu_percent": round(total_cpu, 2),
        "rss_mb": round(total_rss_bytes / (1024 * 1024), 2),
        "vms_mb": round(total_vms_bytes / (1024 * 1024), 2),
        "num_threads": total_threads,
        "io_read_bytes": read_bytes,
        "io_write_bytes": write_bytes,
    }


def classificar_gqm(metrica: str, valor: float) -> str:
    """Retorna o nível de enquadramento GQM (Excelente, Alvo, Mínimo, Insatisfatório)."""
    faixas = GQM_THRESHOLDS.get(metrica, {})
    for nivel, (lim_inf, lim_sup) in faixas.items():
        if lim_inf <= valor < lim_sup:
            return nivel.capitalize()
    return "N/D"


def executar_monitoramento(cenario: str, duracao: int, intervalo: float, saida_csv: Path, pid: int = None):
    """Executa o loop de amostragem periódica para os cenários de Repouso ou Estresse."""
    so = identificar_so()
    print("=" * 70)
    print(f"🔬 BETTY SNYDER - COLETOR DE DESEMPENHO (PSM / GQM Fase 3)")
    print(f"📌 Cenário: {cenario.upper()} | SO: {so.upper()} | Duração: {duracao}s | Taxa: {intervalo}s")
    print("=" * 70)

    anki_proc = encontrar_processo_anki(pid)
    if not anki_proc:
        print("[ERRO] O processo do Anki não foi encontrado em execução!")
        print("Por favor, abra o Anki antes de iniciar a medição deste cenário.")
        sys.exit(1)

    print(f"✅ Anki detectado (PID Principal: {anki_proc.pid}, Nome: '{anki_proc.name()}')")
    print(f"📁 Destino do CSV: {saida_csv}")
    print("Iniciando coleta em 2 segundos... Pressione Ctrl+C para encerrar antecipadamente.\n")
    time.sleep(2)

    # Primeira chamada para inicializar contadores internos do psutil
    _ = coletar_metricas_arvore(anki_proc)

    registros = []
    t_inicio = time.time()
    segundo = 0

    io_read_anterior = 0
    io_write_anterior = 0

    cabecalho = [
        "segundo",
        "timestamp_iso",
        "cpu_total_pct",
        "ram_rss_mb",
        "ram_vms_mb",
        "threads_totais",
        "processos_filhos",
        "io_read_kb_s",
        "io_write_kb_s",
    ]

    try:
        with open(saida_csv, mode="w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerow(cabecalho)

            while True:
                t_atual = time.time()
                t_decorrido = t_atual - t_inicio
                if duracao > 0 and t_decorrido >= duracao:
                    break

                # Verifica se o processo principal ainda está vivo
                if not anki_proc.is_running():
                    print("\n[ALERTA] Processo do Anki foi encerrado durante a coleta.")
                    break

                metricas = coletar_metricas_arvore(anki_proc)

                # Cálculo de taxa de I/O em KB/s
                delta_read_kb = 0.0
                delta_write_kb = 0.0
                if segundo > 0:
                    delta_read_kb = max(0.0, (metricas["io_read_bytes"] - io_read_anterior) / 1024.0 / intervalo)
                    delta_write_kb = max(0.0, (metricas["io_write_bytes"] - io_write_anterior) / 1024.0 / intervalo)

                io_read_anterior = metricas["io_read_bytes"]
                io_write_anterior = metricas["io_write_bytes"]

                linha = [
                    segundo,
                    datetime.now().isoformat(),
                    metricas["cpu_percent"],
                    metricas["rss_mb"],
                    metricas["vms_mb"],
                    metricas["num_threads"],
                    metricas["processos_vivos"],
                    round(delta_read_kb, 2),
                    round(delta_write_kb, 2),
                ]
                writer.writerow(linha)
                f_out.flush()
                registros.append(metricas)

                # Exibição compacta no terminal
                print(
                    f"[{segundo:03d}s] CPU: {metricas['cpu_percent']:5.1f}% | "
                    f"RAM RSS: {metricas['rss_mb']:6.1f} MB | "
                    f"Threads: {metricas['num_threads']:2d} | "
                    f"Procs: {metricas['processos_vivos']:2d} | "
                    f"I/O Escrita: {delta_write_kb:5.1f} KB/s"
                )

                segundo += 1
                time.sleep(intervalo)

    except KeyboardInterrupt:
        print("\n[INTERRUPÇÃO] Coleta finalizada pelo operador via teclado.")

    # Consolidação dos Resultados & Julgamento GQM
    if registros:
        cpus = [r["cpu_percent"] for r in registros]
        rsss = [r["rss_mb"] for r in registros]

        cpu_media = sum(cpus) / len(cpus)
        cpu_pico = max(cpus)
        ram_media = sum(rsss) / len(rsss)
        ram_pico = max(rsss)

        print("\n" + "=" * 70)
        print("📊 RELATÓRIO CONSOLIDADO DA RODADA DE MEDIÇÃO")
        print("=" * 70)
        print(f"Total de amostras: {len(registros)} segundos")
        print(f"CPU Média: {cpu_media:.2f}% | CPU Pico: {cpu_pico:.2f}%")
        print(f"RAM RSS Média: {ram_media:.2f} MB | RAM RSS Pico: {ram_pico:.2f} MB")

        if cenario == "repouso":
            nivel_ram = classificar_gqm("repouso_ram_mb", ram_media)
            nivel_cpu = classificar_gqm("repouso_cpu_pct", cpu_media)
            print("-" * 70)
            print("🎯 ENQUADRAMENTO NAS FAIXAS GQM (FASE 2 / ISO 25010):")
            print(f"  • RAM Repouso ({ram_media:.1f} MB): [{nivel_ram.upper()}] (Alvo: 250-400 MB)")
            print(f"  • CPU Repouso ({cpu_media:.2f}%):    [{nivel_cpu.upper()}] (Alvo: 2-5%)")
        elif cenario == "estresse":
            nivel_ram_pico = classificar_gqm("estresse_pico_ram_mb", ram_pico)
            print("-" * 70)
            print("🎯 ENQUADRAMENTO NAS FAIXAS GQM (FASE 2 / ISO 25010):")
            print(f"  • Pico de RAM sob Carga ({ram_pico:.1f} MB): [{nivel_ram_pico.upper()}] (Alvo: 600-1000 MB)")
        print(f"💾 Arquivo de métricas salvo com sucesso em:\n   {saida_csv}")
        print("=" * 70)


def executar_cold_start(comando_anki: str, saida_csv: Path):
    """
    Executa a rotina do Cenário 1: Cold Start.
    Dispara o Anki a partir do estado frio e cronometra T_0 até o processo estabilizar.
    """
    so = identificar_so()
    print("=" * 70)
    print(f"🧊 CENÁRIO 1: INICIALIZAÇÃO A FRIO (COLD START) - SO: {so.upper()}")
    print("=" * 70)
    print("⚠️ ATENÇÃO: Conforme a Seção 3 (Cenário 1) do protocolo:")
    print("   1. Certifique-se de que o Anki está FECHADO.")
    print("   2. No Linux/Ubuntu: execute 'sync && echo 3 | sudo tee /proc/sys/vm/drop_caches'")
    print("   3. No macOS: execute 'sudo purge'")
    print("   4. No Windows: reinicie ou esvazie a Standby List via RAMMap.")
    print("-" * 70)

    if not comando_anki:
        if so == "ubuntu":
            comando_anki = "anki"
        elif so == "windows":
            comando_anki = "anki.exe"
        elif so == "macos":
            comando_anki = "open -a Anki"

    resp = input(f"Deseja disparar o Anki agora via comando '{comando_anki}'? [S/n]: ").strip().lower()
    if resp in ["n", "nao", "não"]:
        print("[CANCELADO] Operação abortada pelo operador.")
        return

    print(f"\nDisparando '{comando_anki}' e cronometrando...")
    t0 = time.perf_counter()
    proc = subprocess.Popen(comando_anki, shell=True)

    # Monitora até o processo Anki ser detectado pelo psutil
    t_processo = None
    proc_obj = None
    timeout = 30.0

    while time.perf_counter() - t0 < timeout:
        proc_obj = encontrar_processo_anki()
        if proc_obj:
            t_processo = time.perf_counter() - t0
            break
        time.sleep(0.05)

    if not proc_obj:
        print("[ERRO] Timeout de 30s aguardando o surgimento do processo Anki.")
        return

    print(f"⚡ Processo detectado após {t_processo:.3f} segundos (PID {proc_obj.pid}).")
    print("Aguardando estabilização inicial do carregamento da interface (3s)...")
    time.sleep(3.0)

    t_total = t_processo  # Aproximação baseada em detecção de processo
    nivel_start = classificar_gqm("cold_start_seg", t_total)

    print("\n" + "=" * 70)
    print(f"⏱️ Tempo de Cold Start registrado: {t_total:.3f} s")
    print(f"🎯 Julgamento GQM: [{nivel_start.upper()}] (Excelente: <= 3s | Alvo: 3s a 6s)")
    print("=" * 70)

    # Gravação no CSV
    cabecalho = ["data_hora", "so", "comando", "t_cold_start_seg", "nivel_gqm"]
    linha = [datetime.now().isoformat(), so, comando_anki, round(t_total, 3), nivel_start]

    with open(saida_csv, mode="w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        w.writerow(linha)

    print(f"💾 Resultado registrado em: {saida_csv}")


def main():
    parser = argparse.ArgumentParser(
        description="Coletor de Desempenho e Métricas do Anki - Betty Snyder (Fase 3)"
    )
    parser.add_argument(
        "--cenario",
        required=True,
        choices=["repouso", "estresse", "cold_start"],
        help="Cenário de teste conforme o protocolo oficial (repouso, estresse ou cold_start).",
    )
    parser.add_argument(
        "--duracao",
        type=int,
        default=None,
        help="Duração da coleta em segundos (Padrão: 300 para repouso, 180 para estresse).",
    )
    parser.add_argument(
        "--intervalo",
        type=float,
        default=1.0,
        help="Intervalo de amostragem em segundos (Padrão: 1.0s).",
    )
    parser.add_argument(
        "--saida",
        type=str,
        default=None,
        help="Caminho personalizado do arquivo CSV de saída.",
    )
    parser.add_argument(
        "--pid",
        type=int,
        default=None,
        help="PID específico do processo Anki a ser monitorado.",
    )
    parser.add_argument(
        "--comando-anki",
        type=str,
        default=None,
        help="Comando de disparo do Anki para o cenário cold_start (Padrão: 'anki').",
    )

    args = parser.parse_args()
    so = identificar_so()

    # Definir duração padrão se omitida
    if args.duracao is None:
        if args.cenario == "repouso":
            duracao = 300
        elif args.cenario == "estresse":
            duracao = 180
        else:
            duracao = 0
    else:
        duracao = args.duracao

    saida_csv = Path(args.saida) if args.saida else obter_caminho_saida_padrao(args.cenario, so)

    if args.cenario in ["repouso", "estresse"]:
        executar_monitoramento(
            cenario=args.cenario,
            duracao=duracao,
            intervalo=args.intervalo,
            saida_csv=saida_csv,
            pid=args.pid,
        )
    elif args.cenario == "cold_start":
        executar_cold_start(
            comando_anki=args.comando_anki,
            saida_csv=saida_csv,
        )


if __name__ == "__main__":
    main()
