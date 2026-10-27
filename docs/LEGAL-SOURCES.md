# Legal notices: sources and deployment assumptions

Reviewed 27 October 2026. These are drafting sources, not a certification of legal compliance.

## Operator

Confirmed against the operator's existing public privacy notice at https://44-2.de/datenschutz/:

- Christian Neuhaus
- Fabriciusstr. 11–12, 40721 Hilden, Germany
- info@44-2.de

The existing imprint has ambiguous formatting and a malformed email. The privacy notice supplies the complete address and correctly formed email. No tax ID, register entry, professional status or charity status has been invented.

## Primary sources

- Provider information: https://www.gesetze-im-internet.de/ddg/__5.html
- GDPR information duties and lawful processing: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679
- Data-subject rights: https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_de
- Hosting provider and retention criteria: https://www.cloudflare.com/privacypolicy/
- Processor terms and international transfers: https://www.cloudflare.com/cloudflare-customer-dpa/
- Dataset-dependent log retention: https://developers.cloudflare.com/observability/logs/
- Competent regional supervisory authority: https://www.ldi.nrw.de/

## Deployment assumptions

Cloudflare Pages is the intended public host; it has not been configured or verified through this repository. The pages say so. No processor agreement acceptance, particular retention setting, exclusively EU processing or fixed deletion period has been assumed. The code uses no analytics, cookies, local storage, payment provider or externally loaded fonts. Provider-added features must be checked separately.

`legal_review_complete` stays false until the owner checks the real host configuration and contractual arrangements. Merge into main is permitted; it does not approve public launch. A review build remains the default.
