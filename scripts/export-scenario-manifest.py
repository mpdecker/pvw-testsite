#!/usr/bin/env python3
"""Export pvw-testsite scenario manifest from HTML comment blocks."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAD_CRM_FIXTURE = Path(__file__).resolve().parents[2] / "lead-crm" / "src" / "lib" / "__tests__" / "fixtures" / "pvw-testsite-scenarios.json"
OUT_LOCAL = ROOT / "scripts" / "pvw-testsite-scenarios.json"
BASE_URL = "https://pvw-testsite.vercel.app"

COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)
LIST_RE = re.compile(r"EXPECTED (FINDINGS|OBSERVATIONS):\s*\[([^\]]*)\]")


def parse_list(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def scan_file(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = COMMENT_RE.search(text)
    if not m:
        return None
    comment = m.group(1)
    findings: list[str] = []
    observations: list[str] = []
    for kind, body in LIST_RE.findall(comment):
        if kind == "FINDINGS":
            findings = parse_list(body)
        else:
            observations = parse_list(body)
    rel = path.relative_to(ROOT).as_posix()
    return {
        "path": rel,
        "url": f"{BASE_URL}/{rel}",
        "expectedFindings": findings,
        "expectedObservations": observations,
    }


def main() -> None:
    entries: list[dict] = []
    for pattern in (
        "audit-signals/*.html",
        "journey/*.html",
        "observations/*.html",
        "outreach/*.html",
        "legacy/pending-engine/*.html",
    ):
        for path in sorted(ROOT.glob(pattern)):
            if path.name == "clean.html":
                entry = scan_file(path)
                if entry:
                    entry["expectedFindings"] = []
                    entry["expectedObservations"] = []
                    entries.append(entry)
                continue
            entry = scan_file(path)
            if entry:
                entries.append(entry)
    payload = entries
    OUT_LOCAL.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(entries)} scenarios to {OUT_LOCAL}")
    if LEAD_CRM_FIXTURE.parent.exists():
        LEAD_CRM_FIXTURE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"copied to {LEAD_CRM_FIXTURE}")
    else:
        print(f"skip lead-crm fixture (not found): {LEAD_CRM_FIXTURE}")

    smoke_script = ROOT / "scripts" / "export-smoke-manifest.py"
    if smoke_script.exists():
        import subprocess
        subprocess.run([sys.executable, str(smoke_script)], check=True)


if __name__ == "__main__":
    main()
