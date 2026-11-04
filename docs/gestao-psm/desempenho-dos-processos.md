# 3. Desempenho dos processos

**Categoria de informação:** Desempenho dos processos  
**Conceito mensurável:** Eficácia do processo  
**Responsável na Entrega 1:** Dupla B  

Esta página especifica o *measurement construct* da categoria Desempenho dos processos, conforme o modelo de informação do PSM (RAMOS, 2026) e o mapeamento estrutural da equipe (JONES et al., 2021a).

O mapeamento associa a categoria à necessidade de conhecer o status do marco, o trabalho restante comprometido e as tendências de execução em relação ao plano, com as medidas **Trabalho Planejado**, **Trabalho Concluído** e **Trabalho em Aberto**. Na Entrega 1, a equipe operacionalizou a eficácia do processo documental por meio da **densidade de defeitos em revisão** e da **taxa de correção**, alinháveis às especificações de detecção e resolução de defeitos do CID (JONES et al., 2021b). Os dois eixos são complementares: um trata da qualidade do artefato produzido; o outro, da capacidade de cumprir o plano de escopo.

## Necessidade de informação

**Necessidade de informação.** Qual é o status da iteração, do lançamento ou da capacidade? Todo o trabalho restante assumido como compromisso será concluído conforme o planejado? Quais funcionalidades correm risco de atraso? Quais são as tendências de execução em relação ao plano?

## Eixo A: Eficácia do processo de revisão documental (aplicado na Entrega 1)

### Definição operacional

| Elemento | Definição da equipe |
|---|---|
| Defeito | Informação incorreta ou sem fonte; divergência com decisão da equipe; item exigido pela rubrica que está ausente. Conta apenas o defeito **confirmado** pela equipe (inclusive apontamentos com apoio de IA). |
| Fonte | Revisões do artigo; CSV `gestao-psm/desempenho-processos.csv`. |

### Instância do modelo de informação

A Figura 1 particulariza o modelo genérico da Aula 09 para o construto de defeitos aplicado na Entrega 1. Os rótulos dos nós correspondem à instanciação; a topologia é a do Modelo de Informação do PSM (RAMOS, 2026).

```mermaid
flowchart BT
  need["Necessidades de Informação: eficácia da revisão documental"]
  info["Informação: decisão sobre nova revisão"]
  ind["Indicador: densidade D e taxa de correção"]
  analise["Modelo de Análise: comparar D e correção aos critérios"]
  crit["Critérios: D elevado motiva Revisão 2 com dados reais"]
  md1["Medida Derivada: densidade D"]
  md2["Medida Derivada: taxa de correção"]
  func["Função de Medição: razões entre contagens"]
  mb1["Medida Básica: defeitos confirmados"]
  mb2["Medida Básica: seções revisadas"]
  met1["Método de medição: contar defeitos confirmados"]
  met2["Método de Medição: contar seções revisadas"]
  attr1["Atributo: defeito confirmado"]
  attr2["Atributo: seção revisada"]
  ent["Entidades: revisão do artigo e seções"]
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

*Figura 1. Instância do Modelo de Informação do PSM para densidade de defeitos e taxa de correção (estrutura conforme RAMOS, 2026).*

Para a taxa de correção, a terceira medida básica (defeitos corrigidos) entra na função de medição juntamente com os defeitos confirmados, produzindo a segunda medida derivada do mesmo construto.

### Medidas

\[
D = \frac{N_{\text{defeitos}}}{N_{\text{seções}}}
\]

em que:

- \(D\): densidade de defeitos na revisão;
- \(N_{\text{defeitos}}\): quantidade de defeitos confirmados pela equipe;
- \(N_{\text{seções}}\): quantidade de seções (ou unidades) revisadas.

\[
\text{Taxa de correção} = \frac{N_{\text{corrigidos}}}{N_{\text{confirmados}}}
\]

em que:

- \(N_{\text{corrigidos}}\): quantidade de defeitos confirmados já corrigidos;
- \(N_{\text{confirmados}}\): quantidade de defeitos confirmados na revisão.

| Elemento | Descrição |
|---|---|
| Coleta | Revisão 1: \(D_1 = 1{,}44\); correção 61,5% (resumo na visão geral). Revisão 2: [`gestao-psm/desempenho-processos.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/gestao-psm/desempenho-processos.csv), com campos `identificador`, `revisão`, `seção`, `tipo`, `descrição`, `quem apontou`, `confirmado`, `corrigido`. |
| Análise | Rev. 1 motivou a Revisão 2 com dados reais. A Rev. 2 registrou 10 apontamentos; os 10 foram confirmados e corrigidos. |
| Limitação | A Revisão 1 não possui CSV versionado equivalente; `docs/gestao-psm/defeitos.csv` contém apenas o cabeçalho. |

### Indicadores e decisões

| Corte / revisão | Indicador | Decisão |
|---|---|---|
| Revisão 1 | \(D_1 = 1{,}44\); correção 61,5% | Conduzir Revisão 2 com dados reais |
| Revisão 2 | 10 apontamentos; 10 confirmados e 10 corrigidos | Consolidar correções no artigo e na GitPage |

### Gráfico: taxa de correção por revisão { #grafico-taxa-correcao }

<figure class="psm-chart">
<svg viewBox="0 0 760 380" role="img" aria-labelledby="processos-chart-title processos-chart-desc">
  <title id="processos-chart-title">Taxa de correção dos defeitos confirmados por revisão</title>
  <desc id="processos-chart-desc">A taxa de correção foi de 61,5 por cento na Revisão 1 e de 100 por cento na Revisão 2, na qual 10 de 10 apontamentos foram confirmados e corrigidos.</desc>
  <g class="chart-grid">
    <line x1="100" y1="295" x2="700" y2="295" />
    <line x1="100" y1="238.75" x2="700" y2="238.75" />
    <line x1="100" y1="182.5" x2="700" y2="182.5" />
    <line x1="100" y1="126.25" x2="700" y2="126.25" />
    <line x1="100" y1="70" x2="700" y2="70" />
  </g>
  <g class="chart-axis">
    <line x1="100" y1="70" x2="100" y2="295" />
    <line x1="100" y1="295" x2="700" y2="295" />
  </g>
  <g text-anchor="end">
    <text x="90" y="299">0%</text>
    <text x="90" y="243">25%</text>
    <text x="90" y="187">50%</text>
    <text x="90" y="131">75%</text>
    <text x="90" y="74">100%</text>
  </g>
  <text x="23" y="195" transform="rotate(-90 23 195)">Taxa de correção</text>
  <rect class="bar-rate" x="230" y="156.63" width="100" height="138.37" rx="4" />
  <rect class="bar-rate" x="500" y="70" width="100" height="225" rx="4" />
  <g class="chart-value" text-anchor="middle">
    <text x="280" y="148">61,5%</text>
    <text x="550" y="61">100% (10/10)</text>
  </g>
  <g text-anchor="middle">
    <text x="280" y="321">Revisão 1</text>
    <text x="550" y="321">Revisão 2</text>
  </g>
</svg>
<figcaption>A Revisão 1 é o valor consolidado no resumo histórico; a Revisão 2 é calculada do CSV, com 10 defeitos confirmados e 10 corrigidos. A densidade da Revisão 2 não é comparada porque a quantidade total de seções revisadas não foi registrada.</figcaption>
</figure>

### Gráfico: densidade de defeitos { #grafico-densidade }

<figure class="psm-chart">
<svg viewBox="0 0 760 380" role="img" aria-labelledby="densidade-chart-title densidade-chart-desc">
  <title id="densidade-chart-title">Densidade de defeitos por revisão</title>
  <desc id="densidade-chart-desc">A densidade registrada para a Revisão 1 foi 1,44 defeito por seção. A densidade da Revisão 2 não está disponível, pois não foi registrada a quantidade total de seções revisadas.</desc>
  <g class="chart-grid">
    <line x1="100" y1="295" x2="700" y2="295" />
    <line x1="100" y1="238.75" x2="700" y2="238.75" />
    <line x1="100" y1="182.5" x2="700" y2="182.5" />
    <line x1="100" y1="126.25" x2="700" y2="126.25" />
    <line x1="100" y1="70" x2="700" y2="70" />
  </g>
  <g class="chart-axis">
    <line x1="100" y1="70" x2="100" y2="295" />
    <line x1="100" y1="295" x2="700" y2="295" />
  </g>
  <g text-anchor="end">
    <text x="90" y="299">0</text>
    <text x="90" y="243">0,5</text>
    <text x="90" y="187">1,0</text>
    <text x="90" y="131">1,5</text>
    <text x="90" y="74">2,0</text>
  </g>
  <text x="23" y="195" transform="rotate(-90 23 195)">Defeitos por seção</text>
  <rect class="bar-rate" x="230" y="133" width="100" height="162" rx="4" />
  <g class="chart-value" text-anchor="middle">
    <text x="280" y="124">1,44</text>
    <text x="550" y="160">N/D</text>
  </g>
  <g text-anchor="middle">
    <text x="280" y="321">Revisão 1</text>
    <text x="550" y="321">Revisão 2</text>
  </g>
</svg>
<figcaption>A densidade \(D_1 = 1{,}44\) está documentada para a Revisão 1. Para a Revisão 2, o CSV registra os apontamentos, mas não o total de seções efetivamente revisadas; por isso, o indicador não pode ser calculado sem inventar o denominador.</figcaption>
</figure>

## Eixo B: Trabalho planejado, concluído e em aberto (mapeamento)

### Instância do modelo de informação

A Figura 2 aplica a mesma topologia do modelo da Aula 09 às medidas de trabalho planejado, concluído e em aberto previstas no mapeamento.

```mermaid
flowchart BT
  need["Necessidades de Informação: status do marco e tendência plano x execução"]
  info["Informação: projeção de conclusão do marco"]
  ind["Indicador: trabalho em aberto e tendência"]
  analise["Modelo de Análise: Wa versus vazão e tempo restante"]
  crit["Critérios: Wa compatível com capacidade restante do marco"]
  md1["Medida Derivada: trabalho em aberto Wa"]
  md2["Medida Derivada: razão Wa sobre tempo restante"]
  func["Função de Medição: diferença e razão"]
  mb1["Medida Básica: trabalho planejado Wp"]
  mb2["Medida Básica: trabalho concluído Wc"]
  met1["Método de medição: contar itens comprometidos do marco"]
  met2["Método de Medição: contar itens concluídos"]
  attr1["Atributo: compromisso de escopo"]
  attr2["Atributo: conclusão de item"]
  ent["Entidades: marco, corte e itens de trabalho"]
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

*Figura 2. Instância do Modelo de Informação do PSM para trabalho planejado, concluído e em aberto (estrutura conforme RAMOS, 2026).*

### Medidas

| Medida | Definição | Situação |
|---|---|---|
| Trabalho Planejado \(W_p\) | Quantidade (ou peso) de trabalho comprometido no marco ou corte | Parcial: derivável do CSV de calendário e dos milestones |
| Trabalho Concluído \(W_c\) | Quantidade concluída na mesma unidade | Parcial: `status = concluida` / issues fechadas |
| Trabalho em Aberto \(W_a\) | \(W_a = W_p - W_c\) | Sem série formal publicada nesta categoria |

\[
W_a = W_p - W_c
\]

em que:

- \(W_a\): trabalho em aberto (restante comprometido e ainda não concluído);
- \(W_p\): trabalho planejado (comprometido no marco ou corte);
- \(W_c\): trabalho concluído na mesma unidade e no mesmo recorte.

A análise pretendida confronta a tendência de \(W_a\) com a vazão e o tempo restante do marco. O procedimento mínimo consiste em publicar, em cada corte, a trinca \(W_p\), \(W_c\), \(W_a\) e a projeção de conclusão.

### Distinção em relação a Calendário e progresso

As entidades (itens de trabalho) são compartilhadas. A interpretação difere:

- **Calendário e progresso:** prazo, conformidade (ICP) e fluxo (estados, vazão, WIP).
- **Desempenho dos processos:** eficácia do processo (defeitos; tendência de \(W_a\) frente ao plano).

## Fontes no repositório

| Artefato | Papel |
|---|---|
| `gestao-psm/desempenho-processos.csv` | Defeitos da Revisão 2 |
| `gestao-psm/calendario-progresso.csv` | Proxy para \(W_p\) e \(W_c\) |
| Plano da Fase 2 (pasta `PSM/` do projeto acadêmico) | Definição de defeito e escolha da medida |

## Referências

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 1: concepts, definitions, principles, and measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021a. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

JONES, Cheryl L. et al. (ed.). **Practical software and systems measurement continuous iterative development measurement framework**: part 2: measurement specifications and enterprise measures. Version 2.1. [S. l.]: Practical Software & Systems Measurement; National Defense Industrial Association; International Council on Systems Engineering, 15 abr. 2021b. Product No. PSM-2021-03-001; INCOSE-TP-2020-001-06.

RAMOS, Cristiane Soares. **Medição prática de software e sistemas**: PSM: Practical Software and System Measurement. Notas de aula. Brasília: Faculdade do Gama, Universidade de Brasília, 2026. Material didático da disciplina Qualidade de Software 1 (FGA0315).

Voltar à [visão geral do PSM](../gestao-psm.md).
