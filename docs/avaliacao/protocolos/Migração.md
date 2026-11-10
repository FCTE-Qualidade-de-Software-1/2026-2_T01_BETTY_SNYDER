# Protocolo de Migração – Flexibilidade (Q3)

Issue: **E2-32** · Responsáveis: Bryan e Dante (Dupla C) · Métricas: **M-FLEX-05** (T<sub>pd</sub>) e **M-FLEX-06** (T<sub>sub</sub>) · Questão: G3-Q3 · Hipótese: G3-H3 · Coleta: E2-71

## Cenários

- **M1 – Arquivo .apkg**: exportação da coleção com agendamento e mídia, importação em máquina de outro SO.
- **M2 – AnkiWeb**: sincronização da coleção via AnkiWeb entre duas máquinas de SOs diferentes.

Cada cenário tem **três repetições** na coleta (E2-71) e **uma repetição** no piloto (10/11). Pares de máquinas, conforme as máquinas de referência de Flexibilidade em [Ambiente de Avaliação](ambiente.md):

| Cenário | Origem | Destino |
|---|---|---|
| M1 | Windows (Bryan) | Ubuntu (Dante) |
| M2 | Ubuntu (Dante) | Windows (Bryan) |

## Pré-requisitos

- Coleção padrão (E2-20) disponível e íntegra: 10 mil cards, com mídia e histórico de revisões.
- Script `scripts/verificar_integridade.py` copiado para as duas máquinas, com Python 3 instalado.
- Anki Desktop 26.09.3 instalado nas duas máquinas (SOs distintos).
- Conexão com a internet e conta de teste do AnkiWeb da equipe (para M2). Não usar contas pessoais.
- DB Browser for SQLite nas duas máquinas, para as contagens da seção "Cálculo das métricas".

## Antes de cada repetição

1. Na origem, abrir o perfil de teste só com a coleção padrão e rodar Ferramentas, Verificar banco de dados.
2. Fechar o Anki e copiar o arquivo `collection.anki2` do perfil para uma pasta de trabalho (`colecao_origem`). O script e as contagens usam sempre essa **cópia**, nunca o arquivo em uso pelo Anki.
3. No destino, criar um perfil novo e vazio.

## Procedimento M1 – Arquivo .apkg

1. **Na máquina de origem**:
   - Iniciar o cronômetro de T<sub>sub</sub> e anotar o horário (`t_inicio`).
   - Abrir o Anki Desktop.
   - Selecionar o baralho da coleção padrão.
   - Exportar com as opções: "Incluir agendamento" e "Incluir mídia".
   - Salvar o arquivo `export_m1.apkg`.

2. **Transferir** o `export_m1.apkg` para a máquina de destino (pendrive, rede, etc.). O tempo de transferência é anotado em `observacoes`, porque depende da rede e não do Anki.

3. **Na máquina de destino**:
   - Abrir o Anki Desktop no perfil vazio.
   - Importar o `export_m1.apkg`.
   - Fechar o Anki e copiar o `collection.anki2` do perfil para a pasta de trabalho (`colecao_destino`).

4. **Verificação de integridade**:
   - Na máquina de destino, executar:
     ```bash
     python scripts/verificar_integridade.py --antes /caminho/para/colecao_origem/collection.anki2 --depois /caminho/para/colecao_destino/collection.anki2 --saida diff_m1_r1.csv
     ```
   - Parar o cronômetro quando o script terminar e anotar o horário (`t_fim`).

## Procedimento M2 – AnkiWeb

1. **Na máquina de origem**:
   - Iniciar o cronômetro de T<sub>sub</sub> e anotar o horário (`t_inicio`).
   - Fazer login com a conta de teste e clicar em Sincronizar. Se o Anki perguntar a direção, escolher enviar para o AnkiWeb.

2. **Na máquina de destino**:
   - Abrir o perfil vazio, fazer login com a mesma conta e sincronizar. Se o Anki perguntar a direção, escolher baixar do AnkiWeb.
   - Fechar o Anki e copiar o `collection.anki2` do perfil para a pasta de trabalho (`colecao_destino`).

3. **Verificação de integridade**: executar o script como no M1, com `--saida diff_m2_r1.csv`, e parar o cronômetro quando ele terminar (`t_fim`).

## Cálculo das métricas

**M-FLEX-06, tempo de substituição.** T<sub>sub</sub> = `t_fim` − `t_inicio`, em minutos: do início da exportação ou da sincronização até o fim da verificação de integridade, como define a issue E2-32. O tempo de transferência do arquivo no M1 fica de fora.

**M-FLEX-05, taxa de preservação de dados.** T<sub>pd</sub> = (N<sub>totais</sub> − N<sub>diferentes</sub>) ÷ N<sub>totais</sub> × 100%, em que:

- N<sub>totais</sub> é o número de itens na origem: notas, cards, baralhos, revisões e arquivos de mídia. Notas, cards, baralhos e revisões são contados abrindo a cópia `colecao_origem` no DB Browser for SQLite e executando, na aba Executar SQL:
  ```sql
  SELECT (SELECT COUNT(*) FROM notes)   AS notas,
         (SELECT COUNT(*) FROM cards)   AS cards,
         (SELECT COUNT(*) FROM decks)   AS baralhos,
         (SELECT COUNT(*) FROM revlog)  AS revisoes;
  ```
  A mídia é contada pelo número de arquivos da pasta `collection.media` do perfil de origem.
- N<sub>diferentes</sub> é o número de itens que aparecem no arquivo de saída do script com tipo `faltando_no_depois` ou `valor_diferente`. Itens do tipo `extra_no_depois` não são perda de dados: são anotados em `observacoes` e não entram no cálculo.

Qualquer intervenção manual necessária para concluir a migração (reimportar, refazer a sincronização, copiar mídia à mão) é registrada em `intervencoes`, porque define a faixa Mínimo de T<sub>pd</sub> na Tabela XI da Fase 2.

## Teste do script (antes do piloto)

Critério de conclusão da E2-32: o script precisa detectar uma alteração proposital.

1. Fazer duas cópias da coleção padrão: `teste_antes` e `teste_depois`.
2. Abrir `teste_depois` no Anki, editar o texto de um campo de uma nota e apagar um card. Fechar o Anki.
3. Rodar o script com `--antes` em `teste_antes` e `--depois` em `teste_depois`.
4. O teste passa se o arquivo de saída listar a nota editada como `valor_diferente` e o card apagado como `faltando_no_depois`. O resultado é registrado em `observacoes` da linha `teste` da ficha.

## Registro

Cada repetição gera uma linha em [`ficha_migracao.csv`](Flexibilidade/Migração/ficha_migracao.csv). A ficha preenchida e os arquivos de saída do script são salvos em `avaliacao/dados/flexibilidade/bruto/migracao/`, com nomes no padrão `M-FLEX-05_<origem>-<destino>_<cenário>_r<repetição>_<data>.csv`.
