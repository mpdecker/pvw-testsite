#!/usr/bin/env python3
"""Patch Expansion 4 outreach pages with live-audited EXPECTED blocks."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
COMMENT_RE = re.compile(r"<!--\s*\n.*?-->", re.DOTALL)

PATCHES: dict[str, str] = {
    "auto-repair.html": """<!--
  SCENARIO: auto-repair
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Phone as plain text, no tel: link               -> FindingCode: no_click_to_call
    2. Nav has 7 links with font-size:11px/line-height:1 -> FindingCode: small_tap_targets
  EXPECTED FINDINGS: [no_click_to_call, small_tap_targets]
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your phone number can't be tapped on mobile, and your nav links are
    too small for most thumbs — two quick fixes that could mean more calls.
-->""",
    "florist.html": """<!--
  SCENARIO: florist
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No Google Maps / Apple Maps / /directions link     -> FindingCode: no_directions_path
    2. Copyright year 2023                               -> FindingCode: stale_year
  EXPECTED FINDINGS: [no_directions_path, stale_year]
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Customers ready to visit can't tap for directions, and the site looks
    a couple of years out of date.
-->""",
    "salon.html": """<!--
  SCENARIO: salon
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                              -> FindingCode: seo_title
    2. Phone as plain text, no tel: link                -> FindingCode: no_click_to_call
  EXPECTED FINDINGS: [no_click_to_call, seo_title]
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P1
  OUTREACH ANGLE: Your salon doesn't appear in search results at all, and the phone
    number can't be tapped — two issues that cost you walk-in and call traffic every day.
-->""",
    "towing.html": """<!--
  SCENARIO: towing
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                             -> FindingCode: seo_title
    2. Phone as plain text, no tel: link               -> FindingCode: no_click_to_call
    3. Two broken image srcs (empty src)               -> FindingCode: broken_images
  EXPECTED FINDINGS: [broken_images, broken_navigation_path, no_click_to_call, no_email_path, seo_title]
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P0
  OUTREACH ANGLE: Three critical issues on an emergency-service site — invisible in
    search, phone untappable, and images broken.
  NOTES: Live-audited composite. broken_navigation_path and no_email_path come from journey probes.
-->""",
    "locksmith.html": """<!--
  SCENARIO: locksmith
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                             -> FindingCode: seo_title
    2. No service area language anywhere               -> ObservationCode: service_area_gap
    3. Copyright year 2023                             -> FindingCode: stale_year
  EXPECTED FINDINGS: [seo_title, stale_year]
  EXPECTED OBSERVATIONS: [service_area_gap]
  EXPECTED GRADE: P1
  OUTREACH ANGLE: No title tag means no search presence, and there's no mention of
    which towns you cover.
-->""",
    "appliance-repair.html": """<!--
  SCENARIO: appliance-repair
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Form field with impossible pattern constraint   -> FindingCode: form_validation_broken
    2. <pre> block with white-space:nowrap             -> FindingCode: layout_overflow
  EXPECTED FINDINGS: [form_validation_broken, layout_overflow]
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your quote form rejects every submission, and the page scrolls
    sideways on mobile.
-->""",
    "catering.html": """<!--
  SCENARIO: catering
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Form container min-width:650px                  -> FindingCode: form_mobile_layout_blocker
    2. No service area language anywhere               -> ObservationCode: service_area_gap
  EXPECTED FINDINGS: [form_mobile_layout_blocker]
  EXPECTED OBSERVATIONS: [service_area_gap]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your booking form breaks on mobile screens, and there's no mention
    of where you cater.
-->""",
    "moving.html": """<!--
  SCENARIO: moving
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. 7 nav links with font-size:11px/line-height:1   -> FindingCode: small_tap_targets
    2. Form submit says "Continue"                     -> ObservationCode: misleading_submit_label
  EXPECTED FINDINGS: [small_tap_targets]
  EXPECTED OBSERVATIONS: [misleading_submit_label]
  EXPECTED GRADE: P3
  OUTREACH ANGLE: Several buttons are too small to tap reliably, and your form's submit
    button doesn't clearly signal "send my request."
-->""",
}

PHONE_FIXES = {
    "auto-repair.html": [
        ("(413) 555-0200", "413-555-0200"),
    ],
    "salon.html": [
        ("(413) 555-0400", "413-555-0400"),
    ],
    "towing.html": [
        ("(413) 555-0500", "413-555-0500"),
    ],
}


def main() -> None:
    outreach = ROOT / "outreach"
    for name, comment in PATCHES.items():
        path = outreach / name
        text = path.read_text(encoding="utf-8")
        text = COMMENT_RE.sub(comment, text, count=1)
        for old, new in PHONE_FIXES.get(name, []):
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
        print(f"patched {name}")


if __name__ == "__main__":
    main()
