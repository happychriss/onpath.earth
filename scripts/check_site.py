#!/usr/bin/env python3
"""Check generated routes, links/anchors, translations and local resources."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'dist'
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.assets=[];self.ids=set();self.h1=0;self.lang='';self.languages=set();self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang','')
        if tag=='h1':self.h1+=1
        if 'id' in a:self.ids.add(a['id'])
        if 'href' in a:self.links.append(a['href'])
        if tag in ['script','img'] and 'src' in a:self.assets.append(a['src'])
        if tag=='link' and a.get('rel')=='stylesheet':self.assets.append(a['href'])
        if tag=='link' and a.get('rel')=='alternate':self.languages.add(a.get('hreflang'))
pages={p:Page(p.read_text()) for p in D.rglob('*.html')}
errors=[]
for p,page in pages.items():
    if page.h1!=1:errors.append(f'{p}: expected one h1')
    if page.lang not in ['de','en']:errors.append(f'{p}: missing language')
    if page.languages!={'de','en','x-default'}:errors.append(f'{p}: missing translation metadata')
    for asset in page.assets:
        if asset.startswith(('http:','https:','//')):errors.append(f'{p}: remote resource {asset}')
    for link in page.links+page.assets:
        parts=urlsplit(link)
        if parts.scheme or parts.netloc:continue
        if parts.path:
            target=D/parts.path.lstrip('/') if parts.path.startswith('/') else p.parent/parts.path
            if parts.path.endswith('/'):target=target/'index.html'
        else:target=p
        if not target.exists():errors.append(f'{p}: missing target {link}')
        elif parts.fragment and target in pages and parts.fragment not in pages[target].ids:
            errors.append(f'{p}: missing anchor {link}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} HTML documents, internal links/anchors, bilingual metadata and local resources')
