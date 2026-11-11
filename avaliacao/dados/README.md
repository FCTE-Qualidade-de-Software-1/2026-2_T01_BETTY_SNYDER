# Dados da avaliação

Dados do **produto Anki** (não confundir com `gestao-psm/`, que mede o andamento do projeto).

## Pastas por característica

| Pasta | Característica ISO 25010:2023 | Objetivo GQM |
| --- | --- | --- |
| `interacao/` | Capacidade de interação | G1 |
| `desempenho/` | Eficiência de desempenho | G2 |
| `flexibilidade/` | Flexibilidade | G3 |

Em cada uma: `bruto/` (observações e execuções) e `consolidado/` (agregados que apontam para o bruto).

## Padrão de nomes: `<métrica>_<cenário>_<execução>`

Separador `_`.

| Peça | Conteúdo | Exemplos |
| --- | --- | --- |
| métrica | Código GQM | `M-INT-01`, `M-INT_tarefas`, `T_ini`, `T_inst` |
| cenário | Tarefa, rodada ou ambiente | `reconhecimento`, `A3`, `coldstart`, `win11` |
| execução | Participante ou repetição de lab | `PA01`, `PB02`, `01` |

Exemplos:

- `M-INT-01_reconhecimento_PA01.csv`
- `M-INT_tarefas.csv` (várias execuções em um arquivo tabular; coluna `participante`)
- `ficha_PA01_2026-11-12.pdf` (ficha escaneada; código + data)
- `T_ini_coldstart_01.csv` (laboratório de desempenho)

Exceção documentada: `gravacoes.csv` é o **índice** das gravações (mídia fora do repo) e não segue o trio métrica-cenário-execução.

## Códigos de participante

| Código | Grupo | Critério (triagem) |
| --- | --- | --- |
| PA01, PA02 | A — iniciantes | Nunca utilizou o Anki |
| PB01, PB02, PB03 | B — frequentes | Uso regular ≥ 4 semanas, ≥ 3 dias/semana recentes; já criou, revisou e sincronizou |

A tabela que liga código a nome/e-mail fica **fora deste repositório**. Nos CSVs e fichas públicas use apenas o código.

## Gravações

Conforme o TCLE, arquivos de tela/áudio ficam em pasta privada da equipe. Neste repositório:

- Índice: `interacao/bruto/gravacoes.csv` (e índices análogos se outras características gravarem sessão).
- Colunas mínimas: `participante,grupo,data,formato,arquivo_gravacao,observacoes`, onde `arquivo_gravacao` é o caminho **privado** (não um blob no Git).
