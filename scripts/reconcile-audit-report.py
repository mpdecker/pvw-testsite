#!/usr/bin/env python3
"""Run lead-crm reconcile script and save CSV for drift triage."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAD_CRM = ROOT.parent / "lead-crm"
MANIFEST = ROOT / "scripts" / "pvw-testsite-scenarios.json"
OUT = ROOT / "scripts" / "reconcile-report.csv"
RECONCILE_TS = LEAD_CRM / "scripts" / "reconcile-pvw-testsite.ts"


def main() -> None:
    if not LEAD_CRM.exists():
        print(f"lead-crm not found at {LEAD_CRM}", file=sys.stderr)
        print("Manual one-liner:", file=sys.stderr)
        print(
            "  cd lead-crm && npx tsx scripts/reconcile-pvw-testsite.ts "
            "../pvw-testsite/scripts/pvw-testsite-scenarios.json > reconcile-report.csv",
            file=sys.stderr,
        )
        sys.exit(1)
    if not RECONCILE_TS.exists():
        raise SystemExit(f"missing reconcile script: {RECONCILE_TS}")

    cmd = ["npx", "tsx", str(RECONCILE_TS), str(MANIFEST)]
    print("running:", " ".join(cmd), flush=True)
    result = subprocess.run(
        cmd,
        cwd=LEAD_CRM,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    OUT.write_text(result.stdout, encoding="utf-8")
    lines = [line for line in result.stdout.splitlines() if line and not line.startswith("path,")]
    fails = sum(1 for line in lines if ",no," in line or line.endswith(",no"))
    print(f"wrote {OUT} ({len(lines)} scenarios, {fails} with mismatches)")


if __name__ == "__main__":
    main()
