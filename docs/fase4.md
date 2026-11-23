# Fase 4: Executar a avaliação e julgar

Esta página documenta a execução da avaliação do Anki Desktop 26.09.3 e do fluxo de conta, login e sincronização do AnkiWeb. Em sequência: a visão geral (organização dos dados e estado da coleta); o julgamento perante o propósito da [Fase 1](fase1.md); as relações entre características; as sugestões priorizadas; e a ação de melhoria. O detalhamento por característica (coleta, resultados e análise) está nas páginas [Avaliação de Capacidade de interação](avaliacao/analise/interacao.md), [Avaliação de desempenho (Triangulação)](avaliacao/analise/desempenho.md) e [Avaliação de Flexibilidade](avaliacao/analise/flexibilidade.md).

## Visão geral

A Visão geral reúne apenas informações transversais: onde os dados ficam no repositório e qual é o estado objetivo de cada frente de coleta. Os números por métrica, as faixas e o julgamento por questão aparecem somente nas páginas de avaliação de cada característica.

### Organização dos dados { #organizacao-dos-dados }

Os arquivos da avaliação do **produto** (o Anki) ficam em [`avaliacao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao). Essa pasta é distinta de [`gestao-psm/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/gestao-psm), que registra esforço, prazos e processos da **equipe** no projeto acadêmico. Misturar as duas fontes invalida a interpretação: um CSV em `avaliacao/` responde a uma métrica GQM do Anki; um CSV em `gestao-psm/` responde a um indicador PSM do trabalho da equipe.

Na prática, a pasta `avaliacao/` separa quatro papéis que se leem em cadeia:

1. **Protocolos** (`protocolos/`): o roteiro escrito de como coletar (entrevista, instrumentação, instalação, checklist, migração).
2. **Scripts** (`scripts/`): programas que geram ou consolidam medidas de desempenho e utilitários de verificação.
3. **Dados** (`dados/<frente>/{bruto,consolidado}/`): o registro bruto da sessão ou do ensaio e a tabela já calculada para publicação.
4. **Análise** (`analise/` e esta Fase 4): a interpretação frente às questões, hipóteses e faixas da Fase 2.

```text
avaliacao/
  protocolos/     Como conduzir entrevistas e ensaios
  scripts/        Programas de coleta e consolidação
  dados/
    interacao/      {bruto, consolidado}  Capacidade de interação
    desempenho/     {bruto, consolidado}  Eficiência de desempenho
    flexibilidade/  {bruto, consolidado}  Flexibilidade
  analise/        Interpretação das métricas frente ao GQM
```

**Rastreabilidade útil no dia a dia.** Para conferir um número da GitPage ou do artigo, percorra: protocolo > dado bruto > consolidado > análise nesta Fase 4. Os nomes preferenciais dos arquivos brutos seguem `<métrica>_<cenário>_<execução>` (exemplo: `T_ini_coldstart_ubuntu_01.csv`). A exceção deliberada é `sessoes.csv`, que indexa entrevistas (data, formato e ata) sem apontar mídia.

| Frente | O que procurar no bruto | Onde ler o consolidado e a avaliação |
| --- | --- | --- |
| Capacidade de interação | [`M-INT-01_reconhecimento.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/M-INT-01_reconhecimento.csv), [`M-INT_tarefas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/M-INT_tarefas.csv), [`Entrevistas/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/interacao/bruto/Entrevistas), [`sessoes.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/bruto/sessoes.csv) | [`M-INT_metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/blob/main/avaliacao/dados/interacao/consolidado/M-INT_metricas.csv); [Avaliação de Capacidade de interação](avaliacao/analise/interacao.md) |
| Eficiência de desempenho | CSV e gráficos em `docs/avaliacao/dados/desempenho/` (espelho usado na GitPage); canônico previsto em `avaliacao/dados/desempenho/` | [Avaliação de desempenho (Triangulação)](avaliacao/analise/desempenho.md) |
| Flexibilidade | Consolidados em [`flexibilidade/consolidado/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_BETTY_SNYDER/tree/main/avaliacao/dados/flexibilidade/consolidado) (instalação, checklist e migração) | [Avaliação de Flexibilidade](avaliacao/analise/flexibilidade.md) |

**Participantes e privacidade.** Códigos públicos: PA01 (Grupo A, iniciante); PB01, PB02 (piloto) e PB03 (Grupo B, frequentes). A tabela código > pessoa e os termos de consentimento ficam fora do repositório. Gravações de tela e áudio não são versionadas; a evidência pública da sessão são as atas, as fichas anonimizadas e `sessoes.csv`.

### Visão geral da coleta { #visao-geral-da-coleta }

A coleta da Fase 4 materializa o plano da [Fase 3](fase3.md) em três frentes. O quadro abaixo indica apenas o método, o responsável e se a frente está concluída no repositório. Métricas, faixas e julgamento ficam nas páginas de avaliação.

| Frente | Método e responsável | Estado da coleta | Onde aprofundar |
| --- | --- | --- | --- |
| Capacidade de interação | Entrevistas observadas (Dupla A), com TCLE (Termo de Consentimento Livre e Esclarecido) | Quatro sessões publicadas (PA01, PB01, PB02 piloto, PB03); consolidado `M-INT_metricas.csv` disponível | [Avaliação de Capacidade de interação](avaliacao/analise/interacao.md) |
| Eficiência de desempenho | Instrumentação multiplataforma (Dupla B) | Ensaios em Ubuntu, Windows 11 e macOS publicados; ressalvas de plataforma documentadas | [Avaliação de desempenho (Triangulação)](avaliacao/analise/desempenho.md) |
| Flexibilidade | Ensaios de laboratório (Dupla C): instalação, checklist e migração | Consolidados de instalação, checklist e migração M1/M2 publicados | [Avaliação de Flexibilidade](avaliacao/analise/flexibilidade.md) |

---

## Julgamento e coerência com a Fase 1 { #julgamento-e-coerencia }

O [propósito da avaliação](fase1.md#proposito-da-avaliacao-e-uso-pretendido) é **indicar pontos de melhoria** no Anki, sob o ponto de vista do estudante, para a requisitante (professora), com recomendações priorizadas para mantenedores e estudantes.

| Expectativa da Fase 1 | Resultado da Fase 4 | Atende? |
| --- | --- | --- |
| Identificar barreiras de uso na interface (ênfase 5) | Q1 de Capacidade de interação não atendida (T<sub>rf</sub> do iniciante 16,7%); Q2 e Q3 atendidas no escopo amostral | Sim, com limitação de n = 4 (1 iniciante) |
| Informar comportamento de desempenho em estudo prolongado | Cold start e vazão excelentes; RAM na faixa insatisfatório em Unix; Windows parcial | Parcial |
| Informar instalabilidade e migração entre SO | Instalação, checklist e migração publicados; T<sub>sub</sub> na faixa mínimo | Sim, com ressalva de tempo de migração acima de 1 min |
| Fundamentar uma ação de melhoria | Protótipo de alta fidelidade para “Criar baralho” | Sim |

O julgamento cumpre o uso pretendido na característica priorizada (Capacidade de interação), cobre instalabilidade, adaptabilidade e migração com dados de laboratório, e deixa explícitas a faixa mínimo de T<sub>sub</sub> e a incompletude de desempenho no Windows.

## Relações entre características { #relacoes-entre-caracteristicas }

- **Capacidade de interação × Eficiência de desempenho.** Falhas de reconhecibilidade (T<sub>rf</sub> de PA01 = 16,7%; R1 falhou) elevam o esforço cognitivo na primeira sessão, mesmo com cold start e vazão de banco na faixa excelente. Evidência: [interacao.md](avaliacao/analise/interacao.md) e [desempenho.md](avaliacao/analise/desempenho.md).
- **Eficiência de desempenho × uso em notebook.** RAM em repouso na faixa insatisfatório (≈ 780–950 MB em Ubuntu e macOS) e picos de 1,33–1,51 GB sob 100k cards podem afetar a fluidez percebida em máquinas de 8 GB (perfil Ubuntu da avaliação). Limitação: RAM do Windows ainda incompleta (só processo pai).
- **Flexibilidade × Capacidade de interação.** Com T<sub>inst_t</sub> excelente ou alvo e N<sub>int</sub> = 0 nos três sistemas, a barreira de primeiro uso observada nas entrevistas concentra-se na interface (vocabulário e “Criar baralho”), não no tempo de instalação em laboratório. A migração preserva 100% dos dados, mas leva em média 2,51 min (faixa mínimo), o que ainda pode somar esforço no primeiro uso ao trocar de máquina. Evidência: [flexibilidade.md](avaliacao/analise/flexibilidade.md).

Onde os dados não permitem relação: afirmação causal entre o tempo de migração M1/M2 e T<sub>exec</sub> das sessões de entrevista (amostras e contextos distintos).

## Sugestões priorizadas { #sugestoes-priorizadas }

| Prioridade | Sugestão (ação concreta) | Base |
| --- | --- | --- |
| 1 | Destacar **Criar baralho** na tela inicial (lista de baralhos como home) | T<sub>rf</sub> R1; PA01 e PB02 |
| 2 | Incluir glossário ou tooltips para nota, tipo de nota e cartão | Q1; respostas da Etapa 5 |
| 3 | Revisar footprint de memória do QtWebEngine sob coleções grandes | RAM na faixa insatisfatório (Ubuntu 1,33 GB; macOS 1,51 GB com 100k cards) |
| 4 | Reduzir o tempo de migração (T<sub>sub</sub> hoje ≈ 2,5 min) e fechar itens “refazer” no Windows | Q3 na faixa mínimo; desempenho parcial no Windows |

## Ação de melhoria { #acao-de-melhoria }

**Problema.** “Criar baralho” não é reconhecido de imediato (T<sub>rf</sub> do iniciante 16,7%; PB02 só após três tentativas).

**Justificativa.** Prioridade 1 da tabela acima; ênfase 5 da Fase 1; evidência direta de Q1/H1.

**Ação.** Protótipo de alta fidelidade com a lista de baralhos como tela inicial e destaque para **Criar Baralho**, além de tutorial introdutório guiado. Artefato: [Protótipo da ação de melhoria](prototipo-acao-melhoria.md) ([abrir interativo](prototipo-interativo/index.html)).

**Validação.** Sessão de verificação com PA01 no protótipo: R1 correto na 1ª tentativa, funções principais 3/3, conceitos 3/3 e tempo até **Criar baralho** de 5 s (critério ≤ 10 s). Ata: [sessao-PA01-verificacao-prototipo_2026-11-22.md](avaliacao/atas/sessao-PA01-verificacao-prototipo_2026-11-22.md).

**O que a ação não cobre.** Não reduz T<sub>sub</sub> da migração (Q3 de Flexibilidade) nem fecha as medições de desempenho no Windows.
