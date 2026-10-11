"""The author's PhysioNet 2024 story, grounded in the paper and doctoral thesis."""

CHALLENGE = {
    'pt': {
        'kicker': 'Classificação de imagens de ECG · 2024',
        'title': 'PhysioNet Challenge 2024',
        'subtitle': '',
        'summary': 'Participei com a equipe AIMED usando uma ConvNeXt pré-treinada em ECGs e um ensemble de cinco modelos.',
        'status': '1º lugar · Equipe AIMED',
        'period': '2024',
        'opening_title': 'Pesquisa com imagens de ECG no InCor',
        'opening': [
            'Em 2024, eu já pesquisava classificação de imagens de ECG no doutorado na USP, trabalhando no InCor, um hospital de cardiologia. Muitos exames do hospital eram armazenados como imagens, mas boa parte dos modelos disponíveis recebia o sinal como uma série temporal.',
            'O tema do desafio era esse mesmo problema. Usamos os experimentos do doutorado para montar a entrada da equipe AIMED e testar o modelo em dados que não conhecíamos. Ficamos em primeiro lugar na tarefa de classificação.'
        ],
        'award_alt': 'Felipe Dias e Marco Antônio Gutierrez na entrega do prêmio de classificação do PhysioNet Challenge 2024, com Matthew Reyna e Gari Clifford.',
        'award_caption': 'Entrega do prêmio no Computing in Cardiology 2024, em Karlsruhe, Alemanha. Da esquerda para a direita: Matthew Reyna, Felipe Dias, Marco Antônio Gutierrez e Gari Clifford.',
        'photo_source': 'Foto publicada pela SBIS em texto de Marco A. Gutierrez.',
        'certificate_alt': 'Certificado do PhysioNet Challenge 2024: primeiro lugar em classificação para a equipe AIMED, com Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger e Marco A. Gutierrez.',
        'certificate_caption': 'Certificado de primeiro lugar em classificação, equipe AIMED. Karlsruhe, 11 de setembro de 2024.',
        'certificate_link': 'Abrir certificado em tamanho original',
        'challenge_title': 'O que é o PhysioNet Challenge?',
        'challenge_text': 'Desde 2000, PhysioNet e Computing in Cardiology promovem desafios anuais de algoritmos para problemas clínicos e fisiológicos. A competição reúne dados, regras de avaliação e código aberto para comparar propostas em condições comuns.',
        'challenge_2024_title': 'O problema de 2024: ECGs em papel',
        'challenge_2024_text': 'A edição de 2024, Digitization and Classification of ECG Images, tinha duas tarefas com premiações separadas. Era possível participar de uma delas ou das duas:',
        'tasks': [
            ('Digitalização', 'Reconstruir as séries temporais das derivações a partir da imagem do exame.'),
            ('Classificação', 'Identificar categorias do ECG a partir da imagem, diretamente ou usando sinais reconstruídos.')
        ],
        'evaluation': 'As equipes submetiam o código. Os organizadores executavam o treinamento e a avaliação, e cada equipe escolhia uma entrada final para o teste oculto. Nossa participação se concentrou na classificação direta das imagens.',
        'classification_title': 'Por que escolhemos classificar a imagem',
        'classification': [
            'A digitalização exige localizar cada derivação, separar o traçado da grade, recuperar escalas de tempo e amplitude e lidar com sobreposição, perspectiva, sombras e ruído. Erros nessa reconstrução também afetam a classificação do sinal.',
            'Escolhemos trabalhar apenas na classificação. Eu já vinha testando CNNs com imagens de ECG no doutorado, então usamos essa abordagem para identificar as categorias diretamente na imagem, sem reconstruir o sinal.'
        ],
        'doctoral_title': 'Experimentos do doutorado',
        'doctoral_text': 'A pesquisa reunia imagens sintéticas geradas a partir de sinais públicos e imagens reais do ambulatório e da emergência do InCor. Nos experimentos da tese, comparei ConvNeXt, EfficientNet-B3, ResNet50, ViT e Swin Transformer, além de diferentes estratégias de treinamento.',
        'doctoral_tests': [
            'Aumento de dados e mudanças de resolução das imagens.',
            'Inicialização com ImageNet, pré-treinamento com ECGs e a combinação dos dois.',
            'Uso de idade e sexo como metadados e uma função de perda combinando BCE e MCC.',
            'Estudos de ablação para separar o efeito de cada escolha e avaliações com exames fotografados e escaneados.'
        ],
        'doctoral_note': 'Esses experimentos pertencem à pesquisa do doutorado. A versão do desafio teve suas próprias adaptações, descritas abaixo e no artigo de 2024.',
        'pretraining_title': 'Pré-treinamento',
        'pretraining': [
            'Partimos de pesos treinados no ImageNet e depois treinamos a rede com imagens de ECG sintéticas e reais. Essa etapa adaptou as representações aprendidas em fotografias gerais aos traçados de ECG, antes do ajuste para o desafio.',
            'Na tese, testei também começar com pesos aleatórios e pré-treinar só com ECGs. O macro F1 ficou abaixo do baseline com ImageNet. A combinação de ImageNet e pré-treinamento com ECGs teve o melhor resultado entre as três configurações abaixo, e foi a que usamos na competição.'
        ],
        'pretraining_head': ['Inicialização e pré-treinamento', 'Macro F1'],
        'pretraining_rows': [
            ('ImageNet, sem pré-treinamento específico em ECG', '0,737'),
            ('Pesos aleatórios + pré-treinamento em ECG', '0,565'),
            ('ImageNet + pré-treinamento em ECG', '0,759')
        ],
        'pretraining_caption': 'Experimentos de ablação da tese: validação cruzada de 10 folds no InCor-EMG. Estes valores não são os resultados do PhysioNet Challenge.',
        'method_title': 'Método publicado',
        'method_intro': 'No artigo Image-Based Electrocardiogram Classification Using Pre-trained ConvNext, descrevemos o treinamento em quatro etapas:',
        'training_steps': [
            ('ImageNet', 'Começamos com uma ConvNeXt pré-treinada em imagens gerais.'),
            ('CODE15 e InCor-AMB', 'Adaptamos a rede a imagens sintéticas geradas com ECG-Image-Kit e a ECGs reais do ambulatório.'),
            ('InCor-EMG', 'Fizemos um ajuste adicional com imagens da emergência.'),
            ('PTB-XL', 'Ajustamos para as 11 categorias do desafio com validação cruzada de 5 folds e reunimos os cinco modelos em um ensemble.')
        ],
        'method_detail': 'O treinamento usou imagens em tons de cinza, resolução de 224 × 224 no pré-treinamento e 384 × 384 no ajuste final, aumento de dados, AdamW, BCE ponderada por classe e early stopping. As 11 categorias incluíam normalidade, infarto, alterações de ST/T, distúrbios de condução e arritmias.',
        'split_note': 'Excluímos o CINC21 do pré-treinamento porque ele contém o PTB-XL. Também reduzimos a validação de 10 para 5 folds para atender às limitações computacionais do desafio.',
        'results_title': 'Primeiro lugar: equipe AIMED',
        'results_text': 'AIMED ficou em primeiro entre as 16 entradas oficiais da tarefa de classificação, com macro F1 de 0,817. Os três primeiros resultados publicados pelos organizadores foram:',
        'results_head': ['Colocação', 'Equipe', 'Macro F1 do ranking'],
        'results_rows': [('1º', 'AIMED', '0,817'), ('2º', 'Inventec AIC', '0,742'), ('3º', 'BAPORLab', '0,730')],
        'ranking_link': 'Consultar a tabela oficial de classificação',
        'results_note': 'O ranking usou scans coloridos e em preto e branco de ECGs em papel. A avaliação estendida incluiu fotos de celular, manchas, deterioração e capturas de monitor. Nesses oito cenários, nossa média foi 0,733. O desempenho foi menor nas fotografias.',
        'team_title': 'Equipe',
        'team_text': 'Fui integrante da AIMED e primeiro autor do artigo, com Estela Ribeiro, Quenaz B. Soares, José E. Krieger e Marco A. Gutierrez. O trabalho foi desenvolvido no Laboratório de Informática Biomédica do InCor, com apoio da Foxconn Brasil e da Fundação Zerbini.',
        'history_title': 'Edições anteriores',
        'history_text': 'Temas das edições de 2016 a 2023:',
        'history_head': ['Ano', 'Tema'],
        'history_rows': [
            ('2023', 'Recuperação neurológica após coma por parada cardíaca'),
            ('2022', 'Detecção de sopros em fonocardiogramas'),
            ('2021', 'Classificação de ECG com diferentes números de derivações'),
            ('2020', 'Classificação de ECGs de 12 derivações'),
            ('2019', 'Predição precoce de sepse'),
            ('2018', 'Detecção de despertares em estudos do sono'),
            ('2017', 'Fibrilação atrial em ECG curto de uma derivação'),
            ('2016', 'Classificação de sons cardíacos normais e anormais')
        ],
        'history_link': 'Ver o histórico completo desde 2000',
        'news_title': 'Notícias sobre a premiação',
        'news_entries': [
            ('saudebusiness', 'Saúde Business', '15/10/2024', 'Matéria de Juliana Santos.'),
            ('itportal', 'IT Portal', '16/10/2024', 'Notícia com o InCor indicado como fonte.'),
            ('pptasaude', 'PPTA Saúde', '16/10/2024', 'Republicação da matéria do Saúde Business.')
        ],
        'association_title': 'Nota da SBIS',
        'association_text': 'A Sociedade Brasileira de Informática em Saúde publicou um texto de Marco A. Gutierrez sobre a premiação em 08/10/2024.',
        'association_link': 'Ler a nota da SBIS',
        'sources_title': 'Artigo e fontes',
        'paper_link': 'Ler o artigo completo (PDF)',
        'thesis_link': 'Tese de doutorado, incluindo o Apêndice A sobre o desafio',
        'official_link': 'Proposta e regras do desafio de 2024',
        'awards_link': 'Registro dos vencedores no Computing in Cardiology'
    },
    'en': {
        'kicker': 'ECG image classification · 2024',
        'title': 'PhysioNet Challenge 2024',
        'subtitle': '',
        'summary': 'I participated with team AIMED, using a ConvNeXt pretrained on ECGs and an ensemble of five models.',
        'status': '1st place · Team AIMED',
        'period': '2024',
        'opening_title': 'ECG image research at InCor',
        'opening': [
            'In 2024, I was already researching ECG image classification for my PhD at the University of São Paulo, working at InCor, a cardiology hospital. Many hospital ECGs were stored as images, while most available models expected the signal as a time series.',
            'The challenge addressed the same problem. We used my doctoral experiments to build team AIMED’s entry and test the model on data we had not seen. We finished first in the classification task.'
        ],
        'award_alt': 'Felipe Dias and Marco Antônio Gutierrez receiving the PhysioNet Challenge 2024 classification award, with Matthew Reyna and Gari Clifford.',
        'award_caption': 'Award presentation at Computing in Cardiology 2024 in Karlsruhe, Germany. From left to right: Matthew Reyna, Felipe Dias, Marco Antônio Gutierrez and Gari Clifford.',
        'photo_source': 'Photo published by SBIS in an article by Marco A. Gutierrez.',
        'certificate_alt': 'PhysioNet Challenge 2024 certificate: first place in classification for team AIMED, naming Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger and Marco A. Gutierrez.',
        'certificate_caption': 'First-place classification certificate, team AIMED. Karlsruhe, September 11, 2024.',
        'certificate_link': 'Open the full-size certificate',
        'challenge_title': 'What is the PhysioNet Challenge?',
        'challenge_text': 'Since 2000, PhysioNet and Computing in Cardiology have hosted annual algorithm challenges addressing clinical and physiological problems. Shared data, evaluation rules and open-source code allow teams to compare their approaches under common conditions.',
        'challenge_2024_title': 'The 2024 problem: ECGs on paper',
        'challenge_2024_text': 'The 2024 edition, Digitization and Classification of ECG Images, had two tasks with separate awards. Teams could enter either task or both:',
        'tasks': [
            ('Digitization', 'Reconstruct the lead time series from an image of the ECG.'),
            ('Classification', 'Identify ECG categories from the image, either directly or using reconstructed signals.')
        ],
        'evaluation': 'Teams submitted their code. The organizers ran training and evaluation, and each team selected a final entry for hidden-data testing. We focused on direct image classification.',
        'classification_title': 'Why we chose to classify the image',
        'classification': [
            'Digitization requires locating each lead, separating the trace from the grid, recovering time and amplitude scales, and handling overlap, perspective, shadows and noise. Reconstruction errors also affect signal classification.',
            'We chose to work only on classification. I had already been testing CNNs on ECG images in my PhD, so we used that approach to identify categories directly from the image, without reconstructing the signal.'
        ],
        'doctoral_title': 'Doctoral experiments',
        'doctoral_text': 'My research combined synthetic images rendered from public ECG signals with real outpatient and emergency ECG images from InCor. The thesis experiments compared ConvNeXt, EfficientNet-B3, ResNet50, ViT and Swin Transformer, as well as different training strategies.',
        'doctoral_tests': [
            'Data augmentation and changes in image resolution.',
            'ImageNet initialization, ECG pretraining and the combination of both.',
            'Age and sex metadata, and a loss combining BCE and MCC.',
            'Ablation studies to isolate the effect of each choice, plus evaluations on photographed and scanned exams.'
        ],
        'doctoral_note': 'These experiments belong to the doctoral research. The challenge entry had its own adaptations, described below and in the 2024 paper.',
        'pretraining_title': 'Pretraining',
        'pretraining': [
            'We started with ImageNet weights, then trained the network on synthetic and real ECG images. This stage adapted the representations learned from general photographs to ECG traces before fine-tuning for the challenge.',
            'In my thesis, I also tested starting with random weights and pretraining only on ECGs. Macro F1 was below the ImageNet baseline. ImageNet followed by ECG pretraining performed best among the three configurations below, and we used it in the competition.'
        ],
        'pretraining_head': ['Initialization and pretraining', 'Macro F1'],
        'pretraining_rows': [
            ('ImageNet, without ECG-specific pretraining', '0.737'),
            ('Random weights + ECG pretraining', '0.565'),
            ('ImageNet + ECG pretraining', '0.759')
        ],
        'pretraining_caption': 'Thesis ablation experiments: 10-fold cross-validation on InCor-EMG. These values are not PhysioNet Challenge results.',
        'method_title': 'Published method',
        'method_intro': 'In Image-Based Electrocardiogram Classification Using Pre-trained ConvNext, we describe four training stages:',
        'training_steps': [
            ('ImageNet', 'We started with a ConvNeXt pretrained on general images.'),
            ('CODE15 and InCor-AMB', 'We adapted the network to synthetic images generated with ECG-Image-Kit and real outpatient ECGs.'),
            ('InCor-EMG', 'We performed an additional fine-tuning stage on emergency ECG images.'),
            ('PTB-XL', 'We fine-tuned for the 11 challenge categories using 5-fold cross-validation and combined the five models into an ensemble.')
        ],
        'method_detail': 'Training used grayscale images, 224 × 224 resolution for pretraining and 384 × 384 for final fine-tuning, data augmentation, AdamW, class-weighted BCE and early stopping. The 11 categories covered normal ECGs, infarction, ST/T changes, conduction disturbances and arrhythmias.',
        'split_note': 'We excluded CINC21 from pretraining because it contains PTB-XL. We also reduced cross-validation from 10 to 5 folds to fit the challenge computing constraints.',
        'results_title': 'First place: team AIMED',
        'results_text': 'AIMED ranked first among the 16 official classification entries, with a macro F1 of 0.817. The top three results published by the organizers were:',
        'results_head': ['Rank', 'Team', 'Ranking macro F1'],
        'results_rows': [('1st', 'AIMED', '0.817'), ('2nd', 'Inventec AIC', '0.742'), ('3rd', 'BAPORLab', '0.730')],
        'ranking_link': 'View the official classification score table',
        'results_note': 'The ranking used color and black-and-white scans of paper ECGs. An extended evaluation included phone photos, stains, deterioration and monitor captures. Our average across those eight scenarios was 0.733. Performance was lower on photographs.',
        'team_title': 'Team',
        'team_text': 'I was an AIMED team member and first author of the paper, alongside Estela Ribeiro, Quenaz B. Soares, José E. Krieger and Marco A. Gutierrez. The work was developed at InCor’s Biomedical Informatics Laboratory, with support from Foxconn Brazil and the Zerbini Foundation.',
        'history_title': 'Previous editions',
        'history_text': 'Topics from the 2016 to 2023 editions:',
        'history_head': ['Year', 'Topic'],
        'history_rows': [
            ('2023', 'Neurological recovery from coma after cardiac arrest'),
            ('2022', 'Heart murmur detection from phonocardiograms'),
            ('2021', 'ECG classification with different lead counts'),
            ('2020', 'Classification of 12-lead ECGs'),
            ('2019', 'Early prediction of sepsis'),
            ('2018', 'Arousal detection in sleep studies'),
            ('2017', 'Atrial fibrillation in short single-lead ECGs'),
            ('2016', 'Normal and abnormal heart sound classification')
        ],
        'history_link': 'Explore the complete history since 2000',
        'news_title': 'News coverage',
        'news_entries': [
            ('saudebusiness', 'Saúde Business', 'October 15, 2024', 'Article by Juliana Santos.'),
            ('itportal', 'IT Portal', 'October 16, 2024', 'News report citing InCor as its source.'),
            ('pptasaude', 'PPTA Saúde', 'October 16, 2024', 'Republication of the Saúde Business article.')
        ],
        'association_title': 'SBIS announcement',
        'association_text': 'The Brazilian Society of Health Informatics published an article by Marco A. Gutierrez about the award on October 8, 2024.',
        'association_link': 'Read the SBIS announcement',
        'sources_title': 'Paper and sources',
        'paper_link': 'Read the full paper (PDF)',
        'thesis_link': 'Doctoral thesis, including Appendix A on the challenge',
        'official_link': 'The 2024 challenge proposal and rules',
        'awards_link': 'Computing in Cardiology award winners'
    }
}

CHALLENGE_LINKS = {
    'saudebusiness': 'https://www.saudebusiness.com/artigos/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
    'itportal': 'https://itportal.com.br/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
    'pptasaude': 'https://www.pptasaude.com.br/noticias/21020/incor-ganha-premio-internacional-por-inovacao-em-diagnostico-de-arritmias-com-ia/',
    'paper': 'https://cinc.org/archives/2024/pdf/CinC2024-398.pdf',
    'thesis': 'https://doi.org/10.11606/T.3.2025.tde-16012026-084015',
    'official': 'https://moody-challenge.physionet.org/2024/',
    'ranking': 'https://moody-challenge.physionet.org/2024/results/official_scores_classification.tsv',
    'awards': 'https://cinc.org/physionet-cinc-challenge-awards/',
    'history': 'https://moody-challenge.physionet.org/index.html',
    'photo': 'https://sbis.org.br/equipe-do-laboratorio-de-informatica-biomedica-do-incor-hc-fmusp-e-premiada-no-george-b-moody-physionet-challenge-2024/'
}
