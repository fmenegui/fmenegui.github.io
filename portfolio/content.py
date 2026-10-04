LINKS = {'email': 'mailto:f.meneguittidias@gmail.com',
 'linkedin': 'https://www.linkedin.com/in/felipe-meneguitti-dias-312570b3/',
 'github': 'https://github.com/fmenegui',
 'scholar': 'https://scholar.google.com/citations?user=Xr5khtoAAAAJ',
 'orcid': 'https://orcid.org/0000-0001-7778-4606',
 'lattes': 'http://lattes.cnpq.br/3455258218368949',
 'map': 'https://www.openstreetmap.org/?mlat=-12.94539&mlon=-38.44634#map=17/-12.94539/-38.44634',
 'challenge': 'https://moody-challenge.physionet.org/2024/results/'}

PAPERS = [('2026',
  'Image-based deep learning for emergency electrocardiogram classification',
  'Dias FM et al.',
  'medRxiv · Preprint',
  '10.64898/2026.06.18.26355968'),
 ('2025',
  'Exploring the limitations of blood pressure estimation using the photoplethysmography signal',
  'Dias FM et al.',
  'Physiological Measurement',
  '10.1088/1361-6579/adcb86'),
 ('2024',
  'Image-Based Electrocardiogram Classification Using Pre-trained ConvNext',
  'Dias FM, Ribeiro E, Soares QB, Krieger JE, Gutierrez MA.',
  'Computing in Cardiology',
  '10.22489/CinC.2024.398'),
 ('2023',
  'Artificial Intelligence-Driven Screening System for Rapid Image-Based Classification of 12-Lead ECG Exams: A '
  'Promising Solution for Emergency Room Prioritization',
  'Dias FM et al.',
  'IEEE Access',
  '10.1109/ACCESS.2023.3328538'),
 ('2023',
  'Blood Pressure Estimation From Photoplethysmography by Considering Intra- and Inter-Subject Variabilities: '
  'Guidelines for a Fair Assessment',
  'da Silva Costa TB, Dias FM et al.',
  'IEEE Access',
  '10.1109/ACCESS.2023.3284458'),
 ('2021',
  'Arrhythmia classification from single-lead ECG signals using the inter-patient paradigm',
  'Dias FM et al.',
  'Computer Methods and Programs in Biomedicine',
  '10.1016/j.cmpb.2021.105948'),
 ('2023',
  'Quality Assessment of Photoplethysmography Signals For Cardiovascular Biomarkers Monitoring Using Wearable '
  'Devices',
  'Dias FM et al.',
  'arXiv · Preprint',
  '10.48550/arXiv.2307.08766'),
 ('2024',
  'Machine Learning-Based Diabetes Detection Using Photoplethysmography Signal Features',
  'Oliveira FAC, Dias FM et al.',
  'SBCAS',
  '10.5753/sbcas.2024.1889'),
 ('2025',
  'Enhancing Photoplethysmography-Based Sleep Staging Models Through Temporal Context Optimization',
  'Quino JAP, Cardenas DAC, Toledo MAF, Dias FM et al.',
  'Studies in Health Technology and Informatics',
  '10.3233/SHTI250897'),
 ('2022',
  'IoT Medical Device Architecture to Estimate Non-invasive Arterial Blood Pressure',
  'Moreno R, Dias F, Arruda M et al.',
  'Symposium on Internet of Things (SIoT)',
  '10.1109/SIOT56383.2022.10069878'),
 ('2025',
  'Classificação automatizada de imagens de eletrocardiogramas por aprendizado profundo',
  'Dias FM.',
  'Universidade de São Paulo · Tese de doutorado',
  '10.11606/T.3.2025.tde-16012026-084015')]

CONTENT = {'pt': {'locale': 'pt-BR',
        'name': 'Português',
        'nav': ['Projetos', 'Currículo', 'Publicações', 'Contato'],
        'role': 'Engenharia de IA · Pesquisa aplicada',
        'headline': 'Engenharia de IA aplicada à saúde',
        'intro': 'Sou especialista sênior de P&D na Samsung e doutor pela USP. Trabalho com inteligência '
                 'artificial aplicada à saúde, processamento de sinais e validação de modelos, do desenvolvimento '
                 'à implantação.',
        'bio': 'No InCor, desenvolvi pesquisa em classificação de ECGs e liderei a implantação do Gorgona em uma '
               'unidade de pronto atendimento em Salvador.',
        'download': 'Baixar portfólio',
        'see': 'Conhecer os projetos',
        'selected': 'Projetos selecionados',
        'read': 'Ver projeto',
        'back': 'Todos os projetos',
        'article': 'Ler artigo',
        'papers': 'Publicações selecionadas',
        'about': 'Currículo',
        'contact': 'Vamos conversar',
        'contact_text': 'Para oportunidades em engenharia de IA, ciência de dados e pesquisa aplicada à saúde.',
        'pdf_note': 'Uma versão para leitura e envio em candidaturas.',
        'portfolio': 'Portfólio profissional',
        'updated': 'Outubro de 2026',
        'gorgona': {'kicker': '01 / IA em serviço · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'Classificação de ECGs integrada ao atendimento de urgência',
                    'summary': 'Classificação de ECGs de UPAs, com envio ao InCor e alertas pelo Telegram em '
                               'paralelo à telemedicina. Liderei o projeto e o desenvolvimento inicial da '
                               'integração.',
                    'role': 'Liderança do projeto e desenvolvimento inicial do sistema',
                    'objective': 'Antecipar a identificação de ECGs com suspeita de corrente de lesão e comunicar '
                                 'esses exames à equipe de regulação. A análise automática ocorre em paralelo à '
                                 'telemedicina. A avaliação do paciente e a decisão assistencial permanecem com a '
                                 'equipe médica.',
                    'contribution': 'Conectei o modelo de classificação ao cliente Windows, ao processamento no '
                                    'InCor, ao painel web e ao envio de alertas. A equipe clínica conduziu o '
                                    'protocolo assistencial e a avaliação dos exames.',
                    'metrics': [('42.037', 'registros processados'),
                                ('2 min', 'do ECG ao alerta, no caso'),
                                ('41 min', 'antes do primeiro laudo')],
                    'count_note': 'Consulta de 03/10/2026: todas as unidades, período completo, status '
                                  'Processado, classes Corrente de Lesão e Outros. A contagem corresponde a '
                                  'registros de exames, não a pacientes únicos.',
                    'location': 'A implantação apresentada ocorreu na UPA Rodrigo Argolo, em Tancredo Neves, '
                                'Salvador. A unidade realiza os ECGs, e o servidor do InCor concentra a execução '
                                'do modelo.',
                    'map_caption': 'Localização cadastral aproximada. Rua Pernambuco, s/n, Salvador. CNES '
                                   '7033850. Base: © OpenStreetMap contributors. Endereço: CNES/DATASUS. '
                                   'Coordenadas: SaúdeNoPais.',
                    'before': 'O ECG era enviado manualmente à telemedicina. O laudo e a avaliação médica '
                              'orientavam o acionamento do grupo de regulação no Telegram. O médico da UPA também '
                              'podia acionar o grupo diretamente diante de forte suspeita.',
                    'after': 'Acrescentamos uma via automática. O cliente detecta o arquivo, prepara o envio ao '
                             'InCor e o servidor executa o modelo. Quando a probabilidade de Corrente de Lesão '
                             'supera 50%, o sistema envia um alerta ao grupo configurado.',
                    'flow_rows': [('Coleta', 'Envio manual à telemedicina', 'Detecção na pasta de exames'),
                                  ('Análise', 'Avaliação médica e laudo', 'Classificação adicional por IA'),
                                  ('Comunicação', 'Acionamento pela equipe', 'Alerta automático pelo Telegram'),
                                  ('Decisão', 'Equipe médica e regulação', 'Equipe médica e regulação')],
                    'client': 'O ECG-IA Client acompanha a pasta de exames no Windows e coloca novos arquivos em '
                              'uma fila local de envio. Cada instalação utiliza uma credencial própria. O menu na '
                              'bandeja permite configurar, reiniciar e reprocessar a pasta.',
                    'server': 'Uma API FastAPI recebe o exame, extrai metadados e converte o traçado em imagem '
                              'quando necessário. Classes e probabilidades são armazenadas em SQLite. O painel '
                              'permite consultar resultados e acompanhar clientes, enquanto a integração com '
                              'Telegram encaminha os alertas.',
                    'privacy': 'A proposta prevê anonimização no computador da UPA antes da transmissão. O '
                               'recurso é configurável no cliente. HTTPS, autenticação por instalação e perfis de '
                               'acesso complementam o tratamento local dos arquivos. Essas medidas descrevem a '
                               'proteção técnica dos dados, sem constituir uma avaliação formal de conformidade '
                               'integral com a LGPD.',
                    'dashboard': 'A plataforma online permite filtrar por unidade, período, status e classe. A '
                                 'tela abaixo mostra a consulta à classe Corrente de Lesão entre 02/10 e '
                                 '03/10/2026, diferente do filtro usado para a contagem de 42.037 registros.',
                    'case': 'Em 20 de maio de 2026, um atendimento na UPA Rodrigo Argolo permitiu acompanhar o '
                            'fluxo completo. A admissão ocorreu às 18h52. Os dois ECGs geraram alertas '
                            'automáticos 2 minutos após sua realização. A chegada ao centro de referência foi '
                            'registrada às 20h44.',
                    'timeline_caption': 'Trecho da linha do tempo original do estudo de caso, slide 23. O recorte '
                                        'omite o bloco de identificação pessoal e começa no primeiro ECG. '
                                        'Admissão: 18h52.',
                    'case_rows': [('Realização do ECG', '19h15', '19h37'),
                                  ('Alerta da IA', '19h17', '19h39'),
                                  ('Chegada à telemedicina', '19h21', '19h39'),
                                  ('Emissão do laudo', '19h58', '20h04'),
                                  ('Do exame ao alerta', '2 min', '2 min'),
                                  ('Antecedência em relação ao laudo', '41 min', '25 min')],
                    'case_result': 'O primeiro alerta chegou 4 minutos antes de o ECG entrar na telemedicina. A '
                                   'antecedência em relação aos laudos foi de 41 e 25 minutos. O caso demonstra a '
                                   'antecipação da informação à regulação. Não permite atribuir à IA uma redução '
                                   'no tempo até o tratamento ou nos desfechos clínicos.',
                    'model': 'O modelo de emergência usa um ensemble ConvNeXt para 12 categorias. O estudo inclui '
                             '18.519 ECGs de 14.402 pacientes, com anotação de 19 cardiologistas. No teste '
                             'reservado, o macro F1 foi de 0,807 (IC 95%: 0,788 a 0,825). Esses números descrevem '
                             'a pesquisa do classificador, separadamente do volume processado em serviço.',
                    'period': '2026',
                    'foundation': 'O modelo da equipe AIMED, vencedor da tarefa de classificação do George B. '
                                  'Moody PhysioNet Challenge 2024, serviu de base para o desenvolvimento do '
                                  'classificador utilizado no Gorgona. O artigo do Computing in Cardiology (CinC) '
                                  '2024 descreve a abordagem com ConvNeXt, pré-treinamento em imagens de ECG e '
                                  'ensemble de modelos. Minha tese de doutorado documenta a construção dos bancos '
                                  'de imagens, as estratégias de treinamento e a avaliação clínica dessa linha de '
                                  'pesquisa.',
                    'foundation_short': 'O classificador foi desenvolvido a partir do modelo da equipe AIMED '
                                        'vencedor da tarefa de classificação do PhysioNet Challenge 2024. O '
                                        'artigo do CinC 2024 e minha tese documentam essa base científica.',
                    'evidence': '42.037 registros processados na plataforma, na consulta de 03/10/2026.',
                    'decisions': [('Integração ao atendimento',
                                   'A análise automática funciona em paralelo à telemedicina. O alerta acrescenta '
                                   'uma via de comunicação à regulação, mantendo a avaliação e a decisão com a '
                                   'equipe médica.'),
                                  ('Cliente e servidor',
                                   'O cliente Windows monitora a pasta de exames e mantém uma fila de envio. A '
                                   'inferência fica no servidor do InCor. O menu local permite reiniciar o '
                                   'cliente e reprocessar arquivos.'),
                                  ('Dados e acesso',
                                   'Anonimização local configurável, HTTPS e credenciais por instalação compõem '
                                   'os controles técnicos. A existência desses recursos não substitui uma '
                                   'avaliação de conformidade com a LGPD.')],
                    'status': 'Implantação em UPA'},
        'incor': {'kicker': '02 / Integração hospitalar · InCor · 2023–2026',
                  'title': 'ECG na emergência do InCor',
                  'subtitle': 'Do PACS à tela da equipe médica',
                  'summary': 'Classificação de ECGs integrada ao PACS e à aplicação da emergência. Desenvolvi '
                             'modelos, coordenei a anotação clínica e participei da implantação e avaliação.',
                  'role': 'Desenvolvimento de modelos, coordenação da anotação e integração clínica',
                  'objective': 'Apoiar a priorização da revisão médica dos ECGs na emergência, levando a '
                               'classificação automática ao ambiente de trabalho da equipe assistencial.',
                  'method': 'Na arquitetura publicada em 2023, o ECG de 12 derivações é armazenado em formato '
                            'DICOM no PACS, o sistema hospitalar de imagens. O módulo de IA acessa o exame, '
                            'pré-processa a imagem e executa uma rede neural convolucional. A figura inclui '
                            'idade, sexo e etnia como entradas do classificador.',
                  'result': 'A arquitetura de 2023 apresenta três classes: fibrilação atrial, outros e normal. A '
                            'linha de pesquisa evoluiu para um ensemble ConvNeXt com 12 categorias. O estudo de '
                            '2026 reúne 18.519 ECGs de 14.402 pacientes e obteve macro F1 de 0,807 no teste '
                            'reservado (IC 95%: 0,788 a 0,825).',
                  'scope': 'A implantação incluiu avaliação por cardiologista e comparação com especialistas. O '
                           'tamanho da base de pesquisa não representa o volume de exames processados em rotina.',
                  'caption': 'Figura 1 do artigo de Dias et al., IEEE Access (2023). Integração proposta entre '
                             'aquisição do ECG, DICOM/PACS, classificador e aplicação web na emergência. Imagem '
                             'fornecida pelo autor.',
                  'workflow': [('Aquisição e armazenamento', 'ECG de 12 derivações em DICOM, armazenado no PACS.'),
                               ('Processamento', 'Pré-processamento da imagem e classificação por uma CNN.'),
                               ('Resultado', 'Fibrilação atrial, outros ou normal.'),
                               ('Uso pela equipe',
                                'Resultados na aplicação web da emergência para apoiar a priorização da revisão '
                                'médica.')],
                  'period': '2023–2026',
                  'contribution': 'Desenvolvi e implantei modelos de classificação de ECGs na emergência. '
                                  'Coordenei a anotação de aproximadamente 20 mil exames por 19 cardiologistas, '
                                  'com definição de classes, adjudicação e análise de concordância, além da '
                                  'avaliação pós-implantação e da comparação com especialistas.',
                  'evidence': 'Cerca de 20 mil ECGs na iniciativa de anotação com 19 cardiologistas.',
                  'decisions': [('Integração hospitalar',
                                 'A arquitetura utiliza os exames DICOM armazenados no PACS e apresenta a '
                                 'classificação na aplicação da emergência, dentro do fluxo de revisão clínica.'),
                                ('Referência clínica',
                                 'A coordenação da anotação incluiu definição de classes, adjudicação de '
                                 'divergências e análise de concordância entre cardiologistas.'),
                                ('Versões e avaliação',
                                 'A arquitetura de 2023 usa três classes. A pesquisa de 2026 avalia 12 '
                                 'categorias. Os resultados dessa pesquisa não medem volume assistencial nem '
                                 'desempenho de todas as versões implantadas.')],
                  'status': 'Integração hospitalar'},
        'physionet': {'kicker': '02 / Classificação de imagens · 2024',
                      'title': 'PhysioNet Challenge',
                      'subtitle': 'Primeiro lugar em classificação de ECGs',
                      'summary': 'Integrei a equipe AIMED, vencedora da tarefa de classificação do George B. '
                                 'Moody PhysioNet Challenge 2024, com macro F1 de 0,817 no teste oculto reportado '
                                 'no artigo.',
                      'role': 'Integrante da equipe AIMED e primeiro autor do artigo',
                      'method': 'Usamos ConvNeXt com pré-treinamento em imagens de ECG, ajuste no PTB-XL e um '
                                'ensemble de cinco modelos. O trabalho avaliou a classificação de 11 categorias '
                                'diretamente nas imagens.',
                      'result': 'A participação reuniu treinamento, avaliação em dados ocultos e análise de '
                                'diferentes condições de aquisição. O prêmio se refere à tarefa de classificação, '
                                'conduzida separadamente da digitalização dos traçados.',
                      'team': 'Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger e Marco A. '
                              'Gutierrez.'},
        'rpms': {'kicker': '03 / Monitoramento remoto · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': 'Monitoramento remoto com relógios, processamento de PPG no celular e painel médico. '
                            'Desenvolvi protocolos de coleta, pré-processamento e algoritmos com a equipe.',
                 'role': 'Protocolos de coleta, processamento de sinais e desenvolvimento de algoritmos',
                 'objective': 'Permitir o acompanhamento de pacientes fora do hospital, conectando sinais '
                              'coletados por dispositivos vestíveis a biomarcadores disponíveis para a equipe '
                              'médica.',
                 'contribution': 'Minha atuação reuniu protocolos de coleta com relógios protótipos, organização '
                                 'dos dados, pré-processamento de sinais de fotopletismografia (PPG) e '
                                 'desenvolvimento de algoritmos em equipe.',
                 'method': 'O relógio envia o PPG ao aplicativo Android por Bluetooth Low Energy. O celular '
                           'processa o sinal, estima pressão arterial e frequência cardíaca e envia os resultados '
                           'por MQTT ao servidor ThingsBoard. O painel permite acompanhar as medidas de cada '
                           'paciente ao longo do tempo.',
                 'research': 'A pesquisa do RPMS abrange qualidade do sinal, estimativa de pressão arterial, '
                             'classificação relacionada ao diabetes e análise do sono. Os artigos documentam '
                             'essas frentes. A arquitetura de 2022 demonstrada acima integra estimativas de '
                             'pressão arterial e frequência cardíaca.',
                 'caption': 'Arquitetura publicada em Moreno, Dias et al. (SIoT, 2022), Figura 1. O processamento '
                            'ocorre no celular.',
                 'biomarkers': [('Qualidade do sinal',
                                 'Avaliação automática da qualidade dos segmentos de PPG.',
                                 6),
                                ('Pressão arterial',
                                 'Estimativa com calibração e avaliação dos limites de generalização.',
                                 1),
                                ('Diabetes', 'Classificação a partir de características do PPG e metadados.', 7),
                                ('Sono', 'Classificação de estágios do sono com contexto temporal.', 8)],
                 'period': '2022–2026',
                 'evidence': '52 voluntários e 15 pulseiras na versão publicada em 2022.',
                 'decisions': [('Processamento no celular',
                                'O relógio envia PPG por Bluetooth Low Energy. O celular estima pressão e '
                                'frequência cardíaca e transmite os resultados ao servidor, reduzindo o volume '
                                'enviado em relação aos sinais brutos.'),
                               ('Protocolo de coleta',
                                'O protocolo publicado intercala três registros de PPG com medidas de pressão por '
                                'manguito, após repouso. Isso cria pares de sinal e referência para avaliar os '
                                'estimadores.'),
                               ('Validação por participante',
                                'As partições de validação separam participantes. Essa escolha permite avaliar '
                                'generalização para pessoas diferentes das usadas no treinamento.')],
                 'status': 'Protótipo e pesquisa'},
        'education': [('2021–2025', 'Doutorado em Engenharia Biomédica', 'Universidade de São Paulo'),
                      ('2018–2020', 'Mestrado em Engenharia Elétrica', 'Universidade Federal de Juiz de Fora'),
                      ('2015–2016',
                       'Intercâmbio em Engenharia Elétrica',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017', 'Graduação em Engenharia Eletrônica', 'Universidade Federal de Juiz de Fora')],
        'experience': 'Minha experiência no InCor reúne pesquisa em sinais biomédicos, desenvolvimento de modelos '
                      'para ECG e implantação de software em ambientes assistenciais. Gorgona, ECG na emergência '
                      'e RPMS representam essas frentes neste portfólio.',
        'skills': [('IA e dados',
                    'Machine learning, deep learning, LLMs, visão computacional, processamento de sinais, análise '
                    'de dados e validação de modelos.'),
                   ('Tecnologias', 'Python, PyTorch, TensorFlow/Keras, scikit-learn, MATLAB, Git e Linux.'),
                   ('Sistemas',
                    'FastAPI, Docker, SQLite, integração com Telegram, aplicativos móveis e painéis de '
                    'monitoramento.'),
                   ('Saúde digital',
                    'ECG, PPG, wearables, dados clínicos, apoio à decisão, monitoramento remoto, anonimização e '
                    'requisitos de LGPD.')],
        'labels': {'objective': 'Objetivo',
                   'contribution': 'Responsabilidade no projeto',
                   'location': 'Local da implantação',
                   'workflow': 'Do fluxo anterior à proposta',
                   'before': 'Fluxo anterior',
                   'after': 'Com o Gorgona',
                   'client': 'O programa na UPA',
                   'server': 'Servidor e plataforma online',
                   'privacy': 'Proteção de dados e LGPD',
                   'case': 'Estudo de caso',
                   'model': 'Base científica do modelo',
                   'method': 'Abordagem',
                   'result': 'Resultados e avaliação',
                   'team': 'Equipe',
                   'education': 'Formação',
                   'experience': 'Experiência',
                   'skills': 'Competências aplicadas',
                   'refs': 'Artigos de referência',
                   'step': 'Etapa',
                   'event': 'Evento',
                   'first': 'Primeiro ECG',
                   'second': 'Segundo ECG',
                   'openmap': 'Abrir mapa',
                   'official': 'Resultados oficiais',
                   'home': 'Início',
                   'skip': 'Ir para o conteúdo',
                   'how': 'Como funciona'},
        'professional_title': 'Engenharia de IA aplicada à saúde',
        'cv_summary': 'Especialista sênior de P&D na Samsung, com doutorado pela USP. No InCor, liderei a '
                      'integração de classificação de ECGs ao fluxo de UPAs e coordenei a anotação de cerca de 20 '
                      'mil exames por 19 cardiologistas. Minha experiência reúne desenvolvimento de modelos, '
                      'integração de software, protocolos de dados e avaliação clínica.',
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–atual',
                  'Especialista de P&D Sênior',
                  'Campinas, SP',
                  ['Pesquisa, implementação e avaliação quantitativa de soluções de software e IA em P&D '
                   'industrial, com foco em robustez e aplicação em produto.']),
                 ('Instituto do Coração (InCor), HCFMUSP',
                  '2020–2026',
                  'Pesquisador / Analista de Sistemas Sênior, IA aplicada à saúde',
                  'São Paulo, SP',
                  ['Coordenação da anotação de aproximadamente 20 mil ECGs por 19 cardiologistas, incluindo '
                   'classes, fluxo de anotação, adjudicação e análise de concordância.',
                   'Liderança do projeto e desenvolvimento inicial do Gorgona para ECGs de UPAs de Salvador, com '
                   'anonimização configurável e alertas para suspeita de IAM com supradesnivelamento de ST. No '
                   'caso documentado, dois ECGs geraram alertas em 2 minutos. A plataforma contabilizava 42.037 '
                   'registros processados na consulta de 03/10/2026, considerando todas as unidades.',
                   'Desenvolvimento e implantação do classificador na emergência do InCor, com avaliação '
                   'pós-implantação por cardiologista e comparação com especialistas.',
                   'Desenvolvimento de monitoramento remoto com wearables, processamento de PPG e estimativa de '
                   'sinais fisiológicos para acompanhamento longitudinal. Atuação em protocolos de coleta, '
                   'pré-processamento e desenvolvimento de algoritmos com a equipe.',
                   'Desenvolvimento e avaliação de LLMs para anonimização de textos clínicos em português, '
                   'incluindo base anotada, comparação de modelos e execução local para proteção de dados.'])],
        'awards': [('2024',
                    '1º lugar na tarefa de classificação do George B. Moody PhysioNet Challenge, como integrante '
                    'da equipe AIMED.'),
                   ('2015', 'Bolsa Ciência sem Fronteiras, CAPES.'),
                   ('2011', 'Medalha de Bronze, Olimpíada Brasileira de Física (OBF).')]},
 'en': {'locale': 'en',
        'name': 'English',
        'nav': ['Projects', 'CV', 'Publications', 'Contact'],
        'role': 'AI engineering · Applied research',
        'headline': 'AI engineering for healthcare',
        'intro': 'I am a Senior R&D Specialist at Samsung with a PhD from the University of São Paulo. My work '
                 'spans healthcare AI, signal processing and model validation, from development to deployment.',
        'bio': 'At InCor, I developed research on ECG classification and led the deployment of Gorgona at an '
               'urgent care unit in Salvador, Brazil.',
        'download': 'Download portfolio',
        'see': 'Explore my projects',
        'selected': 'Selected projects',
        'read': 'View project',
        'back': 'All projects',
        'article': 'Read paper',
        'papers': 'Selected publications',
        'about': 'CV',
        'contact': 'Get in touch',
        'contact_text': 'For opportunities in AI engineering, data science and applied healthcare research.',
        'pdf_note': 'A standalone portfolio for applications and sharing.',
        'portfolio': 'Professional portfolio',
        'updated': 'October 2026',
        'gorgona': {'kicker': '01 / Deployed AI · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'ECG classification integrated into urgent care',
                    'summary': 'ECG classification for urgent care units, with processing at InCor and Telegram '
                               'alerts alongside telemedicine. I led the project and the initial integration '
                               'work.',
                    'role': 'Project leadership and initial system development',
                    'objective': 'Flag ECGs with suspected current of injury and notify the clinical coordination '
                                 'team earlier. Automated analysis runs alongside the telemedicine workflow. '
                                 'Patient assessment and care decisions remain with the medical team.',
                    'contribution': 'I connected the classification model to the Windows client, InCor processing '
                                    'server, web dashboard and Telegram alerts. The clinical team managed the '
                                    'care protocol and reviewed the ECGs.',
                    'metrics': [('42,037', 'processed records'),
                                ('2 min', 'ECG to alert in the case'),
                                ('41 min', 'before the first report')],
                    'count_note': 'Dashboard query on October 3, 2026: all units, full period, Processed status, '
                                  'Current of Injury and Other classes. The count represents examination records, '
                                  'not unique patients.',
                    'location': 'The deployment presented here took place at UPA Rodrigo Argolo, an urgent care '
                                'unit in Tancredo Neves, Salvador, Brazil. ECGs are acquired at the unit and the '
                                'model runs remotely on the InCor server.',
                    'map_caption': 'Approximate registry location. Rua Pernambuco, s/n, Salvador. CNES 7033850. '
                                   'Map: © OpenStreetMap contributors. Address: CNES/DATASUS. Coordinates: '
                                   'SaúdeNoPais.',
                    'before': 'ECGs were manually sent to telemedicine. The report and medical assessment '
                              'informed whether to contact the coordination group on Telegram. The physician '
                              'could also contact the group directly when clinical suspicion was high.',
                    'after': 'We added an automated path. The client detects the file, prepares the upload and '
                             'sends it to InCor for classification. When the probability of the Current of Injury '
                             'class exceeds 50%, the system sends an alert to the configured group.',
                    'flow_rows': [('Collection', 'Manual telemedicine submission', 'Automatic folder monitoring'),
                                  ('Analysis', 'Medical review and report', 'Additional AI classification'),
                                  ('Communication', 'Staff-initiated contact', 'Automated Telegram alert'),
                                  ('Decision',
                                   'Medical and coordination teams',
                                   'Medical and coordination teams')],
                    'client': 'The ECG-IA Client monitors an examination folder on Windows and queues new files '
                              'for upload. Each installation has its own credential. A system tray menu provides '
                              'configuration, restart and folder reprocessing controls.',
                    'server': 'A FastAPI endpoint receives the examination, extracts metadata and converts the '
                              'tracing into an image when needed. Classes and probabilities are stored in SQLite. '
                              'The dashboard supports result queries and client monitoring, while the Telegram '
                              'integration delivers alerts.',
                    'privacy': 'The proposed workflow includes anonymization on the unit’s computer before '
                               'transmission. This feature is configurable in the client. HTTPS, per-installation '
                               'authentication and access roles complement local file processing. These are '
                               'technical data protection measures, not a formal assessment of full compliance '
                               'with Brazil’s LGPD.',
                    'dashboard': 'The online platform supports filtering by unit, period, status and class. This '
                                 'screenshot shows the Current of Injury query for October 2–3, 2026, which '
                                 'differs from the query used for the 42,037-record count.',
                    'case': 'On May 20, 2026, one encounter at UPA Rodrigo Argolo provided a complete record of '
                            'the alert workflow. Admission was at 18:52. Both ECGs triggered automated alerts 2 '
                            'minutes after acquisition. Arrival at the referral center was recorded at 20:44.',
                    'timeline_caption': 'Excerpt from the original case-study timeline, slide 23. The crop '
                                        'excludes the personal identification block and starts at the first ECG. '
                                        'Admission: 18:52. Original figure in Portuguese.',
                    'case_rows': [('ECG acquisition', '19:15', '19:37'),
                                  ('AI alert', '19:17', '19:39'),
                                  ('Arrival at telemedicine', '19:21', '19:39'),
                                  ('Report issued', '19:58', '20:04'),
                                  ('ECG to alert', '2 min', '2 min'),
                                  ('Lead time before report', '41 min', '25 min')],
                    'case_result': 'The first alert arrived 4 minutes before the ECG reached telemedicine. Alerts '
                                   'preceded the corresponding reports by 41 and 25 minutes. The case '
                                   'demonstrates earlier information delivery to the coordination team. It does '
                                   'not establish a causal reduction in treatment time or improved clinical '
                                   'outcomes.',
                    'model': 'The emergency model uses a ConvNeXt ensemble for 12 categories. The study includes '
                             '18,519 ECGs from 14,402 patients, annotated by 19 cardiologists. Held-out macro F1 '
                             'was 0.807 (95% CI: 0.788–0.825). These figures describe the classifier study, '
                             'separately from operational processing volume.',
                    'period': '2026',
                    'foundation': 'The AIMED model that won the classification task of the 2024 George B. Moody '
                                  'PhysioNet Challenge served as the foundation for developing the classifier '
                                  'used in Gorgona. The Computing in Cardiology (CinC) 2024 paper describes the '
                                  'ConvNeXt approach, ECG image pretraining and model ensemble. My doctoral '
                                  'thesis documents the image datasets, training strategies and clinical '
                                  'evaluation behind this research.',
                    'foundation_short': 'The classifier was developed from the AIMED model that won the 2024 '
                                        'PhysioNet Challenge classification task. The CinC 2024 paper and my '
                                        'doctoral thesis document this foundation.',
                    'evidence': '42,037 records processed across the platform, as queried on October 3, 2026.',
                    'decisions': [('Clinical workflow',
                                   'Automated analysis runs alongside telemedicine. Alerts add a communication '
                                   'route to the clinical coordination team, while assessment and care decisions '
                                   'remain with clinicians.'),
                                  ('Client and server',
                                   'The Windows client monitors the examination folder and queues uploads. '
                                   'Inference runs on the InCor server. Local controls allow staff to restart the '
                                   'client and reprocess files.'),
                                  ('Data and access',
                                   'Configurable local anonymization, HTTPS and per-installation credentials form '
                                   'the technical controls. These features do not replace an assessment of '
                                   'compliance with Brazil’s LGPD.')],
                    'status': 'Urgent care deployment'},
        'incor': {'kicker': '02 / Hospital integration · InCor · 2023–2026',
                  'title': 'ECG classification at InCor',
                  'subtitle': 'From PACS to the emergency room screen',
                  'summary': 'ECG classification integrated with PACS and the emergency department application. I '
                             'developed models, coordinated clinical annotation and worked on deployment and '
                             'evaluation.',
                  'role': 'Model development, annotation coordination and clinical integration',
                  'objective': 'Support the prioritization of ECG review in the emergency room by bringing '
                               'automated classification into the clinical team’s workspace.',
                  'method': 'In the architecture published in 2023, the 12-lead ECG is stored in DICOM format in '
                            'the hospital’s picture archiving and communication system (PACS). The AI module '
                            'retrieves the examination, preprocesses the image and runs a convolutional neural '
                            'network. The figure includes age, sex and ethnicity as classifier inputs.',
                  'result': 'The 2023 architecture uses three classes: atrial fibrillation, other and normal. '
                            'Subsequent research developed a ConvNeXt ensemble for 12 categories. The 2026 study '
                            'includes 18,519 ECGs from 14,402 patients and achieved a macro F1 of 0.807 on the '
                            'held-out test set (95% CI: 0.788–0.825).',
                  'scope': 'Deployment included cardiologist review and comparison with specialists. The research '
                           'dataset size does not represent routine clinical processing volume.',
                  'caption': 'Figure 1 from Dias et al., IEEE Access (2023). Proposed integration of ECG '
                             'acquisition, DICOM/PACS, classification and the emergency room web application. '
                             'Image provided by the author.',
                  'workflow': [('Acquisition and storage', '12-lead ECG in DICOM format, stored in PACS.'),
                               ('Processing', 'Image preprocessing and classification by a CNN.'),
                               ('Output', 'Atrial fibrillation, other or normal.'),
                               ('Clinical use',
                                'Results in the emergency room web application to support prioritization of '
                                'medical review.')],
                  'period': '2023–2026',
                  'contribution': 'I developed and deployed ECG classification models in emergency care. I '
                                  'coordinated the annotation of approximately 20,000 examinations by 19 '
                                  'cardiologists, covering class definitions, adjudication and agreement '
                                  'analysis, as well as post-deployment evaluation and comparison with '
                                  'specialists.',
                  'evidence': 'Around 20,000 ECGs in the annotation initiative with 19 cardiologists.',
                  'decisions': [('Hospital integration',
                                 'The architecture uses DICOM examinations stored in PACS and displays '
                                 'classifications in the emergency department application as part of clinical '
                                 'review.'),
                                ('Clinical reference',
                                 'Annotation coordination covered class definitions, adjudication of '
                                 'disagreements and analysis of agreement between cardiologists.'),
                                ('Versions and evaluation',
                                 'The 2023 architecture uses three classes. The 2026 research evaluates 12 '
                                 'categories. Those research results do not measure clinical processing volume or '
                                 'the performance of every deployed version.')],
                  'status': 'Hospital integration'},
        'physionet': {'kicker': '02 / Image classification · 2024',
                      'title': 'PhysioNet Challenge',
                      'subtitle': 'First place in ECG classification',
                      'summary': 'I contributed to AIMED, the winning team in the classification task of the 2024 '
                                 'George B. Moody PhysioNet Challenge, with a hidden-test macro F1 of 0.817 '
                                 'reported in our paper.',
                      'role': 'AIMED team member and first author of the paper',
                      'method': 'We used ConvNeXt pretrained on ECG images, fine-tuned on PTB-XL, with a '
                                'five-model ensemble. The work evaluated classification of 11 categories directly '
                                'from images.',
                      'result': 'The entry combined model training, hidden-data evaluation and analysis across '
                                'image acquisition conditions. The award was for classification, a separate task '
                                'from ECG waveform digitization.',
                      'team': 'Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger and Marco A. '
                              'Gutierrez.'},
        'rpms': {'kicker': '03 / Remote monitoring · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': 'Remote monitoring with watches, phone-based PPG processing and a clinical dashboard. '
                            'I developed collection protocols, preprocessing and algorithms with the team.',
                 'role': 'Data collection protocols, signal processing and algorithm development',
                 'objective': 'Support patient follow-up outside the hospital by connecting wearable recordings '
                              'to biomarkers available to the clinical team.',
                 'contribution': 'My work covered collection protocols with prototype watches, data organization, '
                                 'photoplethysmography (PPG) preprocessing and collaborative algorithm '
                                 'development.',
                 'method': 'The watch sends PPG to the Android app over Bluetooth Low Energy. The phone processes '
                           'the signal, estimates blood pressure and heart rate, and sends results over MQTT to a '
                           'ThingsBoard server. The dashboard displays each patient’s measurements over time.',
                 'research': 'RPMS research covers signal quality, blood pressure estimation, diabetes-related '
                             'classification and sleep analysis. The papers document these areas. The 2022 '
                             'architecture shown above integrates blood pressure and heart rate estimates.',
                 'caption': 'Architecture published in Moreno, Dias et al. (SIoT, 2022), Figure 1. Signals are '
                            'processed on the phone.',
                 'biomarkers': [('Signal quality', 'Automated assessment of PPG segment quality.', 6),
                                ('Blood pressure',
                                 'Calibrated estimation and evaluation of generalization limits.',
                                 1),
                                ('Diabetes', 'Classification using PPG features and patient metadata.', 7),
                                ('Sleep', 'Sleep stage classification using temporal context.', 8)],
                 'period': '2022–2026',
                 'evidence': '52 volunteers and 15 wristbands in the version published in 2022.',
                 'decisions': [('Phone-based processing',
                                'The watch sends PPG over Bluetooth Low Energy. The phone estimates blood '
                                'pressure and heart rate and transmits results to the server, reducing '
                                'transmitted data volume compared with raw signals.'),
                               ('Collection protocol',
                                'The published protocol interleaves three PPG recordings with cuff blood pressure '
                                'measurements after rest. This creates signal and reference pairs for estimator '
                                'evaluation.'),
                               ('Participant-level validation',
                                'Validation folds keep participants separate. This evaluates generalization to '
                                'people who were not used for training.')],
                 'status': 'Prototype and research'},
        'education': [('2021–2025', 'PhD in Biomedical Engineering', 'University of São Paulo'),
                      ('2018–2020', 'MSc in Electrical Engineering', 'Federal University of Juiz de Fora'),
                      ('2015–2016',
                       'Exchange program in Electrical Engineering',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017', 'BSc in Electronic Engineering', 'Federal University of Juiz de Fora')],
        'experience': 'My experience at InCor spans biomedical signal research, ECG model development and '
                      'software deployment in healthcare settings. Gorgona brings these areas together in this '
                      'portfolio.',
        'skills': [('AI and data',
                    'Machine learning, deep learning, LLMs, computer vision, signal processing, data analysis and '
                    'model validation.'),
                   ('Technologies', 'Python, PyTorch, TensorFlow/Keras, scikit-learn, MATLAB, Git and Linux.'),
                   ('Systems',
                    'FastAPI, Docker, SQLite, Telegram integration, mobile apps and monitoring dashboards.'),
                   ('Digital health',
                    'ECG, PPG, wearables, clinical data, decision support, remote monitoring, anonymization and '
                    'LGPD requirements.')],
        'labels': {'objective': 'Objective',
                   'contribution': 'Project responsibility',
                   'location': 'Deployment location',
                   'workflow': 'From the previous workflow to the proposal',
                   'before': 'Previous workflow',
                   'after': 'With Gorgona',
                   'client': 'The application at the unit',
                   'server': 'Server and online platform',
                   'privacy': 'Data protection and LGPD',
                   'case': 'Case study',
                   'model': 'Scientific basis',
                   'method': 'Approach',
                   'result': 'Results and evaluation',
                   'team': 'Team',
                   'education': 'Education',
                   'experience': 'Experience',
                   'skills': 'Applied skills',
                   'refs': 'Research references',
                   'step': 'Stage',
                   'event': 'Event',
                   'first': 'First ECG',
                   'second': 'Second ECG',
                   'openmap': 'Open map',
                   'official': 'Official results',
                   'home': 'Home',
                   'skip': 'Skip to content',
                   'how': 'How it works'},
        'professional_title': 'AI engineering for healthcare',
        'cv_summary': 'Senior R&D Specialist at Samsung with a PhD from the University of São Paulo. At InCor, I '
                      'led the integration of ECG classification into urgent care workflows and coordinated the '
                      'annotation of around 20,000 examinations by 19 cardiologists. My experience covers model '
                      'development, software integration, data protocols and clinical evaluation.',
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–present',
                  'Senior R&D Specialist',
                  'Campinas, Brazil',
                  ['Research, implementation and quantitative evaluation of software and AI solutions in '
                   'industrial R&D, with a focus on robustness and product applications.']),
                 ('Heart Institute (InCor), HCFMUSP',
                  '2020–2026',
                  'Researcher / Senior Systems Analyst, Healthcare AI',
                  'São Paulo, Brazil',
                  ['Coordination of approximately 20,000 ECG annotations by 19 cardiologists, including class '
                   'definitions, annotation workflows, adjudication and agreement analysis.',
                   'Project leadership and initial development of Gorgona for ECGs from urgent care units in '
                   'Salvador, with configurable anonymization and alerts for suspected ST-elevation myocardial '
                   'infarction. In the documented case, two ECGs triggered alerts in 2 minutes. The platform had '
                   '42,037 processed records across all units in the October 3, 2026 query.',
                   'Development and deployment of the InCor emergency ECG classifier, including post-deployment '
                   'review by a cardiologist and comparison with specialists.',
                   'Development of wearable-based remote monitoring, PPG processing and physiological estimates '
                   'for longitudinal follow-up. Work included collection protocols, preprocessing and '
                   'collaborative algorithm development.',
                   'Development and evaluation of LLMs for anonymizing Portuguese clinical text, including an '
                   'annotated dataset, model benchmarking and local execution to protect patient data.'])],
        'awards': [('2024',
                    'First place in the classification task of the George B. Moody PhysioNet Challenge, as a '
                    'member of team AIMED.'),
                   ('2015', 'Science without Borders scholarship, CAPES.'),
                   ('2011', 'Bronze Medal, Brazilian Physics Olympiad (OBF).')]}}
