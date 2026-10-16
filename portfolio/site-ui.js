/* Shared, dependency-free navigation and full-text search. */
(() => {
  'use strict';
  const body = document.body;
  const isBlog = body.dataset.blogUi === 'true';
  const strings = {
    pt: {contents:'Neste artigo','article-language':'Artigo em inglês · PT / EN altera o idioma da navegação.',search:'Buscar',skip:'Pular para o conteúdo',top:'Voltar ao início',query:'Buscar no site inteiro',english:'Em inglês',filter:'Buscar no texto dos artigos', 'blog-intro':'Experimentos em IA e ECG, com métodos, resultados e código.',empty:'Nenhum resultado. Tente outro termo.',loading:'Carregando busca…',error:'Não foi possível carregar a busca. Tente novamente.',prompt:'Digite um termo para buscar.',close:'Fechar busca',count:n=>`${n} resultado${n===1?'':'s'}`, nav:['Projetos','Currículo','Publicações','Contato']},
    en: {contents:'On this page','article-language':'Article in English · PT / EN changes navigation only.',search:'Search',skip:'Skip to content',top:'Back to top',query:'Search the entire site',english:'In English',filter:'Search within article text','blog-intro':'Experiments in AI and ECG, with methods, results and code.',empty:'No results. Try another term.',loading:'Loading search…',error:'Search could not load. Please try again.',prompt:'Enter a search term.',close:'Close search',count:n=>`${n} result${n===1?'':'s'}`,nav:['Projects','CV','Publications','Contact']}
  };
  let lang=body.dataset.uiLocale || 'en';
  try { if(isBlog) lang=localStorage.getItem('site-language') || lang; } catch (_) {}
  if(!strings[lang]) lang='en';
  const dialog=document.querySelector('#site-search');
  const input=document.querySelector('#search-query');
  const results=document.querySelector('#search-results');
  const status=document.querySelector('#search-status');
  const blogInput=document.querySelector('#blog-query');
  const contents=document.querySelector('.blog-toc details');
  if(contents){const narrow=matchMedia('(max-width: 900px)');contents.open=!narrow.matches;narrow.addEventListener('change',ev=>{contents.open=!ev.matches;});}
  let indexPromise, opener;
  const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase();
  function localize() {
    const t=strings[lang];
    dialog.lang=lang;
    document.querySelector('.footer').lang=lang;
    document.querySelector('.skip').lang=lang;
    const languageNote=document.querySelector('.article-language');
    if(languageNote)languageNote.lang=lang;
    document.querySelectorAll('[data-i18n]').forEach(el=>{el.textContent=t[el.dataset.i18n];el.lang=lang;});
    document.querySelectorAll('.blog-date time').forEach(el=>{el.lang=lang;el.textContent=new Intl.DateTimeFormat(lang==='pt'?'pt-BR':'en',{dateStyle:'long',timeZone:'UTC'}).format(new Date(el.dateTime));});
    document.querySelector('[data-search-close]').setAttribute('aria-label',t.close);
    if(isBlog) {
      if(blogInput) document.querySelector('main').lang=lang;
      const prefix=lang==='pt'?'/':'/en/';
      const targets=[prefix+'#projects',prefix+'about.html',prefix+'about.html#publications',prefix+'#contact'];
      document.querySelector('[data-home]').href=prefix;
      document.querySelector('.header').lang=lang;
      document.querySelector('.nav').setAttribute('aria-label',lang==='pt'?'Principal':'Main');
      document.querySelectorAll('[data-nav]').forEach((a,i)=>{a.href=targets[i];a.textContent=t.nav[i];});
      document.querySelectorAll('[data-ui-language]').forEach(a=>{if(a.dataset.uiLanguage===lang)a.setAttribute('aria-current','true');else a.removeAttribute('aria-current');});
    }
    try{localStorage.setItem('site-language',lang);}catch(_){}
    if(dialog.open) runSearch();
  }
  function loadIndex() {
    if(!indexPromise) indexPromise=fetch(body.dataset.searchIndex).then(r=>{if(!r.ok)throw Error('search');return r.json();}).catch(err=>{indexPromise=null;throw err;});
    return indexPromise;
  }
  function match(rows,query,onlyBlog=false) {
    const tokens=normalize(query).trim().split(/\s+/).filter(Boolean);
    return rows.filter(row=>!onlyBlog || row.objectID.startsWith('blog/') && row.objectID!=='blog/index.html').map(row=>{
      const title=normalize(row.title),text=normalize(row.text);
      if(!tokens.every(t=>title.includes(t)||text.includes(t)))return null;
      const score=tokens.reduce((s,t)=>s+(title.includes(t)?20:0),0)+(row.objectID.startsWith('blog/')&&row.objectID!=='blog/index.html'?8:0)+(row.objectID.startsWith(lang==='en'?'en/':'en/')?(lang==='en'?2:-2):0);
      return {...row,score};
    }).filter(Boolean).sort((a,b)=>b.score-a.score);
  }
  let generation=0;
  async function runSearch() {
    const current=++generation, query=input.value.trim(),t=strings[lang];results.replaceChildren();
    if(!query){status.textContent=t.prompt;return;}
    status.textContent=t.loading;
    try {
      const rows=await loadIndex();if(current!==generation)return;
      const found=match(rows,query);status.textContent=found.length?t.count(found.length):t.empty;
      found.slice(0,30).forEach(row=>{
        const li=document.createElement('li'),a=document.createElement('a'),p=document.createElement('p');
        a.href='/'+row.href;a.textContent=row.title;p.textContent=row.description||row.text.slice(0,170)+'…';li.append(a,p);results.append(li);
      });
    } catch(_){if(current===generation)status.textContent=t.error;}
  }
  async function filterBlog() {
    const query=blogInput.value.trim(),t=strings[lang],notice=document.querySelector('#blog-status');
    try {
      const matches=new Set((await loadIndex()).filter(row=>!query||match([row],query,true).length).map(row=>'/'+row.href));
      let count=0;document.querySelectorAll('#blog-posts article').forEach(el=>{el.hidden=!matches.has(new URL(el.querySelector('a').href).pathname.replace(/index\.html$/, ''));if(!el.hidden)count++;});
      notice.textContent=query?(count?t.count(count):t.empty):'';
    } catch(_){notice.textContent=t.error;}
  }
  document.querySelectorAll('[data-search-open]').forEach(button=>button.addEventListener('click',()=>{opener=button;dialog.showModal();runSearch();input.focus();}));
  document.querySelector('[data-search-close]').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>opener?.focus());
  dialog.addEventListener('click',ev=>{if(ev.target===dialog){const r=dialog.getBoundingClientRect();if(ev.clientX<r.left||ev.clientX>r.right||ev.clientY<r.top||ev.clientY>r.bottom)dialog.close();}});
  document.addEventListener('keydown',ev=>{if(ev.key==='/'&&!dialog.open&&!ev.ctrlKey&&!ev.metaKey&&!ev.altKey&&!ev.target.closest('input,textarea,[contenteditable]')){ev.preventDefault();opener=document.activeElement;dialog.showModal();runSearch();input.focus();}});
  input.addEventListener('input',runSearch);
  if(blogInput)blogInput.addEventListener('input',filterBlog);
  document.querySelectorAll('[data-ui-language]').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault();lang=a.dataset.uiLanguage;localize();if(blogInput)filterBlog();}));
  localize();
})();
