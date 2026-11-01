import sys as _sys, os as _os
_sys.path.insert(0,_os.path.dirname(_os.path.abspath(__file__)))
from help_shots import shots_html, files as shot_files, IMAGES as HELP_IMAGES
from help_topics import help_anchor
from pathlib import Path
import html, json
ROOT=Path(__file__).parent; D=ROOT/'dist'; A=D/'assets'; A.mkdir(parents=True,exist_ok=True)
GITHUB='https://github.com/happychriss/OnPath'
icons={
'route':'<circle cx="5" cy="18" r="2"/><circle cx="19" cy="6" r="2"/><path d="M7 18h7a4 4 0 0 0 0-8H9a4 4 0 0 1 0-8h5"/>',
'offline':'<path d="m3 3 18 18M2 8a16 16 0 0 1 3-2m4-1a16 16 0 0 1 13 3M5 12a11 11 0 0 1 4-2m4 0a11 11 0 0 1 6 2m-11 4a6 6 0 0 1 6-1"/><circle cx="12" cy="20" r="1"/>',
'check':'<path d="m5 12 4 4 10-10"/>',
'mountain':'<path d="m2 20 7-14 4 8 3-5 6 11ZM6 12l3 2 2-2"/>',
'bike':'<circle cx="5" cy="17" r="4"/><circle cx="19" cy="17" r="4"/><path d="m5 17 5-9 5 9H5m5-9h7l2 9M8 5h4m4-2h3l2 4"/>',
'shield':'<path d="M12 2 3 6v6c0 6 9 10 9 10s9-4 9-10V6ZM8 12l3 3 5-6"/>',
'pin':'<path d="M19 9c0 6-7 13-7 13S5 15 5 9a7 7 0 0 1 14 0Z"/><circle cx="12" cy="9" r="2"/>',
'file':'<path d="M14 2H5v20h14V7Zm0 0v5h5M8 12h8m-8 4h6"/>',
'arrow':'<path d="M4 12h16m-6-6 6 6-6 6"/>',
'search':'<circle cx="10" cy="10" r="7"/><path d="m15 15 6 6"/>',
'phone':'<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/>',
'computer':'<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 22h8m-4-5v5"/>',
'heart':'<path d="M12 21S2 15 2 8a5 5 0 0 1 10-2 5 5 0 0 1 10 2c0 7-10 13-10 13Z"/>'}
icons.update({'group':'<circle cx="9" cy="8" r="3"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c2.8 0 5 1.4 5 4"/>','clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>','cable':'<path d="M3 4l18 4"/><path d="M12 6v4"/><rect x="6" y="10" width="12" height="9" rx="2"/><path d="M6 14h12"/>','vibrate':'<rect x="8" y="4" width="8" height="16" rx="2"/><path d="M4 9v6M20 9v6"/>','profile':'<path d="M3 18 8 11l4 3 4-7 5 6"/><path d="M3 21h18"/>'})
def icon(k):return '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">'+icons[k]+'</svg>'
brand='<a class="brand" href="/" aria-label="OnPath Startseite"><img src="/assets/brand.svg" alt="" width="44" height="44"><span>OnPath</span></a>'

def header(active=''):
 return '<a class="skip" href="#inhalt">Zum Inhalt</a><header><div class="wrap header-row">'+brand+'<button class="menu" aria-expanded="false" aria-controls="navigation">Menü <span aria-hidden="true">☰</span></button><nav id="navigation" aria-label="Hauptnavigation">'+''.join('<a '+('aria-current="page" ' if active==p else '')+'href="'+p+'">'+t+'</a>' for p,t in [('/#entdecken','Die App'),('/idee/','Die Idee'),('/ausblick/','Was kommt'),('/hilfe/','Hilfe')])+'<a class="button small" href="/ausprobieren/">OnPath ausprobieren '+icon('arrow')+'</a></nav></div></header>'
def footer():return '<footer><div class="wrap"><div class="footer-grid"><div>'+brand+'<p>Wandern und Radfahren.<br>Mit einem Plan, der zu dir passt.</p><span class="fine">Von Christian Neuhaus entwickelt. Der App-Code ist öffentlich.</span></div><div><b>OnPath</b><a href="/wandern/">Wandern</a><a href="/radfahren/">Radfahren</a><a href="/idee/">Die Idee dahinter</a><a href="/ausblick/">Was als Nächstes kommt</a></div><div><b>Gut zu wissen</b><a href="/hilfe/">Hilfe & erste Schritte</a><a href="/datenschutz/">Datenschutz</a><a href="/projekt/">Projekt & Bildnachweis</a></div><div><b>Mitmachen</b><a href="/ausprobieren/">Tester werden</a><a href="mailto:info@onpath.earth">E-Mail an OnPath</a><a href="'+GITHUB+'/issues">Fehler melden ↗</a><a href="'+GITHUB+'">Quellcode auf GitHub ↗</a></div></div><div class="footer-bottom"><span>© 2026 OnPath · Christian Neuhaus</span><span>Android · Deutsch & Englisch · In Entwicklung</span></div></div></footer><button class="backtop" aria-label="Nach oben" hidden>↑</button>'
PAGES={}
def page(path,title,desc,body,active=''):
 PAGES[path]=(title,desc,body,active)
def ph(eyebrow,title,desc,breadcrumb=''):
 return '<section class="page-hero"><div class="wrap">'+('<div class="breadcrumb"><a href="/">Start</a> <span>/</span> '+breadcrumb+'</div>' if breadcrumb else '')+'<p class="eyebrow">'+eyebrow+'</p><h1>'+title+'</h1><p class="lead">'+desc+'</p></div></section>'
def button(url,text,outline=False):return '<a class="button'+(' outline' if outline else '')+'" href="'+url+'">'+text+icon('arrow')+'</a>'
def notice(title,text):return '<aside class="notice"><b>'+title+'</b><p>'+text+'</p></aside>'
def cta():return '<section class="section"><div class="wrap"><div class="cta"><p class="eyebrow">Gemeinsam besser machen</p><h2>Kommst du eine Runde mit?</h2><p>OnPath ist noch jung. Gesucht werden Menschen, die draußen unterwegs sind und sagen, was im Alltag klappt – und was noch nicht.</p><div class="actions">'+button('/ausprobieren/','Testversion kennenlernen')+'</div><span class="fine">Für Android ab Version 8 · Aktuell nur mit persönlicher Einladung</span></div></div></section>'
DEMO={'de':dict(top='Eine Tour. Ein neuer Plan.',tag='So funktioniert’s',aria='Schematische Tour mit einem zusätzlichen Zwischenstopp',cafe='Pause am Café',start='Start',end='Ziel',ctl='Beispielablauf',b=['1. Planen','2. Ändern','3. Weiter'],t=['Du hast Start und Ziel gewählt. OnPath verbindet die Punkte über Wege.','Du möchtest zum Café? Ergänze den Ort als Zwischenstopp. OnPath passt den weiteren Weg an.','Weiter geht’s. Deine bisherige Tour bleibt aufgezeichnet, auch wenn du den Plan änderst.'],fine='Vereinfachte Darstellung, keine bedienbare App-Karte.'),'en':dict(top='One tour. A new plan.',tag='How it works',aria='Schematic tour with an added stop',cafe='Café stop',start='Start',end='Finish',ctl='Example steps',b=['1. Plan','2. Change','3. Go on'],t=['You chose a start and a destination. OnPath connects them along paths.','Fancy a café? Add it as a stop. OnPath adjusts the rest of the way.','On you go. Your recording keeps running, even though the plan changed.'],fine='Simplified illustration, not the app’s map.')}
def route_demo(lang='de'):
    D=DEMO[lang]
    buttons=''.join('<button data-demo="'+str(i)+'" data-text="'+D['t'][i]+'" aria-pressed="'+('true' if i==0 else 'false')+'">'+D['b'][i]+'</button>' for i in range(3))
    return '<div class="demo"><div class="demo-top"><span>'+D['top']+'</span><span class="tag">'+D['tag']+'</span></div><svg class="route-demo" viewBox="0 0 520 330" role="img" aria-label="'+D['aria']+'"><path class="terrain" d="M-40 220C90 80 100 330 280 100S500 40 570 160M-40 250C90 110 100 360 280 130S500 70 570 190M-40 280C90 140 100 390 280 160S500 100 570 220"/><path class="stream" d="M360-20C210 70 430 150 310 220S270 300 330 360"/><path class="way" d="M60 260 120 210 170 230 235 125 320 100 375 160 440 70M120 210 220 255 310 215 375 160"/><path id="old-route" d="M60 260 120 210 170 230 235 125 320 100 440 70"/><path id="demo-route" d="M60 260 120 210 170 230 235 125 320 100 440 70"/><circle class="start-point" cx="60" cy="260" r="9"/><circle class="end-point" cx="440" cy="70" r="9"/><g id="cafe-dot" opacity="0"><circle cx="310" cy="215" r="9"/><rect x="305" y="234" width="120" height="34" rx="5"/><text x="320" y="256">'+D['cafe']+'</text></g><text class="map-label" x="38" y="292">'+D['start']+'</text><text class="map-label" x="425" y="44">'+D['end']+'</text></svg><div class="demo-controls" aria-label="'+D['ctl']+'">'+buttons+'</div><p id="demo-text" aria-live="polite">'+D['t'][0]+'</p><span class="fine">'+D['fine']+'</span></div>'
MORE={'de': {'eye': 'Auf dem Rad und zu Fuß',
        'h': 'Mehr Natur genießen. Weniger aufs Handy schauen.',
        'lead': 'OnPath sagt dir, wann du ankommst, wo du abbiegst und was vor dir liegt – ohne dass du lange suchen '
                'musst.',
        'items': [('route',
                   'Wege passend zu deiner Aktivität.',
                   'Für jede Aktivität rechnet OnPath anders: mit dem Rad über Radwege und ruhige Nebenstraßen, mit '
                   'dem Gravelbike gern auf Schotter, mit dem Mountainbike auf Trails, zu Fuß auf Wegen bis zu deiner '
                   'Schwierigkeit. Hauptstraßen nur, wenn es nicht anders geht.'),
                  ('clock',
                   'Du weißt, wann du ankommst.',
                   'Nach etwa 15 Minuten richtet sich die Ankunftszeit nach deinem Tempo, getrennt für bergauf, flach '
                   'und bergab.'),
                  ('pin',
                   'Hat die Hütte offen?',
                   'Ein Tipp auf den Ort öffnet ihn in Google Maps, mit Öffnungszeiten und Bildern. Zurück in OnPath '
                   'nimmst du ihn als Stopp in die Route.'),
                  ('vibrate',
                   'Das Handy bleibt in der Tasche.',
                   'Wo du falsch abbiegen könntest, vibriert es: einmal für links, zweimal für rechts. Der '
                   'Sperrbildschirm zeigt die nächste Abzweigung und die Ankunftszeit.'),
                  ('profile',
                   'Die Strecke vorher einschätzen.',
                   'Vor dem Start siehst du Steigungen, Untergrund und Hinweise wie „120 m Schieben · 2 steile '
                   'Abschnitte“ oder „Fähre – Fahrzeiten prüfen“.'),
                  ('cable',
                   'Mit Seilbahn oder Bus? Die Tour stimmt trotzdem.',
                   'Fahrten werden erkannt und lassen sich am Ende einfach herausnehmen.')],
        'links': [('/radfahren/', 'Mehr zum Radfahren'), ('/wandern/', 'Mehr zum Wandern')]},
 'en': {'eye': 'On the bike and on foot',
        'h': 'Enjoy more nature. Look at your phone less.',
        'lead': 'OnPath tells you when you will arrive, where to turn and what lies ahead – without searching around '
                'in the app.',
        'items': [('route',
                   'Routing to suit your activity.',
                   'OnPath routes differently for each activity: by bike on cycleways and quiet side roads, by gravel '
                   'bike happily on gravel, by mountain bike on trails, on foot on paths up to your difficulty. Main '
                   'roads only when there is no other way.'),
                  ('clock',
                   'You know when you will arrive.',
                   'After about 15 minutes the arrival time follows your own pace, uphill, flat and downhill '
                   'separately.'),
                  ('pin',
                   'Is the hut open?',
                   'One tap opens the place in Google Maps, with opening hours and photos. Back in OnPath you add it '
                   'to your route as a stop.'),
                  ('vibrate',
                   'Your phone stays in your pocket.',
                   'Where you could take the wrong way it vibrates: once for left, twice for right. The lock screen '
                   'shows the next junction and your arrival time.'),
                  ('profile',
                   'Assess the route before setting off.',
                   'Before you start you see gradients, surfaces and notes like “120 m pushing · 2 steep sections” or '
                   '“Ferry – check times”.'),
                  ('cable',
                   'Cable car or bus? Your tour still adds up.',
                   'Rides are recognised and can simply be left out at the end.')],
        'links': [('/cycling/', 'More about cycling'), ('/hiking/', 'More about hiking')]}}
SHOTS={'de':dict(top='So sieht OnPath aus',tag='App-Bildschirme',ctl='Bildschirm wählen',items=[('plan-wandern','Wandern','Planung einer Wanderung von Vellau zur Leiteralm mit Karte, Zeit und Höhenprofil','Wandern T2: Zeit, Höhenprofil und steile Abschnitte.'),('plan-ebike','E-Bike','Dieselbe Strecke mit dem E-Bike geplant, mit Hinweis auf Schiebestrecke','E-Bike: Untergrund und Schiebestrecken vor dem Start erkennen.'),('ort-google-maps','Ort finden','Menü zum Gasthof Hochmuth mit „Als neues Ziel anhängen“ und „In Google Maps öffnen“','Gasthof Hochmuth gefunden: als Ziel oder Stopp übernehmen oder bei Google Maps nach den Öffnungszeiten schauen.')]),'en':dict(top='What OnPath looks like',tag='App screens',ctl='Choose a screen',items=[('plan-wandern','Hiking','A hike planned from Vellau to the Leiteralm with map, time and elevation profile','Hike T2: time, elevation profile and steep sections.'),('plan-ebike','E-bike','The same route planned by e-bike, with a note about pushing','E-bike: check surfaces and pushing sections before setting off.'),('ort-google-maps','Find a place','Menu for the Gasthof Hochmuth with “Add as new destination” and “Open in Google Maps”','Found the Gasthof Hochmuth: add it as a destination or stop, or check the opening hours in Google Maps.')])}
def app_shots(lang='de'):
    S=SHOTS[lang]; first=S['items'][0]
    src=lambda k:'/assets/app/'+k+'-'+lang+'.webp'
    buttons=''.join('<button data-shot="'+src(k)+'" data-alt="'+alt+'" data-text="'+txt+'" aria-pressed="'+('true' if i==0 else 'false')+'">'+label+'</button>' for i,(k,label,alt,txt) in enumerate(S['items']))
    return '<div class="demo shots"><div class="demo-top"><span>'+S['top']+'</span><span class="tag">'+S['tag']+'</span></div><div class="shots-phone"><img id="shot-img" src="'+src(first[0])+'" alt="'+first[2]+'" width="600" height="1333" loading="lazy"></div><div class="demo-controls" aria-label="'+S['ctl']+'">'+buttons+'</div><p id="shot-text" aria-live="polite">'+first[3]+'</p></div>'
FEATURES={'de': {'rows': [('route',
                  'Schöne Wege, passend zu deiner Tour.',
                  'Sorgfältig abgestimmt: OnPath bevorzugt ausgewiesene Rad- und Wanderwege, meidet stark befahrene Straßen beim Radfahren und berücksichtigt deine gewählte Schwierigkeit beim Wandern.',
                  'plan-ebike'),
                 ('pin',
                  'Eine Einkehr, auf die du dich freust.',
                  'Fotos, Bewertungen und Öffnungszeiten in Google Maps ansehen – direkt aus OnPath. Gefällt dir die Einkehr? Plane sie als Stopp ein.',
                  'ort-google-maps')],
        'also': '<b>Außerdem:</b> Vibration an entscheidenden Abzweigungen · Ankunftszeit, die dein Tempo lernt · '
                'Seilbahn und Bus werden erkannt.'},
 'en': {'rows': [('route',
                  'Beautiful paths for your outing.',
                  'Carefully tuned: OnPath favours cycling and hiking paths, avoids busy roads when cycling and takes your hiking difficulty into account.',
                  'plan-ebike'),
                 ('pin',
                  'A stop to look forward to.',
                  'See photos, reviews and opening hours in Google Maps – straight from OnPath. Like the place? Add it as a stop.',
                  'ort-google-maps')],
        'also': '<b>Also:</b> a vibration at decision points · an arrival time that learns your pace · cable cars and '
                'buses recognised.'}}
WAYS={'de': {'eye': 'Am Computer vorbereiten',
        'h': 'Bequem am großen Bildschirm planen. Unterwegs auf dem Handy dabei.',
        'lead': 'Plane deine Tour am Computer und übertrage sie per QR-Code in die Android-App.',
        'cards': [('computer',
                   'Deine Tour vorbereiten',
                   ['Punkte mit der Maus setzen und verschieben.', 'Eine vorhandene Tourdatei (GPX) öffnen.']),
                  ('phone',
                   'Auf dem Handy weiter',
                   ['Den QR-Code mit der Handykamera scannen.',
                    'Oder Browser und Handy koppeln (im Test): Gespeicherte Pläne werden abgeglichen.'])],
        'note': 'Ohne Konto und Installation.',
        'open': 'Im Browser planen'},
 'en': {'eye': 'Prepare on your computer',
        'h': 'Plan comfortably on a big screen. Take it along on your phone.',
        'lead': 'Plan your route on the computer and transfer it to the Android app by QR code.',
        'cards': [('computer',
                   'Prepare your route',
                   ['Set and move points with the mouse.', 'Open an existing tour file (GPX).']),
                  ('phone',
                   'Continue on your phone',
                   ['Scan the QR code with your phone camera.',
                    'Or pair browser and phone (in testing) to sync saved plans.'])],
        'note': 'No account or installation needed.',
        'open': 'Plan in your browser'}}
WEBSHOT={'de':dict(tabs=[('web-wandern','Planen','Der Planer im Browser: eine Wanderung von Vellau zur Leiteralm mit Zeit, Höhenprofil und Hinweisen','Große Karte, Höhenprofil und Hinweise wie „2 steile Abschnitte“ – wie in der App.'),('web-qr','Teilen','Der Dialog „Teilen“ mit QR-Code','QR-Code scannen und die Tour aufs Handy übernehmen.')],ctl='Planer-Bildschirm wählen'),
'en':dict(tabs=[('web-wandern','Plan','The browser planner: a hike from Vellau to the Leiteralm with time, elevation profile and notes','A big map, elevation profile and notes like “2 steep sections” – as in the app.'),('web-qr','Share','The “Share” dialog with a QR code','Scan the QR code and take your route along.')],ctl='Choose a planner screen')}
def web_shot(lang='de'):
    W=WEBSHOT[lang]; t0=W['tabs'][0]; src=lambda k:'/assets/app/'+k+'-de.webp'
    btns=''.join('<button data-web="'+src(k)+'" data-alt="'+alt+'" data-text="'+txt+'" aria-pressed="'+('true' if i==0 else 'false')+'">'+lab+'</button>' for i,(k,lab,alt,txt) in enumerate(W['tabs']))
    return '<figure class="web-shot"><div class="browser-bar" aria-hidden="true"><i></i><i></i><i></i><span>plan.onpath.earth</span></div><img id="web-img" src="'+src(t0[0])+'" alt="'+t0[2]+'" width="1440" height="900" loading="lazy"><figcaption><div class="web-tabs" role="group" aria-label="'+W['ctl']+'">'+btns+'</div><span id="web-text" aria-live="polite">'+t0[3]+'</span></figcaption></figure>'
def ways_section(lang='de'):
    de=lang=='de'; W=WAYS[lang]; screens=WEBSHOT[lang]['tabs']
    title='Bequem am großen Bildschirm planen.' if de else 'Plan comfortably on a big screen.'
    items=[('Deine Tour vorbereiten.','Setze und verschiebe Punkte mit der Maus oder öffne eine vorhandene GPX-Tour.'),('Auf dem Handy weiter.','Scanne den QR-Code mit deiner Handykamera. Oder kopple Browser und Handy: Der Abgleich gespeicherter Pläne ist noch im Test.')] if de else [('Prepare your route.','Set and move points with the mouse or open an existing GPX route.'),('Continue on your phone.','Scan the QR code with your phone camera. Or pair browser and phone: syncing saved plans is still in testing.')]
    rows=[]
    for i,((heading,text),(key,_,alt,caption)) in enumerate(zip(items,screens)):
        src='/assets/app/'+key+'-de.webp'
        image=screenshot_button(src,alt,lang,'inline-preview')
        rows.append('<article class="feature-entry'+(' feature-primary' if i==0 else '')+'"><button class="feature-row" data-shot="'+src+'" data-alt="'+html.escape(alt,quote=True)+'" data-text="'+html.escape(caption,quote=True)+'" aria-pressed="'+('true' if i==0 else 'false')+'"><span><b>'+heading+'</b>'+text+'</span></button><figure class="inline-shot planner-inline">'+image+'</figure></article>')
    visual='<figure class="group-preview planner-preview">'+screenshot_button('/assets/app/'+screens[0][0]+'-de.webp',screens[0][2],lang,'preview-enlarge',True)+'<figcaption data-preview-text aria-live="polite">'+('Punkte setzen und die Strecke prüfen.' if de else 'Set points and review your route.')+'</figcaption></figure>'
    actions='<div class="ways-cta">'+button('https://plan.onpath.earth/',W['open'])+'<span class="ways-note">'+W['note']+'</span>'+home_help(lang,'browser',0)+'</div>'
    return '<section class="benefit-band" id="'+('planen' if de else 'plan')+'"><div class="wrap benefit-group benefit-browser" aria-labelledby="browser-heading"><h2 id="browser-heading">'+title+'</h2>'+visual+'<div class="feature-rows">'+''.join(rows)+actions+'</div></div></section>'
EXTRA={'de': [('clock',
         'Wissen, wann du ankommst.',
         'OnPath passt deine Ankunftszeit an dein Tempo an – bergauf, eben und bergab. So kannst du deine nächste Pause besser einschätzen.'),
        ('vibrate',
         'Das Handy bleibt öfter in der Tasche.',
         'OnPath sagt dir die Richtung und beschreibt den nächsten Weg. Sprache und Vibrationen wählst du selbst – auch offline.'),
        ('cable',
         'Deine Leistung zählt.',
         'OnPath erkennt Abschnitte mit Seilbahn oder Bus. Du entscheidest, ob Strecke und Zeit mitzählen.')],
 'en': [('clock',
         'Know when you will arrive.',
         'OnPath adjusts your arrival time to your pace – uphill, on the flat and downhill. That makes it easier to plan your next break.'),
        ('vibrate',
         'Keep your phone in your pocket more often.',
         'Get directions and details of the next path through speech, vibrations or both – your choice, even offline.'),
        ('cable',
         'Your own effort counts.',
         'OnPath recognises cable car and bus sections. You decide whether their distance and time count.')]}
SMALL={'de': {'eye': 'Im Alltag durchdacht',
        'h': 'Damit du deine Tour entspannt genießen kannst.',
        'cols': [('Unterwegs',
                  [('Tour beenden. Speichern. Fertig.',
                    'Speichern und das Handy wegstecken. Ohne weitere Nachfragen zu Fotos, Teilen oder Bewertungen. <a href="/hilfe/navigation/#tour-beenden">Tour speichern →</a>')]),
                 ('Beim Planen',
                  [('Wanderwege, die zu dir passen.',
                    'Wähle deine Schwierigkeit nach der SAC-Wanderskala des Schweizer Alpen-Clubs. OnPath berücksichtigt sie und zeigt anspruchsvollere Abschnitte an. <a href="/hilfe/route-planen/#schwierigkeit">SAC-Stufen erklärt →</a>'),
                   ('Schneller eine schöne Tour planen.',
                    'Kleine Runde oder Fernweg? Hervorgehobene Rad- und Wanderrouten und erkennbare Wegarten helfen dir, eine passende Tour zu finden. <a href="/hilfe/route-planen/#kartenfarben">Kartenfarben und Routen →</a>'),
                   ('Dein Ziel finden – auch ohne Netz.',
                    'Kein Netz, kein Zugriff auf Google Maps? Adressen, Hütten und Gipfel findest du in der eigenen Datenbank, die OnPath automatisch mit den Karten herunterlädt. <a href="/hilfe/orte/#offline-suche">Offline suchen →</a>')])],
        'link': ('/hilfe/', 'Alles Deine erste Tour: die Anleitung')},
 'en': {'eye': 'Thoughtful in everyday use',
        'h': 'Enjoy your outing with peace of mind.',
        'cols': [('On the way',
                  [('End your outing. Save. Done.',
                    'Save and put your phone away. No extra questions about photos, sharing or ratings. <a href="/help/navigation/#finish">Save your outing →</a>')]),
                 ('When planning',
                  [('Hiking paths that suit you.',
                    'Choose your difficulty using the Swiss Alpine Club’s SAC hiking scale. OnPath takes it into account and highlights more demanding sections. <a href="/help/planning/#difficulty">SAC levels explained →</a>'),
                   ('Plan a beautiful outing more quickly.',
                    'Local loop or long-distance trail? Highlighted cycling and hiking routes and clear path types help you find a suitable outing. <a href="/help/planning/#map-colours">Map colours and routes →</a>'),
                   ('Find your destination – even without reception.',
                    'No signal, no access to Google Maps? Find addresses, huts and peaks in OnPath’s own database, downloaded automatically with your maps. <a href="/help/places/#offline-search">Offline search →</a>')])],
        'link': ('/help/', 'Everything step by step in the help')}}
OPEN={'de': {'eye': 'Unabhängig und offen',
        'h': 'Deine Touren gehören dir.',
        'pts': [('',
                 'Deine Touren bleiben auf deinem Handy und zusätzlich als frei zugängliche GPX-Dateien erhalten. Gib sie weiter, nutze sie in anderen Apps oder exportiere alle abgeschlossenen Touren als ZIP. <a href="/hilfe/gpx/#eigene-dateien">Tourdateien sichern und exportieren →</a>'),
                ('Offen für die Zukunft.',
                 'Der Quellcode ist öffentlich. Planen, navigieren und aufzeichnen bleiben kostenlos. Beiträge unterstützen Betrieb, Weiterentwicklung und gemeinnützige Zwecke.')],
        'founder': 'Ich wandere und fahre selbst gern Rad. Deshalb entwickle ich OnPath: einfach, verlässlich und offen – mit Unterstützung von KI.',
        'role': 'Wanderer, Radfahrer und Entwickler',
        'idea': ('/idee/', 'Über OnPath'),
        'funding': ('/ausblick/#abschnitt-5', 'Mehr zur Finanzierung'),
        'founder_title': 'Aus Freude am Draußensein entwickelt.'},
 'en': {'eye': 'Independent and open',
        'h': 'Your tours belong to you.',
        'pts': [('',
                 'Your tours stay on your phone and are also kept as accessible GPX files. Share them, use them in other apps or export all completed outings as a ZIP file. <a href="/help/gpx/#your-files">Back up and export tour files →</a>'),
                ('Open for the future.',
                 'The source code is public. Planning, navigation and recording stay free. Contributions support running costs, development and charitable causes.')],
        'founder': 'I love hiking and cycling. That’s why I’m building OnPath: simple, reliable and open – with the help of AI.',
        'role': 'Hiker, cyclist and developer',
        'idea': ('/about/', 'About OnPath'),
        'funding': ('/whats-next/#section-5', 'More on funding'),
        'founder_title': 'Built from a love of the outdoors.'}}
def open_section(lang='de'):
    O=OPEN[lang]
    points=''.join('<p>'+('<b>'+title+'</b>' if title else '')+text+'</p>' for title,text in O['pts'])
    author='<div class="story-author"><img src="/assets/christian.webp" alt="" width="400" height="400"><span><b>Christian Neuhaus</b>'+O['role']+'</span></div>'
    funding='<a class="text-link" href="'+O['funding'][0]+'">'+O['funding'][1]+' →</a>'
    idea='<a class="text-link" href="'+O['idea'][0]+'">'+O['idea'][1]+' →</a>'
    ownership='<section class="section soft ownership-section"><div class="wrap"><div class="section-heading"><p class="eyebrow">'+O['eye']+'</p><h2>'+O['h']+'</h2></div><div class="points trust-points">'+points+'</div>'+funding+'</div></section>'
    founder='<section class="section founder-section"><div class="wrap"><div class="founder-note"><h2>'+O['founder_title']+'</h2>'+author+'<p>'+O['founder']+'</p>'+idea+'</div></div></section>'
    return ownership+founder
FIRST_STEPS={'de': {'eye': 'So einfach geht’s',
        'h': 'Schnell geplant. Draußen flexibel.',
        'lead': 'So beginnt deine erste Tour mit OnPath.',
        'items': [('halten',
                   'Deine Route in wenigen Schritten.',
                   'Drücke etwas länger auf dein Ziel – das verhindert versehentliches Auswählen. OnPath plant den Weg '
                   'von deinem Standort dorthin, passend zum Wandern oder Radfahren.',
                   'OnPath beim Öffnen: die Karte, ein Punkt gedrückt gehalten'),
                  ('plan',
                   'Vor dem Start wissen, ob die Tour zu dir passt.',
                   'Du siehst, wie lange du unterwegs bist und wie viele Höhenmeter dich erwarten. Streckenhinweise '
                   'machen dich auf Besonderheiten wie steile Abschnitte, Schiebestrecken oder Fähren aufmerksam. '
                   'Passt alles, startest du die Navigation.',
                   'Die geplante Route mit Zeit, Höhenprofil und „Navigation starten“'),
                  ('navi',
                   'Bleib spontan – auch ohne Empfang.',
                   'Ändere deine Route und zieh direkt weiter. OnPath lädt die Karten beim Planen automatisch herunter und berechnet den neuen Weg auf deinem Handy.',
                   'Navigation mit dem Schieber „Stopp“ unten')],
        'prep': '',
        'help': ('/hilfe/offline/', 'Karten vorbereiten'),
        'more': ('/hilfe/erste-schritte/', 'Deine erste Tour: die Anleitung')},
 'en': {'eye': 'It’s that simple',
        'h': 'Quick to plan. Free to explore.',
        'lead': 'This is how your first outing with OnPath begins.',
        'items': [('halten',
                   'Your route in a few simple steps.',
                   'Press a little longer on your destination to avoid selecting it by accident. OnPath plans the way '
                   'from your location, suited to hiking or cycling.',
                   'OnPath when it opens: the map, a point held down (German screen)'),
                  ('plan',
                   'Know whether the route suits you before you start.',
                   'See how long you will be out and how much climbing to expect. Route hints point out features such '
                   'as steep sections, pushing sections or ferries. Happy with the plan? Start navigation.',
                   'The planned route with time, elevation profile and “Start navigation”'),
                  ('navi',
                   'Stay spontaneous – even without reception.',
                   'Change your route. OnPath downloads maps automatically while you plan and calculates the new way on your phone.',
                   'Navigation with the “Stop” slider at the bottom (German screen)')],
        'prep': '',
        'help': ('/help/offline/', 'Prepare your maps'),
        'more': ('/help/getting-started/', 'Step by step in the help')}}
HOME_HELP = {
 'de': {
  'steps': [('/hilfe/route-planen/#punkte', 'Punkte setzen'), ('/hilfe/route-planen/#streckenhinweise', 'Streckenhinweise'), ('/hilfe/unterwegs-aendern/#aendern', 'Unterwegs umplanen')],
  'features': [('/hilfe/route-planen/#aktivitaet', 'Aktivität wählen'), ('/hilfe/orte/#einkehr', 'Einkehr einplanen')],
  'extras': [('/hilfe/navigation/#ankunft', 'Ankunftszeit'), ('/hilfe/navigation/#abbiegen', 'Sprache und Vibration'), ('/hilfe/navigation/#fahrten', 'Fahrten prüfen')],
  'browser': [('/hilfe/route-planen/#browser', 'Tour aufs Handy übertragen')]
 },
 'en': {
  'steps': [('/help/planning/#points', 'Set points'), ('/help/planning/#route-hints', 'Route hints'), ('/help/change-route/#edit', 'Change your route')],
  'features': [('/help/planning/#activity', 'Choose an activity'), ('/help/places/#stop', 'Plan a stop')],
  'extras': [('/help/navigation/#arrival', 'Arrival time'), ('/help/navigation/#turns', 'Speech and vibration'), ('/help/navigation/#rides', 'Review rides')],
  'browser': [('/help/planning/#browser', 'Transfer to your phone')]
 }
}
def home_help(lang, group, index):
    url, label = HOME_HELP[lang][group][index]
    return '<a class="context-help" href="'+url+'">'+label+' →</a>'

STEP_COPY={
 'de':[('Ziel wählen.','Drücke etwas länger auf dein Ziel auf der Karte – deine Route entsteht.'),('Tour prüfen.','Sieh dir Dauer, Höhenmeter und Streckenhinweise an.'),('Losgehen. Flexibel bleiben.','Starte die Navigation und passe deinen Weg unterwegs bei Bedarf an.')],
 'en':[('Choose a destination.','Press a little longer on your destination on the map to create your route.'),('Check your route.','Review time, climbing and route hints.'),('Set off. Stay flexible.','Start navigation and adjust your way along the journey when needed.')]
}
def first_steps(lang='de'):
    F=dict(FIRST_STEPS[lang]); F['items']=[(k,t,x,alt) for (k,_,_,alt),(t,x) in zip(F['items'],STEP_COPY[lang])]; anchor='entdecken' if lang=='de' else 'discover'
    cards=[]
    for i,(key,title,text,alt) in enumerate(F['items']):
        src='/assets/help/'+shot_files(key)[0 if lang=='de' else 1]
        label=('Screenshot zu Schritt '+str(i+1)+' vergrößern') if lang=='de' else ('Enlarge screenshot for step '+str(i+1))
        preview='<button type="button" class="step-preview step-preview-'+key+'" data-lightbox aria-haspopup="dialog" aria-label="'+label+'"><img class="step-thumb" src="'+src+'" alt="'+html.escape(alt,quote=True)+'" width="540" height="1200" loading="lazy"><span class="zoom-mark" aria-hidden="true">'+icon('search')+'</span></button>'
        cards.append('<article class="feature know"><div class="step-heading"><span class="step-number" aria-label="'+('Schritt ' if lang=='de' else 'Step ')+str(i+1)+'">'+str(i+1)+'</span><h3>'+title+'</h3></div><p>'+text+'</p>'+preview+home_help(lang,'steps',i)+'</article>')
    cards=''.join(cards)
    return '<section class="section steps-section" id="'+anchor+'"><div class="wrap"><div class="section-heading"><p class="eyebrow">'+F['eye']+'</p><h2>'+F['h']+'</h2></div><div class="feature-grid">'+cards+'</div><a class="text-link steps-help" href="'+F['more'][0]+'">'+F['more'][1]+' →</a></div></section>'
def home_cta(lang='de'):
    if lang=='de':
        eye='OnPath ausprobieren';title='Bereit für deine nächste Tour?'
        text='Plane eine kleine Wanderung oder Radtour und lerne OnPath unterwegs kennen. Deine Rückmeldung hilft mir, die App weiterzuentwickeln.'
        action=('/ausprobieren/','Einladung zum Test anfragen');help=('/hilfe/','Hilfe für die erste Tour')
        fine='Frühe Testversion · Android ab Version 8 · Persönliche Einladung'
    else:
        eye='Try OnPath';title='Ready for your next outing?'
        text='Plan a short walk or ride and get to know OnPath along the way. Your feedback helps me improve the app.'
        action=('/try/','Ask for a test invitation');help=('/help/','Help for your first outing')
        fine='Early test version · Android 8 or newer · Personal invitation'
    return '<section class="section soft"><div class="wrap cta"><p class="eyebrow">'+eye+'</p><h2>'+title+'</h2><p>'+text+'</p><div class="actions">'+button(action[0],action[1])+'</div><span class="fine">'+fine+'</span><a class="text-link" href="'+help[0]+'">'+help[1]+' →</a></div></section>'
DETAIL_HIGHLIGHTS={'de': {'summary': 'Mehr durchdachte Details',
        'items': [('file',
                   'Deine Tour bleibt erhalten.',
                   'Automatisch gesichert: Auch nach einer Unterbrechung oder leerem Akku kannst du deine Tour fortsetzen. <a href="/hilfe/probleme/#tour-fortsetzen">Tour fortsetzen →</a>'),
                  ('pin',
                   'Zum Treffpunkt auf passenden Wegen.',
                   'Teile einen Ort aus Google Maps oder den Standort von Freunden mit OnPath. Die App führt dich hin. <a href="/hilfe/orte/#geteilte-treffpunkte">Geteilte Orte →</a>')]},
 'en': {'summary': 'More thoughtful details',
        'items': [('file',
                   'Your outing is kept.',
                   'Saved automatically: continue your outing even after an interruption or an empty battery. <a href="/help/troubleshooting/#resume">Resume your outing →</a>'),
                  ('pin',
                   'Reach your meeting point on suitable paths.',
                   'Share a place from Google Maps or a friend’s location with OnPath. The app guides you there. <a href="/help/places/#shared-meeting-points">Shared places →</a>')]}}
EXTRA_SHOT={'de':{'ankunft':('Navigation beim Wandern: 110 m Links, 1:40 h und 3,2 km bis zur Leiteralm, Ankunft 13:55','Abzweigung und Ankunft auf einen Blick.'),'ruheanzeige':('Ruheanzeige am Rad: schwarzer Bildschirm mit Pfeil, 2,3 km Links, 25 min und Ankunft 12:55','Am Lenker nur Pfeil, Entfernung und Ankunft. Die Karte kommt kurz vor der Abzweigung.'),'fahrt':('Tour beenden: OnPath hat eine Liftfahrt erkannt und fragt, was zählen soll','Mit dem Sessellift nach Vellau: OnPath erkennt die Fahrt und fragt, was zählen soll.')},
'en':{'ankunft':('Navigating on a hike: 60 m sharp right, 1:35 h and 3.1 km to the Leiteralm, arrival 13:50','Your next turn and arrival at a glance.'),'ruheanzeige':('Rest view on the bike: black screen with arrow, 600 m slight right, 35 min and arrival 11:05','On the handlebar only arrow, distance and arrival. The map returns shortly before the turn.'),'fahrt':('Ending a tour: OnPath recognised a chairlift ride and asks what should count','By chairlift to Vellau: OnPath recognises the ride and asks what should count.')}}
def screenshot_button(src,alt,lang,css='preview-enlarge',dynamic=False):
    label='Screenshot vergrößern' if lang=='de' else 'Enlarge screenshot'
    return '<button type="button" class="'+css+'" data-lightbox aria-haspopup="dialog" aria-label="'+label+'"><img '+('data-preview-img ' if dynamic else '')+'src="'+src+'" alt="'+html.escape(alt,quote=True)+'" loading="lazy"><span class="zoom-mark" aria-hidden="true">'+icon('search')+'</span></button>'
def more_section(lang='de'):
    de=lang=='de'
    screens={k:(alt,txt) for k,_,alt,txt in SHOTS[lang]['items']}
    def app(ic,title,text,key,help_link=''):
        alt,caption=screens.get(key,EXTRA_SHOT[lang].get(key,(title,title)))
        return (ic,title,text,'/assets/app/'+key+'-'+lang+'.webp',alt,caption,help_link)
    def help_item(item,key):
        ic,title,text=item
        caption=HELP_IMAGES[key][2 if de else 3]
        return (ic,title,text,'/assets/help/'+shot_files(key)[0 if de else 1],caption,caption,'')
    routes=FEATURES[lang]['rows'][0]
    inn=FEATURES[lang]['rows'][1]
    sac,colours,offline=SMALL[lang]['cols'][1][1]
    finish=SMALL[lang]['cols'][0][1][0]
    recovery,shared=DETAIL_HIGHLIGHTS[lang]['items']
    change=FIRST_STEPS[lang]['items'][2]
    sac_help='<a class="context-help" '+sac[1].partition(' <a ')[2]
    map_help='<a class="context-help" '+colours[1].partition(' <a ')[2]
    route_title='Routing passend zu deiner Aktivität.' if de else 'Routing to suit your activity.'
    route_text=('<span class="feature-detail">Sorgfältig abgestimmt: OnPath bevorzugt ausgewiesene Rad- und Wanderwege und meidet beim Radfahren stark befahrene Straßen.</span><span class="feature-detail"><strong>Beim Wandern:</strong> Wähle deine Schwierigkeit nach der SAC-Wanderskala des Schweizer Alpen-Clubs. OnPath berücksichtigt sie und zeigt anspruchsvollere Abschnitte an.</span>' if de else '<span class="feature-detail">Carefully tuned: OnPath favours designated cycling and hiking paths and avoids busy roads when cycling.</span><span class="feature-detail"><strong>When hiking:</strong> Choose your difficulty using the Swiss Alpine Club’s SAC hiking scale. OnPath takes it into account and highlights more demanding sections.</span>')
    discover_title='Tourenplanung: schöne Strecken und Einkehr.' if de else 'Route planning: scenic paths and inviting stops.'
    discover_text=('<span class="feature-detail"><strong>Für die Strecke:</strong> Erkennbare Wegarten und hervorgehobene Rad- und Wanderrouten helfen dir bei der Auswahl – von der kleinen Runde bis zum Fernweg.</span><span class="feature-detail"><strong>Für die Pause:</strong> Sieh dir Fotos, Bewertungen und Öffnungszeiten in Google Maps an, direkt aus OnPath. Deine Einkehr planst du als Stopp ein.</span>' if de else '<span class="feature-detail"><strong>For your route:</strong> Clear path types and highlighted cycling and hiking routes help you choose – from a local loop to a long-distance trail.</span><span class="feature-detail"><strong>For your break:</strong> Check photos, reviews and opening hours in Google Maps, straight from OnPath. Add your chosen place as a stop.</span>')
    groups=[
      ('Schöne Wege finden' if de else 'Find beautiful paths',[
        app('route',route_title,route_text,routes[3],'<div class="feature-help-links">'+home_help(lang,'features',0)+sac_help+'</div>'),
        app('pin',discover_title,discover_text,inn[3],'<div class="feature-help-links">'+map_help+home_help(lang,'features',1)+'</div>')]),
      ('Entspannt unterwegs' if de else 'Enjoy the journey',[
        app(*EXTRA[lang][1],'ankunft',home_help(lang,'extras',1)),
        app(*EXTRA[lang][0],'ankunft',home_help(lang,'extras',0)),
        help_item(recovery,'neustart'),
        help_item(('check',*finish),'beenden')]),
      ('Flexibel bleiben' if de else 'Stay flexible',[
        help_item(('route',change[1],change[2]+(' <a href="/hilfe/unterwegs-aendern/#aendern">Unterwegs umplanen →</a>' if de else ' <a href="/help/change-route/#edit">Change your route →</a>')),'neue-route'),
        help_item(shared,'g-uebernommen'),
        help_item(('search',*offline),'suche'),
        app(*EXTRA[lang][2],'fahrt',home_help(lang,'extras',2))])]
    sections=[]
    for gi,(title,entries) in enumerate(groups):
        preview_index=0
        first=entries[preview_index]
        visual='<figure class="group-preview">'+screenshot_button(first[3],first[4],lang,dynamic=True)+'<figcaption data-preview-text aria-live="polite">'+first[5]+'</figcaption></figure>'
        rows=[]
        for i,(ic,t,text,src,alt,caption,help_link) in enumerate(entries):
            text,sep,embedded=text.partition(' <a ')
            if sep: help_link='<a class="context-help" '+embedded
            selected='true' if i==preview_index else 'false'
            subview=''
            if gi==1 and i==0:
                dark_src='/assets/app/ruheanzeige-'+lang+'.webp'
                dark_alt,dark_caption=EXTRA_SHOT[lang]['ruheanzeige']
                dark_label='Fürs Rad: dunkle Lenkeransicht' if de else 'For cycling: a dark handlebar view'
                subview='<div class="feature-subview"><button type="button" class="feature-suboption" data-shot="'+dark_src+'" data-alt="'+html.escape(dark_alt,quote=True)+'" data-text="'+html.escape(dark_caption,quote=True)+'" aria-pressed="false">'+dark_label+'</button><figure class="inline-shot">'+screenshot_button(dark_src,dark_alt,lang,'inline-preview')+'</figure></div>'
            rows.append('<article class="feature-entry'+(' feature-primary' if i==0 else '')+'"><button class="feature-row" data-shot="'+src+'" data-alt="'+html.escape(alt,quote=True)+'" data-text="'+html.escape(caption,quote=True)+'" aria-pressed="'+selected+'">'+icon(ic)+'<span><b>'+t+'</b>'+text+'</span></button><figure class="inline-shot">'+screenshot_button(src,alt,lang,'inline-preview')+'</figure>'+help_link+subview+'</article>')
        hint='<p class="benefits-hint">'+('Wähle einen Vorteil, um das passende Bild zu sehen.' if de else 'Choose a benefit to see its screen.')+'</p>' if gi==0 else ''
        links=''.join('<a class="text-link" href="'+u+'">'+label+' →</a>' for u,label in MORE[lang]['links']) if gi==0 else ''
        sections.append('<section class="benefit-band'+(' soft' if gi%2==0 else '')+'"><div class="wrap benefit-group'+(' feature-pair' if gi==0 else '')+'" aria-labelledby="benefit-group-'+str(gi)+'"><h2 id="benefit-group-'+str(gi)+'">'+title+'</h2>'+visual+'<div class="feature-rows">'+''.join(rows)+'</div>'+('<div class="benefit-footer">'+hint+links+'</div>' if hint or links else '')+'</div></section>')
    return '<div class="benefits-section" id="'+('so-gehts' if de else 'how')+'">'+''.join(sections)+ways_section(lang)+'</div>'

def home_hero(lang='de'):
    if lang == 'de':
        eye='Für Wandern und Radfahren'; title='Deine Tour.<br><span>Einfach unterwegs.</span>'
        lead='Plane schnell deinen Weg, lass dich führen und bleib unterwegs spontan – auch ohne Empfang.'
        together='Am Computer planen. Mit dem Handy losziehen.'
        app=('/ausprobieren/','Android-App testen'); browser='Im Browser planen'
        value='Planen, navigieren und aufzeichnen bleiben kostenlos.'
        note='Ohne Konto · Ohne Werbung<br>Android · Frühe Testversion mit persönlicher Einladung'
        photo='Ein Weg unter gelbem Herbstlaub bei Vellau'; web='OnPath im Browser: eine Wanderung von Vellau zur Leiteralm'
        phone='Dieselbe Wanderung in der Android-App'; caption='Am Computer planen. Auf dem Handy dabei.'
    else:
        eye='For hiking and cycling'; title='Your route.<br><span>Simply on your way.</span>'
        lead='Plan your way quickly, follow directions and stay spontaneous along the way – even without reception.'
        together='Plan on your computer. Head out with your phone.'
        app=('/try/','Test the Android app'); browser='Plan in your browser'
        value='Planning, navigation and recording stay free.'
        note='No account · No ads<br>Android · Early test version by personal invitation'
        photo='A path under yellow autumn leaves near Vellau'; web='OnPath in the browser: a hike from Vellau to the Leiteralm (German screen)'
        phone='The same hike in the Android app'; caption='Plan on your computer. Take it along on your phone.'
    visual='<figure class="hero-product with-landscape"><img class="product-landscape" src="/assets/vellau-path.webp" alt="'+photo+'" width="1400" height="1054" fetchpriority="high"><img class="product-phone" src="/assets/app/plan-wandern-'+lang+'.webp" alt="'+phone+'" width="600" height="1333" fetchpriority="high"><figcaption>Vellau '+('bei Algund, Südtirol' if lang=='de' else 'near Algund, South Tyrol')+'</figcaption></figure>'
    return '<section class="hero soft"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow">'+eye+'</p><h1>'+title+'</h1><p class="lead">'+lead+'</p><p class="hero-together">'+together+'</p><div class="actions">'+button(*app)+button('https://plan.onpath.earth/',browser,True)+'</div><p class="hero-value">'+value+'</p><p class="hero-note">'+note+'</p></div>'+visual+'</div></section>'

body=home_hero('de')+first_steps('de')+more_section('de')+open_section('de')+home_cta('de')
page('/','Deine Tour. Einfach unterwegs.','OnPath für Android: Wander- und Radtouren planen, unterwegs ändern und offline navigieren. Ohne Konto und Werbung.',body)

HELP = [('erste-schritte',
  'Deine erste Tour',
  'Installieren, Gebiet laden und eine kleine Runde planen.',
  'Start Installation Android Berechtigung Standort',
  [('OnPath installieren',
    '<p>OnPath läuft auf Android ab Version 8. Eine iPhone-Version gibt es derzeit nicht.</p><p>Aktuell läuft Phase 1: '
    'Du brauchst eine persönliche Einladung und Freischaltung durch Christian. Deinen individuellen Link und die '
    'Installationshinweise bekommst du direkt von ihm. Die geschlossene Testgruppe über Google Play ist der nächste '
    'Schritt. Wie das geht, steht unter <a href="/ausprobieren/">OnPath ausprobieren</a>.</p><p>Für technisch '
    'Erfahrene gibt es frühe Fassungen auch als APK-Datei auf <a '
    'href="https://github.com/happychriss/OnPath/releases">GitHub</a>. Sie sind anders signiert als die Play-Fassung; '
    'sichere deine Touren, bevor du zwischen beiden wechselst.</p>'),
   ('Zu Hause vorbereiten',
    '<ol><li>Öffne OnPath mit Internetverbindung, möglichst im WLAN.</li><li>Erlaube den Standortzugriff für '
    'Navigation und Aufzeichnung.</li><li>Plane deine Strecke. OnPath lädt die nötigen Karten und die Orts- und '
    'Adressdatenbank automatisch herunter.</li><li>Lass den Download vollständig abschließen. Prüfe unter '
    'Einstellungen → Offline-Karten, ob die Gebiete bereit sind.</li></ol><p>Beim ersten Laden kann ein neues Gebiet '
    'einige Minuten brauchen. <a href="/hilfe/offline/#vorbereiten">Die Offline-Vorbereitung im Detail →</a></p>'),
   ('Die erste Runde planen',
    '<p>Wähle deine Aktivität. Drücke etwas länger auf dein Ziel auf der Karte und wähle „Hierhin“. OnPath plant von '
    'deinem Standort aus. Das längere Drücken verhindert versehentliche Änderungen durch kurzes '
    'Antippen.</p><p>Möchtest du woanders starten, halte zuerst den Startpunkt gedrückt und wähle „Hier starten“. '
    'Ergänze dann Ziel und Zwischenstopps. Prüfe Länge, Höhenmeter und Streckenhinweise; beginne mit einer kurzen, '
    'bekannten Strecke.</p>'),
   ('Navigation starten',
    '<p>Tippe auf „Navigation starten“. Der Plan bleibt geschützt: Ein kurzer Tipp auf die Karte verändert die Route '
    'nicht. Möchtest du unterwegs etwas ändern, wechselst du bewusst in die Planung.</p>')]),
 ('offline',
  'Ohne Netz unterwegs',
  'Karten vorbereiten und auch im Funkloch umplanen.',
  'Karten Internet WLAN Funkloch Download Flugmodus',
  [('Was offline funktioniert',
    '<p>OnPath lädt beim Planen automatisch Karten für deine Strecke und deren Umgebung herunter – einschließlich '
    'Orts- und Adressdatenbank. In vollständig geladenen Gebieten kannst du Adressen und Orte suchen, Routen planen, '
    'navigieren und unterwegs neu berechnen. Die Suche und Routenberechnung laufen direkt auf deinem '
    'Handy.</p><p>Zusätzliche Online-Suchergebnisse ergänzen die lokale Suche, sie sind keine Voraussetzung dafür. Ein '
    'Link zu Google Maps öffnet einen separaten Dienst; dessen Offline-Funktionen und gespeicherte Gebiete sind '
    'unabhängig von OnPath.</p>'),
   ('Vor der Tour laden',
    '<ol><li>Plane deine Strecke mit Internet, am besten zu Hause im WLAN.</li><li>Lass den automatischen Download '
    'vollständig abschließen. Berücksichtige auch größere Abstecher und den Rückweg.</li><li>Prüfe unter Einstellungen '
    '→ Offline-Karten den Download-Stand.</li><li>Schalte zum Ausprobieren WLAN und mobile Daten aus, lass den '
    'Standort eingeschaltet und teste Suche sowie eine kleine Routenänderung.</li></ol><p>Bereits geladene Gebiete '
    'bleiben auf dem Handy. Führt ein Abstecher darüber hinaus, brauchst du zum Nachladen wieder Internet. Auch der '
    'erste Download muss abgeschlossen sein, bevor du ohne Netz startest.</p>'),
   ('Wenn ein Gebiet fehlt',
    '<p>Ein neues Gebiet benötigt Internet. Beim ersten Abruf kann die Bereitstellung einige Minuten dauern. Starte '
    'die Vorbereitung deshalb zu Hause. Sind nur Teile geladen, ist noch nicht alles offline verfügbar.</p>'),
   ('Was Internet braucht',
    '<p>Neue Karten, App-Updates und zusätzliche Online-Suchergebnisse benötigen eine Verbindung. Wenn du einen Ort in '
    'Google Maps öffnest, gelten außerdem dessen Offline-Möglichkeiten und Datenverbindungen.</p>')]),
 ('route-planen',
  'Eine eigene Route planen',
  'Punkte setzen, Schwierigkeit wählen und die Strecke prüfen.',
  'Punkte Route Wandern Rad T1 T2 T3 Höhenprofil Planung',
  [('Aktivität auswählen',
    '<p>Wähle Fahrrad, Gravelbike, E-Bike, MTB, E-MTB oder Wandern. OnPath stimmt die Wegwahl auf die Aktivität ab. '
    'Beim Radfahren berücksichtigt es unter anderem Untergrund und stark befahrene Straßen; ein Tourenrad wird anders '
    'geplant als ein Gravelbike oder MTB.</p><p>Für Wanderungen wählst du außerdem die Schwierigkeit nach der '
    'SAC-Wanderskala. <a href="#schwierigkeit">Die Stufen erklärt →</a></p>'),
   ('Punkte setzen und ändern',
    '<p>Drücke etwas länger auf eine freie Stelle der Karte und wähle die gewünschte Aktion, zum Beispiel „Hierhin“ '
    'für eine Route von deinem Standort. Ein kurzer Tipp setzt kein neues Ziel – so ändert sich der Plan nicht '
    'versehentlich.</p><p>Halte einen bestehenden Punkt gedrückt, um seine Möglichkeiten zu öffnen. Zum Versetzen auf '
    'der Karte löschst du ihn und setzt ihn neu. In der aufgeklappten Punkteliste kannst du Stopps am Griff '
    'umsortieren und entfernen. Änderungen lassen sich rückgängig machen; außerdem kannst du die Route umkehren oder '
    'zur Rundtour ergänzen.</p>'),
   ('Die Strecke ansehen',
    '<p>Ziehe das Routenfenster nach oben, um Höhenprofil, Wegarten und Untergrund anzusehen. Die Hinweiszeile macht '
    'dich je nach Aktivität auf steile Abschnitte, Schiebestrecken, Treppen, anspruchsvollere Wanderabschnitte, '
    'Fähren, Baustellen, Wasserquerungen und bestimmte Hindernisse für Räder aufmerksam. Tippe auf einen Hinweis, um '
    'die betroffenen Stellen auf der Karte anzusehen.</p><p>Bei Fähren prüfst du die Betriebszeiten selbst; bei '
    'Baustellen kann der Weg gesperrt sein. Die Hinweise hängen von den vorhandenen Karteneinträgen ab und sind keine '
    'vollständige Liste aktueller Gefahren.</p><p>Erreicht die Route einen gesetzten Punkt nicht, zeigt OnPath die '
    'Lücke. Eine gestrichelte Verbindung bestätigt keinen begeh- oder befahrbaren Weg. Prüfe den Punkt und wähle bei '
    'Bedarf einen anderen Zugang.</p>'),
   ('Die Schwierigkeit wählen: SAC T1 bis T5',
    '<p>OnPath verwendet die SAC-Wanderskala des Schweizer Alpen-Clubs. Du kannst T1 bis T5 wählen: T1 steht für '
    'Wandern, T2 für Bergwandern, T3 für anspruchsvolles Bergwandern, T4 für Alpinwandern und T5 für anspruchsvolles '
    'Alpinwandern. Mit den Stufen steigen die Anforderungen an Trittsicherheit, Schwindelfreiheit, Orientierung und '
    'alpine Erfahrung.</p><p>Die Planung vermeidet Wege oberhalb deiner gewählten Stufe und Klettersteige. Enthält '
    'eine Strecke dennoch einen als schwieriger erfassten Abschnitt, zeigt OnPath einen Hinweis. Die Einstufungen '
    'beruhen auf OpenStreetMap und können fehlen oder veraltet sein. Wetter, Wegzustand und deine Erfahrung bleiben '
    'entscheidend; Hinweise und Sperrungen vor Ort haben Vorrang.</p>'),
   ('Kartenfarben und ausgeschilderte Routen',
    '<p>Die Darstellung passt sich deiner Aktivität an. Grün hervorgehobene Wege helfen dir, passende Verbindungen zu '
    'erkennen. Ausgeschilderte Rad- und Wanderrouten werden zusätzlich als Routen mit Namen dargestellt. Fernwege sind '
    'mit einer rosa-grünen Markierung hervorgehoben; dazu gehören nationale und internationale Routen wie '
    'EuroVelo.</p><p>In der Übersicht siehst du vor allem Fernwege. Beim Heranzoomen kommen regionale und lokale '
    'Routen hinzu. So kannst du entweder einem längeren Routenverlauf folgen oder kleine Wege in deiner Umgebung zu '
    'einer Tour verbinden.</p><p>Beim Radfahren weist die Darstellung auch auf den Untergrund hin. Die Farben '
    'unterstützen die Planung, ersetzen aber nicht die Prüfung von Strecke, Schwierigkeit und Beschilderung.</p>'),
   ('Am Computer planen und aufs Handy übertragen',
    '<ol><li>Öffne <a href="https://plan.onpath.earth/">plan.onpath.earth</a> am Computer. Du brauchst kein Konto und '
    'keine Installation.</li><li>Setze Start, Ziel und Zwischenstopps. Punkte lassen sich mit der Maus setzen und '
    'verschieben; vorhandene GPX-Dateien kannst du öffnen.</li><li>Öffne „Teilen“ und scanne den QR-Code mit der '
    'Handykamera. Öffne den Link in OnPath auf deinem Android-Handy.</li><li>Prüfe die Tour und lass die benötigten '
    'Karten auf dem Handy vollständig laden, bevor du ohne Empfang startest.</li></ol><p>Das dauerhafte Koppeln von '
    'Browser und Handy zum Abgleich gespeicherter Pläne ist im Test. Die einmalige QR-Übertragung kannst du bereits '
    'nutzen. <a href="/ausblick/#abschnitt-3">Mehr zum Koppeln →</a></p>')]),
 ('unterwegs-aendern',
  'Unterwegs die Route ändern',
  'Einen Abstecher einbauen und die Aufzeichnung fortsetzen.',
  'Navigation Abstecher umplanen Slider neu berechnen Vibration',
  [('Bewusst zur Planung wechseln',
    '<p>Schiebe unten „Stopp“ zur Seite. Damit öffnest du die Auswahl zum Pausieren, Beenden oder Ändern der Route. '
    'Der Wisch allein beendet die Aufzeichnung nicht. Beim Umplanen läuft sie weiter.</p>'),
   ('Den weiteren Weg anpassen',
    '<p>Entferne einen nicht mehr benötigten Stopp oder ergänze ein neues Ziel. Kontrolliere anschließend die Strecke. '
    'Solange die benötigten Daten auf dem Handy liegen, klappt die Neuberechnung auch ohne Internet. <a href="/hilfe/offline/#vorbereiten">Automatische Downloads und Offline-Vorbereitung →</a></p>'),
   ('Weitergehen oder weiterfahren',
    '<p>Tippe auf „Weiter“, dann bist du wieder in der Navigation. OnPath führt dich von deinem Standort aus weiter '
    'und überspringt bereits besuchte Zwischenpunkte. Deine Aufzeichnung läuft weiter.</p>'),
   ('Du bist von der Route abgewichen',
    '<p>OnPath meldet sich per Vibration und fragt nach, ob du eine neue Route möchtest. Es ändert den Weg nicht '
    'stillschweigend. Nach der Neuberechnung bleibt die ursprüngliche Route grau sichtbar.</p>')]),
 ('orte',
  'Orte suchen & Google Maps nutzen',
  'Ein Café finden, einen Ort teilen oder Öffnungszeiten nachsehen.',
  'Google Suche Adresse Hütte Gipfel teilen Öffnungszeiten Photon',
  [('In OnPath suchen',
    '<p>Gib einen Ortsnamen oder eine Adresse ein. OnPath durchsucht die eigene Orts- und Adressdatenbank auf deinem '
    'Handy. Sie wird automatisch mit den Karten geladen und enthält unter anderem Straßen mit Hausnummern, Dörfer, '
    'Hütten, Gipfel und Bahnhöfe.</p><p>Diese Suche funktioniert in vollständig geladenen Gebieten ohne Netz. Mit '
    'Internet kommen zusätzliche Online-Ergebnisse hinzu. Außerhalb der geladenen Gebiete brauchst du Internet zum '
    'Nachladen; nicht jeder Ort oder jede Hausnummer ist erfasst.</p>'),
   ('Einen Ort aus Google Maps übernehmen',
    '<ol><li>Öffne den gewünschten Ort in Google Maps.</li><li>Tippe auf „Teilen“ und wähle OnPath.</li><li>Prüfe den '
    'markierten Ort auf der Karte.</li><li>Übernimm ihn als Start, Zwischenstopp oder Ziel.</li></ol><p>Übernommen '
    'werden der Ort und sein Name – keine vollständige Google-Route, Bewertungen oder Fotos. Bei einem verkürzten Link '
    'kann eine Internetverbindung zum Auflösen nötig sein.</p>'),
   ('Öffnungszeiten oder Bilder ansehen',
    '<p>Öffne in OnPath den gewünschten Ort und seine Details. Von dort kannst du zu Google Maps wechseln, um '
    'Öffnungszeiten, Bilder oder Bewertungen anzusehen. Kehre danach zu OnPath zurück und ergänze den Ort als '
    'Zwischenstopp oder Ziel. Den Weg dorthin berechnet OnPath für deine gewählte Aktivität.</p>'),
   ('Welche Daten dabei übertragen werden',
    '<p>Für Online-Suchergebnisse wird eine ungefähre Position von etwa einem Kilometer Genauigkeit übermittelt. Bei '
    'Google Maps gelten die Bedingungen und Datenschutzhinweise von Google. <a href="/datenschutz/">Mehr zum '
    'Datenschutz</a>.</p>'),
   ('Einen Treffpunkt aus einer Nachricht übernehmen',
    '<p>Hat dir jemand einen Kartenlink oder Standort geschickt, etwa in Signal? Teile den Link oder die Nachricht '
    'über die Android-Teilen-Funktion mit OnPath. Unterstützt werden unter anderem Google-Maps- und '
    'OpenStreetMap-Links, geo:-Links und Koordinaten.</p><ol><li>Wähle beim Teilen OnPath.</li><li>Prüfe den '
    'markierten Ort auf der Karte.</li><li>Wähle ihn als Ziel oder Zwischenstopp und starte die Navigation, wenn du '
    'losgehen möchtest.</li></ol><p>OnPath liest keine Chats und verfolgt keinen Live-Standort. Es übernimmt den '
    'geteilten Punkt; das genaue Vorgehen hängt von der Nachrichten-App und dem Linkformat ab. Kurze Google-Maps-Links '
    'können Internet benötigen. Ist nur eine Adresse bekannt, prüfe die gefundene Position besonders sorgfältig. Nicht '
    'jedes Nachrichtenformat lässt sich direkt übernehmen.</p>')]),
 ('gpx',
  'Touren als Datei öffnen und sichern',
  'Vorhandene Touren mitnehmen und deine eigenen behalten.',
  'GPX Import Export Verein speichern Sicherung Backup Datei',
  [('Was ist eine GPX-Datei?',
    '<p>Eine GPX-Datei enthält den Verlauf einer Strecke. Viele Tourismusregionen, Wanderseiten und Radvereine stellen '
    'Touren in diesem Format bereit. So kannst du eine Tour mit verschiedenen Apps nutzen.</p>'),
   ('Eine Strecke öffnen',
    '<p>Lade die GPX-Datei auf dein Handy. Öffne sie mit OnPath, zum Beispiel über die Dateiverwaltung von Android. '
    'Prüfe, ob Strecke und Aktivität passen. Lade vor dem Start die benötigten Karten vollständig.</p>'),
   ('Was du damit machen kannst',
    '<p>Du kannst importierten GPX-Strecken folgen. Sie lassen sich derzeit noch nicht in einen frei bearbeitbaren '
    'OnPath-Plan umwandeln. Wenn du selbst flexibel planen möchtest, lege die Route mit eigenen Punkten an.</p>'),
   ('Eigene Touren sichern',
    '<p>Deine Touren liegen in der App. Zusätzlich legt OnPath gespeicherte Routen und abgeschlossene Touren als '
    'GPX-Dateien in einem zugänglichen Ordner ab – standardmäßig Documents/OnPath. Unter Einstellungen → Sicherung '
    'kannst du einen anderen Ordner wählen. Auf Android 8 und 9 ist für den Standardordner die Speicherfreigabe nötig; '
    'nach einer Neuinstallation muss der Zugriff auf einen gewählten Ordner erneut erlaubt werden.</p><p>GPX ist ein '
    'offenes Dateiformat. Über die Android-Dateiverwaltung kannst du die Dateien auf deinen Computer kopieren, an '
    'Freunde weitergeben oder in anderen geeigneten Apps öffnen und bearbeiten. Änderungen außerhalb von OnPath werden '
    'nicht automatisch in die App zurückübernommen.</p><p>In „Meine Routen“ kannst du alle abgeschlossenen Touren '
    'zusammen als ZIP-Datei exportieren. Der Android-Teilen-Dialog bietet dir die verfügbaren Ziele zum Speichern oder '
    'Weitergeben an. Eine laufende Aufzeichnung ist darin nicht enthalten.</p><p>Eine zusätzliche Datei auf demselben '
    'Handy schützt nicht vor Geräteverlust. Kopiere wichtige Touren auch auf einen anderen Speicher. Wird die '
    'automatische Sicherung nicht geschrieben, zeigt OnPath einen Hinweis an.</p>')]),
 ('probleme',
  'Wenn etwas nicht klappt',
  'Fehlende Karten, Standortprobleme und Rückmeldungen.',
  'Fehler Probleme GPS Diagnose Akku Download Support',
  [('Die Karte lädt nicht',
    '<p>Prüfe deine Internetverbindung und den Download-Stand bei den Offline-Karten. Ein erstmals angefordertes '
    'Gebiet braucht länger. Im Funkloch kann OnPath ein fehlendes Gebiet nicht nachladen.</p>'),
   ('Mein Standort fehlt',
    '<p>Prüfe, ob die Standortfunktion von Android eingeschaltet ist und OnPath die nötige Berechtigung hat. Unter '
    'freiem Himmel lässt sich ein Standort meist leichter bestimmen als in Gebäuden. Warte auf eine brauchbare '
    'Position, bevor du die Navigation beurteilst.</p>'),
   ('Die Tour wurde unterbrochen',
    '<p>OnPath speichert aufgezeichnete Punkte fortlaufend und hält den Navigationsstand auf dem Handy fest. Wird die '
    'App beendet, das Handy neu gestartet oder die Aufzeichnung unterbrochen, öffne OnPath erneut. Im Dialog zur '
    'unterbrochenen Tour wählst du „Fortsetzen“, um weiterzumachen, oder „Speichern“, um den bisherigen Verlauf zu '
    'behalten. „Löschen“ verwirft die Aufzeichnung bewusst.</p><p>Die Zeit, in der das Handy aus war, wird nicht '
    'nachträglich aufgezeichnet. Wiederholte Unterbrechungen können durch Androids Akku-Beschränkungen entstehen. <a '
    'href="/hilfe/akku-sicherung/#hintergrund">Hintergrundeinstellungen prüfen →</a></p>'),
   ('Einen Fehler melden',
    '<p>Notiere dein Handy-Modell, die OnPath-Version, die Situation und was du erwartet hast. Unter Einstellungen → '
    'Diagnose → „Send problem report“ (der Knopf ist englisch) kannst du zusätzliche Informationen als Datei erzeugen. '
    'Prüfe sie vor dem Weitergeben, besonders auf Orts- und Tourdaten.</p><p><a '
    'href="https://github.com/happychriss/OnPath/issues">Auf GitHub einen Fehler melden ↗</a>. Ein GitHub-Konto ist '
    'dafür nötig. Öffentlich eingestellte Meldungen und Anhänge können andere lesen; verschicke keine privaten Daten '
    'unbedacht. OnPath sendet den Export nicht automatisch.</p>')]),
 ('navigation',
  'Unterwegs den Weg finden',
  'Abzweigungen, Ankunftszeit und das Ende deiner Tour.',
  'Navigation Vibration links rechts Zeit Sperrbildschirm Aufzeichnung',
  [('Abzweigungen erkennen',
    '<p>OnPath zeigt die nächste Abzweigung und gibt an entscheidenden Stellen Hinweise. Die Sprachansagen nennen '
    'Richtung und Wegtyp und können auf den weiteren Verlauf hinweisen. Die Stimme kommt von deinem Handy und '
    'funktioniert mit einer installierten Offline-Stimme ohne Netz.</p><p>Unter Einstellungen → Navigation wählst du '
    'Sprache, Vibrationen oder beides. Die Einstellungen lassen sich getrennt anpassen; teste die Sprache zunächst '
    'hörbar in der Einrichtung. Bei Vibrationen steht ein Impuls für links, zwei für rechts. Wie gut du sie spürst, '
    'hängt vom Handy und davon ab, wo du es trägst. Probiere beides auf einer bekannten Strecke aus.</p>'),
   ('Ein Blick auf den Sperrbildschirm',
    '<p>Die OnPath-Benachrichtigung zeigt die nächste Abzweigung und die geschätzte Ankunftszeit. Am Fahrrad zeigt die '
    'Ruheanzeige vor allem Richtung, Entfernung und Ankunft; vor der Abzweigung erscheint wieder die Karte. Die '
    'Sprachansagen stellst du unter Einstellungen → Navigation ein.</p>'),
   ('Die Zeit passt sich deinem Tempo an',
    '<p>Zu Beginn nutzt OnPath deine Fitness-Einstellung. Nach ungefähr 15 Minuten und einem Kilometer berücksichtigt '
    'die App dein tatsächliches Tempo – getrennt für bergauf, eben und bergab. Die Ankunftszeit bleibt eine '
    'Schätzung.</p>'),
   ('Die Tour beenden und behalten',
    '<p>Schiebe „Stopp“ zur Seite, wähle „Tour beenden“ und anschließend „Speichern“. Du kannst die Tour behalten, '
    'ohne danach Fotos hochzuladen, sie zu teilen oder zu bewerten. Ein bloßes Sperren des Bildschirms beendet die '
    'Aufzeichnung nicht.</p><p>Wurde eine Fahrt erkannt, etwa mit Bus oder Seilbahn, kannst du beim Abschluss '
    'entscheiden, wie sie in den Tourwerten berücksichtigt wird. <a href="#fahrten">Erkannte Fahrten prüfen →</a></p>'),
   ('Bus- und Seilbahnfahrten berücksichtigen',
    '<p>OnPath erkennt Abschnitte, die du voraussichtlich mit einem Fahrzeug oder Lift zurückgelegt hast. Beim Beenden '
    'prüfst du die erkannten Fahrten und entscheidest, ob sie in Strecke und Zeit mitzählen. Die Erkennung ist ein '
    'Vorschlag, den du selbst kontrollierst. Bei einer gespeicherten Tour kannst du die Fahrtanteile über das Tourmenü '
    'erneut bearbeiten.</p>')]),
 ('akku-sicherung',
  'Akku und Sicherung',
  'Damit die Aufzeichnung weiterläuft und deine Touren erhalten bleiben.',
  'Akku Hintergrund Batterie Sicherung Papierkorb ZIP Backup',
  [('Wenn die Aufzeichnung im Hintergrund stoppt',
    '<p>Prüfe in den Android-Einstellungen bei Apps → OnPath die Standortfreigabe, Benachrichtigungen und die '
    'Akku-Einstellung. Eine starke Akku-Beschränkung kann die App im Hintergrund beenden. Je nach Handyhersteller '
    'heißen diese Einstellungen etwas anders.</p><p>Falls nötig, erlaube OnPath die Nutzung ohne Akku-Einschränkung. '
    'Prüfe anschließend auf einer kurzen Strecke, ob bei gesperrtem Bildschirm weiter aufgezeichnet wird.</p>'),
   ('Vor einer längeren Wanderung',
    '<p>Lade das Handy vorher und nimm bei Bedarf eine Powerbank mit. Der Akkuverbrauch ist noch nicht auf vielen '
    'Geräten gemessen. Display, Gerät und Empfang beeinflussen die Laufzeit.</p>'),
   ('Eine zweite Kopie deiner Touren',
    '<p>OnPath legt zusätzliche GPX-Dateien standardmäßig unter Documents/OnPath ab. Unter Einstellungen → Sicherung '
    'kannst du einen anderen Ordner auswählen. Kopiere wichtige Dateien regelmäßig auf den Computer oder einen anderen '
    'Speicher. Eine Kopie auf demselben Handy schützt nicht vor dessen Verlust. <a '
    'href="/hilfe/gpx/#eigene-dateien">Dateien finden und exportieren →</a></p>'),
   ('Alles sichern oder wiederherstellen',
    '<p>Über „Meine Routen“ lassen sich alle abgeschlossenen Touren gemeinsam als ZIP-Datei teilen oder sichern. '
    'Gelöschte Touren bleiben 30 Tage im Papierkorb. Nach einer Neuinstallation kannst du den vorhandenen '
    'Sicherungsordner zur Wiederherstellung auswählen und den Zugriff erneut erlauben.</p>')])]

def article(path,eye,title,desc,sections,help_page=False):
 side='<aside class="side-nav"><b>'+('Hilfe & erste Schritte' if help_page else 'Auf dieser Seite')+'</b>'
 if help_page:side+=''.join('<a '+('aria-current="page" ' if path=='/hilfe/'+s+'/' else '')+'href="/hilfe/'+s+'/">'+t+'</a>' for s,t,_,_,_ in HELP)
 else:side+=''.join('<a href="#abschnitt-'+str(i)+'">'+t+'</a>' for i,(t,_) in enumerate(sections))
 side+='</aside>'
 slug=path.strip('/').split('/')[-1] if help_page else None
 prose=''.join('<section id="abschnitt-'+str(i)+'"><h2'+(' id="'+help_anchor('de',slug,i)+'"' if help_page else '')+'>'+t+'</h2>'+v+(shots_html('de',slug,i) if help_page else '')+'</section>' for i,(t,v) in enumerate(sections))
 if help_page:
  prose='<nav class="help-contents" aria-label="In diesem Hilfethema"><b>In diesem Hilfethema</b><ul>'+''.join('<li><a href="#'+help_anchor('de',slug,i)+'">'+t+'</a></li>' for i,(t,_) in enumerate(sections))+'</ul></nav>'+prose
 content=ph(eye,title,desc,('<a href="/hilfe/">Hilfe</a> <span>/</span> ' if help_page else '')+title)+'<section class="section"><div class="wrap article-layout">'+side+'<article class="prose">'+prose+'<div class="article-end"><a href="/hilfe/">← Alle Hilfethemen</a><a href="/ausprobieren/">OnPath ausprobieren →</a></div></article></div></section>'
 page(path,title,desc,content,'/hilfe/' if help_page else path)
for slug,title,desc,keys,sections in HELP:article('/hilfe/'+slug+'/','Hilfe & erste Schritte',title,desc,sections,True)
helpbody=ph('OnPath verstehen','Wie können wir dir helfen?','Kurze Anleitungen für deine erste Tour – und für die kleinen Fragen unterwegs.','Hilfe')+'<section class="section help-section"><div class="wrap"><div class="help-search"><label for="help-search">Hilfethema suchen</label><div>'+icon('search')+'<input type="search" id="help-search" placeholder="Zum Beispiel: Karten, GPX oder Google Maps" autocomplete="off"></div></div><p id="search-count" class="fine" role="status">9 Hilfethemen</p><div class="help-grid">'
for slug,title,desc,keys,_ in HELP:helpbody+='<a class="help-card" data-keywords="'+keys+'" href="/hilfe/'+slug+'/"><h2>'+title+'</h2><p>'+desc+'</p><span aria-hidden="true">→</span></a>'
helpbody+='</div><p id="no-results" hidden>Kein passendes Thema gefunden. Versuche es mit „Karten“, „Route“ oder „GPX“.</p></div></section>'
page('/hilfe/','Hilfe & erste Schritte','Einfach erklärte Hilfe zu OnPath: offline planen, Touren ändern, Orte suchen und GPX-Dateien nutzen.',helpbody,'/hilfe/')

article('/wandern/','Zu Fuß unterwegs','Zeit für deinen Weg.','Du musst nicht jeden Weg kennen, um eine eigene Wanderung zu planen. OnPath hilft dir, aus einem Ziel eine Strecke zu machen.',[
('Du wählst das Ziel. OnPath verbindet die Wege.','<p>Suche zuerst dein Ziel, etwa eine Hütte oder einen Ort. Ergänze bei Bedarf einen Zwischenstopp. OnPath verbindet die Punkte über Wege. Du siehst die Entfernung, die Steigungen und die ungefähre Dauer. Wähle die Schwierigkeit passend zu deiner Erfahrung. OnPath verwendet bei der Planung keine als schwieriger eingestuften Wege als eingestellt und keine Klettersteige.</p>'+notice('Mit Augenmaß planen','Die Einstufung hängt von den Kartendaten ab. Wetter, Wegzustand und deine Erfahrung bleiben entscheidend.')),
('Noch zur Hütte – oder früher zurück','<p>Ein guter Wandertag braucht keinen starren Plan. Baue einen Abstecher ein oder ändere das Ziel. Deine Aufzeichnung läuft weiter, während du den restlichen Weg anpasst. Mit vorbereiteten Karten geht das auch ohne Empfang.</p>'),
('Eine Zeitangabe, die sich anpasst','<p>Die erste Schätzung orientiert sich an deiner eingestellten Fitness. Nach etwa 15 Minuten und einem Kilometer berücksichtigt OnPath dein tatsächliches Tempo auf dieser Tour – getrennt nach bergauf, eben und bergab. Pausen werden dabei herausgerechnet.</p>'),
('Weniger aufs Display schauen','<p>Wo du falsch abbiegen könntest, vibriert das Handy: einmal für links, zweimal für rechts. Auf dem Sperrbildschirm findest du die nächste Abzweigung und die Ankunftszeit. Dazu kommen kurze Sprachansagen; du schaltest sie unter Einstellungen → Navigation ein oder aus.</p>'+button('/hilfe/erste-schritte/','Die erste Tour vorbereiten'))])
article('/radfahren/','Mit dem Rad unterwegs','Eine Runde, wie du sie magst.','Am Fluss entlang, durch die Stadt oder über Schotter: Wähle dein Rad und plane deinen Weg.',[
('Das passende Rad auswählen','<p>Fahrrad, Gravelbike, E-Bike, MTB und E-MTB stehen zur Auswahl. Die gewählte Aktivität beeinflusst, welche Wege OnPath bei der Planung bevorzugt. In den Routendetails siehst du Untergrund und Wegarten.</p>'),
('Vorher wissen, was auf der Strecke liegt','<p>Hinweise können dich auf Treppen, steile Abschnitte, Schiebestellen oder eine Fähre aufmerksam machen. Prüfe bei Fähren vorher die Betriebszeiten. Kartendaten beschreiben die Strecke, können aber keine tagesaktuellen Sperrungen garantieren.</p>'),
('Touren von Verein oder Tourenportal','<p>Du hast von deinem Radverein oder aus einem Tourenportal eine GPX-Datei bekommen? Öffne sie in OnPath und nimm die Strecke mit aufs Rad. Ein OnPath-Konto ist dafür nicht erforderlich.</p><p>Wer eine eigene Tour vorbereitet, kann die Strecke als GPX mitnehmen und weitergeben. Das ist auch bei einer gemeinsamen Ausfahrt praktisch. OnPath selbst ist auf Planung und Navigation ausgerichtet; eine Gruppenverwaltung gibt es nicht.</p>'),
('Unterwegs einen Abstecher einbauen','<p>Für eigene Pläne kannst du den weiteren Weg ändern, ohne die Aufzeichnung zu stoppen. Halte dafür an, passe deine Route an und fahre weiter. Importierte GPX-Strecken lassen sich derzeit noch nicht wie ein eigener Plan bearbeiten.</p>'+button('/hilfe/gpx/','GPX-Touren nutzen'))])
article('/idee/','Persönlich entwickelt','Warum ich OnPath baue.','Ich bin gern draußen unterwegs – und wollte eine App, die das Planen und Ändern einer Tour leicht macht.',[
('Wer ich bin','<img src="/assets/christian.webp" alt="Christian Neuhaus beim Wandern in den Bergen" class="me" width="400" height="400"><p>Ich bin Christian Neuhaus und ein bisschen ein Nerd: Seit über 30 Jahren lebe und arbeite ich mit IT. Ich probiere gern Neues aus, baue kleine Geräte mit Sensoren und Kameras und zeige Kindern, wie Programmieren geht.</p><p>Am liebsten bin ich aber draußen – zu Fuß in den Bergen oder mit dem Rad. Bei OnPath kommt beides zusammen.</p><p class="me-link">Mehr über mich und meine Bastelprojekte: <a href="https://44-2.de/de/">44-2.de</a></p>'),
('Aus eigenen Touren entstanden','<p>Komoot habe ich viele Jahre gern genutzt. Unterwegs haben mich aber immer wieder dieselben Dinge gestört: die Route auf dem Handy ändern, ohne Netz neu planen, nach einer Pause einfach weitergehen. Einmal änderte sich mein Plan sogar in der Hosentasche.</p><p>OnPath ist mein Versuch, das einfacher zu lösen. Im Mittelpunkt steht dein Weg – ohne Profil, Feed oder Ranglisten.</p>'),
('Robust heißt: keine Überraschungen','<p>Eine neue Route gibt es nur nach Rückfrage. Zum Ändern wechselst du bewusst in die Planung. Jeder aufgezeichnete Punkt wird sofort gespeichert. So bringt ein falscher Tipp oder ein Funkloch den Tag nicht durcheinander.</p><p>Das ist der Anspruch. OnPath ist noch jung und bisher vor allem von mir getestet. Ob es auf deinem Handy und deinen Wegen taugt, zeigen weitere Tests.</p>'),
('Mit KI gebaut, auf Touren geprüft','<p>KI unterstützt mich beim Programmieren und Prüfen von OnPath. So kann ich das Projekt als einzelner Entwickler umsetzen.</p><p>Auf meinen Wanderungen und Radtouren probiere ich aus, was im Alltag funktioniert. Daraus entstehen die nächsten Verbesserungen: Was muss unterwegs einfach klappen? Wo darf die App nicht stören?</p>'),
('Offen und fair','<p>Der Bauplan der App ist öffentlich („Open Source“): Jeder kann nachsehen, wie sie arbeitet, und mithelfen. Die Karten kommen aus dem Gemeinschaftsprojekt OpenStreetMap.</p><p>Planen, navigieren und aufzeichnen bleiben kostenlos. Spätere Zusatzangebote sollen die Kosten decken, meine Arbeit vergüten und einen Teil spenden. Wie sich das verteilt, soll offen sichtbar sein. <a href="/ausblick/">Mehr zur Finanzierung</a>.</p>'+button(GITHUB,'Das Projekt auf GitHub ansehen'))])
article('/ausblick/','Heute & als Nächstes','OnPath wächst mit deinen Touren.','Was du heute ausprobieren kannst – und was für später gedacht ist.',[
('Heute: die Android-App','<p><span class="tag">Als Testversion verfügbar</span></p><p>Eigene Wege planen, sich führen lassen, unterwegs umplanen und Touren speichern. Geladene Gebiete funktionieren auch ohne Netz. Orte aus Google Maps und vorhandene Tourdateien lassen sich übernehmen. Die Oberfläche ist Deutsch oder Englisch.</p><p>Die Testversion ist kostenlos. Aktuell läuft Phase 1 mit persönlichen Einladungen und Freischaltung durch Christian. Danach folgen die geschlossene Testgruppe und der öffentliche Start. <a href="/ausprobieren/">Die drei Phasen und dein Zugang →</a></p>'),
('Neu: am Computer planen','<p><span class="tag">Im Browser verfügbar</span></p><p>Auf <a href="https://plan.onpath.earth/">plan.onpath.earth</a> planst du deine Tour auf einer großen Karte – kostenlos, ohne Konto und ohne Installation. Die Routen sind dieselben wie in der App. Danach hältst du die Handykamera auf den QR-Code, und der Plan ist auf dem Handy.</p>'),
('Neu: Sprachansagen','<p><span class="tag">In der App</span></p><p>Abbiegehinweise hören, ohne aufs Display zu schauen: OnPath sagt kurz und rechtzeitig an, wo es langgeht – nur dort, wo du dich vertun könntest. Die Stimme kommt vom Handy selbst und braucht kein Netz.</p>'),
('Im Test: Browser und Handy verbinden','<p><span class="tag">Im Test</span></p><p>Einmal mit der Handykamera den Code auf dem Computerbildschirm erfassen: Danach kommen gespeicherte Pläne von selbst auf beide Geräte – verschlüsselt und ohne OnPath-Konto. Die Verbindung lässt sich jederzeit wieder trennen.</p>'),
('Der Kern bleibt frei','<p>Die wichtigsten Funktionen bleiben kostenlos nutzbar: Routen auf dem Handy planen, navigieren und mit geladenen Karten offline umplanen. OnPath ist Open Source. Der App-Code ist öffentlich, und deine Touren kannst du als Dateien sichern und in anderen Apps nutzen.</p>'),
('Spätere Beiträge: Kosten, Arbeit und Spende','<p>Karten bereitzustellen und die App weiterzuentwickeln kostet Geld und Zeit. Spätere kostenpflichtige Zusatzangebote sollen das Projekt tragen, etwa rund um das Speichern und Abgleichen von Plänen im Browser.</p><ul><li>Ein Teil soll die laufenden Kosten decken, zum Beispiel für Kartenbereitstellung und Betrieb.</li><li>Ein Teil soll meine Entwicklungsarbeit vergüten.</li><li>Ein Teil soll an eine Hilfsorganisation gespendet werden.</li></ul><p>OnPath ist nicht als gewinnorientiertes Geschäftsmodell gedacht. Es soll sich fair tragen und zugleich etwas weitergeben.</p>'),
('Die Aufteilung soll nachvollziehbar sein','<p>Vorgesehen ist eine offene Übersicht: Einnahmen, Gebühren, Betriebskosten, mein Anteil und die tatsächlich geleisteten Spenden. So soll sichtbar werden, wohin das Geld geht.</p><p>Preise, Anteile, Hilfsorganisation, genauer Leistungsumfang und Zahlungsweg stehen noch nicht fest. Es gibt hier noch kein bestellbares Bezahlangebot.</p>')])
# Access currently uses personal invitations. No individual invite link is published here.
TESTER={'de':dict(
 eye='Aktuell: Phase 1 von 3',title='OnPath persönlich ausprobieren.',
 lead='OnPath startet im kleinen Kreis. Wenn du mittesten möchtest, schreib mir. Ich stimme deinen persönlichen Testzugang mit dir ab.',
 phases_h='In drei Phasen zum öffentlichen Start',phases=[
  ('Persönliche Einladungen','Jetzt','Ich lade einzelne Wanderer und Radfahrer ein und schalte sie frei. Im direkten Austausch zeigt sich, was im Alltag funktioniert und wo noch etwas hakt.'),
  ('Geschlossene Testgruppe','Als Nächstes','Danach soll eine größere, geschlossene Gruppe OnPath über Google Play testen. Der Zugang bleibt auf die Testgruppe beschränkt. Die Anleitung zur Teilnahme folgt zum Start dieser Phase.'),
  ('Öffentlicher Start','Später','Nach den Tests soll OnPath regulär über Google Play verfügbar werden. Eine persönliche Einladung und Testfreischaltung sind dann nicht mehr nötig.')],
 before_h='Was du brauchst',before=['Ein Android-Handy ab Version 8.'],
 check='Du brauchst kein OnPath-Konto. Der persönliche Test ist kostenlos.',
 steps=[
  ('Einladung anfragen','Schreib mir kurz, ob du zu Fuß oder mit dem Rad unterwegs bist und welches Android-Handy du nutzt.','Danach melde ich mich mit den nächsten Schritten bei dir.','invite','Einladung anfragen',''),
  ('Testzugang erhalten','Ich stimme die Teilnahme mit dir ab und schalte dich frei.','Du bekommst deinen Einladungslink und die Installationshinweise direkt von mir.','','',''),
  ('OnPath ausprobieren','Öffne den Link auf deinem Android-Handy und folge den Installationshinweisen.','Beginne mit einer kurzen, bekannten Strecke und sag mir, was gut klappt oder noch unklar ist.','','','')],
 after='Schon installiert? Hier geht es weiter: <a href="/hilfe/erste-schritte/">Erste Schritte mit OnPath →</a>',
 faq_h='Fragen zum Zugang',faq=[
  ('Ich habe schon einen Einladungslink.','Folge den Hinweisen in deiner Einladung. Wenn der Link nicht funktioniert, melde dich bei mir unter <a href="mailto:info@onpath.earth">info@onpath.earth</a>.'),
  ('Kann ich ohne Einladung etwas ausprobieren?','Ja. Den <a href="https://plan.onpath.earth/">Browserplaner</a> kannst du schon jetzt ohne Einladung, Konto oder Installation ausprobieren. Die Android-App ist aktuell im persönlichen Test.'),
  ('Kostet der Test etwas?','Nein. Die Teilnahme am Test ist kostenlos.'),
  ('Wann beginnt die geschlossene Testgruppe?','Sie ist der nächste Schritt. Sobald sie startet, findest du hier die Anleitung und den Zugang.')],
 more_h='Gut zu wissen',more=[
  ('Eine frühe Testversion','OnPath ist noch jung und wurde bisher vor allem von mir auf eigenen Touren in Südtirol genutzt. Eine iPhone-Version gibt es noch nicht. Plane für den Anfang eine kurze, bekannte Strecke.'),
  ('Was beim Testen hilft','Du musst dich nicht mit Technik auskennen. Sag einfach, was du machen wolltest, was passiert ist und was du erwartet hast. Auch „Diesen Schritt habe ich nicht verstanden“ hilft weiter.')]),
'en':dict(
 eye='Current stage: phase 1 of 3',title='Try OnPath by personal invitation.',
 lead='OnPath is starting with a small group. Write to me if you would like to take part. I will arrange your personal test access with you.',
 phases_h='Three phases towards the public release',phases=[
  ('Personal invitations','Now','I invite individual hikers and cyclists and approve their access. Direct feedback shows what works on real outings and what needs improving.'),
  ('Closed test group','Next','A larger, closed group will then test OnPath through Google Play. Access will remain limited to the test group. Instructions for joining will follow when this phase starts.'),
  ('Public release','Later','After testing, OnPath is intended to become generally available through Google Play. A personal invitation and test approval will then no longer be needed.')],
 before_h='What you need',before=['An Android phone, version 8 or newer.'],
 check='You do not need an OnPath account. The personal test is free.',
 steps=[
  ('Ask for an invitation','Briefly tell me whether you walk or cycle and which Android phone you use.','I will get back to you with the next steps.','invite','Ask for an invitation',''),
  ('Receive test access','I will arrange participation with you and approve your access.','You will receive your invitation link and installation instructions directly from me.','','',''),
  ('Try OnPath','Open the link on your Android phone and follow the installation instructions.','Start with a short route you know and tell me what works well or is still unclear.','','','')],
 after='Already installed? Continue here: <a href="/help/getting-started/">First steps with OnPath →</a>',
 faq_h='Questions about access',faq=[
  ('I already have an invitation link.','Follow the instructions in your invitation. If the link does not work, contact me at <a href="mailto:info@onpath.earth">info@onpath.earth</a>.'),
  ('Can I try anything without an invitation?','Yes. You can already try the <a href="https://plan.onpath.earth/">browser planner</a> without an invitation, account or installation. The Android app is currently in personal testing.'),
  ('Does the test cost anything?','No. Taking part in the test is free.'),
  ('When does the closed test group start?','It is the next step. When it starts, this page will explain how to join.')],
 more_h='Good to know',more=[
  ('An early test version','OnPath is still young and I have mainly used it on my own tours in South Tyrol so far. There is no iPhone version yet. Start with a short route you know.'),
  ('What helps when testing','You do not need technical knowledge. Just say what you wanted to do, what happened and what you expected. “I did not understand this step” helps too.')])}
def tester_page(lang='de'):
    T=TESTER[lang]
    def act(key,label):
        if not key:return ''
        return '<a class="button" href="mailto:info@onpath.earth">'+label+icon('arrow')+'</a>'
    phase_cards=''.join('<article class="feature"'+(' aria-current="step"' if i==0 else '')+'><div class="feature-top"><span>0'+str(i+1)+'</span><span class="tag">'+status+'</span></div><h3>'+title+'</h3><p>'+description+'</p></article>' for i,(title,status,description) in enumerate(T['phases']))
    phases='<section class="section soft"><div class="wrap"><div class="section-heading"><h2>'+T['phases_h']+'</h2></div><div class="feature-grid">'+phase_cards+'</div></div></section>'
    before='<div class="tester-before"><h2>'+T['before_h']+'</h2><ul>'+''.join('<li>'+icon('check')+'<span>'+x+'</span></li>' for x in T['before'])+'</ul><p class="tester-check">'+T['check']+'</p></div>'
    steps='<ol class="tester-steps">'+''.join('<li><span class="step-no" aria-hidden="true">'+str(i+1)+'</span><div><h3>'+t+'</h3><p>'+a+'</p><p class="step-then">'+b+'</p>'+act(k,l)+'</div></li>' for i,(t,a,b,k,l,tip) in enumerate(T['steps']))+'</ol>'
    faq='<div class="tester-faq"><h2>'+T['faq_h']+'</h2>'+''.join('<details><summary>'+q+'</summary><p>'+a+'</p></details>' for q,a in T['faq'])+'</div>'
    more='<div class="points">'+''.join('<p><b>'+t+'</b>'+x+'</p>' for t,x in T['more'])+'</div>'
    hero='<section class="page-hero"><div class="wrap"><p class="eyebrow">'+T['eye']+'</p><h1>'+T['title']+'</h1><p class="lead">'+T['lead']+'</p><div class="actions">'+act('invite',T['steps'][0][4])+'</div></div></section>'
    return hero+phases+'<section class="section"><div class="wrap tester">'+before+steps+'<p class="tester-after">'+T['after']+'</p>'+faq+'</div></section><section class="section soft"><div class="wrap"><h2>'+T['more_h']+'</h2>'+more+'</div></section>'
page('/ausprobieren/','OnPath persönlich ausprobieren','Phase 1: OnPath mit persönlicher Einladung und Freischaltung durch Christian testen.',tester_page('de'))
article('/projekt/','Projektinformationen','Offen entwickelt. Klar beschrieben.','OnPath ist ein unabhängiges Projekt von Christian Neuhaus.',[
('Stand dieser Seite','<p>Stand: 30. Oktober 2026, abgeglichen mit der App-Version 0.13.1 und dem Planer auf plan.onpath.earth. Die Webseite ist noch eine Testfassung und für Suchmaschinen ausgeblendet; Impressum und Datenschutz werden vor dem öffentlichen Start rechtlich geprüft.</p><p>Aktuell läuft Phase 1 mit persönlichen Einladungen und Freischaltung durch Christian. Die geschlossene Testgruppe ist der nächste Schritt: <a href="/ausprobieren/">OnPath ausprobieren</a>.</p>'),
('Bildnachweis','<p>Foto auf der Startseite: Christian Neuhaus, bei Vellau (Südtirol). Porträt: Christian Neuhaus, privat. Keine KI-generierten Fotos.</p><p>Die Bildschirmbilder sind echte Aufnahmen der App (mit simulierter Fahrt) und des Planers.</p>'),
('Quellcode und Karten','<p><a href="'+GITHUB+'">OnPath auf GitHub</a> · Apache 2.0. Kartendaten: <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap-Mitwirkende</a>. Routenberechnung: <a href="https://github.com/abrensch/brouter">BRouter</a>.</p>'),
('Unabhängigkeit','<p>OnPath ist nicht mit Komoot oder Google verbunden. Genannte Namen gehören den jeweiligen Rechteinhabern.</p>')])
page('/404/','Seite nicht gefunden','Hier geht es zurück zur Übersicht.',ph('Seite nicht gefunden','Hier geht der Weg nicht weiter.','Die gesuchte Seite gibt es hier nicht.')+'<section class="section"><div class="wrap actions">'+button('/','Zur Startseite')+button('/hilfe/','Zur Hilfe',True)+'</div></section>')


from legal_content import DE_LEGAL, DE_PRIVACY
article('/impressum/','Anbieterangaben','Impressum','Anbieter und Kontakt für OnPath.',DE_LEGAL)
article('/datenschutz/','Deine Daten','Datenschutzhinweise','Website und Android-App: verständlich getrennt erklärt.',DE_PRIVACY)
