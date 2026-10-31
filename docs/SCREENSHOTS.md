# App screenshots

The German screenshots in `assets/app/v0.13.2/` are owner-supplied captures of
OnPath 0.13.2 (31 October 2026). Original files are 1080 × 2400 PNGs; website
copies are 720 × 1600 WebP images. Only scaling and encoding were applied.
No UI elements, attribution, demo labels or measured values were retouched.
Screenshots use simulated locations and are illustrative, not field-test evidence.

| Website asset | Supplied image |
|---|---|
| plan-wandern-de.webp | 02-plan-wandern.png |
| plan-ebike-de.webp | 03-plan-ebike.png |
| ort-google-maps-de.webp | 04-ort-google-maps.png |
| ankunft-de.webp | 05-ankunft.png |
| ruheanzeige-de.webp | 06-ruheanzeige.png |
| fahrt-de.webp | 07-fahrt.png |
| plan-halten-de.webp | 08b-erste-route-halten.png |
| tour-menue-navigation-de.webp | 09a-unterwegs-navigation.png |
| tour-menue-offen-de.webp | 09b-unterwegs-tourmenue.png |
| umplanen-de.webp | 01-umplanen.png |
| tour-beenden-de.webp | 10a-tour-beenden.png |

The versioned directory prevents stale image caches when the captures change.
All six English showcase screens now use current English captures, including
the arrival screen from the first supplement. English help uses English captures
where supplied; remaining German steps are individually labelled.

The supplied recording-summary images with a 19-minute mountain outing are not
used. Both directions of Google Maps interaction have separate captures:
opening Google Maps from OnPath and sharing a place into OnPath.

## Supplement: 0.13.3 and the current browser planner

`assets/app/v0.13.3/` contains these owner-supplied replacements and additions.
App images are 720 × 1600 website copies of 1080 × 2400 originals; browser
images retain their original 1920 × 1080 resolution. Only resizing and encoding
were applied. Browser images were captured on 31 October 2026; the directory
name identifies the capture batch, not a browser-planner release number.

| Website asset | Supplied image |
|---|---|
| ort-google-maps-de.webp | 09c-unterwegs-ort-halten.png |
| tour-menue-navigation-de.webp | 09a-unterwegs-navigation.png |
| tour-menue-offen-de.webp | 09b-unterwegs-tourmenue.png |
| umplanen-de.webp | 01-umplanen.png |
| navigation-nachher-de.webp | 09e-unterwegs-zurueck.png |
| ort-suche-de.webp | 09b2-unterwegs-suche.png |
| suchtreffer-de.webp | 09c0-unterwegs-suchtreffer.png |
| ankunft-en.webp | 05-ankunft-en.png |
| web-wandern-de.webp | web-planen-1920x1080.png |
| web-qr-de.webp | web-qr-1920x1080.png |

The 0.13.3 tour menu has a compact recording row and a button labelled
“Weiter”. Help text and captions follow that screen; the return-navigation
example now shows the full destination name. Search examples were added to the
places help. The computer-planning section includes an expandable QR example
with the current “Teilen” dialog. Its QR code is for a public example route.

Supplied videos remain source material for the separate film task and are not
embedded by this refresh.

## Second supplement: restart recovery, incoming places and English screens

The second supplement contains all 22 requested source PNGs. The website uses
15 of these in `assets/app/v0.13.3-nachtrag2/`; each WebP has the same stem as
its source PNG. All are resized from 1080 × 2400 to 720 × 1600, with no UI edits.
The source is a debug capture build from app commit `b1b9b35` (0.13.3 plus
A-020), not the 0.13.4 release APK. The folder identifies the capture batch.

| Asset stem | Language | Use |
|---|---|---|
| plan-wandern | en | Hero, showcase, computer/phone example and first-steps help |
| plan-ebike | en | Showcase |
| ort-google-maps | en | Showcase and route-change help |
| ruheanzeige | en | Showcase |
| fahrt | en | Showcase |
| neustart | de, en | Home detail card and interruption help |
| neustart-fortgesetzt | de, en | Interruption help after resuming |
| google-ziel-teilen | de, en | Places help: select OnPath in Google Maps sharing |
| google-ziel-uebernommen | de, en | Home detail card and places help: check the place |
| google-ziel-route | de, en | Places help: check the calculated route |

The two home details now have authentic screen examples and links to their
walkthroughs. Recovery help explicitly says that recording resumes only after
opening OnPath and choosing Continue; the interval before that is a recording
gap. A track is not visible behind the recovery dialog, but appears after
resuming. Both states are preserved as supplied.

Incoming-place help reflects the observed Google Maps sharing sheet, not an
invented Android chooser. If sharing only shows a marked ring, users hold that
ring to open the place menu. Captures use simulated locations, including the
recognised lift ride, and do not establish field reliability or partnership.
The remaining seven source images are alternative/diagnostic views, retained
outside the public website rather than adding duplicate screenshots.

