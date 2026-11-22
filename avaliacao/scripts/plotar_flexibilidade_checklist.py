#!/usr/bin/env python3
"""Gera um gráfico com a pontuação do checklist de flexibilidade por sistema.

Entrada padrão: avaliacao/dados/flexibilidade/consolidado/flexibilidade-checklist-registro.csv
Saída padrão: avaliacao/dados/flexibilidade/consolidado/grafico-flexibilidade-checklist.png
Métrica GQM: P_int (soma dos 10 critérios de adaptabilidade).
"""

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CSV_PADRAO = (
    ROOT
    / "avaliacao"
    / "dados"
    / "flexibilidade"
    / "consolidado"
    / "flexibilidade-checklist-registro.csv"
)

COLUNAS_SO = {
    "windows": "Windows",
    "macos": "macOS",
    "ubuntu": "Ubuntu",
}


def ler_pontuacoes(caminho: Path) -> tuple[list[str], dict[str, int]]:
    """Lê e valida os valores binários dos critérios C1, C2, ... do CSV."""
    pontuacoes = {coluna: 0 for coluna in COLUNAS_SO}
    criterios = []

    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        colunas_necessarias = {"criterio"} | {
            coluna + "_valor" for coluna in COLUNAS_SO
        }
        if leitor.fieldnames is None or not colunas_necessarias.issubset(leitor.fieldnames):
            raise ValueError(
                "O CSV deve conter as colunas criterio, windows_valor, "
                "macos_valor e ubuntu_valor."
            )

        linha_pontuacao = None
        for numero_linha, linha in enumerate(leitor, start=2):
            criterio = (linha.get("criterio") or "").strip()
            if re.fullmatch(r"C\d+", criterio):
                criterios.append(criterio)
                for coluna in COLUNAS_SO:
                    valor = (linha.get(coluna + "_valor") or "").strip()
                    if valor not in {"0", "1"}:
                        raise ValueError(
                            f"Valor inválido na linha {numero_linha}, "
                            f"coluna {coluna}_valor: esperado 0 ou 1."
                        )
                    pontuacoes[coluna] += int(valor)
            elif criterio == "Pint":
                linha_pontuacao = linha

    if not criterios:
        raise ValueError("O CSV não contém critérios identificados como C1, C2, ...")

    if linha_pontuacao is not None:
        for coluna in COLUNAS_SO:
            valor = (linha_pontuacao.get(coluna + "_valor") or "").strip()
            if not valor.isdigit() or int(valor) != pontuacoes[coluna]:
                raise ValueError(
                    f"A soma dos critérios para {COLUNAS_SO[coluna]} não "
                    "corresponde ao valor registrado na linha Pint."
                )

    return criterios, pontuacoes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Plota a pontuação do checklist de flexibilidade por sistema operacional."
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=CSV_PADRAO,
        help="Caminho do CSV de checklist (padrão: arquivo consolidado do repositório).",
    )
    parser.add_argument(
        "--saida",
        type=Path,
        help="Caminho da imagem PNG gerada (padrão: ao lado do CSV).",
    )
    args = parser.parse_args()

    if not args.csv.is_file():
        parser.error(f"CSV não encontrado: {args.csv}")

    try:
        criterios, pontuacoes = ler_pontuacoes(args.csv)
    except (OSError, csv.Error, ValueError) as erro:
        parser.error(str(erro))

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        parser.error(
            "matplotlib não está instalado. Instale com: "
            "py -3 -m pip install matplotlib (Windows) ou "
            "python3 -m pip install matplotlib (macOS/Linux)."
        )

    destino = args.saida or args.csv.with_name("grafico-flexibilidade-checklist.png")
    destino.parent.mkdir(parents=True, exist_ok=True)

    nomes = [COLUNAS_SO[coluna] for coluna in COLUNAS_SO]
    valores = [pontuacoes[coluna] for coluna in COLUNAS_SO]
    limite = len(criterios)

    figura, eixo = plt.subplots(figsize=(8, 5))
    barras = eixo.bar(nomes, valores, color=["#4C78A8", "#F58518", "#54A24B"])
    eixo.set_title("Checklist de flexibilidade por sistema operacional")
    eixo.set_ylabel(f"Critérios atendidos (0 a {limite})")
    eixo.set_ylim(0, limite + 0.8)
    eixo.set_yticks(range(limite + 1))
    eixo.grid(axis="y", linestyle="--", alpha=0.35)
    eixo.set_axisbelow(True)
    eixo.bar_label(barras, padding=3)
    figura.tight_layout()
    figura.savefig(destino, dpi=150)
    plt.close(figura)

    print(f"Gráfico salvo em: {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
