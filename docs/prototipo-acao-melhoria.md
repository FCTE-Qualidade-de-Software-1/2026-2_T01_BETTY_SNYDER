# Protótipo da ação de melhoria

Este protótipo de alta fidelidade (representação visual e interativa próxima do produto final) materializa a ação de melhoria da [Fase 4](fase4.md): ao abrir o Anki, a tela inicial já apresenta a lista de baralhos, com destaque para **Criar Baralho**, em vez da tela intermediária de Início. A verificação com o participante PA01 está documentada na ata de [22/11/2026](avaliacao/atas/sessao-PA01-verificacao-prototipo_2026-11-22.md).

## Objetivo

Reduzir a dificuldade de reconhecimento da ação de criar um baralho (problema observado nas entrevistas de Capacidade de interação) e encurtar o tempo necessário para compreender onde estudar e qual ação tomar em seguida.

## Como usar

1. Abra o [protótipo interativo](prototipo-interativo/index.html) em uma nova aba.
2. Siga o tutorial guiado (ou reabra-o pelo menu **Ajuda**).
3. Experimente **Criar Baralho**, **Adicionar**, opções do baralho e os controles de janela no padrão do Windows.

<iframe
  src="../prototipo-interativo/index.html"
  title="Protótipo interativo da ação de melhoria do Anki"
  style="width:100%;height:720px;border:1px solid #444;border-radius:8px;background:#1a1a1a;"
></iframe>

<p><a class="md-button md-button--primary" href="../prototipo-interativo/index.html" target="_blank" rel="noopener">Abrir protótipo em tela cheia</a></p>

## Pontos modificados e motivos

Cada alteração abaixo compara o comportamento do Anki Desktop 26.09.3 (linha de base das entrevistas) com o que o protótipo demonstra. Os motivos ligam a evidência da [Avaliação de Capacidade de interação](avaliacao/analise/interacao.md) às sugestões priorizadas da [Fase 4](fase4.md#sugestoes-priorizadas).

### 1. Lista de baralhos como tela inicial

**O que mudou.** No Anki atual, o primeiro contato costuma passar por uma tela intermediária de Início antes de a pessoa ver a lista de baralhos. No protótipo, a abertura já mostra a tabela de baralhos (nome, Novos, A aprender, A revisar) e o rodapé com as ações principais.

**Motivo.** Na sessão original de PA01 (14/11/2026), o item R1 (apontar onde criar um baralho) falhou: o participante indicou “Baralhos” em vez de **Criar baralho**. PB02 também descreveu a ação como pouco intuitiva. A sugestão de prioridade 1 da Fase 4 é tornar a lista de baralhos a home, para que o objeto de estudo e a ação de criação fiquem visíveis sem passos extras.

### 2. Destaque visual e posição de Criar Baralho

**O que mudou.** O botão **Criar Baralho** permanece no rodapé, ao lado de **Obter compartilhados** e **Importar arquivo**, com ênfase visual no fluxo guiado (o tutorial ilumina esse controle) e com acesso imediato a partir da home.

**Motivo.** A métrica T<sub>rf</sub> (taxa de reconhecimento de funções) de PA01 ficou em 16,7%, abaixo do alvo de 75%. O tempo até localizar **Criar baralho** na linha de base foi de 20,71 s. A ação de melhoria busca que o iniciante encontre o controle na primeira tentativa e em no máximo 10 s, sem ajuda do facilitador.

### 3. Tutorial introdutório guiado

**O que mudou.** Na primeira abertura (e sempre que a pessoa reabre por **Ajuda**), um tutorial em passos explica baralho, contagens do dia, **Criar Baralho**, opções do baralho, fluxo de estudo e caminhos para obter conteúdo. O destaque (spotlight) aponta o elemento correspondente na interface.

**Motivo.** PB01 pediu tutorial prático; PB03 pediu interface e termos menos técnicos. O roteiro de aprendizagem (Q2) já saiu excelente em PA01, mas a reconhecibilidade (Q1) não. O tutorial reforça o vocabulário e a localização das ações sem substituir a medição espontânea da Etapa 1 na verificação.

### 4. Vocabulário alinhado a “cartão”

**O que mudou.** Menus e diálogos do protótipo privilegiam o termo **cartão** (por exemplo, opções de estudo e o diálogo **Escolher Tipo de Cartão**), em vez de insistir em “nota” / “tipo de nota” como rótulo principal para quem começa.

**Motivo.** PB01 confundiu “nota” com “cartão”; PB03 também apontou confusão em “nota”. A sugestão de prioridade 2 da Fase 4 pede glossário ou tooltips para esses conceitos. O protótipo aplica a parte lexical no fluxo de Adicionar e no estudo, para que a linguagem bata com o que o estudante espera ver.

### 5. Fluxo de estudo a partir do baralho

**O que mudou.** Ao selecionar um baralho na lista, o protótipo abre a tela de estudo (frente, mostrar resposta, avaliação De novo / Difícil / Bom / Fácil), em vez de exigir navegação adicional pela tela intermediária de Início.

**Motivo.** Nas entrevistas, a dúvida “onde estudar agora?” competia com a dificuldade de achar **Criar baralho**. Ligar o clique no baralho ao estudo deixa explícito o próximo passo e reduz o número de telas a memorizar no primeiro uso.

### 6. Opções do baralho e menus contextuais

**O que mudou.** A engrenagem de cada linha abre um menu (renomear, opções do baralho, exportar, excluir). A tela de opções permite ajustar limites diários (novos cartões e revisões), com controles no padrão visual do restante do protótipo.

**Motivo.** Completar o mapa mental do iniciante: depois de ver a lista e criar um baralho, a pessoa precisa saber onde configurar o ritmo de estudo. Isso apoia as perguntas de conceito (R4 a R6) e a sugestão de tornar a interface mais autoexplicativa, pedida por PA01 na Etapa 5.

### 7. Diálogos Adicionar e Criar Baralho

**O que mudou.** **Adicionar** abre um formulário (frente, verso, etiquetas, tipo e baralho). **Criar Baralho** abre um diálogo para nomear o novo conjunto. Ambos usam a mesma linguagem de janela do aplicativo principal.

**Motivo.** Fechar o ciclo da prioridade 1: não basta destacar o botão; a pessoa precisa concluir a criação sem saltar para um fluxo obscuro. O diálogo curto reduz a chance de abandonar a tarefa no primeiro uso.

### 8. Controles de janela no padrão do Windows

**O que mudou.** Barra de título com minimizar, maximizar ou restaurar e fechar; janelas minimizadas reaparecem em uma barra inferior (taskbar do protótipo). O visual acompanha o ambiente em que PA01 foi avaliado (Windows 11).

**Motivo.** Manter fidelidade ao contexto da entrevista presencial e evitar que controles de janela atípicos contaminem a avaliação da ação de melhoria (a pessoa deve julgar a home e o **Criar Baralho**, não um chrome de sistema estranho).

## Validação com PA01

A Dupla A repetiu a Etapa 1 (reconhecimento R1 a R6) com o **mesmo** participante iniciante, em 22/11/2026, usando o protótipo publicado na GitPage. Os enunciados foram os da sessão original de 14/11/2026. A evidência pública está na ata [sessao-PA01-verificacao-prototipo_2026-11-22.md](avaliacao/atas/sessao-PA01-verificacao-prototipo_2026-11-22.md).

### Critérios de validação

| Critério | Limiar definido na Fase 4 |
| --- | --- |
| Localizar **Criar baralho** (R1) | Acerto na 1ª tentativa, sem ajuda |
| Funções principais (R1 a R3) | Pelo menos 75% de acerto |
| Conceitos (R4 a R6) | Melhor que a linha de base |
| Tempo até **Criar baralho** | Até 10 s |

### Resultados documentados (antes e depois)

| Questão | Antes (PA01, 14/11, Anki 26.09.3) | Depois (PA01, 22/11, protótipo) | Critério atendido |
| --- | --- | --- | --- |
| Acertou onde criar um baralho (R1) | Não | Sim, na 1ª tentativa | Sim |
| Funções principais reconhecidas (R1 a R3) | 1 de 3 | 3 de 3 (100%) | Sim |
| Conceitos explicados (R4 a R6) | 0 de 3 | 3 de 3 | Sim |
| Tempo até clicar em Criar baralho | 20,71 s | 5 s | Sim |

### Interpretação

1. **R1.** PA01 passou de falha (apontou “Baralhos”) para acerto espontâneo na primeira tentativa.
2. **Funções principais.** Passou de 1 acerto em 3 para 3 em 3, acima do limiar de 75%.
3. **Conceitos.** Passou de nenhum acerto para três acertos.
4. **Tempo.** Passou de 20,71 s para 5 s, dentro do critério de até 10 s.

Com os quatro itens atendidos, a validação proposta da ação de melhoria fica **satisfeita** nesta evidência. A comparação usa um participante antes e o mesmo depois; o resultado é indicativo para esse caso e não generaliza para todos os iniciantes.

## Base documental

O tutorial interno do protótipo segue a documentação oficial do Anki:

- [Getting Started](https://docs.ankiweb.net/manual/getting-started)
- [Studying](https://docs.ankiweb.net/manual/studying)

Documentos do projeto relacionados:

- [Fase 4 · Ação de melhoria](fase4.md#acao-de-melhoria)
- [Avaliação de Capacidade de interação](avaliacao/analise/interacao.md)
- Ata original PA01: [sessao-PA01_2026-11-14.md](avaliacao/atas/sessao-PA01_2026-11-14.md)
- Ata de verificação do protótipo: [sessao-PA01-verificacao-prototipo_2026-11-22.md](avaliacao/atas/sessao-PA01-verificacao-prototipo_2026-11-22.md)
