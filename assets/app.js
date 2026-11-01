const english=document.documentElement.lang==='en';
const menu=document.querySelector('.menu'),nav=document.querySelector('#navigation');menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.innerHTML=open?(english?'Close ×':'Schließen ×'):(english?'Menu ☰':'Menü ☰')});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){menu.click();menu.focus()}});
const states=[{d:'M60 260 120 210 170 230 235 125 320 100 440 70',text:'Du hast Start und Ziel gewählt. OnPath verbindet die Punkte über Wege.'},{d:'M60 260 120 210 220 255 310 215 375 160 440 70',text:'Du möchtest zum Café? Ergänze den Ort als Zwischenstopp. OnPath passt den weiteren Weg an.'},{d:'M60 260 120 210 220 255 310 215 375 160 440 70',text:'Weiter geht’s. Deine bisherige Tour bleibt aufgezeichnet, auch wenn du den Plan änderst.'}];document.querySelectorAll('[data-demo]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-demo]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const i=Number(b.dataset.demo);document.querySelector('#demo-route').setAttribute('d',states[i].d);document.querySelector('#old-route').style.opacity=i===0?'0':'.55';document.querySelector('#cafe-dot').setAttribute('opacity',i===0?'0':'1');document.querySelector('#demo-text').textContent=b.dataset.text||states[i].text}));
const search=document.querySelector('#help-search');search?.addEventListener('input',()=>{const q=search.value.toLocaleLowerCase('de').trim();let count=0;document.querySelectorAll('.help-card').forEach(c=>{const visible=(c.textContent+' '+c.dataset.keywords).toLocaleLowerCase('de').includes(q);c.hidden=!visible;if(visible)count++});document.querySelector('#search-count').textContent=count+(english?' matching help topics':' passende Hilfethemen');document.querySelector('#no-results').hidden=count>0});const back=document.querySelector('.backtop');window.addEventListener('scroll',()=>{if(back)back.hidden=window.scrollY<600},{passive:true});back?.addEventListener('click',()=>window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));

document.querySelectorAll('[data-shot]').forEach(b=>b.addEventListener('click',()=>{
  const group=b.closest('.benefit-group')||document;
  group.querySelectorAll('[data-shot]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
  const image=group.querySelector('[data-preview-img],#shot-img');
  const caption=group.querySelector('[data-preview-text],#shot-text');
  if(image){image.src=b.dataset.shot;image.alt=b.dataset.alt}
  if(caption)caption.textContent=b.dataset.text;
}));

document.querySelectorAll('[data-web]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-web]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const i=document.querySelector('#web-img');i.src=b.dataset.web;i.alt=b.dataset.alt;document.querySelector('#web-text').textContent=b.dataset.text}))


// A native modal keeps keyboard focus inside the enlarged screenshot.
const screenshotTriggers=document.querySelectorAll('[data-lightbox]');
if(screenshotTriggers.length){
  const viewer=document.createElement('dialog');
  viewer.className='screenshot-viewer';
  viewer.setAttribute('aria-label',english?'Enlarged screenshot':'Vergrößerter Screenshot');
  const close=document.createElement('button');
  close.type='button';close.className='screenshot-close';close.textContent='×';
  close.setAttribute('aria-label',english?'Close screenshot':'Screenshot schließen');
  const full=document.createElement('button');
  full.type='button';full.className='screenshot-full';
  full.setAttribute('aria-label',english?'Close screenshot':'Screenshot schließen');
  const img=document.createElement('img');full.append(img);viewer.append(close,full);document.body.append(viewer);
  let trigger=null;
  const dismiss=()=>viewer.close();
  close.addEventListener('click',dismiss);full.addEventListener('click',dismiss);
  viewer.addEventListener('click',e=>{if(e.target===viewer)dismiss()});
  viewer.addEventListener('close',()=>trigger?.focus({preventScroll:true}));
  screenshotTriggers.forEach(button=>button.addEventListener('click',()=>{
    trigger=button;const source=button.querySelector('img');
    img.src=source.src;img.alt=source.alt;viewer.showModal();close.focus();
  }));
}
