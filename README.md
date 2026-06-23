# pvw-testsite

Live testing grounds for [lead-crm](https://github.com/mpdecker/lead-crm) automations — audit engine validation and outreach pipeline end-to-end testing.

**Live URL:** https://pvw-testsite.vercel.app

## Directory structure

| Directory | Purpose |
|---|---|
| `audit-signals/` | One page per promoted `FindingCode` (or promotion-boundary scenario) |
| `journey/` | Headless journey probe scenarios — forms, nav, contact paths, CTAs |
| `observations/` | `ObservationCode`-only pages — findings stay `[]`, observations documented |
| `outreach/` | Realistic composite business pages for full pipeline (audit → score → email) testing |
| `legacy/pending-engine/` | Reserved scenarios for future engine signals (no findings today) |
| `api/` | Stub for Vercel serverless functions |
| `scripts/` | Manifest export and expansion maintenance scripts |

## Page comment block

Every scenario HTML file starts with a structured comment:

```
SCENARIO: ...
CATEGORY: ...
SIGNALS TRIGGERED: ...
EXPECTED FINDINGS: [code_a, code_b]   # promoted FindingCodes only
EXPECTED OBSERVATIONS: [code_c]       # observation-only pages use this field
EXPECTED GRADE: ...
NOTES: ...
```

Finding and observation codes must match the lead-crm engine (`src/lib/audit-findings.ts`).

## Adding a scenario

1. Create an HTML file in the appropriate directory
2. Copy the comment block format from an existing page in the same category
3. Run `python scripts/export-scenario-manifest.py` to refresh the lead-crm test manifest
4. `git push` — Vercel deploys in seconds

## Automated validation (lead-crm)

From the `lead-crm` repo root, after deploying pvw-testsite:

```bash
# Regenerate manifest from HTML comment blocks (run in pvw-testsite)
python scripts/export-scenario-manifest.py

# Run full audit regression against deployed URLs
PVW_TESTSITE_AUDIT=1 npx vitest run src/lib/__tests__/pvw-testsite-scenarios.test.ts
```

The integration test runs HTTP + headless + journey audits per scenario. Findings must match exactly; observations use subset matching (expected codes must appear, extras allowed).

## Manual audit (single page)

```bash
# HTTP signals only
npx tsx --tsconfig tsconfig.json -e "
import { runHttpAudit } from './src/lib/audit-http';
const s = await runHttpAudit('https://pvw-testsite.vercel.app/audit-signals/no-title.html');
console.log(JSON.stringify(s.signals, null, 2));
"

# Full findings + observations
npx tsx --tsconfig tsconfig.json -e "
import { runHttpAudit } from './src/lib/audit-http';
import { runHeadlessAudit } from './src/lib/audit-headless';
import { runJourneyAudit } from './src/lib/audit-journey';
import { buildFindings, buildObservations } from './src/lib/audit-findings';
const url = 'https://pvw-testsite.vercel.app/audit-signals/no-title.html';
const http = await runHttpAudit(url);
const headless = await runHeadlessAudit(url);
const journey = await runJourneyAudit(url);
const signals = { ...http.signals, ...headless, journeyResults: journey };
console.log('findings', buildFindings(signals).map(f => f.code));
console.log('observations', buildObservations(signals).map(o => o.code));
"
```

## Out of scope on static Vercel hosting

These `FindingCode` values cannot be isolated on this testsite:

- `dead_site`, `no_https` — infrastructure / TLS
- `slow_load` (finding) — requires >6s load time
- `http_redirect` (finding) — requires multiple redirect hops

## Maintenance

**`audit-signals/clean.html` copyright year** — Update the footer `&copy; YEAR` each calendar year so the clean baseline stays finding-free (`stale_year` fires when the year is 2+ years behind current).
