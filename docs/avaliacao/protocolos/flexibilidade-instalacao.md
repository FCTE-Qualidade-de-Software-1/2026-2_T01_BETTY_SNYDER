# Flexibilidade: instalação e desinstalação

## 1. Definições

Esta página descreve o procedimento de instalação e desinstalação do Anki Desktop 26.09.3 nas três plataformas, executado pela Dupla C (responsável: Bryan Smith Rodrigues Cavalcante). As métricas M-FLEX-01 (T<sub>inst</sub>), M-FLEX-02 (T<sub>inst_t</sub>) e M-FLEX-03 (N<sub>int</sub>), bem como a hipótese G3-H1 e as faixas de julgamento, estão na [Fase 2](../../fase2.md).

Em síntese operacional, espera-se sucesso integral sem intervenções e tempo inferior a dois minutos no Windows e no macOS, e tempo entre dois e cinco minutos com ao menos uma intervenção no Ubuntu.

## 2. Pré-requisitos

- Ambiente limpo: VM com *snapshot* limpo ou novo perfil de usuário. Ver [Ambiente](ambiente.md).
- Rede ativa para dependências.
- Instalador do Anki Desktop 26.09.3 já baixado.
- Seguir as instruções oficiais em `docs.ankiweb.net`.

### Definição de intervenção (M-FLEX-03)

Ação manual extra para a instalação concluir, por exemplo: `sudo apt install zstd` no Ubuntu; SmartScreen (“Executar assim mesmo”) no Windows; Gatekeeper no macOS; alterar permissões.

## 3. Procedimento passo a passo

### Instalação (M-FLEX-01 e M-FLEX-02)

1. Iniciar o cronômetro ao abrir o instalador.
2. Executar a instalação.
3. Parar o cronômetro quando a primeira janela principal do Anki for renderizada.
4. Registrar tempo (min) e número de intervenções.
5. Três tentativas por SO, cada uma por integrante diferente; restaurar o *snapshot* entre tentativas.

### Desinstalação (qualitativa)

1. Remover pelo mecanismo padrão do SO.
2. Registrar sucesso (Sim/Não).
3. Verificar arquivos remanescentes (`AppData`, `~/.local/share/Anki2`, etc.).

## 4. Registro de dados

- Gravar a tela de cada tentativa.
- Ficha: `avaliacao/dados/flexibilidade/bruto/instalacao/ficha_instalacao.csv`.
- Padrão de nomes: [Dados](../../dados.md).

## 5. Critérios de invalidação

Descartar a tentativa se o ambiente não estiver limpo (snapshot não restaurado), se a rede cair no meio do download de dependências essenciais ou se o avaliador se desviar do guia oficial sem registrar a intervenção.

## 6. Relação com o instrumento e com os dados

A Parte C do [Pré-entrevista com participante](pre-entrevista-participante.md) espelha os campos de instalabilidade. Os demais testes de G3 estão em [Checklist](flexibilidade-checklist.md) e [Migração](flexibilidade-migracao.md). A visão das três frentes está em [Protocolos](index.md).
