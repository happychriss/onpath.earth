# Website contributors

Read [docs/AGENT-BRIEF.md](docs/AGENT-BRIEF.md) and apply [docs/UX-CHECK.md](docs/UX-CHECK.md) before editing. Recheck the whole introduction after each content or layout change; flag conflicts with its information hierarchy instead of stacking requested elements. This is the website repository `happychriss/onpath.earth`, not the Android app repository.

Push small commits straight to `main` (owner 2026-10-31, standing permission) – no pull request, don't ask first. Open a pull request to the owner only for `.github/workflows/` / deploy configuration, anything with keys or secrets, and the legal pages (privacy, imprint: `/privacy/`, `/de/datenschutz/`, `/legal/`, `/de/impressum/`, `legal_content.py`). Never force-push, never delete a shared branch. The owner connects hosting. Do not request or store infrastructure credentials, modify the app repo, publish WordPress drafts or copy private marketing data here.

Run `python3 build.py`, `python3 scripts/check_site.py` and `node --check assets/app.js`. Preserve both languages and the original OnPath identity. Public launch requires the legal review in `docs/RELEASE.md`.

## Pictures and outside helpers – owner 2026-11-08
The whole flow (where the raw pictures live, who takes them, refreshing only the changed ones, publishing, helpers
without git) is in `happychriss/onpath.private` → `marketing/bilder/ABLAUF.md`. The essence:
- Helpers without git access (e.g. ChatGPT): never upload file by file through the GitHub API – hand over one ZIP with
  a `git format-patch --binary` against the named `main` commit, a short description and the check commands above.
- donald applies it with `git am --3way`, runs the checks, looks at the pages and pushes to `main`.
- Pictures keep their names (`assets/help/<key>-de|en.webp`, `assets/app/…`), so the page texts need no change.
  Legal pages, workflows and deploy settings only after asking the owner.
