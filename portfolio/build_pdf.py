"""Concise bilingual portfolio: introduction and one page per project."""
from pathlib import Path
from html import escape as e
from content import CONTENT, PAPERS, LINKS
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'print';OUT.mkdir(exist_ok=True)
def p(t,cls=''):return f'<p class="{cls}">{e(t)}</p>'
def img(name,caption='',cls=''):return f'<figure class="{cls}"><img src="{(ROOT/"assets"/name).as_uri()}" alt=""><figcaption>{e(caption)}</figcaption></figure>'
def title(n,label,name):return f'<div class="kicker">{n} / {label}</div><h2>{e(name)}</h2>'
def references(indices,lang):
 s='<div class="compact-refs"><h3>'+('Artigos da equipe' if lang=='pt' else 'Team publications')+'</h3>'
 for i in indices:
  yr,name,authors,venue,doi=PAPERS[i]
  s+=f'<p><a href="https://doi.org/{doi}">{e(name)}</a>. {e(venue)}, {yr}.</p>'
 return s+'</div>'
def make(lang):
 c=CONTENT[lang];l=c['labels'];pt=lang=='pt';pages=[]
 s=f'<div class="kicker">{c["portfolio"]} · {c["updated"]}</div><div class="cover"><div><h1>Felipe<br>Meneguitti Dias</h1><p class="tagline">{c["headline"]}</p></div>{img("felipe.jpg",cls="portrait")}</div>'+p(c['intro'])
 s+=f'<h3>{c["selected"]}</h3><div class="overview">'
 for n,key in enumerate(['gorgona','incor','rpms'],1):
  z=c[key];s+=f'<section><span>0{n}</span><div><h3>{e(z["title"])}</h3>{p(z["summary"])}<p class="note">{e(z["role"])}</p></div></section>'
 s+='</div>'
 s+=p('Doutorado em Engenharia Elétrica · Universidade de São Paulo' if pt else 'PhD in Electrical Engineering · University of São Paulo','qualification')
 s+=f'<div class="contactline"><a href="{LINKS["email"]}">f.meneguittidias@gmail.com</a><br><a href="https://fmenegui.github.io/">fmenegui.github.io</a> · <a href="{LINKS["linkedin"]}">LinkedIn</a> · <a href="{LINKS["github"]}">GitHub</a></div>'
 pages.append(s)
 v=c['gorgona'];s=title('01','Gorgona',v['subtitle'])+p(v['summary'],'lead')
 s+='<div class="metrics">'+''.join(f'<div><strong>{x}</strong><span>{y}</span></div>' for x,y in v['metrics'])+'</div>'
 s+=p(v['count_note'],'note')
 s+=f'<h3>{l["objective"]}</h3>'+p(v['objective'])
 before='ECG enviado à telemedicina. Laudo e avaliação médica orientavam o acionamento da regulação.' if pt else 'ECGs were sent to telemedicine. Reports and medical assessment informed contact with the coordination team.'
 after='O cliente Windows detecta o exame e envia ao InCor. O servidor classifica e alerta o grupo no Telegram quando a probabilidade de Corrente de Lesão supera 50%.' if pt else 'The Windows client detects the examination and sends it to InCor. The server classifies it and alerts the Telegram group when Current of Injury probability exceeds 50%.'
 s+=f'<div class="cols"><div><h3>{l["before"]}</h3>{p(before)}</div><div><h3>{l["after"]}</h3>{p(after)}</div></div>'
 s+=p('Integrei cliente, servidor, painel web e alertas. O projeto prevê anonimização local configurável, HTTPS e credenciais por instalação.' if pt else 'I connected the client, server, web dashboard and alerts. The design includes configurable local anonymization, HTTPS and per-installation credentials.')
 s+=f'<h3>{l["case"]} · UPA Rodrigo Argolo · 20/05/2026</h3>'
 s+=img('timeline.png', 'Linha do tempo original, slide 23. Recorte sem o bloco de identificação.' if pt else 'Original timeline, slide 23. Personal identification block omitted.','timeline')
 s+=p('Dois ECGs do mesmo atendimento geraram alertas em 2 minutos, antecipando os laudos em 41 e 25 minutos. O caso documenta o tempo de comunicação à regulação.' if pt else 'Two ECGs from the same encounter triggered alerts within 2 minutes, preceding their reports by 41 and 25 minutes. The case documents communication timing.')
 s+=references([0],lang)
 pages.append(s)
 v=c['incor'];s=title('02','InCor',v['subtitle'])+p(v['summary'],'lead')
 s+=f'<h3>{l["objective"]}</h3>'+p(v['objective'])
 s+=f'<figure class="incor-figure"><div class="figure-window"><img src="{(ROOT/"assets/incor-integration.png").as_uri()}" alt=""></div><figcaption>{e(v["caption"])}</figcaption></figure>'
 s+=p(v['method'])+p(v['result'])
 s+=p(v['role'],'note')+references([3],lang)
 pages.append(s)
 v=c['rpms'];s=title('03','RPMS',v['subtitle'])+p(v['objective'],'lead')
 s+=f'<h3>{l["contribution"]}</h3>'+p(v['contribution'])
 s+=img(f'rpms-{lang}.svg',v['caption'],'rpms-flow')+p(v['method'])
 s+=f'<h3>{"Algoritmos e pesquisa" if pt else "Algorithms and research"}</h3><div class="biomarkers">'
 for name,desc,i in v['biomarkers']:s+=f'<div><b>{e(name)}</b>{p(desc)}</div>'
 s+='</div>'+references([6,1,7,8],lang)
 pages.append(s)
 html=f'<!doctype html><html lang="{c["locale"]}"><head><meta charset="utf-8"><title>Felipe Dias | {c["portfolio"]}</title><link rel="stylesheet" href="{(ROOT/"print.css").as_uri()}"></head><body>'
 for i,body in enumerate(pages,1):html+=f'<article class="sheet compact">{body}<footer><span>Felipe Meneguitti Dias · {c["portfolio"]}</span><span>{i:02} / {len(pages):02}</span></footer></article>'
 html+='</body></html>'; (OUT/f'portfolio_{lang}.html').write_text(html,encoding='utf-8')
for lang in ['pt','en']:make(lang)
