# Decisões da Reunião 01 — Avaliação de Qualidade do Anki

**Disciplina:** FGA0315 Qualidade de Software 1 — Profa. Cristiane Ramos
**Equipe:** Betty Snyder (turma T01)
**Data da reunião:** 7 de outubro de 2026, das 10h41 às 11h01, online
**Redator:** Davi Severiano Freitas
**Ata da reunião:** [ata da reunião 01](reuniao-01-ata.md)
**Gravação:** [gravação da reunião 01](https://youtu.be/rpLn9-Eqy-s)

Este documento registra apenas o que foi decidido na reunião 01 e o que foi combinado logo depois, por mensagem à equipe. Os pontos ainda em aberto estão na seção "Pendências".

## 1. Contexto

O projeto avalia a qualidade de produto do Anki ([ankitects/anki](https://github.com/ankitects/anki)) seguindo o processo de avaliação de produto da família SQuaRE. As métricas são definidas pelo método GQM, e a gestão do projeto é acompanhada com métricas do PSM.

| Marco | Data | O que precisa estar pronto |
| --- | --- | --- |
| Ponto de Controle 1 | 19/10/2026 | Fase 1 concluída e Fase 2 iniciada |
| Entrega 1 | 26/10/2026 | GitPage até a Fase 2; artigo v1 (Introdução, Referencial teórico, Metodologia, Fase 1 e Fase 2); tabela de contribuição; release E1 |
| Ponto de Controle 2 | 04/11/2026 | Conforme o cronograma da disciplina |
| Entrega 2 | 18/11/2026 | Fases 3 e 4, ação de melhoria, artigo v2, release E2 |
| Apresentação final | 23/11/2026 | Apresentação do trabalho |

## 2. Decisões de escopo

| Decisão | O que foi decidido | Justificativa |
| --- | --- | --- |
| Características avaliadas | Usabilidade, Eficiência de desempenho e Portabilidade | Definidas pela equipe e acordadas com a professora |
| Versão da norma | ISO/IEC 25010:2011 | A equipe não tem acesso completo à versão de 2023, e os slides da disciplina usam a de 2011 |
| Produto avaliado | Anki Desktop | O repositório oficial cobre só o desktop. AnkiDroid, AnkiWeb e AnkiMobile ficam fora desta fase |
| Plataformas | Windows e macOS | Avaliar o desktop nessas duas plataformas já cobre o escopo viável para a equipe. O Anki Desktop é gratuito nas duas; a versão paga é a de iPhone, que está fora do escopo |
| Versão do Anki | 26.09.3, baixada na página de Releases do repositório (seção Assets) | Todos precisam avaliar a mesma versão para que a Fase 4 seja reproduzível |
| Documento de métricas | Funciona como catálogo de consulta, não como lista final | Ele reúne métricas possíveis; cada dupla escolhe as que vai usar no seu GQM |
| Definição do GQM | Cada dupla define o GQM da sua característica (objetivos, questões e métricas). A forma de construir e consolidar o GQM será definida na reunião de 12/10 (ver Pendências) | Divide o trabalho da Fase 2 pelas características |

## 3. Divisão da equipe

A divisão foi feita por escolha dos integrantes, e não por sorteio. Cada dupla é responsável por uma característica de qualidade, uma categoria do PSM e uma frente de apoio.

| Dupla | Membros | Característica | Categoria PSM | Frente de apoio |
| --- | --- | --- | --- | --- |
| A | Davi Severiano Freitas e Pedro Henrique Freire Rodrigues | Usabilidade | Recursos e Custos | Organização geral: atas, planilha de horas e termo de consentimento |
| B | Karolina Vieira Barbosa e Mateus de Siqueira Silva | Eficiência de desempenho | Desempenho dos Processos | Estrutura do artigo no Overleaf e da GitPage |
| C | Bryan Smith Rodrigues Cavalcante e Dante Fernandes Scarpati | Portabilidade | Calendário e Progresso | Repositório: issues, milestones e releases |

A frente de apoio cuida da estrutura. O conteúdo do artigo, da GitPage e do repositório é produzido por todos.

## 4. Gestão do projeto com PSM

- As três categorias exigidas pelo enunciado (Calendário e Progresso, Recursos e Custos e Desempenho dos Processos) foram distribuídas uma por dupla, conforme a seção 3.
- A professora não dará aula sobre PSM. Cada dupla estuda a sua categoria nos capítulos 1 e 2 do livro de McGarry et al. e no material de estudo compartilhado, e traz uma proposta de medida para a reunião de 12/10.
- As medições, a interpretação e as decisões tomadas a partir delas passam a ser registradas nas atas das reuniões.

## 5. Atividades até a reunião de 12/10

Não haverá contato entre os integrantes até a próxima reunião, então cada dupla chega com a sua parte pronta.

**Dupla A — Davi e Pedro**

- Subir no repositório a ata da reunião 01, com o link da gravação.
- Criar a planilha de horas e o modelo de ata.
- Rascunhar o termo de consentimento e a forma de anonimizar os participantes.
- Estudar Recursos e Custos e trazer a proposta de medida.
- Escrever no Overleaf a justificativa de Usabilidade para a Fase 1.

**Dupla B — Karolina e Mateus**

- Montar o esqueleto do artigo no Overleaf, com o template escolhido (Karolina, até 08/10).
- Montar a estrutura inicial da GitPage.
- Estudar Desempenho dos Processos e trazer a proposta de medida.
- Escrever no Overleaf a justificativa de Eficiência de desempenho para a Fase 1.
- Juntar as partes da Fase 1 escritas pelas duplas no Overleaf, para revisão na reunião.

**Dupla C — Bryan e Dante**

- Criar o repositório, as issues e as milestones "PC1" (19/10) e "Entrega 1" (26/10), até a meia-noite de 07/10.
- Criar as labels e as pastas e registrar a versão do Anki usada (26.09.3).
- Propor o critério de pronto das issues.
- Estudar Calendário e Progresso e trazer a proposta de medida.
- Escrever no Overleaf a justificativa de Portabilidade para a Fase 1.

**Todos**

- Ler o material de estudo do PSM.
- Ler a explicação do GQM enviada à equipe e chegar à reunião com uma ideia de quais subcaracterísticas da sua característica fazem mais sentido avaliar.
- Instalar o Anki 26.09.3 e registrar sistema, arquitetura (x64 ou ARM) e hardware na issue aberta pela Dupla C.
- Registrar as próprias horas na planilha desde a reunião de 07/10.
- Pensar em quem é o requisitante e qual é o propósito da avaliação, para fechar a Fase 1 na reunião.

O texto das duplas no Overleaf deve estar pronto até domingo, 11/10, para que a Dupla B consiga juntar tudo antes da reunião.

## 6. Pendências

| Pendência | Quando será tratada |
| --- | --- |
| Requisitante e propósito da avaliação (necessários para a Fase 1) | Reunião de 12/10 |
| Forma de construir e consolidar o GQM. Proposta: com base no propósito, no requisitante e no ponto de vista definidos em conjunto na Fase 1, cada dupla detalha o objetivo de medição da sua característica, com questões, hipóteses, métricas e níveis de pontuação. A equipe revisa os três em conjunto, identifica métricas compartilhadas e consolida tudo em um único GQM e um único diagrama | Reunião de 12/10 |
| Medidas de PSM de cada categoria (medidas base, indicador e critério de decisão) | Reunião de 12/10, a partir das propostas das duplas |
| Perfil dos participantes, caso a avaliação inclua testes ou entrevistas com usuários | Durante a definição do GQM de Usabilidade |
| Tipo de ação de melhoria da Entrega 2 (protótipo, mudança de código, templates ou processo) | Após a Fase 2 |

## 7. Próxima reunião

**Data:** segunda-feira, 12 de outubro de 2026.

## 8. Uso de IA

O documento de preparação da reunião, a análise do repositório do Anki, o material de estudo do PSM, a ata e este documento foram elaborados com apoio de IA (Claude, da Anthropic), a partir do registro da reunião e dos documentos da disciplina. O conteúdo foi conferido e ajustado pelo redator, e todas as decisões aqui registradas foram tomadas pela equipe.