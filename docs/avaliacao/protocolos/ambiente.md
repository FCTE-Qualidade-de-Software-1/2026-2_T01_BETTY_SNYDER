# Ambiente de avaliação

Página de apoio à [Fase 3](../../fase3.md): hardware e software das máquinas usadas na avaliação do Anki Desktop (Windows, macOS e Ubuntu).

## 1. Objetivo

Registrar as configurações que condicionam os testes de desempenho e de flexibilidade e as sessões de entrevista.

## 2. Configuração das máquinas


| Integrante | Sistema Operacional | Nativo/VM (Virtual Machine) | Processador | Memória RAM | Armazenamento | Placa de Vídeo (GPU) |
|---|---|---|---|---|---|---|
| [Bryan Smith](https://github.com/Bryan70897) | Windows 11 | Nativo | Ryzen 5 5500 | 16 GB | SSD | RTX 3060 12 GB |
| [Dante Fernandes](https://github.com/dantescarpati) | Ubuntu | Nativo | 11th Gen Intel Core i5-1145G7 × 8 | 8 GB | SSD | Integrada |
| [Davi Severiano](https://github.com/Davi-Unb.png) | macOS | Nativo | Apple Silicon M4 | 16 GB | SSD | Integrada |
| [Karolina Vieira]() | Windows 11 | Nativo | Intel Core i7-1165G7 (11ª geração) | 16 GB | SSD | Intel Iris Xe Graphics (Integrada) |
| [Mateus de Siqueira](https://github.com/siqueira-prog) | Ubuntu | Nativo | Intel Core i7-1185G7 (11ª geração) @ 3.00 GHz | 8 GB | SSD | Intel Iris Xe Graphics (Integrada) |
| [Pedro Henrique](https://github.com/Pedro-Henrique3) | Windows 11 | Nativo | 12th Gen Intel Core i5-1235U | 8 GB | SSD | Integrada |


## 3. Máquinas de referência

Definir qual máquina será utilizada como referência para cada sistema operacional e característica avaliada.

| Sistema Operacional | Eficiência de desempenho | Flexibilidade |
|---|---|---|
| Windows | [Karolina Vieira](https://github.com/Karolina91) | [Bryan Smith](https://github.com/Bryan70897) |
| macOS | [Davi Severiano](https://github.com/Davi-Unb.png) | [Davi Severiano](https://github.com/Davi-Unb.png) |
| Ubuntu | [Mateus de Siqueira](https://github.com/siqueira-prog) | [Dante Fernandes](https://github.com/dantescarpati) |

## 4. Versões do software

| Software | Versão / Registro |
|---|---|
| Anki Desktop | 26.09.3 |
| AnkiWeb | Data de acesso registrada em cada ficha de sessão (PB01/PB02/PA01 em 13–14/11/2026) |

## 5. Massa de dados e perfil exigido (F3-C2)

| Frente | Massa de dados | Justificativa | Conhecimento exigido |
| --- | --- | --- | --- |
| Eficiência de desempenho | Coleções sintéticas (ex.: 10k, 50k, 100k cards) geradas com o pacote `anki` | Exercer capacidade e utilização de recursos sob carga próxima a coleções grandes reais; alinhar às métricas de vazão e RAM da [Fase 2](../../fase2.md) | Avaliador com informática intermediária e familiaridade com o coletor em `avaliacao/scripts/` |
| Flexibilidade | Coleção padrão de migração M1/M2 (protocolo) | Medir T<sub>pd</sub> e T<sub>sub</sub> com conteúdo conhecido | Avaliador com informática básica e o roteiro do protocolo |
| Capacidade de interação | Baralhos compartilhados / tarefas do instrumento unificado | Exercícios de reconhecimento e estudo sem depender de coleção do participante | Participante: informática básica; sem exigência de domínio de repetição espaçada (Fase 1). Facilitador: treinado no [Pré-entrevista](pre-entrevista-participante.md) |

## 6. Observações

Diferenças relevantes: notebooks Ubuntu de referência com 8 GB de RAM condicionam a interpretação da faixa de memória em Eficiência de desempenho; o cold start no Windows/macOS medido como *launcher* não é comparável 1:1 ao TTI do Ubuntu (ver [Avaliação de Eficiência de desempenho](../analise/desempenho.md)).