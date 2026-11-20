@echo off
chcp 65001 > nul
rem ==============================================================================
rem FCTE / UnB - Qualidade de Software 1 (2026-2) | Grupo 01: Betty Snyder
rem Script: executar_testes.cmd (Menu Interativo de Execução das Medições no Windows)
rem Autores: Dupla B (Karolina Vieira Barbosa e Mateus de Siqueira Silva)
rem ==============================================================================

setlocal enabledelayedexpansion

set "DIR_SCRIPTS=%~dp0"
set "DIR_RAIZ=%DIR_SCRIPTS%..\..\..\"
set "DIR_SAIDA=%DIR_RAIZ%docs\avaliacao\dados\desempenho\bruto\"

if not exist "%DIR_SAIDA%" mkdir "%DIR_SAIDA%"

rem Detecta o interpretador Python (py ou python)
where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if %ERRORLEVEL% equ 0 (
        set "PYTHON_CMD=python"
    ) else (
        echo [ERRO] Python nao foi encontrado no PATH do Windows!
        echo Instale o Python 3.10+ ou adicione-o as variaveis de ambiente.
        pause
        exit /b 1
    )
)

:MENU
cls
echo ========================================================================
echo 🔬 BETTY SNYDER - PAINEL DE EXECUÇÃO DE MEDIÇÕES NO WINDOWS (ISO 25010)
echo 📂 Destino dos CSVs: %DIR_SAIDA%
echo 🐍 Interpretador: %PYTHON_CMD%
echo ========================================================================
echo.
echo Escolha o cenário que deseja executar:
echo   [1] Cenário 2A: Repouso Basal (5 minutos / 300s) -^> CPU_repouso_windows_01.csv
echo   [2] Cenário 2A: Threads em Repouso (300s)       -^> threads_repouso_windows_01.csv
echo   [3] Cenário 2B: Estresse de Recursos (180s)     -^> metricas_estresse_windows_01.csv
echo   [4] Cenário 2B: Threads sob Estresse (180s)     -^> threads_estresse_windows_01.csv
echo   [5] Cenário 1:  Cold Start (Inicializacao Fria) -^> T_ini_coldstart_windows_01.csv
echo   [6] Sair
echo.
set /p OPCAO="Digite o número da opção desejada [1-6]: "

if "%OPCAO%"=="1" goto CENARIO_1_REPOUSO
if "%OPCAO%"=="2" goto CENARIO_2_THREADS_REPOUSO
if "%OPCAO%"=="3" goto CENARIO_3_ESTRESSE
if "%OPCAO%"=="4" goto CENARIO_4_THREADS_ESTRESSE
if "%OPCAO%"=="5" goto CENARIO_5_COLDSTART
if "%OPCAO%"=="6" goto FIM
echo Opcao invalida! Pressione qualquer tecla para tentar novamente.
pause >nul
goto MENU

:CENARIO_1_REPOUSO
cls
echo ========================================================================
echo ▶️ Iniciando Cenário 2A: Repouso Basal (300 segundos)...
echo ⚠️ Certifique-se de que o Anki está ABERTO com uma coleção limpa.
echo ⚠️ Não mexa no teclado ou mouse durante a coleta (5 minutos).
echo ========================================================================
%PYTHON_CMD% "%DIR_SCRIPTS%coletor.py" --cenario repouso --duracao 300 --saida "%DIR_SAIDA%CPU_repouso_windows_01.csv"
goto CONCLUIDO

:CENARIO_2_THREADS_REPOUSO
cls
echo ========================================================================
echo ▶️ Iniciando Cenário 2A: Auditoria de Threads em Repouso (300s)...
echo ⚠️ Certifique-se de que o Anki está ABERTO em repouso.
echo ========================================================================
%PYTHON_CMD% "%DIR_SCRIPTS%analisador_threads.py" --modo realtime --duracao 300 --cenario repouso --saida "%DIR_SAIDA%threads_repouso_windows_01.csv"
goto CONCLUIDO

:CENARIO_3_ESTRESSE
cls
echo ========================================================================
echo ▶️ Iniciando Cenário 2B: Estresse de Recursos (180s)...
echo ⚠️ Com a coleção de 100k aberta, execute a sequência:
echo    1. Abrir o Browse (Painel)
echo    2. Ordenar por Modificado
echo    3. Executar 'Verificar banco de dados' (Ctrl + Shift + D)
echo ========================================================================
%PYTHON_CMD% "%DIR_SCRIPTS%coletor.py" --cenario estresse --duracao 180 --saida "%DIR_SAIDA%metricas_estresse_windows_01.csv"
goto CONCLUIDO

:CENARIO_4_THREADS_ESTRESSE
cls
echo ========================================================================
echo ▶️ Iniciando Cenário 2B: Auditoria de Threads sob Carga (180s)...
echo ⚠️ Dispare as operações de carga (Check Database) no Anki durante o teste.
echo ========================================================================
%PYTHON_CMD% "%DIR_SCRIPTS%analisador_threads.py" --modo realtime --duracao 180 --cenario estresse --saida "%DIR_SAIDA%threads_estresse_windows_01.csv" --grafico
goto CONCLUIDO

:CENARIO_5_COLDSTART
cls
echo ========================================================================
echo ▶️ Iniciando Cenário 1: Cold Start (Inicialização a Frio)...
echo ⚠️ Requisitos prévios:
echo    1. FECHE o Anki completamente (confira no Gerenciador de Tarefas).
echo    2. Esvazie a Standby List no RAMMap (Empty -> Empty Standby List)
echo       ou reinicie a máquina.
echo ========================================================================
%PYTHON_CMD% "%DIR_SCRIPTS%coletor.py" --cenario cold_start --saida "%DIR_SAIDA%T_ini_coldstart_windows_01.csv"
goto CONCLUIDO

:CONCLUIDO
echo.
echo ========================================================================
echo ✅ Medição concluída com sucesso!
echo 📁 Arquivo salvo em: %DIR_SAIDA%
echo ========================================================================
echo.
pause
goto MENU

:FIM
echo Saindo do painel de medições.
exit /b 0
