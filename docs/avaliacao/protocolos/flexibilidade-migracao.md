# Flexibilidade: migração

## 1. Definições

Esta página descreve os cenários de migração de coleção entre máquinas e sistemas operacionais, executados pela Dupla C (Bryan Smith Rodrigues Cavalcante e Dante Fernandes Scarpati). As métricas M-FLEX-05 (T<sub>pd</sub>) e M-FLEX-06 (T<sub>sub</sub>), a questão G3-Q3 e a hipótese G3-H3 estão na [Fase 2](../../fase2.md).

## 2. Pré-requisitos

- Coleção padrão (E2-20): 10 mil cards, com mídia e histórico de revisões.
- Script `scripts/verificar_integridade.py` e Python 3 nas duas máquinas.
- Anki Desktop 26.09.3 instalado em SOs distintos.
- Conta de teste do AnkiWeb (M2); não usar contas pessoais.
- DB Browser for SQLite nas duas máquinas.
- Máquinas de referência: [Ambiente](ambiente.md).

Cenários (3 repetições na coleta; 1 no piloto):

| Cenário | Descrição | Origem e destino |
| --- | --- | --- |
| M1 | Arquivo `.apkg` (com agendamento e mídia) | Windows (Bryan) → Ubuntu (Dante) |
| M2 | Sincronização via AnkiWeb | Ubuntu (Dante) → Windows (Bryan) |

Antes de cada repetição: verificar banco na origem; copiar `collection.anki2` para pasta de trabalho (`colecao_origem`); perfil vazio no destino.

## 3. Procedimento passo a passo

### M1. Arquivo `.apkg`

1. Origem: iniciar cronômetro T<sub>sub</sub> (`t_inicio`); exportar baralho com agendamento e mídia (`export_m1.apkg`).
2. Transferir o arquivo (tempo de transferência só em `observacoes`).
3. Destino: importar no perfil vazio; copiar `collection.anki2` para `colecao_destino`.
4. Verificar integridade e parar o cronômetro (`t_fim`):

```bash
python scripts/verificar_integridade.py --antes /caminho/colecao_origem/collection.anki2 --depois /caminho/colecao_destino/collection.anki2 --saida diff_m1_r1.csv
```

### M2. AnkiWeb

1. Origem: cronômetro; login na conta de teste; sincronizar (enviar).
2. Destino: perfil vazio; mesmo login; sincronizar (baixar); copiar `collection.anki2`.
3. Rodar o script com `--saida diff_m2_r1.csv`; parar o cronômetro.

### Cálculo

- **T<sub>sub</sub>** = `t_fim` − `t_inicio` (min), excluindo o tempo de transferência do M1.
- **T<sub>pd</sub>** = (N<sub>totais</sub> − N<sub>diferentes</sub>) ÷ N<sub>totais</sub> × 100%, com N<sub>totais</sub> = notas + cards + baralhos + revisões + arquivos de mídia na origem; N<sub>diferentes</sub> = linhas `faltando_no_depois` ou `valor_diferente` no diff. Contagem SQL na origem:

```sql
SELECT (SELECT COUNT(*) FROM notes) AS notas,
       (SELECT COUNT(*) FROM cards) AS cards,
       (SELECT COUNT(*) FROM decks) AS baralhos,
       (SELECT COUNT(*) FROM revlog) AS revisoes;
```

Intervenções manuais entram em `intervencoes` (faixa Mínimo de T<sub>pd</sub> na Fase 2).

### Teste do script (antes do piloto)

Duas cópias da coleção; editar uma nota e apagar um card na cópia “depois”; o script deve listar `valor_diferente` e `faltando_no_depois`.

## 4. Registro de dados

Linhas da ficha e diffs em `avaliacao/dados/flexibilidade/bruto/migracao/`, nomes `M-FLEX-05_<origem>-<destino>_<cenário>_r<repetição>_<data>.csv`. Ver [Dados](../../dados.md).

## 5. Critérios de invalidação

Descartar a repetição se a cópia `collection.anki2` for lida com o Anki ainda aberto, se a conta pessoal for usada no lugar da conta de teste, ou se a verificação de integridade não for executada até o fim.

## 6. Relação com o instrumento e com os dados

Os campos de substituibilidade constam na Parte C do [Pré-entrevista com participante](pre-entrevista-participante.md). Os demais testes de G3 estão em [Instalação](flexibilidade-instalacao.md) e [Checklist](flexibilidade-checklist.md). A visão das três frentes está em [Protocolos](index.md).
