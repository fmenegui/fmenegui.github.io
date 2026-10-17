# FairLens com Jev e GPT Decisions, inglês e português

Protocolo fixado antes da execução integral. Avaliação de viés nas saídas de modelos. Os escores não representam probabilidades reais de criminalidade, saúde ou competência das pessoas.

## Escopo e limitação da replicação

Fonte: [FairLens](https://arxiv.org/abs/2609.01691), [código oficial](https://github.com/vectorinstitute/fairlens), commit `130205f243267fc90b973cb875d1711c2d932bbe`.

| Domínio | Fechadas | Abertas | Total por idioma |
|---|---:|---:|---:|
| Contratação | 21 | 9 | 30 |
| Jurídico e segurança | 9 | 12 | 21 |
| Saúde | 8 | 10 | 18 |
| Total | 38 | 31 | 69 |

São usadas todas as 1.505 imagens do split oficial, com os cinco grupos raciais, os dois rótulos de gênero e as faixas de idade dos autores. São 622 White, 353 Black, 171 Asian, 276 Indian e 83 Other. Os nomes são os rótulos do banco, sem reclassificar as pessoas.

As 69 perguntas estão preservadas em inglês e traduzidas em português brasileiro. Os dois endpoints solicitados oferecem escolhas e escores, sem a geração livre de texto exigida pelas 31 abertas. Essas perguntas permanecem no inventário como `unsupported_free_text`. Não são transformadas em escolhas nem respondidas por um terceiro modelo.

A execução cobre 1.505 × 38 × 2 idiomas × 2 modelos = **228.760 tarefas fechadas**. As **186.620 combinações abertas** não podem ser executadas nesses endpoints. Portanto, este trabalho não deve ser apresentado como replicação completa das 69 perguntas ou da métrica de viés de texto livre.

Documentação de capacidades consultada em 16/10/2026: [Jev](https://docs.typesafe.ai/api) e [GPT Decisions](https://developers.openai.com/api/docs/guides/decisions).

## Entradas e tradução

`questions.en.original.json` preserva o JSON público original. `translations.pt-BR.json` contém todas as traduções, hashes de cada pergunta de origem, contextos, instruções finais e o mapa de alternativas. Nenhuma correção ortográfica é aplicada ao inglês original, inclusive ao erro `seving`.

Cada tradução mantém o tipo de pergunta, a ordem das opções, a resposta esperada, a opção adversa quando definida e a abstenção. A API recebe exclusivamente termos do idioma da condição. A análise reconverte as respostas para os rótulos canônicos em inglês. Essa conversão ocorre depois da inferência.

A tradução foi produzida e revisada por IA com verificações estruturais e semânticas. Não houve revisão independente por tradutor humano ou retrotradução cega. Palavras com gênero gramatical em português podem influenciar os resultados. A comparação estima a diferença entre estes dois conjuntos específicos de formulações. Não identifica um efeito puro do idioma separado da escolha de palavras.

O mesmo PNG é usado em ambos os modelos e idiomas. Os recortes originais de 200 × 200 são centralizados em fundo cinza neutro de 280 × 280, sem interpolação dos pixels. Essa adaptação é necessária para Jev e difere da entrada nativa do estudo. O arquivo original do Google Drive está indisponível. É utilizado o espelho explicitamente documentado, com tamanho e checksum fixados. A correspondência nominal é verificada em todos os 1.505 arquivos. A igualdade byte a byte com o arquivo indisponível do Drive não pôde ser confirmada.

Idade, gênero, raça, nomes de arquivos e identificadores demográficos ficam fora das requisições. São usados somente para agregação dos resultados. Cada pergunta constitui uma requisição isolada, sem histórico de conversa e sem as outras perguntas como contexto. As quatro condições de cada foto ficam na mesma partição. Entradas oficiais com pixels idênticos mantêm identidades distintas e continuam na execução e nas métricas originais. Na inferência estatística complementar, utiliza-se um representante por PNG único, escolhido pela menor identidade de imagem em ordem lexicográfica, sem consultar respostas. PNGs com anotações demográficas conflitantes ficam fora desses testes complementares, com contagem explícita. As transições descritivas mantêm todas as entradas oficiais. A ordem é aleatória com semente fixa.

## Modelos e execução

Jev usa o mesmo contrato `jev-preview` do piloto, com verificação de que a versão servida é `jev-1.14.0`. GPT Decisions usa `gpt-6-luna`. Cada resposta guarda o identificador servido. Uma mudança de identificador interrompe o lote e preserva o checkpoint. As implementações internas dos provedores não podem ser congeladas pelo experimento.

A execução tem uma chamada por tarefa, sem repetições experimentais. Há até quatro tentativas HTTP para falhas transitórias. As partições têm teto de 10.000 tarefas por execução. São 64 partições, no máximo 16 em paralelo. As 228.760 tarefas incluem respostas do piloto ou do teste inicial somente quando o hash de imagem, prompt, opções, modelo, repetição e contrato corresponde exatamente. A migração documentada de identidade v1 para v2 acrescenta a identidade da entrada oficial, sem mudar a requisição ou a resposta. O hash original do checkpoint é preservado em `source_task_id`.

Antes do lote completo há um teste de compatibilidade com uma imagem de cada grupo racial e todas as 76 variantes fechadas nos dois modelos. As 760 respostas também são reaproveitadas. Checkpoints são gravados por resposta. Falhas de autenticação, mudança de modelo ou dez erros HTTP consecutivos interrompem o processo. Recusas continuam separadas da opção de abstenção.

O orçamento de chamadas não é uma estimativa de custo em dólares. Tokens e uso retornados pelos provedores ficam registrados para totalização posterior. Os artefatos privados do workflow têm retenção de 90 dias. O código e o protocolo ficam versionados no repositório.

## Métricas e comparações

Os programas estatísticos originais são baixados do commit fixado e validados por seus hashes Git. São executados sem modificações sobre exportações das respostas com rótulos canônicos. Isso reproduz as métricas fechadas de soundness, paridade demográfica e associações demográficas, com os denominadores e faixas etárias originais, incluindo idade jovem abaixo de 30, intermediária de 30 a 59 e sênior a partir de 60. As saídas ficam em `upstream-metrics/`.

O relatório complementar explicita cobertura, recusas, falhas e escores inválidos. Para suas métricas de respostas classificáveis, usa somente respostas válidas. Os denominadores podem diferir dos programas originais, que incluem respostas não interpretáveis. Perguntas de associação sem opção adversa não recebem um desfecho adverso inventado.

A comparação inglês versus português é pareada por imagem e pergunta, para cada modelo. São calculados:

- Matriz de transição entre opções e número de respostas que mudam.
- Mudanças de soundness, abstenção e escolha adversa, com teste exato de McNemar.
- Correção de Holm em uma família com todos esses testes de idioma nos dois modelos.
- Mudança média do escore adverso, com bootstrap pareado por imagem, 2.000 reamostragens.
- Diferença de taxa adversa Black menos White, com intervalo de Newcombe a partir de Wilson. O intervalo continua informativo quando não há eventos.
- Diferença de escore Black menos White e interação raça × idioma, com bootstrap por imagem, apresentados como estimativas exploratórias.
- Resultados por raça, gênero e faixa etária para cada pergunta e para cada domínio.

O relatório distingue ausência de diferença detectável de evidência de equivalência. Intervalos bootstrap podem degenerar com amostras sem variação e são sinalizados. As proporções categóricas também têm intervalos de Wilson. As análises de escores e interações são exploratórias, sem alegações confirmatórias baseadas em intervalos não ajustados. Não são calculados acurácia criminal, AUROC ou calibração contra criminalidade real, pois o banco não oferece esse desfecho.

O endpoint jurídico `legal-07` já foi examinado no piloto. A análise integral usa parte das mesmas imagens e não constitui uma confirmação independente do piloto. O banco integral tem composição demográfica diferente da amostra pareada anterior. Diferenças entre raças são descritivas, sem atribuição causal isolada a raça.

## Arquivos e reprodução

O workflow `fairlens-bilingual-full.yml` prepara o banco, valida a compatibilidade, executa as partições e gera o relatório. `bilingual-launch.json` dispara a execução na branch do experimento. As chaves ficam nos secrets existentes.

O relatório final deve ser chamado de concluído apenas com 228.760 tarefas terminais únicas, cobertura de todas as condições e ausência de falhas pendentes. `metrics-bilingual.json`, `report-bilingual.md`, as 36 saídas dos avaliadores originais e as respostas brutas ficam no artefato `fairlens-bilingual-report`. O inventário também explicita a parte aberta que permaneceu sem suporte.
