#!/usr/bin/env python3
"""Expansion 3: move legacy pages and patch scenario comment blocks."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
LEGACY = ROOT / "legacy" / "pending-engine"
LEGACY.mkdir(parents=True, exist_ok=True)

LEGACY_FILES = [
    "no-schema.html",
    "no-favicon.html",
    "images-no-alt.html",
    "low-contrast.html",
    "small-font.html",
    "duplicate-h1.html",
]

LEGACY_HEADER = """<!--
  SCENARIO: {scenario}
  CATEGORY: legacy/pending-engine
  SIGNALS TRIGGERED: (none — pending lead-crm engine support)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: (n/a)
  NOTES: Reserved for a future engine FindingCode. No observation or finding fires today.
-->"""

PATCHES: dict[str, str] = {
    "audit-signals/no-address.html": """<!--
  SCENARIO: no-address
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasAddressSignal=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: (observation only)
  NOTES: No street address on page lowers trustSignalCount. No no_address FindingCode exists.
-->""",
    "audit-signals/no-hours.html": """<!--
  SCENARIO: no-hours
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasHoursSignal=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: (observation only)
  NOTES: Missing hours text lowers trustSignalCount. No no_hours FindingCode exists.
-->""",
    "audit-signals/no-reviews.html": """<!--
  SCENARIO: no-reviews
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: reviewSignalCount=0, isThinBrochure=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [review_signal_gap]
  EXPECTED GRADE: (observation only)
  NOTES: Non-thin page without testimonials triggers review_signal_gap. No no_reviews FindingCode.
-->""",
    "audit-signals/no-service-area.html": """<!--
  SCENARIO: no-service-area
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasServiceAreaSignal=false, hasAddressSignal=true
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [service_area_gap]
  EXPECTED GRADE: (observation only)
  NOTES: Address present but no service-area language. No no_service_area FindingCode.
-->""",
    "audit-signals/phone-not-linked.html": """<!--
  SCENARIO: phone-not-linked
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasClickToCall=true (hero tel:), plain text phone in contact/footer
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: []
  EXPECTED GRADE: (no finding — hero tel: link satisfies hasClickToCall)
  NOTES: Demonstrates partial tel: coverage. no_click_to_call requires !hasClickToCall globally.
-->""",
    "audit-signals/stale-year.html": """<!--
  SCENARIO: stale-year
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasStaleYear=true, trustSignalCount<=1
  EXPECTED FINDINGS: [stale_year]
  EXPECTED GRADE: P2
  NOTES: Footer copyright 2020. trustSignalCount kept at 1 (business identity only) so stale_year promotes.
-->""",
    "journey/form-no-confirmation.html": """<!--
  SCENARIO: form-no-confirmation
  CATEGORY: journey
  SIGNALS TRIGGERED: form submits via preventDefault with no confirmation
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [form_friction]
  EXPECTED GRADE: (observation only)
  NOTES: No form_no_confirmation FindingCode. Journey probe may stall; form_friction observation likely.
-->""",
    "journey/popup-blocks-page.html": """<!--
  SCENARIO: popup-blocks-page
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryCtaBlocked=true, stickyOverlayBlockerCount>0
  EXPECTED FINDINGS: [primary_cta_blocked]
  EXPECTED OBSERVATIONS: [sticky_overlay_blocker]
  EXPECTED GRADE: P1
  NOTES: Full-screen modal blocks CTA. No popup_blocks_cta FindingCode in engine.
-->""",
    "journey/chatbot-over-cta.html": """<!--
  SCENARIO: chatbot-over-cta
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryCtaBlocked=true, stickyOverlayBlockerCount>0
  EXPECTED FINDINGS: [primary_cta_blocked]
  EXPECTED OBSERVATIONS: [sticky_overlay_blocker]
  EXPECTED GRADE: P1
  NOTES: Fixed chat widget covers phone CTA. No chatbot_blocks_cta FindingCode.
-->""",
    "journey/video-modal-trap.html": """<!--
  SCENARIO: video-modal-trap
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryCtaBlocked=true, stickyOverlayBlockerCount>0
  EXPECTED FINDINGS: [primary_cta_blocked]
  EXPECTED OBSERVATIONS: [sticky_overlay_blocker]
  EXPECTED GRADE: P1
  NOTES: Autoplay modal with no dismiss blocks CTA. No modal_trap FindingCode.
-->""",
    "journey/cta-disabled.html": """<!--
  SCENARIO: cta-disabled
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryCtaActionable=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [weak_primary_cta]
  EXPECTED GRADE: (observation only)
  NOTES: Disabled hero button; tel: link in contact section provides alternate path. No cta_disabled FindingCode.
-->""",
    "journey/no-mobile-cta.html": """<!--
  SCENARIO: no-mobile-cta
  CATEGORY: journey
  SIGNALS TRIGGERED: contactCtaAboveFold=false at mobile viewport
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [primary_cta_hidden, contact_cta_buried]
  EXPECTED GRADE: (observation only)
  NOTES: CTA hidden via CSS at mobile width. No no_mobile_cta FindingCode.
-->""",
    "journey/contact-buried.html": """<!--
  SCENARIO: contact-buried
  CATEGORY: journey
  SIGNALS TRIGGERED: contactCtaAboveFold=false, contactCtaCount>0
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [contact_cta_buried]
  EXPECTED GRADE: (observation only)
  NOTES: Contact section far below fold with no nav anchor. No contact_buried FindingCode.
-->""",
    "journey/multi-step-broken.html": """<!--
  SCENARIO: multi-step-broken
  CATEGORY: journey
  SIGNALS TRIGGERED: multiStepFormAdvances=false
  EXPECTED FINDINGS: [multi_step_form_blocked]
  EXPECTED GRADE: P1
  NOTES: Step 1 Next button has onclick return false. No multi_step_failure FindingCode.
-->""",
    "journey/no-cta.html": """<!--
  SCENARIO: no-cta
  CATEGORY: journey
  SIGNALS TRIGGERED: no CTA above fold, form buried below fold
  EXPECTED FINDINGS: [no_lead_form]
  EXPECTED OBSERVATIONS: [primary_cta_hidden, contact_cta_buried]
  EXPECTED GRADE: P1
  NOTES: Differs from no-lead-form.html: form exists but buried; journey probe finds no usable lead form in viewport.
-->""",
    "journey/no-email-path.html": """<!--
  SCENARIO: no-email-path
  CATEGORY: journey
  SIGNALS TRIGGERED: probeEmailContactPath=fail, contactPathTypes includes 'call'
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [no_email_path, limited_contact_paths]
  EXPECTED GRADE: (observation only)
  NOTES: tel: link blocks no_email_path finding promotion. See journey/no-email-finding.html for promoted finding.
-->""",
}

COMMENT_RE = re.compile(r"<!--\s*\n.*?-->", re.DOTALL)


def replace_comment(path: Path, new_header: str) -> None:
    text = path.read_text(encoding="utf-8")
    if not COMMENT_RE.search(text):
        raise ValueError(f"No comment block in {path}")
    path.write_text(COMMENT_RE.sub(new_header.strip(), text, count=1), encoding="utf-8", newline="\n")


def move_legacy(name: str) -> None:
    src = ROOT / "audit-signals" / name
    dst = LEGACY / name
    if not src.exists():
        print(f"skip missing {src}")
        return
    shutil.move(str(src), str(dst))
    scenario = name.replace(".html", "")
    text = dst.read_text(encoding="utf-8")
    text = COMMENT_RE.sub(LEGACY_HEADER.format(scenario=scenario).strip(), text, count=1)
    text = text.replace('href="../styles.css"', 'href="../../styles.css"')
    dst.write_text(text, encoding="utf-8", newline="\n")
    print(f"moved legacy {name}")


def patch_stale_year_body() -> None:
    path = ROOT / "audit-signals" / "stale-year.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("<h2>Our Services</h2>", "<h2>How We Help</h2>")
    text = text.replace(
        "Full-service plumbing and home repair for Hampshire County residents.",
        "We help homeowners with repairs and maintenance. Call for a free estimate.",
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    for name in LEGACY_FILES:
        move_legacy(name)
    for rel, header in PATCHES.items():
        replace_comment(ROOT / rel, header)
        print(f"patched {rel}")
    patch_stale_year_body()
    print("done")


if __name__ == "__main__":
    main()
