# Protocolo de Instalação e Desinstalação – Flexibilidade (Q1)

**Responsável:** Bryan Smith Rodrigues Cavalcante (Dupla C)
**Métricas:** M-FLEX-01 (Taxa de sucesso), M-FLEX-02 (Tempo de instalação), M-FLEX-03 (Número de intervenções)
**Hipótese base (G3-H1):** Windows e macOS terão 100% de sucesso, 0 intervenções e < 2 min. Ubuntu levará de 2 a 5 min e exigirá ≥ 1 intervenção.

## 1. Preparação do Ambiente
- **Ambiente limpo:** Utilizar máquina virtual (VM) restaurada de um *snapshot* limpo ou um novo perfil de usuário no SO.
- **Rede:** Conexão com a internet ativa para baixar dependências.
- **Arquivo:** O instalador do Anki Desktop 26.09.3 já deve estar baixado previamente.
- **Guia:** Seguir estritamente as instruções oficiais em `docs.ankiweb.net`.

## 2. Definição de Intervenção (M-FLEX-03)
Considera-se uma intervenção qualquer ação manual extra que o avaliador precise realizar para que a instalação prossiga ou conclua com sucesso. Exemplos:
- Abrir terminal para instalar dependências (ex.: `sudo apt install zstd` no Ubuntu).
- Clicar em "Mais informações" -> "Executar assim mesmo" no SmartScreen do Windows.
- Ir em Preferências do Sistema -> Segurança e Privacidade -> "Abrir assim mesmo" no macOS (Gatekeeper).
- Alterar permissões de arquivo ou pasta.

## 3. Procedimento de Instalação (M-FLEX-01 e M-FLEX-02)
1. Iniciar o cronômetro **no exato momento em que o instalador é aberto**.
2. Executar a instalação.
3. Parar o cronômetro **quando a primeira janela principal do Anki for renderizada** na tela.
4. Registrar o tempo (em minutos) e o número de intervenções na ficha.
5. **Regra das 3 tentativas:** Cada sistema operacional (Windows, macOS, Ubuntu) deve ser testado 3 vezes. **Cada tentativa deve ser conduzida por um integrante diferente da equipe** (ex.: Bryan, Dante e Pedro).
6. Entre uma tentativa e outra, restaurar o *snapshot* da VM para garantir o ambiente limpo.

## 4. Procedimento de Desinstalação
1. Utilizar o mecanismo padrão do SO (Painel de Controle no Windows, Finder no macOS, Central de Software no Ubuntu).
2. Registrar se a desinstalação foi concluída com sucesso (Sim/Não).
3. Verificar e registrar se restaram **arquivos remanescentes** (ex.: pastas de configuração em `AppData`, `~/.local/share/Anki2`, etc.).

## 5. Registro de Evidências
- Gravar a tela de cada tentativa para comprovar o tempo e as intervenções.
- Preencher a ficha: `avaliacao/dados/flexibilidade/bruto/instalacao/ficha_instalacao.csv`.