# Avaliação do produto Anki

Esta pasta concentra os artefatos da **Fase 3 (plano)** e da **Fase 4 (execução)** da avaliação de qualidade do Anki Desktop 26.09.3 e do fluxo AnkiWeb, segundo a ISO/IEC 25010:2023 e o GQM da [Fase 2](../docs/fase2.md).

Objetivos desta estrutura:

- **Rastreabilidade** entre dado bruto e métrica (critério F4-C2; premissas 4 e 5 do enunciado).
- **Proteção da identificação** dos participantes (apenas códigos no repositório público).

## Árvore

```text
avaliacao/
  protocolos/     Instrumento unificado e protocolos por característica
  scripts/        Coletores e consolidados (quando existirem)
  dados/
    interacao/      {bruto, consolidado}   — Capacidade de interação (G1)
    desempenho/     {bruto, consolidado}   — Eficiência de desempenho (G2)
    flexibilidade/  {bruto, consolidado}   — Flexibilidade (G3)
  analise/        Julgamentos GQM e evidências derivadas
```

Documentação pública na GitPage: [Dados](../docs/dados.md).

## Fluxo de rastreabilidade

```text
protocolos  →  dados/<caracteristica>/bruto  →  consolidado  →  analise
                     ↑
              códigos GQM (Fase 2)
```

Cada arquivo bruto segue o padrão de nomes `<métrica>_<cenário>_<execução>` (ver [dados/README.md](dados/README.md)). Arquivos consolidados e de análise citam as fontes brutas.

## Privacidade

| Artefato | Onde fica |
| --- | --- |
| Dados tabulados (CSV) e fichas anonimizadas | Neste repositório, sob `dados/` |
| Códigos de participante (PA01–PA02, PB01–PB03) | Neste repositório |
| Tabela código → pessoa | **Fora do repositório** (pasta privada da equipe) |
| Termos de consentimento assinados | Pasta privada, separados dos dados |
| Gravações de tela/áudio das sessões | Pasta privada; no repo só o índice `gravacoes.csv` |

Decisão alinhada ao Termo de Consentimento Livre e Esclarecido: registros em diretório privado, acesso restrito à professora e à equipe, anonimização antes da apresentação dos resultados, retenção até 14/12/2026.
