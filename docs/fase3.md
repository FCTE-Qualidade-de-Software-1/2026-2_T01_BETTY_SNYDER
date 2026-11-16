# Fase 3: Protocolos de avaliação

Esta seção documenta o plano de avaliação (Fase 3) do Anki Desktop 26.09.3 e do fluxo de conta, login e sincronização do AnkiWeb. Os procedimentos estão em três frentes que correspondem aos objetivos GQM da [Fase 2](fase2.md) e à árvore de pastas descrita em [Dados](dados.md).

O formulário aplicado em cada sessão com participante é o [Pré-entrevista com participante](avaliacao/protocolos/pre-entrevista-participante.md). As configurações de hardware e software das máquinas de referência estão em [Ambiente](avaliacao/protocolos/ambiente.md).

A Dupla A conduz todas as entrevistas com participantes voluntários e aplica o formulário de pré-entrevista completo. A Dupla B executa os testes instrumentados de eficiência de desempenho. A Dupla C executa os testes de flexibilidade. Quando a pré-entrevista contém blocos elaborados pelas Duplas B ou C, a Dupla A os aplica na sessão, desde que tenham sido preenchidos previamente.

## 1. Método e instruções repetíveis

A execução segue o GQM da Fase 2 e o instrumento unificado, em três frentes:

| Frente | Quem executa | O que cobre | Páginas | Dados |
| --- | --- | --- | --- | --- |
| Entrevista com participante voluntário | Dupla A (todas as sessões) | Termo de consentimento, triagem, etapas de Capacidade de interação, eficiência percebida e campos de Flexibilidade quando preenchidos | [Entrevista](avaliacao/protocolos/entrevista.md), [Pré-entrevista](avaliacao/protocolos/pre-entrevista-participante.md) | Capacidade de interação e evidência qualitativa de Eficiência de desempenho; `avaliacao/dados/interacao/` |
| Testes de desempenho | Dupla B | Condições de controle e cenários instrumentados (inicialização a frio, repouso e estresse, capacidade, threads) | [Eficiência de desempenho](avaliacao/protocolos/desempenho.md) | Eficiência de desempenho; `avaliacao/dados/desempenho/` |
| Testes de flexibilidade | Dupla C, em laboratório nas máquinas de referência | Instalação e desinstalação, checklist de integração e migração da coleção padrão | [Instalação](avaliacao/protocolos/flexibilidade-instalacao.md), [Checklist](avaliacao/protocolos/flexibilidade-checklist.md), [Migração](avaliacao/protocolos/flexibilidade-migracao.md) | Flexibilidade; `avaliacao/dados/flexibilidade/` |

## 2. Recursos e ambiente

- **Software:** Anki Desktop 26.09.3; AnkiWeb na data da sessão; coletores em `avaliacao/scripts/` para Eficiência de desempenho.
- **Hardware e sistemas operacionais:** tabela em [Ambiente](avaliacao/protocolos/ambiente.md) (Windows, macOS e Ubuntu; máquinas de referência por característica).
- **Participantes (plano):** até 2 iniciantes (PA) e até 3 frequentes (PB); triagem conforme [Fase 2](fase2.md).
- **Realizado até a Entrega 2:** PA01 (Grupo A, 14/11/2026), PB01 e PB02 (Grupo B, 13/11/2026). Gravações em `avaliacao/dados/interacao/bruto/gravacoes/`. Ver [análise de Capacidade de interação](avaliacao/analise/interacao.md).

## 3. Cronograma de avaliação

| Atividade | Previsto | Status |
| --- | --- | --- |
| Protocolos e pré-entrevista publicados na GitPage | até 11/11/2026 | Páginas publicadas em `docs/avaliacao/protocolos/` |
| Entrevistas de Capacidade de interação (PB01 e PB02) | 13/11/2026 | Realizado: Grupo B, Etapas 1, 4 e 5; tempos da seção Etapa 2 (PB01) e Etapa 3 (PB02) da ficha contabilizados como Etapa 4 |
| Entrevista de Capacidade de interação (PA01) | 14/11/2026 | Realizado: Grupo A, Etapas 1 a 3 e 5 |
| Coletas de Eficiência de desempenho (Ubuntu, Windows e macOS) | PC2 até Entrega 2 | Publicada a [análise de desempenho](avaliacao/analise/desempenho.md); no PC2 permanecem itens marcados “refazer” e medições incompletas no Windows |
| Coletas de Flexibilidade (instalação, integração e migração) | PC2 até Entrega 2 | Sem CSV completo de Ubuntu e sem gráficos de instalação no repositório |
| Cálculo das métricas a partir dos CSV e redação da análise de Capacidade de interação | 15/11/2026 a 16/11/2026 | `M-INT_metricas.csv` e [análise de Capacidade de interação](avaliacao/analise/interacao.md) publicados |
| Julgamento, sugestões e ação de melhoria | Entrega 2 (18/11/2026) | Ver [Fase 4](fase4.md) |
| Cortes PSM | 08/11/2026 e 15/11/2026 | Atualizar CSV da gestão se necessário |

## Fluxo

```mermaid
flowchart TD
  ambiente["Ambiente"]
  entrevista["Entrevista com participante"]
  desempenho["Testes de desempenho"]
  flexibilidade["Testes de flexibilidade"]
  dadosInt["Dados de interação"]
  dadosDes["Dados de desempenho"]
  dadosFlex["Dados de flexibilidade"]
  ambiente --> entrevista
  ambiente --> desempenho
  ambiente --> flexibilidade
  entrevista --> dadosInt
  desempenho --> dadosDes
  flexibilidade --> dadosFlex
```

## Seções comuns das páginas de procedimento

As páginas de procedimento repetem a mesma sequência de seções, para permitir leitura cruzada entre as frentes:

1. Definições específicas daquela frente (sem repetir o que já consta na Fase 2 ou nesta visão geral)
2. Pré-requisitos e condições de controle
3. Procedimento passo a passo
4. Registro de dados em `avaliacao/dados/...`, com o padrão `<métrica>_<cenário>_<execução>`
5. Critérios de invalidação ou encerramento
6. Relação com o [Pré-entrevista com participante](avaliacao/protocolos/pre-entrevista-participante.md) e com a página [Dados](dados.md)
