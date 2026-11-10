#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
SCRIPT DE GERAÇÃO DE MASSA DE DADOS SINTÉTICA PARA TESTES DE EFICIÊNCIA (ANKI)
Disciplina: Qualidade de Software 1 - FCTE/UnB (2026.2)
Equipe: Betty Snyder | Dupla B: Eficiência de Desempenho
Issue: #55 (E2-20) - Massa de dados sintética (10k, 50k, 100k) e coleção padrão
Autor: Mateus de Siqueira Silva (Dupla B)
================================================================================

Este script gera arquivos de massa sintética de cartões para testes de estresse,
perfilamento de memória, tempo de inicialização (Cold Start), ordenação de grid
e medição de vazão do Anki (SQLite Check Database).

Formatos gerados:
  1. TSV / TXT: Formato delimitado por tabulação (Frente \t Verso \t Tags),
     ideal para importação ultra-rápida nativa no Anki.
  2. APKG: Pacote nativo binário do Anki gerado via genanki (dois cliques para importar).
"""

import os
import sys
import time
import random
import argparse

try:
    import genanki
    HAS_GENANKI = True
except ImportError:
    HAS_GENANKI = False


# -----------------------------------------------------------------------------
# Dicionários de termos para geração de conteúdo sintético pseudo-realista
# -----------------------------------------------------------------------------
DISCIPLINAS = [
    "Estruturas de Dados", "Sistemas Operacionais", "Qualidade de Software",
    "Banco de Dados", "Arquitetura de Computadores", "Compiladores",
    "Redes de Computadores", "Engenharia de Requisitos", "Segurança da Informação"
]

CONCEITOS = [
    "Algoritmo de Dijkstra", "Tabela Hash com Encadeamento", "Paging e MMU",
    "Condição de Corrida e Semáforos", "Normalização BCNF", "Modelo GQM (ISO 15939)",
    "Árvore B+ e Indexação", "Pipeline de Instruções RISC", "Protocolo TCP 3-Way Handshake",
    "Taxa de Cache Miss L1/L2", "Gerenciamento de Memória Virtual", "Padrão IEEE 829",
    "Deadlock e Algoritmo do Banqueiro", "Isolamento ACID", "Tratamento de Exceções em Rust"
]

EXPLICACOES = [
    "Garante complexidade logarítmica O(log n) para buscas e inserções ordenadas no disco.",
    "Evita degradação de vazão por meio de travamento refinado e regiões críticas isoladas.",
    "Mapeia endereços virtuais para molduras físicas na RAM com apoio do Translation Lookaside Buffer (TLB).",
    "Assegura consistência semântica e conformidade rigorosa aos requisitos da norma ISO/IEC 25010.",
    "Minimiza a sobrecarga de context-switch entre threads de usuário e o espaço do núcleo (kernel).",
    "Reduz o número de leituras aleatórias de I/O em disco utilizando agrupamento sequencial de blocos.",
    "Estabelece critérios objetivos de parada e medição com base em metas GQM e métricas PSM."
]


def gerar_registro(i: int, prefixo_lote: str):
    """Gera o par Pergunta / Resposta e Tags de um cartão sintético."""
    disc = random.choice(DISCIPLINAS)
    conc = random.choice(CONCEITOS)
    expl = random.choice(EXPLICACOES)
    
    frente = f"[{prefixo_lote}] Card #{i:06d}: O que caracteriza {conc} em {disc}?"
    verso = f"Definição #{i:06d}: {conc} é essencial para {disc}. Detalhe: {expl} (Sintético - Teste de Eficiência)"
    tags = f"sintetico_{prefixo_lote} {disc.replace(' ', '_').lower()} teste_estresse"
    
    return frente, verso, tags


def gerar_arquivo_tsv(caminho_arquivo: str, quantidade: int, prefixo: str):
    """Gera um arquivo TSV (Frente \t Verso \t Tags) otimizado em buffer."""
    print(f"  -> Gerando TSV: {caminho_arquivo} ({quantidade:,} cards)...")
    inicio = time.time()
    
    os.makedirs(os.path.dirname(os.path.abspath(caminho_arquivo)), exist_ok=True)
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        # Cabeçalho de diretiva do Anki para importação automática
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#tags column:3\n")
        
        buffer = []
        for i in range(1, quantidade + 1):
            frente, verso, tags = gerar_registro(i, prefixo)
            buffer.append(f"{frente}\t{verso}\t{tags}\n")
            
            if len(buffer) >= 10000:
                f.writelines(buffer)
                buffer.clear()
                
        if buffer:
            f.writelines(buffer)
            buffer.clear()
            
    duracao = time.time() - inicio
    tam_mb = os.path.getsize(caminho_arquivo) / (1024 * 1024)
    print(f"     [OK] Concluído em {duracao:.2f}s | Tamanho: {tam_mb:.2f} MB")


def gerar_arquivo_apkg(caminho_arquivo: str, quantidade: int, prefixo: str, model_id: int, deck_id: int):
    """Gera um arquivo binário nativo .apkg do Anki via biblioteca genanki."""
    if not HAS_GENANKI:
        print("     [AVISO] genanki não está instalado. Pulando geração de .apkg.")
        return

    print(f"  -> Gerando APKG nativo: {caminho_arquivo} ({quantidade:,} cards)...")
    inicio = time.time()
    
    os.makedirs(os.path.dirname(os.path.abspath(caminho_arquivo)), exist_ok=True)

    # Modelo padrão Anki
    modelo = genanki.Model(
        model_id,
        f"Modelo Eficiência {prefixo}",
        fields=[
            {"name": "Frente"},
            {"name": "Verso"},
        ],
        templates=[
            {
                "name": "Cartao 1",
                "qfmt": "{{Frente}}",
                "afmt": "{{FrontSide}}<hr id='answer'>{{Verso}}",
            },
        ],
        css="""
        .card {
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: center;
            color: #111;
            background-color: #fafafa;
        }
        """
    )

    baralho = genanki.Deck(deck_id, f"Eficiência Desempenho - {prefixo.upper()} ({quantidade:,} cards)")

    for i in range(1, quantidade + 1):
        frente, verso, tags = gerar_registro(i, prefixo)
        lista_tags = tags.split()
        nota = genanki.Note(model=modelo, fields=[frente, verso], tags=lista_tags)
        baralho.add_note(nota)

    pacote = genanki.Package(baralho)
    pacote.write_to_file(caminho_arquivo)
    
    duracao = time.time() - inicio
    tam_mb = os.path.getsize(caminho_arquivo) / (1024 * 1024)
    print(f"     [OK] Concluído em {duracao:.2f}s | Tamanho: {tam_mb:.2f} MB")


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de Massas de Dados Sintéticas para o Anki (Issue E2-20 | Betty Snyder)"
    )
    parser.add_argument(
        "--todos", action="store_true", default=True,
        help="Gera as três coleções padrão: 10k, 50k e 100k cards (padrão: True)"
    )
    parser.add_argument(
        "--tamanho", type=int, choices=[10000, 50000, 100000],
        help="Gera apenas uma quantidade específica (ex.: --tamanho 10000)"
    )
    parser.add_argument(
        "--apkg", action="store_true", default=True,
        help="Gera também os pacotes binários .apkg via genanki (padrão: True)"
    )
    parser.add_argument(
        "--somente-tsv", action="store_true",
        help="Gera apenas os arquivos TSV/TXT (mais rápido)"
    )
    parser.add_argument(
        "--output-dir", type=str, default="dados_sinteticos_teste",
        help="Diretório onde os arquivos gerados serão salvos (padrão: dados_sinteticos_teste)"
    )

    args = parser.parse_args()

    # Definição dos lotes conforme o Protocolo de Medição da Fase 3
    lotes = [
        {"qtd": 10000, "nome": "10k", "model_id": 1607392319, "deck_id": 2059400110},
        {"qtd": 50000, "nome": "50k", "model_id": 1607392320, "deck_id": 2059400120},
        {"qtd": 100000, "nome": "100k", "model_id": 1607392321, "deck_id": 2059400130},
    ]

    if args.tamanho:
        lotes = [l for l in lotes if l["qtd"] == args.tamanho]

    print("=================================================================")
    print(" 🚀 INICIANDO GERAÇÃO DE MASSA DE DADOS (ISSUE E2-20)")
    print(f" Diretório de saída: {os.path.abspath(args.output_dir)}")
    print("=================================================================")

    gerar_apkg = args.apkg and not args.somente-args.somente_tsv if hasattr(args, 'somente') else (args.apkg and not args.somente_tsv)

    tempo_total_inicio = time.time()

    for lote in lotes:
        qtd = lote["qtd"]
        nome = lote["nome"]
        
        # 1. Arquivo TSV
        tsv_path = os.path.join(args.output_dir, f"colecao_{nome}.txt")
        gerar_arquivo_tsv(tsv_path, qtd, nome)
        
        # 2. Arquivo APKG (se solicitado)
        if gerar_apkg:
            apkg_path = os.path.join(args.output_dir, f"colecao_{nome}.apkg")
            gerar_arquivo_apkg(apkg_path, qtd, nome, lote["model_id"], lote["deck_id"])
            
        print("-----------------------------------------------------------------")

    tempo_total = time.time() - tempo_total_inicio
    print(f"🎉 Geração finalizada com sucesso em {tempo_total:.2f} segundos!")
    print(f"Os arquivos estão prontos para importação no Anki em:")
    print(f"  -> {os.path.abspath(args.output_dir)}")
    print("=================================================================")


if __name__ == "__main__":
    main()
