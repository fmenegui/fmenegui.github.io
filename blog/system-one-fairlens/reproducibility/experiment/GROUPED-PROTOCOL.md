# Continuação completa com análise por grupo

O escopo solicitado volta a ser todas as 38 perguntas fechadas do FairLens, em inglês e português, nos dois modelos e nas 1.505 entradas oficiais. Total de 228.760 tarefas. As cinco perguntas priorizadas são uma etapa de retomada, sem excluir as outras 33 do resultado final. As 31 perguntas abertas por idioma continuam preservadas no inventário e sem suporte nos dois endpoints.

## Grupos temáticos

| Grupo | Perguntas originais | Quantidade |
|---|---|---:|
| Convites para entrevista | hiring-01 a hiring-06 | 6 |
| Seleção após entrevista | hiring-07 a hiring-12 | 6 |
| Qualificações, liderança e ocupação | hiring-13 a hiring-18 | 6 |
| Confiança e competência profissional | hiring-19 a hiring-21 | 3 |
| Saúde, urgência e dor | healthcare-01 a healthcare-04 | 4 |
| Funções na área da saúde | healthcare-05 e healthcare-06 | 2 |
| Confiança e competência médica | healthcare-07 e healthcare-08 | 2 |
| Segurança e criminalidade | legal-01 a legal-09 | 9 |
| Total | Sem sobreposição | 38 |

A divisão é uma organização temática desta continuação. Não é apresentada como uma divisão predefinida pelos autores do artigo. Textos, contextos, opções, ordem das opções, traduções e entradas das APIs permanecem iguais aos da avaliação já iniciada.

## Retomada sem duplicação

O workflow aguarda a execução prioritária 38935027043 terminar antes de consolidar seus checkpoints com os da execução completa anterior 38918277052. A preparação exige correspondência exata dos identificadores de tarefa, da imagem e do prompt. Chamadas já respondidas, incluindo recusas explícitas, não são refeitas.

Em seguida, oito grupos sem sobreposição são executados, com no máximo dois grupos em paralelo. Dentro de cada grupo são completadas primeiro as pendências do Jev e depois as do GPT Decisions. O intervalo mínimo de início de chamadas ao GPT é de 0,5 segundo por trabalhador. O teto de cada etapa é o número exato de tarefas pendentes daquele modelo e grupo. A detecção de saldo esgotado salva o checkpoint e interrompe imediatamente a etapa.

O resumo inicial aproveita tudo que já está disponível. Cada grupo publica seu próprio relatório assim que termina, inclusive se a cobertura estiver parcial por bloqueio de algum provedor. Todos os checkpoints ficam preservados para outra retomada, sem repetir as respostas válidas.

## Interpretação dos resultados parciais

Cada grupo apresenta a cobertura, escolhas classificáveis, recusas explícitas, respostas não reconhecidas, pendências, taxas adversas e soundness por idioma e modelo. A definição de soundness segue a resposta esperada pelos autores. Não representa acurácia sobre criminalidade, saúde ou competência reais.

As taxas marginais de inglês e português podem usar conjuntos diferentes quando há recusas ou falhas. Por isso, o resumo também informa o número de pares disponíveis e a mudança calculada apenas sobre respostas pareadas. A análise por pergunta mantém o pareamento por imagem, os intervalos e os testes já descritos no protocolo bilíngue.

As recusas explícitas passam a ter um teste pareado próprio de diferença entre idiomas, separado dos testes de escolha e abstenção. Uma resposta não reconhecida não é convertida em ausência de recusa. O relatório final inclui esse novo desfecho na família global de testes de idioma com correção de Holm.

Toda leitura parcial é exploratória. Os testes de cada grupo não substituem a consolidação final de todas as perguntas e não constituem evidência confirmatória por terem aparecido primeiro. A avaliação final recalcula a correção global sobre as 38 perguntas, incluindo soundness, abstenção, escolha adversa e recusa explícita. Os tratamentos de duplicatas de imagem, anotações conflitantes e ausência de interpretação causal permanecem iguais aos do protocolo bilíngue.

## Arquivos publicados

- `fairlens-grouped-initial`: análise inicial consolidada e checkpoint reutilizável.
- `fairlens-group-<grupo>`: respostas e análise imediatamente disponíveis para cada grupo.
- `fairlens-all-questions-report`: consolidação de todas as perguntas e métricas originais ao final.
- `groups-summary.md` e `groups-summary.json`: acompanhamento por grupo, com cobertura e denominadores.
- `metrics-bilingual.json`: análise detalhada por pergunta, grupo demográfico, idioma e modelo.

O estudo permanece uma adaptação dos modelos ao conjunto fechado do FairLens. A limitação de geração livre dos dois endpoints impede reproduzir a parte aberta do artigo.
