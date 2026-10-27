"""Approved public product copy. No internal plans or marketing research."""
ARTICLES = {
 '/hiking/': ('Time for your own trail.', 'Plan a walk that suits you, from a local woodland loop to a day in the hills.', [
 ('Choose a destination, find a route', 'Search for a village, a hut or another destination. Add stops you want to visit. OnPath connects the points along paths and shows distance, climbing and estimated time.'),
 ('Choose the difficulty', 'For hiking, choose a level from T1 to T5. The planner avoids paths marked above that level and excludes via ferratas. This relies on the available map data: weather, closures, conditions and your own experience still matter.'),
 ('Change your mind along the way', 'A hut is closed or you want a shorter way home? Edit the remaining plan and continue. Your recording keeps going. With the required maps downloaded, this also works without a connection.'),
 ('An arrival time that adapts', 'After about 15 minutes and one kilometre, the estimate starts using your pace on this outing, separately for uphill, level and downhill sections. It remains an estimate.')]),
 '/cycling/': ('A ride that suits you.', 'A short evening ride, a day out or a route from your local cycling group.', [
 ('Choose your bike', 'Select Bike, Gravelbike, E-bike, MTB or E-MTB. The activity influences the route. Check surfaces, climbing and any notices about steps, steep sections, pushing or ferries before setting off.'),
 ('For ADFC members and ride leaders', 'If your local group provides a GPX file, open it in OnPath and follow the route. A GPX file contains the course of a tour. You do not need an OnPath account. OnPath is independent and is not an official ADFC service.'),
 ('Make room for a stop', 'Add a café or change the way home in a plan made in OnPath. Stop safely before using your phone. Your recording continues while you edit.'),
 ('Use an existing route', 'Imported GPX tracks can be followed but cannot yet be turned into freely editable OnPath plans. Download the maps before your ride.')]),
 '/about/': ('Why I am building OnPath.', 'I am Christian Neuhaus. I enjoy walking and cycling, and want an app that makes planning and changing a route straightforward.', [
 ('It started with my own outings', 'I used Komoot for many years and still respect the work its team has done. On my own trips I wanted easier changes along the way, new routes without mobile reception and a plan that would not change accidentally in my pocket.'),
 ('The outing comes first', 'OnPath focuses on planning, finding your way and changing the remaining route. No social feed, followers or leaderboards. You can still head out with friends and exchange tour files.'),
 ('Built with AI, guided by experience', 'AI helps me write and check code. It lets me turn ideas into an app faster than I could on my own. My own walking and cycling experience guides the decisions; real outings and testing show whether they work. I want to pass that advantage on through open code, free core features and fair funding.'),
 ('What open source means', 'The app’s code is public. People with the right expertise can inspect it and contribute improvements. You do not need programming knowledge to use the app. Public code does not by itself guarantee that software has no bugs.'),
 ('A free core and fair funding', 'Core functions remain free to use. Future paid extras are intended to cover running costs, pay for some of my work and include a donation to a charitable organisation. The aim is to sustain a useful project, rather than build a profit-driven business. Prices and shares have not been set.')]),
 '/whats-next/': ('Growing one useful step at a time.', 'What you can try today, and what is still being developed.', [
 ('Today: the Android app', 'Plan, navigate, edit your own routes while recording, search places and use GPX files. Prepared areas work offline. The interface supports German and English. This is still an early test version.'),
 ('In development: plan on a computer', 'A browser planner should let you prepare a route on a larger screen and transfer it to your phone using a QR code. A technical prototype exists, but no public service or launch date has been confirmed.'),
 ('Planned: link browser and phone', 'The intention is to pair the devices once and exchange plans in both directions, without an additional OnPath account. Saving plans in the browser is also being considered. These features are not available yet.'),
 ('The core stays free', 'Planning, navigation and offline route changes with downloaded maps remain free. Your tours can be kept as normal files and used in other apps.'),
 ('Costs, development and a donation', 'Future paid extras should help cover operating costs, compensate some development work and contribute a share to a charitable organisation. A transparent breakdown of income, costs, the developer’s share and donations is planned. Prices, amounts, the organisation and payment method are undecided. There is nothing to buy on this site.')]),
 '/try/': ('Try OnPath on familiar paths.', 'Walkers, leisure cyclists and ADFC members can help make OnPath more useful in everyday use.', [
 ('An early version', 'You need Android 8 or newer. OnPath has mainly been used by its developer so far. There is no iPhone version, spoken navigation or released browser planner yet. Begin with a short route you know.'),
 ('A Google Play test is being prepared', 'The planned group test will use an invitation through Google Play. The group and invitation links are not ready yet. No payment is planned for that test.'),
 ('Useful feedback does not need technical knowledge', 'Tell the developer what you were trying to do, what happened and what you expected. Your phone model and app version help. An unclear instruction is useful feedback too.'),
 ('For technically experienced users', 'Early APK releases and discussions are available in the app’s GitHub repository. The GitHub and future Play builds may use different signatures: back up your tours before changing between them. OnPath itself does not need an account.')]),
 '/project/': ('Open code. Clear information.', 'OnPath is an independent project by Christian Neuhaus.', [
 ('Current status', 'Product copy checked against the app README and release v0.11.5 on 27 October 2026. Future features are labelled as planned. Real app screenshots and Google Play invitations still need to be added.'),
 ('Image credits', 'Forest photograph: Daniel Seßler / Unsplash, Ramsau bei Berchtesgaden. Used under the Unsplash License. The route illustration is explanatory artwork, not an app screenshot. The logo follows the original app artwork.'),
 ('Code and maps', 'App source: happychriss/OnPath, Apache 2.0. Map data © OpenStreetMap contributors. Routing uses BRouter. Manrope font © The Manrope Project Authors, SIL Open Font License 1.1.'),
 ('Independent', 'OnPath is not affiliated with Komoot, Google or the ADFC. No endorsement or partnership is claimed.')]),

}
HELP_EN = [
 ('getting-started','Your first outing','Install, prepare an area and plan a short route.', 'start install location android', [
 ('Prepare at home','OnPath needs Android 8 or newer. The Google Play group test is being prepared; its invitation is not available yet. Allow the location access needed for navigation and recording. Prepare your area while connected, preferably on Wi-Fi.'),
 ('Plan a familiar route','Choose your activity. Hold a finger on the map to set points. Add your start, destination and any stops. Check distance, climbing, time and route notices. Wait until the required maps are downloaded.'),
 ('Start navigation','Start on a short, familiar route. The route is protected against accidental map taps during navigation. Switch deliberately to editing when you want to change it.')]),
 ('offline','Without a connection','Download your maps before you head out.', 'map internet download wifi offline', [
 ('What works offline','With the required maps and route data downloaded, you can search local places, plan, navigate and recalculate routes on your phone.'),
 ('Before leaving','Plan while connected and let the areas along the route finish downloading. Include possible detours and the return route. Check download status in offline map settings. Test a small change with mobile data and Wi-Fi off, leaving location enabled.'),
 ('What still needs internet','New areas, additional online search and Google Maps information need a connection. Preparing a new area can take a few minutes. Missing data cannot be downloaded in a dead zone.')]),
 ('planning','Plan your own route','Set points and check the way ahead.', 'plan points difficulty climbing surface', [
 ('Choose an activity','Bike, Gravelbike, E-bike, MTB, E-MTB and Hike are available. For hiking choose a difficulty from T1 to T5. The choice relies on recorded map information; check conditions and your own experience too.'),
 ('Set and change points','Hold on the map to add a point. Hold an existing point to see its actions. To move a point on the map, delete and add it again. The expanded list lets you reorder or remove stops. Changes can be undone.'),
 ('Check the route','Inspect the elevation profile, surfaces and notices. A dashed gap to an unreachable destination is not a confirmed usable path. Signs, closures and conditions on the ground take priority.')]),
 ('change-route','Change the route along the way','Add a stop and keep your recording.', 'edit change detour route navigation', [
 ('Switch to editing','Use the deliberate edit control to change the remaining plan. Your current recording keeps running.'),
 ('Adjust the next part','Remove a stop or add a new destination and check the new route. Recalculation works offline when all the required areas are ready.'),
 ('Continue from here','Return to navigation. Points already visited are skipped. If you leave the route, OnPath asks before calculating a new one; the original stays visible in grey. Imported GPX tracks are not yet freely editable plans.')]),
 ('places','Places and Google Maps','Find a café, check details and plan the way there.', 'google maps search photon address hut cafe', [
 ('Find a place','Search a name or address in OnPath. Downloaded maps include streets, villages, huts, peaks and stations. With internet, additional online results are added.'),
 ('Check details in Google Maps','Open the place details in OnPath and use the Google Maps action to check opening hours, photos or reviews. Return to OnPath and add the place as a stop or destination. OnPath calculates the route for your activity.'),
 ('Bring a place from Google Maps','Open the place in Google Maps, choose Share and select OnPath. Check the marked location and use it as your start, stop or destination. This transfers the place, not a complete Google route. Short links may need a connection to resolve.'),
 ('Online search and privacy','Online search sends the query and a rough location to Photon. When you open Google Maps, Google’s own terms and privacy policy apply. Opening hours are not guaranteed to be current.')]),
 ('gpx','Use and save tour files','Take an existing route with you and keep your own.', 'gpx import export backup file adfc', [
 ('What a GPX file contains','It holds the course of a route. Tourist organisations, cycling clubs and other people can provide tours in this format.'),
 ('Open a route','Download the file to your phone and open it with OnPath. Check the activity and route, then download the maps. Imported tracks can be followed but are not yet freely editable OnPath plans.'),
 ('Keep your own files','Choose a folder for GPX copies of saved routes and completed tours. You can also export everything as a ZIP. Keep an additional copy on another device or storage location.')]),
 ('troubleshooting','If something goes wrong','Missing maps, location problems and feedback.', 'problem error gps battery map diagnostics', [
 ('Maps are missing','Check your connection and download status. A first request for a new area may take longer. Missing maps cannot be fetched without internet.'),
 ('Your position is missing','Check Android’s location setting and the app’s permission. Wait outdoors for a usable position; dense trees, buildings and valleys can reduce accuracy.'),
 ('Report a problem','Note your phone model, app version, what you tried and what happened. You can create a diagnostic export in settings. Nothing is sent automatically. Check it for private tour information before sharing.')]),
 ('navigation','Follow the way','Junctions, arrival time and ending your outing.', 'left right vibration recording time lock screen', [
 ('Before a turn','OnPath shows the next junction and vibrates twice for left and three times for right. Try the signals on a familiar route; their visibility depends on your phone and where you carry it. There are no spoken directions yet.'),
 ('Lock screen and time','The notification shows the next junction and estimated arrival. After about 15 minutes and one kilometre, the estimate starts adapting to your actual pace.'),
 ('Finish deliberately','End and save the outing in the app. Locking the phone does not finish it. Recorded points are saved continuously.')]),
 ('battery-backup','Battery and backup','Keep recording and keep a second copy of your tours.', 'battery backup zip recycle bin android background', [
 ('Background restrictions','If recording stops, check location permissions, notifications and Android’s battery restrictions for OnPath. Names differ by phone manufacturer. If necessary allow unrestricted background use, then test a short route with the screen locked.'),
 ('Before a long day','Charge your phone and consider a power bank. Battery use has not been measured across many devices. Screen use and reception affect runtime.'),
 ('A second copy','Copy important GPX files to another device. A copy on the same phone does not protect against losing it. Deleted tours stay in the recycle bin for 30 days. A backup folder can be used after reinstalling if you grant access again.')]),
]

from legal_content import EN_LEGAL, EN_PRIVACY
ARTICLES['/legal/']=('Legal notice','Provider and contact for OnPath.',EN_LEGAL)
ARTICLES['/privacy/']=('Privacy notice','Website and Android app processing, explained separately.',EN_PRIVACY)
