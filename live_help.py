"""Public help for sharing your location during a tour (app 0.18.10)."""

HELP_DE = [
    (
        'standort-teilen', 'Standort teilen',
        'Andere sehen im Browser, wo du gerade unterwegs bist – nur solange du es willst.',
        'Standort teilen Link Familie Live verfolgen Tour teilen Teilen beenden Zuschauer',
        [
            ('Wofür das gut ist',
             '<p>Du bist allein in den Bergen unterwegs, und zu Hause möchte jemand wissen, wo du gerade bist. Mit „Standort teilen“ schickst du einen Link, zum Beispiel per Signal oder WhatsApp. Wer ihn öffnet, sieht im Browser deinen bisherigen Weg, deinen letzten Standort und wann er zuletzt ankam. Eine App oder ein Konto braucht dafür niemand.</p>'
             '<p>Das Teilen geht nur in eine Richtung: Du siehst die anderen nicht, und es gibt keine Gruppen.</p>'),
            ('Den Standort teilen',
             '<p>Starte deine Tour. Rechts über dem ⚙ steht in der Navigation das Teilen-Zeichen. Tippe darauf. Beim ersten Mal fragt OnPath nach dem Namen für die Seite, zum Beispiel „Anna“. Wer den Link öffnet, sieht dann „Tour von Anna“. Du kannst das Feld auch leer lassen.</p>'
             '<p>Danach öffnet sich das Teilen-Menü von Android. Wähle deine Nachrichten-App und schicke den Link an die Menschen, die dich verfolgen sollen.</p>'
             '[[shots:teilen-knopf,teilen-link]]'),
            ('Während der Tour',
             '<p>Solange du teilst, ist das Zeichen grün. Etwa alle zwei Minuten schickt dein Handy die neuen Punkte, im Stillstand seltener. Deine Aufzeichnung hängt nicht davon ab, sie läuft genauso weiter wie sonst.</p>'
             '<p>Ohne Netz steht unter der Navigation „Standort · wartet auf Netz“. Die Punkte gehen nicht verloren: Sobald das Handy wieder Empfang hat, schickt es sie nach.</p>'
             '[[shots:teilen-aktiv,teilen-wartet]]'),
            ('Was die anderen sehen',
             '<p>Die Seite zeigt deinen Weg auf der Karte, ob du unterwegs bist oder pausierst, wann der letzte Standort kam, Strecke und Höhenmeter und den Akkustand deines Handys. Folgst du einem Plan, sehen sie auch den geplanten Weg, wie weit es noch ist und wann du ungefähr ankommst.</p>'
             '<p>Die Seite ist kein Notruf-Dienst. Im Notfall gilt 112.</p>'
             '[[shots:teilen-seite]]'),
            ('Das Teilen beenden',
             '<p>Tippe noch einmal auf das grüne Zeichen und wähle „Teilen beenden“. Dann werden die Daten auf dem Server sofort gelöscht, und der Link funktioniert nicht mehr. Über „Link nochmal teilen“ schickst du denselben Link an weitere Menschen. Beides findest du auch in den Einstellungen der Tour (⚙).</p>'
             '<p>Wenn du die Tour beendest, endet auch das Teilen. Die anderen sehen danach noch 12 Stunden deinen ganzen Weg, dann löscht der Server alles. Für die nächste Tour gibt es einen neuen Link.</p>'
             '[[shots:teilen-beendet]]'),
            ('Wer was lesen kann',
             '<p>Dein Handy verschlüsselt alles, bevor es abgeschickt wird. Der Schlüssel steckt nur in dem Link, den du verschickst. Unser Server sieht nur verschlossene Daten und kann weder deinen Ort noch deinen Namen lesen. Wer den Link hat, sieht deine Tour, auch wenn der Link weitergeleitet wurde. Schicke ihn deshalb nur an Menschen, denen du vertraust. <a href="/datenschutz/">Mehr im Datenschutz</a>.</p>'),
        ],
    ),
]

HELP_EN = [
    (
        'share-location', 'Share your location',
        'Others see in their browser where you are on your way – only as long as you want.',
        'share location link family follow live tour stop sharing viewer',
        [
            ('What it is for',
             '<p>You are out alone in the mountains and someone at home wants to know where you are. With “Share location” you send a link, for example by Signal or WhatsApp. Whoever opens it sees in their browser your way so far, your last position and when it arrived. Nobody needs an app or an account for it.</p>'
             '<p>Sharing works one way only: you do not see the others, and there are no groups.</p>'),
            ('Share your location',
             '<p>Start your outing. In navigation, the share symbol sits on the right above the ⚙. Tap it. The first time, OnPath asks for the name for the page, for example “Anna”. Whoever opens the link then sees “Tour of Anna”. You can also leave the field empty.</p>'
             '<p>Android’s share menu opens next. Choose your messaging app and send the link to the people who should follow you.</p>'
             '[[shots:teilen-knopf,teilen-link]]'),
            ('During the outing',
             '<p>While you share, the symbol is green. Your phone sends the new points about every two minutes, less often while you stand still. Your recording does not depend on it and carries on as usual.</p>'
             '<p>Without a connection, “Location · waiting for network” appears below the navigation. No points are lost: as soon as the phone has reception again, it sends them.</p>'
             '[[shots:teilen-aktiv,teilen-wartet]]'),
            ('What the others see',
             '<p>The page shows your way on the map, whether you are moving or taking a break, when the last position arrived, distance and climbing, and your phone’s battery level. If you follow a plan, they also see the planned route, how far you still have to go and roughly when you will arrive.</p>'
             '<p>The page is not an emergency service. In an emergency, call 112.</p>'
             '[[shots:teilen-seite]]'),
            ('Stop sharing',
             '<p>Tap the green symbol again and choose “Stop sharing”. The data on the server is deleted at once and the link no longer works. “Share link again” sends the same link to more people. You also find both in the tour settings (⚙).</p>'
             '<p>When you finish the outing, sharing ends too. The others still see your whole way for 12 hours, then the server deletes everything. Your next outing gets a new link.</p>'
             '[[shots:teilen-beendet]]'),
            ('Who can read what',
             '<p>Your phone encrypts everything before it is sent. The key is only in the link you send. Our server sees locked data only and cannot read your position or your name. Whoever has the link sees your outing, also if the link was forwarded, so send it only to people you trust. <a href="/privacy/">More in the privacy notes</a>.</p>'),
        ],
    ),
]
