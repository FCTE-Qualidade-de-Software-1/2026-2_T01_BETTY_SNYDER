## Fase 1 — Estabelecer os requisitos de avaliação

### Requisitante
Professora da disciplina de Qualidade de Software.

### Objetivos da avaliação
Indicar pontos para melhoria no produto.

### Uso dos resultados
Os pontos de melhoria identificados serão usados pela professora para avaliar a capacidade da equipe de fundamentar tecnicamente uma avaliação de produto.

Também serão registrados como recomendações priorizadas para dois públicos:

- **Mantenedores do Anki:** podem usar as recomendações para decidir correções.
- **Estudantes:** podem usá-las como orientação de uso.

O ponto de melhoria mais relevante será a base da ação de melhoria da Entrega 2.

### Ponto de vista
Usuário do produto (estudante) — usuário final.

### Partes interessadas

| Parte interessada | Papel | Necessidade | Critério de sucesso | Influência na avaliação |
|---|---|---|---|---|
| Professora da disciplina | Requisitante | Uma avaliação fundamentada e rastreável | Pontos de melhoria justificados por evidências coletadas | Acordou as características avaliadas e define prazos e formato |
| Estudante | Usuário final (operador) | Usar o Anki sozinho, sem lentidão, em qualquer sistema | Concluir as tarefas sem ajuda, sem demora perceptível e sem perder dados | Define o ponto de vista, as tarefas dos testes e os critérios de julgamento |
| Mantenedores do Anki | Desenvolvedores e fornecedores | Problemas descritos de forma reproduzível e priorizada | Cada ponto de melhoria acompanhado de evidência e passos para reproduzir | Limitam o escopo ao que é observável e ao código aberto; o AnkiWeb é de código fechado |
| Equipe avaliadora | Avaliadores | Um escopo viável no prazo | Entregas no prazo, com dados rastreáveis | Define as plataformas disponíveis e a profundidade da avaliação |

### Características do produto

- **Nome do produto:** Anki Desktop e AnkiWeb.
- **Versão do produto:** Anki Desktop 26.09.3; AnkiWeb na versão em produção na data da avaliação, registrando a data de acesso.
- **Avaliação do AnkiWeb:** limitada à criação de conta, ao login e à sincronização com o Anki Desktop.
- **Domínio da aplicação:** educação.
- **Objetivo da avaliação:** indicar pontos para melhoria no produto sob o ponto de vista do usuário final, com relação à Usabilidade, Eficiência de desempenho e Portabilidade.

### Priorização das características

A ênfase de cada característica foi definida pela combinação de dois critérios: o impacto para o estudante e a viabilidade de medição com os recursos e o prazo da equipe. A escolha de Usabilidade foi acordada com a requisitante.

| Característica (ISO/IEC 25010:2011) | Impacto para o estudante | Viabilidade de medição | Ênfase |
|---|---|---|---:|
| Usabilidade | Alto: todo estudante usa a interface sem treinamento | Média: exige testes com participantes | 5 |
| Eficiência de desempenho | Médio: notebooks variados e coleções que crescem | Alta: medições instrumentadas | 3 |
| Portabilidade | Médio: estudantes usam sistemas diferentes e trocam de computador | Alta: instalação e migração controladas | 3 |

As cinco características não escolhidas ficam fora do escopo por acordo com a requisitante.

### Classificação e tipo do produto

- **Classificação do produto (Pressman):** software de computador pessoal.
- **Tipo (IEEE 1062):** COTS, gratuito e de código aberto.
- **Observação:** o AnkiWeb é um serviço gratuito de código fechado.

### Principais usuários
Estudantes universitários e autodidatas.

### Conhecimento exigido
- **Informática:** básico.
- **Domínio:** nenhum; não é preciso conhecer repetição espaçada antes de usar.

### Componentes avaliados

- Instalação e desinstalação do Anki Desktop (Portabilidade).
- Interface do usuário do Anki Desktop (Usabilidade).
- Execução do Anki Desktop em Windows, macOS e Ubuntu (Eficiência de desempenho e Portabilidade).
- Criação de conta no AnkiWeb, login e sincronização entre o Anki Desktop e o AnkiWeb (Usabilidade, Eficiência de desempenho e Portabilidade).

### Descrição geral do produto

#### Funções principais

O Anki possui oito funções principais:

1. Autenticação de usuário: login na conta AnkiWeb para sincronização.
2. Criar deck de cards.
3. Escrever cards.
4. Revisar cards: o estudante avalia a própria resposta e o agendamento define quando o card volta.
5. Buscar e editar cards no navegador de cards.
6. Importar e exportar baralhos e coleções.
7. Sincronizar a coleção com o AnkiWeb.
8. Configurar opções de estudo do baralho.

#### Principais tarefas do produto

- Criar uma conta no site do AnkiWeb.
- Fazer login no Anki Desktop para sincronizar.
- Criar um deck.
- Escrever cada card e sua respectiva resposta.
- Acessar um deck.
- Revisar os cards do dia, avaliando a própria resposta.
- Escolher outro deck para responder.
- Fazer logout.
- Instalar o Anki Desktop.
- Sincronizar a coleção com o AnkiWeb.
- Exportar a coleção e importá-la em outro computador.

#### Funções que merecem maior dedicação durante a avaliação

- Criar deck de cards.
- Escrever cards.
- Revisar cards.
- Login e sincronização.

### Janelas de interação com o usuário

O Anki Desktop possui 16 janelas principais:

- A janela principal, que reúne três telas: lista de baralhos, visão geral do baralho e revisão.
- Adicionar, Navegador de cards, Editar card atual e Estatísticas.
- Opções do baralho, Criar baralho filtrado e Preferências.
- Importar, Exportar e Login de sincronização.
- Gerenciar tipos de nota, Campos, Modelos de card (Cards), Perfis e Complementos.

### Ambiente de uso

- Uso individual, em computador pessoal com Windows, macOS ou Ubuntu.
- O estudo funciona sem internet. A criação de conta, o login e a sincronização exigem conexão.
- O estudante usa o Anki por conta própria, sem treinamento formal e sem suporte técnico.

### Massa de dados para avaliação

Sim, de duas fontes:

- **Coleções sintéticas:** geradas com o pacote `anki`, biblioteca Python do próprio Anki publicada no PyPI. É possível criar coleções de tamanhos controlados, por exemplo, 10 mil, 50 mil e 100 mil cards, iguais em todos os ambientes, para os testes de Eficiência de desempenho e Portabilidade.
- **Baralhos compartilhados no AnkiWeb:** podem ser importados como dados realistas nos testes com usuários de Usabilidade.

### Requisitos de hardware e software

- **Windows:** Windows 10 ou posterior (x64), ou Windows 11 (ARM). O manual de instalação detalha a versão mínima do Windows 10 como a 1703.
- **macOS:** macOS 13 ou posterior, em Apple Silicon ou Intel.
- **Ubuntu:** distribuição Linux de 2022 ou posterior (x64), ou de 2024 ou posterior (ARM). O manual traduz isso em glibc 2.35 ou posterior (x64) e 2.39 ou posterior (ARM). É preciso instalar o pacote `zstd` e executar o script de instalação.
- **AnkiWeb:** navegador atualizado e conexão com a internet.
- **Hardware:** a página de download e o manual não definem memória ou processador mínimos. Os computadores usados pela equipe serão registrados no plano de avaliação.
- **Fontes:** página de download do Anki (`apps.ankiweb.net`) e manual de instalação (`docs.ankiweb.net`), consultados em 14/10/2026.

### Requisitos de avaliação

#### Objetos avaliados
Os componentes listados em "Componentes avaliados": instalação e desinstalação, interface do usuário e execução do Anki Desktop 26.09.3; criação de conta, login e sincronização no AnkiWeb.

#### Abrangência
- Três características da ISO/IEC 25010:2011: Usabilidade, Eficiência de desempenho e Portabilidade. As subcaracterísticas de cada uma serão escolhidas na Fase 2.
- Plataformas: Windows, macOS e Ubuntu.
- No AnkiWeb, apenas criação de conta, login e sincronização.

#### Profundidade
- Avaliação externa, do ponto de vista do estudante, baseada no comportamento observável do produto. Os métodos são testes com usuários, medições instrumentadas de tempo e de uso de recursos e inspeção da interface.
- O código-fonte do Anki Desktop serve apenas como apoio para entender o produto. O AnkiWeb, de código fechado, é avaliado só pelo comportamento.
- Não se trata de certificação nem de laudo de conformidade.

#### Relacionamento com outras avaliações
É uma avaliação independente, sem vínculo com avaliações anteriores do Anki. A documentação oficial (manual e página de download) é usada como referência dos requisitos declarados pelo fabricante. Os pontos de melhoria identificados servem de base para a ação de melhoria da Entrega 2.

#### Restrições
- Prazo até 18/11/2026.
- Seis avaliadores, sem custo de aquisição.
- Apenas computadores pessoais da equipe.
- Participantes de testes somente com consentimento registrado.

#### Fora do escopo
- **AnkiDroid e AnkiMobile:** são produtos e bases de código separados, e o tempo da equipe não cobre mais plataformas.
- **Algoritmo de agendamento:** sua eficácia para a memorização exigiria acompanhar usuários por semanas e não corresponde às características escolhidas.
- **Demais funções do AnkiWeb:** como estudo pelo navegador e baralhos compartilhados, não fazem parte do fluxo de sincronização definido.
- As cinco características não escolhidas ficam fora do escopo por acordo com a requisitante.

---

## Relação com os Objetivos de Desenvolvimento Sustentável

A avaliação se relaciona ao **ODS 4 — Educação de Qualidade**.

- **Meta 4.3:** assegurar acesso igualitário à educação superior de qualidade, a preços acessíveis. O Anki Desktop é gratuito e apoia o estudo autônomo de estudantes de graduação.
- **Meta 4.4:** aumentar o número de jovens e adultos com habilidades relevantes. O indicador 4.4.1, sobre habilidades em tecnologias da informação e comunicação, se relaciona à facilidade de aprendizado avaliada em Usabilidade.
- **Meta 4.5:** eliminar disparidades e garantir acesso a pessoas em situação de vulnerabilidade, incluindo pessoas com deficiência. Relaciona-se à Portabilidade, que busca garantir o funcionamento em diferentes sistemas e computadores, e aos aspectos de inclusão da interface.

Pontos de melhoria que reduzem barreiras de uso ampliam o alcance de uma ferramenta gratuita de estudo, o que contribui para essas metas.