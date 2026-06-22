# pvw-testsite

Live testing grounds for [lead-crm](https://github.com/mpdecker/lead-crm) automations — audit engine validation and outreach pipeline end-to-end testing.

**Live URL:** https://pvw-testsite.vercel.app

## Directory structure

| Directory | Purpose |
|---|---|
| `audit-signals/` | One page per audit signal — each triggers exactly one known finding |
| `journey/` | Headless journey probe scenarios — broken nav, forms, overlays, missing CTAs |
| `outreach/` | Realistic composite business pages for full pipeline (audit → score → email) testing |
| `api/` | Stub for Vercel serverless functions — add `.js` files here when server-side behavior is needed |

## Adding a scenario

1. Create an HTML file in the appropriate directory
2. Open the file with the structured comment block (copy format from any existing page)
3. `git push` — Vercel deploys in seconds

## Running the auditor against a page

From the `lead-crm` repo root:

```bash
# HTTP signals only
npx tsx --tsconfig tsconfig.json -e "
import { runHttpAudit } from './src/lib/audit-http';
const s = await runHttpAudit('https://pvw-testsite.vercel.app/audit-signals/no-seo.html');
console.log(JSON.stringify(s, null, 2));
"

# Full findings (HTTP + headless)
npx tsx --tsconfig tsconfig.json -e "
import { runHttpAudit } from './src/lib/audit-http';
import { runHeadlessAudit } from './src/lib/audit-headless';
import { buildFindings } from './src/lib/audit-findings';
const http = await runHttpAudit('https://pvw-testsite.vercel.app/audit-signals/no-seo.html');
const headless = await runHeadlessAudit('https://pvw-testsite.vercel.app/audit-signals/no-seo.html');
const signals = { ...http, ...headless };
console.log(buildFindings(signals, []));
"
```
