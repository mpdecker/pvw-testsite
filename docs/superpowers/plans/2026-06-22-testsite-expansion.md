# Testsite Major Expansion — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 27 new scenario pages (11 audit-signal, 8 journey-probe, 8 outreach-composite) and update the index registry, covering all priority tiers (P0–P3), new trade categories, and 11 new FindingCodes.

**Architecture:** All pages are static HTML. Audit-signal pages derive from the Enriched Base Template (defined below) by modifying exactly one element. Journey pages contain self-contained failure mechanisms in inline JS/CSS. Outreach composites are unique business personas with intentionally injected flaws.

**Tech Stack:** HTML5, CSS (existing `styles.css`), inline JavaScript only (no external script dependencies)

## Global Constraints

- Stylesheet link in every file: `<link rel="stylesheet" href="../styles.css">`
- Every file opens with a structured comment block: `SCENARIO`, `CATEGORY`, `SIGNALS TRIGGERED`, `EXPECTED FINDINGS`, `EXPECTED GRADE`, `NOTES`
- Journey page failure mechanisms: inline `<script>` or `onclick` attributes only — no `<script src="...">` tags
- Outreach intentional flaws: preceded by `<!-- Intentionally [description] -->`
- Footer copyright year: `2025` everywhere except `outreach/handyman.html` which uses `2022`
- Geography: Pioneer Valley, MA — Northampton, Easthampton, Florence, Amherst
- Do not modify `clean.html`, `styles.css`, or `api/`
- Data URI for inline images (always loads, no external request): `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=`

---

## Enriched Base Template

All audit-signal pages derive from this template. It satisfies every positive signal for the new FindingCodes (schema, address, hours, reviews, service area, favicon, linked phone, alt text, single H1, readable font, good contrast). Each audit-signal page removes or modifies exactly one element.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100 for a free estimate.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Pioneer Home Services",
    "telephone": "+14135550100",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "123 Main Street",
      "addressLocality": "Northampton",
      "addressRegion": "MA"
    }
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer a full range of home services throughout Hampshire County.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning</li>
        <li>Emergency service available 24/7</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone in the Valley."</p>
        <cite>— Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>— Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>Our Work</h2>
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="Pioneer Home Services technician at work" width="600" height="1"
           style="width:100%;max-width:600px;display:block;">
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon–Fri 8am–6pm, Sat 9am–3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe the work you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

---

## File Structure

**Create (27 files):**

| Path | FindingCode(s) |
|---|---|
| `audit-signals/no-schema.html` | `no_schema` |
| `audit-signals/no-address.html` | `no_address` |
| `audit-signals/no-hours.html` | `no_hours` |
| `audit-signals/no-reviews.html` | `no_reviews` |
| `audit-signals/no-service-area.html` | `no_service_area` |
| `audit-signals/images-no-alt.html` | `images_no_alt` |
| `audit-signals/low-contrast.html` | `low_contrast` |
| `audit-signals/small-font.html` | `small_font` |
| `audit-signals/duplicate-h1.html` | `duplicate_h1` |
| `audit-signals/phone-not-linked.html` | `phone_not_linked` |
| `audit-signals/no-favicon.html` | `no_favicon` |
| `journey/form-no-confirmation.html` | `form_no_confirmation` |
| `journey/popup-blocks-page.html` | `popup_blocks_cta` |
| `journey/chatbot-over-cta.html` | `chatbot_blocks_cta` |
| `journey/cta-disabled.html` | `cta_disabled` |
| `journey/no-mobile-cta.html` | `no_mobile_cta` |
| `journey/contact-buried.html` | `contact_buried` |
| `journey/video-modal-trap.html` | `modal_trap` |
| `journey/multi-step-broken.html` | `multi_step_failure` |
| `outreach/roofer.html` | `seo_desc` + `broken_navigation_path` + `broken_images` |
| `outreach/hvac.html` | `no_schema` + `no_hours` |
| `outreach/contractor.html` | `no_og` + `contact_buried` |
| `outreach/painter.html` | `no_address` + `images_no_alt` |
| `outreach/tree-service.html` | `low_contrast` + `no_service_area` |
| `outreach/handyman.html` | `stale_year` + `no_hours` |
| `outreach/pest-control.html` | `duplicate_h1` + `small_font` |
| `outreach/cleaning-service.html` | `no_reviews` + `phone_not_linked` |

**Modify (1 file):** `index.html`

---

### Task 1: Audit-signal pages — absence signals

**Files:**
- Create: `audit-signals/no-schema.html`
- Create: `audit-signals/no-address.html`
- Create: `audit-signals/no-hours.html`
- Create: `audit-signals/no-reviews.html`
- Create: `audit-signals/no-service-area.html`

**Interfaces:**
- Consumes: `../styles.css` (existing, no changes)
- Produces: 5 isolated-signal URLs for audit engine testing

Each file: start from the Enriched Base Template, prepend the comment block shown below, apply the described modification. All other elements remain identical to the template.

- [ ] **Step 1: Create `audit-signals/no-schema.html`**

Comment block to prepend (before `<!DOCTYPE html>`):
```html
<!--
  SCENARIO: no-schema
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasLocalBusinessSchema=false
  EXPECTED FINDINGS: [no_schema]
  EXPECTED GRADE: P2
  NOTES: All enriched-template signals present. The <script type="application/ld+json"> block is absent.
-->
```

Modification: remove the entire `<script type="application/ld+json">…</script>` block from `<head>`. Replace it with:
```html
  <!-- Intentionally missing: no LocalBusiness JSON-LD schema -->
```

- [ ] **Step 2: Create `audit-signals/no-address.html`**

Comment block:
```html
<!--
  SCENARIO: no-address
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasStreetAddress=false
  EXPECTED FINDINGS: [no_address]
  EXPECTED GRADE: P2
  NOTES: Hours, schema, service area, reviews all present. No street address in body or footer.
         JSON-LD address object also omitted.
-->
```

Modifications:
1. In the JSON-LD block, remove the `"address": { ... }` property (keep `name` and `telephone`)
2. In `#contact`, replace `<p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>` with `<!-- Intentionally missing: no street address -->`
3. In `<footer>`, change `123 Main Street, Northampton, MA` to `Northampton, MA`

- [ ] **Step 3: Create `audit-signals/no-hours.html`**

Comment block:
```html
<!--
  SCENARIO: no-hours
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasBusinessHours=false
  EXPECTED FINDINGS: [no_hours]
  EXPECTED GRADE: P2
  NOTES: Address, schema, service area, reviews all present. Business hours paragraph absent.
-->
```

Modification: remove `<p><strong>Hours:</strong> Mon–Fri 8am–6pm, Sat 9am–3pm</p>` from `#contact`. Replace with `<!-- Intentionally missing: no business hours -->`.

- [ ] **Step 4: Create `audit-signals/no-reviews.html`**

Comment block:
```html
<!--
  SCENARIO: no-reviews
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasReviews=false
  EXPECTED FINDINGS: [no_reviews]
  EXPECTED GRADE: P2
  NOTES: All signals green. The "What Our Customers Say" section with blockquotes is absent.
-->
```

Modification: remove the entire `<section>` containing `<h2>What Our Customers Say</h2>` and the two `<blockquote>` elements. Replace with `<!-- Intentionally missing: no testimonials/reviews section -->`.

- [ ] **Step 5: Create `audit-signals/no-service-area.html`**

Comment block:
```html
<!--
  SCENARIO: no-service-area
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasServiceArea=false
  EXPECTED FINDINGS: [no_service_area]
  EXPECTED GRADE: P2
  NOTES: Address, hours, schema, reviews all present. Service area paragraph removed.
         General "Hampshire County" text in services section removed too.
-->
```

Modifications:
1. Remove `<p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>` from `#contact`
2. Change `throughout Hampshire County` in the Services section to `for residential and commercial customers`

- [ ] **Step 6: Verify all 5 pages in browser**

Open each file directly (`file:///...`). Check:
- `no-schema.html`: View Source → confirm no `application/ld+json` script
- `no-address.html`: no "Main Street" text visible anywhere on page
- `no-hours.html`: no hours text in contact section
- `no-reviews.html`: no testimonials section present
- `no-service-area.html`: no service area sentence in contact section

- [ ] **Step 7: Commit**

```bash
git add audit-signals/no-schema.html audit-signals/no-address.html audit-signals/no-hours.html audit-signals/no-reviews.html audit-signals/no-service-area.html
git commit -m "feat: add absence-signal audit pages (no-schema, no-address, no-hours, no-reviews, no-service-area)"
```

---

### Task 2: Audit-signal pages — presence/modification signals

**Files:**
- Create: `audit-signals/images-no-alt.html`
- Create: `audit-signals/low-contrast.html`
- Create: `audit-signals/small-font.html`
- Create: `audit-signals/duplicate-h1.html`
- Create: `audit-signals/phone-not-linked.html`
- Create: `audit-signals/no-favicon.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 6 isolated-signal URLs

Each file: Enriched Base Template + prepended comment block + described modification.

- [ ] **Step 1: Create `audit-signals/images-no-alt.html`**

Comment block:
```html
<!--
  SCENARIO: images-no-alt
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: imagesWithoutAlt=2
  EXPECTED FINDINGS: [images_no_alt]
  EXPECTED GRADE: P2
  NOTES: Two images present, both with alt="". All other signals green.
-->
```

Modification: replace the single `<img>` in the "Our Work" section with two images, both with `alt=""`:
```html
    <section>
      <h2>Our Work</h2>
      <!-- Intentionally missing alt text on both images -->
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="" width="600" height="1" style="width:100%;max-width:600px;display:block;margin-bottom:0.5rem;">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="" width="600" height="1" style="width:100%;max-width:600px;display:block;">
    </section>
```

- [ ] **Step 2: Create `audit-signals/low-contrast.html`**

Comment block:
```html
<!--
  SCENARIO: low-contrast
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasLowContrastText=true
  EXPECTED FINDINGS: [low_contrast]
  EXPECTED GRADE: P2
  NOTES: Body text set to #aaa on white background — approx 2.3:1 contrast ratio, below WCAG AA 4.5:1.
         All other signals green.
-->
```

Modification: add an inline `<style>` block inside `<head>`, after the stylesheet link:
```html
  <!-- Intentionally low contrast: #aaa on white is ~2.3:1 ratio, below WCAG AA -->
  <style>body { color: #aaa; }</style>
```

- [ ] **Step 3: Create `audit-signals/small-font.html`**

Comment block:
```html
<!--
  SCENARIO: small-font
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: bodyFontSizePx=10
  EXPECTED FINDINGS: [small_font]
  EXPECTED GRADE: P2
  NOTES: Body font-size forced to 10px. All other signals green.
-->
```

Modification: add inside `<head>` after the stylesheet link:
```html
  <!-- Intentionally small font: 10px body text -->
  <style>body { font-size: 10px; }</style>
```

- [ ] **Step 4: Create `audit-signals/duplicate-h1.html`**

Comment block:
```html
<!--
  SCENARIO: duplicate-h1
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: h1Count=2
  EXPECTED FINDINGS: [duplicate_h1]
  EXPECTED GRADE: P2
  NOTES: Two <h1> elements on the page. All other signals green.
-->
```

Modification: in the `<footer>`, change the `<p>` to add a second `<h1>`:
```html
  <footer>
    <!-- Intentionally duplicate H1: second h1 in footer -->
    <h1 style="font-size:1rem;margin:0 0 0.25rem">Pioneer Home Services</h1>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
```

- [ ] **Step 5: Create `audit-signals/phone-not-linked.html`**

Comment block:
```html
<!--
  SCENARIO: phone-not-linked
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: phoneLinkedWithTel=false
  EXPECTED FINDINGS: [phone_not_linked]
  EXPECTED GRADE: P2
  NOTES: Phone number appears as plain text in all locations — no <a href="tel:..."> wrapping it.
         Hero CTA button is a tel: link to keep contact_info signal green.
         Contact section and footer phone are plain text.
-->
```

Modifications:
1. In `#contact`, change `<a href="tel:+14135550100">(413) 555-0100</a>` to `(413) 555-0100` (plain text)
2. In `<footer>`, change `<a href="tel:+14135550100">(413) 555-0100</a>` to `(413) 555-0100` (plain text)
3. Add comment before both: `<!-- Intentionally unlinked: phone as plain text -->`

(Keep the hero `<a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>` as a tel: link to preserve the contact signal.)

- [ ] **Step 6: Create `audit-signals/no-favicon.html`**

Comment block:
```html
<!--
  SCENARIO: no-favicon
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasFavicon=false
  EXPECTED FINDINGS: [no_favicon]
  EXPECTED GRADE: P3
  NOTES: No <link rel="icon"> in <head>. All other signals green.
-->
```

Modification: remove `<link rel="icon" href="/favicon.ico">` from `<head>`. Replace with:
```html
  <!-- Intentionally missing: no favicon link -->
```

- [ ] **Step 7: Verify all 6 pages in browser**

Open each file. Check:
- `images-no-alt.html`: two images visible; right-click → Inspect → both `<img>` have `alt=""`
- `low-contrast.html`: text appears gray/light on white background
- `small-font.html`: body text visibly tiny (≈10px)
- `duplicate-h1.html`: Inspect → two `<h1>` elements present
- `phone-not-linked.html`: phone numbers in contact section and footer are plain text, not clickable links
- `no-favicon.html`: View Source → no `<link rel="icon">`

- [ ] **Step 8: Commit**

```bash
git add audit-signals/images-no-alt.html audit-signals/low-contrast.html audit-signals/small-font.html audit-signals/duplicate-h1.html audit-signals/phone-not-linked.html audit-signals/no-favicon.html
git commit -m "feat: add presence/modification audit-signal pages (images-no-alt, low-contrast, small-font, duplicate-h1, phone-not-linked, no-favicon)"
```

---

### Task 3: Journey probe pages — blocking failures

**Files:**
- Create: `journey/popup-blocks-page.html`
- Create: `journey/chatbot-over-cta.html`
- Create: `journey/video-modal-trap.html`
- Create: `journey/cta-disabled.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 4 journey URLs where a headless probe cannot reach the CTA

- [ ] **Step 1: Create `journey/popup-blocks-page.html`**

```html
<!--
  SCENARIO: popup-blocks-page
  CATEGORY: journey
  SIGNALS TRIGGERED: ctaBlockedByOverlay=true
  EXPECTED FINDINGS: [popup_blocks_cta]
  EXPECTED GRADE: P1
  NOTES: Full-screen modal fires immediately on load. No dismiss button.
         CTA button is rendered in the page beneath the overlay but is unreachable.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
  <style>
    #modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.88);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #modal-box {
      background: #fff;
      padding: 2rem;
      max-width: 420px;
      width: 90%;
      border-radius: 8px;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Intentionally blocking: full-screen modal with no dismiss button -->
  <div id="modal-overlay">
    <div id="modal-box">
      <h2>Special Offer</h2>
      <p>Sign up for our newsletter and get 10% off your first service call.</p>
      <input type="email" placeholder="Your email address"
             style="width:100%;padding:0.5rem;margin:1rem 0;border:1px solid #ccc;border-radius:4px;">
      <button style="background:#2563eb;color:#fff;border:none;padding:0.75rem 2rem;border-radius:4px;font-size:1rem;cursor:pointer;">
        Subscribe
      </button>
      <!-- Intentionally missing: no close/dismiss button -->
    </div>
  </div>

  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `journey/chatbot-over-cta.html`**

```html
<!--
  SCENARIO: chatbot-over-cta
  CATEGORY: journey
  SIGNALS TRIGGERED: ctaBlockedByChatWidget=true
  EXPECTED FINDINGS: [chatbot_blocks_cta]
  EXPECTED GRADE: P2
  NOTES: A fixed-position chat widget is z-indexed over the sticky "Call Now" CTA bar.
         The CTA bar is rendered but the chat button fully overlaps it in the bottom-right corner.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
  <style>
    #sticky-cta {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: #1d4ed8;
      color: #fff;
      text-align: center;
      padding: 0.85rem;
      z-index: 100;
      font-size: 1.05rem;
    }
    #sticky-cta a { color: #fff; font-weight: bold; text-decoration: none; }
    /* Intentionally blocking: chat widget z-index higher than CTA bar */
    #chat-widget {
      position: fixed;
      bottom: 0;
      right: 0;
      width: 220px;
      height: 52px;
      background: #16a34a;
      color: #fff;
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px 0 0 0;
      font-size: 0.95rem;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>

  <!-- Sticky CTA bar — blocked by chat widget below -->
  <div id="sticky-cta">
    <a href="tel:+14135550100">Call Now: (413) 555-0100</a>
  </div>

  <!-- Intentionally blocking: chat widget covers the right portion of the sticky CTA -->
  <div id="chat-widget">💬 Chat with us</div>
</body>
</html>
```

- [ ] **Step 3: Create `journey/video-modal-trap.html`**

```html
<!--
  SCENARIO: video-modal-trap
  CATEGORY: journey
  SIGNALS TRIGGERED: undismissableModalOnLoad=true
  EXPECTED FINDINGS: [modal_trap]
  EXPECTED GRADE: P1
  NOTES: A video modal fires automatically on page load. No close button.
         Clicking outside the modal does nothing. Page content is unreachable.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
  <style>
    #video-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.92);
      z-index: 9999;
      align-items: center;
      justify-content: center;
    }
    #video-modal.open { display: flex; }
    #video-box {
      background: #000;
      width: 90%;
      max-width: 640px;
      aspect-ratio: 16/9;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 1.1rem;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <!-- Intentionally trapping: modal opens on load, no close path -->
  <div id="video-modal">
    <div id="video-box">
      ▶ Watch our intro video
      <!-- Intentionally missing: no × close button -->
    </div>
  </div>

  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>

  <script>
    // Intentionally auto-opens on load with no dismiss mechanism
    window.addEventListener('DOMContentLoaded', function() {
      document.getElementById('video-modal').classList.add('open');
    });
  </script>
</body>
</html>
```

- [ ] **Step 4: Create `journey/cta-disabled.html`**

```html
<!--
  SCENARIO: cta-disabled
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryCtaInteractive=false
  EXPECTED FINDINGS: [cta_disabled]
  EXPECTED GRADE: P2
  NOTES: The main CTA button renders visually as active but has the disabled attribute
         and pointer-events:none. A probe click registers no action.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <!-- Intentionally disabled: styled as active but pointer-events blocked -->
      <button class="btn" disabled style="pointer-events:none;opacity:1;cursor:default;">
        Call (413) 555-0100
      </button>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
```

- [ ] **Step 5: Verify all 4 pages in browser**

- `popup-blocks-page.html`: modal covers entire page; no way to close it
- `chatbot-over-cta.html`: green chat widget overlaps bottom-right of blue CTA bar
- `video-modal-trap.html`: dark video modal covers page immediately; no X button visible
- `cta-disabled.html`: "Call" button renders in the hero but clicking does nothing

- [ ] **Step 6: Commit**

```bash
git add journey/popup-blocks-page.html journey/chatbot-over-cta.html journey/video-modal-trap.html journey/cta-disabled.html
git commit -m "feat: add blocking-failure journey probe pages (popup, chatbot, video-trap, cta-disabled)"
```

---

### Task 4: Journey probe pages — interaction failures

**Files:**
- Create: `journey/form-no-confirmation.html`
- Create: `journey/no-mobile-cta.html`
- Create: `journey/contact-buried.html`
- Create: `journey/multi-step-broken.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 4 journey URLs where a headless probe fails to confirm task completion

- [ ] **Step 1: Create `journey/form-no-confirmation.html`**

```html
<!--
  SCENARIO: form-no-confirmation
  CATEGORY: journey
  SIGNALS TRIGGERED: formConfirmationPresent=false
  EXPECTED FINDINGS: [form_no_confirmation]
  EXPECTED GRADE: P2
  NOTES: Form fields work and the submit button is type="submit", but onsubmit=preventDefault()
         means the page never navigates or shows a success message. A probe clicking submit
         observes no change in page state.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <!-- Intentionally no confirmation: preventDefault stops submit; no success message shown -->
      <form class="contact-form" id="contact-form" onsubmit="event.preventDefault()">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `journey/no-mobile-cta.html`**

```html
<!--
  SCENARIO: no-mobile-cta
  CATEGORY: journey
  SIGNALS TRIGGERED: ctaVisibleAtMobileViewport=false
  EXPECTED FINDINGS: [no_mobile_cta]
  EXPECTED GRADE: P2
  NOTES: Hero CTA button is visible at desktop width (>480px) but hidden via CSS at <=480px.
         A headless probe at mobile viewport finds no actionable CTA in the hero.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
  <!-- Intentionally hides hero CTA on mobile -->
  <style>
    @media (max-width: 480px) {
      .hero .btn { display: none; }
    }
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <!-- Visible on desktop, hidden on mobile via the stylesheet above -->
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Create `journey/contact-buried.html`**

```html
<!--
  SCENARIO: contact-buried
  CATEGORY: journey
  SIGNALS TRIGGERED: contactScrollDepthPx>2000, noContactAnchorInNav=true
  EXPECTED FINDINGS: [contact_buried]
  EXPECTED GRADE: P2
  NOTES: Contact section is ~3200px below the fold. Nav links go to #services and #about
         but not #contact. A probe must scroll past the entire page to find the form.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <!-- Intentionally missing: no #contact anchor in nav -->
      <ul class="nav-links" id="nav-links">
        <li><a href="#services">Services</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#faq">FAQ</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
    </section>

    <section id="services">
      <h2>Our Services</h2>
      <p>We offer a full range of home services throughout Hampshire County.</p>
      <ul>
        <li>Plumbing repairs and installation — leaks, clogs, pipe replacement</li>
        <li>Water heater installation and replacement</li>
        <li>Drain cleaning and hydro-jetting</li>
        <li>Toilet, sink, and faucet installation</li>
        <li>Sump pump installation and service</li>
        <li>Emergency service available 24/7</li>
      </ul>
      <p>All technicians are Massachusetts-licensed and carry full liability insurance. We serve Northampton, Florence, Easthampton, Amherst, and all surrounding Pioneer Valley communities.</p>
      <p>Whether you need a dripping faucet fixed or an entire bathroom repiped, Pioneer Home Services has the experience and equipment to get it done right the first time. Our trucks are fully stocked so most jobs are completed in a single visit.</p>
    </section>

    <section id="about">
      <h2>About Us</h2>
      <p>Pioneer Home Services has been locally owned and operated since 2005. We started as a one-truck operation and have grown to a team of eight licensed technicians — all of them background-checked, drug-tested, and committed to treating your home with respect.</p>
      <p>We don't use subcontractors. Every job is handled by a Pioneer employee who takes personal pride in the work. That's why we can stand behind every job with a 90-day labor warranty.</p>
      <p>Owner Mike Pelletier has been in the trades since 1998 and still takes service calls himself. He built this company on the belief that honest pricing and showing up on time is all it takes to earn a customer for life.</p>
      <p>We're proud members of the Northampton Area Chamber of Commerce and the Western Massachusetts Plumbing Contractors Association. We carry a $2 million general liability policy and all required workers' compensation coverage.</p>
    </section>

    <section>
      <h2>Why Choose Pioneer?</h2>
      <p>There are a lot of plumbers in Hampshire County. Here's why customers keep calling us back:</p>
      <ul>
        <li><strong>Upfront pricing</strong> — We give you a price before we start. No surprises on the invoice.</li>
        <li><strong>On-time arrival</strong> — We call ahead if we're running late. Your time matters.</li>
        <li><strong>Fully stocked trucks</strong> — Most jobs done same day. We carry the parts.</li>
        <li><strong>Licensed and insured</strong> — MA License #12345. $2M liability coverage.</li>
        <li><strong>90-day labor warranty</strong> — If something we fixed breaks again, we come back at no charge.</li>
      </ul>
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Mike and his crew fixed a major pipe leak in our basement on a Sunday evening. Fair price, great work. Can't recommend them enough."</p>
        <cite>— Dave H., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Called at 7am with no hot water. Pioneer was at my door by 9. New water heater installed by noon. Outstanding service."</p>
        <cite>— Linda C., Easthampton</cite>
      </blockquote>
      <blockquote>
        <p>"They fixed a slow drain problem that two other plumbers couldn't solve. Polite, fast, and cleaned up after themselves."</p>
        <cite>— Ryan S., Florence</cite>
      </blockquote>
      <blockquote>
        <p>"Honest pricing, showed up on time, did exactly what they said they would. I've found my plumber for life."</p>
        <cite>— Teri M., Amherst</cite>
      </blockquote>
    </section>

    <section id="faq">
      <h2>Frequently Asked Questions</h2>
      <h3>Do you offer emergency service?</h3>
      <p>Yes. We have a technician on call 24 hours a day, 7 days a week. Emergency rates apply after 6pm and on weekends. Call (413) 555-0100 and press 1 for emergency dispatch.</p>
      <h3>How much does a service call cost?</h3>
      <p>Our standard diagnostic fee is $75, which is waived if you proceed with the repair. We provide a written estimate before any work begins — no surprises.</p>
      <h3>Do you offer financing?</h3>
      <p>Yes, we offer 0% financing for 12 months on jobs over $1,000 through our lending partner. Ask your technician for details.</p>
      <h3>Are your technicians licensed?</h3>
      <p>Yes. All Pioneer technicians hold current Massachusetts plumbing licenses. Our company license number is MA #12345. We carry $2 million in general liability coverage and full workers' compensation insurance.</p>
      <h3>What areas do you serve?</h3>
      <p>We serve Northampton, Florence, Easthampton, Amherst, Hadley, South Hadley, Belchertown, Ware, and surrounding Pioneer Valley communities. If you're unsure whether we cover your area, just call.</p>
      <h3>How soon can you come out?</h3>
      <p>For non-emergencies, we typically schedule within 1–2 business days. For urgent situations during business hours, we often have same-day availability. Emergency calls are dispatched immediately.</p>
    </section>

    <!-- Intentionally buried: contact section has no nav anchor pointing to it -->
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe the work you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 4: Create `journey/multi-step-broken.html`**

```html
<!--
  SCENARIO: multi-step-broken
  CATEGORY: journey
  SIGNALS TRIGGERED: multiStepFormAdvances=false
  EXPECTED FINDINGS: [multi_step_failure]
  EXPECTED GRADE: P1
  NOTES: Two-step quote form. Step 1 renders and fields are fillable.
         "Next" button has onclick="return false" — step 2 never appears.
         A probe filling step 1 and clicking Next observes no state change.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services — Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="Reliable home services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
  <style>
    .form-step { display: none; }
    .form-step.active { display: block; }
    .step-indicator { color: #666; font-size: 0.9rem; margin-bottom: 1rem; }
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#quote">Get a Quote</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="#quote" class="btn">Get a Free Quote</a>
    </section>

    <section id="quote">
      <h2>Get a Free Estimate</h2>
      <div class="contact-form">
        <div id="step1" class="form-step active">
          <p class="step-indicator">Step 1 of 2 — Tell us about the job</p>
          <label for="service">Service needed</label>
          <select id="service" name="service" style="width:100%;padding:0.5rem;margin-bottom:1rem;border:1px solid #ccc;border-radius:4px;">
            <option value="">Select a service...</option>
            <option>Plumbing repair</option>
            <option>Water heater</option>
            <option>Drain cleaning</option>
            <option>Emergency service</option>
            <option>Other</option>
          </select>
          <label for="description">Describe the issue</label>
          <textarea id="description" name="description" placeholder="e.g. Slow kitchen drain, water heater making noise..."></textarea>
          <!-- Intentionally broken: onclick="return false" prevents advancing to step 2 -->
          <button class="btn" onclick="return false">Next: Your Contact Info →</button>
        </div>

        <div id="step2" class="form-step">
          <p class="step-indicator">Step 2 of 2 — Your contact info</p>
          <label for="name">Name</label>
          <input type="text" id="name" name="name" placeholder="Your name">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
          <button type="submit" class="btn">Submit Request</button>
        </div>
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
```

- [ ] **Step 5: Verify all 4 pages in browser**

- `form-no-confirmation.html`: fill the form and click Send — nothing happens (no navigation, no message)
- `no-mobile-cta.html`: resize browser to ≤480px — "Call" button in hero disappears
- `contact-buried.html`: page loads showing hero; must scroll through ~5 content sections to reach the form
- `multi-step-broken.html`: fill Step 1, click "Next" — Step 2 never appears

- [ ] **Step 6: Commit**

```bash
git add journey/form-no-confirmation.html journey/no-mobile-cta.html journey/contact-buried.html journey/multi-step-broken.html
git commit -m "feat: add interaction-failure journey probe pages (form-no-confirmation, no-mobile-cta, contact-buried, multi-step-broken)"
```

---

### Task 5: Outreach composites — P0 and P1 (3 pages)

**Files:**
- Create: `outreach/roofer.html`
- Create: `outreach/hvac.html`
- Create: `outreach/contractor.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 3 outreach URLs covering the P0 and P1 priority tiers

- [ ] **Step 1: Create `outreach/roofer.html`**

```html
<!--
  SCENARIO: roofer
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No <meta name="description">                →  FindingCode: seo_desc
    2. .hamburger has no onclick                   →  FindingCode: broken_navigation_path
    3. Two <img> with src="images/roof-*.jpg"      →  FindingCode: broken_images
  EXPECTED GRADE: P0
  OUTREACH ANGLE: Three critical issues found — missing search description, broken mobile menu,
    and broken gallery images — any one of which costs you leads.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Valley Ridge Roofing — Northampton, MA</title>
  <!-- Intentionally missing: no meta description -->
  <meta property="og:title" content="Valley Ridge Roofing">
  <meta property="og:description" content="Expert roofing services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Valley Ridge Roofing</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <!-- Intentionally broken: no onclick -->
      <button class="hamburger" aria-label="Menu">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Valley Ridge Roofing</h1>
      <p>Northampton's trusted roofing contractor since 1998. Residential and commercial roofing throughout the Pioneer Valley.</p>
      <a href="tel:+14135550200" class="btn">Call (413) 555-0200</a>
    </section>

    <section>
      <h2>Roofing Services</h2>
      <p>Valley Ridge Roofing handles every aspect of your roof — from a minor repair to a full replacement. We work with asphalt shingles, metal roofing, flat roofs, and cedar shakes.</p>
      <ul>
        <li>Full roof replacement</li>
        <li>Leak repair and emergency patching</li>
        <li>Gutter installation and cleaning</li>
        <li>Storm damage assessment and insurance claims</li>
        <li>Skylights and ventilation</li>
        <li>Flat roof systems (TPO, EPDM, modified bitumen)</li>
        <li>Free estimates — no pressure, no obligation</li>
      </ul>
      <p>All work is performed by our own employees — no subcontractors. We're fully licensed (MA License #55432) and insured, with a 10-year workmanship warranty on all full replacements.</p>
    </section>

    <section>
      <h2>Recent Projects</h2>
      <!-- Intentionally broken: image files do not exist -->
      <img src="images/roof-replacement-northampton.jpg" alt="Roof replacement in Northampton" width="600" height="400"
           style="width:100%;max-width:600px;display:block;margin-bottom:0.5rem;">
      <img src="images/roof-repair-easthampton.jpg" alt="Roof repair in Easthampton" width="600" height="400"
           style="width:100%;max-width:600px;display:block;">
    </section>

    <section>
      <h2>Why Valley Ridge?</h2>
      <p>We've been roofing homes and businesses in Hampshire County for over 25 years. We know the climate here — the ice dams, the heavy snow loads, the wind. We spec every job for Pioneer Valley conditions, not generic specs from a manufacturer's brochure.</p>
      <p>Our crews are fast, clean, and respectful of your property. We put down tarps, pick up every nail with a magnet roller, and haul away all old materials. Most residential replacements are completed in a single day.</p>
    </section>

    <section id="contact">
      <h2>Get a Free Estimate</h2>
      <p class="phone-cta">Call now: <a href="tel:+14135550200">(413) 555-0200</a></p>
      <p style="margin-bottom:1.5rem">Fill out the form and we'll schedule a free on-site estimate within 48 hours.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Describe the project</label>
        <textarea id="message" name="message"
          placeholder="e.g. Missing shingles after storm, full replacement needed, gutter repair..."></textarea>
        <button type="submit" class="btn">Request Free Estimate</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Valley Ridge Roofing &mdash; Northampton, MA &mdash; MA License #55432 &mdash;
      <a href="tel:+14135550200">(413) 555-0200</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `outreach/hvac.html`**

```html
<!--
  SCENARIO: hvac
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No <script type="application/ld+json">      →  FindingCode: no_schema
    2. No business hours in contact section        →  FindingCode: no_hours
  EXPECTED GRADE: P1
  OUTREACH ANGLE: Your site isn't showing up in "near me" searches, and customers
    can't tell if you're open — two quick fixes that directly affect inbound calls.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Comfort Zone HVAC — Northampton, MA</title>
  <meta name="description" content="Heating and cooling services in Northampton, MA. Call (413) 555-0300.">
  <meta property="og:title" content="Comfort Zone HVAC">
  <meta property="og:description" content="Heating and cooling services in Northampton, MA.">
  <meta property="og:type" content="website">
  <!-- Intentionally missing: no LocalBusiness JSON-LD schema -->
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Comfort Zone HVAC</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Comfort Zone HVAC</h1>
      <p>Heating and cooling solutions for homes and businesses throughout Hampshire County.</p>
      <a href="tel:+14135550300" class="btn">Call (413) 555-0300</a>
    </section>

    <section>
      <h2>HVAC Services</h2>
      <p>Comfort Zone handles all aspects of home comfort — from an emergency furnace failure in January to a new central AC installation in May.</p>
      <ul>
        <li>Furnace and boiler installation, repair, and maintenance</li>
        <li>Central air conditioning installation and service</li>
        <li>Heat pump systems — installation and maintenance</li>
        <li>Mini-split ductless systems</li>
        <li>Ductwork design, installation, and cleaning</li>
        <li>Air quality solutions — humidifiers, filtration, UV systems</li>
        <li>Emergency heating and cooling service</li>
      </ul>
      <p>We service all major brands: Carrier, Trane, Lennox, Bryant, Goodman, and more. Our technicians are NATE-certified and carry Massachusetts HVAC contractor licenses.</p>
    </section>

    <section>
      <h2>Why Comfort Zone?</h2>
      <p>We've been keeping Pioneer Valley homes comfortable since 2008. Every job comes with a 1-year parts and labor warranty. We offer annual maintenance plans that keep your system running at peak efficiency — and prevent the breakdowns that always seem to happen on the coldest or hottest days.</p>
      <p>We're a Carrier Factory Authorized Dealer, which means we have access to the latest equipment, factory training, and extended warranty programs that we pass along to our customers.</p>
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Our furnace died at 10pm on a Friday in February. Comfort Zone had a tech here by midnight and the heat back on by 2am. Incredible service."</p>
        <cite>— Paul R., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Installed a new heat pump system — professional crew, clean work, explained everything. We're saving $80/month on energy costs."</p>
        <cite>— Karen T., Florence</cite>
      </blockquote>
    </section>

    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 456 King Street, Northampton, MA 01060</p>
      <!-- Intentionally missing: no business hours listed -->
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, Hadley, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550300">(413) 555-0300</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message"
          placeholder="e.g. Furnace making noise, need new AC, annual tune-up..."></textarea>
        <button type="submit" class="btn">Request Service</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Comfort Zone HVAC &mdash; Northampton, MA &mdash;
      <a href="tel:+14135550300">(413) 555-0300</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Create `outreach/contractor.html`**

```html
<!--
  SCENARIO: contractor
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No og: meta tags                            →  FindingCode: no_og
    2. Contact section only reachable by           →  FindingCode: contact_buried
       scrolling past ~3000px; no nav anchor
  EXPECTED GRADE: P1
  OUTREACH ANGLE: Your social media previews are broken, and anyone trying to contact
    you from your website has to scroll past your entire portfolio to find the form.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Berkshire Build &amp; Remodel — Northampton, MA</title>
  <meta name="description" content="Kitchen, bathroom, and home remodeling in Northampton, MA. Call (413) 555-0400.">
  <!-- Intentionally missing: no og:title, og:description, og:type -->
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Berkshire Build &amp; Remodel</a>
      <!-- Intentionally missing: no #contact link in nav -->
      <ul class="nav-links" id="nav-links">
        <li><a href="#services">Services</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#about">About</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Berkshire Build &amp; Remodel</h1>
      <p>Custom kitchens, bathrooms, additions, and whole-home renovations in the Pioneer Valley.</p>
      <a href="tel:+14135550400" class="btn">Call (413) 555-0400</a>
    </section>

    <section id="services">
      <h2>Remodeling Services</h2>
      <p>Berkshire Build & Remodel handles projects of every scale — from a single bathroom refresh to a whole-home transformation. We're a design-build firm, which means we handle design, permits, and construction under one roof.</p>
      <ul>
        <li>Kitchen remodeling — full gut renovations, cabinet refacing, countertop replacement</li>
        <li>Bathroom remodeling — custom tile, walk-in showers, heated floors</li>
        <li>Home additions — room additions, garage conversions, in-law suites</li>
        <li>Basement finishing — home offices, rec rooms, media rooms</li>
        <li>Deck and outdoor living spaces</li>
        <li>Window and door replacement</li>
        <li>Interior and exterior painting</li>
      </ul>
    </section>

    <section id="projects">
      <h2>Recent Projects</h2>
      <p>Every project is different. Here's a sample of what we've built for Pioneer Valley homeowners in the past year.</p>
      <h3>Kitchen Renovation — Northampton</h3>
      <p>Complete gut renovation: new custom cabinets, quartz countertops, tile backsplash, hardwood floors, recessed lighting, and a new island. Project duration: 6 weeks.</p>
      <h3>Master Bath Addition — Easthampton</h3>
      <p>Converted an underutilized bedroom into a master suite with a walk-in closet and spa bathroom featuring a freestanding tub and double vanity. Project duration: 4 weeks.</p>
      <h3>Basement Finishing — Florence</h3>
      <p>Turned an unfinished basement into a home office, a gym area, and a full bath. All permits pulled and inspected. Project duration: 5 weeks.</p>
      <h3>Two-Story Addition — Amherst</h3>
      <p>Added a two-story addition to a 1960s cape: new primary bedroom suite upstairs, expanded living room below. Matched existing trim and siding exactly. Project duration: 12 weeks.</p>
    </section>

    <section id="about">
      <h2>About Berkshire Build &amp; Remodel</h2>
      <p>We've been remodeling homes in Hampshire County since 2002. Owner Jim Bertrand is a licensed general contractor (MA License #78901) who still walks every job site daily. We employ twelve full-time tradespeople and work with a small network of trusted subcontractors for specialty trades.</p>
      <p>We're members of the National Association of the Remodeling Industry (NARI) and the Better Business Bureau. Every project includes a detailed written contract, a fixed-price quote, and a weekly progress update.</p>
      <p>We don't take on more work than we can execute well. Our current lead time is 6–10 weeks, and we maintain that schedule by not overcommitting. When we give you a completion date, we mean it.</p>
    </section>

    <section>
      <h2>What Our Clients Say</h2>
      <blockquote>
        <p>"Jim and his team completely transformed our kitchen. On time, on budget, and the quality is beyond what we hoped for. Highly recommend."</p>
        <cite>— Carol &amp; Mark D., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"We've used Berkshire Build for three projects now. They're professional, communicative, and do beautiful work. They're the only remodelers we'll call."</p>
        <cite>— Steve P., Amherst</cite>
      </blockquote>
    </section>

    <!-- Intentionally buried: contact section reachable only by scrolling past full page -->
    <section id="contact">
      <h2>Start Your Project</h2>
      <p><strong>Address:</strong> 789 Elm Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon–Fri 8am–5pm</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550400">(413) 555-0400</a></p>
      <p style="margin-bottom:1.5rem">Fill out the form and we'll schedule a free in-home consultation.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Tell us about your project</label>
        <textarea id="message" name="message"
          placeholder="e.g. Kitchen renovation, approximately $40k budget, hoping to start in the fall..."></textarea>
        <button type="submit" class="btn">Request Consultation</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Berkshire Build &amp; Remodel &mdash; Northampton, MA &mdash; MA License #78901 &mdash;
      <a href="tel:+14135550400">(413) 555-0400</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 4: Verify all 3 pages in browser**

- `roofer.html`: View Source → no meta description; click hamburger → menu doesn't open; broken images show alt text placeholders
- `hvac.html`: View Source → no og: tags; scroll to contact → no hours listed
- `contractor.html`: View Source → no og: tags; scroll down — contact section only at bottom after all content sections; nav has no Contact link

- [ ] **Step 5: Commit**

```bash
git add outreach/roofer.html outreach/hvac.html outreach/contractor.html
git commit -m "feat: add P0/P1 outreach composites (roofer, hvac, contractor)"
```

---

### Task 6: Outreach composites — P2

**Files:**
- Create: `outreach/painter.html`
- Create: `outreach/tree-service.html`
- Create: `outreach/handyman.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 3 outreach URLs at P2 priority

- [ ] **Step 1: Create `outreach/painter.html`**

```html
<!--
  SCENARIO: painter
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No street address anywhere on page          →  FindingCode: no_address
    2. Portfolio images have alt=""                →  FindingCode: images_no_alt
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your portfolio photos are invisible to search engines and screen
    readers, and there's no address on the site — both make it harder for local
    customers to trust and find you.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Five Star Painting Co — Northampton, MA</title>
  <meta name="description" content="Interior and exterior painting in Northampton, MA. Call (413) 555-0500 for a free estimate.">
  <meta property="og:title" content="Five Star Painting Co">
  <meta property="og:description" content="Interior and exterior painting in Northampton, MA.">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Five Star Painting Co",
    "telephone": "+14135550500"
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Five Star Painting Co</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">Gallery</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Five Star Painting Co</h1>
      <p>Interior and exterior painting for homes and businesses throughout the Pioneer Valley.</p>
      <a href="tel:+14135550500" class="btn">Call (413) 555-0500</a>
    </section>

    <section>
      <h2>Painting Services</h2>
      <p>Five Star Painting handles every painting project from a single accent wall to a full exterior. We use premium paints, prep every surface properly, and clean up completely before we leave.</p>
      <ul>
        <li>Interior painting — walls, ceilings, trim, cabinets</li>
        <li>Exterior painting and staining</li>
        <li>Deck and fence staining</li>
        <li>Drywall repair and patching</li>
        <li>Wallpaper removal</li>
        <li>Color consultation included with every estimate</li>
      </ul>
    </section>

    <section>
      <h2>Our Work</h2>
      <!-- Intentionally missing alt text on portfolio images -->
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="" width="600" height="1" style="width:100%;max-width:600px;display:block;margin-bottom:0.5rem;">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="" width="600" height="1" style="width:100%;max-width:600px;display:block;margin-bottom:0.5rem;">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg="
           alt="" width="600" height="1" style="width:100%;max-width:600px;display:block;">
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Best painters we've used. On time, tidy, and the finished rooms look incredible."</p>
        <cite>— Jennifer M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Painted our entire exterior in two days. Neighbors keep asking who did it."</p>
        <cite>— Bob L., Easthampton</cite>
      </blockquote>
    </section>

    <section id="contact">
      <h2>Get a Free Estimate</h2>
      <!-- Intentionally missing: no street address -->
      <p><strong>Hours:</strong> Mon–Fri 8am–5pm, Sat 9am–2pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550500">(413) 555-0500</a></p>
      <p style="margin-bottom:1.5rem">Fill out the form and we'll schedule a free on-site estimate.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Describe the project</label>
        <textarea id="message" name="message"
          placeholder="e.g. Interior of 3-bedroom house, exterior repaint, deck staining..."></textarea>
        <button type="submit" class="btn">Request Estimate</button>
      </form>
    </section>
  </main>

  <footer>
    <!-- Intentionally missing: no street address in footer -->
    <p>&copy; 2025 Five Star Painting Co &mdash; Northampton, MA &mdash;
      <a href="tel:+14135550500">(413) 555-0500</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `outreach/tree-service.html`**

```html
<!--
  SCENARIO: tree-service
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Body text color: #aaa (low contrast)        →  FindingCode: low_contrast
    2. No service area mentioned anywhere          →  FindingCode: no_service_area
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your site text is hard to read on mobile — and there's no mention
    of which towns you serve, so customers searching locally may not know you cover them.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Tree &amp; Landscape — Northampton, MA</title>
  <meta name="description" content="Tree removal, trimming, and stump grinding in Northampton, MA. Call (413) 555-0600.">
  <meta property="og:title" content="Pioneer Tree &amp; Landscape">
  <meta property="og:description" content="Tree removal, trimming, and stump grinding in Northampton, MA.">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Pioneer Tree & Landscape",
    "telephone": "+14135550600",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "321 Elm Street",
      "addressLocality": "Northampton",
      "addressRegion": "MA"
    }
  }
  </script>
  <!-- Intentionally low contrast: #aaa body text on white -->
  <style>body { color: #aaa; }</style>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Tree &amp; Landscape</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Pioneer Tree &amp; Landscape</h1>
      <p>Professional tree care and landscaping for residential and commercial properties.</p>
      <a href="tel:+14135550600" class="btn">Call (413) 555-0600</a>
    </section>

    <section>
      <h2>Our Services</h2>
      <p>Pioneer Tree & Landscape provides complete tree and landscape care. Our ISA-certified arborists assess every tree before any work begins.</p>
      <ul>
        <li>Tree removal — including large and hazardous trees</li>
        <li>Tree trimming and crown reduction</li>
        <li>Stump grinding and removal</li>
        <li>Emergency storm damage cleanup</li>
        <li>Land clearing for construction</li>
        <li>Hedge trimming and shrub maintenance</li>
        <li>Seasonal cleanup — spring and fall</li>
      </ul>
      <!-- Intentionally missing: no service area or town names -->
      <p>We carry full liability insurance and workers' compensation coverage. All work performed by our own trained employees.</p>
    </section>

    <section>
      <h2>About Pioneer Tree</h2>
      <p>We've been caring for trees and landscapes since 2010. Our team of six includes two ISA-certified arborists. We use professional-grade equipment and follow ANSI A300 pruning standards on every job.</p>
      <p>Free estimates available Monday through Saturday. Emergency service available around the clock for storm damage and hazardous trees.</p>
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Removed a massive oak that was threatening our house. Professional, careful, and cleaned up every branch and chip."</p>
        <cite>— Tom H.</cite>
      </blockquote>
      <blockquote>
        <p>"Fast response after the storm. Had three downed trees cleared within 24 hours. Excellent work."</p>
        <cite>— Maria S.</cite>
      </blockquote>
    </section>

    <section id="contact">
      <h2>Get a Free Estimate</h2>
      <p><strong>Address:</strong> 321 Elm Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon–Sat 7am–6pm</p>
      <!-- Intentionally missing: no service area in contact section -->
      <p class="phone-cta">Call us: <a href="tel:+14135550600">(413) 555-0600</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Describe the work needed</label>
        <textarea id="message" name="message"
          placeholder="e.g. Large oak needs removal, stump grinding, storm debris..."></textarea>
        <button type="submit" class="btn">Request Estimate</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Pioneer Tree &amp; Landscape &mdash; 321 Elm Street, Northampton, MA &mdash;
      <a href="tel:+14135550600">(413) 555-0600</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Create `outreach/handyman.html`**

```html
<!--
  SCENARIO: handyman
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Copyright year 2022 in footer               →  FindingCode: stale_year
    2. No business hours in contact section        →  FindingCode: no_hours
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your site looks like it hasn't been touched in years — the copyright
    is from 2022 — and there are no hours listed, so customers don't know when to call.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Valley Handyman Services — Northampton, MA</title>
  <meta name="description" content="Handyman services in Northampton, MA. Call (413) 555-0700 for a free estimate.">
  <meta property="og:title" content="Valley Handyman Services">
  <meta property="og:description" content="Handyman services in Northampton, MA.">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Valley Handyman Services",
    "telephone": "+14135550700",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "88 Bridge Street",
      "addressLocality": "Northampton",
      "addressRegion": "MA"
    }
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Valley Handyman Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Valley Handyman Services</h1>
      <p>Reliable home repairs and maintenance for Northampton and the Pioneer Valley.</p>
      <a href="tel:+14135550700" class="btn">Call (413) 555-0700</a>
    </section>

    <section>
      <h2>What We Do</h2>
      <p>Valley Handyman tackles the jobs that need doing but keep getting pushed to the weekend — and then the next weekend. We handle small repairs, installations, and maintenance tasks that don't require a specialist.</p>
      <ul>
        <li>Drywall repair and patching</li>
        <li>Door and window repair and weatherstripping</li>
        <li>Deck repair and staining</li>
        <li>Furniture assembly and mounting</li>
        <li>Fixture installation — fans, lights, towel bars</li>
        <li>Tile grout repair and caulking</li>
        <li>Fence repair</li>
        <li>Gutter cleaning</li>
      </ul>
      <p>We're licensed, insured, and background-checked. We show up when we say we will and charge what we quoted.</p>
    </section>

    <section>
      <h2>About Valley Handyman</h2>
      <p>Owner Dan Valle has been doing home repairs professionally since 2014. He started Valley Handyman Services because he kept seeing homeowners stuck waiting weeks for contractors to fix simple things. Dan specializes in the work that falls between DIY and a full contractor — done right, done quickly, at fair prices.</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Fixed six things in one visit that had been on our list for two years. Efficient, professional, reasonable price."</p>
        <cite>— Anne K., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Dan repaired our deck boards and re-stained the whole thing. Looks brand new."</p>
        <cite>— Chris W., Florence</cite>
      </blockquote>
    </section>

    <section id="contact">
      <h2>Book a Visit</h2>
      <p><strong>Address:</strong> 88 Bridge Street, Northampton, MA 01060</p>
      <!-- Intentionally missing: no business hours listed -->
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550700">(413) 555-0700</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">What needs doing?</label>
        <textarea id="message" name="message"
          placeholder="e.g. Drywall repair in bedroom, deck board replacement, door won't close..."></textarea>
        <button type="submit" class="btn">Request a Visit</button>
      </form>
    </section>
  </main>

  <footer>
    <!-- Intentionally stale: copyright year 2022, not current year -->
    <p>&copy; 2022 Valley Handyman Services &mdash; 88 Bridge Street, Northampton, MA &mdash;
      <a href="tel:+14135550700">(413) 555-0700</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 4: Verify all 3 pages in browser**

- `painter.html`: Inspect → 3 portfolio images all have `alt=""`; no street address visible on page
- `tree-service.html`: all body text appears gray/light; no town names in services or contact sections
- `handyman.html`: footer shows `© 2022`; contact section has address but no hours

- [ ] **Step 5: Commit**

```bash
git add outreach/painter.html outreach/tree-service.html outreach/handyman.html
git commit -m "feat: add P2 outreach composites (painter, tree-service, handyman)"
```

---

### Task 7: Outreach composites — P3

**Files:**
- Create: `outreach/pest-control.html`
- Create: `outreach/cleaning-service.html`

**Interfaces:**
- Consumes: `../styles.css`
- Produces: 2 outreach URLs at P3 priority (minor flaws only)

- [ ] **Step 1: Create `outreach/pest-control.html`**

```html
<!--
  SCENARIO: pest-control
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Two <h1> elements on page                   →  FindingCode: duplicate_h1
    2. Body font-size: 10px                        →  FindingCode: small_font
  EXPECTED GRADE: P3
  OUTREACH ANGLE: A couple of minor technical issues are holding back an otherwise
    solid site — small text is hurting readability and a duplicate heading may
    confuse search engines about your primary topic.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Green Shield Pest Control — Northampton, MA</title>
  <meta name="description" content="Pest control services in Northampton, MA. Call (413) 555-0800 for a free inspection.">
  <meta property="og:title" content="Green Shield Pest Control">
  <meta property="og:description" content="Pest control in Northampton, MA.">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Green Shield Pest Control",
    "telephone": "+14135550800",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "200 Main Street",
      "addressLocality": "Northampton",
      "addressRegion": "MA"
    }
  }
  </script>
  <!-- Intentionally small font: 10px body text -->
  <style>body { font-size: 10px; }</style>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Green Shield Pest Control</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Green Shield Pest Control</h1>
      <p>Safe, effective pest management for homes and businesses in the Pioneer Valley.</p>
      <a href="tel:+14135550800" class="btn">Call (413) 555-0800</a>
    </section>

    <section>
      <h2>Pest Control Services</h2>
      <p>Green Shield uses integrated pest management (IPM) — targeting pests while minimizing chemical exposure to your family and pets.</p>
      <ul>
        <li>Rodent control — mice, rats, exclusion work</li>
        <li>Ant and cockroach treatment</li>
        <li>Bed bug inspection and treatment</li>
        <li>Wasp and hornet nest removal</li>
        <li>Wildlife exclusion — squirrels, bats, raccoons</li>
        <li>Termite inspection and treatment</li>
        <li>Seasonal mosquito and tick control</li>
      </ul>
      <p>All treatments are EPA-registered. We're licensed by the Massachusetts Department of Agricultural Resources and carry full liability insurance.</p>
    </section>

    <section>
      <!-- Intentionally duplicate H1: second h1 in a content section -->
      <h1 style="font-size:1.4rem">Why Choose Green Shield?</h1>
      <p>We've been protecting Pioneer Valley homes since 2012. Owner-operated, local, and accountable. We don't use toxic shortcuts, and we stand behind our results with a 30-day re-treatment guarantee.</p>
      <p>Our technicians are licensed applicators who explain every treatment before they start. We give you a full written report after every visit.</p>
    </section>

    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Had a bad mouse problem before winter. Green Shield sealed the entry points and eliminated the problem. Haven't seen one since."</p>
        <cite>— Patricia D., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Used them for a bed bug issue. Professional, thorough, and discrete. Problem solved in two visits."</p>
        <cite>— James K., Amherst</cite>
      </blockquote>
    </section>

    <section id="contact">
      <h2>Schedule a Free Inspection</h2>
      <p><strong>Address:</strong> 200 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon–Fri 8am–5pm, Sat 9am–1pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550800">(413) 555-0800</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Describe the problem</label>
        <textarea id="message" name="message"
          placeholder="e.g. Seeing mice in kitchen, ant trails in bathroom, noticed bed bugs..."></textarea>
        <button type="submit" class="btn">Request Inspection</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Green Shield Pest Control &mdash; 200 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550800">(413) 555-0800</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `outreach/cleaning-service.html`**

```html
<!--
  SCENARIO: cleaning-service
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No testimonials or reviews section          →  FindingCode: no_reviews
    2. Phone numbers shown as plain text,          →  FindingCode: phone_not_linked
       not <a href="tel:..."> links
  EXPECTED GRADE: P3
  OUTREACH ANGLE: There's no social proof on the site, and the phone number
    can't be tapped on mobile — small fixes that could meaningfully increase conversions.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Spotless Home Cleaning — Northampton, MA</title>
  <meta name="description" content="Professional home cleaning services in Northampton, MA. Call (413) 555-0900.">
  <meta property="og:title" content="Spotless Home Cleaning">
  <meta property="og:description" content="Professional home cleaning in Northampton, MA.">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Spotless Home Cleaning",
    "telephone": "+14135550900",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "55 Pleasant Street",
      "addressLocality": "Northampton",
      "addressRegion": "MA"
    }
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Spotless Home Cleaning</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">☰</button>
    </nav>
  </header>

  <main>
    <section class="hero">
      <h1>Spotless Home Cleaning</h1>
      <p>Professional residential and commercial cleaning throughout the Pioneer Valley.</p>
      <!-- Intentionally unlinked: phone as plain text in hero -->
      <a href="#contact" class="btn">Get a Quote</a>
    </section>

    <section>
      <h2>Cleaning Services</h2>
      <p>Spotless Home Cleaning provides reliable, thorough cleaning for homes and small offices. Our teams are trained, bonded, and insured.</p>
      <ul>
        <li>Regular weekly and bi-weekly cleaning</li>
        <li>Deep cleaning — inside appliances, baseboards, windows</li>
        <li>Move-in and move-out cleaning</li>
        <li>Post-construction cleanup</li>
        <li>Airbnb and vacation rental turnover</li>
        <li>Small office cleaning</li>
      </ul>
      <p>We bring all supplies and equipment. All products are EPA Safer Choice certified — safe for children and pets.</p>
    </section>

    <section>
      <h2>About Spotless</h2>
      <p>Spotless Home Cleaning was founded in 2016 by Maria Reyes, who built the company around one principle: show up reliably and clean thoroughly, every single time. Our teams are W-2 employees — not contractors — fully insured and background-checked.</p>
      <p>We serve Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley communities.</p>
    </section>

    <!-- Intentionally missing: no testimonials/reviews section -->

    <section id="contact">
      <h2>Get a Quote</h2>
      <p><strong>Address:</strong> 55 Pleasant Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon–Fri 8am–5pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <!-- Intentionally unlinked: phone as plain text, not tel: href -->
      <p class="phone-cta">Call us: (413) 555-0900</p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" required placeholder="Jane Smith">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">Tell us about your home</label>
        <textarea id="message" name="message"
          placeholder="e.g. 3-bedroom house, need bi-weekly cleaning, first clean on..."></textarea>
        <button type="submit" class="btn">Request Quote</button>
      </form>
    </section>
  </main>

  <footer>
    <!-- Intentionally unlinked: phone in footer as plain text -->
    <p>&copy; 2025 Spotless Home Cleaning &mdash; 55 Pleasant Street, Northampton, MA &mdash;
      (413) 555-0900</p>
  </footer>
</body>
</html>
```

- [ ] **Step 3: Verify both pages in browser**

- `pest-control.html`: body text is visibly tiny (10px); Inspect → two `<h1>` elements
- `cleaning-service.html`: no testimonials section; phone numbers in contact and footer are plain text, not tappable

- [ ] **Step 4: Commit**

```bash
git add outreach/pest-control.html outreach/cleaning-service.html
git commit -m "feat: add P3 outreach composites (pest-control, cleaning-service)"
```

---

### Task 8: Update index.html

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: all 27 new HTML files (must exist before this task)
- Produces: updated registry with all 43 scenarios listed

- [ ] **Step 1: Add 11 new entries to the Audit Signal Pages section**

In `index.html`, append these `<li>` items inside the `<ul>` of the "Audit Signal Pages" `<div class="registry-section">`, after the existing 8 entries:

```html
      <li><a href="audit-signals/no-schema.html">no-schema</a><span>FindingCode: no_schema</span></li>
      <li><a href="audit-signals/no-address.html">no-address</a><span>FindingCode: no_address</span></li>
      <li><a href="audit-signals/no-hours.html">no-hours</a><span>FindingCode: no_hours</span></li>
      <li><a href="audit-signals/no-reviews.html">no-reviews</a><span>FindingCode: no_reviews</span></li>
      <li><a href="audit-signals/no-service-area.html">no-service-area</a><span>FindingCode: no_service_area</span></li>
      <li><a href="audit-signals/images-no-alt.html">images-no-alt</a><span>FindingCode: images_no_alt</span></li>
      <li><a href="audit-signals/low-contrast.html">low-contrast</a><span>FindingCode: low_contrast</span></li>
      <li><a href="audit-signals/small-font.html">small-font</a><span>FindingCode: small_font</span></li>
      <li><a href="audit-signals/duplicate-h1.html">duplicate-h1</a><span>FindingCode: duplicate_h1</span></li>
      <li><a href="audit-signals/phone-not-linked.html">phone-not-linked</a><span>FindingCode: phone_not_linked</span></li>
      <li><a href="audit-signals/no-favicon.html">no-favicon</a><span>FindingCode: no_favicon</span></li>
```

- [ ] **Step 2: Add 8 new entries to the Journey Probe Pages section**

Append to the "Journey Probe Pages" `<ul>`, after the existing 4 entries:

```html
      <li><a href="journey/form-no-confirmation.html">form-no-confirmation</a><span>FindingCode: form_no_confirmation</span></li>
      <li><a href="journey/popup-blocks-page.html">popup-blocks-page</a><span>FindingCode: popup_blocks_cta</span></li>
      <li><a href="journey/chatbot-over-cta.html">chatbot-over-cta</a><span>FindingCode: chatbot_blocks_cta</span></li>
      <li><a href="journey/cta-disabled.html">cta-disabled</a><span>FindingCode: cta_disabled</span></li>
      <li><a href="journey/no-mobile-cta.html">no-mobile-cta</a><span>FindingCode: no_mobile_cta</span></li>
      <li><a href="journey/contact-buried.html">contact-buried</a><span>FindingCode: contact_buried</span></li>
      <li><a href="journey/video-modal-trap.html">video-modal-trap</a><span>FindingCode: modal_trap</span></li>
      <li><a href="journey/multi-step-broken.html">multi-step-broken</a><span>FindingCode: multi_step_failure</span></li>
```

- [ ] **Step 3: Add 8 new entries to the Outreach Composite Pages section**

Append to the "Outreach Composite Pages" `<ul>`, after the existing 3 entries:

```html
      <li><a href="outreach/roofer.html">roofer</a><span>Valley Ridge Roofing — P0 (seo_desc + broken_navigation_path + broken_images)</span></li>
      <li><a href="outreach/hvac.html">hvac</a><span>Comfort Zone HVAC — P1 (no_schema + no_hours)</span></li>
      <li><a href="outreach/contractor.html">contractor</a><span>Berkshire Build &amp; Remodel — P1 (no_og + contact_buried)</span></li>
      <li><a href="outreach/painter.html">painter</a><span>Five Star Painting Co — P2 (no_address + images_no_alt)</span></li>
      <li><a href="outreach/tree-service.html">tree-service</a><span>Pioneer Tree &amp; Landscape — P2 (low_contrast + no_service_area)</span></li>
      <li><a href="outreach/handyman.html">handyman</a><span>Valley Handyman Services — P2 (stale_year + no_hours)</span></li>
      <li><a href="outreach/pest-control.html">pest-control</a><span>Green Shield Pest Control — P3 (duplicate_h1 + small_font)</span></li>
      <li><a href="outreach/cleaning-service.html">cleaning-service</a><span>Spotless Home Cleaning — P3 (no_reviews + phone_not_linked)</span></li>
```

- [ ] **Step 4: Verify index.html in browser**

Open `index.html`. Confirm:
- All three sections show the correct number of entries (audit: 19 total, journey: 12 total, outreach: 11 total)
- All new links are clickable and open the correct page
- No broken anchors (`href="#"` placeholders or typos)

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: update registry — add 27 new scenario entries to index.html"
```
