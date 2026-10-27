# Before public launch

- [ ] Owner reviews and merges the PR. Only this repository is connected to Pages.
- [ ] Operator address/email and bilingual notices are included; verify they remain current. Review the actual hosting, retention and app data flows; do not publish legal draft text.
- [ ] Update `site-config.json`, remove resolved draft markers in source, then run `python3 build.py --release` and `python3 scripts/check_site.py`.
- [ ] Add confirmed Google Play test links and real screenshots where appropriate. Do not invent a registration form or an installation invitation.
- [ ] Verify feature status against the current Android release and browser planner before updating any availability claim.
- [ ] Check both languages at desktop/mobile sizes, the language switch, help search and keyboard navigation.
- [ ] Confirm photograph/font/brand notices, final domain and any owner-approved redirects from old public URLs.
- [ ] Keep WordPress drafts unpublished. Archive private marketing files in Drive, outside Git history.

The public-source PR is a reviewable deliverable, not evidence that these launch tasks have been completed.
