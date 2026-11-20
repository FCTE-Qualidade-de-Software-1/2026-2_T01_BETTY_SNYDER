#!/usr/bin/env bash
# ==============================================================================
# FCTE / UnB - Qualidade de Software 1 (2026-2) | Grupo 01: Betty Snyder
# Script: executar_testes.sh (Menu Interativo para Linux/Ubuntu e macOS)
# Autores: Dupla B (Karolina Vieira Barbosa e Mateus de Siqueira Silva)
# ==============================================================================

set -e

DIR_SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIR_RAIZ="$(cd "$DIR_SCRIPTS/../../.." && pwd)"
DIR_SAIDA="$DIR_RAIZ/docs/avaliacao/dados/desempenho/bruto"

mkdir -p "$DIR_SAIDA"

# Detecta o Sistema Operacional (Ubuntu/Linux vs macOS)
OS_UNAME="$(uname -s)"
if [ "$OS_UNAME" = "Darwin" ]; then
    SO_TAG="macos"
    COMANDO_LIMPEZA="sudo purge"
else
    SO_TAG="ubuntu"
    COMANDO_LIMPEZA="sync && echo 3 | sudo tee /proc/sys/vm/drop_caches"
fi

# Detecta interpretador python3
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
else
    echo "[ERRO] Interpretador Python não encontrado no PATH!"
    exit 1
fi

mostrar_menu() {
    clear
    echo "========================================================================"
    echo "🔬 BETTY SNYDER - PAINEL DE EXECUÇÃO DE MEDIÇÕES ($OS_UNAME / ISO 25010)"
    echo "📂 Destino dos CSVs: $DIR_SAIDA"
    echo "🏷️ Sufixo de SO: $SO_TAG"
    echo "========================================================================"
    echo ""
    echo "Escolha o cenário que deseja executar:"
    echo "  [1] Cenário 2A: Repouso Basal (5 min / 300s) -> CPU_repouso_${SO_TAG}_01.csv"
    echo "  [2] Cenário 2A: Threads em Repouso (300s)   -> threads_repouso_${SO_TAG}_01.csv"
    echo "  [3] Cenário 2B: Estresse de Recursos (180s) -> metricas_estresse_${SO_TAG}_01.csv"
    echo "  [4] Cenário 2B: Threads sob Estresse (180s) -> threads_estresse_${SO_TAG}_01.csv"
    echo "  [5] Cenário 1:  Cold Start (Inicialização)  -> T_ini_coldstart_${SO_TAG}_01.csv"
    echo "  [6] Sair"
    echo ""
}

while true; do
    mostrar_menu
    read -rp "Digite o número da opção desejada [1-6]: " OPCAO

    case "$OPCAO" in
      1)
        echo ""
        echo "▶️ Iniciando Cenário 2A: Repouso Basal (300 segundos)..."
        echo "⚠️ Certifique-se de que o Anki está ABERTO em repouso."
        echo "⚠️ Por favor, não mexa no mouse nem no teclado durante os 5 minutos!"
        echo ""
        "$PYTHON_CMD" "$DIR_SCRIPTS/coletor.py" --cenario repouso --duracao 300 \
          --saida "$DIR_SAIDA/CPU_repouso_${SO_TAG}_01.csv"
        ;;
      2)
        echo ""
        echo "▶️ Iniciando Cenário 2A: Auditoria de Threads em Repouso (300s)..."
        "$PYTHON_CMD" "$DIR_SCRIPTS/analisador_threads.py" --modo realtime --duracao 300 --cenario repouso \
          --saida "$DIR_SAIDA/threads_repouso_${SO_TAG}_01.csv"
        ;;
      3)
        echo ""
        echo "▶️ Iniciando Cenário 2B: Estresse de Recursos (180s)..."
        echo "⚠️ Com a coleção de 100k aberta, execute no Anki:"
        echo "   1. Abrir o Painel (Browse / atalho 'B')"
        echo "   2. Ordenar por Modificado"
        echo "   3. Executar 'Verificar banco de dados' (Ctrl + Shift + D)"
        echo ""
        "$PYTHON_CMD" "$DIR_SCRIPTS/coletor.py" --cenario estresse --duracao 180 \
          --saida "$DIR_SAIDA/metricas_estresse_${SO_TAG}_01.csv"
        ;;
      4)
        echo ""
        echo "▶️ Iniciando Cenário 2B: Auditoria de Threads sob Carga (180s)..."
        "$PYTHON_CMD" "$DIR_SCRIPTS/analisador_threads.py" --modo realtime --duracao 180 --cenario estresse \
          --saida "$DIR_SAIDA/threads_estresse_${SO_TAG}_01.csv" --grafico
        ;;
      5)
        echo ""
        echo "▶️ Iniciando Cenário 1: Cold Start (Inicialização a Frio)..."
        echo "⚠️ Requisitos prévios:"
        echo "   1. Feche o Anki completamente ('pkill -f anki' ou feche a janela)."
        echo "   2. Limpe os caches do SO executando: $COMANDO_LIMPEZA"
        echo ""
        "$PYTHON_CMD" "$DIR_SCRIPTS/coletor.py" --cenario cold_start \
          --saida "$DIR_SAIDA/T_ini_coldstart_${SO_TAG}_01.csv"
        ;;
      6)
        echo "Saindo do painel de medições."
        exit 0
        ;;
      *)
        echo "Opção inválida! Pressione Enter para continuar..."
        read -r
        continue
        ;;
    esac

    echo ""
    echo "========================================================================"
    echo "✅ Medição finalizada com sucesso!"
    echo "📁 Destino: $DIR_SAIDA"
    echo "========================================================================"
    echo "Pressione Enter para voltar ao menu principal..."
    read -r
done
