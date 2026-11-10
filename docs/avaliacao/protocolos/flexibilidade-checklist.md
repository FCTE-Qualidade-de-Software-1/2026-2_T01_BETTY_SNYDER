# Flexibilidade: procedimento do checklist de integração

Issue: **E2-31** · Responsável: Dante (Dupla C) · Métrica: **M-FLEX-04** (P<sub>int</sub>) · Questão: G3-Q2 (Adaptabilidade) · Hipótese: G3-H2 · Coleta: E2-71

## 1. Objetivo

Padronizar como o avaliador verifica, em cada sistema operacional, os 10 critérios de integração do Anki Desktop 26.09.3 com o sistema definidos na Fase 2, de modo que a pontuação P<sub>int</sub> seja repetível por outro avaliador.

## 2. O que é medido

P<sub>int</sub> é a soma dos critérios atendidos: P<sub>int</sub> = c<sub>1</sub> + ... + c<sub>10</sub>, com c<sub>i</sub> = 1 quando o critério é atendido e c<sub>i</sub> = 0 caso contrário. A faixa vai de 0 a 10 e o resultado é classificado pela Tabela XI da Fase 2:

| Nível | P<sub>int</sub> |
|---|---|
| Insatisfatório | menor que 6 |
| Mínimo | 6 ou 7 |
| Alvo | 8 ou 9 |
| Excelente | 10 |

H2 espera 10/10 no macOS e 9/10 no Windows e no Ubuntu.

## 3. Quem, onde e quando

Cada sistema é avaliado por um integrante, na máquina de referência de Flexibilidade, e conferido por outro, como define o planejamento da E2 (seção 5.3).

| Sistema | Máquina de referência e avaliador | Conferente |
|---|---|---|
| Windows | Bryan | Dante |
| macOS | Davi | Bryan |
| Ubuntu | Dante | Bryan |

As máquinas estão descritas em [Ambiente de Avaliação](ambiente.md). O **avaliador** executa os passos, pontua e salva as capturas. O **conferente** revê as capturas de cada critério, sem refazer o teste, e confirma ou contesta a pontuação. Em caso de divergência, vale a regra escrita do critério, e a decisão é anotada em `observacoes`.

O piloto é em 10/11/2026 e a coleta (E2-71) vai até 12/11/2026. O teste leva cerca de 30 minutos por sistema.

## 4. Preparação (antes de começar)

1. Instalar o Anki Desktop 26.09.3 pelo procedimento da E2-30 e abrir o aplicativo uma vez.
2. Criar um perfil de teste chamado `checklist` (Arquivo, Trocar perfil, Adicionar). Não usar perfis pessoais.
3. Ter à mão um arquivo `.apkg` pequeno, de preferência exportado da massa de dados sintética da E2-20, salvo na pasta Downloads.
4. Ter aberto um editor de texto com formatação (LibreOffice Writer, Word ou Pages) com um parágrafo que tenha **negrito** e *itálico* e uma imagem.
5. Registrar na planilha (seção 7) a versão exata do sistema, a arquitetura (x64 ou ARM) e se o usuário tem permissão de administrador, que são os fatores de variação da Fase 2. No Ubuntu, registrar também a sessão gráfica (Wayland ou X11), que pode alterar o resultado dos critérios 1, 6 e 9.
6. Iniciar a captura de tela. Cada critério gera uma evidência, nomeada como `M-FLEX-04_<SO>_c<número>_<data>.png` (por exemplo, `M-FLEX-04_ubuntu_c03_2026-11-11.png`), salva em `avaliacao/dados/flexibilidade/bruto/checklist/`.

## 5. Regras gerais de pontuação

- **Atendido (1):** o comportamento descrito no critério ocorre por completo, sem instalar extensões, plugins ou complementos do Anki.
- **Não atendido (0):** o comportamento não ocorre, ocorre pela metade ou exige configuração fora do Anki e do sistema padrão.
- **Recurso inexistente:** se o Anki não oferece o recurso, o critério vale 0, como define a Fase 2. Marque também a coluna "Recurso inexistente" no formulário, para separar ausência de recurso de falha na análise.
- **Dúvida:** repita o passo uma vez. Se persistir, pontue 0 e descreva o que aconteceu em Observações.
- Configurações do Anki ficam no padrão, exceto o tema (critério 5).

## 6. Os 10 critérios

### C1. Ícone na bandeja do sistema

1. Com o Anki aberto, olhar a área de notificação: canto inferior direito no Windows, barra de menus no canto superior direito no macOS e área de indicadores no canto superior direito no Ubuntu.
2. Minimizar a janela do Anki e olhar de novo.

**Atendido se** um ícone do Anki aparece nessa área enquanto o aplicativo está aberto. O ícone na barra de tarefas ou no Dock não conta.

### C2. Atalhos globais de teclado

1. Consultar Ferramentas, Preferências e o manual do Anki para identificar atalhos que funcionem fora da janela do aplicativo.
2. Se houver, deixar outra janela em primeiro plano e acionar o atalho.

**Atendido se** algum atalho do Anki age com o aplicativo fora de foco. Atalhos que só funcionam com a janela do Anki ativa não contam.

### C3. Associação de arquivos `.apkg`

1. No gerenciador de arquivos (Explorador, Finder ou Arquivos), dar duplo clique no `.apkg` de teste.

**Atendido se** o Anki abre (ou vem para frente) e inicia a importação do arquivo, sem precisar escolher o programa em "Abrir com".

### C4. Diálogos nativos de abrir e salvar

1. No Anki, abrir Arquivo, Importar.
2. Depois, abrir Arquivo, Exportar e avançar até a escolha do local de salvamento.

**Atendido se** as duas janelas de arquivo são as do sistema: as do Explorador no Windows, as do Finder no macOS e o seletor de arquivos do GNOME no Ubuntu, com os atalhos laterais e a busca do sistema.

### C5. Tema escuro sincronizado com o sistema

1. No Anki, abrir Ferramentas, Preferências e escolher, em Tema, a opção que segue o sistema.
2. Com o Anki aberto, mudar o sistema para o modo escuro:
    - Windows: Configurações, Personalização, Cores, Escolha o modo, Escuro.
    - macOS: Ajustes do Sistema, Aparência, Escuro.
    - Ubuntu: Configurações, Aparência, Estilo, Escuro.
3. Observar a janela principal e a tela de revisão. Voltar o sistema para o modo claro e observar de novo.

**Atendido se** o Anki acompanha a mudança nos dois sentidos. Registrar em Observações se foi preciso reiniciar o Anki para a troca aparecer.

### C6. Notificações nativas

1. Executar no Anki uma ação que conclua uma tarefa em segundo plano, como a sincronização com a conta de teste do AnkiWeb.
2. Olhar a central de notificações do sistema.

**Atendido se** uma notificação do Anki aparece na central de notificações do sistema. Mensagens dentro da própria janela do Anki não contam.

### C7. Integração com a área de transferência

1. Copiar, do editor de texto da preparação, o parágrafo formatado e colar no campo Frente da tela Adicionar do Anki.
2. Copiar a imagem e colar no campo Verso.
3. Copiar um texto de um campo do Anki e colar no editor de texto.

**Atendido se** os três passos funcionam: a formatação básica (negrito e itálico) é mantida, a imagem aparece no card e o texto chega ao outro aplicativo.

### C8. Menu contextual nativo

1. Clicar com o botão direito em um campo de texto da tela Adicionar.

**Atendido se** aparece um menu com as ações padrão de edição do sistema (recortar, copiar, colar) e elas funcionam.

### C9. Arrastar e soltar arquivos `.apkg`

1. Arrastar o `.apkg` de teste do gerenciador de arquivos e soltar sobre a janela principal do Anki.

**Atendido se** a importação do arquivo começa.

### C10. Compatibilidade com recursos de acessibilidade do SO

1. Ligar o leitor de tela do sistema: Narrador no Windows (Ctrl + Windows + Enter), VoiceOver no macOS (Command + F5) e Orca no Ubuntu (Super + Alt + S).
2. Com a janela principal do Anki em foco, navegar com a tecla Tab pelos botões e pela lista de baralhos.
3. Desligar o leitor de tela ao terminar.

**Atendido se** o leitor anuncia, ao passar por eles, o nome dos cinco itens da barra superior da janela principal (Baralhos, Adicionar, Navegar, Estatísticas e Sincronizar) e o nome dos baralhos da lista.

## 7. Planilha de registro

O registro é feito na planilha [`flexibilidade-checklist-registro.csv`](flexibilidade-checklist-registro.csv), no formato critério × sistema. Para cada sistema há duas colunas: o valor (0 ou 1) e o link da evidência (o nome do arquivo da captura). As últimas linhas guardam o avaliador, o conferente, a data e os fatores de variação de cada sistema.

Ao final, a linha `Pint` recebe a soma dos valores de cada sistema. Critérios com recurso inexistente valem 0 e são anotados na coluna `observacoes`, por exemplo: `Windows e Ubuntu: recurso inexistente`.

A planilha preenchida é salva em `avaliacao/dados/flexibilidade/bruto/checklist/` com o nome `M-FLEX-04_registro_<data>.csv`, junto das capturas.

## 8. Análise

1. Somar os c<sub>i</sub> de cada sistema e classificar P<sub>int</sub> pela tabela da seção 2.
2. Comparar com H2. Uma diferença de um ponto em relação à hipótese é registrada com o critério responsável.
3. Separar, na discussão, os critérios que falharam dos que valem 0 por recurso inexistente. Uma falha em um sistema que funciona nos outros indica problema de adaptação. Um recurso inexistente em todos os sistemas indica limite do produto ou do checklist.
4. Pontuações abaixo do alvo viram recomendações priorizadas, conforme a regra de julgamento da Fase 2.

## 9. Ponto de atenção para o piloto (10/11)

Os critérios C1, C2, C6 e C8 descrevem recursos que podem não existir no Anki em nenhum sistema. Se o piloto confirmar isso, o máximo alcançável fica abaixo de 10 e H2 (10/10 no macOS) deixa de ser alcançável. Nesse caso, a equipe decide antes da coleta entre manter a contagem atual ou calcular P<sub>int</sub> sobre os critérios aplicáveis. A decisão deve ser registrada em ata e na Fase 2.
