#!/usr/bin/env python3
"""Build pvw-testsite-smoke.json from full manifest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULL = ROOT / "scripts" / "pvw-testsite-scenarios.json"
LEAD_CRM = ROOT.parent / "lead-crm" / "src" / "lib" / "__tests__" / "fixtures" / "pvw-testsite-smoke.json"

SMOKE_PATHS = [
    "audit-signals/clean.html",
    "audit-signals/no-title.html",
    "audit-signals/blank-above-fold.html",
    "audit-signals/script-errors.html",
    "audit-signals/render-incomplete.html",
    "journey/no-call-path.html",
    "journey/no-email-finding.html",
    "journey/form-validation-broken.html",
    "observations/trust-signal-gap.html",
    "outreach/towing.html",
]

def main() -> None:
    full = json.loads(FULL.read_text(encoding="utf-8"))
    by_path = {e["path"]: e for e in full}
    smoke = [by_path[p] for p in SMOKE_PATHS]
    missing = [p for p in SMOKE_PATHS if p not in by_path]
    if missing:
        raise SystemExit(f"missing from full manifest: {missing}")
    LEAD_CRM.parent.mkdir(parents=True, exist_ok=True)
    LEAD_CRM.write_text(json.dumps(smoke, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(smoke)} smoke scenarios to {LEAD_CRM}")

if __name__ == "__main__":
    main()
