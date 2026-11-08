# onpath.earth

Static English and German website for OnPath: **Your outing. Simply on your way. / Deine Tour. Einfach unterwegs.**

This repository is independent of the Android app at `happychriss/OnPath`.

## Build and preview

Python 3.10+ and Node.js (only for the JavaScript syntax check) are enough. There are no package dependencies.

```sh
python3 build.py
python3 scripts/check_site.py
node --check assets/app.js
python3 -m http.server 8000 --directory dist
```

English is at `/`, German at `/de/`. Every page has a corresponding language-switch destination and `hreflang` links. Font, photograph and scripts are served locally. No analytics or third-party embeds are included.

## Homepage and shared design

`home_de.html` and `home_en.html` contain the approved homepage. `home_page.py` loads them into the existing
bilingual builder. `assets/home-v2.css` is scoped to this homepage; `assets/editorial.css` extends the shared
article, help, access-page, header and footer styles. Secondary-page copy stays in `content_de.py`,
`content_en.py` and `legal_content.py`. Route URLs, language switches and review/noindex controls stay in the builder.

## Help pictures

App screens on the help pages: `help_shots.py` says which picture goes under which help section (DE and EN) with its
caption. Swap or add pictures: put the PNGs (phone screenshots, 1080 × 2400) in a folder, run
`python3 scripts/help_shots.py <folder> …` (writes `assets/help/*.webp` and `sizes.json`), then `python3 build.py`.
Current pictures: the Meran round captured on 7 November 2026 with app 0.17.3 and the current browser planner.
The pairing confirmation pictures are German app-test snapshots; where an English picture is unavailable, the
English page explicitly labels the German screen. Later source folders win.
Pictures can also sit inside a help text: `[[shots:name,name]]`. `ARTICLE_SHOTS` adds the same current pictures
to relevant hiking, cycling and outlook sections without editing their prose. All screenshots can be enlarged;
phone images retain their complete aspect ratio.

## Review and public launch

The default build is a **review build**: `noindex`, robots disallow crawling, notices describing the intended hosting configuration. This does not make a deployment private: configure preview access separately in the hosting dashboard if needed.

Provider contact details and bilingual legal/privacy notices are included. See [legal sources and remaining hosting verification](docs/LEGAL-SOURCES.md). Before public launch, verify the actual hosting setup, processing and retention, update the notices as needed, then mark the review complete in `site-config.json` before using:

```sh
python3 build.py --release
```

The release command refuses incomplete operator settings and unresolved legal draft markers. A completed form is not a substitute for reviewing the actual pages and data flows.

## Cloudflare Pages

The owner connects **this repository only** through the Cloudflare dashboard. No API token or account credentials belong here.

- Production branch: `main` (sessions push straight to it; pull requests only for workflows / deploy config, secrets and the legal pages – see `AGENTS.md`).
- Build command during review: `python3 build.py`.
- Output directory: `dist`.
- After legal completion and launch approval: `python3 build.py --release`.
- The app repo, its builds and its releases are not involved.

No Cloudflare project, domain, DNS record or WordPress content is modified by this source change. Automatic deployment begins only after the owner connects the repository.

## Content and ownership

See [the five-point agent brief](docs/AGENT-BRIEF.md) and [release checklist](docs/RELEASE.md). `onpath.earth` is the canonical project website. Personal-background links use `https://44-2.de/` only; the owner plans to remove the old OnPath/OnPass pages there. Private marketing research, tentative numerical prices, tester lists, credentials and private Drive content must stay outside this public repository.

See [the original website colour palette](docs/COLORS.md) for the exact HEX codes and their uses.

See [asset notices](ASSET-NOTICES.md) for the photograph, font and logo sources. The original app artwork is used rather than a new logo interpretation.
