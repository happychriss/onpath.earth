#!/usr/bin/env python3
"""Dependency-free static build. Default: review version; --release enforces legal completion."""
from pathlib import Path
import hashlib, html, json, re, runpy, shutil, sys
from content_en import ARTICLES, HELP_EN
from help_shots import shots_html
from help_topics import help_anchor

ROOT=Path(__file__).parent
OUT=ROOT/'dist'
CFG=json.loads((ROOT/'site-config.json').read_text())
release='--release' in sys.argv
if release and not (CFG['legal_review_complete'] and CFG['operator_address'] and CFG['operator_email']):
    raise SystemExit('Release blocked: complete verified operator details and legal review in site-config.json.')
OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)

def versioned_asset(filename):
    """Give changed CSS/JS a new URL so cached assets cannot outlive their HTML."""
    source=ROOT/'assets'/filename
    content=source.read_bytes()
    digest=hashlib.sha256(content).hexdigest()[:12]
    versioned=f'{source.stem}.{digest}{source.suffix}'
    (OUT/'assets'/versioned).write_bytes(content)
    return '/assets/'+versioned

STYLESHEET_URL=versioned_asset('style.css')
SCRIPT_URL=versioned_asset('app.js')
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
    return f'<footer><div class="wrap"><div class="footer-grid"><div>{brand("en")}<p>Ride. Walk. Make it your route.</p><span class="fine">An independent project by Christian Neuhaus.</span></div><div><b>OnPath</b><a href="/cycling/">Cycling</a><a href="/hiking/">Hiking</a><a href="/about/">The idea</a><a href="/whats-next/">What comes next</a></div><div><b>Good to know</b><a href="/help/">Help &amp; first steps</a><a href="/try/">Try OnPath</a><a href="/privacy/">Privacy</a><a href="/legal/">Legal notice</a></div><div><b>The project</b><a href="/project/">Credits &amp; status</a><a href="mailto:info@onpath.earth">Email OnPath</a><a href="https://github.com/happychriss/OnPath">App source on GitHub ↗</a></div></div><div class="footer-bottom"><span>© 2026 OnPath · Christian Neuhaus</span><span>Android · In development</span></div></div></footer><button class="backtop" aria-label="Back to top" hidden>↑</button>'
def write(path,title,desc,body,lang='en',original=None):
    en=MAP[path] if lang=='de' else path
    depath=path if lang=='de' else REVERSE[path]
    local='/de'+path if lang=='de' else path
    head=f'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | OnPath</title><meta name="description" content="{html.escape(desc,quote=True)}"><meta name="theme-color" content="#245f46"><link rel="icon" href="/assets/brand.svg" type="image/svg+xml"><link rel="stylesheet" href="{STYLESHEET_URL}"><script src="{SCRIPT_URL}" defer></script>'
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
    slug=path.strip('/').split('/')[-1] if help_page else None
    contents=''.join(f'<section id="section-{i}"><h2'+(f' id="{help_anchor("en",slug,i)}"' if help_page else '')+f'>{t}</h2><p>{text}</p>'+(shots_html('en',slug,i) if help_page else '')+'</section>' for i,(t,text) in enumerate(sections))
    if help_page:
        contents='<nav class="help-contents" aria-label="In this help topic"><b>In this help topic</b><ul>'+''.join(f'<li><a href="#{help_anchor("en",slug,i)}">{t}</a></li>' for i,(t,_) in enumerate(sections))+'</ul></nav>'+contents
    write(path,title,desc,intro(title,desc,'Help &amp; first steps' if help_page else 'OnPath')+f'<section class="section"><div class="wrap article-layout"><aside class="side-nav">{side}</aside><article class="prose">{contents}<div class="article-end"><a href="/help/">All help topics →</a><a href="/try/">Try OnPath →</a></div></article></div></section>')

for path,(title,desc,body,active) in de['PAGES'].items():write(path,title,desc,body,'de',active)
for path,(title,desc,sections) in ARTICLES.items():
    if path!='/try/':article(path,title,desc,sections)
write('/try/','Try OnPath by personal invitation','Phase 1: test OnPath with a personal invitation and approval from Christian.',de['tester_page']('en'))
for slug,title,desc,keys,sections in HELP_EN:article('/help/'+slug+'/',title,desc,sections,True)
cards=''.join(f'<a class="help-card" data-keywords="{keys}" href="/help/{slug}/"><h2>{title}</h2><p>{desc}</p><span aria-hidden="true">→</span></a>' for slug,title,desc,keys,_ in HELP_EN)
write('/help/','Help for your next outing','Short, practical guides for planning, navigating and keeping your tours.',intro('How can we help?','Start with your first route or find an answer for a question along the way.','OnPath help')+f'<section class="section"><div class="wrap"><div class="help-search"><label for="help-search">Find a help topic</label><div>{icon("search")}<input type="search" id="help-search" placeholder="For example: maps, Google or battery"></div></div><p class="fine" id="search-count" role="status">9 help topics</p><div class="help-grid">{cards}</div><p id="no-results" hidden>No topic found. Try a shorter word.</p></div></section>')
home=de['home_hero']('en')
home+=de['first_steps']('en')+de['more_section']('en')+de['ways_section']('en')+de['small_section']('en')+de['open_section']('en')+de['home_cta']('en')
write('/','Your route. Simply on your way.','Plan and follow cycling and hiking routes, change the plan and keep your own files.',home)
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
