"""Public help for round-trip suggestions and multi-day planning."""

HELP_DE = [
    (
        'rundtouren', 'Eine passende Rundtour finden',
        'Startpunkt wählen, Wünsche einstellen und eine Runde übernehmen.',
        'Rundtour Rundgang Vorschläge Rundwanderung Zeit Höhenmeter Einkehr Wasser',
        [
            ('Eine Runde für den freien Nachmittag',
             '<p>Du hast ein paar Stunden Zeit und möchtest wieder an deinem Startpunkt ankommen. OnPath berechnet Rundtouren passend zu deiner Aktivität, deiner gewünschten Dauer und den Höhenmetern. Das funktioniert auf dem Handy und im Browserplaner.</p>'),
            ('Start und Wünsche wählen',
             '<p>Beginne mit einem leeren Plan. Halte deinen Startpunkt auf der Karte gedrückt und wähle <strong>„Rundtour von hier“</strong>. Prüfe die Aktivität und beim Wandern die Schwierigkeit.</p>'
             '<p>Stelle einen Bereich für die Dauer ein, zum Beispiel zwei bis drei Stunden, und wie viel Aufstieg du dir vornehmen möchtest. Als Ziel kannst du etwa Wasser, Aussicht oder eine Einkehr wählen.</p>'),
            ('Die Vorschläge durchsehen',
             '<p>Die Ergebnisse stehen als Karten nebeneinander. Wische durch die Reihe und wähle eine Runde aus. Auf der Karte siehst du jeweils den Verlauf des ausgewählten Vorschlags.</p>'
             '<p>Entfernung, Dauer, Aufstieg und die kurze Beschreibung helfen bei der Auswahl. Schau auch auf die Hinweise zu Straßenabschnitten und Wegen. Über „Wunsch ändern“ kannst du die Suche anpassen.</p>'),
            ('Die Runde übernehmen',
             '<p>Mit <strong>„Übernehmen“</strong> wird der Vorschlag zu deinem Plan. Prüfe den Weg, das Höhenprofil und die Streckenhinweise. Du kannst Zwischenstopps ergänzen oder den Verlauf ändern.</p>'
             '<p>Warte vor einer Offline-Tour, bis die benötigten Karten und Daten vollständig geladen sind. Dann kannst du starten. <a href="/hilfe/offline/#vorbereiten">Offline-Tour vorbereiten</a>.</p>'),
            ('Wenn keine passende Runde erscheint',
             '<p>Versuche einen anderen Startpunkt oder einen größeren Zeitbereich und prüfe die gewählte Aktivität. Die Vorschläge hängen vom nutzbaren Wegenetz und den verfügbaren Gebietsdaten ab. Fehlende Daten müssen zunächst über eine Internetverbindung geladen werden.</p>'),
        ],
    ),
    (
        'mehrtagestouren', 'Eine Mehrtagestour planen',
        'Eigene Pläne und GPX-Tracks verbinden, Tagesenden festlegen und Hotels einbauen.',
        'Mehrtagestour Mehrtagesplaner Etappen GPX anhängen Hotel Übernachtung graue Punkte Mond',
        [
            ('Eine Reise wächst aus deiner Route',
             '<p>Du möchtest mit dem Rad von München nach Venedig. Die Richtung steht, die Tagesetappen dürfen sich beim Planen ergeben. Im Browserplaner machst du aus einer Route eine Mehrtagestour. Auf dem gekoppelten Handy wählst du später den jeweiligen Tag.</p>'
             '<p>Das Beispiel funktioniert genauso für eine mehrtägige Wanderung. Öffne <a href="https://plan.onpath.earth/">den Browserplaner</a> und wähle <strong>„Mehrtagestour planen“</strong>.</p>'),
            ('Mit einem eigenen Plan oder einer GPX-Datei beginnen',
             '<p>Im ersten Schritt wählst du <strong>„GPX-Track laden“</strong> oder <strong>„Gespeicherte Route öffnen“</strong>. So wird eine vorhandene Strecke zur Grundlage deiner Reise.</p>'
             '<p>Du hast deine Route bereits selbst auf der Karte geplant? Öffne das Plan-Menü und wähle <strong>„Als Mehrtagestour planen“</strong>. Alternativ speicherst du deinen Plan und öffnest ihn im Mehrtagesplaner.</p>'
             '<p>Bei einem GPX-Track kannst du Anfang und Ende auf der Linie oder im Höhenprofil verschieben. Ausgesparte Teile werden grau. Übernimm den gewünschten Abschnitt als bearbeitbaren Plan und prüfe den berechneten Verlauf. Die ursprüngliche Datei bleibt erhalten.</p>'),
            ('Eine weitere Strecke anhängen',
             '<p>Dein erster GPX-Track reicht nur bis zum Brenner? Unter <strong>„Noch etwas anhängen“</strong> lädst du die nächste Datei, etwa vom Brenner nach Venedig. Schneide sie bei Bedarf zu und wähle <strong>„An die Route anhängen“</strong>. Auch eine gespeicherte Route lässt sich hier ergänzen.</p>'
             '<p>OnPath setzt die zusätzliche Strecke hinter das bisherige Ende. Läuft der geladene Track in die andere Richtung, dreht OnPath ihn für den Anschluss um, wenn sein Ende näher liegt. Prüfe den Gesamtweg und die Verbindung zwischen den Abschnitten. Die Tagesetappen legst du anschließend fest.</p>'),
            ('Tage und tägliche Grenzen festlegen',
             '<p>Wähle <strong>„Weiter: Tage festlegen“</strong> und gib deiner Reise einen Namen. Unter „Höchstens pro Tag“ kannst du Grenzen für Dauer und Aufstieg eintragen. Daraus schlägt OnPath eine Tageszahl vor. Mit Plus und Minus passt du sie an.</p>'
             '<p>Nehmen wir sechs Tage. Nach „Fertig“ siehst du die Etappen mit Entfernung, Aufstieg und geschätzter Zeit. Liegt ein Tag über einer deiner Grenzen, hebt OnPath den betreffenden Wert orange hervor.</p>'),
            ('Der Clou mit den schwebenden grauen Tagesenden',
             '<p>Für sechs Tage schlägt OnPath fünf Übernachtungsstellen vor. Die <strong>hellgrauen Mondsymbole</strong> zeigen, wo deine Tage vorläufig enden könnten. Diese Nächte sind noch offen.</p>'
             '<p>Änderst du den Weg, die Tageszahl oder eine Übernachtung, verteilt OnPath die noch offenen Tagesenden neu. Dabei berücksichtigt es deine Grenzen für Zeit und Aufstieg, soweit die Strecke das zulässt. Ohne Grenzen orientiert sich die Verteilung an ähnlich langen Tagesetappen nach Zeit.</p>'
             '<p>Die grauen Symbole zeigen mögliche Tagesenden auf dem bereits berechneten Weg. Du kannst deine Reise damit Schritt für Schritt festlegen, während OnPath die offenen Etappen neu verteilt.</p>'),
            ('Aus einem Vorschlag wird deine Übernachtung',
             '<p>Ein Ort gefällt dir als Tagesziel? Klicke dort auf die Route und wähle <strong>„Übernachtung hier“</strong>. Das Symbol wird ein <strong>blauer Mond</strong>. Diese Stelle ist jetzt von dir festgelegt. Die übrigen grauen Vorschläge verteilen sich darum herum neu.</p>'
             '<p>Du kannst auch einen grauen Mond an die gewünschte Stelle ziehen. Beim Ablegen wird daraus eine blaue Übernachtung. Beim Neuverteilen der grauen Vorschläge bleiben deine blauen Übernachtungen und hinterlegten Hotels an ihren gewählten Orten.</p>'),
            ('Dein Hotel in die Route aufnehmen',
             '<p>Für die zweite Nacht hast du ein Hotel gebucht. Öffne das Übernachtungssymbol und wähle <strong>„Hotel hinterlegen“</strong>. Suche den Namen oder füge die Adresse beziehungsweise einen Google-Maps- oder Booking-Link ein. Wähle den passenden Treffer und prüfe seinen Standort. Falls der Link keinen passenden Treffer ergibt, suche mit Hotelname oder Adresse.</p>'
             '<p>Das Symbol wird zum <strong>grünen Bett</strong>. OnPath führt die Route bis zum Hotel und berücksichtigt den zusätzlichen Weg in der Tagesetappe.</p>'
             '<p>Hast du zuerst das Hotel über die Ortssuche gefunden, wähle <strong>„Hotel für diese Tour“</strong> und ordne es einer Nacht zu. Die nächstgelegene Nacht ist vorausgewählt.</p>'
             '<p>Ändern sich deine Pläne, kannst du „Hotel ändern“ oder „Hotel entfernen“ wählen. Beim Entfernen des Hotels bleibt die Übernachtung als blauer Mond auf der Route bestehen. Mit „Übernachtung entfernen“ gibst du auch das Tagesende wieder frei.</p>'),
            ('Speichern und auf dem Handy einen Tag wählen',
             '<p>Speichere die Mehrtagestour wie jeden anderen Plan. Über die <a href="/hilfe/route-planen/#koppeln">Kopplung von Browser und Handy</a> kommt sie in deine App. Öffne dort die Tour und wähle eine Tagesetappe.</p>'
             '<p>Beim ersten Öffnen fragt OnPath, ob du die Karten für die ganze Tour, zunächst nur einen Tag oder später laden möchtest. Die geschätzte Datenmenge steht dabei. Im Mobilfunk wartet der Download der ganzen Tour auf WLAN. Warte vor dem Start ohne Netz, bis die benötigten Daten vollständig geladen sind.</p>'
             '[[shots:mehrtage-handy]]'
             '<p>Morgens wählst du zum Beispiel Tag 2 und tippst auf <strong>„Tag 2 fahren“</strong>. Prüfe den Tagesplan und starte anschließend mit „Los geht’s“. Der Knopf heißt auch bei einer Wanderung „Tag 2 fahren“.</p>'
             '<p>Für mehrere aufeinanderfolgende Tage wählst du den ersten und hältst den letzten gewünschten Tag gedrückt. Änderungen am Tagesplan werden auch in die gesamte Mehrtagestour übernommen.</p>'),
        ],
    ),
]

HELP_EN = [
    (
        'round-trips', 'Find a round trip that suits you',
        'Choose a start, set your preferences and turn a suggestion into a plan.',
        'round trip loop suggestions hiking cycling time ascent cafe water',
        [
            ('A loop for a free afternoon',
             '<p>You have a few hours and want to finish where you started. OnPath calculates round trips for your activity, preferred duration and climbing. You can do this on your phone and in the browser planner.</p>'),
            ('Choose your start and preferences',
             '<p>Begin with an empty plan. Press and hold your starting point on the map and choose <strong>“Round trip from here”</strong>. Check the activity and, for hiking, the difficulty.</p>'
             '<p>Set a duration range, such as two to three hours, and how much climbing you want. You can also choose destinations such as water, a view or a place for a break.</p>'),
            ('Browse the suggestions',
             '<p>The results appear as cards side by side. Swipe through the row and select a trip. The map shows the course of the selected suggestion.</p>'
             '<p>Distance, time, climbing and a short description help you choose. Check the road and path notes too. Use “Change wish” to adjust your search.</p>'),
            ('Use the loop as your plan',
             '<p>Choose <strong>“Use this”</strong> to turn the suggestion into your plan. Check the course, elevation profile and route notices. You can add stops or change the route.</p>'
             '<p>Before an offline outing, wait until the required maps and data have finished downloading. Then you can set off. <a href="/help/offline/#prepare">Prepare an offline outing</a>.</p>'),
            ('If no suitable loop appears',
             '<p>Try a different start or a wider time range and check your activity. Suggestions depend on the usable paths and area data available. Missing data needs an internet connection to download first.</p>'),
        ],
    ),
    (
        'multi-day-tours', 'Plan a multi-day tour',
        'Combine plans and GPX tracks, choose overnight stops and add hotels.',
        'multi day tour stages GPX append join hotel overnight grey points moon',
        [
            ('Build a journey around your route',
             '<p>You want to cycle from Munich to Venice. You know the direction, and the daily stages can take shape as you plan. Turn a route into a multi-day tour in the browser planner. Later, choose each day on your paired phone.</p>'
             '<p>The example works just as well for a multi-day hike. Open <a href="https://plan.onpath.earth/">the browser planner</a> and choose <strong>“Plan a multi-day tour”</strong>.</p>'),
            ('Start with your own plan or a GPX file',
             '<p>In the first step, choose <strong>“Load GPX track”</strong> or <strong>“Open saved route”</strong>. An existing route can become the basis of your journey.</p>'
             '<p>Already planned your route on the map? Open the plan menu and choose <strong>“Plan as multi-day tour”</strong>. You can also save your plan and open it in the multi-day guide.</p>'
             '<p>For a GPX track, move the start and end on the line or in the elevation profile. Excluded sections turn grey. Turn the section you want into an editable plan and check the calculated route. Your original file is kept.</p>'),
            ('Append another route',
             '<p>Does your first GPX track end at the Brenner Pass? Under <strong>“Append more”</strong>, load the next file, perhaps from the Brenner Pass to Venice. Trim it if needed and choose <strong>“Append to the route”</strong>. You can also add a saved route here.</p>'
             '<p>OnPath adds the extra route after the current end. If a loaded track runs the other way, it reverses the track when its end is closer to the connection. Check the whole route and the join. Choose the daily stages afterwards.</p>'),
            ('Set your days and daily limits',
             '<p>Choose <strong>“Next: set the days”</strong> and name your journey. Set daily limits for time and climbing. OnPath suggests a number of days from those limits. Adjust it with plus and minus.</p>'
             '<p>Suppose you choose six days. After “Done”, the overview shows distance, climbing and estimated time for each stage. If a day exceeds a limit, OnPath highlights that value in orange.</p>'),
            ('How the floating grey day ends work',
             '<p>For six days, OnPath suggests five overnight stops. The <strong>light grey moon symbols</strong> show where each day could end. Those nights are still open.</p>'
             '<p>Change the route, the number of days or an overnight stop, and OnPath redistributes the day ends that are still open. It considers your time and climbing limits where the route allows. Without limits, it aims for days of similar duration.</p>'
             '<p>The grey symbols suggest day ends along the route already calculated. You can settle your plans a little at a time while OnPath redistributes the open stages.</p>'),
            ('Choose an overnight stop',
             '<p>Found a place where you want to end the day? Click the route there and choose <strong>“Overnight stop here”</strong>. The symbol becomes a <strong>blue moon</strong>. You have chosen that location, and the remaining grey suggestions redistribute around it.</p>'
             '<p>You can also drag a grey moon to the place you want. On release it becomes a blue overnight stop. Your blue overnight stops and hotels stay where you chose them when OnPath redistributes the grey suggestions.</p>'),
            ('Bring your hotel into the route',
             '<p>You have booked a hotel for the second night. Open the overnight symbol and choose <strong>“Add hotel”</strong>. Search by name or paste its address, a Google Maps link or a Booking link. Choose the matching result and check its location. If a link gives no suitable result, search by hotel name or address.</p>'
             '<p>The symbol becomes a <strong>green bed</strong>. OnPath routes you to the hotel and includes the extra distance in the daily stage.</p>'
             '<p>If you find the hotel through place search first, choose <strong>“Hotel for this tour”</strong> and assign it to a night. The nearest night is preselected.</p>'
             '<p>If your plans change, choose “Change hotel” or “Remove hotel”. Removing the hotel keeps an overnight stop on the route as a blue moon. “Remove overnight stop” also frees that day end.</p>'),
            ('Save and choose a day on your phone',
             '<p>Save the multi-day tour like any other plan. <a href="/help/planning/#pair">Pair your browser and phone</a> to bring it into the app, then open the tour and select a day.</p>'
             '<p>On first opening, OnPath asks whether to download maps for the whole tour, one day or later. It shows the estimated download size. On mobile data, the whole-tour download waits for Wi-Fi. Before setting off offline, wait for the required data to finish downloading.</p>'
             '[[shots:mehrtage-handy]]'
             '<p>In the morning, select day 2 and choose <strong>“Ride day 2”</strong>. Check the day’s plan, then start with “Let’s go”. The button also says “Ride day 2” for a hike.</p>'
             '<p>To follow consecutive days together, select the first and press and hold the last day you want. Changes to a day’s plan are also written back into the whole multi-day tour.</p>'),
        ],
    ),
]
