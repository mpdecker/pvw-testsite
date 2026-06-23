#!/usr/bin/env python3
"""Patch outreach composite comment blocks for engine-aligned expectations."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
COMMENT_RE = re.compile(r"<!--\s*\n.*?-->", re.DOTALL)

OUTREACH: dict[str, str] = {
    "hvac.html": """<!--
  SCENARIO: hvac
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No JSON-LD schema (no engine FindingCode)
    2. No business hours in contact section
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Customers can't tell if you're open — trust signals are thin on the page.
-->""",
    "contractor.html": """<!--
  SCENARIO: contractor
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No og: meta tags
    2. Contact section buried below ~3000px scroll; no nav anchor
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [no_og, contact_cta_buried]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Social previews are weak and the contact form is buried below your portfolio.
-->""",
    "painter.html": """<!--
  SCENARIO: painter
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No street address on page
    2. Portfolio images use empty alt text (no engine FindingCode)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: P3
  OUTREACH ANGLE: No address on-site makes it harder for local customers to trust you.
-->""",
    "tree-service.html": """<!--
  SCENARIO: tree-service
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Body text color #aaa (no engine FindingCode)
    2. No service area language (address present)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [service_area_gap]
  EXPECTED GRADE: P3
  OUTREACH ANGLE: No mention of which towns you serve — local searchers may not know you cover them.
-->""",
    "handyman.html": """<!--
  SCENARIO: handyman
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Copyright year 2022 in footer
    2. No business hours in contact section
  EXPECTED FINDINGS: [stale_year]
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Site looks neglected and hours are missing — customers don't know when to call.
-->""",
    "cleaning-service.html": """<!--
  SCENARIO: cleaning-service
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No testimonials section
    2. Phone as plain text in contact (hero may have tel:)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [review_signal_gap]
  EXPECTED GRADE: P3
  OUTREACH ANGLE: No social proof on the site — reviews build trust for in-home services.
-->""",
    "pest-control.html": """<!--
  SCENARIO: pest-control
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Two h1 elements (no engine FindingCode)
    2. Body font-size 10px (no engine FindingCode)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: P3
  OUTREACH ANGLE: Minor polish issues on an otherwise solid site — reserved for future a11y signals.
-->""",
    "plumber.html": """<!--
  SCENARIO: plumber
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing meta description
    2. Services nav link → 404
  EXPECTED FINDINGS: [broken_navigation_path]
  EXPECTED OBSERVATIONS: [seo_desc]
  EXPECTED GRADE: P1
  OUTREACH ANGLE: Broken services navigation and weak SEO basics are costing you search traffic.
-->""",
    "roofer.html": """<!--
  SCENARIO: roofer
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing meta description
    2. Services nav → 404
    3. Two broken image src paths
  EXPECTED FINDINGS: [broken_navigation_path, broken_images]
  EXPECTED OBSERVATIONS: [seo_desc]
  EXPECTED GRADE: P0
  OUTREACH ANGLE: Three critical issues — broken nav, broken images, and weak search snippets.
-->""",
    "electrician.html": """<!--
  SCENARIO: electrician
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No og: meta tags
    2. Copyright year 2020
  EXPECTED FINDINGS: [stale_year]
  EXPECTED OBSERVATIONS: [no_og]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Site looks out of date and social sharing previews are incomplete.
-->""",
    "landscaper.html": """<!--
  SCENARIO: landscaper
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing H1 heading
    2. Small tap targets in nav
  EXPECTED FINDINGS: [small_tap_targets]
  EXPECTED OBSERVATIONS: [seo_h1]
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Nav links are too small on mobile and heading structure is weak for SEO.
-->""",
}


def main() -> None:
    for name, header in OUTREACH.items():
        path = ROOT / "outreach" / name
        text = path.read_text(encoding="utf-8")
        path.write_text(COMMENT_RE.sub(header.strip(), text, count=1), encoding="utf-8", newline="\n")
        print(f"patched outreach/{name}")


if __name__ == "__main__":
    main()
