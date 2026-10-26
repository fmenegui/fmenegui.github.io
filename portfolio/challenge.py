"""The author's PhysioNet 2024 story, grounded in the paper and doctoral thesis."""

CHALLENGE = {'pt': {'kicker': 'Classificação de imagens de ECG · 2024',
        'title': 'PhysioNet Challenge 2024',
        'subtitle': '',
        'summary': 'Liderei a AIMED, que ficou em primeiro lugar na classificação de imagens de '
                   'ECG. Usamos pré-treinamento com ECGs e cinco modelos ConvNeXt em conjunto.',
        'status': '1º lugar · Equipe AIMED',
        'period': '2024',
        'opening_title': 'Pesquisa com imagens de ECG no InCor',
        'opening': ['Quando o tema de 2024 foi anunciado, eu já estudava a classificação de ECGs '
                    'por imagem no doutorado, na USP e no InCor. Muitos exames do hospital estavam '
                    'armazenados como imagens, mas os modelos geralmente recebiam o sinal em série '
                    'temporal. Minha pesquisa partia dessa diferença.',
                    'Na AIMED, equipe que liderei, aproveitamos o que eu já havia testado no '
                    'doutorado para definir o treinamento. Os organizadores avaliaram nosso código '
                    'com dados que não conhecíamos. Ficamos em primeiro lugar em classificação.'],
        'award_alt': 'Felipe Dias e Marco Antônio Gutierrez na entrega do prêmio de classificação '
                     'do PhysioNet Challenge 2024, com Matthew Reyna e Gari Clifford.',
        'award_caption': 'Entrega do prêmio no Computing in Cardiology 2024, em Karlsruhe, '
                         'Alemanha. Da esquerda para a direita: Matthew Reyna, Felipe Dias, Marco '
                         'Antônio Gutierrez e Gari Clifford.',
        'photo_source': 'Foto: SBIS.',
        'certificate_alt': 'Certificado do PhysioNet Challenge 2024: primeiro lugar em '
                           'classificação para a equipe AIMED, com Felipe M. Dias, Estela Ribeiro, '
                           'Quenaz B. Soares, José E. Krieger e Marco A. Gutierrez.',
        'certificate_caption': 'Certificado de primeiro lugar em classificação, equipe AIMED. '
                               'Karlsruhe, 11 de setembro de 2024.',
        'challenge_title': 'O que é o PhysioNet Challenge?',
        'challenge_text': 'O PhysioNet Challenge é uma competição anual de pesquisa, organizada '
                          'pelo PhysioNet e pelo Computing in Cardiology desde 2000. A cada ano, '
                          'as equipes trabalham com um mesmo problema clínico ou fisiológico. Os '
                          'organizadores fornecem os dados e as regras de avaliação, testam os '
                          'algoritmos e disponibilizam o código para que outros pesquisadores '
                          'possam estudar e reproduzir os métodos.',
        'challenge_2024_title': 'O problema de 2024: ECGs em papel',
        'challenge_2024_text': 'Em 2024, o tema foi Digitization and Classification of ECG Images. '
                               'Havia duas tarefas, com premiações separadas. As equipes podiam '
                               'participar de uma delas ou das duas:',
        'tasks': [('Digitalização',
                   'Reconstruir as séries temporais das derivações a partir da imagem do exame.'),
                  ('Classificação',
                   'Identificar categorias do ECG a partir da imagem, diretamente ou usando sinais '
                   'reconstruídos.')],
        'evaluation': 'As equipes enviavam o código, e os organizadores executavam o treinamento e '
                      'a avaliação. Cada equipe escolhia uma versão final para o teste com dados '
                      'ocultos. Concentramos nosso trabalho na classificação direta das imagens.',
        'classification_title': 'Por que escolhemos classificar a imagem',
        'classification': ['Digitalizar um ECG significa recuperar o sinal a partir da imagem. '
                           'Isso exige separar cada derivação da grade, recuperar as escalas de '
                           'tempo e amplitude e lidar com traçados sobrepostos, sombras, '
                           'perspectiva e ruído. Um erro nessa etapa pode se propagar para o '
                           'classificador que usa o sinal reconstruído.',
                           'Eu já tinha testado CNNs para classificar imagens de ECG, então '
                           'decidimos concentrar o esforço nessa tarefa. O modelo analisa a imagem '
                           'diretamente, sem uma etapa de reconstrução do sinal.'],
        'doctoral_title': 'Experimentos do doutorado',
        'doctoral_text': 'No doutorado, usei imagens sintéticas geradas a partir de sinais '
                         'públicos e ECGs reais do ambulatório e da emergência do InCor. Comparei '
                         'ConvNeXt, EfficientNet-B3, ResNet50, ViT e Swin Transformer e testei '
                         'diferentes formas de treinar essas redes.',
        'doctoral_tests': ['Testei aumento de dados e diferentes resoluções de imagem.',
                           'Comparei a inicialização com ImageNet, o pré-treinamento com ECGs e a '
                           'combinação dos dois.',
                           'Experimentei incluir idade e sexo e usar uma função de perda que '
                           'combinava BCE e MCC.',
                           'Fiz estudos de ablação para avaliar cada escolha e testes com exames '
                           'fotografados e escaneados.'],
        'doctoral_note': 'O desafio aproveitou parte desses experimentos. O treinamento que '
                         'submetemos está descrito abaixo.',
        'pretraining_title': 'Pré-treinamento',
        'pretraining': ['Partimos dos pesos do ImageNet, mas um ECG é bem diferente das '
                        'fotografias desse banco. Antes do ajuste para o desafio, treinamos a rede '
                        'com imagens de ECG sintéticas e reais.',
                        'Na tese, também testei a inicialização com pesos aleatórios seguida de '
                        'pré-treinamento só com ECGs. O macro F1 foi menor do que com a '
                        'inicialização pelo ImageNet. A combinação de ImageNet e pré-treinamento '
                        'com ECGs teve o melhor resultado entre as três configurações abaixo, e '
                        'foi a que usamos na competição.'],
        'pretraining_head': ['Inicialização e pré-treinamento', 'Macro F1'],
        'pretraining_rows': [('ImageNet, sem pré-treinamento específico em ECG', '0,737'),
                             ('Pesos aleatórios + pré-treinamento em ECG', '0,565'),
                             ('ImageNet + pré-treinamento em ECG', '0,759')],
        'pretraining_caption': 'Resultados de ablação da tese, com validação cruzada de 10 folds '
                               'no InCor-EMG. A avaliação do PhysioNet Challenge aparece na seção '
                               'de resultados.',
        'method_title': 'Método publicado',
        'method_intro': 'No artigo Image-Based Electrocardiogram Classification Using Pre-trained '
                        'ConvNext, mostramos o treinamento usado no desafio:',
        'method_alt': 'Figura 1 do artigo do CinC 2024: pesos do ImageNet, pré-treinamento em '
                      'CODE15 e InCor-AMB, ajuste em InCor-EMG e ajuste final no PTB-XL com cinco '
                      'folds.',
        'method_caption': 'Metodologia final da AIMED, reproduzida da Figura 1 do artigo do CinC '
                          '2024.',
        'training_steps': [('ImageNet',
                            'Começamos com uma ConvNeXt pré-treinada em imagens gerais.'),
                           ('CODE15 e InCor-AMB',
                            'Adaptamos a rede a imagens sintéticas geradas com ECG-Image-Kit e a '
                            'ECGs reais do ambulatório.'),
                           ('InCor-EMG', 'Fizemos um ajuste adicional com imagens da emergência.'),
                           ('PTB-XL',
                            'Ajustamos para as 11 categorias do desafio com validação cruzada de 5 '
                            'folds e reunimos os cinco modelos em um ensemble.')],
        'method_detail': 'Usamos imagens em tons de cinza, com resolução de 224 × 224 no '
                         'pré-treinamento e 384 × 384 no ajuste final. O treinamento incluiu '
                         'aumento de dados, AdamW, BCE ponderada por classe e early stopping. As '
                         '11 categorias abrangiam normalidade, infarto, alterações de ST/T, '
                         'distúrbios de condução e arritmias.',
        'split_note': 'Retiramos o CINC21 do pré-treinamento porque ele contém o PTB-XL. Também '
                      'passamos de 10 para 5 folds de validação cruzada para respeitar os limites '
                      'computacionais do desafio.',
        'repository_title': 'Código e modelos',
        'repository_text': 'Reorganizei o código da AIMED em um repositório público com tutoriais '
                           'de instalação, inferência e treinamento, além de um manifesto dos '
                           'pesos e da configuração de inferência.',
        'repository_link': 'Acessar código e documentação da AIMED no GitHub',
        'results_title': 'Primeiro lugar: equipe AIMED',
        'results_text': 'A AIMED ficou em primeiro lugar entre as 16 entradas oficiais da tarefa '
                        'de classificação, com macro F1 de 0,817. Estes foram os três primeiros '
                        'resultados publicados pelos organizadores:',
        'results_head': ['Colocação', 'Equipe', 'Macro F1 do ranking'],
        'results_rows': [('1º', 'AIMED', '0,817'),
                         ('2º', 'Inventec AIC', '0,742'),
                         ('3º', 'BAPORLab', '0,730')],
        'ranking_link': 'Consultar a tabela oficial de classificação',
        'results_note': 'O ranking foi calculado com imagens de ECGs em papel escaneadas em cores '
                        'e em preto e branco. A avaliação estendida também incluiu fotos de '
                        'celular, papel manchado ou deteriorado e capturas de tela. Nos oito '
                        'cenários, nossa média foi 0,733. O desempenho caiu nas fotografias.',
        'team_title': 'Equipe',
        'team_text': 'Liderei a AIMED e fui o primeiro autor do artigo. O trabalho foi feito com '
                     'Estela Ribeiro, Quenaz B. Soares, José E. Krieger e Marco A. Gutierrez, no '
                     'Laboratório de Informática Biomédica do InCor. Tivemos apoio da Foxconn '
                     'Brasil e da Fundação Zerbini.',
        'history_title': 'Edições anteriores',
        'history_text': 'Temas das edições de 2016 a 2023:',
        'history_head': ['Ano', 'Tema'],
        'history_rows': [('2023', 'Recuperação neurológica após coma por parada cardíaca'),
                         ('2022', 'Detecção de sopros em fonocardiogramas'),
                         ('2021', 'Classificação de ECG com diferentes números de derivações'),
                         ('2020', 'Classificação de ECGs de 12 derivações'),
                         ('2019', 'Predição precoce de sepse'),
                         ('2018', 'Detecção de despertares em estudos do sono'),
                         ('2017', 'Fibrilação atrial em ECG curto de uma derivação'),
                         ('2016', 'Classificação de sons cardíacos normais e anormais')],
        'history_link': 'Ver o histórico completo desde 2000',
        'news_title': 'Notícias sobre a premiação',
        'news_entries': [('saudebusiness',
                          'Saúde Business',
                          '15/10/2024',
                          'Matéria de Juliana Santos.'),
                         ('itportal',
                          'IT Portal',
                          '16/10/2024',
                          'Matéria com informações do InCor.'),
                         ('pptasaude',
                          'PPTA Saúde',
                          '16/10/2024',
                          'Republicação da matéria do Saúde Business.')],
        'association_title': 'Nota da SBIS',
        'association_text': 'A Sociedade Brasileira de Informática em Saúde publicou um texto de '
                            'Marco A. Gutierrez sobre a premiação em 08/10/2024.',
        'association_link': 'Ler a nota da SBIS',
        'sources_title': 'Artigo e fontes',
        'paper_link': 'Ler o artigo completo (PDF)',
        'thesis_link': 'Tese de doutorado, incluindo o Apêndice A sobre o desafio',
        'official_link': 'Proposta e regras do desafio de 2024',
        'awards_link': 'Registro dos vencedores no Computing in Cardiology'},
 'en': {'kicker': 'ECG image classification · 2024',
        'title': 'PhysioNet Challenge 2024',
        'subtitle': '',
        'summary': 'I led AIMED to first place in ECG image classification. Our method combined '
                   'ECG pretraining with an ensemble of five ConvNeXt models.',
        'status': '1st place · Team AIMED',
        'period': '2024',
        'opening_title': 'ECG image research at InCor',
        'opening': ['When the 2024 topic was announced, I was already studying ECG image '
                    'classification during my PhD at the University of São Paulo and InCor. Many '
                    'hospital ECGs were stored as images, while most models expected time-series '
                    'signals. That mismatch was central to my research.',
                    'I led AIMED in the challenge. We used what I had already tested during my PhD '
                    'to choose the training strategy. The organizers then evaluated our code on '
                    'unseen data. We finished first in classification.'],
        'award_alt': 'Felipe Dias and Marco Antônio Gutierrez receiving the PhysioNet Challenge '
                     '2024 classification award, with Matthew Reyna and Gari Clifford.',
        'award_caption': 'Award presentation at Computing in Cardiology 2024 in Karlsruhe, '
                         'Germany. From left to right: Matthew Reyna, Felipe Dias, Marco Antônio '
                         'Gutierrez and Gari Clifford.',
        'photo_source': 'Photo: SBIS.',
        'certificate_alt': 'PhysioNet Challenge 2024 certificate: first place in classification '
                           'for team AIMED, naming Felipe M. Dias, Estela Ribeiro, Quenaz B. '
                           'Soares, José E. Krieger and Marco A. Gutierrez.',
        'certificate_caption': 'First-place classification certificate, team AIMED. Karlsruhe, '
                               'September 11, 2024.',
        'challenge_title': 'What is the PhysioNet Challenge?',
        'challenge_text': 'The PhysioNet Challenge is an annual research competition organized by '
                          'PhysioNet and Computing in Cardiology since 2000. Each year, teams work '
                          'on the same clinical or physiological problem. The organizers provide '
                          'the data and evaluation rules, test the algorithms and make the code '
                          'available so other researchers can study and reproduce the methods.',
        'challenge_2024_title': 'The 2024 problem: ECGs on paper',
        'challenge_2024_text': 'The 2024 topic was Digitization and Classification of ECG Images. '
                               'There were two tasks, with separate awards. Teams could enter '
                               'either task or both:',
        'tasks': [('Digitization', 'Reconstruct the lead time series from an image of the ECG.'),
                  ('Classification',
                   'Identify ECG categories from the image, either directly or using reconstructed '
                   'signals.')],
        'evaluation': 'Teams submitted their code, and the organizers ran the training and '
                      'evaluation. Each team selected a final version for testing on hidden data. '
                      'We focused on classifying the images directly.',
        'classification_title': 'Why we chose to classify the image',
        'classification': ['Digitizing an ECG means recovering the signal from the image. It '
                           'involves separating each lead from the grid, recovering the time and '
                           'amplitude scales, and dealing with overlapping traces, shadows, '
                           'perspective and noise. Errors can carry through to the classifier that '
                           'uses the reconstructed signal.',
                           'I had already tested CNNs for ECG image classification, so we decided '
                           'to focus on that task. The model analyzes the image directly, without '
                           'first reconstructing the signal.'],
        'doctoral_title': 'Doctoral experiments',
        'doctoral_text': 'During my PhD, I used synthetic images generated from public ECG signals '
                         "and real ECGs from InCor's outpatient and emergency departments. I "
                         'compared ConvNeXt, EfficientNet-B3, ResNet50, ViT and Swin Transformer, '
                         'and tested different ways to train them.',
        'doctoral_tests': ['I tested data augmentation and different image resolutions.',
                           'I compared ImageNet initialization, ECG pretraining and the '
                           'combination of both.',
                           'I tested adding age and sex, and using a loss function that combined '
                           'BCE and MCC.',
                           'I ran ablation studies to assess individual choices, and tested the '
                           'models on photographed and scanned ECGs.'],
        'doctoral_note': 'Our challenge entry built on some of these experiments. The training '
                         'strategy we submitted is outlined below.',
        'pretraining_title': 'Pretraining',
        'pretraining': ['We started with ImageNet weights, but ECGs look very different from the '
                        'photographs in that dataset. Before fine-tuning for the challenge, we '
                        'trained the network on synthetic and real ECG images.',
                        'In my thesis, I also tested random initialization followed by ECG-only '
                        'pretraining. Macro F1 was lower than with ImageNet initialization. '
                        'Combining ImageNet initialization with ECG pretraining gave the best '
                        'result among the three configurations below. We used that combination in '
                        'the competition.'],
        'pretraining_head': ['Initialization and pretraining', 'Macro F1'],
        'pretraining_rows': [('ImageNet, without ECG-specific pretraining', '0.737'),
                             ('Random weights + ECG pretraining', '0.565'),
                             ('ImageNet + ECG pretraining', '0.759')],
        'pretraining_caption': 'Thesis ablation results from 10-fold cross-validation on '
                               'InCor-EMG. The PhysioNet Challenge evaluation appears in the '
                               'results section.',
        'method_title': 'Published method',
        'method_intro': 'Our paper, Image-Based Electrocardiogram Classification Using Pre-trained '
                        'ConvNext, describes the training strategy we used in the challenge:',
        'method_alt': 'Figure 1 from the CinC 2024 paper: ImageNet weights, pretraining on CODE15 '
                      'and InCor-AMB, fine-tuning on InCor-EMG and final fine-tuning on PTB-XL '
                      'with five folds.',
        'method_caption': 'AIMED’s final method, reproduced from Figure 1 of the CinC 2024 paper.',
        'training_steps': [('ImageNet', 'We started with a ConvNeXt pretrained on general images.'),
                           ('CODE15 and InCor-AMB',
                            'We adapted the network to synthetic images generated with '
                            'ECG-Image-Kit and real outpatient ECGs.'),
                           ('InCor-EMG',
                            'We performed an additional fine-tuning stage on emergency ECG '
                            'images.'),
                           ('PTB-XL',
                            'We fine-tuned for the 11 challenge categories using 5-fold '
                            'cross-validation and combined the five models into an ensemble.')],
        'method_detail': 'We used grayscale images at 224 × 224 resolution for pretraining and 384 '
                         '× 384 for final fine-tuning. Training included data augmentation, AdamW, '
                         'class-weighted BCE and early stopping. The 11 categories covered normal '
                         'ECGs, infarction, ST/T changes, conduction disturbances and arrhythmias.',
        'split_note': 'We left CINC21 out of pretraining because it contains PTB-XL. We also '
                      'reduced cross-validation from 10 to 5 folds to stay within the challenge '
                      'computing limits.',
        'repository_title': 'Code and models',
        'repository_text': 'I reorganized the AIMED code into a public repository with tutorials '
                           'for installation, inference and training, plus a manifest of the '
                           'weights and inference configuration.',
        'repository_link': 'View AIMED code and documentation on GitHub',
        'results_title': 'First place: team AIMED',
        'results_text': 'AIMED finished first among the 16 official classification entries, with a '
                        'macro F1 of 0.817. These were the top three results published by the '
                        'organizers:',
        'results_head': ['Rank', 'Team', 'Ranking macro F1'],
        'results_rows': [('1st', 'AIMED', '0.817'),
                         ('2nd', 'Inventec AIC', '0.742'),
                         ('3rd', 'BAPORLab', '0.730')],
        'ranking_link': 'View the official classification score table',
        'results_note': 'The ranking was based on color and black-and-white scans of paper ECGs. '
                        'The extended evaluation also tested phone photos, stained or damaged '
                        'paper and monitor screenshots. Our average score across the eight '
                        'scenarios was 0.733. Scores were lower on photographs.',
        'team_title': 'Team',
        'team_text': "I led AIMED and was the paper's first author. The team included Estela "
                     "Ribeiro, Quenaz B. Soares, José E. Krieger and Marco A. Gutierrez at InCor's "
                     'Biomedical Informatics Laboratory. Foxconn Brazil and the Zerbini Foundation '
                     'supported the work.',
        'history_title': 'Previous editions',
        'history_text': 'Topics from the 2016 to 2023 editions:',
        'history_head': ['Year', 'Topic'],
        'history_rows': [('2023', 'Neurological recovery from coma after cardiac arrest'),
                         ('2022', 'Heart murmur detection from phonocardiograms'),
                         ('2021', 'ECG classification with different lead counts'),
                         ('2020', 'Classification of 12-lead ECGs'),
                         ('2019', 'Early prediction of sepsis'),
                         ('2018', 'Arousal detection in sleep studies'),
                         ('2017', 'Atrial fibrillation in short single-lead ECGs'),
                         ('2016', 'Normal and abnormal heart sound classification')],
        'history_link': 'Explore the complete history since 2000',
        'news_title': 'News coverage',
        'news_entries': [('saudebusiness',
                          'Saúde Business',
                          'October 15, 2024',
                          'Article by Juliana Santos.'),
                         ('itportal',
                          'IT Portal',
                          'October 16, 2024',
                          'Report based on information from InCor.'),
                         ('pptasaude',
                          'PPTA Saúde',
                          'October 16, 2024',
                          'Republication of the Saúde Business article.')],
        'association_title': 'SBIS announcement',
        'association_text': 'The Brazilian Society of Health Informatics published an article by '
                            'Marco A. Gutierrez about the award on October 8, 2024.',
        'association_link': 'Read the SBIS announcement',
        'sources_title': 'Paper and sources',
        'paper_link': 'Read the full paper (PDF)',
        'thesis_link': 'Doctoral thesis, including Appendix A on the challenge',
        'official_link': 'The 2024 challenge proposal and rules',
        'awards_link': 'Computing in Cardiology award winners'}}

CHALLENGE_LINKS = {'saudebusiness': 'https://www.saudebusiness.com/artigos/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
 'itportal': 'https://itportal.com.br/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
 'pptasaude': 'https://www.pptasaude.com.br/noticias/21020/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
 'repository': 'https://github.com/fmenegui/aimed_physionet2024',
 'paper': 'https://cinc.org/archives/2024/pdf/CinC2024-398.pdf',
 'thesis': 'https://doi.org/10.11606/T.3.2025.tde-16012026-084015',
 'official': 'https://moody-challenge.physionet.org/2024/',
 'ranking': 'https://moody-challenge.physionet.org/2024/results/official_scores_classification.tsv',
 'awards': 'https://cinc.org/physionet-cinc-challenge-awards/',
 'history': 'https://moody-challenge.physionet.org/index.html',
 'photo': 'https://sbis.org.br/equipe-do-laboratorio-de-informatica-biomedica-do-incor-hc-fmusp-e-premiada-no-george-b-moody-physionet-challenge-2024/'}
