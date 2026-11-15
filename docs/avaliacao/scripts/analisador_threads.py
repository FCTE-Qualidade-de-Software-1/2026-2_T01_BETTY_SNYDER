#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
FCTE / UnB - Qualidade de Software 1 (2026-2)
Grupo 01: Betty Snyder | Dupla B: Eficiência de Desempenho
Script: analisador_threads.py (Questão Q4 - Issue #56 / E2-21)
Versão MULTIPLATAFORMA: Windows 10/11, Ubuntu/Linux e macOS
===============================================================================
Finalidade:
  Auditar o isolamento entre a Main Thread (UI PyQt) e as Worker Threads
  (SQLite / backend Rust) do Anki, conforme a Questão Q4:
    - docs/avaliacao/protocolos/desempenho.md (Seção 3, Cenário 2B e Seção 4)

Critérios GQM (Q4 - CPU da Main Thread sob carga de 100k):
  - Excelente:      CPU_Main <= 15.0%
  - Alvo:           15.0% < CPU_Main <= 30.0%
  - Mínimo:         30.0% < CPU_Main <= 50.0%
  - Insatisfatório: CPU_Main > 50.0%

Como funciona em cada SO (modo realtime):
  - Linux:   psutil.Process.threads() (lê /proc). Main Thread = TID == PID.
  - Windows: psutil.Process.threads() (API do Windows). Main Thread = primeira
             thread da lista (a mais antiga).
  - macOS:   psutil.Process.threads(); se o macOS negar acesso (AccessDenied),
             cai para `ps -M` (valor aproximado, média decaída do SO).

Modos:
  python analisador_threads.py --modo realtime --duracao 180 --cenario estresse
  python analisador_threads.py --modo parse --arquivo threads_estresse.txt
      (parse lê um dump do `pidstat -t`, gerado só no Linux; o parse em si
       roda em qualquer SO)

Requisitos:
  pip install psutil        (matplotlib só se for usar --grafico: pip install matplotlib)
===============================================================================
"""

import sys
import os
import re
import csv
import time
import argparse
import platform
import subprocess
from datetime import datetime
from pathlib import Path

# Evita UnicodeEncodeError com emojis no console do Windows (cp1252)
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

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

SISTEMA = platform.system()  # "Linux", "Windows" ou "Darwin"


def identificar_so() -> str:
    return {"Linux": "ubuntu", "Windows": "windows", "Darwin": "macos"}.get(SISTEMA, "desconhecido")


def classificar_gqm_q4(cpu_main_pct: float) -> str:
    """Enquadra o uso da Main Thread nas faixas oficiais do GQM."""
    for nivel, (lim_inf, lim_sup) in GQM_Q4_THRESHOLDS.items():
        if lim_inf <= cpu_main_pct <= lim_sup:
            return nivel.capitalize()
    return "N/D"


def obter_caminho_saida_padrao(cenario: str) -> Path:
    """Caminho padrão em docs/avaliacao/dados/, com o SO real no nome."""
    base_dir = Path(__file__).resolve().parent.parent / "dados"
    base_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return base_dir / f"threads_{cenario}_{identificar_so()}_{timestamp}.csv"


# =============================================================================
# Localização do processo do Anki (portável)
# =============================================================================
def encontrar_pid_anki(pid_informado: int = None):
    """
    Localiza o processo principal do Anki.
    Entre os candidatos, descarta os que têm pai também candidato (ex.:
    QtWebEngineProcess) e escolhe o que tiver mais threads.
    """
    if pid_informado:
        return pid_informado

    if psutil is None:
        return None

    meu_pid = os.getpid()
    candidatos = {}
    for p in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if p.pid == meu_pid:
                continue
            cmdline = " ".join(p.info["cmdline"] or []).lower()
            nome = (p.info["name"] or "").lower()
            if "analisador_threads" in cmdline or "coletor.py" in cmdline:
                continue
            if "anki" in nome or "anki" in cmdline:
                candidatos[p.pid] = p
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not candidatos:
        return None

    raizes = []
    for pid, p in candidatos.items():
        try:
            if p.ppid() not in candidatos:
                raizes.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    pool = raizes or list(candidatos.values())

    def n_threads(p):
        try:
            return p.num_threads()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0

    return max(pool, key=n_threads).pid


# =============================================================================
# Coletor de CPU por thread (uma implementação por estratégia)
# =============================================================================
class ColetorThreads:
    """
    amostrar() devolve: (cpu_main_pct, cpu_workers_pct, qtd_threads, nome_main)
    cpu em % de UM núcleo (a Main Thread nunca passa de ~100%).
    """

    def __init__(self, proc):
        self.proc = proc
        self.pid = proc.pid
        self.usar_ps = False          # fallback macOS
        self.anterior = {}            # tid -> segundos de CPU acumulados
        self.t_anterior = None
        self.main_tid = None
        try:
            self._ler_tempos()
        except psutil.AccessDenied:
            if SISTEMA == "Darwin":
                self.usar_ps = True
                print("[AVISO] macOS negou acesso às threads via psutil. "
                      "Usando `ps -M` (valores aproximados). "
                      "Para precisão, rode com: sudo python3 analisador_threads.py ...")
            else:
                raise

    # ---- estratégia 1: tempos de CPU via psutil (Linux/Windows/macOS) -------
    def _ler_tempos(self):
        threads = self.proc.threads()
        if not threads:
            return {}
        if SISTEMA == "Linux":
            self.main_tid = self.pid                 # na Linux, TID principal == PID
        elif self.main_tid is None or self.main_tid not in {t.id for t in threads}:
            self.main_tid = threads[0].id            # Windows/macOS: primeira = principal
        return {t.id: t.user_time + t.system_time for t in threads}

    # ---- estratégia 2: `ps -M` no macOS (aproximado) --------------------------
    def _ler_ps_macos(self):
        saida = subprocess.check_output(
            ["ps", "-M", "-p", str(self.pid)], stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
        pcts = []
        for linha in saida.splitlines()[1:]:
            tokens = linha.split()
            for i, tok in enumerate(tokens[:-1]):
                if re.fullmatch(r"\d+[.,]\d+", tok) and re.fullmatch(r"[A-Z][A-Za-z+<>]*", tokens[i + 1]):
                    pcts.append(float(tok.replace(",", ".")))
                    break
        return pcts

    def _nome_main(self) -> str:
        if SISTEMA == "Linux":
            try:
                with open(f"/proc/{self.pid}/task/{self.pid}/comm", encoding="utf-8") as f:
                    return f.read().strip()
            except (IOError, PermissionError):
                pass
        try:
            return self.proc.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return "main"

    def amostrar(self):
        if self.usar_ps:
            pcts = self._ler_ps_macos()
            if not pcts:
                return 0.0, 0.0, 0, self._nome_main()
            # ps -M lista a thread principal primeiro
            return pcts[0], sum(pcts[1:]), len(pcts), self._nome_main()

        agora = time.monotonic()
        atuais = self._ler_tempos()
        cpu_main = cpu_workers = 0.0
        if self.t_anterior is not None:
            dt = max(agora - self.t_anterior, 1e-6)
            for tid, total in atuais.items():
                if tid in self.anterior:
                    pct = max(0.0, total - self.anterior[tid]) / dt * 100.0
                    if tid == self.main_tid:
                        cpu_main += pct
                    else:
                        cpu_workers += pct
        self.anterior = atuais
        self.t_anterior = agora
        return cpu_main, cpu_workers, len(atuais), self._nome_main()


# =============================================================================
# Modo 1: Monitoramento em tempo real
# =============================================================================
def executar_modo_realtime(pid: int, duracao: int, intervalo: float, saida_csv: Path, cenario: str):
    print("=" * 72)
    print("🔬 ANÁLISE DE THREADS EM TEMPO REAL (QUESTÃO Q4 - ISO/IEC 25010)")
    print(f"📌 PID Alvo: {pid} | SO: {identificar_so().upper()} | "
          f"Duração: {duracao}s | Amostragem: {intervalo}s")
    print("=" * 72)

    if psutil is None:
        print("[ERRO CRÍTICO] psutil não está instalado. Execute: pip install psutil")
        sys.exit(1)

    try:
        proc = psutil.Process(pid)
        print(f"✅ Anki detectado: PID {pid} ({proc.name()})")
        coletor = ColetorThreads(proc)
    except psutil.NoSuchProcess:
        print(f"[ERRO] Processo com PID {pid} não encontrado.")
        sys.exit(1)
    except psutil.AccessDenied:
        print("[ERRO] Acesso negado às threads do processo. "
              "No Windows, abra o terminal como Administrador; no Linux/macOS, use sudo.")
        sys.exit(1)

    print(f"📁 Destino CSV: {saida_csv}")
    print("Iniciando amostragem... Pressione Ctrl+C para finalizar.\n")

    time.sleep(intervalo)  # primeira leitura serve só de referência

    cabecalho = [
        "segundo", "timestamp_iso", "cpu_main_thread_pct", "cpu_workers_total_pct",
        "cpu_processo_total_pct", "qtd_threads_ativas", "nome_main_thread",
        "classificacao_gqm_q4",
    ]
    amostras = []
    t_inicio = time.monotonic()
    segundo = 0

    try:
        with open(saida_csv, mode="w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerow(cabecalho)

            while duracao <= 0 or (time.monotonic() - t_inicio) < duracao:
                if not proc.is_running():
                    print("\n[ALERTA] Processo do Anki finalizou durante a coleta.")
                    break

                try:
                    cpu_main, cpu_workers, qtd, nome_main = coletor.amostrar()
                except psutil.NoSuchProcess:
                    print("\n[ALERTA] Processo do Anki finalizou durante a coleta.")
                    break

                cpu_total = cpu_main + cpu_workers
                nivel = classificar_gqm_q4(cpu_main)

                writer.writerow([
                    segundo, datetime.now().isoformat(), round(cpu_main, 2),
                    round(cpu_workers, 2), round(cpu_total, 2), qtd, nome_main, nivel,
                ])
                f_out.flush()
                amostras.append({"cpu_main": cpu_main, "cpu_workers": cpu_workers, "cpu_total": cpu_total})

                print(
                    f"[{segundo:03d}s] Main Thread (UI): {cpu_main:5.1f}% | "
                    f"Workers: {cpu_workers:5.1f}% | Total: {cpu_total:5.1f}% | "
                    f"Threads: {qtd:2d} | GQM: [{nivel.upper()}]"
                )

                segundo += 1
                # compensa o tempo gasto na amostragem para manter ~1 amostra/intervalo
                alvo = t_inicio + segundo * intervalo
                time.sleep(max(0.0, alvo - time.monotonic()))

    except KeyboardInterrupt:
        print("\n[INFO] Coleta interrompida pelo operador.")

    imprimir_resumo_q4(amostras, saida_csv)


# =============================================================================
# Modo 2: Parser de dump gerado pelo `pidstat -t` (dump só existe no Linux)
# =============================================================================
def executar_modo_parse(caminho_arquivo: Path, saida_csv: Path):
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
            chave = "main" if is_main else "workers"
            amostras_por_segundo[hora][chave] += cpu_val
            amostras_por_segundo[hora]["tids"][tid] = cpu_val

    if not amostras_por_segundo:
        print("[ERRO] Nenhuma linha válida de métrica encontrada no log do pidstat.")
        sys.exit(1)

    amostras = []
    with open(saida_csv, mode="w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow([
            "timestamp", "cpu_main_thread_pct", "cpu_workers_total_pct",
            "cpu_processo_total_pct", "qtd_threads", "classificacao_gqm_q4",
        ])
        for hora, dados in amostras_por_segundo.items():
            cpu_main, cpu_workers = dados["main"], dados["workers"]
            cpu_total = cpu_main + cpu_workers
            writer.writerow([
                hora, round(cpu_main, 2), round(cpu_workers, 2), round(cpu_total, 2),
                len(dados["tids"]), classificar_gqm_q4(cpu_main),
            ])
            amostras.append({"cpu_main": cpu_main, "cpu_workers": cpu_workers, "cpu_total": cpu_total})

    imprimir_resumo_q4(amostras, saida_csv)


def imprimir_resumo_q4(amostras: list, saida_csv: Path):
    if not amostras:
        return

    mains = [a["cpu_main"] for a in amostras]
    workers = [a["cpu_workers"] for a in amostras]
    totais = [a["cpu_total"] for a in amostras]

    media_main = sum(mains) / len(mains)
    pico_main = max(mains)
    media_workers = sum(workers) / len(workers)
    media_total = sum(totais) / len(totais)
    razao = (media_main / media_total * 100.0) if media_total > 0 else 0.0
    nivel_final = classificar_gqm_q4(media_main)

    print("\n" + "=" * 72)
    print("📊 RESULTADO CONSOLIDADO DA AUDITORIA DE THREADS (QUESTÃO Q4)")
    print("=" * 72)
    print(f"Total de Janelas Avaliadas: {len(amostras)} segundos")
    print(f"CPU Média da Main Thread (UI):       {media_main:5.2f}% (Pico: {pico_main:5.2f}%)")
    print(f"CPU Média das Worker Threads (Back): {media_workers:5.2f}%")
    print(f"Consumo Médio Agregado do Anki:      {media_total:5.2f}%")
    print(f"Participação da UI na Carga Total:   {razao:5.1f}%")
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
# Gráfico para o PC2 (tarefa da Karolina Vieira Barbosa - Dupla B)
# =============================================================================
def gerar_grafico_threads(caminho_csv: Path, saida_png: Path = None, cenario: str = "estresse"):
    """
    Lê o CSV gerado e plota (300 DPI):
      - Eixo X: segundo (ou índice da amostra, se o CSV vier do modo parse)
      - Eixo Y: cpu_main_thread_pct e cpu_workers_total_pct
      - Linha vermelha tracejada em 15% (teto da faixa 'Excelente' da Q4)
      - Título, legenda e anotação do enquadramento GQM conquistado
    Salva por padrão em docs/avaliacao/dados/grafico_threads_<cenario>.png
    """
    try:
        import matplotlib
        matplotlib.use("Agg")  # sem janela: funciona em qualquer SO, inclusive sem display
        import matplotlib.pyplot as plt
    except ImportError:
        print("[AVISO] matplotlib não instalado. Instale com: pip install matplotlib")
        return

    xs, cpu_main, cpu_workers = [], [], []
    with open(caminho_csv, "r", encoding="utf-8", newline="") as f:
        for i, row in enumerate(csv.DictReader(f)):
            xs.append(int(row["segundo"]) if row.get("segundo") not in (None, "") else i)
            cpu_main.append(float(row["cpu_main_thread_pct"]))
            cpu_workers.append(float(row["cpu_workers_total_pct"]))

    if not xs:
        print("[AVISO] CSV sem amostras; gráfico não gerado.")
        return

    media_main = sum(cpu_main) / len(cpu_main)
    pico_main = max(cpu_main)
    nivel = classificar_gqm_q4(media_main)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(xs, cpu_main, label="Main Thread (PyQt UI)", color="#2563eb", linewidth=2)
    ax.plot(xs, cpu_workers, label="Worker Threads (Rust/SQLite)", color="#10b981",
            linewidth=1.5, linestyle="--")
    ax.axhline(y=15.0, color="#ef4444", linestyle="--", linewidth=1.5,
               label="Teto GQM Excelente (15%)")

    ax.set_title(f"Isolamento de Threads no Anki - cenário {cenario} "
                 f"(Questão Q4 - ISO/IEC 25010)")
    ax.set_xlabel("Tempo de execução (s)")
    ax.set_ylabel("Uso de CPU (% de um núcleo)")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")

    ax.annotate(
        f"Enquadramento: {nivel.upper()}\nMédia Main: {media_main:.1f}% | Pico: {pico_main:.1f}%",
        xy=(0.02, 0.95), xycoords="axes fraction", va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#2563eb", alpha=0.9),
    )

    if saida_png is None:
        base = Path(__file__).resolve().parent.parent / "dados"
        base.mkdir(parents=True, exist_ok=True)
        saida_png = base / f"grafico_threads_{cenario}.png"
    saida_png = Path(saida_png)
    saida_png.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(saida_png, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"📊 Gráfico gerado com sucesso em: {saida_png}")


def main():
    parser = argparse.ArgumentParser(
        description="Auditor de Isolamento de Threads do Anki (Q4) - multiplataforma"
    )
    parser.add_argument("--modo", choices=["realtime", "parse"], default="realtime",
                        help="'realtime' monitora o Anki ativo; 'parse' lê um dump do pidstat.")
    parser.add_argument("--cenario", choices=["repouso", "estresse"], default="estresse",
                        help="Cenário de medição (repouso ou estresse).")
    parser.add_argument("--duracao", type=int, default=180,
                        help="Duração em segundos no modo realtime (padrão: 180).")
    parser.add_argument("--intervalo", type=float, default=1.0,
                        help="Intervalo de amostragem em segundos (padrão: 1.0).")
    parser.add_argument("--pid", type=int, default=None, help="PID do Anki (opcional).")
    parser.add_argument("--arquivo", type=str, default=None,
                        help="Arquivo txt do pidstat para o modo 'parse'.")
    parser.add_argument("--saida", type=str, default=None, help="Caminho do CSV de saída.")
    parser.add_argument("--grafico", action="store_true", default=False,
                        help="Gera o PNG (300 DPI) com as curvas das threads para o PC2.")
    args = parser.parse_args()

    saida_csv = Path(args.saida) if args.saida else obter_caminho_saida_padrao(args.cenario)

    if args.modo == "parse":
        if not args.arquivo:
            print("[ERRO] No modo 'parse', informe --arquivo <caminho.txt>")
            sys.exit(1)
        executar_modo_parse(Path(args.arquivo), saida_csv)
    else:
        if psutil is None:
            print("[ERRO CRÍTICO] psutil não está instalado. Execute: pip install psutil")
            sys.exit(1)
        pid = encontrar_pid_anki(args.pid)
        if not pid:
            print("[ERRO] Processo do Anki não localizado em execução.")
            print("Abra o Anki antes de rodar o modo realtime ou informe --pid <NUM>.")
            sys.exit(1)
        executar_modo_realtime(pid, args.duracao, args.intervalo, saida_csv, args.cenario)

    if args.grafico:
        gerar_grafico_threads(saida_csv, cenario=args.cenario)


if __name__ == "__main__":
    main()