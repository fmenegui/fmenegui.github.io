#!/usr/bin/env python3
"""Build the bilingual portfolio and CV."""
from pathlib import Path
from html import escape as e
from hashlib import sha256
import json
import shutil
import subprocess
import sys
from content import CONTENT, LINKS, PAPERS
from challenge import CHALLENGE_LINKS
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
ASSETS=Path(__file__).parent/'assets'
PROJECTS=('gorgona','incor','physionet','rpms')
READING=json.loads((Path(__file__).parent/'current-reading.json').read_text(encoding='utf-8'))
OUT.mkdir(exist_ok=True)
shutil.copytree(ASSETS,OUT/'assets',dirs_exist_ok=True,ignore=shutil.ignore_patterns('README.md'))
for withdrawn in ['README.md']:
 (OUT/'assets'/withdrawn).unlink(missing_ok=True)
shutil.copy(Path(__file__).parent/'style.css',OUT/'assets/style.css')
CSS_VERSION=sha256((OUT/'assets/style.css').read_bytes()).hexdigest()[:12]
shutil.copytree(Path(__file__).parent/'downloads',OUT/'downloads',dirs_exist_ok=True)
PDF_VERSIONS={lang:sha256((OUT/'downloads'/f'Felipe_Dias_Portfolio_{lang.upper()}.pdf').read_bytes()).hexdigest()[:12] for lang in CONTENT}

def institution(c):
 name=('Instituto do Coração (InCor), Hospital das Clínicas da Faculdade de Medicina da Universidade de São Paulo' if c['locale']=='pt-BR' else 'Heart Institute (InCor), Hospital das Clínicas, University of São Paulo Medical School')
 return '<p class="institution"><a href="https://www.incor.usp.br/">'+name+'</a></p>'

def par(t):return '<p>'+e(t)+'</p>'
def table(head,rows):return '<div class="table-scroll"><table><thead><tr>'+''.join('<th scope="col">'+e(x)+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+e(x)+('</th>' if i==0 else '</td>') for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def fig(base,file,caption):return f'<figure><a class="image-link" href="{base}assets/{file}"><img src="{base}assets/{file}" alt="{e(caption)}" loading="lazy"></a><figcaption>{e(caption)}</figcaption></figure>'
def refs(indices):
 return '<ol class="refs">'+''.join(f'<li>{e(PAPERS[i][2])} <a href="https://doi.org/{PAPERS[i][4]}">{e(PAPERS[i][1])}</a>. <small>{e(PAPERS[i][3])}, {PAPERS[i][0]}.</small></li>' for i in indices)+'</ol>'
def metrics(c):return '<div class="metrics">'+''.join(f'<div class="metric"><strong>{a}</strong><span>{b}</span></div>' for a,b in c['gorgona']['metrics'])+'</div>'
def section(title,text,id=''):
 anchor=f' id="{e(id)}"' if id else ''
 return f'<section class="article-section"{anchor}><h2>{e(title)}</h2>{par(text)}</section>'
def social():return '<div class="social">'+''.join(f'<a href="{LINKS[k]}">{label}</a>' for k,label in [('linkedin','LinkedIn'),('github','GitHub'),('scholar','Google Scholar'),('orcid','ORCID'),('lattes','Lattes')])+'</div>'
def publications(cv=False):
 return '<ol class="pub-list">'+''.join(f'<li><time>{yr}</time><div><h3><a href="https://doi.org/{doi}">{e(title)}</a></h3><p>{e(authors)} · {e(venue)}</p></div></li>' for i,(yr,title,authors,venue,doi) in sorted(enumerate(PAPERS),key=lambda item:-int(item[1][0])) if cv or i!=2)+'</ol>'
def education(c):return '<ol class="education">'+''.join(f'<li><time>{date}</time><div><strong>{e(name)}</strong><small>{e(school)}</small></div></li>' for date,name,school in c['education'])+'</ol>'
def home(c,base,lang):
 pdf=f'{base}downloads/Felipe_Dias_Portfolio_{lang.upper()}.pdf?v={PDF_VERSIONS[lang]}'
 s=f'<section class="hero"><div class="hero-copy"><h1>Felipe Meneguitti Dias</h1><p class="location">{e(c["location"])}</p><p class="intro">{e(c["intro"])}</p><p class="email-line"><a href="{LINKS["email"]}">f.meneguittidias@gmail.com</a></p>{social()}<p class="profile-links"><a href="{pdf}">{c["download"]} (PDF)</a><a href="about.html">{c["about"]}</a></p></div><figure class="portrait-frame"><a class="image-link" href="{base}assets/felipe.jpg"><img class="portrait" src="{base}assets/felipe.jpg" alt="Felipe Meneguitti Dias" width="400" height="400" fetchpriority="high" decoding="async"></a></figure></section>'
 s+=f'<section class="section" id="projects"><div class="section-head"><h2>{c["selected"]}</h2></div>'+institution(c)
 for key in PROJECTS:
  v=c[key]
  imagefile={'gorgona':'flows.png','incor':'incor-integration.png','physionet':'physionet-award.jpg','rpms':'rpms-app.jpeg'}[key]
  thumb=f'<div class="project-media"><a class="project-thumb {key}-thumb" href="projects/{key}.html" aria-label="{e(v["title"])}"><img src="{base}assets/{imagefile}" alt="" loading="lazy" decoding="async"></a></div>'
  doi=PAPERS[{'gorgona':0,'incor':3,'physionet':2,'rpms':9}[key]][4]
  s+=f'<article class="project">{thumb}<div class="project-copy"><h3><a href="projects/{key}.html">{e(v["title"])}</a></h3><p class="project-info">{e(v["status"])} · {e(v["period"])}</p><p class="desc">{e(v["summary"])}</p><p class="project-links"><a href="projects/{key}.html">{c["read"]}</a><a href="https://doi.org/{doi}">{c["article"]}</a></p></div></article>'
 s+='</section>'
 # Filled from rendered article metadata by the shared UI pass.
 s+='<section class="section blog-feature" id="blog"></section>'
 return s
def challenge(c,base,s):
 v=c['physionet']
 def paragraphs(items):return ''.join(par(t) for t in items)
 s+='<div class="challenge-story">'
 s+=f'<section class="article-section" id="story"><h2>{e(v["opening_title"])}</h2>{paragraphs(v["opening"])}</section>'
 s+=f'<figure class="award-photo"><a class="image-link" href="{base}assets/physionet-award.jpg"><img src="{base}assets/physionet-award.jpg" alt="{e(v["award_alt"])}" width="783" height="556" decoding="async" fetchpriority="high"></a><figcaption>{e(v["award_caption"])} {e(v["photo_source"])}</figcaption></figure>'
 s+=f'<nav class="contents" aria-label="{("Nesta página" if c["locale"]=="pt-BR" else "On this page")}">'+''.join(f'<a href="#{key}">{e(v[label])}</a>' for key,label in [('challenge','challenge_title'),('pretraining','pretraining_title'),('results','results_title'),('news','news_title')])+'</nav>'
 s+=section(v['challenge_title'],v['challenge_text'],'challenge')
 s+=f'<section class="article-section"><h2>{e(v["challenge_2024_title"])}</h2>{par(v["challenge_2024_text"])}<dl class="challenge-tasks">'+''.join(f'<div><dt>{e(title)}</dt><dd>{e(text)}</dd></div>' for title,text in v['tasks'])+'</dl>'+par(v['evaluation'])+'</section>'
 s+=f'<section class="article-section" id="classification"><h2>{e(v["classification_title"])}</h2>{paragraphs(v["classification"])}</section>'
 s+=f'<section class="article-section"><h2>{e(v["doctoral_title"])}</h2>{par(v["doctoral_text"])}<ul>'+''.join(f'<li>{e(t)}</li>' for t in v['doctoral_tests'])+'</ul>'+par(v['doctoral_note'])+'</section>'
 s+=f'<section class="article-section" id="pretraining"><h2>{e(v["pretraining_title"])}</h2>{paragraphs(v["pretraining"])}{table(v["pretraining_head"],v["pretraining_rows"])}<p class="note">{e(v["pretraining_caption"])} <a href="{CHALLENGE_LINKS["thesis"]}">{e(v["thesis_link"])}</a>.</p></section>'
 s+=f'<section class="article-section" id="method"><h2>{e(v["method_title"])}</h2>{par(v["method_intro"])}<figure class="method-figure"><a class="image-link" href="{base}assets/physionet-method.png"><img src="{base}assets/physionet-method.png" alt="{e(v["method_alt"])}" width="2000" height="1451" loading="lazy" decoding="async"></a><figcaption>{e(v["method_caption"])}</figcaption></figure><ol class="training-stages">'+''.join(f'<li><strong>{e(title)}</strong><p>{e(text)}</p></li>' for title,text in v['training_steps'])+'</ol>'+par(v['method_detail'])+par(v['split_note'])+'</section>'
 s+=f'<section class="article-section" id="results"><h2>{e(v["results_title"])}</h2>{par(v["results_text"])}{table(v["results_head"],v["results_rows"])}<p><a href="{CHALLENGE_LINKS["ranking"]}">{e(v["ranking_link"])}</a></p>{par(v["results_note"])}<figure class="certificate-photo"><a class="image-link" href="{base}assets/physionet-certificate.jpg"><img src="{base}assets/physionet-certificate.jpg" alt="{e(v["certificate_alt"])}" width="1536" height="1152" loading="lazy" decoding="async"></a><figcaption>{e(v["certificate_caption"])}</figcaption></figure></section>'
 s+=section(v['team_title'],v['team_text'])
 s+=f'<section class="article-section" id="news"><h2>{e(v["news_title"])}</h2><ul class="news-list">'+''.join(f'<li><a href="{CHALLENGE_LINKS[key]}">{e(outlet)}</a><span class="news-date"> · {e(date)}</span><p>{e(description)}</p></li>' for key,outlet,date,description in v['news_entries'])+f'</ul><h3>{e(v["association_title"])}</h3>{par(v["association_text"])}<a href="{CHALLENGE_LINKS["photo"]}">{e(v["association_link"])}</a></section>'
 s+=f'<section class="article-section" id="history"><h2>{e(v["history_title"])}</h2>{par(v["history_text"])}{table(v["history_head"],v["history_rows"])}<p><a href="{CHALLENGE_LINKS["history"]}">{e(v["history_link"])}</a></p></section>'
 s+=f'<section class="article-section"><h2>{e(v["sources_title"])}</h2><ul class="challenge-sources">'+''.join(f'<li><a href="{CHALLENGE_LINKS[key]}">{e(v[key+"_link"])}</a></li>' for key in ['paper','thesis','official','awards'])+'</ul>'+refs([2,10])+'</section>'
 return s+'</div>'
def detail(c,key,base):
 v=c[key];l=c['labels']
 subtitle=f'<p class="subtitle">{e(v["subtitle"])}</p>' if v['subtitle'] else ''
 s=f'<header class="detail-top"><a class="back" href="../index.html#projects">← {c["back"]}</a><p class="eyebrow">{v["kicker"]}</p><h1>{v["title"]}</h1>{subtitle}</header>'
 s+=institution(c)
 if key=='physionet':return challenge(c,base,s)
 s+=section(l['objective'],v['objective'],'objective')+section(l['contribution'],v['contribution'])
 if key=='rpms':
  lang='pt' if c['locale']=='pt-BR' else 'en'
  s+=f'<section class="article-section"><h2>{"Como funciona" if lang=="pt" else "How it works"}</h2>{fig(base,"rpms-architecture.jpeg",v["caption"])}{par(v["method"])}</section>'
  evidence=('Na arquitetura publicada em 2022, o aplicativo mantinha o histórico das medidas no celular e enviava ao servidor as estimativas de pressão sistólica, diastólica e frequência cardíaca.' if lang=='pt' else 'In the architecture published in 2022, the app kept a history of measurements on the phone and sent systolic pressure, diastolic pressure and heart rate estimates to the server.')
  appcap=('Aplicativo Android: coleta de PPG, medidas e histórico. Figura 3, SIoT 2022.' if lang=='pt' else 'Android app: PPG recording, measurements and history. Figure 3, SIoT 2022.')
  dashcap=('Painel ThingsBoard com as medidas recebidas. Figura 4, SIoT 2022.' if lang=='pt' else 'ThingsBoard dashboard showing the measurements received. Figure 4, SIoT 2022.')
  s+=f'<section class="article-section"><h2>{l["result"]}</h2>{par(evidence)}<div class="rpms-gallery">{fig(base,"rpms-app.jpeg",appcap)}{fig(base,"rpms-dashboard.jpeg",dashcap)}</div></section>'
  protocol=('No protocolo de 2022, cada voluntário descansava por 10 minutos. Depois, fazia três coletas de um minuto de PPG, intercaladas com medidas de pressão por manguito. Processamos o sinal com filtro de 0,5 a 10 Hz, reamostragem de 200 para 125 Hz e janelas de 8 segundos. Na validação, os participantes do teste eram separados dos usados no treinamento.' if lang=='pt' else 'Under the 2022 protocol, volunteers rested for 10 minutes, then completed three one-minute PPG recordings with cuff blood pressure measurements in between. Signal processing used a 0.5–10 Hz filter, resampling from 200 to 125 Hz and 8-second windows. Test participants were kept separate from those used for training.')
  s+=f'<details class="technical"><summary>{"Protocolo e processamento do sinal" if lang=="pt" else "Collection protocol and signal processing"}</summary>{par(protocol)}{fig(base,"rpms-protocol.png","SIoT 2022 · Figure 2")}</details>'
  s+=f'<section class="article-section"><h2>{"Algoritmos e pesquisa" if lang=="pt" else "Algorithms and research"}</h2>{par(v["research"])}<div class="biomarker-grid">'
  for name,description,i in v['biomarkers']:
   s+=f'<div><h3>{e(name)}</h3>{par(description)}<a href="https://doi.org/{PAPERS[i][4]}">{c["article"]} ({PAPERS[i][0]})</a></div>'
  s+='</div></section>'
  return s+f'<section class="article-section"><h2>{l["refs"]}</h2>{refs([9,6,1,4,7,8])}</section>'
 if key=='incor':
  s+=f'<section class="article-section"><h2>{l["how"]}</h2><figure class="incor-figure"><div class="figure-window"><a class="image-link" href="{base}assets/incor-integration.png"><img src="{base}assets/incor-integration.png" alt="{e(v["caption"])}"></a></div><figcaption>{e(v["caption"])}</figcaption></figure>{par(v["method"])}{table([l["step"],l["method"]],v["workflow"])}</section>'
  s+=section(l['result'],v['result'])+par(v['scope'])
  s+=''
  return s+f'<section class="article-section"><h2>{l["refs"]}</h2>{refs([3,0,10])}</section>'
 s+='<figure class="gorgona-flow"><div class="flow-window"><a class="image-link" href="'+base+'assets/flows.png"><img src="'+base+'assets/flows.png" alt="'+('Fluxo proposto com IA: cliente, anonimização, servidor InCor e alerta no Telegram, em paralelo à telemedicina.' if c['locale']=='pt-BR' else 'Proposed AI workflow: client, anonymization, InCor server and Telegram alerts alongside telemedicine.')+'"></a></div><figcaption>'+('Fluxo proposto com IA. Figura original do projeto.' if c['locale']=='pt-BR' else 'Proposed AI workflow. Original project figure, with Portuguese labels.')+'</figcaption></figure>'
 s+=metrics(c)
 s+='<nav class="contents" aria-label="'+('Nesta página' if c['locale']=='pt-BR' else 'On this page')+'">'+''.join(f'<a href="#{k}">{l[k]}</a>' for k in ['objective','workflow','server','case'])+'</nav>'
 s+=f'<section class="article-section"><h2>{l["location"]}</h2>{par(v["location"])}{fig(base,"upa-map-"+("pt" if c["locale"]=="pt-BR" else "en")+".webp",v["map_caption"])}</section>'
 s+=f'<section class="article-section" id="workflow"><h2>{l["how"]}</h2><div class="split"><div><h3>{l["before"]}</h3>{par(v["before"])}</div><div><h3>{l["after"]}</h3>{par(v["after"])}</div></div>{fig(base,"flows.png",l["workflow"]+(". Diagramas originais do projeto." if c["locale"]=="pt-BR" else ". Original project diagrams in Portuguese."))}{table([l["step"],l["before"],l["after"]],v["flow_rows"])}</section>'
 s+='<details class="technical implementation"><summary>'+('Cliente Windows, servidor e plataforma online' if c['locale']=='pt-BR' else 'Windows client, server and online platform')+'</summary>'
 s+=f'<section class="article-section"><h2>{l["client"]}</h2>{par(v["client"])}<div class="two-images">{fig(base,"client-install.png","ECG-IA Client 1.6.66 · Windows")}{fig(base,"client-menu.png","ECG-IA Client · "+("Menu na bandeja do Windows" if c["locale"]=="pt-BR" else "Windows system tray menu"))}</div></section>'
 s+=f'<section class="article-section" id="server"><h2>{l["server"]}</h2>{par(v["server"])}{fig(base,"architecture.png",("Arquitetura do sistema." if c["locale"]=="pt-BR" else "System architecture. Original labels in Portuguese."))}<h3>{l["privacy"]}</h3>{par(v["privacy"])}{par(v["dashboard"])}{fig(base,"dashboard.png",("Painel do Gorgona: filtros e resultados de classificação." if c["locale"]=="pt-BR" else "Gorgona dashboard: filters and classification results."))}</section>'
 s+='</details>'
 s+=f'<section class="article-section" id="case"><h2>{l["result"]}</h2><h3>{l["case"]}</h3>{par(v["case"])}{fig(base,"timeline.png",v["timeline_caption"])}{table([l["event"],l["first"],l["second"]],v["case_rows"])}{par(v["case_result"])}</section>'
 s+=f'<section class="article-section"><h2>{l["model"]}</h2>{par(v["foundation"])}{par(v["model"])}<h3>{l["refs"]}</h3>{refs([2,10,0,3])}</section>'
 return s
def about(c,base):
 l=c['labels'];pt=c['locale']=='pt-BR'
 intro=''.join(par(text) for text in c['cv_summary'].split('\n\n'))
 s=f'<header class="detail-top" id="about"><p class="eyebrow">{c["about"]}</p><h1>Felipe Meneguitti Dias</h1><p>São Paulo, {"Brasil" if pt else "Brazil"} · <a href="tel:+5532991734060">+55 (32) 99173-4060</a></p>{intro}</header>'
 s+=institution(c)
 s+=f'<section class="article-section"><h2>{"Experiência profissional" if pt else "Professional experience"}</h2>'
 for company,dates,role,location,items in c['jobs']:
  s+=f'<article class="cv-job"><h3>{e(company)}</h3><p class="job-meta">{e(role)}<br>{e(dates)} · {e(location)}</p><ul>'+''.join(f'<li>{e(x)}</li>' for x in items)+'</ul></article>'
 s+='</section>'
 s+=f'<section class="article-section"><h2>{l["education"]}</h2>{education(c)}</section>'
 s+=f'<section class="article-section"><h2>{l["skills"]}</h2>{table([("Área" if pt else "Area"),("Competências" if pt else "Skills")],c["skills"])}</section>'
 s+=f'<section class="article-section" id="awards"><h2>{"Premiações" if pt else "Awards"}</h2><ul class="cv-awards">'+''.join(f'<li><strong>{yr}</strong> · {e(text)}</li>' for yr,text in c['awards'])+f'</ul><a href="{LINKS["challenge"]}">{l["official"]}: PhysioNet Challenge 2024</a></section>'
 s+=f'<section class="section" id="publications"><h2>{c["papers"]}</h2>{publications(cv=True)}</section>'
 return s
def current_reading(lang,base):
 if not READING['enabled']:return ''
 label='Lendo agora' if lang=='pt' else 'Currently reading'
 newtab='abre em nova aba' if lang=='pt' else 'opens in a new tab'
 title=e(READING['title']);author=e(READING['author'])
 cover=ASSETS/READING['cover']
 if not cover.is_file():raise FileNotFoundError(f'Current reading cover not found: {cover}')
 version=sha256(cover.read_bytes()).hexdigest()[:12]
 return f'<aside class="current-reading" aria-label="{label}"><a class="reading-item" href="{e(READING["url"])}" target="_blank" rel="noopener noreferrer" aria-label="{label}: {title}, {author} ({newtab})"><img class="reading-cover" src="{base}assets/{e(READING["cover"])}?v={version}" alt="" width="36" height="54" loading="lazy" decoding="async"><span class="reading-copy"><span class="reading-label">{label}</span><span class="reading-title" lang="en">{title}</span><span class="reading-author">{author}</span></span></a></aside>'

def page(lang,kind):
 c=CONTENT[lang];prefix='' if lang=='pt' else 'en/'
 rel='index.html' if kind=='home' else 'about.html' if kind=='about' else f'projects/{kind}.html'
 path=prefix+rel;depth=len(Path(path).parts)-1;base='../'*depth
 homepath=('../' if kind in PROJECTS else '')+'index.html'
 switchpt=base+rel;switchen=base+'en/'+rel
 title=('Felipe Meneguitti Dias | IA aplicada à saúde' if lang=='pt' else 'Felipe Meneguitti Dias | Healthcare AI') if kind=='home' else (c['about'] if kind=='about' else c[kind]['title'])+' | Felipe Meneguitti Dias'
 desc=c['intro'] if kind=='home' else c['cv_summary'].replace('\n\n',' ') if kind=='about' else c[kind]['summary']
 body=home(c,base,lang) if kind=='home' else about(c,base) if kind=='about' else detail(c,kind,base)
 nav=''
 for anchor,label in zip(['projects','about','publications','contact'],c['nav']):
  target=(('../' if kind not in ['home','about'] else '')+'about.html#'+anchor) if anchor in ['about','publications'] else homepath+'#'+anchor
  nav+=f'<a href="{target}">{label}</a>'
 nav+=f'<a href="{base}blog/">Blog</a>'
 html=f'''<!doctype html><html lang="{c['locale']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="https://fmenegui.com/{path}"><link rel="alternate" hreflang="pt-BR" href="https://fmenegui.com/{rel}"><link rel="alternate" hreflang="en" href="https://fmenegui.com/en/{rel}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="https://fmenegui.com/assets/felipe.jpg"><link rel="icon" href="{base}assets/favicon.svg"><link rel="stylesheet" href="{base}assets/style.css?v={CSS_VERSION}"></head><body class="{'home-page' if kind=='home' else 'about-page' if kind=='about' else 'project-page'}"><a class="skip" href="#main">{c['labels']['skip']}</a><header class="header"><div class="wrap"><a class="brand" href="{homepath}">fmenegui</a><nav class="nav" aria-label="{c['labels']['home']}">{nav}</nav><span class="lang"><a lang="pt-BR" hreflang="pt-BR" href="{switchpt}" {'aria-current="page"' if lang=='pt' else ''}>PT</a><a lang="en" hreflang="en" href="{switchen}" {'aria-current="page"' if lang=='en' else ''}>EN</a></span></div></header><main id="main" class="wrap">{body}<section class="contact" id="contact"><h2>{e(c['contact'])}</h2><p class="contact-email"><a href="{LINKS['email']}">f.meneguittidias@gmail.com</a></p>{social()}<p class="contact-download"><a href="{base}downloads/Felipe_Dias_Portfolio_{lang.upper()}.pdf?v={PDF_VERSIONS[lang]}">{c['download']} (PDF)</a></p></section>{current_reading(lang,base) if kind=='home' else ''}</main><footer class="footer"><div class="wrap"><span>Felipe Meneguitti Dias</span><span>{c['updated']} · PT / EN</span></div></footer></body></html>'''
 dest=OUT/path;dest.parent.mkdir(exist_ok=True,parents=True);dest.write_text(html,encoding='utf-8')

for lang in CONTENT:
 for kind in ['home','about',*PROJECTS]:page(lang,kind)
(OUT/'cv').mkdir(exist_ok=True)
(OUT/'cv/cv.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=../about.html"><title>Felipe Dias</title><a href="../about.html">Sobre / About</a></html>')
(OUT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#111614"/><text x="11" y="44" font-family="Georgia,serif" font-size="35" fill="#96d6b5">fd</text></svg>')
(OUT/'.nojekyll').touch()
(OUT/'CNAME').write_text('fmenegui.com\n')
(OUT/'404.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Página não encontrada | Felipe Dias</title><h1>Página não encontrada / Page not found</h1><p><a href="/">Português</a> · <a href="/en/">English</a></p></html>')
print(f'Built {2*(2+len(PROJECTS))} bilingual portfolio pages in {OUT}')

for prefix in ["", "en/"]:
 (OUT/prefix/"projects/ppg.html").write_text('<meta http-equiv="refresh" content="0;url=rpms.html"><a href="rpms.html">RPMS</a>')

# Retain source notes in git, but exclude them and their search entries from publication.
shutil.rmtree(OUT/'learning',ignore_errors=True)
for stale in ['search.json','sitemap.xml']:
 (OUT/stale).unlink(missing_ok=True)
sys.path.insert(0, str(ROOT/'scripts'))
from site_ui import enhance
enhance(OUT)
subprocess.run([sys.executable, str(ROOT/'scripts/site_seo.py')], check=True)
