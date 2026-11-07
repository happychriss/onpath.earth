# Website contributors

Read [docs/AGENT-BRIEF.md](docs/AGENT-BRIEF.md) before editing. This is the website repository `happychriss/onpath.earth`, not the Android app repository.

Push small commits straight to `main` (owner 2026-10-31, standing permission) – no pull request, don't ask first. Open a pull request to the owner only for `.github/workflows/` / deploy configuration, anything with keys or secrets, and the legal pages (privacy, imprint: `/privacy/`, `/de/datenschutz/`, `/legal/`, `/de/impressum/`, `legal_content.py`). Never force-push, never delete a shared branch. The owner connects hosting. Do not request or store infrastructure credentials, modify the app repo, publish WordPress drafts or copy private marketing data here.

Run `python3 build.py`, `python3 scripts/check_site.py` and `node --check assets/app.js`. Preserve both languages and the original OnPath identity. Public launch requires the legal review in `docs/RELEASE.md`.

## Outside helpers without git access (e.g. ChatGPT) – owner 2026-11-08
Don't upload through the GitHub API file by file (binary images fail or crawl). Hand over one ZIP instead: a `git
format-patch` (binaries included) against the current `main` commit – name that commit –, a short description and the
check commands above. Images already as WebP, sized for the web. Legal pages, workflows and deploy settings only after
asking the owner. donald (the owner's computer) applies the patch with `git am --3way`, runs the checks, looks at the
pages and pushes to `main` (first done 2026-11-08, 58a8a5d).
