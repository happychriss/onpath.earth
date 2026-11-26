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

IMAGES = {'leer': ('D01-handy-leerer-plan-de.png',
          'D01-handy-leerer-plan-en.png',
          'Leerer Plan: hier beginnt die Planung.',
          'Empty plan: this is where planning begins.'),
 'halten': ('D03-handy-karte-halten-hierhin-de.png',
            'D03-handy-karte-halten-hierhin-en.png',
            'Karte gedrückt halten: „Hier starten“ oder „Hierhin“.',
            'Hold the map: Start here or Go here.'),
 'punkt1': ('D04-handy-start-gesetzt-de.png',
            'D04-handy-start-gesetzt-en.png',
            'Der Start ist gesetzt, jetzt kommt das Ziel.',
            'The start is set, now choose the destination.'),
 'ziel': ('D09-handy-ort-halten-als-zwischenstopp-de.png',
          'D09-handy-ort-halten-als-zwischenstopp-en.png',
          'Einen Ort als Zwischenstopp oder neues Ziel übernehmen.',
          'Use a place as a stop or a new destination.'),
 'fertig': ('D05-handy-route-fertig-los-gehts-de.png',
            'D05-handy-route-fertig-los-gehts-en.png',
            'Der Plan steht: Strecke prüfen und mit „Los geht’s“ starten.',
            'The plan is ready: check the route and tap Let’s go.'),
 'plan': ('D06-handy-plan-wandern-t2-de.png',
          'D06-handy-plan-wandern-t2-en.png',
          'Wandern T2: Zeit, Höhenmeter, Streckenhinweise und Höhenprofil.',
          'Hike T2: time, climbing, route notes and elevation profile.'),
 'ebike': ('K01-handy-plan-ebike-de.png',
           'K01-handy-plan-ebike-en.png',
           'Ein E-Bike-Plan bei Meran: Zeit, Höhenprofil und Schiebestrecke.',
           'An e-bike plan near Meran: time, elevation profile and a pushing section.'),
 'punkteliste': ('D11-handy-punkteliste-de.png',
                 'D11-handy-punkteliste-en.png',
                 'Das Plan-Fenster ganz hochgezogen: Profil und alle Punkte.',
                 'The plan panel pulled up: profile and all points.'),
 'hinweise': ('D07-handy-hinweise-steil-de.png',
              'D07-handy-hinweise-steil-en.png',
              'Die Streckenhinweise zeigen, wo es steil wird.',
              'Route notes show the steep sections.'),
 'navi': ('E01-handy-navigation-gesperrt-de.png',
          'E01-handy-navigation-gesperrt-en.png',
          'Navigation: nächste Abzweigung, Restzeit, Ankunft sowie Anhalten und Planen.',
          'Navigation: next turn, remaining time, arrival, Stop and Plan.'),
 'tourmenue': ('E06-handy-pause-de.png',
               'E06-handy-pause-en.png',
               'Die Tour ist angehalten: weiter, Tour beenden oder planen.',
               'The outing is stopped: resume, end the tour or plan.'),
 'suche': ('F02-handy-suche-einkehr-offline-de.png',
           'F02-handy-suche-einkehr-offline-en.png',
           'Eine Einkehr suchen, auch ohne Netz.',
           'Search for a place to stop, even offline.'),
 'ort': ('F03-handy-pin-karte-einkehr-de.png',
         'F03-handy-pin-karte-einkehr-en.png',
         'Eine Einkehr auf der Karte: hinzufügen oder weitere Möglichkeiten öffnen.',
         'An inn on the map: add it or open more options.'),
 'neue-route': ('F04-handy-neue-route-mit-einkehr-de.png',
                'F04-handy-neue-route-mit-einkehr-en.png',
                'Die angepasste Route mit Einkehr während einer laufenden Tour.',
                'The adjusted route with a stop during a recorded outing.'),
 'zurueck': ('F05-handy-weiter-gehts-de.png',
             'F05-handy-weiter-gehts-en.png',
             'Mit „Weiter geht’s“ zurück in die Navigation.',
             'Return to navigation with On we go.'),
 'g-uebernommen': ('J02-handy-ort-aus-google-de.png',
                   'J02-handy-ort-aus-google-en.png',
                   'Aus Google Maps geteilt: der Ort in OnPath.',
                   'Shared from Google Maps: the place in OnPath.'),
 'g-route': ('J03-handy-route-zum-ort-de.png',
             'J03-handy-route-zum-ort-en.png',
             'Der Weg zum übernommenen Ort in OnPath.',
             'The route to the shared place in OnPath.'),
 'ankunft': ('E03-handy-abzweigung-ankunft-de.png',
             'E03-handy-abzweigung-ankunft-en.png',
             'Nächste Abzweigung und geschätzte Ankunft auf einen Blick.',
             'Next turn and estimated arrival at a glance.'),
 'ruhe': ('K02-handy-ruheanzeige-de.png',
          'K02-handy-ruheanzeige-en.png',
          'Ruheanzeige am Rad: Richtung, Entfernung und Ankunft.',
          'Cycling rest view: direction, distance and arrival.'),
 'beenden': ('H02-handy-tour-beenden-de.png',
             'H02-handy-tour-beenden-en.png',
             'Die Tour bewusst beenden und speichern.',
             'Finish and save the outing.'),
 'fahrt': ('H03-handy-liftfahrt-erkannt-de.png',
           'H03-handy-liftfahrt-erkannt-en.png',
           'Eine erkannte Liftfahrt: Du entscheidest, was zählt.',
           'A detected lift journey: you decide what counts.'),
 'gespeichert': ('H04-handy-gemacht-gerade-gespeichert-de.png',
                 'H04-handy-gemacht-gerade-gespeichert-en.png',
                 'Die abgeschlossene Tour unter „Meine Touren“ → „Gemacht“.',
                 'The completed outing under My tours → Done.'),
 'meine-routen': ('I01-handy-meine-touren-geplant-de.png',
                  'I01-handy-meine-touren-geplant-en.png',
                  'Meine Touren: gespeicherte Pläne und GPX-Import.',
                  'My tours: saved plans and GPX import.'),
 'web-plan': ('B02-web-route-fertig-de.png',
              'B02-web-route-fertig-en.png',
              'Der Browser-Planer: Route, Zeit, Höhenprofil und Punkte.',
              'The browser planner: route, time, elevation profile and points.'),
 'web-teilen': ('B06-web-teilen-qr-de.png',
                'B06-web-teilen-qr-en.png',
                '„Teilen“: den QR-Code mit der Handykamera scannen.',
                'Share: scan the QR code with your phone camera.'),
 'web-handy': ('C01-web-handy-fenster-de.png',
               'C01-web-handy-fenster-en.png',
               'Das Handy-Fenster im Browser: verbinden und abgleichen.',
               'The phone window in the browser: pair and sync.'),
 'web-koppeln': ('C02-web-koppel-code-de.png',
                 'C02-web-koppel-code-en.png',
                 'Der Code zum Koppeln, hier unkenntlich gemacht: mit OnPath scannen.',
                 'The pairing code, blurred here: scan it with OnPath.'),
 'app-koppeln': ('C03-handy-menue-koppeln-de.png',
                 'C03-handy-menue-koppeln-en.png',
                 'Im App-Menü „Mit Browser koppeln“ öffnen.',
                 'Open Pair with browser in the app menu.'),
 'app-verbunden': ('C05-handy-verbunden-de.png',
                   None,
                   'Browser und Handy sind verbunden.',
                   'Browser and phone are paired.'),
 'app-routen': ('C07-handy-plan-aus-browser-de.png',
                None,
                'Ein gespeicherter Plan aus dem Browser auf dem Handy.',
                'A saved browser plan on the phone.'),
 'app-trennen': ('C08-handy-trennen-de.png',
                 None,
                 'Einstellungen → Browser-Abgleich: die Verbindung trennen.',
                 'Settings → Browser sync: unpair the devices.'),
 'neustart-hinweis': ('L01-handy-neustart-hinweis-de.png',
                      'L01-handy-neustart-hinweis-en.png',
                      'Nach einem Neustart: Die Aufzeichnung ist gespeichert.',
                      'After a restart: the recording is saved.'),
 'neustart': ('L02-handy-unterbrochene-tour-de.png',
              'L02-handy-unterbrochene-tour-en.png',
              'Eine unterbrochene Tour fortsetzen, speichern oder löschen.',
              'Resume, save or delete an interrupted outing.'),
 'ohne-netz': ('D12-handy-ohne-netz-erklaert-de.png',
               'D12-handy-ohne-netz-erklaert-en.png',
               '„Ohne Netz ✓“ erklärt, was für die Strecke auf dem Handy liegt.',
               'Offline ✓ explains what is downloaded for this route.'),
 't-band': ('D08-handy-t-band-t3-de.png',
            'D08-handy-t-band-t3-en.png',
            'Ein T3-Weg ist gegenüber der gewählten Stufe T2 hervorgehoben.',
            'A T3 path is highlighted against the selected T2 difficulty.'),
 'erreichbar': ('D10-handy-erreichbar-ab-t2-de.png',
                'D10-handy-erreichbar-ab-t2-en.png',
                'OnPath zeigt, ab welcher Schwierigkeit ein gesetzter Punkt erreichbar ist.',
                'OnPath shows which difficulty can reach a selected point.'),
 'hinweise-stimme': ('E07-einstellungen-hinweise-stimme-de.png',
                     'E07-einstellungen-hinweise-stimme-en.png',
                     'Hinweise an Abzweigungen: Aus, Vibration oder Stimme.',
                     'Turn hints: Off, Vibration or Voice.'),
 'sicherung': ('L03-einstellungen-sicherung-de.png',
               'L03-einstellungen-sicherung-en.png',
               'Einstellungen → Sicherung: den Ordner für deine Dateien auswählen.',
               'Settings → Backup: choose the folder for your files.'),
 'handy-einrichten': ('A02-handy-einrichten-de.png',
                      'A02-handy-einrichten-en.png',
                      'Das Handy für zuverlässige Aufzeichnung einrichten.',
                      'Set up the phone for reliable recording.'),
 'abseits': ('G01-handy-abseits-der-route-de.png',
             'G01-handy-abseits-der-route-en.png',
             'OnPath zeigt, wenn du abseits der Route bist.',
             'OnPath shows when you are off the route.'),
 'neue-route-frage': ('G02-handy-neue-route-frage-de.png',
                      'G02-handy-neue-route-frage-en.png',
                      '„Original behalten“ oder „Neue Route“: Du entscheidest.',
                      'Keep original or New route: you decide.'),
 'angekommen': ('H01-handy-angekommen-de.png',
                'H01-handy-angekommen-en.png',
                'Am Ziel: weiter aufzeichnen oder die Tour beenden.',
                'At the destination: keep recording or finish the outing.'),
 'gpx-plan': ('I04-handy-gpx-als-plan-de.png',
              'I04-handy-gpx-als-plan-en.png',
              'Einen importierten GPX-Track als eigenen Plan übernehmen.',
              'Turn an imported GPX track into your own plan.'),
 'web-3d': ('B04-web-3d-gelaende-de.png',
            'B04-web-3d-gelaende-en.png',
            'Die geplante Route im dreidimensionalen Gelände.',
            'The planned route in 3D terrain.'),
 'web-profil': ('B03-web-grosses-profil-de.png',
                'B03-web-grosses-profil-en.png',
                'Das große Höhenprofil im Browser.',
                'The large elevation profile in the browser.'),
 'web-touren': ('B07-web-meine-touren-de.png',
                'B07-web-meine-touren-en.png',
                'Gespeicherte Pläne unter „Meine Touren“ im Browser.',
                'Saved plans under My tours in the browser.')}

IMAGES['mehrtage-handy'] = (
    'M01-handy-mehrtagestour-tagesuebersicht-de.png',
    'M01-handy-mehrtagestour-tagesuebersicht-en.png',
    'Eine dreitägige Wanderung am Meraner Höhenweg. Tag 2 ist ausgewählt, die Übersicht zeigt Etappen und Übernachtungen.',
    'A three-day hike on the Meraner Höhenweg. Day 2 is selected, with stages and overnight stops in the overview.',
)

IMAGES.update({
    'rundtour-start': ('N03-handy-rundtour-von-hier-de.png', 'N03-handy-rundtour-von-hier-en.png', 'Auf dem Handy den Startpunkt gedrückt halten und „Rundtour von hier“ wählen.', 'On your phone, press and hold the start and choose “Round trip from here”.'),
    'rundtour-wunsch': ('N01-web-rundtour-wunsch-de.png', 'N01-web-rundtour-wunsch-en.png', 'Wünsche im Browserplaner. Hier sind Wandern T2, 3,5 bis 4,5 Stunden und bis zu 800 Höhenmeter eingestellt.', 'Preferences in the browser planner. This example uses hiking T2, 3.5 to 4.5 hours and up to 800 metres of climbing.'),
    'rundtour-vorschlaege': ('N04-handy-rundtour-kartenreihe-de.png', 'N04-handy-rundtour-kartenreihe-en.png', 'Fünf Rundtourvorschläge bei Alken. Die ausgewählte Karte zeigt Strecke, Dauer und Aufstieg; der Verlauf erscheint auf der Karte.', 'Five round-trip suggestions near Alken. The selected card shows distance, duration and climbing, with the route on the map.'),
    'mehrtage-start': ('B11-web-mehrtagestour-planen-de.png', 'B11-web-mehrtagestour-planen-en.png', 'Der Mehrtagesplaner im Browser. Eine Route ist gewählt; weitere GPX-Tracks oder gespeicherte Routen lassen sich anhängen.', 'The multi-day guide in the browser. A route is selected, with options to append GPX tracks or saved routes.'),
    'mehrtage-tage': ('B13-web-tage-festlegen-de.png', 'B13-web-tage-festlegen-en.png', 'Tage und tägliche Grenzen festlegen. Dieses Beispiel zeigt fünf Tage mit höchstens acht Stunden pro Tag.', 'Set the days and daily limits. This example shows five days with a limit of eight hours per day.'),
    'mehrtage-uebersicht': ('B14-web-mehrtagestour-uebersicht-de.png', 'B14-web-mehrtagestour-uebersicht-en.png', 'Beispiel mit fünf Tagen am Meraner Höhenweg. Blau sind festgelegte Übernachtungen, grün das Hotel und grau das noch offene Tagesende. Das Höhenprofil zeigt die Tagesgrenzen.', 'A five-day example on the Meraner Höhenweg. Blue marks chosen overnight stops, green the hotel and grey the day end still open. The elevation profile shows the day boundaries.'),
    'mehrtage-karte': ('M03-handy-mehrtagestour-naechte-karte-de.png', 'M03-handy-mehrtagestour-naechte-karte-en.png', 'Die Reise auf dem Handy. Übernachtungen und Hotel sind auch auf der Karte zu erkennen; Tag 2 ist zum Laden ausgewählt.', 'The journey on your phone. Overnight stops and the hotel also appear on the map; day 2 is selected to load.'),
})

IMAGES.update({
    'teilen-knopf': ('O01-handy-tour-bubble-teilen-de.png', 'O01-handy-tour-bubble-teilen-en.png', 'Während der Tour: das Teilen-Zeichen rechts über dem ⚙.', 'During the outing: the share symbol on the right above the ⚙.'),
    'teilen-link': ('O02-handy-standort-teilen-link-de.png', 'O02-handy-standort-teilen-link-en.png', 'Den Link mit einer Nachrichten-App verschicken.', 'Send the link with a messaging app.'),
    'teilen-aktiv': ('O03-handy-teilen-aktiv-de.png', 'O03-handy-teilen-aktiv-en.png', 'Das grüne Zeichen: Dein Standort wird geteilt.', 'The green symbol: your location is being shared.'),
    'teilen-wartet': ('O05-handy-wartet-auf-netz-de.png', 'O05-handy-wartet-auf-netz-en.png', 'Ohne Empfang wartet das Teilen auf Netz und schickt die Punkte später nach.', 'Without reception, sharing waits for the network and sends the points later.'),
    'teilen-seite': ('O04-web-geteilter-standort-de.png', 'O04-web-geteilter-standort-en.png', 'Die Seite im Browser: Weg, letzter Standort, Strecke, Ankunft und Akkustand.', 'The page in the browser: way, last position, distance, arrival and battery level.'),
    'teilen-beendet': ('O06-handy-teilen-beendet-de.png', 'O06-handy-teilen-beendet-en.png', 'In den Tour-Einstellungen (⚙): „Standort teilen“ und der Name auf der Seite.', 'In the tour settings (⚙): “Share location” and the name on the page.'),
})

SHOTS = {'de': {('erste-schritte', 2): ['leer', 'halten', 'ziel', 'fertig'],
        ('erste-schritte', 3): ['navi'],
        ('offline', 0): ['ohne-netz'],
        ('route-planen', 0): ['plan', 'ebike'],
        ('route-planen', 1): ['punkt1', 'ziel', 'punkteliste'],
        ('route-planen', 2): ['hinweise', 'erreichbar'],
        ('unterwegs-aendern', 0): ['navi'],
        ('unterwegs-aendern', 1): ['suche', 'ort', 'neue-route'],
        ('unterwegs-aendern', 2): ['zurueck'],
        ('orte', 0): ['suche'],
        ('orte', 1): ['g-uebernommen', 'g-route'],
        ('orte', 2): ['ort'],
        ('route-planen', 5): ['web-plan', 'web-teilen'],
        ('gpx', 3): ['gespeichert', 'meine-routen'],
        ('probleme', 2): ['neustart-hinweis', 'neustart'],
        ('navigation', 0): ['ankunft', 'hinweise-stimme'],
        ('navigation', 3): ['angekommen', 'beenden', 'fahrt'],
        ('erste-schritte', 1): ['handy-einrichten'],
        ('route-planen', 3): ['t-band'],
        ('unterwegs-aendern', 3): ['abseits', 'neue-route-frage'],
        ('gpx', 1): ['meine-routen'],
        ('gpx', 2): ['gpx-plan'],
        ('navigation', 1): ['ruhe'],
        ('akku-sicherung', 0): ['handy-einrichten'],
        ('akku-sicherung', 2): ['sicherung']},
 'en': {('getting-started', 1): ['leer', 'halten', 'ziel', 'fertig'],
        ('getting-started', 2): ['navi'],
        ('offline', 0): ['ohne-netz'],
        ('planning', 0): ['plan', 'ebike'],
        ('planning', 1): ['punkt1', 'ziel', 'punkteliste'],
        ('planning', 2): ['hinweise', 'erreichbar'],
        ('change-route', 0): ['navi'],
        ('change-route', 1): ['suche', 'ort', 'neue-route'],
        ('change-route', 2): ['zurueck'],
        ('places', 0): ['suche'],
        ('places', 1): ['ort'],
        ('places', 2): ['g-uebernommen', 'g-route'],
        ('planning', 5): ['web-plan', 'web-teilen'],
        ('gpx', 2): ['gespeichert', 'meine-routen'],
        ('navigation', 0): ['ankunft', 'hinweise-stimme'],
        ('navigation', 2): ['angekommen', 'beenden', 'fahrt'],
        ('getting-started', 0): ['handy-einrichten'],
        ('planning', 3): ['t-band'],
        ('gpx', 1): ['gpx-plan'],
        ('navigation', 1): ['ruhe'],
        ('troubleshooting', 3): ['neustart-hinweis', 'neustart'],
        ('battery-backup', 0): ['handy-einrichten'],
        ('battery-backup', 2): ['sicherung']}}

WIDTH, HEIGHT = 540, 1200  # phone screens are stored 540 wide (1080 × 2400 halved); other shapes keep their ratio
WIDE = {'web-plan','web-teilen','web-handy','web-koppeln','web-3d','web-profil','web-touren'}
WIDE.update({'rundtour-wunsch', 'mehrtage-start', 'mehrtage-tage', 'mehrtage-uebersicht'})
WIDE_MAX = 1200
TOP = {}  # Current screenshots are shown in full.
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
        figs += (f'<figure{wide}><button type="button" class="help-shot-button" data-lightbox aria-haspopup="dialog" aria-label="{escape(("Bild vergrößern" if lang == "de" else "Enlarge picture") + ": " + text)}"><img src="/assets/help/{file}" alt="{t}" width="{w}" height="{h}" '
                 f'loading="lazy" decoding="async"></button><figcaption>{t}</figcaption></figure>')
    return f'<div class="help-shots">{figs}</div>'


ARTICLE_SHOTS = {
 'de': {('/wandern/',0): ['plan'], ('/wandern/',1): ['ort'], ('/wandern/',3): ['navi'], ('/radfahren/',0): ['ebike'], ('/radfahren/',2): ['gpx-plan'], ('/radfahren/',3): ['ruhe'], ('/ausblick/',0): ['plan'], ('/ausblick/',1): ['web-3d'], ('/ausblick/',2): ['hinweise-stimme'], ('/ausblick/',3): ['web-handy','app-verbunden'], ('/ausblick/',4): ['teilen-seite']},
 'en': {('/hiking/',0): ['plan'], ('/hiking/',1): ['ort'], ('/hiking/',3): ['navi'], ('/cycling/',0): ['ebike'], ('/cycling/',2): ['gpx-plan'], ('/cycling/',3): ['ruhe'], ('/whats-next/',0): ['plan'], ('/whats-next/',1): ['web-3d'], ('/whats-next/',2): ['hinweise-stimme'], ('/whats-next/',3): ['web-handy','app-verbunden'], ('/whats-next/',4): ['teilen-seite']}
}
def article_pictures(lang, path, index):
    return figures(lang, ARTICLE_SHOTS.get(lang, {}).get((path,index), []))
