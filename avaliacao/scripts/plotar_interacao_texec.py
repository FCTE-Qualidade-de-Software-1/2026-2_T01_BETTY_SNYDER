#!/usr/bin/env python3
"""Gera gráficos legíveis de Capacidade de interação (T_exec e T_rf)."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parents[2]
CSV_TAREFAS = ROOT / "avaliacao" / "dados" / "interacao" / "bruto" / "M-INT_tarefas.csv"
CSV_METRICAS = ROOT / "avaliacao" / "dados" / "interacao" / "consolidado" / "M-INT_metricas.csv"

OUT_TEXEC = [
    ROOT / "docs" / "assets" / "grafico_texec_tarefas_interacao.png",
    ROOT / "docs" / "avaliacao" / "dados" / "grafico_texec_tarefas_interacao.png",
]
OUT_TRF = [
    ROOT / "docs" / "assets" / "grafico_trf_interacao.png",
    ROOT / "docs" / "avaliacao" / "dados" / "grafico_trf_interacao.png",
]

# Alinhamento semântico A (aprendizagem) × B (uso diário)
MAPA_A = {
    "Criar conta": "A1",
    "Criar baralho": "A2",
    "Adicionar cartões": "A3",
    "Estudar / revisar": "A4",
    "Sincronizar": "A5",
}
MAPA_B = {
    "Criar conta": "B1",
    "Criar baralho": "B3",
    "Adicionar cartões": "B4",
    "Estudar / revisar": "B2",
    "Sincronizar": "B5",
}

COR_A = "#0B3D91"
COR_B = "#C2410C"
COR_ALVO = "#FBBF24"
COR_TEXTO = "#111827"
COR_GRADE = "#9CA3AF"


def carregar_tarefas(caminho: Path) -> dict[tuple[str, str], float]:
    dados: dict[tuple[str, str], float] = {}
    with caminho.open(encoding="utf-8-sig", newline="") as arq:
        for linha in csv.DictReader(arq):
            dur = (linha.get("duracao_s") or "").strip()
            if not dur:
                continue
            chave = (linha["participante"], linha["tarefa"])
            dados[chave] = float(dur)
    return dados


def media(valores: list[float]) -> float | None:
    return sum(valores) / len(valores) if valores else None


def plot_texec(tarefas: dict[tuple[str, str], float]) -> None:
    rotulos = list(MAPA_A.keys())
    vals_a: list[float] = []
    vals_b: list[float] = []
    secs_a: list[float] = []
    secs_b: list[float | None] = []

    for rotulo in rotulos:
        sa = tarefas[("PA01", MAPA_A[rotulo])]
        secs_a.append(sa)
        vals_a.append(sa / 60.0)

        tb = MAPA_B[rotulo]
        amostra = [
            tarefas[p]
            for p in (("PB01", tb), ("PB02", tb), ("PB03", tb))
            if (p[0], tb) in tarefas
        ]
        mb = media(amostra)
        secs_b.append(mb)
        vals_b.append((mb / 60.0) if mb is not None else 0.0)

    fig, ax = plt.subplots(figsize=(12.5, 7.2), dpi=160)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FAFBFC")

    x = list(range(len(rotulos)))
    largura = 0.36
    barras_a = ax.bar(
        [i - largura / 2 for i in x],
        vals_a,
        width=largura,
        color=COR_A,
        edgecolor="#062554",
        linewidth=1.2,
        label="Grupo A (PA01, rodada 1)",
        zorder=3,
    )
    barras_b = ax.bar(
        [i + largura / 2 for i in x],
        vals_b,
        width=largura,
        color=COR_B,
        edgecolor="#7C2D12",
        linewidth=1.2,
        label="Grupo B (média PB01–PB03)",
        zorder=3,
    )

    ax.axhspan(2, 5, color=COR_ALVO, alpha=0.28, zorder=1)
    ax.axhline(2, color="#B45309", linestyle="--", linewidth=2.0, zorder=2)
    ax.axhline(5, color="#B45309", linestyle="--", linewidth=2.0, zorder=2)

    for barra, segundos in zip(barras_a, secs_a):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 0.12,
            f"{segundos:.0f} s",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
            color=COR_A,
        )
    for barra, segundos in zip(barras_b, secs_b):
        if segundos is None:
            continue
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 0.12,
            f"{segundos:.0f} s",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
            color=COR_B,
        )

    ax.set_xticks(x)
    ax.set_xticklabels(rotulos, fontsize=13, fontweight="bold", color=COR_TEXTO)
    ax.set_ylabel("Tempo de execução (minutos)", fontsize=14, fontweight="bold", color=COR_TEXTO)
    ax.set_xlabel("Tarefa", fontsize=14, fontweight="bold", color=COR_TEXTO)
    ax.set_title(
        "Capacidade de interação: tempo por tarefa (T_exec)",
        fontsize=18,
        fontweight="bold",
        color=COR_TEXTO,
        pad=14,
    )
    ax.set_ylim(0, 5.8)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.tick_params(axis="y", labelsize=12, colors=COR_TEXTO)
    ax.yaxis.grid(True, linestyle=":", linewidth=1.0, color=COR_GRADE, zorder=0)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color("#374151")
        ax.spines[spine].set_linewidth(1.2)

    legendas = [
        Patch(facecolor=COR_ALVO, edgecolor="#B45309", alpha=0.45, label="Faixa alvo (2 a 5 min)"),
        barras_a,
        barras_b,
    ]
    ax.legend(
        handles=legendas,
        loc="upper right",
        fontsize=12,
        frameon=True,
        fancybox=False,
        edgecolor="#6B7280",
        framealpha=0.98,
    )

    fig.text(
        0.01,
        0.01,
        "Fonte: M-INT_tarefas.csv. Grupo B: média das tarefas com tempo (PB03 sem B2). "
        "Abaixo de 2 min = faixa excelente.",
        fontsize=11,
        color="#1F2937",
        ha="left",
        va="bottom",
    )

    fig.tight_layout(rect=(0, 0.04, 1, 1))
    for saida in OUT_TEXEC:
        saida.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(saida, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"Salvo: {saida}")
    plt.close(fig)


def plot_trf(caminho: Path) -> None:
    valores: dict[str, float] = {}
    with caminho.open(encoding="utf-8-sig", newline="") as arq:
        for linha in csv.DictReader(arq):
            if linha["metrica"] == "Trf" and linha["participante"] in {"PA01", "PB01", "PB02", "PB03"}:
                valores[linha["participante"]] = float(linha["valor"])

    ordem = ["PA01", "PB01", "PB02", "PB03"]
    alturas = [valores[p] for p in ordem]
    cores = [COR_A if p == "PA01" else COR_B for p in ordem]

    fig, ax = plt.subplots(figsize=(10.5, 6.4), dpi=160)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FAFBFC")

    barras = ax.bar(
        ordem,
        alturas,
        color=cores,
        edgecolor="#111827",
        linewidth=1.2,
        width=0.62,
        zorder=3,
    )

    ax.axhline(75, color="#047857", linestyle="--", linewidth=2.2, zorder=2, label="Alvo (≥ 75%)")
    ax.axhline(50, color="#B45309", linestyle=":", linewidth=1.8, zorder=2, label="Mínimo (≥ 50%)")

    for barra, valor in zip(barras, alturas):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 1.8,
            f"{valor:.1f}%".replace(".", ","),
            ha="center",
            va="bottom",
            fontsize=14,
            fontweight="bold",
            color=COR_TEXTO,
        )

    ax.set_ylabel("T_rf (%)", fontsize=14, fontweight="bold", color=COR_TEXTO)
    ax.set_xlabel("Participante", fontsize=14, fontweight="bold", color=COR_TEXTO)
    ax.set_title(
        "Capacidade de interação: taxa de reconhecimento (T_rf)",
        fontsize=18,
        fontweight="bold",
        color=COR_TEXTO,
        pad=14,
    )
    ax.set_ylim(0, 110)
    ax.tick_params(axis="both", labelsize=13, colors=COR_TEXTO)
    ax.yaxis.grid(True, linestyle=":", linewidth=1.0, color=COR_GRADE, zorder=0)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color("#374151")
        ax.spines[spine].set_linewidth(1.2)

    ax.legend(loc="upper right", fontsize=12, frameon=True, edgecolor="#6B7280", framealpha=0.98)
    fig.text(
        0.01,
        0.01,
        "Fonte: M-INT_metricas.csv. PA01 = Grupo A (iniciante); PB01–PB03 = Grupo B (frequentes).",
        fontsize=11,
        color="#1F2937",
        ha="left",
        va="bottom",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    for saida in OUT_TRF:
        saida.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(saida, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"Salvo: {saida}")
    plt.close(fig)


def main() -> None:
    tarefas = carregar_tarefas(CSV_TAREFAS)
    plot_texec(tarefas)
    plot_trf(CSV_METRICAS)


if __name__ == "__main__":
    main()
