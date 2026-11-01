"""App screens on the help pages – one place to say which picture goes where.

To swap a picture: drop the new PNG (same file name) into the source folder and run
`python3 scripts/help_shots.py <folder with the PNGs>`, then `python3 build.py`.
To add one: add it to IMAGES and to SHOTS, then run the same two commands.

IMAGES: name -> (source PNG German app, source PNG English app or None, German text, English text).
        The text is both the alt text and the caption. Without an English PNG the English pages show
        the German screen and say so.
SHOTS:  language -> (help page slug, section number from 0) -> picture names, shown under that section.
        Inside a section's text, [[shots:name,name]] puts pictures at that place instead (see inline()).
"""
import json
import re
from html import escape
from pathlib import Path

IMAGES = {
    'leer': ('08a-erste-route-leer.png', None, 'Leerer Plan: Hier setzt du den ersten Punkt.', 'Empty plan: this is where you set the first point.'),
    'halten': ('08b-erste-route-halten.png', 'halten-en.png', 'Karte gedrückt halten: „Hier starten“ oder „Von meinem Standort hierhin“.', 'Hold the map: “Start here” or “Go here from my location”.'),
    'punkt1': ('08c-erste-route-punkt1.png', None, 'Der Start ist gesetzt, jetzt kommt das Ziel.', 'The start is set, now the destination.'),
    'ziel': ('08d-erste-route-ziel-menue.png', None, 'Einen Ort halten und als Ziel setzen.', 'Hold a place and set it as the destination.'),
    'fertig': ('08e-erste-route-fertig.png', None, 'Die Route steht: Zeit, Länge, Hinweise und Höhenprofil.', 'The route is ready: time, distance, notes and elevation profile.'),
    'plan': ('02-plan-wandern.png', 'plan-wandern-en.png', 'Wandern T2: Zeit, Höhenmeter und zwei steile Abschnitte.', 'Hike T2: time, climbing and two steep sections.'),
    'ebike': ('03-plan-ebike.png', 'plan-ebike-en.png', 'Dieselbe Strecke mit dem E-Bike, mit Schiebestück.', 'The same route by e-bike, with a short push.'),
    'punkteliste': ('08f-plan-punkteliste.png', 'plan-punkteliste-en.png', 'Das Plan-Fenster ganz hochgezogen: Profil und alle Punkte.', 'The plan panel pulled all the way up: profile and all points.'),
    'hinweise': ('02b-plan-wandern-hinweise.png', None, 'Die Hinweise zur Strecke: wo es steil wird.', 'Notes on the route: where it gets steep.'),
    'navi': ('09a-unterwegs-navigation-stopp.png', 'navigation-stopp-en.png', 'Navigation, unten der Schieber „Stopp“.', 'Navigation, with the “Stop” slider at the bottom.'),
    'tourmenue': ('09b-unterwegs-tourmenue.png', 'tourmenue-en.png', 'Nach dem Schieben: Die Tour läuft weiter, „Weiter“ führt zurück.', 'After sliding: the tour keeps running, “Continue” takes you back.'),
    'suche': ('09b2-unterwegs-suche.png', None, 'Einen Ort suchen, auch unterwegs.', 'Search for a place, also on the way.'),
    'ort': ('09c-unterwegs-ort-halten.png', 'ort-google-maps-en.png', 'Ort gefunden: als neues Ziel anhängen oder in Google Maps öffnen.', 'Place found: add it as a new destination or open it in Google Maps.'),
    'neue-route': ('09d-unterwegs-neue-route.png', None, 'Die neue Route zum Gasthof – ohne Netz berechnet.', 'The new route to the inn – calculated without a connection.'),
    'zurueck': ('09e-unterwegs-zurueck.png', None, 'Zurück in der Navigation, mit neuer Ankunftszeit.', 'Back in navigation, with the new arrival time.'),
    'g-uebernommen': ('google-ziel-uebernommen-de.png', 'google-ziel-uebernommen-en.png', 'Aus Google Maps geteilt: der Ort in OnPath.', 'Shared from Google Maps: the place in OnPath.'),
    'g-route': ('google-ziel-route-de.png', 'google-ziel-route-en.png', 'Nach „Hierhin“: die Route zu diesem Ort.', 'After “Go here”: the route to this place.'),
    'ankunft': ('05-ankunft.png', '05-ankunft-en.png', 'Navigation: nächste Abzweigung, Restzeit und Ankunft.', 'Navigation: next turn, time left and arrival.'),
    'ruhe': ('06-ruheanzeige.png', 'ruheanzeige-en.png', 'Ruheanzeige am Rad: nur Pfeil, Entfernung und Ankunft.', 'Rest view on the bike: only arrow, distance and arrival.'),
    'beenden': ('10a-tour-beenden.png', None, '„Tour beenden?“ – dann „Speichern“.', '“End this tour?” – then “Save”.'),
    'fahrt': ('07-fahrt.png', 'fahrt-en.png', 'Eine erkannte Liftfahrt: Du entscheidest, ob sie zählt.', 'A recognised chairlift ride: you decide whether it counts.'),
    'gespeichert': ('10b-tour-gespeichert.png', None, 'Die Tour ist gespeichert, auf Wunsch auch als GPX.', 'The tour is saved, also as GPX if you like.'),
    'meine-routen': ('10c-meine-routen.png', None, 'Meine Routen → Gemacht: deine Touren.', 'My routes → Done: your tours.'),
    'web-plan': ('web-plan-de.png', 'web-plan-en.png', 'Der Planer im Browser: Route, Zeit, Höhenprofil und Punkte.', 'The planner in the browser: route, time, elevation profile and points.'),
    'web-teilen': ('web-teilen-de.png', 'web-teilen-en.png', '„Teilen“: den QR-Code mit der Handykamera scannen.', '“Share”: scan the QR code with your phone camera.'),
    'web-handy': ('web-handy-de.png', 'web-handy-en.png', 'Im Browser oben „Handy verbinden“ – hier steht auch, wie es funktioniert.', '“Pair phone” at the top of the browser – it also says how it works.'),
    'web-koppeln': ('web-koppeln-de.png', None, 'Der Code zum Koppeln (hier unkenntlich gemacht) – mit OnPath scannen.', 'The pairing code (blurred here) – scan it with OnPath.'),
    'app-koppeln': ('com.onpath.app.ui_GermanScreenshotTest_planPairHint.png', 'com.onpath.app.ui_ScreenshotTest_planPairHint.png', 'In der App: ☰ → „Mit Browser verbinden“ → „Kamera öffnen“.', 'In the app: ☰ → “Pair with browser” → “Open camera”.'),
    'app-verbunden': ('com.onpath.app.ui_GermanScreenshotTest_planPairedNote.png', 'com.onpath.app.ui_ScreenshotTest_planPairedNote.png', 'Verbunden – was du im Browser speicherst, kommt aufs Handy.', 'Paired – what you save in the browser comes to your phone.'),
    'app-routen': ('com.onpath.app.ui_GermanScreenshotTest_toursFromBrowser.png', 'com.onpath.app.ui_ScreenshotTest_toursFromBrowser.png', '„Meine Routen“: Routen aus dem Browser mit „Neu“ oder „Geändert“.', '“My routes”: routes from the browser marked “New” or “Changed”.'),
    'app-trennen': ('com.onpath.app.ui_GermanScreenshotTest_settingsSyncPaired.png', None, 'Einstellungen → Browser-Abgleich: hier trennst du.', 'Settings → Browser sync: this is where you unpair.'),
    'neustart-hinweis': ('neustart-hinweis-de.png', 'neustart-hinweis-en.png', 'Nach einem Neustart: Die Aufzeichnung ist gespeichert.', 'After a restart: the recording is saved.'),
    'neustart': ('neustart-de.png', 'neustart-en.png', '„Unterbrochene Tour“: fortsetzen, löschen oder speichern.', '“Unfinished tour”: continue, delete or save.'),
}

SHOTS = {
    'de': {
        ('erste-schritte', 2): ['leer', 'halten', 'ziel', 'fertig'],
        ('erste-schritte', 3): ['navi'],
        ('offline', 0): ['neue-route'],
        ('route-planen', 0): ['plan', 'ebike'],
        ('route-planen', 1): ['punkt1', 'ziel', 'punkteliste'],
        ('route-planen', 2): ['hinweise'],
        ('unterwegs-aendern', 0): ['navi', 'tourmenue'],
        ('unterwegs-aendern', 1): ['suche', 'ort', 'neue-route'],
        ('unterwegs-aendern', 2): ['zurueck'],
        ('orte', 0): ['suche'],
        ('orte', 1): ['g-uebernommen', 'g-route'],
        ('orte', 2): ['ort'],
        ('route-planen', 5): ['web-plan', 'web-teilen'],
        ('gpx', 3): ['gespeichert', 'meine-routen'],
        ('probleme', 2): ['neustart-hinweis', 'neustart'],
        ('navigation', 0): ['ankunft', 'ruhe'],
        ('navigation', 3): ['beenden', 'fahrt'],
    },
    'en': {
        ('getting-started', 1): ['leer', 'halten', 'ziel', 'fertig'],
        ('getting-started', 2): ['navi'],
        ('offline', 0): ['neue-route'],
        ('planning', 0): ['plan', 'ebike'],
        ('planning', 1): ['punkt1', 'ziel', 'punkteliste'],
        ('planning', 2): ['hinweise'],
        ('change-route', 0): ['navi', 'tourmenue'],
        ('change-route', 1): ['suche', 'ort', 'neue-route'],
        ('change-route', 2): ['zurueck'],
        ('places', 0): ['suche'],
        ('places', 1): ['ort'],
        ('places', 2): ['g-uebernommen', 'g-route'],
        ('planning', 5): ['web-plan', 'web-teilen'],
        ('gpx', 2): ['gespeichert', 'meine-routen'],
        ('navigation', 0): ['ankunft', 'ruhe'],
        ('navigation', 2): ['beenden', 'fahrt'],
    },
}

WIDTH, HEIGHT = 540, 1200  # phone screens are stored 540 wide (1080 × 2400 halved); other shapes keep their ratio
WIDE = {'web-plan'}           # browser screens shown across the text column, stored up to 1200 wide
WIDE_MAX = 1200
TOP = {'app-routen': 0.335, 'app-trennen': 0.2}  # keep only this top share of a mostly empty screen
SIZES_FILE = Path(__file__).resolve().parent / 'assets' / 'help' / 'sizes.json'


def sizes():
    """Stored picture sizes, written by scripts/help_shots.py ({file: [width, height]})."""
    try:
        return json.loads(SIZES_FILE.read_text())
    except (OSError, ValueError):
        return {}


def files(name):
    """Website files of a picture: (German file, English file)."""
    de_src, en_src, *_ = IMAGES[name]
    return f'{name}-de.webp', (f'{name}-en.webp' if en_src else f'{name}-de.webp')


def shots_html(lang, slug, index):
    return figures(lang, SHOTS[lang].get((slug, index), []))


def inline(lang, text):
    """Pictures inside a section's text: [[shots:name,name]] becomes a row of pictures at that place."""
    return re.sub(r'\[\[shots:([a-z0-9,-]+)\]\]', lambda m: figures(lang, m.group(1).split(',')), text)


def figures(lang, names):
    if not names:
        return ''
    figs, known = '', sizes()
    for name in names:
        de_src, en_src, de_text, en_text = IMAGES[name]
        if lang == 'de':
            file, text = files(name)[0], de_text
        else:
            file, text = files(name)[1], en_text + ('' if en_src else ' (German screen)')
        t = escape(text)
        w, h = known.get(file, (WIDTH, HEIGHT))
        wide = ' class="wide"' if name in WIDE else (' class="part"' if name in TOP else '')
        figs += (f'<figure{wide}><img src="/assets/help/{file}" alt="{t}" width="{w}" height="{h}" '
                 f'loading="lazy" decoding="async"><figcaption>{t}</figcaption></figure>')
    return f'<div class="help-shots">{figs}</div>'
