"""Approved public product copy. No internal plans or marketing research."""
ARTICLES = {
 '/hiking/': ('Time for your own trail.', 'Plan a walk that suits you, from a local woodland loop to a day in the hills.', [
 ('Choose a destination, find a route', 'Search for a village, a hut or another destination. Add stops you want to visit. OnPath connects the points along paths and shows distance, climbing and estimated time.'),
 ('Choose the difficulty', 'For hiking, choose a level from T1 to T5. The planner avoids paths marked above that level and excludes via ferratas. This relies on the available map data: weather, closures, conditions and your own experience still matter.'),
 ('Change your mind along the way', 'A hut is closed or you want a shorter way home? Edit the remaining plan and continue. Your recording keeps going. With the required maps downloaded, this also works without a connection.'),
 ('An arrival time that adapts', 'After about 15 minutes and one kilometre, the estimate starts using your pace on this outing, separately for uphill, level and downhill sections. It remains an estimate.')]),
 '/cycling/': ('A ride that suits you.', 'A short evening ride, a day out or a route from your local cycling group.', [
 ('Choose your bike', 'Select Bike, Gravelbike, E-bike, MTB or E-MTB. The activity influences the route. Check surfaces, climbing and any notices about steps, steep sections, pushing or ferries before setting off.'),
 ('Routes from your club or a tour portal', 'If your cycling club or a tour portal provides a GPX file, open it in OnPath and follow the route. A GPX file contains the course of a tour. You do not need an OnPath account.'),
 ('Make room for a stop', 'Add a café or change the way home in a plan made in OnPath. Stop safely before using your phone. Your recording continues while you edit.'),
 ('Use an existing route', 'Imported GPX tracks can be followed but cannot yet be turned into freely editable OnPath plans. Download the maps before your ride.')]),
 '/about/': ('Why I am building OnPath.', 'I love being outdoors – and wanted an app that makes planning and changing a tour easy.', [
 ('Who I am', '<img src="/assets/christian.webp" alt="Christian Neuhaus hiking in the mountains" class="me" width="400" height="400">I am Christian Neuhaus and a bit of a nerd: for more than 30 years I have lived and worked with IT. I like trying out new things, build small devices with sensors and cameras, and show children how programming works. Most of all, though, I like being outside – on foot in the mountains or on my bike. OnPath brings both together. More about me and my tinkering: <a href="https://44-2.de/">44-2.de</a>'),
 ('It started with my own tours', 'I used Komoot happily for many years. On the way, though, the same things kept bothering me: changing the route on the phone, planning again without signal, simply carrying on after a break. Once my plan even changed in my pocket. OnPath is my attempt to make this simpler. It is about your way – no profile, feed or leaderboards.'),
 ('Robust means: no surprises', 'A new route only comes after asking. To change things, you switch to planning on purpose. Every recorded point is saved at once. So a wrong tap or a dead spot does not mess up your day. That is the aim. OnPath is still young and mainly tested by me so far; more testing will show whether it works on your phone and your paths.'),
 ('Built with AI, tested on tours', 'AI helps me write and check OnPath’s code, allowing me to develop the project on my own. On my walks and rides I try out how it works in everyday use. That shapes the next improvements: what needs to work easily on the way, and where should the app stay out of the way?'),
 ('Open and fair', 'The app’s blueprint is public (open source): anyone can see how it works and help. The maps come from the community project OpenStreetMap. Planning, navigating and recording stay free. Later paid extras are meant to cover costs, pay for my work and include a donation; how this is split should be visible. <a href="/whats-next/">More on funding</a>.')]),
 '/whats-next/': ('Growing one useful step at a time.', 'What you can try today, and what is still being developed.', [
 ('Today: the Android app', 'Plan, navigate, edit your own routes while recording, search places and use GPX files. Prepared areas work offline. The interface supports German and English. This is still an early test version. Phase 1 currently requires a personal invitation and approval from Christian. A closed test group and the public release will follow. <a href="/try/">The three phases and your access →</a>'),
 ('New: plan on a computer', 'At <a href="https://plan.onpath.earth/">plan.onpath.earth</a> you plan your tour on a big map – free, without an account and without installing anything. The routes are the same as in the app. Then point your phone camera at the QR code and the plan is on your phone.'),
 ('New: spoken directions', '<span class="tag">In the app</span> Hear turn instructions without looking at the screen: OnPath announces turns briefly and in good time – only where you could go wrong. The voice comes from your phone and needs no connection.'),
 ('In testing: link browser and phone', 'Scan the code on the computer screen once with your phone camera: saved plans then reach both devices by themselves – encrypted and without an OnPath account. You can disconnect at any time.'),
 ('The core stays free', 'Planning, navigation and offline route changes with downloaded maps remain free. Your tours can be kept as normal files and used in other apps.'),
 ('Costs, development and a donation', 'Future paid extras should help cover operating costs, compensate some development work and contribute a share to a charitable organisation. A transparent breakdown of income, costs, the developer’s share and donations is planned. Prices, amounts, the organisation and payment method are undecided. There is nothing to buy on this site.')]),
 '/try/': ('Try OnPath on familiar paths.', 'Walkers and leisure cyclists can help make OnPath more useful in everyday use.', [
 ('An early version', 'You need Android 8 or newer. OnPath has mainly been used by its developer so far. There is no iPhone version yet. Begin with a short route you know.'),
 ('Phase 1: personal invitations', 'Participation currently requires an individual invitation link and approval from Christian. The closed Google Play test group is the next step. Taking part in the test is free.'),
 ('Useful feedback does not need technical knowledge', 'Tell the developer what you were trying to do, what happened and what you expected. Your phone model and app version help. An unclear instruction is useful feedback too.'),
 ('For technically experienced users', 'Early APK releases and discussions are available in the app’s GitHub repository. The GitHub and future Play builds may use different signatures: back up your tours before changing between them. OnPath itself does not need an account.')]),
 '/project/': ('Open code. Clear information.', 'OnPath is an independent project by Christian Neuhaus.', [
 ('Current status', 'As of 30 October 2026, checked against app version 0.13.1 and the planner at plan.onpath.earth. The website is still a test version and hidden from search engines; the legal notice and privacy notes are reviewed before the public launch. Phase 1 currently requires a personal invitation and approval from Christian. The closed test group is the next step; see the Try page for access.'),
 ('Image credits', 'Home page photograph: Christian Neuhaus, near Vellau (South Tyrol). Portrait: Christian Neuhaus, private. The screen images are real captures of the app (with a simulated ride) and of the planner. The logo follows the original app artwork.'),
 ('Code and maps', 'App source: happychriss/OnPath, Apache 2.0. Map data © OpenStreetMap contributors. Routing uses BRouter. Manrope font © The Manrope Project Authors, SIL Open Font License 1.1.'),
 ('Independent', 'OnPath is not affiliated with Komoot or Google. No endorsement or partnership is claimed.')]),

}
HELP_EN = [('getting-started',
  'Your first outing',
  'Install, prepare an area and plan a short route.',
  'start install location android',
  [('Prepare at home',
    'OnPath needs Android 8 or newer. Phase 1 requires a personal invitation and approval from Christian; see <a '
    'href="/try/">test access</a>. Allow location access for navigation and recording. Plan while connected, '
    'preferably at home on Wi-Fi. OnPath downloads the required maps and its place and address database automatically. '
    'Wait for the download to finish and check Settings → Offline maps. A new area can take a few minutes. <a '
    'href="/help/offline/#prepare">Offline preparation in detail →</a>'),
   ('Plan a familiar route',
    'Choose your activity. Press a little longer on your destination and choose “Go here from my location” to plan from your location. '
    'A short tap does not set a new destination, preventing accidental changes. To start elsewhere, hold the start '
    'point and choose “Start here”, then add your destination and stops. Check distance, climbing, time and route '
    'hints. Wait for the required maps to finish downloading and begin with a short, familiar route.'),
   ('Start navigation',
    'Start on a short, familiar route. The route is protected against accidental map taps during navigation. Switch '
    'deliberately to editing when you want to change it.')]),
 ('offline',
  'Without a connection',
  'Download your maps before you head out.',
  'map internet download wifi offline',
  [('What works offline',
    'OnPath automatically downloads maps for your route and its surroundings while you plan, including its place and '
    'address database. In fully downloaded areas, you can search addresses and places, plan, navigate and recalculate '
    'routes directly on your phone. Additional online search supplements local results; it is not required for local '
    'search. Google Maps is a separate service with its own downloaded areas and offline capabilities.'),
   ('Before leaving',
    'Plan while connected, preferably on Wi-Fi. Wait for automatic downloads to finish and include larger detours and '
    'the return route. Check Settings → Offline maps. Try search and a small route change with mobile data and Wi-Fi '
    'switched off, leaving location enabled. Downloaded areas stay on your phone. A detour beyond them needs a '
    'connection to fetch more data; the initial download must also finish before you leave reception.'),
   ('What still needs internet',
    'New areas, additional online search and Google Maps information need a connection. Preparing a new area can take '
    'a few minutes. Missing data cannot be downloaded in a dead zone.')]),
 ('planning',
  'Plan your own route',
  'Set points and check the way ahead.',
  'plan points difficulty climbing surface',
  [('Choose an activity',
    'Choose Bike, Gravelbike, E-bike, MTB, E-MTB or Hike. OnPath adapts route choices to your activity, considering '
    'surfaces and busy roads for cycling. A touring bike is planned differently from a gravel bike or MTB. Hiking also '
    'has a difficulty setting using the SAC hiking scale. <a href="#difficulty">Difficulty levels explained →</a>'),
   ('Set and change points',
    'Press a little longer on the map and choose an action, such as “Go here from my location” to plan from your location. A short tap '
    'does not set a new destination. Hold an existing point to open its actions. To move it on the map, delete and add '
    'it again. In the expanded point list, drag stops into order or remove them. Undo changes, reverse the route or '
    'make it a round trip.'),
   ('Check the route',
    'Pull the route panel up to inspect the elevation profile, surfaces and path types. Depending on activity, route '
    'hints include steep sections, pushing, steps, demanding hiking sections, ferries, construction, fords and certain '
    'barriers for bikes. Tap a hint to see the affected places on the map. Check ferry timetables yourself; '
    'construction may mean a closure. Hints depend on available map entries and are not a complete list of current '
    'hazards. A gap to an unreachable point is not a confirmed usable path. Check that point and choose another '
    'approach if needed. Signs and conditions on the ground take priority.'),
   ('Choose the difficulty: SAC T1 to T5',
    'OnPath uses the Swiss Alpine Club’s SAC hiking scale. Choose T1 (hiking), T2 (mountain hiking), T3 (demanding '
    'mountain hiking), T4 (alpine hiking) or T5 (demanding alpine hiking). Higher grades require more sure-footedness, '
    'a head for heights, navigation skills and alpine experience. Planning avoids paths above your level and via '
    'ferratas. If a route still contains a section marked as harder, OnPath shows a hint. OpenStreetMap grades can be '
    'missing or outdated. Check weather, conditions and your own experience; signs and closures on the ground take '
    'priority.'),
   ('Map colours and signed routes',
    'The display adapts to your activity. Green highlights help you recognise suitable paths. Signed cycling and '
    'hiking routes are also shown with their names. Long-distance routes, including national and international '
    'networks such as EuroVelo, have a pink-and-green marking. Zoomed out, you mainly see long-distance routes. '
    'Regional and local routes appear as you zoom in. Follow a longer route or combine local paths into an outing. '
    'Cycling maps also indicate surfaces. Colours help with planning; check the route, difficulty and signs too.'),
   ('Plan on a computer and transfer to your phone',
    '<ol><li>Open <a href="https://plan.onpath.earth/">plan.onpath.earth</a> on your computer – no account, nothing '
    'to install.</li><li>Set start, destination and stops with the mouse, or open a GPX file. You see time, elevation '
    'profile and notes as in the app.</li><li>Click “Share” and scan the QR code with your phone camera. The route '
    'opens in OnPath.</li><li>Let the phone download the maps for the route before you head out without '
    'reception.</li></ol><p>Often plan on the computer? Pair browser and phone once – your saved routes are then on '
    'both. <a href="#pair">How to pair →</a></p>'),
   ('Pair browser and phone',
    '<p>Pair once – then your saved routes are in the browser and on your phone, both ways.</p>'
    '<h3>Pair</h3><ol><li>In the browser: click “Pair phone” at the top, then “Pair phone” again in the window. A QR '
    'code appears.</li><li>On your phone: open OnPath, tap ☰ → “Pair with browser” → “Open camera” and scan the '
    'code.</li><li>OnPath shows six check digits. If they match the browser, tap “Pair”.</li></ol>[[shots:web-handy,web-koppeln,app-koppeln]]'
    '<h3>Your routes on both</h3><p>Save a route in the browser and it appears in the app under “My routes”, marked '
    '“New” or “Changed”. What you save on your phone shows up in the browser under “My routes”. They sync while OnPath '
    'is open on the phone and while the browser page is open. Recorded outings stay on your phone.</p>[[shots:app-verbunden,app-routen]]'
    '<h3>Unpair</h3><p>In the app: Settings → Browser sync → “Unpair”. Or in the browser: “Phone” → “Unpair”. Your '
    'routes stay on both devices.</p>[[shots:app-trennen]]'
    '<p>End-to-end encrypted, no account. Keep the QR code to yourself – whoever scans it sees your saved routes.</p>')]),
 ('change-route',
  'Change the route along the way',
  'Add a stop and keep your recording.',
  'edit change detour route navigation',
  [('Switch to editing',
    'Slide “Stop” at the bottom of the screen aside. This opens the options to pause, end the outing or edit the '
    'route. The swipe alone does not end recording. Recording continues while you change the plan.'),
   ('Adjust the next part',
    'Remove a stop or add a new destination and check the new route. Recalculation works offline when all the required '
    'areas are ready.'),
   ('Continue from here',
    'Tap “Continue” to return to navigation. Points already visited are skipped. If you leave the route, OnPath asks '
    'before calculating a new one; the original stays visible in grey. Imported GPX tracks are not yet freely editable '
    'plans.')]),
 ('places',
  'Places and Google Maps',
  'Find a café, check details and plan the way there.',
  'google maps search photon address hut cafe',
  [('Find a place',
    'Search a name or address. OnPath searches its own place and address database on your phone, downloaded '
    'automatically with the maps. It includes streets, house numbers, villages, huts, peaks and stations. In fully '
    'downloaded areas this works without reception. Online results are added when connected. New areas need a '
    'connection to download; not every place or house number is recorded.'),
   ('Check details in Google Maps',
    'Open the place details in OnPath and use the Google Maps action to check opening hours, photos or reviews. Return '
    'to OnPath and add the place as a stop or destination. OnPath calculates the route for your activity.'),
   ('Bring a place from Google Maps',
    'Open the place in Google Maps, choose Share and select OnPath. Check the marked location and use it as your '
    'start, stop or destination. This transfers the place, not a complete Google route. Short links may need a '
    'connection to resolve.'),
   ('Online search and privacy',
    'Online search sends the query and a rough location to Photon. When you open Google Maps, Google’s own terms and '
    'privacy policy apply. Opening hours are not guaranteed to be current.'),
   ('Use a meeting point from a message',
    'Someone sent you a map link or location, for example in Signal? Share the link or message with OnPath through '
    'Android’s Share function. Supported formats include Google Maps and OpenStreetMap links, geo: links and '
    'coordinates. Check the marked place, choose it as your destination or stop, and start navigation when ready. '
    'OnPath does not read chats or follow a live location; it uses the shared point. The exact steps depend on the '
    'messaging app and link format, and not every format is supported. Short map links may need internet. If a '
    'position was found from an address, check it carefully.')]),
 ('gpx',
  'Use and save tour files',
  'Take an existing route with you and keep your own.',
  'gpx import export backup file adfc',
  [('What a GPX file contains',
    'It holds the course of a route. Tourist organisations, cycling clubs and other people can provide tours in this '
    'format.'),
   ('Open a route',
    'Download the file to your phone and open it with OnPath. Check the activity and route, then download the maps. '
    'Imported tracks can be followed but are not yet freely editable OnPath plans.'),
   ('Keep your own files',
    'Your tours are stored in the app. OnPath also writes saved routes and completed outings as GPX files in an '
    'accessible folder, Documents/OnPath by default. Choose another folder in Settings → Backup. Android 8–9 needs '
    'storage permission for the default folder; after reinstalling, grant access to a chosen folder again. Use '
    'Android’s file manager to copy the files to a computer, share them or edit them in suitable apps. GPX is an open '
    'format. External edits are not automatically imported back into OnPath. In My routes, export all completed '
    'outings together as a ZIP, then choose a save or sharing destination in Android’s Share dialog. A running '
    'recording is not included. Keep another copy off your phone to protect against device loss. OnPath shows a notice '
    'if an automatic backup fails.')]),
 ('troubleshooting',
  'If something goes wrong',
  'Missing maps, location problems and feedback.',
  'problem error gps battery map diagnostics',
  [('Maps are missing',
    'Check your connection and download status. A first request for a new area may take longer. Missing maps cannot be '
    'fetched without internet.'),
   ('Your position is missing',
    'Check Android’s location setting and the app’s permission. Wait outdoors for a usable position; dense trees, '
    'buildings and valleys can reduce accuracy.'),
   ('Report a problem',
    'Note your phone model, app version, what you tried and what happened. You can create a file with more details in '
    'Settings → Diagnostics → “Send problem report”. Nothing is sent automatically. Check it for private tour '
    'information before sharing.'),
   ('Continue an interrupted outing',
    'OnPath saves recorded points continuously and keeps the navigation state on the phone. If the app is stopped, the '
    'phone restarts or recording is interrupted, reopen OnPath. In the unfinished-tour dialog, choose “Continue” to '
    'carry on, “Save” to keep the recorded part, or “Delete” to discard it deliberately. Time while the phone was off '
    'cannot be recorded afterwards. Repeated interruptions may be caused by Android battery restrictions. <a '
    'href="/help/battery-backup/#background">Check background settings →</a>')]),
 ('navigation',
  'Follow the way',
  'Junctions, arrival time and ending your outing.',
  'left right vibration recording time lock screen',
  [('Before a turn',
    'OnPath shows the next turn and gives cues where you could take the wrong way. Spoken directions name the '
    'direction and way type and may describe what follows. The voice comes from your phone and works without reception '
    'with an installed offline voice. In Settings → Navigation choose speech, vibrations or both and adjust them '
    'separately. First try the audible setup test. One vibration means left, two mean right. How clearly you feel them '
    'depends on your phone and where you carry it. Test on a familiar route.'),
   ('Lock screen and time',
    'The notification shows the next junction and estimated arrival. After about 15 minutes and one kilometre, the '
    'estimate starts adapting to your pace, separately uphill, on level ground and downhill. It remains an estimate. '
    'On the handlebar, the quiet view shows direction, distance and arrival; the map returns before the turn.'),
   ('Finish deliberately',
    'Slide “Stop” aside, choose “End tour”, then “Save”. Keep your outing without questions about uploading photos, '
    'sharing or ratings. Locking the phone does not end recording. If OnPath detected a bus or cable-car section, '
    'review how it should count. <a href="#rides">Review detected rides →</a>'),
   ('Review bus and cable-car sections',
    'OnPath recognises sections likely travelled by vehicle or lift. When finishing, review them and decide whether '
    'they count towards distance and time. Detection is a suggestion for you to check. You can edit ride contributions '
    'again through the saved outing’s menu.')]),
 ('battery-backup',
  'Battery and backup',
  'Keep recording and keep a second copy of your tours.',
  'battery backup zip recycle bin android background',
  [('Background restrictions',
    'If recording stops, check location permissions, notifications and Android’s battery restrictions for OnPath. '
    'Names differ by phone manufacturer. If necessary allow unrestricted background use, then test a short route with '
    'the screen locked.'),
   ('Before a long day',
    'Charge your phone and consider a power bank. Battery use has not been measured across many devices. Screen use '
    'and reception affect runtime.'),
   ('A second copy',
    'OnPath writes additional GPX files to Documents/OnPath by default; choose another folder in Settings → Backup. '
    'Copy important files to a computer or other storage. A copy on the same phone does not protect against losing it. '
    'In My routes export all completed outings together as a ZIP to save or share. Deleted tours stay in the recycle '
    'bin for 30 days. After reinstalling, select the existing backup folder to restore and grant access again. <a '
    'href="/help/gpx/#your-files">Find and export your files →</a>')])]

from legal_content import EN_LEGAL, EN_PRIVACY
ARTICLES['/legal/']=('Legal notice','Provider and contact for OnPath.',EN_LEGAL)
ARTICLES['/privacy/']=('Privacy notice','Website and Android app processing, explained separately.',EN_PRIVACY)
