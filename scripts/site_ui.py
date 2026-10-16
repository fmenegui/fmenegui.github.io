#!/usr/bin/env python3
"""Share navigation, search and reading tools across the rendered site."""
from copy import deepcopy
from hashlib import sha256
from html import escape as e
from pathlib import Path
import re
from lxml import html as H
from site_seo import Document

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
 'pt': ['Projetos', 'Currículo', 'Publicações', 'Contato', 'Buscar'],
 'en': ['Projects', 'CV', 'Publications', 'Contact', 'Search'],
}

def header(lang, relative):
    labels = LABELS[lang]
    prefix = '/en/' if lang == 'en' else '/'
    blog = relative.startswith('blog/')
    targets = [prefix+'#projects', prefix+'about.html', prefix+'about.html#publications', prefix+'#contact']
    links = ''.join(f'<a data-nav="{i}" href="{url}"'+(' aria-current="page"' if relative == prefix.lstrip('/')+'about.html' and i == 1 else '')+f'>{labels[i]}</a>' for i,url in enumerate(targets))
    links += '<a href="/blog/"'+(' aria-current="page"' if blog else '')+'>Blog</a>'
    rel = 'index.html' if relative=='404.html' else relative.removeprefix('en/')
    switch = ''.join(f'<a lang="{locale}" '+(f'data-ui-language="{code}" href="#" aria-label="'+('Navegação em português' if code=='pt' else 'Navigation in English')+'"' if blog else f'hreflang="{locale}" href="{prefix2}{rel}"')+(' aria-current="true"' if code==lang else '')+f'>{code.upper()}</a>' for code,locale,prefix2 in [('pt','pt-BR','/'),('en','en','/en/')])
    return f'<a class="skip" href="#main" data-i18n="skip">'+('Pular para o conteúdo' if lang=='pt' else 'Skip to content')+f'</a><header class="header" lang="{lang}"><div class="wrap"><a class="brand" data-home href="{prefix}" aria-label="Felipe Meneguitti Dias">fmenegui</a><nav class="nav" aria-label="'+('Principal' if lang=='pt' else 'Main')+f'">{links}<button class="search-toggle" type="button" data-search-open data-i18n="search">{labels[4]}</button></nav><span class="lang">{switch}</span></div></header>'

def footer(lang):
    return '<footer class="footer"><div class="wrap"><span>Felipe Meneguitti Dias</span><span><a href="/blog/index.xml">RSS</a> · <a href="#main" data-i18n="top">'+('Voltar ao início' if lang=='pt' else 'Back to top')+'</a></span></div></footer>'

def search_dialog(lang):
    return '''<dialog id="site-search" aria-labelledby="search-heading"><div class="search-dialog-head"><h2 id="search-heading" data-i18n="search">Search</h2><button type="button" data-search-close aria-label="Close search">×</button></div><label for="search-query" data-i18n="query">Search the entire site</label><input id="search-query" type="search" autocomplete="off" spellcheck="false"><p id="search-status" role="status" aria-live="polite"></p><ol id="search-results"></ol></dialog>'''

def recent_posts(output):
    posts = []
    for path in (output/'blog').glob('*/index.html'):
        d = Document(path.read_text())
        if d.meta.get('dcterms.date'):
            posts.append({'url':'/'+path.relative_to(output).as_posix().removesuffix('index.html'), 'title':d.heading, 'description':d.meta.get('description',''), 'date':d.meta['dcterms.date']})
    return sorted(posts,key=lambda p:p['date'],reverse=True)

def cards(posts, lang):
    return ''.join(f'<article class="blog-preview" lang="en"><p class="blog-date"><time datetime="{p["date"]}">{p["date"]}</time> · ECG · AI · <span data-i18n="english">'+('Em inglês' if lang=='pt' else 'In English')+f'</span></p><h2><a href="{p["url"]}">{e(p["title"])}</a></h2><p>{e(p["description"])}</p></article>' for p in posts)

def enhance(output):
    posts = recent_posts(output)
    cssver = sha256((output/'assets/style.css').read_bytes()).hexdigest()[:12]
    js = (ROOT/'portfolio/site-ui.js').read_bytes()
    jsname = 'site-ui-'+sha256(js).hexdigest()[:12]+'.js'
    (output/'assets'/jsname).write_bytes(js)
    paths = [p for p in output.rglob('*.html') if not any(s in p.parts for s in ['site_libs','learning'])]
    for path in paths:
        rel=path.relative_to(output).as_posix()
        raw=path.read_text()
        if 'http-equiv="refresh"' in raw: continue
        if rel=='404.html':
            raw='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Página não encontrada | Felipe Dias</title><link rel="stylesheet" href="/assets/style.css?v='+cssver+'"></head><body><a class="skip" href="#main">Pular para o conteúdo</a><header class="header"></header><main id="main" class="wrap" tabindex="-1"><section class="detail-top"><p class="eyebrow">404</p><h1>Página não encontrada</h1><p>Você pode voltar à página inicial, abrir o blog ou buscar pelo título de um artigo.</p><p><a href="/">Início</a> · <a href="/blog/">Blog</a> · <a href="/en/" lang="en">English home</a></p><button type="button" class="search-toggle" data-search-open>Buscar no site</button></section></main><footer class="footer"></footer></body></html>'
        lang='en' if rel.startswith(('en/','blog/')) else 'pt'
        blog=rel.startswith('blog/')
        if blog:
            root=H.fromstring(raw)
            body=root.find('body')
            main=root.xpath('//main')[0]
            before=Document(H.tostring(main,encoding='unicode')).text(Document(H.tostring(main,encoding='unicode')).main_parts)
            toc=root.xpath('//nav[@id="TOC"]')
            scripts=[deepcopy(s) for s in body.xpath('.//script') if main not in s.iterancestors()]
            main.set('id','main');main.set('class','blog-main content');main.set('tabindex','-1');main.set('lang','en')
            # Keep all original article nodes, prose and scientific values.
            if rel!='blog/index.html':
                for img in main.xpath('.//img[@src]'):
                    if any(a.tag=='a' for a in img.iterancestors()): continue
                    link=H.Element('a',href=img.get('src'),attrib={'class':'figure-original','target':'_blank','rel':'noopener','aria-label':'Open original figure in a new tab','title':'Open original figure in a new tab'})
                    img.addprevious(link);link.append(img)
                for box in main.xpath('.//div[contains(@style,"overflow-x:")]'):
                    box.set('tabindex','0');box.set('role','region');box.set('aria-label','Figure, scroll horizontally to see all details')
                    box.set('class',(box.get('class','')+' figure-scroll').strip())
                for table in list(main.xpath('.//table')):
                    if any('table-scroll' in a.get('class','') or 'overflow' in a.get('style','') for a in table.iterancestors()): continue
                    wrap=H.Element('div',attrib={'class':'table-scroll','tabindex':'0','role':'region','aria-label':'Table, scroll horizontally if needed'})
                    table.addprevious(wrap);wrap.append(table)
                after=Document(H.tostring(main,encoding='unicode'))
                assert before==after.text(after.main_parts), f'Article text changed: {rel}'
            else:
                main=H.fragment_fromstring('<main id="main" class="blog-main blog-index" tabindex="-1"><header class="detail-top"><h1>Blog</h1><p data-i18n="blog-intro">Experiments in AI and ECG, with methods, results and code.</p></header><label for="blog-query" data-i18n="filter">Search within articles</label><input type="search" id="blog-query" autocomplete="off"><p id="blog-status" role="status" aria-live="polite"></p><div id="blog-posts">'+cards(posts,lang)+'</div><p><a href="/blog/index.xml">RSS</a></p></main>')
            for child in list(body): body.remove(child)
            body.attrib.clear();body.set('class','blog-page');body.set('data-blog-ui','true')
            layout=H.Element('div',attrib={'class':'blog-layout wrap'})
            layout.append(main)
            if toc and rel!='blog/index.html':
                aside=H.Element('div',attrib={'class':'blog-toc','role':'complementary','aria-label':'On this page'})
                contents=H.Element('details',attrib={'open':'open'});aside.append(contents)
                summary=H.Element('summary',attrib={'data-i18n':'contents'});contents.append(summary)
                summary.text='On this page'
                for heading in toc[0].xpath('./h2'):
                    toc[0].remove(heading)
                contents.append(toc[0]);layout.append(aside)
            for node in H.fragments_fromstring(header(lang,rel)): body.append(node)
            if rel!='blog/index.html':
                note=H.fragment_fromstring('<p class="wrap article-language" data-i18n="article-language">Article in English · PT / EN changes navigation only.</p>')
                body.append(note)
            body.append(layout)
            for node in H.fragments_fromstring(footer(lang)): body.append(node)
            for node in scripts: body.append(node)
            head=root.find('head')
            head.append(H.Element('link',rel='stylesheet',href=f'/assets/style.css?v={cssver}'))
            if not head.xpath('./link[@rel="icon"]'):
                head.append(H.Element('link',rel='icon',href='/assets/favicon.svg'))
            raw='<!doctype html>\n'+H.tostring(root,encoding='unicode',method='html')
        else:
            raw=re.sub(r'<a class="skip".*?</header>',lambda m:header(lang,rel),raw,count=1,flags=re.S)
            raw=re.sub(r'<footer class="footer">.*?</footer>',lambda m:footer(lang),raw,count=1,flags=re.S)
            raw=raw.replace('<main id="main" class="wrap">','<main id="main" class="wrap" tabindex="-1">')
            if rel in ['index.html','en/index.html']:
                title='Do blog' if lang=='pt' else 'From the blog'
                intro=('Experimentos e ideias que tenho explorado, com métodos e código para quem quiser acompanhar.' if lang=='pt' else 'Experiments and ideas I have been exploring, with methods and code you can follow.')
                previews=cards(posts[:3],lang).replace('<h2>','<h3>').replace('</h2>','</h3>')
                feature=f'<section class="section blog-feature" id="blog"><div class="section-head"><h2>{title}</h2></div><p>{intro}</p>{previews}<p><a href="/blog/">'+('Ver todos os posts' if lang=='pt' else 'All posts')+'</a></p></section>'
                raw=re.sub(r'<section class="section blog-feature".*?</section>',lambda m:feature,raw,count=1,flags=re.S)
        raw=raw.replace('<body ',f'<body data-ui-locale="{lang}" ',1)
        if '<body>' in raw: raw=raw.replace('<body>',f'<body data-ui-locale="{lang}">',1)
        raw=raw.replace('</body>',search_dialog(lang)+f'<script src="/assets/{jsname}" defer></script></body>')
        path.write_text(raw)
    print('Shared navigation, article layout, recent posts and search controls built')
