# onpath.earth

Static English and German website for OnPath: **Your route. Simply planned. / Deine Tour. Einfach geplant.**

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

See [the five-point agent brief](docs/AGENT-BRIEF.md) and [release checklist](docs/RELEASE.md). The 44-2.de drafts remain unpublished references; the new site becomes canonical only when the owner approves launch. Private marketing research, tentative numerical prices, tester lists, credentials and private Drive content must stay outside this public repository.

See [the original website colour palette](docs/COLORS.md) for the exact HEX codes and their uses.

See [asset notices](ASSET-NOTICES.md) for the photograph, font and logo sources. The original app artwork is used rather than a new logo interpretation.
