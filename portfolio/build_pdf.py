"""Bilingual, evidence-led portfolio: profile and three engineering case studies."""
from pathlib import Path
from html import escape as e
from content import CONTENT,PAPERS,LINKS
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'print';OUT.mkdir(exist_ok=True)
def p(s,cls=''):return f'<p class="{cls}">{e(s)}</p>'
def img(name,caption='',cls=''):return f'<figure class="{cls}"><img src="{(ROOT/"assets"/name).as_uri()}" alt=""><figcaption>{e(caption)}</figcaption></figure>'
def refs(ids,pt):
 return '<div class="references"><h3>'+('Referências' if pt else 'References')+'</h3>'+''.join(f'<p><a href="https://doi.org/{PAPERS[i][4]}">{e(PAPERS[i][1])}</a> · {e(PAPERS[i][3])}, {PAPERS[i][0]}.</p>' for i in ids)+'</div>'
def heading(k,v):return f'<p class="kicker">{e(v["status"])} · {v["period"]}</p><h2>{e(v["title"])}</h2>'+p(v['subtitle'],'subtitle')
def block(h,t):return '<h3>'+e(h)+'</h3>'+p(t)
def make(lang):
 c=CONTENT[lang];pt=lang=='pt';l=c['labels'];pages=[]
 s='<p class="kicker">'+c['portfolio']+' · '+c['updated']+'</p><h1>Felipe<br>Meneguitti Dias</h1>'+p(c['headline'],'subtitle')+p(c['intro'],'intro')
 s+='<h3>'+c['selected']+'</h3><div class="overview">'
 for key in ['gorgona','incor','rpms']:
  v=c[key];url='https://fmenegui.com/'+('' if pt else 'en/')+'projects/'+key+'.html'
  s+='<section><h2><a href="'+url+'">'+v['title']+'</a></h2>'+p(v['summary'])+p(v['evidence'],'evidence')+'</section>'
 s+='</div>'+p('Samsung · 2026–atual | InCor · 2020–2026' if pt else 'Samsung · 2026–present | InCor · 2020–2026','career')
 s+='<p class="contact"><a href="'+LINKS['email']+'">f.meneguittidias@gmail.com</a><br><a href="https://fmenegui.com/">fmenegui.com</a> · <a href="'+LINKS['linkedin']+'">LinkedIn</a> · <a href="https://fmenegui.com/'+('about.html' if pt else 'en/about.html')+'">'+c['about']+'</a></p>'
 pages.append(s)
 v=c['gorgona'];s=heading('gorgona',v)+block(l['objective'],v['objective'])+block(l['contribution'],v['contribution'])
 s+='<div class="cols">'+block(l['before'],('Envio manual à telemedicina e comunicação da equipe com a regulação, conforme a avaliação médica.' if pt else 'Manual submission to telemedicine and staff communication with the coordination team, based on clinical assessment.'))+block(l['after'],('Cliente Windows, anonimização configurável, servidor InCor e alerta automático pelo Telegram.' if pt else 'Windows client, configurable anonymization, InCor server and automated Telegram alert.'))+'</div>'
 s+='<figure class="new-flow"><div class="flow-window"><img src="'+(ROOT/'assets/flows.png').as_uri()+'"></div><figcaption>'+('Fluxo proposto com IA. Figura original do projeto.' if pt else 'Proposed AI workflow. Original project figure, in Portuguese.')+'</figcaption></figure>'
 s+=p('A telemedicina e a decisão clínica permanecem no fluxo. HTTPS e credenciais por instalação complementam a anonimização local configurável.' if pt else 'Telemedicine and clinical decisions remain part of the workflow. HTTPS and per-installation credentials complement configurable local anonymization.','note')
 pages.append(s)
 s='<p class="kicker">Gorgona · '+('Evidências da implantação' if pt else 'Deployment evidence')+'</p><h2>'+('Operação e estudo de caso' if pt else 'Operation and case study')+'</h2>'
 s+='<div class="metrics">'+''.join('<div><strong>'+a+'</strong><span>'+b+'</span></div>' for a,b in v['metrics'])+'</div>'+p(v['count_note'],'note')
 s+=block('UPA Rodrigo Argolo · 20/05/2026',v['case'])+img('timeline.png',v['timeline_caption'],'timeline')+p(v['case_result'])
 s+=block(l['model'],v['foundation_short'])+refs([2,10,0],pt)
 s+='<p class="more"><a href="https://fmenegui.com/'+('' if pt else 'en/')+'projects/gorgona.html">'+('Mapa da UPA, cliente Windows e plataforma online no estudo completo' if pt else 'See the full case study for the location map, Windows client and online platform')+'</a></p>'
 pages.append(s)
 v=c['incor'];s=heading('incor',v)+block(l['objective'],v['objective'])+block(l['contribution'],v['contribution'])
 s+='<figure class="incor-figure"><div class="figure-window"><img src="'+(ROOT/'assets/incor-integration.png').as_uri()+'"></div><figcaption>'+e(v['caption'])+'</figcaption></figure>'
 s+=block(l['result'],v['result'])+p(v['scope'],'note')+refs([3,0,10],pt)
 pages.append(s)
 v=c['rpms'];s=heading('rpms',v)+block(l['objective'],v['objective'])+block(l['contribution'],v['contribution'])+img('rpms-architecture.jpeg',v['caption'],'rpms-flow')+p(v['method'])+p(v['evidence'],'evidence')
 s+=block('Validação e pesquisa' if pt else 'Validation and research',('O protocolo publicado separa participantes entre as partições de validação. A implementação de 2022 estima pressão e frequência cardíaca. Qualidade do sinal, diabetes e sono são frentes de pesquisa documentadas nos artigos abaixo.' if pt else 'The published protocol keeps participants separate across validation folds. The 2022 implementation estimates blood pressure and heart rate. Signal quality, diabetes and sleep are research areas documented in the papers below.'))+refs([9,6,1,7,8],pt)
 pages.append(s)
 html='<html lang="'+c['locale']+'"><head><meta charset="utf-8"><title>Felipe Dias | Portfolio</title><link rel="stylesheet" href="'+(ROOT/'print.css').as_uri()+'"></head><body>'
 for i,s in enumerate(pages,1):html+='<article class="sheet">'+s+'<footer><span>Felipe Meneguitti Dias · '+c['portfolio']+'</span><span>'+str(i)+' / '+str(len(pages))+'</span></footer></article>'
 (OUT/('portfolio_'+lang+'.html')).write_text(html+'</body></html>')
for lang in ['pt','en']:make(lang)
