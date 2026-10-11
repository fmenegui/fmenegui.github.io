from challenge import CHALLENGE

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
  'Artificial Intelligence-Driven Screening System for Rapid Image-Based Classification of 12-Lead '
  'ECG Exams: A Promising Solution for Emergency Room Prioritization',
  'Dias FM et al.',
  'IEEE Access',
  '10.1109/ACCESS.2023.3328538'),
 ('2023',
  'Blood Pressure Estimation From Photoplethysmography by Considering Intra- and Inter-Subject '
  'Variabilities: Guidelines for a Fair Assessment',
  'da Silva Costa TB, Dias FM et al.',
  'IEEE Access',
  '10.1109/ACCESS.2023.3284458'),
 ('2021',
  'Arrhythmia classification from single-lead ECG signals using the inter-patient paradigm',
  'Dias FM et al.',
  'Computer Methods and Programs in Biomedicine',
  '10.1016/j.cmpb.2021.105948'),
 ('2023',
  'Quality Assessment of Photoplethysmography Signals For Cardiovascular Biomarkers Monitoring '
  'Using Wearable Devices',
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
        'intro': 'Sou especialista sênior de P&D na Samsung e doutor pela USP. Trabalho com '
                 'inteligência artificial aplicada à saúde, processamento de sinais e validação de '
                 'modelos, do desenvolvimento à implantação.',
        'bio': 'No InCor, pesquisei a classificação de ECGs por imagem e liderei a implantação do '
               'Gorgona em uma UPA de Salvador.',
        'download': 'Portfólio',
        'see': 'Conhecer os projetos',
        'selected': 'Alguns trabalhos',
        'location': 'São Paulo, Brasil',
        'read': 'Ver projeto',
        'back': 'Todos os projetos',
        'article': 'Ler artigo',
        'papers': 'Publicações selecionadas',
        'about': 'Currículo',
        'contact': 'Contato',
        'contact_text': '',
        'pdf_note': 'Portfólio para baixar e compartilhar.',
        'portfolio': 'Portfólio profissional',
        'updated': 'Outubro de 2026',
        'gorgona': {'kicker': 'ECGs de UPAs · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'Classificação de ECGs integrada ao atendimento de urgência',
                    'summary': 'Liderei o Gorgona, um sistema que analisa ECGs de UPAs de Salvador '
                               'e envia alertas pelo Telegram à equipe de regulação.',
                    'role': 'Liderança do projeto e desenvolvimento inicial do sistema',
                    'objective': 'Quando um ECG feito na UPA sugere infarto agudo do miocárdio, o '
                                 'Gorgona avisa a equipe de regulação pelo Telegram. O exame '
                                 'também segue para a telemedicina. A ideia é antecipar o aviso '
                                 'para que a equipe médica avalie o paciente e decida a conduta.',
                    'contribution': 'Além de liderar o projeto, fiz a integração inicial entre o '
                                    'modelo, o programa Windows, o servidor do InCor, o painel e o '
                                    'Telegram. Trabalhei junto à equipe clínica, responsável pelo '
                                    'protocolo de atendimento e pela avaliação dos exames.',
                    'metrics': [('2 min', 'entre o ECG e o alerta neste caso'), ('41 min', 'antes do primeiro laudo')],
                    'location': 'Implantamos o sistema na UPA Rodrigo Argolo, no bairro de '
                                'Tancredo Neves, em Salvador. Os ECGs são feitos na UPA e '
                                'analisados no servidor do InCor.',
                    'map_caption': 'Localização aproximada da UPA. Rua Pernambuco, s/n, Salvador. CNES 7033850. Mapa: © OpenStreetMap contributors. Endereço: CNES/DATASUS. Coordenadas: SaúdeNoPais.',
                    'before': 'A equipe enviava o ECG à telemedicina manualmente. Depois do laudo '
                              'e da avaliação médica, podia acionar a regulação pelo Telegram. '
                              'Quando a suspeita clínica era forte, o médico da UPA também podia '
                              'contatar o grupo diretamente.',
                    'after': 'O programa acompanha a pasta de exames e envia os novos arquivos ao '
                             'InCor para classificação. Quando a probabilidade da classe Corrente '
                             'de Lesão passa de 50%, o sistema avisa o grupo de regulação pelo '
                             'Telegram.',
                    'flow_rows': [('Coleta',
                                   'Envio manual à telemedicina',
                                   'Detecção na pasta de exames'),
                                  ('Análise',
                                   'Avaliação médica e laudo',
                                   'Classificação adicional por IA'),
                                  ('Comunicação',
                                   'Acionamento pela equipe',
                                   'Alerta automático pelo Telegram'),
                                  ('Decisão',
                                   'Equipe médica e regulação',
                                   'Equipe médica e regulação')],
                    'client': 'O ECG-IA Client acompanha uma pasta no Windows e coloca os novos '
                              'exames na fila de envio. Cada instalação tem sua própria '
                              'credencial. Pelo menu na bandeja do Windows, a equipe pode '
                              'configurar o programa, reiniciá-lo ou reenviar arquivos.',
                    'server': 'Uma API em FastAPI recebe o exame, lê os metadados e converte o '
                              'traçado em imagem quando necessário. As classes e probabilidades '
                              'ficam em SQLite. O painel mostra os resultados e o estado dos '
                              'clientes, e a integração com o Telegram envia os alertas.',
                    'privacy': 'O cliente permite anonimizar os arquivos no computador da UPA '
                               'antes do envio. A transmissão usa HTTPS, com credenciais por '
                               'instalação e perfis de acesso. Esses recursos, isoladamente, não '
                               'comprovam conformidade integral com a LGPD.',
                    'dashboard': 'O painel permite filtrar resultados por unidade, período, status '
                                 'e classe.',
                    'case': 'O caso é de um atendimento em 20 de maio de 2026, na UPA Rodrigo '
                            'Argolo. O paciente deu entrada às 18h52 e fez dois ECGs. Cada exame '
                            'gerou um alerta 2 minutos depois. A chegada ao centro de referência '
                            'foi registrada às 20h44.',
                    'timeline_caption': 'Horários do estudo de caso, a partir do primeiro ECG. '
                                        'Admissão às 18h52. A identificação do paciente foi '
                                        'retirada.',
                    'case_rows': [('Realização do ECG', '19h15', '19h37'),
                                  ('Alerta da IA', '19h17', '19h39'),
                                  ('Chegada à telemedicina', '19h21', '19h39'),
                                  ('Emissão do laudo', '19h58', '20h04'),
                                  ('Do exame ao alerta', '2 min', '2 min'),
                                  ('Antecedência em relação ao laudo', '41 min', '25 min')],
                    'case_result': 'O primeiro alerta chegou 4 minutos antes de o exame entrar na '
                                   'telemedicina. Os dois avisos antecederam os laudos em 41 e 25 '
                                   'minutos. A regulação recebeu a informação mais cedo, mas esse '
                                   'caso isolado não permite concluir que a IA reduziu o tempo de '
                                   'tratamento ou melhorou o desfecho.',
                    'model': 'O classificador reúne modelos ConvNeXt para identificar 12 '
                             'categorias. No estudo com 18.519 ECGs de 14.402 pacientes, anotados '
                             'por 19 cardiologistas, o macro F1 no teste reservado foi de 0,807 '
                             '(IC 95%: 0,788 a 0,825).',
                    'period': '2026',
                    'foundation': 'O Gorgona usa como base o modelo da AIMED, equipe que liderei '
                                  'no PhysioNet Challenge 2024. Ficamos em primeiro lugar em '
                                  'classificação. O artigo do CinC 2024 descreve o pré-treinamento '
                                  'com ECGs e o ensemble ConvNeXt. Na minha tese, detalho os '
                                  'bancos de imagens, os experimentos e a avaliação clínica.',
                    'foundation_short': 'O Gorgona usa como base o modelo da AIMED. Liderei a '
                                        'equipe no PhysioNet Challenge 2024, em que ficamos em '
                                        'primeiro lugar em classificação. O artigo do CinC 2024 e '
                                        'minha tese descrevem o método.',
                    'status': 'Implantação em UPA'},
        'incor': {'kicker': 'Integração hospitalar · InCor · 2023–2026',
                  'title': 'ECG na emergência do InCor',
                  'subtitle': '',
                  'summary': 'Desenvolvi modelos para classificar ECGs na emergência do InCor, '
                             'coordenei a anotação com cardiologistas e trabalhei na integração '
                             'com o sistema do hospital.',
                  'role': 'Desenvolvimento de modelos, coordenação da anotação e integração '
                          'clínica',
                  'objective': 'O classificador foi desenvolvido para ajudar a equipe da '
                               'emergência a priorizar a revisão dos ECGs. Sua análise aparece na '
                               'aplicação que os médicos já usam no hospital.',
                  'method': 'Na arquitetura publicada em 2023, o ECG de 12 derivações é armazenado '
                            'em DICOM no PACS, o sistema de imagens do hospital. O módulo de IA '
                            'busca o exame, prepara a imagem e faz a classificação com uma rede '
                            'neural convolucional. A figura também mostra idade, sexo e etnia como '
                            'entradas.',
                  'result': 'A versão de 2023 classificava os exames como fibrilação atrial, '
                            'outros ou normal. Depois, trabalhamos com um ensemble ConvNeXt para '
                            '12 categorias. No estudo de 2026, com 18.519 ECGs de 14.402 '
                            'pacientes, o macro F1 no teste reservado foi de 0,807 (IC 95%: 0,788 '
                            'a 0,825).',
                  'scope': 'A avaliação após a implantação incluiu revisão por cardiologista e comparação com especialistas. Os números acima descrevem o banco da pesquisa e os resultados do teste reservado.',
                  'caption': 'Integração entre o ECG, o PACS, o classificador e a aplicação da '
                             'emergência. Figura 1 de Dias et al., IEEE Access (2023).',
                  'workflow': [('Aquisição e armazenamento',
                                'ECG de 12 derivações em DICOM, armazenado no PACS.'),
                               ('Processamento',
                                'Pré-processamento da imagem e classificação por uma CNN.'),
                               ('Resultado', 'Fibrilação atrial, outros ou normal.'),
                               ('Uso pela equipe',
                                'Resultados na aplicação web da emergência para apoiar a '
                                'priorização da revisão médica.')],
                  'period': '2023–2026',
                  'contribution': 'Desenvolvi os modelos e trabalhei na implantação na emergência. '
                                  'Coordenei a anotação com os cardiologistas, desde a definição '
                                  'das classes até a revisão das leituras divergentes e a análise '
                                  'de concordância. Também participei da avaliação após a '
                                  'implantação, com revisão por cardiologista e comparação com '
                                  'especialistas.',
                  'evidence': 'Cerca de 20 mil ECGs na iniciativa de anotação com 19 '
                              'cardiologistas.',
                  'status': 'Integração hospitalar'},
        'physionet': CHALLENGE['pt'],
        'rpms': {'kicker': 'Monitoramento remoto · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': 'No RPMS, trabalhei nos protocolos de coleta com relógios, no '
                            'processamento de PPG e nos algoritmos usados pelo aplicativo.',
                 'role': 'Protocolos de coleta, processamento de sinais e desenvolvimento de '
                         'algoritmos',
                 'objective': 'O RPMS usa relógios e um aplicativo para acompanhar medidas '
                              'fisiológicas fora do hospital. O celular processa os sinais e envia '
                              'os resultados a um painel que a equipe médica pode consultar.',
                 'contribution': 'Trabalhei com os relógios protótipos, ajudei a definir os '
                                 'protocolos de coleta e organizei os dados. Com a equipe, '
                                 'desenvolvi o pré-processamento dos sinais de fotopletismografia '
                                 '(PPG) e os algoritmos usados no projeto.',
                 'method': 'O relógio envia o PPG ao aplicativo Android por Bluetooth Low Energy. '
                           'O celular processa o sinal, estima pressão arterial e frequência '
                           'cardíaca e envia os resultados por MQTT ao servidor ThingsBoard. O '
                           'painel permite acompanhar as medidas de cada paciente ao longo do '
                           'tempo.',
                 'research': 'A arquitetura publicada em 2022 estima pressão arterial e frequência '
                             'cardíaca. Em estudos relacionados, também avaliamos a qualidade do '
                             'PPG, seu uso na classificação de diabetes e a identificação de '
                             'estágios do sono. Os artigos abaixo descrevem esse trabalho.',
                 'caption': 'Relógio, aplicativo e painel médico. Figura 1 de Moreno, Dias et al., '
                            'SIoT (2022).',
                 'biomarkers': [('Qualidade do sinal',
                                 'Avaliação automática da qualidade dos segmentos de PPG.',
                                 6),
                                ('Pressão arterial',
                                 'Estimativa com calibração e avaliação dos limites de '
                                 'generalização.',
                                 1),
                                ('Diabetes',
                                 'Classificação a partir de características do PPG e metadados.',
                                 7),
                                ('Sono',
                                 'Classificação de estágios do sono com contexto temporal.',
                                 8)],
                 'period': '2022–2026',
                 'evidence': 'Arquitetura de monitoramento remoto publicada no SIoT em 2022.',
                 'status': 'Protótipo e pesquisa'},
        'education': [('2021–2025',
                       'Doutorado em Engenharia Biomédica',
                       'Universidade de São Paulo'),
                      ('2018–2020',
                       'Mestrado em Engenharia Elétrica',
                       'Universidade Federal de Juiz de Fora'),
                      ('2015–2016',
                       'Intercâmbio em Engenharia Elétrica',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017',
                       'Graduação em Engenharia Eletrônica',
                       'Universidade Federal de Juiz de Fora')],
        'experience': 'No InCor, pesquisei sinais biomédicos, desenvolvi modelos para ECG e '
                      'participei da implantação de software no atendimento. Os projetos estão '
                      'descritos neste site.',
        'skills': [('Modelos de IA',
                    'Treinamento e validação de modelos para classificação de imagens e '
                    'anonimização de textos clínicos.'),
                   ('Sinais biomédicos',
                    'Processamento e análise de ECG e PPG.'),
                   ('Programação',
                    'Python e MATLAB. PyTorch, TensorFlow/Keras e scikit-learn.'),
                   ('Software',
                    'APIs com FastAPI, integração de modelos e uso de Git, Linux e Docker.')],
        'labels': {'objective': 'Objetivo',
                   'contribution': 'O que fiz',
                   'location': 'Local da implantação',
                   'workflow': 'Fluxo anterior e fluxo com IA',
                   'before': 'Fluxo anterior',
                   'after': 'Com o Gorgona',
                   'client': 'O programa na UPA',
                   'server': 'Servidor e plataforma online',
                   'privacy': 'Proteção de dados e LGPD',
                   'case': 'Estudo de caso',
                   'model': 'Modelo de classificação',
                   'method': 'Abordagem',
                   'result': 'Resultados e avaliação',
                   'team': 'Equipe',
                   'education': 'Formação',
                   'experience': 'Experiência',
                   'skills': 'Competências',
                   'refs': 'Artigos de referência',
                   'step': 'Etapa',
                   'event': 'Evento',
                   'first': 'Primeiro ECG',
                   'second': 'Segundo ECG',
                   'official': 'Resultados oficiais',
                   'home': 'Início',
                   'skip': 'Ir para o conteúdo',
                   'how': 'Como funciona'},
        'professional_title': 'Engenharia de IA aplicada à saúde',
        'cv_summary': 'Sou engenheiro eletrônico e doutor pela USP. Hoje trabalho na Samsung, em '
                      'Campinas, como especialista sênior de P&D. Antes, no InCor, pesquisei '
                      'sinais biomédicos e desenvolvi modelos e software para o atendimento '
                      'hospitalar.\n'
                      '\n'
                      'No doutorado, estudei a classificação de ECGs por imagem. Levei esse '
                      'trabalho ao PhysioNet Challenge 2024 como líder da AIMED, e ficamos em '
                      'primeiro lugar em classificação. Também liderei o Gorgona, que analisa ECGs '
                      'de UPAs de Salvador e envia alertas pelo Telegram.',
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–atual',
                  'Especialista de P&D Sênior',
                  'Campinas, SP',
                  ['Trabalho com pesquisa e desenvolvimento de IA e software. Também faço testes e '
                   'avalio os resultados.']),
                 ('Instituto do Coração (InCor), HCFMUSP',
                  '2020–2026',
                  'Pesquisador / Analista de Sistemas Sênior, IA aplicada à saúde',
                  'São Paulo, SP',
                  ['Desenvolvi modelos para classificar imagens de ECG e trabalhei na integração '
                   'do classificador à emergência. A avaliação incluiu revisão por cardiologista e '
                   'comparação com especialistas.',
                   'Coordenei a anotação de cerca de 20 mil ECGs com 19 cardiologistas, incluindo '
                   'a definição das classes, a revisão das leituras divergentes e a análise de '
                   'concordância.',
                   'Liderei a AIMED no PhysioNet Challenge 2024. Ficamos em primeiro lugar em '
                   'classificação, e fui o primeiro autor do artigo sobre o método.',
                   'Liderei o Gorgona e fiz a integração inicial entre as UPAs de Salvador, o '
                   'servidor do InCor e os alertas pelo Telegram. O sistema avisa a equipe sobre '
                   'ECGs com suspeita de IAM com supradesnivelamento de ST, em paralelo à '
                   'telemedicina.',
                   'No RPMS, desenvolvi protocolos de coleta com relógios. Com a equipe, trabalhei '
                   'no processamento de PPG e nos algoritmos para estimar medidas fisiológicas.',
                   'Desenvolvi e avaliei modelos de linguagem para anonimizar textos clínicos em '
                   'português. Preparei uma base anotada, comparei os modelos e trabalhei com '
                   'execução local para proteger os dados.'])],
        'awards': [('2024',
                    '1º lugar em classificação no George B. Moody PhysioNet Challenge com a equipe '
                    'AIMED, que liderei.'),
                   ('2015', 'Bolsa Ciência sem Fronteiras, CAPES.'),
                   ('2011', 'Medalha de Bronze, Olimpíada Brasileira de Física (OBF).')]},
 'en': {'locale': 'en',
        'name': 'English',
        'nav': ['Projects', 'CV', 'Publications', 'Contact'],
        'role': 'AI engineering · Applied research',
        'headline': 'AI engineering for healthcare',
        'intro': 'I am a Senior R&D Specialist at Samsung with a PhD from the University of São '
                 'Paulo. My work spans healthcare AI, signal processing and model validation, from '
                 'development to deployment.',
        'bio': 'At InCor, I studied ECG image classification and led the deployment of Gorgona at '
               'an urgent care unit in Salvador, Brazil.',
        'download': 'Portfolio',
        'see': 'Explore my projects',
        'selected': 'Selected work',
        'location': 'São Paulo, Brazil',
        'read': 'View project',
        'back': 'All projects',
        'article': 'Read paper',
        'papers': 'Selected publications',
        'about': 'CV',
        'contact': 'Contact',
        'contact_text': '',
        'pdf_note': 'Downloadable portfolio for sharing.',
        'portfolio': 'Professional portfolio',
        'updated': 'October 2026',
        'gorgona': {'kicker': 'Urgent care ECGs · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'ECG classification integrated into urgent care',
                    'summary': 'I led Gorgona, a system that analyzes ECGs from urgent care units '
                               'in Salvador and sends Telegram alerts to the team coordinating '
                               'referrals.',
                    'role': 'Project leadership and initial system development',
                    'objective': 'Gorgona sends a Telegram alert to the team coordinating '
                                 'referrals when an ECG suggests myocardial infarction. The ECG '
                                 'also goes through the usual telemedicine review. The aim is to '
                                 'give the team an earlier warning. Clinicians assess the patient '
                                 'and decide what to do next.',
                    'contribution': 'I led the project and connected the model to the Windows app, '
                                    'InCor server, dashboard and Telegram in the initial '
                                    'implementation. The clinical team defined the care protocol '
                                    'and reviewed the ECGs.',
                    'metrics': [('2 min', 'from ECG to alert in this case'),
                                ('41 min', 'before the first report')],
                    'location': 'We deployed the system at UPA Rodrigo Argolo, an urgent care unit '
                                'in the Tancredo Neves neighborhood of Salvador. ECGs are recorded '
                                'at the unit and analyzed on the InCor server.',
                    'map_caption': 'Approximate location of the unit. Rua Pernambuco, s/n, Salvador. CNES 7033850. Map: © OpenStreetMap contributors. Address: CNES/DATASUS. Coordinates: SaúdeNoPais.',
                    'before': 'Staff sent ECGs to the telemedicine service manually. After the '
                              'report and clinical assessment, they could contact the referral '
                              'coordination team on Telegram. If clinical suspicion was high, the '
                              'physician at the unit could contact the group directly.',
                    'after': 'The app monitors the ECG folder and sends new files to InCor for '
                             'classification. When the probability assigned to the Current of '
                             'Injury class exceeds 50%, it sends a Telegram alert to the referral '
                             'coordination team.',
                    'flow_rows': [('Collection',
                                   'Manual telemedicine submission',
                                   'Automatic folder monitoring'),
                                  ('Analysis',
                                   'Medical review and report',
                                   'Additional AI classification'),
                                  ('Communication',
                                   'Staff-initiated contact',
                                   'Automated Telegram alert'),
                                  ('Decision',
                                   'Medical and coordination teams',
                                   'Medical and coordination teams')],
                    'client': 'The ECG-IA Client monitors a Windows folder and queues new ECGs for '
                              'upload. Each installation has its own credentials. Staff can use '
                              'the system tray menu to configure or restart the app, or upload '
                              'files again.',
                    'server': 'A FastAPI endpoint receives the ECG, reads its metadata and '
                              'converts the waveform to an image when needed. Class labels and '
                              'probabilities are stored in SQLite. The dashboard shows results and '
                              'the status of connected clients, while the Telegram integration '
                              'sends alerts.',
                    'privacy': "The client can anonymize files on the unit's computer before "
                               'upload. Transfers use HTTPS, with credentials for each '
                               "installation and role-based access. These controls alone don't "
                               "establish full compliance with Brazil's LGPD.",
                    'dashboard': 'The dashboard filters results by unit, period, status and class.',
                    'case': 'This case was recorded on May 20, 2026, at UPA Rodrigo Argolo. The '
                            'patient was admitted at 18:52 and had two ECGs, each triggering an '
                            'alert 2 minutes later. Arrival at the referral center was recorded at '
                            '20:44.',
                    'timeline_caption': 'Case study timeline, starting with the first ECG. '
                                        'Admission was at 18:52. Patient identifiers have been '
                                        'removed.',
                    'case_rows': [('ECG recorded', '19:15', '19:37'),
                                  ('AI alert', '19:17', '19:39'),
                                  ('Received by telemedicine', '19:21', '19:39'),
                                  ('Report issued', '19:58', '20:04'),
                                  ('ECG to alert', '2 min', '2 min'),
                                  ('Time before report', '41 min', '25 min')],
                    'case_result': 'The first alert arrived 4 minutes before the ECG reached the '
                                   'telemedicine service. The two alerts preceded the reports by '
                                   '41 and 25 minutes. The coordination team received the '
                                   "information sooner, but this single case doesn't establish "
                                   'whether AI improved treatment times or outcomes.',
                    'model': 'The classifier uses a ConvNeXt ensemble to identify 12 categories. '
                             'In a study of 18,519 ECGs from 14,402 patients, annotated by 19 '
                             'cardiologists, it achieved a macro F1 of 0.807 on the held-out test '
                             'set (95% CI: 0.788–0.825).',
                    'period': '2026',
                    'foundation': 'Gorgona builds on the AIMED model. I led the team in the 2024 '
                                  'PhysioNet Challenge, where we won the classification task. The '
                                  'CinC 2024 paper describes ECG pretraining and the ConvNeXt '
                                  'ensemble. My thesis covers the image datasets, experiments and '
                                  'clinical evaluation in more detail.',
                    'foundation_short': 'Gorgona builds on the AIMED model. I led the team in the '
                                        '2024 PhysioNet Challenge, where we won the classification '
                                        'task. The CinC 2024 paper and my thesis describe the '
                                        'method.',
                    'status': 'Urgent care deployment'},
        'incor': {'kicker': 'Hospital integration · InCor · 2023–2026',
                  'title': 'ECG classification at InCor',
                  'subtitle': '',
                  'summary': 'I developed models to classify ECGs in the InCor emergency '
                             'department, coordinated annotation with cardiologists and helped '
                             'integrate the classifier into the hospital system.',
                  'role': 'Model development, annotation coordination and clinical integration',
                  'objective': 'We built the classifier to help emergency department clinicians '
                               'decide which ECGs to review first. Its predictions appear in the '
                               'hospital application they already use.',
                  'method': 'In the architecture published in 2023, 12-lead ECGs are stored in '
                            "DICOM format in the hospital's picture archiving and communication "
                            'system (PACS). The AI module retrieves the ECG, prepares the image '
                            'and classifies it with a convolutional neural network. The figure '
                            'also shows age, sex and ethnicity as inputs.',
                  'result': 'The 2023 version classified ECGs as atrial fibrillation, other or '
                            'normal. We later developed a ConvNeXt ensemble for 12 categories. In '
                            'the 2026 study of 18,519 ECGs from 14,402 patients, it achieved a '
                            'macro F1 of 0.807 on the held-out test set (95% CI: 0.788–0.825).',
                  'scope': 'Evaluation after deployment included cardiologist review and comparison with specialists. The figures above describe the research dataset and its held-out test results.',
                  'caption': 'Integration of the ECG, PACS, classifier and emergency department '
                             'application. Figure 1 from Dias et al., IEEE Access (2023).',
                  'workflow': [('Recording and storage',
                                '12-lead ECGs stored in DICOM format in PACS.'),
                               ('Processing', 'Image preprocessing and classification with a CNN.'),
                               ('Output', 'Atrial fibrillation, other or normal.'),
                               ('Clinical use',
                                'Predictions shown in the emergency department web app to help '
                                'clinicians prioritize ECG review.')],
                  'period': '2023–2026',
                  'contribution': 'I developed the models and helped deploy the classifier in the '
                                  "emergency department. I coordinated the cardiologists' ECG "
                                  'annotations, including class definitions, review of conflicting '
                                  'readings and agreement analysis. After deployment, I helped '
                                  'evaluate the system with a cardiologist and compare it with '
                                  'specialists.',
                  'evidence': 'Around 20,000 ECGs in the annotation initiative with 19 '
                              'cardiologists.',
                  'status': 'Hospital integration'},
        'physionet': CHALLENGE['en'],
        'rpms': {'kicker': 'Remote monitoring · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': 'On RPMS, I developed data collection protocols and worked on PPG '
                            'processing and the algorithms used by the mobile app.',
                 'role': 'Data collection protocols, signal processing and algorithm development',
                 'objective': 'RPMS uses watches and a mobile app to track physiological '
                              'measurements outside the hospital. The phone processes the signals '
                              'and sends results to a dashboard that clinicians can consult.',
                 'contribution': 'I worked with prototype watches, helped define the recording '
                                 'protocols and organized the data. With the team, I developed the '
                                 'photoplethysmography (PPG) preprocessing pipeline and the '
                                 'algorithms used in the project.',
                 'method': 'The watch sends PPG to the Android app over Bluetooth Low Energy. The '
                           'phone processes the signal, estimates blood pressure and heart rate, '
                           'and sends results over MQTT to a ThingsBoard server. The dashboard '
                           'displays each patient’s measurements over time.',
                 'research': 'The 2022 system estimates blood pressure and heart rate. Related '
                             'studies examined PPG signal quality, diabetes classification and '
                             'sleep staging. The papers below describe that work.',
                 'caption': 'Watch, app and clinical dashboard. Figure 1 from Moreno, Dias et al., '
                            'SIoT (2022).',
                 'biomarkers': [('Signal quality',
                                 'Automated assessment of PPG segment quality.',
                                 6),
                                ('Blood pressure',
                                 'Calibrated estimation and evaluation of generalization limits.',
                                 1),
                                ('Diabetes',
                                 'Classification using PPG features and patient metadata.',
                                 7),
                                ('Sleep', 'Sleep stage classification using temporal context.', 8)],
                 'period': '2022–2026',
                 'evidence': 'Remote monitoring architecture published at SIoT in 2022.',
                 'status': 'Prototype and research'},
        'education': [('2021–2025', 'PhD in Biomedical Engineering', 'University of São Paulo'),
                      ('2018–2020',
                       'MSc in Electrical Engineering',
                       'Federal University of Juiz de Fora'),
                      ('2015–2016',
                       'Exchange program in Electrical Engineering',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017',
                       'BSc in Electronic Engineering',
                       'Federal University of Juiz de Fora')],
        'experience': 'At InCor, I researched biomedical signals, developed ECG models and worked '
                      'on software deployment in clinical care. The projects are described on this '
                      'site.',
        'skills': [('AI models',
                    'Training and validation of models for image classification and '
                    'clinical text anonymization.'),
                   ('Biomedical signals',
                    'ECG and PPG processing and analysis.'),
                   ('Programming',
                    'Python and MATLAB. PyTorch, TensorFlow/Keras and scikit-learn.'),
                   ('Software',
                    'APIs with FastAPI, model integration, Git, Linux and Docker.')],
        'labels': {'objective': 'Objective',
                   'contribution': 'My work',
                   'location': 'Deployment location',
                   'workflow': 'Before and after adding Gorgona',
                   'before': 'Previous workflow',
                   'after': 'With Gorgona',
                   'client': 'The app at the urgent care unit',
                   'server': 'Server and online platform',
                   'privacy': 'Data protection and LGPD',
                   'case': 'Case study',
                   'model': 'Classification model',
                   'method': 'Approach',
                   'result': 'Results and evaluation',
                   'team': 'Team',
                   'education': 'Education',
                   'experience': 'Experience',
                   'skills': 'Skills',
                   'refs': 'Related papers',
                   'step': 'Stage',
                   'event': 'Event',
                   'first': 'First ECG',
                   'second': 'Second ECG',
                   'official': 'Official results',
                   'home': 'Home',
                   'skip': 'Skip to content',
                   'how': 'How it works'},
        'professional_title': 'AI engineering for healthcare',
        'cv_summary': "I'm an electronics engineer with a PhD from the University of São Paulo. I "
                      'work as a Senior R&D Specialist at Samsung in Campinas, Brazil. Before '
                      'joining Samsung, I worked at InCor, researching biomedical signals and '
                      'developing models and software for clinical care.\n'
                      '\n'
                      'My PhD focused on classifying ECG images. I built on that research to lead '
                      'AIMED in the 2024 PhysioNet Challenge, where we won the classification '
                      'task. I also led Gorgona, a system that analyzes ECGs from urgent care '
                      'units in Salvador and sends Telegram alerts.',
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–present',
                  'Senior R&D Specialist',
                  'Campinas, Brazil',
                  ['I work on AI and software research, development and testing, and evaluate the '
                   'results.']),
                 ('Heart Institute (InCor), HCFMUSP',
                  '2020–2026',
                  'Researcher / Senior Systems Analyst, Healthcare AI',
                  'São Paulo, Brazil',
                  ['I developed models for ECG image classification and helped integrate the '
                   'classifier into the emergency department. Evaluation included cardiologist '
                   'review and comparison with specialists.',
                   'I coordinated the annotation of around 20,000 ECGs by 19 cardiologists, '
                   'including class definitions, review of conflicting readings and agreement '
                   'analysis.',
                   'I led AIMED in the 2024 PhysioNet Challenge. We won the classification task, '
                   'and I was the first author of the paper describing our method.',
                   'I led Gorgona and built the initial integration between urgent care units in '
                   'Salvador, the InCor server and Telegram alerts. It flags ECGs with suspected '
                   'ST-elevation myocardial infarction while the usual telemedicine review '
                   'continues.',
                   'For RPMS, I developed protocols for recording signals with watches. With the '
                   'team, I worked on PPG processing and algorithms for estimating physiological '
                   'measurements.',
                   'I developed and evaluated language models for anonymizing Portuguese clinical '
                   'text. I prepared an annotated dataset, compared models and worked on running '
                   'them locally to protect the data.'])],
        'awards': [('2024',
                    'First place in classification in the George B. Moody PhysioNet Challenge with '
                    'team AIMED, which I led.'),
                   ('2015', 'Science without Borders scholarship, CAPES.'),
                   ('2011', 'Bronze Medal, Brazilian Physics Olympiad (OBF).')]}}
