# Flexibilidade: checklist de integração

## 1. Definições

Esta página padroniza a verificação dos dez critérios de integração do Anki Desktop 26.09.3 com o sistema operacional, sob responsabilidade de Dante Fernandes Scarpati (Dupla C). A métrica é M-FLEX-04 (P<sub>int</sub>), associada à questão G3-Q2 (adaptabilidade). As faixas de julgamento e a hipótese G3-H2 estão na [Fase 2](../../fase2.md).

P<sub>int</sub> é a soma dos critérios atendidos (cada critério vale 0 ou 1). Em operação, o avaliador pontua e registra capturas; o conferente revisa as evidências sem refazer o teste.

## 2. Pré-requisitos

| Sistema | Avaliador (máquina de referência) | Conferente |
| --- | --- | --- |
| Windows | Bryan | Dante |
| macOS | Davi | Bryan |
| Ubuntu | Dante | Bryan |

Máquinas: [Ambiente](ambiente.md). O avaliador executa e pontua; o conferente revê capturas. Divergência: vale a regra escrita do critério; anotar em `observacoes`.

Preparação:

1. Instalar o Anki 26.09.3 ([instalação](flexibilidade-instalacao.md)) e abrir uma vez.
2. Perfil de teste `checklist` (sem perfil pessoal).
3. Arquivo `.apkg` pequeno em Downloads.
4. Editor com negrito, itálico e uma imagem.
5. Registrar SO, arquitetura, permissão de admin; no Ubuntu, Wayland ou X11.
6. Capturas: `M-FLEX-04_<SO>_c<número>_<data>.png` em `avaliacao/dados/flexibilidade/bruto/checklist/`.

## 3. Procedimento passo a passo

### Regras de pontuação

- **Atendido (1):** comportamento completo, sem extensões.
- **Não atendido (0):** não ocorre, parcial ou exige configuração fora do Anki/SO padrão.
- Recurso inexistente no Anki: 0, marcando a coluna correspondente.
- Dúvida: repetir uma vez; se persistir, 0 e descrever.

### Os 10 critérios

**C1. Ícone na bandeja.** Com o Anki aberto (e após minimizar), o ícone aparece na área de notificação. Barra de tarefas/Dock não conta.

**C2. Atalhos globais.** Algum atalho do Anki age com o app fora de foco.

**C3. Associação `.apkg`.** Duplo clique no `.apkg` abre o Anki e inicia a importação.

**C4. Diálogos nativos.** Em Arquivo, Importar e Exportar usam o seletor nativo do SO.

**C5. Tema escuro sincronizado.** Com tema “seguir o sistema”, o Anki acompanha modo escuro/claro do SO.

**C6. Notificações nativas.** Ação em segundo plano (ex.: sincronização) gera notificação na central do SO.

**C7. Área de transferência.** Colar texto formatado e imagem no Anki; copiar do Anki para o editor.

**C8. Menu contextual nativo.** Botão direito em campo de texto: recortar/copiar/colar do sistema.

**C9. Arrastar e soltar `.apkg`.** Soltar o arquivo na janela principal inicia a importação.

**C10. Acessibilidade.** Com leitor de tela (Narrador / VoiceOver / Orca), Tab anuncia os cinco itens da barra superior e os baralhos.

## 4. Registro de dados

Planilha modelo: [`flexibilidade-checklist-registro.csv`](flexibilidade-checklist-registro.csv). Preenchida: `M-FLEX-04_registro_<data>.csv` em `avaliacao/dados/flexibilidade/bruto/checklist/`, com as capturas. Ver [Dados](../../dados.md).

## 5. Critérios de invalidação / análise

1. Somar c<sub>i</sub> por sistema e classificar P<sub>int</sub>.
2. Comparar com H2. Se houver diferença de um ponto, registrar o critério responsável.
3. Separar falha de adaptação de recurso inexistente.
4. Pontuações abaixo do alvo geram recomendações priorizadas, conforme a Fase 2.

Piloto (10/11): se C1, C2, C6 ou C8 forem inexistentes em todos os SOs, a equipe decide antes da coleta se mantém a contagem ou recalcula sobre critérios aplicáveis (registrar em ata).

## 6. Relação com o instrumento e com os dados

Os campos de adaptabilidade constam na Parte C do [Pré-entrevista com participante](pre-entrevista-participante.md). Os demais testes de G3 estão em [Instalação](flexibilidade-instalacao.md) e [Migração](flexibilidade-migracao.md). A visão das três frentes está em [Protocolos](index.md).
