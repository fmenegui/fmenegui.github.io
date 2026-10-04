#!/usr/bin/env python3
"""Build the bilingual portfolio and CV."""
from pathlib import Path
from html import escape as e
import shutil
from content import CONTENT, LINKS, PAPERS
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
ASSETS=Path(__file__).parent/'assets'
OUT.mkdir(exist_ok=True)
shutil.copytree(ASSETS,OUT/'assets',dirs_exist_ok=True)
shutil.copy(Path(__file__).parent/'style.css',OUT/'assets/style.css')
shutil.copytree(Path(__file__).parent/'downloads',OUT/'downloads',dirs_exist_ok=True)

def par(t):return '<p>'+e(t)+'</p>'
def table(head,rows):return '<div class="table-scroll"><table><thead><tr>'+''.join('<th scope="col">'+e(x)+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+e(x)+('</th>' if i==0 else '</td>') for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def fig(base,file,caption):return f'<figure><img src="{base}assets/{file}" alt="{e(caption)}" loading="lazy"><figcaption>{e(caption)}</figcaption></figure>'
def refs(indices):
 return '<ol class="refs">'+''.join(f'<li>{e(PAPERS[i][2])} <a href="https://doi.org/{PAPERS[i][4]}">{e(PAPERS[i][1])}</a>. <small>{e(PAPERS[i][3])}, {PAPERS[i][0]}.</small></li>' for i in indices)+'</ol>'
def metrics(c):return '<div class="metrics">'+''.join(f'<div class="metric"><strong>{a}</strong><span>{b}</span></div>' for a,b in c['gorgona']['metrics'])+'</div>'
def section(title,text,id=''):return f'<section class="article-section" id="{id}"><h2>{e(title)}</h2>{par(text)}</section>'
def social():return '<div class="social">'+''.join(f'<a href="{LINKS[k]}">{label}</a>' for k,label in [('linkedin','LinkedIn'),('github','GitHub'),('scholar','Google Scholar'),('orcid','ORCID'),('lattes','Lattes')])+'</div>'
def publications(cv=False):
 return '<ol class="pub-list">'+''.join(f'<li><time>{yr}</time><div><h3><a href="https://doi.org/{doi}">{e(title)}</a></h3><p>{e(authors)} · {e(venue)}</p></div></li>' for i,(yr,title,authors,venue,doi) in sorted(enumerate(PAPERS),key=lambda item:-int(item[1][0])) if cv or i!=2)+'</ol>'
def education(c):return '<ol class="education">'+''.join(f'<li><time>{date}</time><div><strong>{e(name)}</strong><small>{e(school)}</small></div></li>' for date,name,school in c['education'])+'</ol>'
def visual(key,c,base):
 if key=='gorgona':return f'<div class="project-visual"><img src="{base}assets/dashboard.png" alt="Gorgona dashboard" loading="lazy"></div>'
 if key=='physionet':return '<div class="project-visual award"><span class="small">PHYSIONET CHALLENGE 2024</span><span class="rank">01</span><span>AIMED · '+('Classificação' if c['locale']=='pt-BR' else 'Classification')+'</span><span class="score">Macro F1 · 0.817</span></div>'
 return '<div class="project-visual ppg-visual"><span class="eyebrow">PPG → BP</span><span class="letters">Siamese ResNet</span><span>'+('Sinal + calibração' if c['locale']=='pt-BR' else 'Signal + calibration')+'</span></div>'
def home(c,base,lang):
 pdf=f'{base}downloads/Felipe_Dias_Portfolio_{lang.upper()}.pdf'
 s=f'<section class="hero"><div><h1>Felipe Meneguitti Dias</h1><p class="email-line">email: <a href="{LINKS["email"]}">f.meneguittidias@gmail.com</a></p>{social()}<p class="intro">{c["intro"]}</p><p class="profile-links"><a href="{pdf}">{c["download"]} (PDF)</a> · <a href="about.html">{c["about"]}</a></p></div><figure><img class="portrait" src="{base}assets/felipe.jpg" alt="Felipe Meneguitti Dias" width="320" height="360"></figure></section>'
 s+=f'<section class="section" id="projects"><div class="section-head"><h2>{c["selected"]}</h2></div>'
 for key in ['gorgona','incor','rpms']:
  v=c[key]
  imagefile={'gorgona':'flows.png','incor':'incor-integration.png','rpms':'rpms-app.jpeg'}[key]
  thumb=f'<a class="project-thumb {key}-thumb" href="projects/{key}.html"><img src="{base}assets/{imagefile}" alt="{e(v["title"])}" loading="lazy"></a>'
  doi=PAPERS[{'gorgona':0,'incor':3,'rpms':9}[key]][4]
  s+=f'<article class="project">{thumb}<div><h3><a href="projects/{key}.html">{v["title"]}</a></h3><p class="project-info">{v["status"]} · {v["period"]}</p><p class="desc">{v["summary"]}</p><p class="project-evidence">{v["evidence"]}</p><p class="project-links"><a href="projects/{key}.html">{c["read"]}</a> · <a href="https://doi.org/{doi}">{c["article"]}</a></p></div></article>'
 s+='</section>'
 return s
def detail(c,key,base):
 v=c[key];l=c['labels'];s=f'<header class="detail-top"><a class="back" href="../index.html#projects">← {c["back"]}</a><p class="eyebrow">{v["kicker"]}</p><h1>{v["title"]}</h1><p class="subtitle">{v["subtitle"]}</p></header>'
 s+=f'<p class="project-evidence">{e(v["evidence"])}</p>'
 s+=section(l['objective'],v['objective'],'objective')+section(l['contribution'],v['contribution'])
 s+='<section class="article-section decisions"><h2>'+('Decisões de engenharia' if c['locale']=='pt-BR' else 'Engineering decisions')+'</h2><dl>'+''.join('<div><dt>'+e(a)+'</dt><dd>'+e(b)+'</dd></div>' for a,b in v['decisions'])+'</dl></section>'
 if key=='rpms':
  lang='pt' if c['locale']=='pt-BR' else 'en'
  s+=f'<section class="article-section"><h2>{"Como funciona" if lang=="pt" else "How it works"}</h2>{fig(base,"rpms-architecture.jpeg",v["caption"])}{par(v["method"])}</section>'
  evidence=('A versão descrita no artigo de 2022 reuniu dados de 52 voluntários e foi utilizada no monitoramento remoto com 15 pulseiras. O aplicativo preservava o histórico local e enviava ao servidor as estimativas de pressão sistólica, diastólica e frequência cardíaca.' if lang=='pt' else 'The version described in the 2022 paper used data from 52 volunteers and supported remote monitoring with 15 wristbands. The app retained a local history and sent systolic pressure, diastolic pressure and heart rate estimates to the server.')
  appcap=('Aplicativo Android: medição, aquisição do PPG e histórico. Figura 3, SIoT 2022.' if lang=='pt' else 'Android app: measurement, PPG acquisition and history. Figure 3, SIoT 2022.')
  dashcap=('Painel ThingsBoard: visualização das medidas recebidas. Figura 4, SIoT 2022.' if lang=='pt' else 'ThingsBoard dashboard: received measurements. Figure 4, SIoT 2022.')
  s+=f'<section class="article-section"><h2>{l["result"]}</h2>{par(evidence)}<div class="rpms-gallery">{fig(base,"rpms-app.jpeg",appcap)}{fig(base,"rpms-dashboard.jpeg",dashcap)}</div></section>'
  protocol=('No protocolo de 2022, cada voluntário descansava por 10 minutos e realizava três coletas de um minuto de PPG, intercaladas com medidas de pressão por manguito. O processamento incluía filtro de 0,5 a 10 Hz, reamostragem de 200 para 125 Hz e janelas de 8 segundos. A avaliação separava os participantes entre as partições de validação.' if lang=='pt' else 'In the 2022 protocol, volunteers rested for 10 minutes and completed three one-minute PPG recordings interleaved with cuff blood pressure measurements. Processing used a 0.5–10 Hz filter, resampling from 200 to 125 Hz and 8-second windows. Evaluation kept participants separate across validation folds.')
  s+=f'<details class="technical"><summary>{"Protocolo e processamento do sinal" if lang=="pt" else "Collection protocol and signal processing"}</summary>{par(protocol)}{fig(base,"rpms-protocol.png","SIoT 2022 · Figure 2")}</details>'
  s+=f'<section class="article-section"><h2>{"Algoritmos e pesquisa" if lang=="pt" else "Algorithms and research"}</h2>{par(v["research"])}<div class="biomarker-grid">'
  for name,description,i in v['biomarkers']:
   s+=f'<div><h3>{e(name)}</h3>{par(description)}<a href="https://doi.org/{PAPERS[i][4]}">{c["article"]} ({PAPERS[i][0]})</a></div>'
  s+='</div></section>'
  return s+f'<section class="article-section"><h2>{l["refs"]}</h2>{refs([9,6,1,4,7,8])}</section>'
 if key=='incor':
  s+=f'<section class="article-section"><h2>{l["how"]}</h2><figure class="incor-figure"><div class="figure-window"><img src="{base}assets/incor-integration.png" alt="{e(v["caption"])}"></div><figcaption>{e(v["caption"])}</figcaption></figure>{par(v["method"])}{table([l["step"],l["method"]],v["workflow"])}</section>'
  s+=section(l['result'],v['result'])+par(v['scope'])
  s+=''
  return s+f'<section class="article-section"><h2>{l["refs"]}</h2>{refs([3,0,10])}</section>'
 if key!='gorgona':
  s+='<div class="split"><div>'+visual(key,c,base)+'</div><div>'+par(v['method'])+par(v['result'])+'</div></div>'
  s+=section(l['team'],v['team'])
  s+=f'<section class="article-section"><h2>{l["refs"]}</h2>{refs([2] if key=="physionet" else [1,4])}'
  if key=='physionet':s+=f'<a class="text-link" href="{LINKS["challenge"]}">{l["official"]} ↗</a>'
  return s+'</section>'
 s+='<figure class="gorgona-flow"><div class="flow-window"><img src="'+base+'assets/flows.png" alt="'+('Fluxo proposto com IA: cliente, anonimização, servidor InCor e alerta no Telegram, em paralelo à telemedicina.' if c['locale']=='pt-BR' else 'Proposed AI workflow: client, anonymization, InCor server and Telegram alerts alongside telemedicine.')+'"></div><figcaption>'+('Fluxo proposto com IA. Figura original do projeto.' if c['locale']=='pt-BR' else 'Proposed AI workflow. Original project figure, with Portuguese labels.')+'</figcaption></figure>'
 s+=metrics(c)+f'<p class="note">{v["count_note"]}</p>'
 s+='<nav class="contents" aria-label="'+('Nesta página' if c['locale']=='pt-BR' else 'On this page')+'">'+''.join(f'<a href="#{k}">{l[k]}</a>' for k in ['objective','workflow','server','case'])+'</nav>'
 s+=f'<section class="article-section"><h2>{l["location"]}</h2>{par(v["location"])}{fig(base,"upa-map-"+("pt" if c["locale"]=="pt-BR" else "en")+".webp",v["map_caption"])}<a class="text-link" href="{LINKS["map"]}">{l["openmap"]} ↗</a></section>'
 s+=f'<section class="article-section" id="workflow"><h2>{l["how"]}</h2><div class="split"><div><h3>{l["before"]}</h3>{par(v["before"])}</div><div><h3>{l["after"]}</h3>{par(v["after"])}</div></div>{fig(base,"flows.png",l["workflow"]+(". Diagramas originais do projeto." if c["locale"]=="pt-BR" else ". Original project diagrams in Portuguese."))}{table([l["step"],l["before"],l["after"]],v["flow_rows"])}</section>'
 s+='<details class="technical implementation"><summary>'+('Cliente Windows, servidor e plataforma online' if c['locale']=='pt-BR' else 'Windows client, server and online platform')+'</summary>'
 s+=f'<section class="article-section"><h2>{l["client"]}</h2>{par(v["client"])}<div class="two-images">{fig(base,"client-install.png","ECG-IA Client 1.6.66 · Windows")}{fig(base,"client-menu.png","ECG-IA Client · "+("Menu na bandeja do Windows" if c["locale"]=="pt-BR" else "Windows system tray menu"))}</div></section>'
 s+=f'<section class="article-section" id="server"><h2>{l["server"]}</h2>{par(v["server"])}{fig(base,"architecture.png",("Arquitetura do sistema." if c["locale"]=="pt-BR" else "System architecture. Original labels in Portuguese."))}<h3>{l["privacy"]}</h3>{par(v["privacy"])}{par(v["dashboard"])}{fig(base,"dashboard.png","Gorgona · Dashboard · 03/10/2026")}</section>'
 s+='</details>'
 s+=f'<section class="article-section" id="case"><h2>{l["result"]}</h2><h3>{l["case"]}</h3>{par(v["case"])}{fig(base,"timeline.png",v["timeline_caption"])}{table([l["event"],l["first"],l["second"]],v["case_rows"])}{par(v["case_result"])}</section>'
 s+=f'<section class="article-section"><h2>{l["model"]}</h2>{par(v["foundation"])}{par(v["model"])}<h3>{l["refs"]}</h3>{refs([2,10,0,3])}</section>'
 return s
def about(c,base):
 l=c['labels'];pt=c['locale']=='pt-BR'
 s=f'<header class="detail-top" id="about"><p class="eyebrow">Felipe Meneguitti Dias</p><h1>{c["about"]}</h1><p class="subtitle">{c["professional_title"]}</p><p>São Paulo, {"Brasil" if pt else "Brazil"} · <a href="tel:+5532991734060">+55 (32) 99173-4060</a></p>{par(c["cv_summary"])}</header>'
 s+=f'<section class="article-section"><h2>{"Experiência profissional" if pt else "Professional experience"}</h2>'
 for company,dates,role,location,items in c['jobs']:
  s+=f'<article class="cv-job"><h3>{e(company)}</h3><p class="job-meta">{e(role)}<br>{e(dates)} · {e(location)}</p><ul>'+''.join(f'<li>{e(x)}</li>' for x in items)+'</ul></article>'
 s+='</section>'
 s+=f'<section class="article-section"><h2>{l["education"]}</h2>{education(c)}</section>'
 s+=f'<section class="article-section"><h2>{l["skills"]}</h2>{table([("Área" if pt else "Area"),("Competências" if pt else "Skills")],c["skills"])}</section>'
 s+=f'<section class="article-section" id="awards"><h2>{"Premiações" if pt else "Awards"}</h2><ul class="cv-awards">'+''.join(f'<li><strong>{yr}</strong> · {e(text)}</li>' for yr,text in c['awards'])+f'</ul><a href="{LINKS["challenge"]}">{l["official"]}: PhysioNet Challenge 2024</a></section>'
 s+=f'<section class="section" id="publications"><h2>{c["papers"]}</h2>{publications(cv=True)}</section>'
 return s
def page(lang,kind):
 c=CONTENT[lang];prefix='' if lang=='pt' else 'en/'
 rel='index.html' if kind=='home' else 'about.html' if kind=='about' else f'projects/{kind}.html'
 path=prefix+rel;depth=len(Path(path).parts)-1;base='../'*depth
 homepath=('../' if kind in ['gorgona','incor','rpms'] else '')+'index.html'
 switchpt=base+rel;switchen=base+'en/'+rel
 title='Felipe Dias' if kind=='home' else (c['about'] if kind=='about' else c[kind]['title'])+' | Felipe Dias'
 desc=c['intro'] if kind in ['home','about'] else c[kind]['summary']
 body=home(c,base,lang) if kind=='home' else about(c,base) if kind=='about' else detail(c,kind,base)
 nav=''
 for anchor,label in zip(['projects','about','publications','contact'],c['nav']):
  target=(('../' if kind not in ['home','about'] else '')+'about.html#'+anchor) if anchor in ['about','publications'] else homepath+'#'+anchor
  nav+=f'<a href="{target}">{label}</a>'
 html=f'''<!doctype html><html lang="{c['locale']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="https://fmenegui.com/{path}"><link rel="alternate" hreflang="pt-BR" href="https://fmenegui.com/{rel}"><link rel="alternate" hreflang="en" href="https://fmenegui.com/en/{rel}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="https://fmenegui.com/assets/felipe.jpg"><link rel="icon" href="{base}assets/favicon.svg"><link rel="stylesheet" href="{base}assets/style.css"></head><body><a class="skip" href="#main">{c['labels']['skip']}</a><header class="header"><div class="wrap"><a class="brand" href="{homepath}">Felipe Dias<span aria-hidden="true">.</span></a><nav class="nav" aria-label="{c['labels']['home']}">{nav}<span class="lang"><a lang="pt-BR" hreflang="pt-BR" href="{switchpt}" {'aria-current="page"' if lang=='pt' else ''}>PT</a><a lang="en" hreflang="en" href="{switchen}" {'aria-current="page"' if lang=='en' else ''}>EN</a></span></nav></div></header><main id="main" class="wrap">{body}<section class="contact" id="contact"><p><a href="{LINKS['email']}">f.meneguittidias@gmail.com</a></p>{social()}<p><a href="{base}downloads/Felipe_Dias_Portfolio_{lang.upper()}.pdf">{c['download']} (PDF)</a></p></section></main><footer class="footer"><div class="wrap"><span>Felipe Meneguitti Dias</span><span>{c['updated']} · PT / EN</span></div></footer></body></html>'''
 dest=OUT/path;dest.parent.mkdir(exist_ok=True,parents=True);dest.write_text(html,encoding='utf-8')

for lang in CONTENT:
 for kind in ['home','about','gorgona','incor','rpms']:page(lang,kind)
(OUT/'cv').mkdir(exist_ok=True)
(OUT/'cv/cv.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=../about.html"><title>Felipe Dias</title><a href="../about.html">Sobre / About</a></html>')
(OUT/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#172c35"/><text x="11" y="44" font-family="Georgia,serif" font-size="35" fill="#faf9f5">fd</text></svg>')
(OUT/'.nojekyll').touch()
(OUT/'CNAME').write_text('fmenegui.com\n')
(OUT/'404.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Página não encontrada | Felipe Dias</title><h1>Página não encontrada / Page not found</h1><p><a href="/">Português</a> · <a href="/en/">English</a></p></html>')
print(f'Built 10 bilingual portfolio pages in {OUT}')

# Previous draft project URLs now point to the CV award section.
for prefix in ['', 'en/']:
 (OUT/prefix/'projects/physionet.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=../about.html#awards"><a href="../about.html#awards">CV</a>')

for prefix in ["", "en/"]:
 (OUT/prefix/"projects/ppg.html").write_text('<meta http-equiv="refresh" content="0;url=rpms.html"><a href="rpms.html">RPMS</a>')

# Retain source notes in git, but exclude them and their search entries from publication.
shutil.rmtree(OUT/'learning',ignore_errors=True)
for stale in ['search.json','sitemap.xml']:
 (OUT/stale).unlink(missing_ok=True)
paths=['index.html','about.html','projects/gorgona.html','projects/incor.html','projects/rpms.html']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://fmenegui.com/'+prefix+p+'</loc></url>' for prefix in ['', 'en/'] for p in paths)+'</urlset>')
