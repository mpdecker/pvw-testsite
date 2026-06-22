# Testsite Major Expansion — Design Spec
Date: 2026-06-22

## Overview

Add 27 new scenario pages to pvw-testsite, expanding all three existing categories proportionally. The expansion fills signal coverage gaps in the audit engine, adds missing journey-probe failure modes, and extends outreach composites to cover all priority tiers (P0–P3) and more trade categories.

**Current state:** 16 pages (8 audit-signal, 4 journey, 3 outreach, 1 clean baseline)
**After expansion:** 43 pages (+27)

---

## Section 1: New Audit-Signal Pages (11 pages)

All pages follow the existing convention: one page triggers exactly one `FindingCode`; all other signals match `clean.html`. All use the Pioneer Home Services persona.

| File | `FindingCode` | How it fires |
|---|---|---|
| `audit-signals/no-schema.html` | `no_schema` | No JSON-LD `LocalBusiness` block in `<head>` |
| `audit-signals/no-address.html` | `no_address` | Phone and hours present, but no street address anywhere on page |
| `audit-signals/no-hours.html` | `no_hours` | Contact section has phone + address, but no business hours |
| `audit-signals/no-reviews.html` | `no_reviews` | No testimonials, star ratings, or review-count signals anywhere |
| `audit-signals/no-service-area.html` | `no_service_area` | No city, region, or service-area text on page |
| `audit-signals/images-no-alt.html` | `images_no_alt` | 2–3 `<img>` tags, all with empty or absent `alt` |
| `audit-signals/low-contrast.html` | `low_contrast` | Body text at `color:#aaa` on white — below WCAG AA 4.5:1 ratio |
| `audit-signals/small-font.html` | `small_font` | Body `font-size:10px` — below readable threshold |
| `audit-signals/duplicate-h1.html` | `duplicate_h1` | Two `<h1>` elements on the same page |
| `audit-signals/phone-not-linked.html` | `phone_not_linked` | Phone number as plain text, not wrapped in `<a href="tel:...">` |
| `audit-signals/no-favicon.html` | `no_favicon` | No `<link rel="icon">` in `<head>` |

### Signal isolation rule
Each page must satisfy all signals that `clean.html` satisfies, minus exactly the one being tested. The structured comment block at the top of each file must declare: `SCENARIO`, `CATEGORY`, `SIGNALS TRIGGERED`, `EXPECTED FINDINGS`, `EXPECTED GRADE`, and `NOTES`.

---

## Section 2: New Journey-Probe Pages (8 pages)

All pages are distinct from the 4 existing journey pages. Each tests a failure mode a headless probe would detect during a simulated user journey.

| File | `FindingCode` | Mechanism |
|---|---|---|
| `journey/form-no-confirmation.html` | `form_no_confirmation` | Form fields work, button is `type="submit"`, but no success message appears and page doesn't change after submit |
| `journey/popup-blocks-page.html` | `popup_blocks_cta` | Full-screen modal fires on load with no dismiss button — CTA rendered beneath it but unreachable |
| `journey/chatbot-over-cta.html` | `chatbot_blocks_cta` | Fixed-position floating chat widget z-indexed over the phone/CTA button |
| `journey/cta-disabled.html` | `cta_disabled` | CTA button visually styled as active but has `disabled` attribute + `pointer-events:none` |
| `journey/no-mobile-cta.html` | `no_mobile_cta` | CTA visible at desktop width; `display:none` at ≤480px — probe at mobile viewport finds nothing |
| `journey/contact-buried.html` | `contact_buried` | Contact section ~3000px below fold; no nav anchor shortcut to it |
| `journey/video-modal-trap.html` | `modal_trap` | Autoplay video modal fires on load with no close/dismiss path |
| `journey/multi-step-broken.html` | `multi_step_failure` | Two-step quote form; step 1 renders fine, "Next" button has `onclick="return false"` — step 2 never appears |

### Journey page conventions
- Pages should be otherwise clean (no audit-signal findings)
- The failure mechanism must be implemented purely in HTML/CSS/inline JS (no external dependencies)
- The structured comment block must document the exact mechanism so the probe author knows what to look for

---

## Section 3: New Outreach Composite Pages (8 pages)

Fills missing priority tiers (P0, P3) and expands trade coverage. Each uses a distinct business persona with a plausible outreach angle that follows naturally from the signal combination.

| File | Business | Grade | Signals | Outreach angle |
|---|---|---|---|---|
| `outreach/roofer.html` | Valley Ridge Roofing | P0 | `seo_desc` + `broken_navigation_path` + `broken_images` | Three critical issues — strongest urgency hook |
| `outreach/hvac.html` | Comfort Zone HVAC | P1 | `no_schema` + `no_hours` | Not showing in "near me" results; customers can't tell if you're open |
| `outreach/contractor.html` | Berkshire Build & Remodel | P1 | `no_og` + `contact_buried` | Social previews broken; contact buried below wall of content |
| `outreach/painter.html` | Five Star Painting Co | P2 | `no_address` + `images_no_alt` | Trust gap: no address on-site, portfolio photos inaccessible |
| `outreach/tree-service.html` | Pioneer Tree & Landscape | P2 | `low_contrast` + `no_service_area` | Hard-to-read text; no mention of which towns you serve |
| `outreach/handyman.html` | Valley Handyman Services | P2 | `stale_year` + `no_hours` | Site looks inactive; hours never listed |
| `outreach/pest-control.html` | Green Shield Pest Control | P3 | `duplicate_h1` + `small_font` | Minor polish issues on an otherwise solid site |
| `outreach/cleaning-service.html` | Spotless Home Cleaning | P3 | `no_reviews` + `phone_not_linked` | No social proof; phone number can't be tapped on mobile |

### Composite page conventions
- Each page should read as a realistic local business website — sufficient body copy, real-feeling service lists, consistent Pioneer Valley geography
- Intentional flaws must be commented in-line (matching the existing pattern in `plumber.html`)
- The outreach angle comment at the top should be written as a one-sentence hook a sales email could use verbatim

### Priority tier definitions (for reference)
| Grade | Meaning |
|---|---|
| P0 | 3+ critical signals — immediate action required |
| P1 | 1–2 high-severity signals — strong outreach hook |
| P2 | 2 moderate signals — clear improvement opportunity |
| P3 | 1–2 minor signals — polish / low-urgency |

---

## Section 4: Index Updates

`index.html` gains 27 new entries across the three existing registry sections. No new top-level sections are added. Each entry follows the existing format:

```html
<li><a href="path/file.html">slug</a><span>FindingCode(s) or description</span></li>
```

---

## Out of Scope

- No new top-level directories (accessibility category deferred until lead-crm has dedicated a11y detection)
- No server-side pages (no additions to `api/`)
- No changes to `styles.css` unless a new page requires a trivial addition that doesn't affect existing pages
- No changes to `clean.html`
