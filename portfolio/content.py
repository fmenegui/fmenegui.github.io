"""Editorial content shared by the bilingual website and portfolio PDFs."""
LINKS = {
 'email':'mailto:f.meneguittidias@gmail.com',
 'linkedin':'https://www.linkedin.com/in/felipe-meneguitti-dias-312570b3/',
 'github':'https://github.com/fmenegui',
 'scholar':'https://scholar.google.com/citations?user=Xr5khtoAAAAJ',
 'orcid':'https://orcid.org/0000-0001-7778-4606',
 'lattes':'http://lattes.cnpq.br/3455258218368949',
 'map':'https://www.openstreetmap.org/?mlat=-12.94539&mlon=-38.44634#map=17/-12.94539/-38.44634',
 'challenge':'https://moody-challenge.physionet.org/2024/results/'
}
PAPERS = [
 ('2026','Image-based deep learning for emergency electrocardiogram classification','Dias FM et al.','medRxiv · Preprint','10.64898/2026.06.18.26355968'),
 ('2025','Exploring the limitations of blood pressure estimation using the photoplethysmography signal','Dias FM et al.','Physiological Measurement','10.1088/1361-6579/adcb86'),
 ('2024','Image-Based Electrocardiogram Classification Using Pre-trained ConvNext','Dias FM, Ribeiro E, Soares QB, Krieger JE, Gutierrez MA.','Computing in Cardiology','10.22489/CinC.2024.398'),
 ('2023','Artificial Intelligence-Driven Screening System for Rapid Image-Based Classification of 12-Lead ECG Exams: A Promising Solution for Emergency Room Prioritization','Dias FM et al.','IEEE Access','10.1109/ACCESS.2023.3328538'),
 ('2023','Blood Pressure Estimation From Photoplethysmography by Considering Intra- and Inter-Subject Variabilities: Guidelines for a Fair Assessment','da Silva Costa TB, Dias FM et al.','IEEE Access','10.1109/ACCESS.2023.3284458'),
 ('2021','Arrhythmia classification from single-lead ECG signals using the inter-patient paradigm','Dias FM et al.','Computer Methods and Programs in Biomedicine','10.1016/j.cmpb.2021.105948'),
 ('2023','Quality Assessment of Photoplethysmography Signals For Cardiovascular Biomarkers Monitoring Using Wearable Devices','Dias FM et al.','arXiv · Preprint','10.48550/arXiv.2307.08766'),
 ('2024','Machine Learning-Based Diabetes Detection Using Photoplethysmography Signal Features','Oliveira FAC, Dias FM et al.','SBCAS','10.5753/sbcas.2024.1889'),
 ('2025','Enhancing Photoplethysmography-Based Sleep Staging Models Through Temporal Context Optimization','Quino JAP, Cardenas DAC, Toledo MAF, Dias FM et al.','Studies in Health Technology and Informatics','10.3233/SHTI250897'),
 ('2022','IoT Medical Device Architecture to Estimate Non-invasive Arterial Blood Pressure','Moreno R, Dias F, Arruda M et al.','Symposium on Internet of Things (SIoT)','10.1109/SIOT56383.2022.10069878')
]
CONTENT = {
'pt': {
 'locale':'pt-BR','name':'Português','nav':['Projetos','Currículo','Publicações','Contato'],
 'role':'Engenharia de IA · Pesquisa aplicada',
 'headline':'Modelos, sinais e software para a saúde.',
 'intro':'Sou Felipe Meneguitti Dias, engenheiro e pesquisador com doutorado pela USP. Trabalho com aprendizado de máquina, visão computacional e sinais biomédicos, do desenvolvimento dos modelos à integração em sistemas de atendimento.',
 'bio':'No InCor, desenvolvi pesquisa em classificação de ECGs e liderei a implantação do Gorgona em uma unidade de pronto atendimento em Salvador.',
 'download':'Baixar portfólio','see':'Conhecer os projetos','selected':'Projetos selecionados','read':'Ver projeto','back':'Todos os projetos','article':'Ler artigo','papers':'Publicações selecionadas','about':'Currículo','contact':'Vamos conversar',
 'contact_text':'Para oportunidades em engenharia de IA, ciência de dados e pesquisa aplicada à saúde.',
 'pdf_note':'Uma versão para leitura e envio em candidaturas.','portfolio':'Portfólio profissional','updated':'Outubro de 2026',
 'gorgona':{
  'kicker':'01 / IA em serviço · InCor · 2026','title':'Gorgona','subtitle':'Classificação de ECGs integrada ao atendimento de urgência',
  'summary':'Liderei a implantação de uma plataforma que coleta ECGs nos computadores da UPA, executa o modelo no InCor e envia alertas ao grupo de regulação no Telegram.',
  'role':'Liderança do projeto e desenvolvimento inicial do sistema',
  'objective':'Antecipar a identificação de ECGs com suspeita de corrente de lesão e comunicar esses exames à equipe de regulação. A análise automática ocorre em paralelo à telemedicina. A avaliação do paciente e a decisão assistencial permanecem com a equipe médica.',
  'contribution':'Conectei o modelo de classificação ao cliente Windows, ao processamento no InCor, ao painel web e ao envio de alertas. A equipe clínica conduziu o protocolo assistencial e a avaliação dos exames.',
  'metrics':[('42.037','registros processados'),('2 min','do ECG ao alerta, no caso'),('41 min','antes do primeiro laudo')],
  'count_note':'Consulta de 03/10/2026: todas as unidades, período completo, status Processado, classes Corrente de Lesão e Outros. A contagem corresponde a registros de exames, não a pacientes únicos.',
  'location':'A implantação apresentada ocorreu na UPA Rodrigo Argolo, em Tancredo Neves, Salvador. A unidade realiza os ECGs, e o servidor do InCor concentra a execução do modelo.',
  'map_caption':'Localização cadastral aproximada. Rua Pernambuco, s/n, Salvador. CNES 7033850. Base: © OpenStreetMap contributors. Endereço: CNES/DATASUS. Coordenadas: SaúdeNoPais.',
  'before':'O ECG era enviado manualmente à telemedicina. O laudo e a avaliação médica orientavam o acionamento do grupo de regulação no Telegram. O médico da UPA também podia acionar o grupo diretamente diante de forte suspeita.',
  'after':'Acrescentamos uma via automática. O cliente detecta o arquivo, prepara o envio ao InCor e o servidor executa o modelo. Quando a probabilidade de Corrente de Lesão supera 50%, o sistema envia um alerta ao grupo configurado.',
  'flow_rows':[('Coleta','Envio manual à telemedicina','Detecção na pasta de exames'),('Análise','Avaliação médica e laudo','Classificação adicional por IA'),('Comunicação','Acionamento pela equipe','Alerta automático pelo Telegram'),('Decisão','Equipe médica e regulação','Equipe médica e regulação')],
  'client':'O ECG-IA Client acompanha a pasta de exames no Windows e coloca novos arquivos em uma fila local de envio. Cada instalação utiliza uma credencial própria. O menu na bandeja permite configurar, reiniciar e reprocessar a pasta.',
  'server':'Uma API FastAPI recebe o exame, extrai metadados e converte o traçado em imagem quando necessário. Classes e probabilidades são armazenadas em SQLite. O painel permite consultar resultados e acompanhar clientes, enquanto a integração com Telegram encaminha os alertas.',
  'privacy':'A proposta prevê anonimização no computador da UPA antes da transmissão. O recurso é configurável no cliente. HTTPS, autenticação por instalação e perfis de acesso complementam o tratamento local dos arquivos. Essas medidas descrevem a proteção técnica dos dados, sem constituir uma avaliação formal de conformidade integral com a LGPD.',
  'dashboard':'A plataforma online permite filtrar por unidade, período, status e classe. A tela abaixo mostra a consulta à classe Corrente de Lesão entre 02/10 e 03/10/2026, diferente do filtro usado para a contagem de 42.037 registros.',
  'case':'Em 20 de maio de 2026, um atendimento na UPA Rodrigo Argolo permitiu acompanhar o fluxo completo. A admissão ocorreu às 18h52. Os dois ECGs geraram alertas automáticos 2 minutos após sua realização. A chegada ao centro de referência foi registrada às 20h44.',
  'timeline_caption':'Trecho da linha do tempo original do estudo de caso, slide 23. O recorte omite o bloco de identificação pessoal e começa no primeiro ECG. Admissão: 18h52.',
  'case_rows':[('Realização do ECG','19h15','19h37'),('Alerta da IA','19h17','19h39'),('Chegada à telemedicina','19h21','19h39'),('Emissão do laudo','19h58','20h04'),('Do exame ao alerta','2 min','2 min'),('Antecedência em relação ao laudo','41 min','25 min')],
  'case_result':'O primeiro alerta chegou 4 minutos antes de o ECG entrar na telemedicina. A antecedência em relação aos laudos foi de 41 e 25 minutos. O caso demonstra a antecipação da informação à regulação. Não permite atribuir à IA uma redução no tempo até o tratamento ou nos desfechos clínicos.',
  'model':'O modelo de emergência usa um ensemble ConvNeXt para 12 categorias. O estudo inclui 18.519 ECGs de 14.402 pacientes, com anotação de 19 cardiologistas. No teste reservado, o macro F1 foi de 0,807 (IC 95%: 0,788 a 0,825). Esses números descrevem a pesquisa do classificador, separadamente do volume processado em serviço. [1]',
 },
 'incor':{'kicker': '02 / Integração hospitalar · InCor · 2023',
 'title': 'ECG na emergência do InCor',
 'subtitle': 'Do PACS à tela da equipe médica',
 'summary': 'Desenvolvi pesquisa em classificação de imagens de ECG e uma proposta de integração à infraestrutura '
            'hospitalar, com os resultados apresentados em uma aplicação web na emergência.',
 'role': 'Desenvolvimento do método e primeiro autor do artigo no IEEE Access',
 'objective': 'Apoiar a priorização da revisão médica dos ECGs na emergência, levando a classificação automática '
              'ao ambiente de trabalho da equipe assistencial.',
 'method': 'O exame de 12 derivações entra na infraestrutura hospitalar em formato DICOM e é armazenado no PACS, '
           'o sistema de arquivamento e comunicação de imagens. O módulo de IA acessa a imagem do ECG, realiza o '
           'pré-processamento e executa uma rede neural convolucional. A figura também prevê idade, sexo e etnia '
           'como entradas do classificador.',
 'result': 'A saída do modelo organiza os exames em três classes: fibrilação atrial, outros e normal. Uma '
           'aplicação web apresenta essas classificações na tela da emergência, com cores que permitem à equipe '
           'identificar os exames sinalizados para revisão prioritária.',
 'scope': 'O artigo de 2023 apresenta essa arquitetura de integração. A figura documenta a proposta e a '
          'interface, sem estabelecer, por si só, o volume de uso em rotina ou uma redução no tempo de '
          'atendimento.',
 'caption': 'Figura 1 do artigo de Dias et al., IEEE Access (2023). Integração proposta entre aquisição do ECG, '
            'DICOM/PACS, classificador e aplicação web na emergência. Imagem fornecida pelo autor.',
 'workflow': [('Aquisição e armazenamento', 'ECG de 12 derivações em DICOM, armazenado no PACS.'),
              ('Processamento', 'Pré-processamento da imagem e classificação por uma CNN.'),
              ('Resultado', 'Fibrilação atrial, outros ou normal.'),
              ('Uso pela equipe',
               'Resultados na aplicação web da emergência para apoiar a priorização da revisão médica.')]},
 'physionet':{
  'kicker':'02 / Classificação de imagens · 2024','title':'PhysioNet Challenge','subtitle':'Primeiro lugar em classificação de ECGs',
  'summary':'Integrei a equipe AIMED, vencedora da tarefa de classificação do George B. Moody PhysioNet Challenge 2024, com macro F1 de 0,817 no teste oculto reportado no artigo.',
  'role':'Integrante da equipe AIMED e primeiro autor do artigo',
  'method':'Usamos ConvNeXt com pré-treinamento em imagens de ECG, ajuste no PTB-XL e um ensemble de cinco modelos. O trabalho avaliou a classificação de 11 categorias diretamente nas imagens.',
  'result':'A participação reuniu treinamento, avaliação em dados ocultos e análise de diferentes condições de aquisição. O prêmio se refere à tarefa de classificação, conduzida separadamente da digitalização dos traçados.',
  'team':'Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger e Marco A. Gutierrez.',
 },
 'rpms':{'kicker': '03 / Monitoramento remoto · InCor',
 'title': 'RPMS',
 'subtitle': 'Do sinal no relógio ao acompanhamento médico',
 'summary': 'Atuei na coleta de dados com relógios protótipos, na criação de protocolos e no desenvolvimento de '
            'algoritmos de PPG para um sistema de monitoramento remoto de pacientes.',
 'role': 'Protocolos de coleta, processamento de sinais e pesquisa de algoritmos',
 'objective': 'Permitir o acompanhamento de pacientes fora do hospital, conectando sinais coletados por '
              'dispositivos vestíveis a biomarcadores disponíveis para a equipe médica.',
 'contribution': 'Minha atuação reuniu protocolos de coleta com relógios protótipos, organização dos dados, '
                 'pré-processamento de sinais de fotopletismografia (PPG) e desenvolvimento de algoritmos em '
                 'equipe.',
 'method': 'O relógio envia o PPG ao aplicativo Android por Bluetooth Low Energy. O celular processa o sinal, estima pressão arterial e frequência cardíaca e envia os resultados por MQTT ao servidor ThingsBoard. O painel permite acompanhar as medidas de cada paciente ao longo do tempo.',
 'research': 'A pesquisa abrangeu qualidade do sinal, estimativa de pressão arterial, classificação relacionada '
             'ao diabetes e análise do sono. Os artigos abaixo documentam essas frentes de desenvolvimento.',
 'caption': 'Arquitetura publicada em Moreno, Dias et al. (SIoT, 2022), Figura 1. O processamento ocorre no celular.',
 'biomarkers': [('Qualidade do sinal', 'Avaliação automática da qualidade dos segmentos de PPG.', 6),
                ('Pressão arterial', 'Estimativa com calibração e avaliação dos limites de generalização.', 1),
                ('Diabetes', 'Classificação a partir de características do PPG e metadados.', 7),
                ('Sono', 'Classificação de estágios do sono com contexto temporal.', 8)]},
 'ppg':{
  'kicker':'03 / Sinais biomédicos · 2023–2025','title':'Pressão arterial por PPG','subtitle':'Avaliação dos limites da predição',
  'summary':'Investiguei o que a fotopletismografia pode oferecer à estimativa de pressão arterial e como avaliar modelos sem superestimar sua capacidade de generalização.',
  'role':'Pesquisa em equipe e primeiro autor do estudo publicado em 2025',
  'method':'No estudo de 2025, usamos uma ResNet siamesa com calibração e comparamos sinais normalizados de PPG e de pressão arterial invasiva. O objetivo foi separar informação útil do sinal e limitações da estimativa.',
  'result':'O estudo mostrou que a informação correlacionada à pressão no PPG não foi suficiente para uma predição precisa nas condições avaliadas. O resultado ajuda a definir expectativas realistas para esse tipo de modelo.',
  'team':'Felipe M. Dias, Diego A. C. Cardenas, Marcelo A. F. Toledo, Filipe A. C. Oliveira, Estela Ribeiro, José E. Krieger e Marco A. Gutierrez.',
 },
 'education':[('2021–2025','Doutorado em Engenharia Elétrica','Universidade de São Paulo'),('2018–2020','Mestrado em Engenharia Elétrica','Universidade Federal de Juiz de Fora'),('2015–2016','Intercâmbio em Engenharia Elétrica','Illinois Institute of Technology, Chicago'),('2012–2017','Graduação em Engenharia Eletrônica','Universidade Federal de Juiz de Fora')],
 'experience':'Minha experiência no InCor reúne pesquisa em sinais biomédicos, desenvolvimento de modelos para ECG e implantação de software em ambientes assistenciais. Gorgona, ECG na emergência e RPMS representam essas frentes neste portfólio.',
 'skills':[('Modelagem','PyTorch, ConvNeXt, aprendizado por transferência e ensembles.'),('Avaliação','Validação entre pacientes, anotação especializada e avaliação em dados reservados.'),('Software','Python, FastAPI, Docker, SQLite e integração com Telegram.')],
 'labels':{'objective':'Objetivo','contribution':'Minha atuação','location':'Local da implantação','workflow':'Do fluxo anterior à proposta','before':'Fluxo anterior','after':'Com o Gorgona','client':'O programa na UPA','server':'Servidor e plataforma online','privacy':'Proteção de dados e LGPD','case':'Estudo de caso','model':'Base científica do modelo','method':'Abordagem','result':'Resultado','team':'Equipe','education':'Formação','experience':'Experiência','skills':'Competências aplicadas','refs':'Artigos de referência','step':'Etapa','event':'Evento','first':'Primeiro ECG','second':'Segundo ECG','openmap':'Abrir mapa','official':'Resultados oficiais','notes':'Notas de estudo','notes_text':'Materiais sobre experimentação, estatística e programação no site original. Conteúdo em inglês.','home':'Início','skip':'Ir para o conteúdo'}
},
'en': {
 'locale':'en','name':'English','nav':['Projects','CV','Publications','Contact'],
 'role':'AI engineering · Applied research',
 'headline':'Models, signals and software for healthcare.',
 'intro':'I am Felipe Meneguitti Dias, an engineer and researcher with a PhD from the University of São Paulo. I work on machine learning, computer vision and biomedical signals, from model development to integration into healthcare systems.',
 'bio':'At InCor, I developed research on ECG classification and led the deployment of Gorgona at an urgent care unit in Salvador, Brazil.',
 'download':'Download portfolio','see':'Explore my projects','selected':'Selected projects','read':'View project','back':'All projects','article':'Read paper','papers':'Selected publications','about':'CV','contact':'Get in touch',
 'contact_text':'For opportunities in AI engineering, data science and applied healthcare research.',
 'pdf_note':'A standalone portfolio for applications and sharing.','portfolio':'Professional portfolio','updated':'October 2026',
 'gorgona':{
  'kicker':'01 / Deployed AI · InCor · 2026','title':'Gorgona','subtitle':'ECG classification integrated into urgent care',
  'summary':'I led the deployment of a platform that collects ECGs from computers at an urgent care unit, runs the model at InCor and sends alerts to the clinical coordination group on Telegram.',
  'role':'Project leadership and initial system development',
  'objective':'Flag ECGs with suspected current of injury and notify the clinical coordination team earlier. Automated analysis runs alongside the telemedicine workflow. Patient assessment and care decisions remain with the medical team.',
  'contribution':'I connected the classification model to the Windows client, InCor processing server, web dashboard and Telegram alerts. The clinical team managed the care protocol and reviewed the ECGs.',
  'metrics':[('42,037','processed records'),('2 min','ECG to alert in the case'),('41 min','before the first report')],
  'count_note':'Dashboard query on October 3, 2026: all units, full period, Processed status, Current of Injury and Other classes. The count represents examination records, not unique patients.',
  'location':'The deployment presented here took place at UPA Rodrigo Argolo, an urgent care unit in Tancredo Neves, Salvador, Brazil. ECGs are acquired at the unit and the model runs remotely on the InCor server.',
  'map_caption':'Approximate registry location. Rua Pernambuco, s/n, Salvador. CNES 7033850. Map: © OpenStreetMap contributors. Address: CNES/DATASUS. Coordinates: SaúdeNoPais.',
  'before':'ECGs were manually sent to telemedicine. The report and medical assessment informed whether to contact the coordination group on Telegram. The physician could also contact the group directly when clinical suspicion was high.',
  'after':'We added an automated path. The client detects the file, prepares the upload and sends it to InCor for classification. When the probability of the Current of Injury class exceeds 50%, the system sends an alert to the configured group.',
  'flow_rows':[('Collection','Manual telemedicine submission','Automatic folder monitoring'),('Analysis','Medical review and report','Additional AI classification'),('Communication','Staff-initiated contact','Automated Telegram alert'),('Decision','Medical and coordination teams','Medical and coordination teams')],
  'client':'The ECG-IA Client monitors an examination folder on Windows and queues new files for upload. Each installation has its own credential. A system tray menu provides configuration, restart and folder reprocessing controls.',
  'server':'A FastAPI endpoint receives the examination, extracts metadata and converts the tracing into an image when needed. Classes and probabilities are stored in SQLite. The dashboard supports result queries and client monitoring, while the Telegram integration delivers alerts.',
  'privacy':'The proposed workflow includes anonymization on the unit’s computer before transmission. This feature is configurable in the client. HTTPS, per-installation authentication and access roles complement local file processing. These are technical data protection measures, not a formal assessment of full compliance with Brazil’s LGPD.',
  'dashboard':'The online platform supports filtering by unit, period, status and class. This screenshot shows the Current of Injury query for October 2–3, 2026, which differs from the query used for the 42,037-record count.',
  'case':'On May 20, 2026, one encounter at UPA Rodrigo Argolo provided a complete record of the alert workflow. Admission was at 18:52. Both ECGs triggered automated alerts 2 minutes after acquisition. Arrival at the referral center was recorded at 20:44.',
  'timeline_caption':'Excerpt from the original case-study timeline, slide 23. The crop excludes the personal identification block and starts at the first ECG. Admission: 18:52. Original figure in Portuguese.',
  'case_rows':[('ECG acquisition','19:15','19:37'),('AI alert','19:17','19:39'),('Arrival at telemedicine','19:21','19:39'),('Report issued','19:58','20:04'),('ECG to alert','2 min','2 min'),('Lead time before report','41 min','25 min')],
  'case_result':'The first alert arrived 4 minutes before the ECG reached telemedicine. Alerts preceded the corresponding reports by 41 and 25 minutes. The case demonstrates earlier information delivery to the coordination team. It does not establish a causal reduction in treatment time or improved clinical outcomes.',
  'model':'The emergency model uses a ConvNeXt ensemble for 12 categories. The study includes 18,519 ECGs from 14,402 patients, annotated by 19 cardiologists. Held-out macro F1 was 0.807 (95% CI: 0.788–0.825). These figures describe the classifier study, separately from operational processing volume. [1]',
 },
 'incor':{'kicker': '02 / Hospital integration · InCor · 2023',
 'title': 'ECG classification at InCor',
 'subtitle': 'From PACS to the emergency room screen',
 'summary': 'I developed research on ECG image classification and a proposed integration with hospital '
            'infrastructure, presenting results in an emergency room web application.',
 'role': 'Method development and first author of the IEEE Access paper',
 'objective': 'Support the prioritization of ECG review in the emergency room by bringing automated '
              'classification into the clinical team’s workspace.',
 'method': 'The 12-lead examination enters the hospital infrastructure in DICOM format and is stored in PACS, the '
           'picture archiving and communication system. The AI module retrieves the ECG image, preprocesses it '
           'and runs a convolutional neural network. The diagram also includes age, sex and ethnicity as '
           'classifier inputs.',
 'result': 'The model assigns one of three classes: atrial fibrillation, other or normal. A web application '
           'displays these classifications on the emergency room screen, using colors to help the clinical team '
           'identify examinations flagged for priority review.',
 'scope': 'The 2023 paper presents this integration architecture. The figure documents the proposal and interface '
          'but does not, by itself, establish routine usage volume or a reduction in care delays.',
 'caption': 'Figure 1 from Dias et al., IEEE Access (2023). Proposed integration of ECG acquisition, DICOM/PACS, '
            'classification and the emergency room web application. Image provided by the author.',
 'workflow': [('Acquisition and storage', '12-lead ECG in DICOM format, stored in PACS.'),
              ('Processing', 'Image preprocessing and classification by a CNN.'),
              ('Output', 'Atrial fibrillation, other or normal.'),
              ('Clinical use',
               'Results in the emergency room web application to support prioritization of medical review.')]},
 'physionet':{
  'kicker':'02 / Image classification · 2024','title':'PhysioNet Challenge','subtitle':'First place in ECG classification',
  'summary':'I contributed to AIMED, the winning team in the classification task of the 2024 George B. Moody PhysioNet Challenge, with a hidden-test macro F1 of 0.817 reported in our paper.',
  'role':'AIMED team member and first author of the paper',
  'method':'We used ConvNeXt pretrained on ECG images, fine-tuned on PTB-XL, with a five-model ensemble. The work evaluated classification of 11 categories directly from images.',
  'result':'The entry combined model training, hidden-data evaluation and analysis across image acquisition conditions. The award was for classification, a separate task from ECG waveform digitization.',
  'team':'Felipe M. Dias, Estela Ribeiro, Quenaz B. Soares, José E. Krieger and Marco A. Gutierrez.',
 },
 'rpms':{'kicker': '03 / Remote monitoring · InCor',
 'title': 'RPMS',
 'subtitle': 'From wearable signals to clinical follow-up',
 'summary': 'I worked on data collection with prototype watches, study protocols and PPG algorithms for a remote '
            'patient monitoring system.',
 'role': 'Data collection protocols, signal processing and algorithm research',
 'objective': 'Support patient follow-up outside the hospital by connecting wearable recordings to biomarkers '
              'available to the clinical team.',
 'contribution': 'My work covered collection protocols with prototype watches, data organization, '
                 'photoplethysmography (PPG) preprocessing and collaborative algorithm development.',
 'method': 'The watch sends PPG to the Android app over Bluetooth Low Energy. The phone processes the signal, estimates blood pressure and heart rate, and sends results over MQTT to a ThingsBoard server. The dashboard displays each patient’s measurements over time.',
 'research': 'Research covered signal quality, blood pressure estimation, diabetes-related classification and '
             'sleep analysis. The papers below document these development areas.',
 'caption': 'Architecture published in Moreno, Dias et al. (SIoT, 2022), Figure 1. Signals are processed on the phone.',
 'biomarkers': [('Signal quality', 'Automated assessment of PPG segment quality.', 6),
                ('Blood pressure', 'Calibrated estimation and evaluation of generalization limits.', 1),
                ('Diabetes', 'Classification using PPG features and patient metadata.', 7),
                ('Sleep', 'Sleep stage classification using temporal context.', 8)]},
 'ppg':{
  'kicker':'03 / Biomedical signals · 2023–2025','title':'Blood pressure from PPG','subtitle':'Understanding prediction limits',
  'summary':'I investigated what photoplethysmography can contribute to blood pressure estimation and how to assess models without overstating their ability to generalize.',
  'role':'Collaborative research and first author of the 2025 study',
  'method':'In the 2025 study, we used a calibration-based Siamese ResNet and compared normalized PPG and invasive arterial pressure signals. The aim was to distinguish useful signal information from estimation limitations.',
  'result':'The study found that blood-pressure-correlated information in PPG was insufficient for accurate prediction under the evaluated conditions. The result helps set realistic expectations for this type of model.',
  'team':'Felipe M. Dias, Diego A. C. Cardenas, Marcelo A. F. Toledo, Filipe A. C. Oliveira, Estela Ribeiro, José E. Krieger and Marco A. Gutierrez.',
 },
 'education':[('2021–2025','PhD in Electrical Engineering','University of São Paulo'),('2018–2020','MSc in Electrical Engineering','Federal University of Juiz de Fora'),('2015–2016','Exchange program in Electrical Engineering','Illinois Institute of Technology, Chicago'),('2012–2017','BSc in Electronic Engineering','Federal University of Juiz de Fora')],
 'experience':'My experience at InCor spans biomedical signal research, ECG model development and software deployment in healthcare settings. Gorgona brings these areas together in this portfolio.',
 'skills':[('Modeling','PyTorch, ConvNeXt, transfer learning and ensembles.'),('Evaluation','Inter-patient validation, expert annotation and held-out evaluation.'),('Software','Python, FastAPI, Docker, SQLite and Telegram integration.')],
 'labels':{'objective':'Objective','contribution':'My role','location':'Deployment location','workflow':'From the previous workflow to the proposal','before':'Previous workflow','after':'With Gorgona','client':'The application at the unit','server':'Server and online platform','privacy':'Data protection and LGPD','case':'Case study','model':'Scientific basis','method':'Approach','result':'Result','team':'Team','education':'Education','experience':'Experience','skills':'Applied skills','refs':'Research references','step':'Stage','event':'Event','first':'First ECG','second':'Second ECG','openmap':'Open map','official':'Official results','notes':'Study notes','notes_text':'Material on experimentation, statistics and programming from the original website. Content in English.','home':'Home','skip':'Skip to content'}
}}
