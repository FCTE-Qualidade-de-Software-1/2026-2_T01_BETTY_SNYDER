# Dados de avaliação

Estrutura por característica ISO/IEC 25010:

```
dados/
  interacao/
    bruto/
    consolidado/
  desempenho/
    bruto/
    consolidado/
  flexibilidade/
    bruto/
    consolidado/
```

## Nomenclatura dos arquivos brutos

Padrão preferido: `métrica_cenário_execução` (ou código de participante + data).

Exemplos:

- `M-INT-01_reconhecimento_PA01.csv`
- `M-INT_tarefas.csv` (várias execuções em um arquivo tabular; coluna `participante`)
- `ficha_PA01_2026-11-12.pdf` (ficha escaneada; código + data)
- `T_ini_coldstart_01.csv` (laboratório de desempenho)

Exceção documentada: `sessoes.csv` é o **índice** das sessões (data, formato e ata; mídia fora do repo) e não segue o trio métrica-cenário-execução.

## Códigos de participante

| Código | Grupo | Critério (triagem) |
| --- | --- | --- |
| PA01, PA02 | A : iniciantes | Nunca utilizou o Anki |
| PB01, PB02, PB03 | B : frequentes | Uso regular ≥ 4 semanas, ≥ 3 dias/semana recentes; já criou, revisou e sincronizou |

A tabela que liga código a nome/e-mail fica **fora deste repositório**. Nos CSVs e fichas públicas use apenas o código.

## Gravações

Conforme o TCLE, arquivos de tela/áudio ficam em pasta privada da equipe. Neste repositório:

- Índice: `interacao/bruto/sessoes.csv` (e índices análogos se outras características gravarem sessão).
- Colunas mínimas: `participante,grupo,data,formato,duracao,ata_gitpage,observacoes`. A mídia não é versionada.
