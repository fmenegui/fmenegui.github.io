# Revisão do artigo FairLens

O manuscrito em inglês apresenta uma replicação de todas as 38 perguntas fechadas, em inglês e português, com Jev e GPT Decisions. São 228.760 tarefas concluídas. As 31 perguntas abertas não foram executadas, pois os endpoints utilizados não geram texto livre.

## O que está conferido

As respostas brutas reproduzem a normalização e os totais finais. Não há divergências entre respostas terminais duplicadas nos checkpoints. A reanálise offline reproduz todos os intervalos, os 260 testes pareados e os 36 relatórios originais, com tolerância numérica relativa de 1e-12 para diferenças entre bibliotecas. Todos os totais e a estrutura devem coincidir exatamente. Os 39 testes do código passaram. O manuscrito foi renderizado e conferido visualmente em sete páginas.

O texto separa acerto no benchmark, cobertura de respostas classificáveis, recusas e escolhas sem evidência suficiente. Apresenta a inversão do ranking entre média por pergunta e média por domínio. Registra também os 612 vetores Jev cuja soma difere de um e os 11 casos em que a escolha tem probabilidade exibida 0,01 abaixo da maior. Não alteramos respostas para corrigir esses casos.

## Revisão humana ainda necessária

O pacote de tradução contém 69 pares de perguntas, três contextos e dois sufixos. Todos os 74 itens estão pendentes de revisão independente. O formulário registra nome, data, retrotradução, equivalência de significado, contexto, opções, gênero gramatical e adjudicação. Quando possível, revisar sem consultar os resultados dos modelos.

Observações preliminares de IA para a revisão semântica, que não constituem validação humana:

- O contexto de contratação traduz random photo como foto casual. A formulação pode mudar a ênfase de seleção aleatória para apresentação informal.
- Profissões específicas, como Nurse e Doctor, são traduzidas em algumas opções como profissional de enfermagem e profissional de medicina. Avaliar se a extensão das categorias permanece equivalente.
- Há marcação gramatical de gênero em opções como Piloto, Comissário, Professor, Criminoso e Réu. Isso deve entrar na interpretação do contraste entre os prompts completos.
- A hipótese de pessoa qualificada nas perguntas de confiança deve manter o mesmo sentido lógico e pragmático nas duas versões. Discordar da resposta esperada do benchmark também é um julgamento a documentar, não um motivo para reclassificar respostas retrospectivamente.

Preservar o arquivo executado pt-BR-v1. Sugestões devem entrar em uma nova versão e, se mudarem o experimento, exigir nova execução autorizada e orçamento separado. A revisão posterior não torna o desenho original pré-registrado.

Antes de submissão, os autores humanos devem confirmar autoria, afiliações, financiamento, conflitos, interpretação das conclusões e declaração ética aplicável. Antes de distribuição pública, conferir as condições do UTKFace e dos materiais de terceiros. A árvore upstream fixada não contém um arquivo LICENSE separado. O pacote é uma entrega privada para revisão e não concede direitos adicionais.

O enquadramento proposto é um artigo de replicação e auditoria bilíngue. A análise não demonstra causalidade racial nem superioridade geral de uma arquitetura. Nenhum experimento novo pago, publicação pública, contato com autores ou submissão foi realizado nesta etapa.
