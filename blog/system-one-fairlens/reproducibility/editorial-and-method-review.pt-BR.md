# Revisão editorial e metodológica do post FairLens

Revisão de 16 de outubro de 2026. Escopo: conteúdo do blog e interpretação dos resultados já obtidos. Não foram alterados os dados executados, as traduções, os gabaritos ou as análises estatísticas. Não houve novas chamadas de inferência.

## Revisão editorial aplicada

A referência de voz foram as versões atuais dos posts CODE Test e PTB-XL no repositório do site, lidas diretamente. Foram mantidos o inglês, a primeira pessoa, a explicação concreta do experimento e a discussão das diferenças entre scores e decisões. O novo texto não usa perguntas retóricas. As perguntas literais do benchmark e das chamadas de API permanecem intactas.

A seção sobre Joseph Redmon foi retirada. As fontes anteriormente verificadas atribuem sua saída da pesquisa em visão computacional a aplicações militares e privacidade. O episódio não é evidência sobre viés demográfico nos modelos aqui avaliados e interrompia a passagem do caso Twitter para nosso protocolo. A retirada é editorial e não altera o registro histórico das fontes já consultadas.

O título passou a ser declarativo. A sequência agora é: problema, Twitter, modelos e FairLens, desenho, critérios de contagem, resultados, interpretação, limitações, API e dados. Os exemplos JSON continuam completos, depois da discussão principal.

## Problemas metodológicos e tratamento

| Importância | Ponto | Correção no post | Limite que permanece |
|:--|:--|:--|:--|
| Alta | Soundness podia ser lida como medida geral de justiça | Definição explícita de concordância com o alvo lógico e separação de disparidade, resposta sem evidência e recusa | Não há um único índice que estabeleça justiça geral |
| Alta | Aparência podia ser interpretada como causa da resposta | Explicação de que não houve controle sem imagem nem intervenção sobre raça percebida | Não se identifica contribuição da imagem, causalidade racial ou mecanismo interno |
| Alta | O contraste racial podia parecer confirmado por testes corrigidos | Separação explícita dos intervalos raciais sem ajuste e da família Holm de 260 testes de idioma | Contrastes raciais seguem exploratórios e não ajustados por idade, gênero ou condições visuais |
| Alta | Intervalo em inglês fora de zero e em português incluindo zero podia sugerir teste de interação | O texto afirma que comparar esses dois intervalos não testa mudança da disparidade | Não se promove o contraste entre idiomas a resultado causal |
| Alta | Recusas em contratação podiam ser interpretadas como discriminação ou falha simples de conhecimento | Descrição do conflito entre o alvo do benchmark e a recusa do endpoint, sem atribuir intenção interna | O score do benchmark não decide se a política de recusa é apropriada em uso real |
| Alta | Tradução podia ser tratada como intervenção isolada de idioma | Exemplos concretos de random photo versus foto casual e gênero gramatical | Falta revisão humana independente. Preservar pt-BR-v1, sem correção retroativa |
| Alta | A motivação sobre probabilidades estava incompletamente respondida | Tabela com scores médios de Criminal por grupo, nos quatro conjuntos, e contraste Jev EN no subconjunto limpo | Scores não podem ser calibrados contra criminalidade real, que não é observada |
| Média | Número de avaliações podia ser tomado como número de pessoas independentes | 228.760 tarefas separadas de 1.505 entradas, 1.500 PNGs únicos e até 1.497 observações inferenciais | Identidade não verificada, dependências além de duplicatas exatas permanecem possíveis |
| Média | Alta soundness podia ser entendida como capacidade de reconhecer atributos em rostos | Alvo fixo por pergunta e possibilidade de resposta pelo texto descritos | Não há demonstração de utilidade de análise facial |
| Média | Diferenças entre APIs podiam ser atribuídas apenas à arquitetura | Duplicação do prompt no adaptador GPT descrita antes dos exemplos | Interface, política do provedor, prompt e modelo não foram isolados |
| Média | Replicação podia sugerir reprodução integral do artigo | Todas as 38 perguntas fechadas separadas das 31 abertas não executadas | Saída tipada, imagem adquirida por espelho e pré-processamento diferem do protocolo original |
| Média | Comparação com os modelos publicados podia parecer avaliação pareada | Mesma média por domínio, mas diferenças de protocolo e falta de saídas individuais explicitadas | Não há teste direto contra os modelos do artigo |
| Média | Intervalos podiam ser entendidos como estabilidade entre execuções | Unidade de reamostragem, ausência de estudo de repetibilidade e inspeção dos resultados parciais declaradas | Não há validação independente, pré-registro confirmatório ou amostragem de futuras versões |
| Média | JSON de entrada podia parecer log original de rede | Reconstrução pelo adaptador e manifesto mantida, distinguindo resposta gravada de chamada reconstruída | Cabeçalhos HTTP completos e requests originais de rede não foram gravados |
| Média | Metadados demográficos podiam ser lidos como identidades verificadas | Categorias herdadas do UTKFace e falta de representatividade brasileira explicitadas | Categorias binárias e Other limitam a análise |

## Verificações numéricas da revisão

- Mantidos os totais de 228.760 tarefas, 57.190 por modelo e idioma, 38 perguntas fechadas e 16.761 recusas GPT.
- Mantida a definição de soundness com todas as respostas terminais no denominador nas tabelas principais.
- Mantidos os 36 relatórios estatísticos originais e as estatísticas bilíngues, anteriormente reproduzidos a partir do CSV.
- A nova tabela de scores usa as médias por raça e idioma já presentes em metrics-bilingual.json. Não adiciona inferência ou nova seleção de casos.
- Para GPT EN, a média Black usa 352 respostas classificáveis. A recusa não recebeu score zero. Os outros denominadores descritivos são 353 Black e 622 White.
- Diferença de score Jev EN no subconjunto limpo: 2,0498425 pontos percentuais, intervalo bootstrap de 0,4728843 a 3,6778674, sem ajuste múltiplo.
- O contraste por categoria Jev EN permanece 2,6825180 pontos, intervalo de 0,2710164 a 5,6627809. Não foi convertido em afirmação causal.
- A queda de 1,9372077 pontos na seleção de Criminal entre prompts Jev EN/PT tem p Holm 8,0466270 × 10⁻⁷. Esse teste não valida o contraste racial nem mede calibração.

## Avaliação final

O material sustenta um post técnico de auditoria exploratória, com dados suficientes para conferir as respostas e reproduzir as análises salvas. Não sustenta um diagnóstico geral de racismo de um sistema, uma comparação causal de raça, uma conclusão sobre risco criminal individual ou uma declaração de superioridade entre arquiteturas.

As lacunas experimentais foram explicitadas, sem simular controles que não foram executados. O rascunho continua privado para revisão do autor. A revisão humana das traduções permanece pendente.

## Exemplos visuais adicionados

A pedido do autor, o rascunho passou a incluir dez entradas reais, duas por categoria racial anotada no UTKFace, selecionadas pelo menor ID em cada estrato de raça e gênero binário do banco. A seleção exclui anotações conflitantes e não consulta respostas dos modelos. As legendas explicitam a origem das categorias e a ausência de representatividade proporcional.

A fotografia do exemplo de API já existente também foi incluída, totalizando onze PNGs. Todos foram reconstruídos a partir do arquivo de origem com SHA-256 conferido, e cada PNG coincide com o hash do input realmente avaliado. O CSV e os resultados não foram alterados. A inclusão é restrita ao rascunho privado. Não foi disponibilizado o banco completo de imagens.

## Nova conferência e versão compacta

Foram reconferidos 228.760 registros terminais, as 57.190 tarefas de cada condição, os totais por domínio, as 16.761 recusas e os denominadores de categoria. Os numeradores dos oito grupos correspondem a contagens inteiras de respostas que coincidem com o alvo. Os quatro conjuntos de respostas de legal-07 somam 1.505 entradas cada, contando recusas separadamente. A família Holm contém 260 testes e os contrastes de categoria usam pares classificáveis, enquanto os de recusa usam todos os pares terminais elegíveis.

Não foram detectadas divergências nos totais ou nas estatísticas citadas. Isso não elimina as limitações do desenho listadas acima. Os limites essenciais permanecem no corpo do texto: ausência de intervenção causal e controle sem imagem, caráter exploratório, intervalos raciais sem ajuste múltiplo, tradução sem validação humana e ausência de criminalidade real observada.

O texto principal foi reduzido para aproximadamente 1.100 palavras visíveis. O anexo usa details/summary nativos, começa fechado e preserva os detalhes técnicos, as tabelas completas, os JSONs, os métodos de reprodução e as referências. Somente a tabela de campos foi substituída por uma descrição e pelo esquema completo já distribuído. Não houve remoção de registros, mudança de denominadores ou nova inferência. A galeria de dez imagens continua visível no texto principal.

## Releitura integral do FairLens e destaque para criminalidade

Foram relidos a introdução, o desenho do benchmark, as métricas, as tabelas de resultados, a discussão e os apêndices do arXiv:2609.01691v1. O artigo distingue validade da resposta e disparidade entre grupos, além da associação a papéis ou status sem suporte e da avaliação aberta. A pergunta sobre criminalidade aparece na Tabela 7 do apêndice B. Cannot tell é o alvo e Criminal é o rótulo adverso. O artigo observa que paridade pequena pode coexistir com inferências sem fundamento distribuídas amplamente.

A redação passou a apresentar criminalidade antes das médias gerais. A tabela completa de respostas, o gráfico de diferença Black menos White e a tabela de scores estão visíveis fora do anexo. A discussão inclui as 461 escolhas Jev em inglês e 97 em português que atribuem Criminal ou Law-abiding Civilian sem evidência suficiente. Esses totais são somas dos rótulos registrados, sem nova análise inferencial.

Os intervalos permanecem exploratórios e sem ajuste múltiplo. A comparação descritiva com o estudo original não passou a ser teste pareado. Nenhum resultado de perguntas abertas foi atribuído à nossa execução. O limite inferior do intervalo Jev PT é mostrado como −1,84 ponto percentual, seguindo a formatação direta do valor salvo em duas casas, de forma consistente com a figura.

A figura para celular usa exatamente as mesmas estimativas e os mesmos intervalos da versão de computador. Só a disposição muda. Métodos, regras de seleção, modelos de request, JSONs completos e reprodução permanecem no toggle, fechado por padrão. A narrativa principal fica em aproximadamente 1.400 palavras. CSV, respostas e estatísticas não foram alterados.
