#!/usr/bin/env python3
"""Dependency-free static build. Default: review version; --release enforces legal completion."""
from pathlib import Path
import html, json, re, runpy, shutil, sys
from content_en import ARTICLES, HELP_EN

ROOT=Path(__file__).parent
OUT=ROOT/'dist'
CFG=json.loads((ROOT/'site-config.json').read_text())
release='--release' in sys.argv
if release and not (CFG['legal_review_complete'] and CFG['operator_address'] and CFG['operator_email']):
    raise SystemExit('Release blocked: complete verified operator details and legal review in site-config.json.')
OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
de=runpy.run_path(str(ROOT/'content_de.py'))
icon=de['icon']
MAP={'/':'/','/wandern/':'/hiking/','/radfahren/':'/cycling/','/idee/':'/about/','/ausblick/':'/whats-next/','/ausprobieren/':'/try/','/datenschutz/':'/privacy/','/projekt/':'/project/','/hilfe/':'/help/','/impressum/':'/legal/','/404/':'/404/'}
for (de_slug,*_),(en_slug,*_) in zip(de['HELP'],HELP_EN):
    MAP['/hilfe/'+de_slug+'/']='/help/'+en_slug+'/'
REVERSE={v:k for k,v in MAP.items()}
def brand(lang):
    return f'<a class="brand" href="{"/de/" if lang=="de" else "/"}" aria-label="OnPath"><img src="/assets/brand.svg" alt="" width="44" height="44"><span>OnPath</span></a>'
def languages(lang,path):
    return f'<a class="language-switch" href="{MAP[path] if lang=="de" else "/de"+REVERSE[path]}" lang="{"en" if lang=="de" else "de"}" hreflang="{"en" if lang=="de" else "de"}" aria-label="{"Read in English" if lang=="de" else "Auf Deutsch lesen"}">{"EN" if lang=="de" else "DE"}</a>'
def footer_en():
    return f'<footer><div class="wrap"><div class="footer-grid"><div>{brand("en")}<p>Ride. Walk. Make it your route.</p><span class="fine">An independent project by Christian Neuhaus.</span></div><div><b>OnPath</b><a href="/cycling/">Cycling &amp; ADFC</a><a href="/hiking/">Hiking</a><a href="/about/">The idea</a><a href="/whats-next/">What comes next</a></div><div><b>Good to know</b><a href="/help/">Help &amp; first steps</a><a href="/try/">Try OnPath</a><a href="/privacy/">Privacy</a><a href="/legal/">Legal notice</a></div><div><b>The project</b><a href="/project/">Credits &amp; status</a><a href="https://github.com/happychriss/OnPath">App source on GitHub ↗</a></div></div><div class="footer-bottom"><span>© 2026 OnPath · Christian Neuhaus</span><span>Android · In development</span></div></div></footer><button class="backtop" aria-label="Back to top" hidden>↑</button>'
def write(path,title,desc,body,lang='en',original=None):
    en=MAP[path] if lang=='de' else path
    depath=path if lang=='de' else REVERSE[path]
    local='/de'+path if lang=='de' else path
    head=f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | OnPath</title><meta name="description" content="{html.escape(desc,quote=True)}"><meta name="theme-color" content="#245f46"><link rel="icon" href="/assets/brand.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><script src="/assets/app.js" defer></script>'
    for code,p in [('en',en),('de','/de'+depath),('x-default',en)]:
        head+=f'<link rel="alternate" hreflang="{code}" href="{CFG["origin"]}{p}">'
    if not release:head+='<meta name="robots" content="noindex,nofollow">'
    if lang=='de':
        h=de['header'](original or '')
        h=re.sub(r'href="(/[^\"]*)"',lambda m:'href="/de'+m[1]+'"',h)
        h=h.replace('</nav>',languages(lang,path)+'</nav>')
        f=de['footer']().replace('<a href="/datenschutz/">Datenschutz</a>','<a href="/datenschutz/">Deine Daten</a><a href="/impressum/">Impressum</a>')
        f=re.sub(r'href="(/[^\"]*)"',lambda m:'href="/de'+m[1]+'"',f)
        body=re.sub(r'href="(/[^\"]*)"',lambda m:'href="/de'+m[1]+'"',body)
    else:
        h=f'<a class="skip" href="#inhalt">Skip to content</a><header><div class="wrap header-row">{brand(lang)}<button class="menu" aria-expanded="false" aria-controls="navigation">Menu ☰</button><nav id="navigation" aria-label="Main navigation"><a href="/#discover">The app</a><a href="/about/">The idea</a><a href="/whats-next/">What’s next</a><a href="/help/">Help</a><a class="button small" href="/try/">Try OnPath {icon("arrow")}</a>{languages(lang,path)}</nav></div></header>'
        f=footer_en()
    document='<!doctype html><html lang="'+lang+'"><head>'+head+'</head><body>'+h+'<main id="inhalt">'+body+'</main>'+f+'</body></html>'
    dest=OUT/local.strip('/')/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(document)
def intro(title,desc,eye='OnPath'):
    return f'<section class="page-hero"><div class="wrap"><p class="eyebrow">{eye}</p><h1>{title}</h1><p class="lead">{desc}</p></div></section>'
def article(path,title,desc,sections,help_page=False):
    if help_page:
        side='<b>Help &amp; first steps</b>'+''.join(f'<a href="/help/{slug}/">{t}</a>' for slug,t,*_ in HELP_EN)
    else:
        side='<b>On this page</b>'+''.join(f'<a href="#section-{i}">{t}</a>' for i,(t,_) in enumerate(sections))
    contents=''.join(f'<section id="section-{i}"><h2>{t}</h2><p>{text}</p></section>' for i,(t,text) in enumerate(sections))
    write(path,title,desc,intro(title,desc,'Help &amp; first steps' if help_page else 'OnPath')+f'<section class="section"><div class="wrap article-layout"><aside class="side-nav">{side}</aside><article class="prose">{contents}<div class="article-end"><a href="/help/">All help topics →</a><a href="/try/">Try OnPath →</a></div></article></div></section>')

for path,(title,desc,body,active) in de['PAGES'].items():write(path,title,desc,body,'de',active)
for path,(title,desc,sections) in ARTICLES.items():article(path,title,desc,sections)
for slug,title,desc,keys,sections in HELP_EN:article('/help/'+slug+'/',title,desc,sections,True)
cards=''.join(f'<a class="help-card" data-keywords="{keys}" href="/help/{slug}/"><h2>{title}</h2><p>{desc}</p><span aria-hidden="true">→</span></a>' for slug,title,desc,keys,_ in HELP_EN)
write('/help/','Help for your next outing','Short, practical guides for planning, navigating and keeping your tours.',intro('How can we help?','Start with your first route or find an answer for a question along the way.','OnPath help')+f'<section class="section"><div class="wrap"><div class="help-search"><label for="help-search">Find a help topic</label><div>{icon("search")}<input type="search" id="help-search" placeholder="For example: maps, Google or battery"></div></div><p class="fine" id="search-count" role="status">9 help topics</p><div class="help-grid">{cards}</div><p id="no-results" hidden>No topic found. Try a shorter word.</p></div></section>')
home=f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">The app for cycling and hiking</p><h1>Your route.<br><span>Simply planned.</span></h1><p class="lead">On your bike or on foot: choose a destination and find a way there. Change the plan along the way, even without reception when the maps are ready.</p><div class="actions"><a class="button" href="/try/">Get to know OnPath {icon('arrow')}</a><a class="plain-link" href="#discover">See what it does ↓</a></div><p class="hero-note">Android · No OnPath account · Early test version</p></div><figure class="hero-photo"><img src="/assets/forest-real.webp" alt="A walking path through woodland near Ramsau" width="1800" height="2699" fetchpriority="high"><figcaption>Your next path awaits.<span class="photo-location">Ramsau bei Berchtesgaden</span></figcaption></figure></div></section>
<section class="section" id="discover"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">For real days out</p><h2>A good plan can change.</h2></div><p>A café is closed. A path is blocked. Or you feel like heading home sooner. Your app should make that easy.</p></div><div class="feature-grid">'''
for ic,title,text in [('offline','No reception? Keep planning.','Download the area before you leave. OnPath calculates routes on your phone, so a new route does not need mobile data.'),('route','A detour can fit in.','Change a stop or choose another destination. Your recording keeps running while you adjust the remaining plan.'),('shield','You choose the way.','If you leave the route, OnPath asks before calculating another. An accidental map tap does not change your plan.')]:
    home+=f'<article class="feature"><div class="feature-top">{icon(ic)}</div><h3>{title}</h3><p>{text}</p></article>'
home+='</div></div></section><section class="section soft" id="how"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">Ride or walk</p><h2>Make the day your own.</h2></div><p>You choose the destination. OnPath connects your stops along suitable paths.</p></div><div class="choice-grid">'
for title,text,link,label in [('Cycling','Choose Bike, Gravelbike, E-bike, MTB or E-MTB. Check surfaces and climbing, then leave room for a stop along the way.','/cycling/','More about cycling'),('Hiking','Find a hut or village, choose a difficulty and check the distance, climbing and estimated time.','/hiking/','More about hiking'),('ADFC members','Take a route from your local group as a GPX file and follow it with downloaded maps. OnPath is an independent project.','/cycling/','For ADFC members')]:
    home+=f'<article><h3>{title}</h3><p>{text}</p><a class="text-link" href="{link}">{label} →</a></article>'
home+='</div><p class="section-footnote">A café or hut along the way? Find it in OnPath, check the opening hours in Google Maps and add it as a stop. <a href="/help/places/">Places and Google Maps →</a></p></div></section><section class="story-section"><div class="wrap story-grid"><div><p class="eyebrow">Why OnPath?</p><h2>More time on the trail.<br>Less time in the app.</h2></div><div><p class="story-text">“I used Komoot for years. I wanted easier changes along the way, including without reception. That is how OnPath started.”</p><p>Christian Neuhaus develops OnPath from his own walking and cycling experience, with support from AI. The focus is your outing, without a social feed or leaderboards.</p><a class="text-link" href="/about/">The idea and the differences →</a></div></div></section><section class="section"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">Part of the idea</p><h2>Open code.<br>Your tours stay yours.</h2></div><p>A useful app with free core functions and a fair approach to your data.</p></div><div class="points"><p><b>The core stays free.</b>Planning, navigation and offline changes with downloaded maps remain free to use.</p><p><b>Keep your own files.</b>Tours live on your phone as ordinary tour files. No OnPath account and no ads.</p><p><b>Open source, normally used.</b>The app code is public. You do not need programming skills to use OnPath.</p></div><a class="text-link" href="/whats-next/">The free core and funding →</a></div></section><section class="section soft"><div class="wrap cta"><p class="eyebrow">Help make it useful</p><h2>Come along for a test ride or walk.</h2><p>The planned group test will use Google Play. Invitation links are being prepared.</p><div class="actions"><a class="button" href="/try/">About the test phase →</a></div><span class="fine">Android 8 or newer · Early test version · No spoken directions or iPhone app yet</span><p class="cta-links"><a class="text-link" href="/help/">Help and first steps →</a><a class="text-link" href="/whats-next/">Current status and next steps →</a></p></div></section>'
write('/','Your route. Simply planned.','Plan and follow cycling and hiking routes, change the plan and keep your own files.',home)
write('/404/','Page not found','Find your way back to OnPath.',intro('This path ends here.','Use the home page or help to find your way back.')+'<section class="section"><div class="wrap actions"><a class="button" href="/">Home</a><a class="text-link" href="/help/">Help →</a></div></section>')
(OUT/'404.html').write_text((OUT/'404/index.html').read_text())
(OUT/'robots.txt').write_text('User-agent: *\n'+('Allow: /\n' if release else 'Disallow: /\n'))
(OUT/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n'+('' if release else '  X-Robots-Tag: noindex, nofollow\n'))
if release:
    for legal_path in ['legal/index.html','privacy/index.html','de/impressum/index.html','de/datenschutz/index.html']:
        legal_text=(OUT/legal_path).read_text()
        if any(marker in legal_text for marker in ['Noch zu ergänzen','not a completed legal','incomplete draft','müssen die Angaben','Entwurf für den späteren','Draft provider information']):
            raise SystemExit('Release blocked: unresolved legal draft text in '+legal_path)
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+CFG['origin']+p+'</loc></url>' for p in list(MAP.values())+['/de'+p for p in MAP])+ '</urlset>')
print('Built',len(MAP)*2,'pages; mode:', 'release' if release else 'review')
