"""Stable help destinations; numbered section IDs remain valid for older links."""

ANCHORS = {
    'erste-schritte': ['installieren', 'vorbereiten', 'erste-route', 'starten'],
    'getting-started': ['prepare', 'first-route', 'start'],
    'offline': ['offline', 'prepare', 'missing', 'internet'],
    'route-planen': ['aktivitaet', 'punkte', 'streckenhinweise', 'schwierigkeit', 'kartenfarben', 'browser'],
    'planning': ['activity', 'points', 'route-hints', 'difficulty', 'map-colours', 'browser'],
    'unterwegs-aendern': ['aendern', 'neuer-weg', 'weiter', 'abweichung'],
    'change-route': ['edit', 'new-route', 'continue'],
    'orte': ['offline-suche', 'google-maps', 'einkehr', 'daten', 'geteilte-treffpunkte'],
    'places': ['offline-search', 'stop', 'google-maps', 'data', 'shared-meeting-points'],
    'gpx': ['format', 'open', 'your-files'],
    'probleme': ['karten', 'standort', 'tour-fortsetzen', 'melden'],
    'troubleshooting': ['maps', 'location', 'report', 'resume'],
    'navigation': ['turns', 'arrival', 'finish', 'rides'],
    'akku-sicherung': ['hintergrund', 'akku', 'kopie', 'wiederherstellen'],
    'battery-backup': ['background', 'battery', 'backup'],
}

DE_OVERRIDES = {
    'offline': ['offline', 'vorbereiten', 'fehlende-gebiete', 'internet'],
    'gpx': ['format', 'oeffnen', 'verwenden', 'eigene-dateien'],
    'navigation': ['abbiegen', 'sperrbildschirm', 'ankunft', 'tour-beenden', 'fahrten'],
}


def help_anchor(lang, slug, index):
    anchors = DE_OVERRIDES.get(slug, ANCHORS[slug]) if lang == 'de' else ANCHORS[slug]
    return anchors[index]
