# 2. Calendário e progresso

**Categoria de informação:** Calendário e progresso  
**Conceito mensurável:** Progresso da unidade de trabalho  
**Responsável na Entrega 1:** Dupla C  

Esta página especifica o *measurement construct* da categoria Calendário e progresso, conforme o modelo de informação do PSM (RAMOS, 2026), o mapeamento estrutural da equipe e as especificações CID de *Committed vs Completed*, fluxo cumulativo, *Cycle Time* / *Lead Time* e vazão (JONES et al., 2021a; JONES et al., 2021b).

Na Entrega 1, a medida operacional central foi o **Índice de Conformidade de Prazos (ICP)**. Após o Ponto de Controle 1, as tarefas do CSV foram materializadas em 46 issues. Em 04/11/2026, as 46 Issues estavam vinculadas ao Project `BETTY SNYDER` (#40), conforme o provisionamento descrito em [Organização no GitHub](github-organizacao.md). Data fim planejada e Data fim real sustentam o ICP; as transições de Status registram início e conclusão reais para medidas de fluxo como *Cycle Time* e *Throughput*.

## Necessidade 1: Entrega conforme o compromisso e risco de atraso

**Necessidade de informação.** As histórias, funcionalidades ou capacidades estão sendo entregues conforme o compromisso estabelecido? Quais itens correm o risco de não serem concluídos dentro do cronograma?

A necessidade exige quantificar o compromisso com prazo, a conclusão tempestiva e o residual em atraso, como análise de desempenho do calendário do projeto.

### Instância do modelo de informação

A Figura 1 particulariza o modelo genérico da Aula 09 para o construto de conformidade de prazos e de percentual de conclusão.

```mermaid
flowchart BT
  need["Necessidades de Informação: entrega conforme compromisso e risco de atraso"]
  info["Informação: decisão de redistribuir tarefas"]
  ind["Indicador: conformidade de prazos e risco de atraso"]
  analise["Modelo de Análise: comparar ICP ao limiar por corte"]
  crit["Critérios: ICP menor que 70% implica redistribuição"]
  md1["Medida Derivada: ICP"]
  md2["Medida Derivada: percentual concluído"]
  func["Função de Medição: razões Tc/Tp e concluídos/comprometidos"]
  mb1["Medida Básica: tarefas com prazo Tp"]
  mb2["Medida Básica: tarefas concluídas no prazo Tc"]
  met1["Método de medição: contar itens com prazo no corte"]
  met2["Método de Medição: contar concluídas no prazo"]
  attr1["Atributo: prazo da tarefa"]
  attr2["Atributo: conclusão no prazo"]
  ent["Entidades: tarefa e issue com prazo"]
  ent --> attr1
  ent --> attr2
  attr1 --> met1
  attr2 --> met2
  met1 --> mb1
  met2 --> mb2
  mb1 --> func
  mb2 --> func
  func --> md1
  func --> md2
  md1 --> analise
  md2 --> analise
  crit --> analise
  analise --> ind
  ind --> info
  info --> need
```

*Figura 1. Instância do Modelo de Informação do PSM para Calendário e progresso: compromisso e conformidade de prazos (estrutura conforme RAMOS, 2026).*

### Medidas básicas

#### Tarefas com prazo (\(T_p\)) e concluídas no prazo (\(T_c\))

| Elemento | Descrição |
|---|---|
| Definição | \(T_p\): quantidade de itens com prazo até a data do corte. \(T_c\): quantidade desses itens com `concluida_no_prazo = sim`. |
| Escala | Inteiro ≥ 0. |
| Coleta | [`gestao-psm/calendario-progresso.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/gestao-psm/calendario-progresso.csv) (e cópia `2026-10-25_calendario-progresso.csv`). Campos: `data_corte`, `tarefa_id`, `prazo`, `status`, `concluida_no_prazo`, `evidencia_planilha_ou_ata`, `fonte_planejamento`. |
| Cálculo | Filtrar pelo `data_corte`; contar \(T_p\) e \(T_c\). |
| Análise | Base do ICP; identificação de itens em risco (`status` pendente/parcial ou `concluida_no_prazo = nao`). |
| Observação metodológica | Na E1 a consolidação foi retrospectiva (atas e planilha). Após 25/10, as issues e o Project passam a ser fonte viva; o CSV permanece a série histórica dos cortes documentados. |

#### Work items comprometidos e concluídos (iteração e release)

| Elemento | Descrição |
|---|---|
| Definição | Contagens inteiras de itens comprometidos e concluídos por iteração e por release, conforme o CID (JONES et al., 2021a; JONES et al., 2021b). |
| Status | Parcial. |
| Situação | Cortes por `data_corte` aproximam iterações semanais; milestones `PC1`, `F1`, `F2` e `E2` aproximam releases. O campo `status` permite contar concluídos; não há, ainda, story points nem campos distintos *committed each iteration* versus *committed each release*. |
| Encaminhamento | Marcar explicitamente o conjunto comprometido de cada corte; contar concluídos por milestone. |

### Medidas derivadas

#### Índice de Conformidade de Prazos (ICP)

\[
\mathrm{ICP} = \frac{T_c}{T_p} \times 100
\]

em que:

- \(T_c\): número de tarefas concluídas no prazo até a data do corte;
- \(T_p\): número de tarefas com prazo definido até a data do corte.

| Elemento | Descrição |
|---|---|
| Status | Aplicada. |
| Resultados | 11/10: 56,3% (\(T_c/T_p = 9/16\)); 18/10: 21,4% (\(3/14\)); 19/10 (PC1): 100% (\(1/1\)); 25/10: 40,0% (\(6/15\)). |
| Critério | ICP inferior a 70% associado às ações C2 e C4 da Retrospectiva E1. |

#### Percentual de work items concluídos

\[
\text{Percentual concluído} = \frac{\sum \text{itens concluídos}}{\sum \text{itens comprometidos}} \times 100
\]

em que:

- \(\sum \text{itens concluídos}\): quantidade de *work items* concluídos no recorte;
- \(\sum \text{itens comprometidos}\): quantidade de *work items* assumidos como compromisso no mesmo recorte.

| Elemento | Descrição |
|---|---|
| Status | Parcial. |
| Distinção em relação ao ICP | O percentual concluído responde “quanto do comprometido foi entregue”; o ICP responde “quanto foi entregue no prazo”. A série E1 privilegia o ICP. |

### Indicadores e decisões

| Corte | Indicador | Decisão |
|---|---|---|
| 11/10 | ICP 56,3% (9/16) | Redistribuir |
| 18/10 | ICP 21,4% (3/14) | Redistribuir |
| 19/10 (PC1) | ICP 100% (1/1) | Apresentação realizada; amostra de um item |
| 25/10 | ICP 40,0% (6/15) | Redistribuir 9 restantes |

### Gráfico: conformidade de prazos por recorte { #grafico-icp }

<figure class="psm-chart">
<svg viewBox="0 0 760 380" role="img" aria-labelledby="calendario-chart-title calendario-chart-desc">
  <title id="calendario-chart-title">Índice de Conformidade de Prazos por recorte</title>
  <desc id="calendario-chart-desc">Gráfico de linha do ICP: 56,3 por cento em 11 de outubro (9 de 16), 21,4 por cento em 18 de outubro (3 de 14), 100 por cento no Ponto de Controle 1 em 19 de outubro (1 de 1) e 40 por cento em 25 de outubro (6 de 15). A linha tracejada indica o critério de 70 por cento.</desc>
  <g class="chart-grid">
    <line x1="90" y1="295" x2="710" y2="295" />
    <line x1="90" y1="238.75" x2="710" y2="238.75" />
    <line x1="90" y1="182.5" x2="710" y2="182.5" />
    <line x1="90" y1="126.25" x2="710" y2="126.25" />
    <line x1="90" y1="70" x2="710" y2="70" />
  </g>
  <g class="chart-axis">
    <line x1="90" y1="70" x2="90" y2="295" />
    <line x1="90" y1="295" x2="710" y2="295" />
  </g>
  <line class="threshold" x1="90" y1="137.5" x2="710" y2="137.5" />
  <g text-anchor="end">
    <text x="80" y="299">0%</text>
    <text x="80" y="243">25%</text>
    <text x="80" y="187">50%</text>
    <text x="80" y="131">75%</text>
    <text x="80" y="74">100%</text>
  </g>
  <text x="19" y="195" transform="rotate(-90 19 195)">ICP</text>
  <path class="line-icp" d="M 155 168.3 L 320 246.85 L 485 70 L 650 205" />
  <g>
    <circle class="point-icp" cx="155" cy="168.3" r="6" />
    <circle class="point-icp" cx="320" cy="246.85" r="6" />
    <circle class="point-icp" cx="485" cy="70" r="6" />
    <circle class="point-icp" cx="650" cy="205" r="6" />
  </g>
  <g class="chart-value" text-anchor="middle">
    <text x="155" y="151">56,3% (9/16)</text>
    <text x="320" y="229">21,4% (3/14)</text>
    <text x="485" y="51">100% (1/1)</text>
    <text x="650" y="187">40% (6/15)</text>
  </g>
  <g text-anchor="middle">
    <text x="155" y="321">11/10</text>
    <text x="320" y="321">18/10</text>
    <text x="485" y="321">19/10 · PC1</text>
    <text x="650" y="321">25/10</text>
  </g>
  <line class="threshold" x1="430" y1="357" x2="470" y2="357" />
  <text x="480" y="362">Critério: 70%</text>
</svg>
<figcaption>Valores calculados por recorte a partir de <code>gestao-psm/calendario-progresso.csv</code>. Cada fração mostra tarefas concluídas no prazo / tarefas com prazo no recorte. O resultado de 19/10 corresponde a um único item do PC1 e não deve ser comparado sem considerar o tamanho da amostra.</figcaption>
</figure>

## Necessidade 2: Fluxo, vazão e filas

**Necessidades de informação.**

1. O fluxo de trabalho avança ao longo da cadeia de valor?
2. A vazão (*throughput*) é previsível?
3. Existem filas ou atrasos que impedem otimizar a vazão?

### Instância do modelo de informação

A Figura 2 aplica a mesma topologia do modelo da Aula 09 aos atributos de estado de fluxo. Os estados adotados são A Fazer (*To Do*), Em Andamento (*In Progress*) e Concluído (*Done*); Implantado (*Deployed*) permanece fora de escopo, conforme o mapeamento.

```mermaid
flowchart BT
  need["Necessidades de Informação: fluxo, vazão e filas"]
  info["Informação: redistribuir trabalho ou reduzir WIP"]
  ind["Indicador: previsibilidade de entrega e saturação do fluxo"]
  analise["Modelo de Análise: vazão observada versus vazão do marco"]
  crit["Critérios: vazão necessária ao marco; limite de WIP"]
  md1["Medida Derivada: throughput e cycle time"]
  md2["Medida Derivada: WIP médio"]
  func["Função de Medição: médias temporais por estado"]
  mb1["Medida Básica: contagem em A Fazer e Em Andamento"]
  mb2["Medida Básica: contagem em Concluído"]
  met1["Método de medição: contar por Status do Project"]
  met2["Método de Medição: registrar datas de transição"]
  attr1["Atributo: estado de fluxo"]
  attr2["Atributo: data de entrada e saída de estado"]
  ent["Entidades: item de trabalho no Project"]
  ent --> attr1
  ent --> attr2
  attr1 --> met1
  attr2 --> met2
  met1 --> mb1
  met2 --> mb2
  mb1 --> func
  mb2 --> func
  func --> md1
  func --> md2
  md1 --> analise
  md2 --> analise
  crit --> analise
  analise --> ind
  ind --> info
  info --> need
```

*Figura 2. Instância do Modelo de Informação do PSM para fluxo, vazão e filas (estrutura conforme RAMOS, 2026).*

### Medidas derivadas de fluxo

| Medida | Definição | Situação |
|---|---|---|
| Contagem por estado | Número de itens em A Fazer, Em Andamento e Concluído | Habilitada pelo Status do Project; série E1 ainda baseada no CSV |
| Tempo de ciclo médio aproximado | Duração média do conjunto de itens concluídos no período | Coleta via Planned/Actual e histórico de Status |
| Vazão (*Throughput*) | Média de itens concluídos por unidade de tempo | Idem |
| Trabalho em andamento (WIP) | Média de itens Em Andamento por unidade de tempo | Idem |

**Procedimento de coleta, cálculo e análise.** Em cada corte semanal: (1) contar itens por estado no Project; (2) calcular *Throughput*, WIP médio e *Cycle Time* aproximado, ou aplicar a especificação individual de *Cycle Time* / *Lead Time* do CID quando houver durações por item (JONES et al., 2021b); (3) interpretar acúmulo em A Fazer ou Em Andamento como fila e confrontar a vazão com a demanda do marco (F2, E2).

Na Entrega 1, a necessidade de fluxo foi atendida de forma indireta (ICP e lista de pendências). Com o Project constituído, os cortes seguintes combinam ICP com contagens por estado, *Throughput*, WIP e *Cycle Time*.

## Fontes no repositório

| Artefato | Papel |
|---|---|
| `gestao-psm/calendario-progresso.csv` | Série histórica dos cortes ICP |
| Issues e milestones | Materialização pós-PC1 das tarefas |
| [Organização no GitHub](github-organizacao.md) | Project, labels e vínculos CSV → issues |
| [Retrospectiva E1](../retrospectiva-e1.md) | Limiar ICP inferior a 70%; ação C4 |

## Referências

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 1: concepts, definitions, principles, and measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021a. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 2: measurement specifications and enterprise measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021b. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

RAMOS, Cristiane Soares. **Medição prática de software e sistemas**: PSM: Practical Software and System Measurement. Notas de aula. Brasília: Faculdade do Gama, Universidade de Brasília, 2026. Material didático da disciplina Qualidade de Software 1 (FGA0315).

Voltar à [visão geral do PSM](../gestao-psm.md).
