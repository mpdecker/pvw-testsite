# Testsite Expansion 2 — Design Spec
Date: 2026-06-22

## Overview

Second major expansion of pvw-testsite, filling remaining gaps in FindingCode coverage, adding 6 missing journey probe scenarios, introducing a new `observations/` directory for ObservationCode-only pages, and extending outreach composites to 8 new personas.

**Current state:** 43 pages (19 audit-signal, 12 journey, 11 outreach, 1 clean baseline)
**After expansion:** 74 pages (+31)

---

## Section 1: New Audit-Signal Pages (5 pages)

All use the Enriched Base Template (same as Expansion 1) minus exactly the one element being tested. Each isolates one FindingCode.

| File | FindingCode | Mechanism |
|---|---|---|
| `audit-signals/no-title.html` | `seo_title` | `<title>` tag removed from `<head>` entirely |
| `audit-signals/layout-overflow.html` | `layout_overflow` | `<pre>` block with a 120-char `white-space:nowrap` string forces horizontal scroll past 390px viewport |
| `audit-signals/blank-above-fold.html` | `blank_primary_content` | Hero section has `visibility:hidden; height:0` — rendered above-fold has < 30 chars of text, no images, no actionables; all other content intact below fold |
| `audit-signals/script-errors.html` | `script_errors` | Inline JS throws 2 uncaught errors + 2 `console.error()` calls (cluster ≥ 3); two non-primary `<button onclick="return false">` elements below fold satisfy `brokenInteractiveControlCount > 1` for `hasUserVisibleTechnicalBreakage`; buttons are not in header/nav so `primaryInteractiveFailureCount = 0` and `interactive_control_failure` finding does NOT fire |
| `audit-signals/mixed-content.html` | `mixed_content` | `<img src="http://example.com/1x1.gif">` on the HTTPS-served Vercel page; detected statically by HTTP audit src/href scan; `hasMixedContent = true` fires the finding |

### Notes

**`script_errors` is inherently compound.** The engine requires `runtimeErrorClusterCount >= 3 && hasUserVisibleTechnicalBreakage`. The page produces `script_errors` finding + `interactive_control_failure` observation (not finding — finding requires `primaryInteractiveFailureCount > 0`, which stays 0). This is documented in the comment block.

**`blank_primary_content` trigger condition.** Fires when `(primaryContentMissing && blankAboveFold) || (blankAboveFold && blockedCriticalAssetCount > 0)`. Using `visibility:hidden; height:0` on the hero satisfies `blankAboveFold` (< 30 above-fold chars, no hero media, no actionables) while `primaryContentMissing` is also true (main text < 80 words in viewport). Below-fold content stays intact so other signals don't fire.

---

## Section 2: New Journey Probe Pages (6 pages)

Each tests a specific journey probe failure. All pages are otherwise clean (no audit-signal findings).

| File | FindingCode | Mechanism |
|---|---|---|
| `journey/no-lead-form.html` | `no_lead_form` | No `<form>` element anywhere on page; only a `tel:` CTA — `probeLeadFormUsability` finds nothing |
| `journey/form-validation-broken.html` | `form_validation_broken` | Text input with `pattern="^IMPOSSIBLE_PATTERN_XYZ$" required` — every valid-looking submission is rejected by browser validation; field is fillable but impossible to satisfy |
| `journey/form-mobile-blocker.html` | `form_mobile_layout_blocker` | Form container styled `min-width:650px; overflow:visible` — at 390px mobile viewport fields overflow and are partially off-screen |
| `journey/no-call-path.html` | `no_call_path` | Phone number as plain text only (no `tel:` link), no email, no form — `probeTapToCall` fails, `hasStrongAlternateContact = false`; produces both `no_call_path` and `no_click_to_call` findings (documented in comment block — intentional and correct engine behavior) |
| `journey/no-email-path.html` | `no_email_path` | Has a working `tel:` link, no `mailto:`, no contact form, no contact page link — `probeEmailContactPath` fails; `no_email_path` fires because contactPathTypes excludes email/form |
| `journey/no-directions-path.html` | `no_directions_path` | Street address visible and in JSON-LD, but no Google Maps link, no Apple Maps link, no `/directions` or `/location` href anywhere — `probeDirectionsPath` fails; `no_directions_path` fires because `hasAddressSignal = true` |

### Notes

**`no-call-path.html` intentionally produces two findings.** The engine's `no_call_path` finding (`journeyCodes.has('no_call_path') && !hasStrongAlternateContact`) and `no_click_to_call` finding (`!hasClickToCall && hasPhone && !hasStrongAlternateContact`) both fire on the same condition: phone text exists but no `tel:` link and no email/form fallback. This is correct behaviour — both codes are documented in the comment block.

**`no-email-path.html` design constraint.** `no_email_path` finding fires only when `journeyCodes.has('no_email_path') && !hasContactForm && !contactPathTypes.includes('call')`. This last condition requires no call path in `contactPathTypes`. Since the page has a `tel:` link, `contactPathTypes` includes 'call', so this finding does NOT fire as a promoted finding — it fires as an observation only. The page is still valuable for testing the `probeEmailContactPath` probe detection. EXPECTED FINDINGS: `[]`, EXPECTED OBSERVATIONS: `[no_email_path, limited_contact_paths]`.

---

## Section 3: Observation Signal Pages (12 pages in new `observations/` directory)

New top-level directory. Pages here test `ObservationCode` detection — they produce observations but no promoted findings (or at most minor low-severity findings that stay below the promotion threshold). Comment blocks use `EXPECTED FINDINGS: []` and a new `EXPECTED OBSERVATIONS:` field.

Each page uses the Enriched Base Template as its base, modified to suppress the target signal.

### 3a — Isolated pages (8)

| File | ObservationCode | Mechanism |
|---|---|---|
| `service-clarity-gap.html` | `service_clarity_gap` | All section headings use "How We Help" / "Our Work" — body text avoids "service(s)", "what we do", "menu", "offerings"; `hasServiceClarity = false` |
| `about-team-gap.html` | `about_team_gap` | No "about us", "our story", "our team", "family owned", "locally owned", "meet the team", "who we are" language anywhere; `hasAboutTeamSignal = false`; has > 120 words (non-thin) |
| `trust-signal-gap.html` | `trust_signal_gap` | Has title + H1 (`hasBusinessIdentity = true`, trustSignalCount = 1); no address, hours, testimonials, service clarity, service area, or about-team language — `trustSignalCount = 1 < 2`; has contact form to remain non-thin |
| `misleading-submit-label.html` | `misleading_submit_label` | Form submit button labeled "Continue" — does not match `FINAL_SUBMIT_RE` (`/\b(submit\|send\|send message\|request quote\|request now\|book now\|place order)\b/i`); `primaryFormSuspiciousSubmitLabel = true` |
| `duplicate-contact-fields.html` | `duplicate_contact_fields` | Form has `<input type="email" name="email">` and `<input type="email" name="confirm_email">` — `duplicateContactFieldCount = 1` |
| `overconstrained-form.html` | `overconstrained_form` | 6 required fields (name, company, address, phone, email, zip), no message/textarea field, submit says "Continue" — `constraintScore ≥ 4` (`frictionScore`: +2 for 6 fields, +1 for 5 required; +2 for `excessiveRequiredFields`; +1 for suspicious label = 6 total) |
| `business-identity-mismatch.html` | `business_identity_mismatch` | `<title>` "Summit Pro Services — Northampton, MA" but `<h1>` "Your Trusted Home Improvement Partner" — title tokens `[summit, pro, services, northampton]` share no 3+ char tokens with H1 tokens `[your, trusted, home, improvement, partner]`; `hasConsistentBusinessIdentity = false` |
| `pricing-intent-gap.html` | `pricing_intent_gap` | Primary CTA `<a href="/get-estimate" class="btn">Contact Us Today</a>` — href `/get-estimate` matches `PRICING_RE`, classifying `primaryCtaType = 'quote'`; body text never uses "quote", "estimate", "pricing", "price" so `hasPricingIntent = false`; observation fires |

### 3b — Combo pages (4)

Each shows a realistic multi-observation flaw cluster useful for outreach scoring validation.

| File | ObservationCodes | Pattern |
|---|---|---|
| `trust-gap-combo.html` | `service_clarity_gap` + `about_team_gap` + `trust_signal_gap` | Minimal "We can help!" page — business name, phone, form, but no services language, no team content, no trust anchors |
| `form-friction-combo.html` | `duplicate_contact_fields` + `required_field_overload` + `misleading_submit_label` + `overconstrained_form` | Overbuilt form: confirm-email field, 6 required fields (including company + zip), submit says "Continue", no message field |
| `content-gap-combo.html` | `service_clarity_gap` + `pricing_intent_gap` + `review_signal_gap` | Quote-CTA page (`href="/get-estimate"`) with generic content — no pricing language, section headings avoid "service", no reviews |
| `identity-gap-combo.html` | `business_identity_mismatch` + `service_area_gap` + `about_team_gap` | Title/H1 name clash, no geographic coverage text, no team/about language |

### Stylesheet path

Pages in `observations/` use `<link rel="stylesheet" href="../styles.css">` (same subdirectory depth as `audit-signals/`, `journey/`, `outreach/`).

---

## Section 4: New Outreach Composites (8 pages)

All follow the existing outreach composite conventions: realistic local business persona, Pioneer Valley geography, intentional flaws commented inline, outreach angle in comment block header.

### Contact-path composites (3)

| File | Business | Grade | Signals | Outreach angle |
|---|---|---|---|---|
| `outreach/auto-repair.html` | Metro Auto & Service | P2 | `no_click_to_call` (phone as plain text, no `tel:`) + `small_tap_targets` (overcrowded nav with 7 small links) | Your phone number can't be tapped on mobile, and your nav links are too small for most thumbs — two quick fixes that could mean more calls |
| `outreach/florist.html` | Bloom & Co Florist | P2 | `no_directions_path` (street address present, no maps link anywhere) + `stale_year` (copyright 2023) | Customers ready to visit can't tap for directions, and the site looks a couple years out of date |
| `outreach/salon.html` | Studio 47 Salon | P1 | `seo_title` (missing `<title>` tag) + `no_click_to_call` (phone text only) | Your salon doesn't appear in search results at all, and the phone number can't be tapped — two issues that cost you walk-in and call traffic every day |

### New trade composites (5)

| File | Business | Grade | Signals | Outreach angle |
|---|---|---|---|---|
| `outreach/towing.html` | Pioneer Towing & Recovery | P0 | `seo_title` + `no_click_to_call` + `broken_images` (2 broken image srcs) | Three critical issues on an emergency-service site — invisible in search, phone untappable, and images broken |
| `outreach/locksmith.html` | Capital Lock & Key | P1 | `seo_title` + `service_area_gap` (obs: no service area language) + `stale_year` | No title tag means no search presence, and there's no mention of which towns you cover |
| `outreach/appliance-repair.html` | Valley Appliance Repair | P2 | `form_validation_broken` (impossible `pattern` constraint) + `layout_overflow` (wide `pre` block) | Your quote form rejects every submission, and the page scrolls sideways on mobile |
| `outreach/catering.html` | Valley Catering Co | P2 | `form_mobile_layout_blocker` (form `min-width:650px`) + `service_area_gap` (obs: no service area text) | Your booking form breaks on mobile screens, and there's no mention of where you cater |
| `outreach/moving.html` | Pioneer Moving Co | P3 | `small_tap_targets` (cramped nav) + `misleading_submit_label` (obs: submit says "Continue") | Several buttons are too small to tap reliably, and your form's submit button doesn't clearly signal "send my request" |

---

## Section 5: Registry Update (`index.html`)

31 new `<li>` entries across 4 sections. New "Observation Signals" section uses the same `<h2>` + `<ul>` pattern as the existing three sections.

```html
<h2>Observation Signals</h2>
<ul>
  <!-- 12 entries, each with href="observations/filename.html" -->
</ul>
```

Each observation entry uses `ObservationCode(s)` in the description `<span>` instead of a `FindingCode`.

**Final counts after expansion:**

| Section | Before | Added | After |
|---|---|---|---|
| `audit-signals/` | 19 | 5 | 24 |
| `journey/` | 12 | 6 | 18 |
| `outreach/` | 11 | 8 | 19 |
| `observations/` | 0 | 12 | 12 |
| **Total** | **43** | **31** | **74** |

---

## Out of Scope

- No changes to `clean.html`, `styles.css`, or `api/`
- No splitting of existing `no-seo.html` — `seo_desc`/`seo_h1`/`no_og` fire only as a cluster per engine logic; isolated pages would not produce findings and would be misleading
- No `dead_site`, `no_https`, `slow_load`, `http_redirect` pages — these are infrastructure signals not testable on a static Vercel deployment
