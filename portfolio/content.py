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
        'download': 'Portfólio',
        'see': 'Conhecer os projetos',
        'selected': 'Alguns trabalhos',
        'location': 'São Paulo, Brasil',
        'notes_title': 'No meu GitHub',
        'render_caption': 'Um ECG sintético produzido pela minha biblioteca.',
        'experiments': [
            ('ecg-torch-renderer', 'https://github.com/fmenegui/ecg-torch-renderer',
             'De sinais para imagens de ECG, dentro do treinamento em PyTorch.'),
            ('anatomy-coordinate-probe', 'https://github.com/fmenegui/anatomy-coordinate-probe',
             'Um modelo de linguagem consegue desenhar a silhueta do corpo só com coordenadas?')],
        'read': 'Ver projeto',
        'back': 'Todos os projetos',
        'article': 'Ler artigo',
        'papers': 'Publicações selecionadas',
        'about': 'Currículo',
        'contact': 'Contato',
        'contact_text': '',
        'pdf_note': 'Uma versão para leitura e envio em candidaturas.',
        'portfolio': 'Portfólio profissional',
        'updated': 'Outubro de 2026',
        'gorgona': {'kicker': 'ECGs de UPAs · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'Classificação de ECGs integrada ao atendimento de urgência',
                    'summary': (((('Liderei o Gorgona, que analisa ECGs de UPAs de Salvador no servidor do '
                                   'InCor e envia alertas pelo Telegram, em paralelo à telemedicina.')))),
                    'role': 'Liderança do projeto e desenvolvimento inicial do sistema',
                    'objective': (((('O Gorgona analisa ECGs feitos em UPAs e avisa a equipe de regulação '
                                     'quando encontra exames com suspeita de corrente de lesão. O aviso '
                                     'chega pelo Telegram enquanto o exame também segue para a telemedicina. '
                                     'A equipe médica avalia o paciente e decide a conduta.')))),
                    'contribution': (((('Liderei o projeto e desenvolvi a integração inicial do modelo com o '
                                        'programa Windows, o servidor do InCor, o painel e o Telegram. '
                                        'Trabalhei com a equipe clínica, que definiu o protocolo de '
                                        'atendimento e avaliou os exames.')))),
                    'metrics': [('2 min', 'do ECG ao alerta, no caso'),
                                ('41 min', 'antes do primeiro laudo')],
                    'location': (((('A implantação apresentada aqui foi feita na UPA Rodrigo Argolo, em '
                                    'Tancredo Neves, Salvador. Os ECGs são feitos na UPA, e o modelo roda no '
                                    'servidor do InCor.')))),
                    'map_caption': 'Localização cadastral aproximada. Rua Pernambuco, s/n, Salvador. CNES '
                                   '7033850. Base: © OpenStreetMap contributors. Endereço: CNES/DATASUS. '
                                   'Coordenadas: SaúdeNoPais.',
                    'before': (((('A equipe enviava o ECG manualmente à telemedicina. Depois do laudo e da '
                                  'avaliação médica, podia acionar a regulação pelo Telegram. Se a suspeita '
                                  'clínica fosse forte, o médico da UPA também podia contatar o grupo '
                                  'diretamente.')))),
                    'after': (((('Acrescentamos o envio automático: o programa detecta o arquivo na pasta de '
                                 'exames e o encaminha ao InCor, onde o modelo faz a classificação. Se a '
                                 'probabilidade da classe Corrente de Lesão supera 50%, o sistema envia um '
                                 'alerta ao grupo configurado.')))),
                    'flow_rows': [('Coleta', 'Envio manual à telemedicina', 'Detecção na pasta de exames'),
                                  ('Análise', 'Avaliação médica e laudo', 'Classificação adicional por IA'),
                                  ('Comunicação', 'Acionamento pela equipe', 'Alerta automático pelo Telegram'),
                                  ('Decisão', 'Equipe médica e regulação', 'Equipe médica e regulação')],
                    'client': (((('O ECG-IA Client acompanha uma pasta no Windows e coloca os novos exames '
                                  'em uma fila de envio. Cada instalação tem sua própria credencial. Pelo '
                                  'menu na bandeja, é possível configurar o programa, reiniciá-lo ou '
                                  'reenviar os arquivos da pasta.')))),
                    'server': (((('No servidor, uma API em FastAPI recebe o exame, lê os metadados e '
                                  'converte o traçado em imagem quando necessário. Guardamos as classes e '
                                  'probabilidades em SQLite. O painel mostra os resultados e o estado dos '
                                  'clientes, e a integração com o Telegram envia os alertas.')))),
                    'privacy': (((('O cliente tem uma opção de anonimizar os arquivos no computador da UPA '
                                   'antes do envio. A transmissão usa HTTPS, e o acesso tem credenciais por '
                                   'instalação e perfis de usuário. São controles técnicos de proteção dos '
                                   'dados, que por si só não demonstram conformidade integral com a LGPD.')))),
                    'dashboard': 'O painel permite filtrar resultados por unidade, período, status e classe.',
                    'case': (((('No atendimento documentado em 20 de maio de 2026, na UPA Rodrigo Argolo, a '
                                'admissão foi às 18h52. Foram feitos dois ECGs, e cada um gerou um alerta 2 '
                                'minutos após sua realização. A chegada ao centro de referência foi '
                                'registrada às 20h44.')))),
                    'timeline_caption': (((('Linha do tempo do estudo de caso, a partir do primeiro ECG. A '
                                            'identificação do paciente foi retirada. Admissão às 18h52.')))),
                    'case_rows': [('Realização do ECG', '19h15', '19h37'),
                                  ('Alerta da IA', '19h17', '19h39'),
                                  ('Chegada à telemedicina', '19h21', '19h39'),
                                  ('Emissão do laudo', '19h58', '20h04'),
                                  ('Do exame ao alerta', '2 min', '2 min'),
                                  ('Antecedência em relação ao laudo', '41 min', '25 min')],
                    'case_result': (((('O primeiro alerta chegou 4 minutos antes de o exame entrar na '
                                       'telemedicina. Os avisos antecederam os laudos em 41 e 25 minutos. '
                                       'Esses horários mostram que a informação chegou mais cedo à '
                                       'regulação. Com esse caso isolado, não dá para atribuir à IA uma '
                                       'melhora no tempo de tratamento ou no desfecho.')))),
                    'model': (((('O classificador usa um ensemble ConvNeXt para 12 categorias. No estudo com '
                                 '18.519 ECGs de 14.402 pacientes, anotados por 19 cardiologistas, o macro '
                                 'F1 no teste reservado foi de 0,807 (IC 95%: 0,788 a 0,825). Esse é o '
                                 'resultado da avaliação do modelo no estudo.')))),
                    'period': '2026',
                    'foundation': (((('Partimos do modelo da AIMED, equipe que liderei no PhysioNet '
                                      'Challenge 2024 e que ficou em primeiro lugar na classificação. O '
                                      'artigo do CinC 2024 descreve a ConvNeXt, o pré-treinamento com ECGs e '
                                      'o ensemble. Na tese, detalho os bancos de imagens, os experimentos e '
                                      'a avaliação clínica.')))),
                    'foundation_short': (((('Partimos do modelo da AIMED, equipe que liderei no PhysioNet '
                                            'Challenge 2024. Ficamos em primeiro lugar na classificação. O '
                                            'artigo do CinC 2024 e minha tese descrevem o método.')))),
                    'decisions': [('Telemedicina',
                                   'Mantivemos o fluxo de telemedicina e acrescentamos o alerta automático. '
                                   'A equipe médica continua responsável pela avaliação e pela decisão de '
                                   'atendimento.'),
                                  ('Onde o modelo roda',
                                   'O programa Windows acompanha a pasta de exames e organiza os envios. A '
                                   'classificação roda no servidor do InCor, e os controles locais permitem '
                                   'reiniciar o programa ou reenviar arquivos.'),
                                  ('Proteção dos dados',
                                   'O cliente oferece anonimização local configurável. O envio usa HTTPS e '
                                   'credenciais próprias de cada instalação. Esses recursos precisam ser '
                                   'considerados no contexto dos requisitos de proteção de dados.')],
                    'status': 'Implantação em UPA'},
        'incor': {'kicker': 'Integração hospitalar · InCor · 2023–2026',
                  'title': 'ECG na emergência do InCor',
                  'subtitle': '',
                  'summary': (((('No InCor, desenvolvi modelos para classificar ECGs na emergência. '
                                 'Coordenei a anotação dos exames com cardiologistas e trabalhei na '
                                 'integração com o sistema do hospital.')))),
                  'role': 'Desenvolvimento de modelos, coordenação da anotação e integração clínica',
                  'objective': (((('A proposta era ajudar a equipe da emergência a organizar a revisão dos '
                                   'ECGs. O classificador apresenta sua análise na aplicação que os médicos '
                                   'já usam no hospital.')))),
                  'method': (((('Na arquitetura que publicamos em 2023, o ECG de 12 derivações fica '
                                'armazenado em DICOM no PACS, o sistema de imagens do hospital. O módulo de '
                                'IA busca o exame, prepara a imagem e faz a classificação com uma rede '
                                'neural convolucional. Na figura, idade, sexo e etnia também aparecem como '
                                'entradas.')))),
                  'result': (((('A versão de 2023 classificava os exames como fibrilação atrial, outros ou '
                                'normal. Depois, trabalhamos com um ensemble ConvNeXt para 12 categorias. No '
                                'estudo de 2026, com 18.519 ECGs de 14.402 pacientes, o macro F1 no teste '
                                'reservado foi de 0,807 (IC 95%: 0,788 a 0,825).')))),
                  'scope': (((('A implantação foi avaliada por cardiologista e comparada com especialistas. '
                               'Os números acima se referem ao banco e ao teste da pesquisa, não à '
                               'quantidade de exames atendidos na rotina.')))),
                  'caption': (((('Integração entre o ECG, o PACS, o classificador e a aplicação da '
                                 'emergência. Figura 1 de Dias et al., IEEE Access (2023).')))),
                  'workflow': [('Aquisição e armazenamento', 'ECG de 12 derivações em DICOM, armazenado no PACS.'),
                               ('Processamento', 'Pré-processamento da imagem e classificação por uma CNN.'),
                               ('Resultado', 'Fibrilação atrial, outros ou normal.'),
                               ('Uso pela equipe',
                                'Resultados na aplicação web da emergência para apoiar a priorização da revisão '
                                'médica.')],
                  'period': '2023–2026',
                  'contribution': (((('Desenvolvi os modelos e trabalhei na implantação na emergência. '
                                      'Também coordenei a anotação de cerca de 20 mil ECGs com 19 '
                                      'cardiologistas, organizando as classes, a revisão de divergências e a '
                                      'análise de concordância. Depois da implantação, participei da '
                                      'avaliação com cardiologista e da comparação com especialistas.')))),
                  'evidence': 'Cerca de 20 mil ECGs na iniciativa de anotação com 19 cardiologistas.',
                  'decisions': [('Dentro do sistema do hospital',
                                 'Usamos os ECGs armazenados no PACS e apresentamos a classificação na '
                                 'aplicação da emergência, junto ao fluxo de revisão médica.'),
                                ('Anotação com cardiologistas',
                                 'Organizei a anotação com definição de classes, revisão das leituras '
                                 'divergentes e análise da concordância entre cardiologistas.'),
                                ('Versões do modelo',
                                 'A versão de 2023 usa três classes. A pesquisa de 2026 avalia 12 '
                                 'categorias. O resultado desse teste descreve o modelo estudado, não todas '
                                 'as versões implantadas.')],
                  'status': 'Integração hospitalar'},
        'physionet': CHALLENGE['pt'],
        'rpms': {'kicker': 'Monitoramento remoto · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': (((('Trabalhei com a equipe no monitoramento remoto por relógios, desde os '
                                'protocolos de coleta até o processamento de PPG e os algoritmos no celular.')))),
                 'role': 'Protocolos de coleta, processamento de sinais e desenvolvimento de algoritmos',
                 'objective': (((('O RPMS usa relógios e um aplicativo para acompanhar medidas fisiológicas '
                                  'fora do hospital. O celular processa os sinais e envia os resultados a um '
                                  'painel, onde a equipe médica pode acompanhar cada paciente.')))),
                 'contribution': (((('Trabalhei com relógios protótipos e ajudei a definir como coletar os '
                                     'sinais. Organizei os dados e, com a equipe, desenvolvi o '
                                     'pré-processamento de fotopletismografia (PPG) e os algoritmos usados '
                                     'no projeto.')))),
                 'method': 'O relógio envia o PPG ao aplicativo Android por Bluetooth Low Energy. O celular '
                           'processa o sinal, estima pressão arterial e frequência cardíaca e envia os resultados '
                           'por MQTT ao servidor ThingsBoard. O painel permite acompanhar as medidas de cada '
                           'paciente ao longo do tempo.',
                 'research': (((('Além de estimar pressão arterial e frequência cardíaca, pesquisamos a '
                                 'qualidade do PPG, a classificação relacionada ao diabetes e os estágios do '
                                 'sono. Os artigos abaixo descrevem esses estudos. Na arquitetura publicada '
                                 'em 2022, o aplicativo estima pressão arterial e frequência cardíaca.')))),
                 'caption': (((('Relógio, aplicativo e painel médico. Figura 1 de Moreno, Dias et al., SIoT '
                                '(2022).')))),
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
                                'O relógio envia o PPG por Bluetooth Low Energy. O celular calcula as '
                                'estimativas e envia os resultados ao servidor, em vez de transmitir todos '
                                'os sinais brutos.'),
                               ('Sinal e medida de referência',
                                'Intercalamos três registros de PPG com medidas de pressão por manguito, '
                                'após repouso. Assim, cada coleta tem uma referência para avaliar a '
                                'estimativa.'),
                               ('Pessoas diferentes no teste',
                                'Separamos os participantes entre as partições de validação. Isso permite '
                                'testar o modelo em pessoas que não fizeram parte do treinamento.')],
                 'status': 'Protótipo e pesquisa'},
        'education': [('2021–2025', 'Doutorado em Engenharia Biomédica', 'Universidade de São Paulo'),
                      ('2018–2020', 'Mestrado em Engenharia Elétrica', 'Universidade Federal de Juiz de Fora'),
                      ('2015–2016',
                       'Intercâmbio em Engenharia Elétrica',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017', 'Graduação em Engenharia Eletrônica', 'Universidade Federal de Juiz de Fora')],
        'experience': 'No InCor, pesquisei sinais biomédicos, desenvolvi modelos para ECG e participei da '
                      'implantação de software no atendimento. Os projetos estão descritos neste site.',
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
        'cv_summary': (((('Sou engenheiro eletrônico e doutor pela USP. Hoje trabalho como especialista '
                          'sênior de P&D na Samsung, em Campinas. Antes disso, trabalhei no InCor, com '
                          'pesquisa em sinais biomédicos, modelos de IA e software para o atendimento.\n'
                          '\n'
                          'No doutorado, estudei como classificar ECGs diretamente a partir de imagens. '
                          'Liderei a equipe AIMED no PhysioNet Challenge 2024, em que ficamos em primeiro '
                          'lugar na tarefa de classificação. Também liderei o Gorgona, que leva essa análise '
                          'a ECGs feitos em UPAs de Salvador.')))),
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–atual',
                  'Especialista de P&D Sênior',
                  'Campinas, SP',
                  ['Trabalho na pesquisa e no desenvolvimento de IA e software. Testo as implementações e '
                   'avalio os resultados.']),
                 ('Instituto do Coração (InCor), HCFMUSP',
                  '2020–2026',
                  'Pesquisador / Analista de Sistemas Sênior, IA aplicada à saúde',
                  'São Paulo, SP',
                  ['Desenvolvi modelos para classificar imagens de ECG e trabalhei na implantação do '
                   'classificador na emergência. A avaliação incluiu revisão por cardiologista e comparação '
                   'com especialistas.',
                   'Coordenei a anotação de cerca de 20 mil ECGs com 19 cardiologistas. Organizei as classes '
                   'e as leituras, a revisão das divergências e a análise de concordância.',
                   'Liderei a equipe AIMED no PhysioNet Challenge 2024. Ficamos em primeiro lugar na tarefa '
                   'de classificação, e fui o primeiro autor do artigo que descreve o método.',
                   'Liderei o Gorgona e desenvolvi a integração inicial entre as UPAs de Salvador, o '
                   'servidor do InCor e os alertas pelo Telegram. O sistema envia alertas para ECGs com '
                   'suspeita de IAM com supradesnivelamento de ST em paralelo à telemedicina.',
                   'No RPMS, trabalhei com relógios para monitoramento remoto. Desenvolvi protocolos de '
                   'coleta e, com a equipe, o processamento de PPG e os algoritmos para estimar medidas '
                   'fisiológicas.',
                   'Desenvolvi e avaliei modelos de linguagem para anonimizar textos clínicos em português. '
                   'O trabalho incluiu uma base anotada, comparação de modelos e execução local para '
                   'proteger os dados.'])],
        'awards': [('2024',
                    '1º lugar em classificação no George B. Moody PhysioNet Challenge com a equipe AIMED, '
                    'que liderei.'),
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
        'download': 'Portfolio',
        'see': 'Explore my projects',
        'selected': 'Selected work',
        'location': 'São Paulo, Brazil',
        'notes_title': 'On my GitHub',
        'render_caption': 'A synthetic ECG produced by my renderer.',
        'experiments': [
            ('ecg-torch-renderer', 'https://github.com/fmenegui/ecg-torch-renderer',
             'From signals to ECG images, inside a PyTorch training loop.'),
            ('anatomy-coordinate-probe', 'https://github.com/fmenegui/anatomy-coordinate-probe',
             'Can a language model draw a body silhouette from coordinates alone?')],
        'read': 'View project',
        'back': 'All projects',
        'article': 'Read paper',
        'papers': 'Selected publications',
        'about': 'CV',
        'contact': 'Contact',
        'contact_text': '',
        'pdf_note': 'A standalone portfolio for applications and sharing.',
        'portfolio': 'Professional portfolio',
        'updated': 'October 2026',
        'gorgona': {'kicker': 'Urgent care ECGs · InCor · 2026',
                    'title': 'Gorgona',
                    'subtitle': 'ECG classification integrated into urgent care',
                    'summary': (((('I led Gorgona, which analyzes ECGs from urgent care units in Salvador on '
                                   'the InCor server and sends Telegram alerts alongside telemedicine.')))),
                    'role': 'Project leadership and initial system development',
                    'objective': (((('Gorgona analyzes ECGs recorded at urgent care units and notifies the '
                                     'clinical coordination team when an ECG suggests current of injury. The '
                                     'alert arrives through Telegram while the examination also goes to '
                                     'telemedicine. Clinicians assess the patient and decide on care.')))),
                    'contribution': (((('I led the project and developed the initial integration of the '
                                        'model with the Windows application, InCor server, dashboard and '
                                        'Telegram. I worked with the clinical team, who defined the care '
                                        'protocol and reviewed the ECGs.')))),
                    'metrics': [('2 min', 'ECG to alert in the case'),
                                ('41 min', 'before the first report')],
                    'location': (((('The deployment shown here was at UPA Rodrigo Argolo, an urgent care '
                                    'unit in Tancredo Neves, Salvador. ECGs are recorded at the unit, and '
                                    'the model runs on the InCor server.')))),
                    'map_caption': 'Approximate registry location. Rua Pernambuco, s/n, Salvador. CNES 7033850. '
                                   'Map: © OpenStreetMap contributors. Address: CNES/DATASUS. Coordinates: '
                                   'SaúdeNoPais.',
                    'before': (((('Staff sent the ECG to telemedicine manually. The report and medical '
                                  'assessment informed whether to contact the coordination group on '
                                  'Telegram. If clinical suspicion was high, the physician could also '
                                  'contact the group directly.')))),
                    'after': (((('We added automatic submission: the application detects the file in the '
                                 'examination folder and sends it to InCor for classification. If the '
                                 'probability of the Current of Injury class exceeds 50%, the system alerts '
                                 'the configured group.')))),
                    'flow_rows': [('Collection', 'Manual telemedicine submission', 'Automatic folder monitoring'),
                                  ('Analysis', 'Medical review and report', 'Additional AI classification'),
                                  ('Communication', 'Staff-initiated contact', 'Automated Telegram alert'),
                                  ('Decision',
                                   'Medical and coordination teams',
                                   'Medical and coordination teams')],
                    'client': (((('The ECG-IA Client watches a folder on Windows and queues new examinations '
                                  'for upload. Each installation has its own credential. The system tray '
                                  'menu lets staff configure the application, restart it or resubmit files '
                                  'from the folder.')))),
                    'server': (((('On the server, a FastAPI endpoint receives the examination, reads its '
                                  'metadata and converts the trace to an image when needed. We store classes '
                                  'and probabilities in SQLite. The dashboard shows results and client '
                                  'status, and the Telegram integration sends the alerts.')))),
                    'privacy': (((('The client has an option to anonymize files on the unit’s computer '
                                   'before upload. Transmission uses HTTPS, with credentials for each '
                                   'installation and user access roles. These are technical data protection '
                                   'controls and do not, by themselves, demonstrate full compliance with '
                                   'Brazil’s LGPD.')))),
                    'dashboard': 'The dashboard filters results by unit, period, status and class.',
                    'case': (((('In the encounter documented on May 20, 2026, at UPA Rodrigo Argolo, '
                                'admission was at 18:52. Two ECGs were recorded, and each triggered an alert '
                                '2 minutes later. Arrival at the referral center was recorded at 20:44.')))),
                    'timeline_caption': (((('Case study timeline, starting with the first ECG. Patient '
                                            'identifiers have been removed. Admission was at 18:52.')))),
                    'case_rows': [('ECG acquisition', '19:15', '19:37'),
                                  ('AI alert', '19:17', '19:39'),
                                  ('Arrival at telemedicine', '19:21', '19:39'),
                                  ('Report issued', '19:58', '20:04'),
                                  ('ECG to alert', '2 min', '2 min'),
                                  ('Lead time before report', '41 min', '25 min')],
                    'case_result': (((('The first alert arrived 4 minutes before the examination reached '
                                       'telemedicine. The alerts preceded the reports by 41 and 25 minutes. '
                                       'These times show that information reached the coordination team '
                                       'earlier. This single case does not establish that AI improved '
                                       'treatment times or outcomes.')))),
                    'model': (((('The classifier uses a ConvNeXt ensemble for 12 categories. In the study of '
                                 '18,519 ECGs from 14,402 patients, annotated by 19 cardiologists, held-out '
                                 'macro F1 was 0.807 (95% CI: 0.788–0.825). This is the model’s evaluation '
                                 'result in that study.')))),
                    'period': '2026',
                    'foundation': (((('We started from the AIMED model. I led the team in the 2024 PhysioNet '
                                      'Challenge, where we placed first in classification. The CinC 2024 '
                                      'paper describes ConvNeXt, ECG pretraining and the ensemble. My thesis '
                                      'details the image datasets, experiments and clinical evaluation.')))),
                    'foundation_short': (((('We started from the AIMED model. I led the team in the 2024 '
                                            'PhysioNet Challenge, where we placed first in classification. '
                                            'The CinC 2024 paper and my thesis describe the method.')))),
                    'decisions': [('Telemedicine',
                                   'We kept the telemedicine workflow and added automated alerts. Clinicians '
                                   'remain responsible for assessment and care decisions.'),
                                  ('Where the model runs',
                                   'The Windows application watches the examination folder and queues '
                                   'uploads. Classification runs on the InCor server. Local controls let '
                                   'staff restart the application or resubmit files.'),
                                  ('Data protection',
                                   'The client offers configurable local anonymization. Uploads use HTTPS '
                                   'and credentials for each installation. These features need to be '
                                   'considered within the data protection requirements.')],
                    'status': 'Urgent care deployment'},
        'incor': {'kicker': 'Hospital integration · InCor · 2023–2026',
                  'title': 'ECG classification at InCor',
                  'subtitle': '',
                  'summary': (((('At InCor, I developed models to classify emergency ECGs. I coordinated ECG '
                                 'annotation with cardiologists and worked on integration with the hospital '
                                 'system.')))),
                  'role': 'Model development, annotation coordination and clinical integration',
                  'objective': (((('The aim was to help the emergency team prioritize ECG review. The '
                                   'classifier presents its analysis in the application clinicians already '
                                   'use at the hospital.')))),
                  'method': (((('In the architecture we published in 2023, the 12-lead ECG is stored in '
                                'DICOM format in the hospital’s picture archiving and communication system '
                                '(PACS). The AI module retrieves the examination, prepares the image and '
                                'classifies it with a convolutional neural network. The figure also shows '
                                'age, sex and ethnicity as inputs.')))),
                  'result': (((('The 2023 version classified examinations as atrial fibrillation, other or '
                                'normal. We later worked with a ConvNeXt ensemble for 12 categories. In the '
                                '2026 study of 18,519 ECGs from 14,402 patients, held-out macro F1 was 0.807 '
                                '(95% CI: 0.788–0.825).')))),
                  'scope': (((('Deployment was reviewed by a cardiologist and compared with specialists. The '
                               'figures above describe the research dataset and test results, rather than '
                               'the number of examinations processed in routine care.')))),
                  'caption': (((('Integration of the ECG, PACS, classifier and emergency department '
                                 'application. Figure 1 from Dias et al., IEEE Access (2023).')))),
                  'workflow': [('Acquisition and storage', '12-lead ECG in DICOM format, stored in PACS.'),
                               ('Processing', 'Image preprocessing and classification by a CNN.'),
                               ('Output', 'Atrial fibrillation, other or normal.'),
                               ('Clinical use',
                                'Results in the emergency room web application to support prioritization of '
                                'medical review.')],
                  'period': '2023–2026',
                  'contribution': (((('I developed the models and worked on deployment in the emergency '
                                      'department. I also coordinated annotation of around 20,000 ECGs with '
                                      '19 cardiologists, organizing class definitions, review of '
                                      'disagreements and agreement analysis. After deployment, I worked on '
                                      'cardiologist review and comparison with specialists.')))),
                  'evidence': 'Around 20,000 ECGs in the annotation initiative with 19 cardiologists.',
                  'decisions': [('Within the hospital system',
                                 'We use ECGs stored in PACS and show classifications in the emergency '
                                 'application alongside medical review.'),
                                ('Annotation with cardiologists',
                                 'I organized annotation around class definitions, review of conflicting '
                                 'readings and agreement analysis between cardiologists.'),
                                ('Model versions',
                                 'The 2023 version uses three classes. The 2026 research evaluates 12 '
                                 'categories. That test result describes the model studied, not every '
                                 'deployed version.')],
                  'status': 'Hospital integration'},
        'physionet': CHALLENGE['en'],
        'rpms': {'kicker': 'Remote monitoring · InCor',
                 'title': 'RPMS',
                 'subtitle': 'Remote Patient Monitoring System',
                 'summary': (((('I worked with the team on remote monitoring with watches, from collection '
                                'protocols to PPG processing and algorithms running on the phone.')))),
                 'role': 'Data collection protocols, signal processing and algorithm development',
                 'objective': (((('RPMS uses watches and a mobile app to track physiological measurements '
                                  'outside the hospital. The phone processes the signals and sends results '
                                  'to a dashboard, where the clinical team can follow each patient.')))),
                 'contribution': (((('I worked with prototype watches and helped define how to collect the '
                                     'signals. I organized the data and worked with the team on '
                                     'photoplethysmography (PPG) preprocessing and the project’s algorithms.')))),
                 'method': 'The watch sends PPG to the Android app over Bluetooth Low Energy. The phone processes '
                           'the signal, estimates blood pressure and heart rate, and sends results over MQTT to a '
                           'ThingsBoard server. The dashboard displays each patient’s measurements over time.',
                 'research': (((('Alongside blood pressure and heart rate estimation, we studied PPG '
                                 'quality, diabetes-related classification and sleep stages. The papers '
                                 'below describe these studies. In the architecture published in 2022, the '
                                 'app estimates blood pressure and heart rate.')))),
                 'caption': (((('Watch, app and clinical dashboard. Figure 1 from Moreno, Dias et al., SIoT '
                                '(2022).')))),
                 'biomarkers': [('Signal quality', 'Automated assessment of PPG segment quality.', 6),
                                ('Blood pressure',
                                 'Calibrated estimation and evaluation of generalization limits.',
                                 1),
                                ('Diabetes', 'Classification using PPG features and patient metadata.', 7),
                                ('Sleep', 'Sleep stage classification using temporal context.', 8)],
                 'period': '2022–2026',
                 'evidence': '52 volunteers and 15 wristbands in the version published in 2022.',
                 'decisions': [('Processing on the phone',
                                'The watch sends PPG over Bluetooth Low Energy. The phone calculates '
                                'estimates and sends the results to the server rather than transmitting all '
                                'raw signals.'),
                               ('Signal and reference measurement',
                                'We interleaved three PPG recordings with cuff blood pressure measurements '
                                'after rest. Each recording therefore has a reference for evaluating the '
                                'estimate.'),
                               ('Different people in the test',
                                'We keep participants separate across validation folds, so the model is '
                                'tested on people who were not part of training.')],
                 'status': 'Prototype and research'},
        'education': [('2021–2025', 'PhD in Biomedical Engineering', 'University of São Paulo'),
                      ('2018–2020', 'MSc in Electrical Engineering', 'Federal University of Juiz de Fora'),
                      ('2015–2016',
                       'Exchange program in Electrical Engineering',
                       'Illinois Institute of Technology, Chicago'),
                      ('2012–2017', 'BSc in Electronic Engineering', 'Federal University of Juiz de Fora')],
        'experience': 'At InCor, I researched biomedical signals, developed ECG models and worked on software '
                      'deployment in clinical care. The projects are described on this site.',
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
                   'contribution': 'My work',
                   'location': 'Deployment location',
                   'workflow': 'Previous workflow and workflow with AI',
                   'before': 'Previous workflow',
                   'after': 'With Gorgona',
                   'client': 'The application at the unit',
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
                   'refs': 'Research references',
                   'step': 'Stage',
                   'event': 'Event',
                   'first': 'First ECG',
                   'second': 'Second ECG',
                   'official': 'Official results',
                   'home': 'Home',
                   'skip': 'Skip to content',
                   'how': 'How it works'},
        'professional_title': 'AI engineering for healthcare',
        'cv_summary': ((((('I am an electronics engineer with a PhD from the University of São Paulo. I now '
                           'work as a Senior R&D Specialist at Samsung in Campinas, Brazil. Before joining '
                           'Samsung, I worked at InCor on biomedical signals, AI models and software for '
                           'clinical care.\n'
                           '\n'
                           'My doctoral research focused on classifying ECGs directly from images. I led '
                           'team AIMED in the 2024 PhysioNet Challenge, where we placed first in the '
                           'classification task. I also led Gorgona, which brings this analysis to ECGs '
                           'recorded at urgent care units in Salvador.'))))),
        'jobs': [('Samsung R&D Institute Brazil (SRBR)',
                  '2026–present',
                  'Senior R&D Specialist',
                  'Campinas, Brazil',
                  ['I research and develop AI and software, test the implementations and evaluate the '
                   'results.']),
                 ('Heart Institute (InCor), HCFMUSP',
                  '2020–2026',
                  'Researcher / Senior Systems Analyst, Healthcare AI',
                  'São Paulo, Brazil',
                  ['I developed models to classify ECG images and worked on deploying the classifier in the '
                   'emergency department. Evaluation included cardiologist review and comparison with '
                   'specialists.',
                   'I coordinated the annotation of around 20,000 ECGs with 19 cardiologists. I organized '
                   'class definitions, readings, review of disagreements and agreement analysis.',
                   'I led team AIMED in the 2024 PhysioNet Challenge. We placed first in the classification '
                   'task, and I was the first author of the paper describing our method.',
                   'I led Gorgona and developed the initial integration between urgent care units in '
                   'Salvador, the InCor server and Telegram alerts. The system sends alerts for ECGs with '
                   'suspected ST-elevation myocardial infarction alongside telemedicine.',
                   'On RPMS, I worked with watches for remote patient monitoring. I developed collection '
                   'protocols and worked with the team on PPG processing and algorithms for estimating '
                   'physiological measurements.',
                   'I developed and evaluated language models to anonymize Portuguese clinical text. The '
                   'work included an annotated dataset, model comparisons and local execution to protect the '
                   'data.'])],
        'awards': [('2024',
                    'First place in classification in the George B. Moody PhysioNet Challenge with team '
                    'AIMED, which I led.'),
                   ('2015', 'Science without Borders scholarship, CAPES.'),
                   ('2011', 'Bronze Medal, Brazilian Physics Olympiad (OBF).')]}}
