# Testsite Expansion 2 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 31 new HTML scenario pages to pvw-testsite, filling FindingCode coverage gaps, adding 6 missing journey probes, creating a new `observations/` directory for ObservationCode-only pages, and extending outreach composites to 8 new trade personas.

**Architecture:** Static HTML files — one per scenario. Each file is self-contained with inline JSON-LD schema, inline CSS where needed, and a single stylesheet link. No build step, no JS dependencies. The new `observations/` directory is a new top-level sibling of `audit-signals/`, `journey/`, and `outreach/`.

**Tech Stack:** HTML5, inline CSS, inline ES5 JS, Vercel static hosting.

## Global Constraints

- All pages: `<!DOCTYPE html>`, `lang="en"`, `charset="UTF-8"`, viewport meta tag
- Stylesheet path for all subdirectory pages: `<link rel="stylesheet" href="../styles.css">`
- CSS cascade rule: when a page has an intentional inline `<style>` override, the `<link rel="stylesheet">` MUST come BEFORE the `<style>` tag so the inline rule wins the cascade
- Geography: Pioneer Valley, MA — Northampton, Easthampton, Florence, Amherst
- Phone format: `(413) 555-XXXX` with `href="tel:+14135550XXX"`
- Placeholder image data URI: `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==`
- Comment block at top of every file: `SCENARIO`, `CATEGORY`, `SIGNALS TRIGGERED`, `EXPECTED FINDINGS`, `EXPECTED GRADE`, `NOTES`; observation-category pages also include `EXPECTED OBSERVATIONS`
- Copyright year: **2025** for all pages EXCEPT `outreach/florist.html` and `outreach/locksmith.html` which use **2023** to trigger `stale_year`
- No changes to `clean.html`, `styles.css`, or `api/`

---

### Task 1: Audit-Signal Pages — FindingCode gaps (5 pages)

**Files:**
- Create: `audit-signals/no-title.html`
- Create: `audit-signals/layout-overflow.html`
- Create: `audit-signals/blank-above-fold.html`
- Create: `audit-signals/script-errors.html`
- Create: `audit-signals/mixed-content.html`

- [ ] **Step 1: Write the files**

`audit-signals/no-title.html`:
```html
<!--
  SCENARIO: no-title
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasTitle=false
  EXPECTED FINDINGS: [seo_title]
  EXPECTED GRADE: P2
  NOTES: All enriched-template signals present. <title> tag removed entirely.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally missing: no <title> tag -->
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&#8212; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&#8212; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&#8211;Fri 8am&#8211;6pm, Sat 9am&#8211;3pm</p>
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
    <p>&copy; 2025 Pioneer Home Services &#8212; 123 Main Street, Northampton, MA &#8212;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`audit-signals/layout-overflow.html`:
```html
<!--
  SCENARIO: layout-overflow
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasLayoutOverflow=true
  EXPECTED FINDINGS: [layout_overflow]
  EXPECTED GRADE: P2
  NOTES: All enriched-template signals present. A <pre> block with white-space:nowrap
    and a ~140-char string forces horizontal scroll past the 390px mobile viewport.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
      <!-- Intentionally wide: white-space:nowrap forces horizontal scroll at mobile viewport -->
      <pre style="white-space:nowrap; font-size:0.9rem; margin:1rem 0">Pioneer Home Services &mdash; Serving Northampton, Easthampton, Florence, Amherst, South Hadley, Hadley, and all Hampshire County communities since 2005</pre>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone in the Valley."</p>
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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

`audit-signals/blank-above-fold.html`:
```html
<!--
  SCENARIO: blank-above-fold
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: blankAboveFold=true, blockedCriticalAssetCount>=1
  EXPECTED FINDINGS: [blank_primary_content]
  EXPECTED GRADE: P1
  NOTES: Fires via: blankAboveFold && blockedCriticalAssetCount > 0.
    blankAboveFold=true because: header is display:none (no nav actionables above fold),
    a 2000px spacer pushes real content below fold, <30 chars visible above fold, no images
    or buttons above fold. blockedCriticalAssetCount>0 because nonexistent-extra.css 404s.
    CSS ordering: styles.css link comes first; nonexistent stylesheet and display:none
    override both come after, so the inline style wins the cascade.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
  <!-- Intentionally broken stylesheet: 404 increments blockedCriticalAssetCount -->
  <link rel="stylesheet" href="nonexistent-extra.css">
  <!-- Intentionally hides header: removes all above-fold actionables so blankAboveFold=true -->
  <style>header { display: none; }</style>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <!-- Intentionally pushes all content below fold; aria-hidden excludes from text count -->
    <div style="height:2000px" aria-hidden="true"></div>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team serves Hampshire County with
        same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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

`audit-signals/script-errors.html`:
```html
<!--
  SCENARIO: script-errors
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: runtimeErrorClusterCount=4 (2 uncaught throws + 2 console.error),
    brokenInteractiveControlCount=2
  EXPECTED FINDINGS: [script_errors]
  EXPECTED GRADE: P2
  NOTES: script_errors fires when runtimeErrorClusterCount>=3 && hasUserVisibleTechnicalBreakage.
    hasUserVisibleTechnicalBreakage = brokenInteractiveControlCount > 1 = true (2 broken buttons).
    Buttons are in a content section (not header/nav), so primaryInteractiveFailureCount=0
    and interactive_control_failure FINDING does not fire (observation only).
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
  <!-- Intentionally throws runtime errors: 2 uncaught + 2 console.error = cluster of 4 -->
  <script>
    setTimeout(function() { throw new Error("Gallery module failed to initialize"); }, 100);
    setTimeout(function() { throw new Error("Review carousel failed to load"); }, 200);
    console.error("Font loading error: Unable to load custom font resource");
    console.error("Analytics tracking error: Missing required site ID");
  </script>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>Photo Gallery</h2>
      <p>Browse photos of our recent work. Gallery and carousel failed to load due to a script error.</p>
      <!-- Intentionally broken: onclick="return false" simulates non-primary JS UI breakage -->
      <!-- NOT the primary CTA, so primaryInteractiveFailureCount stays 0 -->
      <button type="button" class="btn" onclick="return false" style="margin-right:0.5rem">View Gallery</button>
      <button type="button" class="btn" onclick="return false">Load More Photos</button>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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

`audit-signals/mixed-content.html`:
```html
<!--
  SCENARIO: mixed-content
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: hasMixedContent=true
  EXPECTED FINDINGS: [mixed_content]
  EXPECTED GRADE: P2
  NOTES: All enriched-template signals present. An <img> with an http:// src on an
    HTTPS-served page is detected statically by the HTTP audit src/href scan.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
      <!-- Intentionally mixed content: http:// image on HTTPS-served page -->
      <img src="http://example.com/placeholder.gif" alt="Home services work photo"
           width="600" height="400" style="width:100%;max-width:600px;display:block;margin-top:1rem">
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone in the Valley."</p>
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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

- [ ] **Step 2: Self-review** &mdash; for each file: (a) confirm comment-block signals match HTML; (b) no accidental second signal (e.g. `blank-above-fold.html` still has schema, tel: link, address, hours, reviews, service area); (c) `blank-above-fold.html` CSS order: `<link styles.css>` then `<link nonexistent>` then `<style>`.

- [ ] **Step 3: Commit**

```
git add audit-signals/no-title.html audit-signals/layout-overflow.html audit-signals/blank-above-fold.html audit-signals/script-errors.html audit-signals/mixed-content.html
git commit -m "feat: add audit-signal pages for seo_title, layout_overflow, blank_primary_content, script_errors, mixed_content"
```

---

### Task 2: Journey Probe Pages &mdash; Contact-Path Failures (3 pages)

**Files:**
- Create: `journey/no-call-path.html`
- Create: `journey/no-email-path.html`
- Create: `journey/no-directions-path.html`

- [ ] **Step 1: Write the files**

`journey/no-call-path.html`:
```html
<!--
  SCENARIO: no-call-path
  CATEGORY: journey
  SIGNALS TRIGGERED: hasClickToCall=false, hasPhone=true (plain text), hasStrongAlternateContact=false
  EXPECTED FINDINGS: [no_call_path, no_click_to_call]
  EXPECTED GRADE: P1
  NOTES: Both findings fire on the same condition: phone text exists but no tel: link
    and no email/form fallback. no_call_path fires because probeTapToCall fails and
    hasStrongAlternateContact=false. no_click_to_call fires because !hasClickToCall &&
    hasPhone && !hasStrongAlternateContact. This double-firing is correct engine behavior.
    No form, no mailto link, no contact page link anywhere on this page.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <!-- Intentionally plain text: no tel: href, so hasClickToCall=false -->
      <p class="phone-cta" style="font-size:1.1rem;font-weight:bold">Call us: (413) 555-0100</p>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team serves Hampshire County with
        same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <!-- Intentionally plain text: no tel: link, no form, no mailto anywhere on page -->
      <p>To reach us, call <strong>(413) 555-0100</strong> during business hours.</p>
    </section>
  </main>
  <footer>
    <!-- Intentionally plain text phone in footer too -->
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash; (413) 555-0100</p>
  </footer>
</body>
</html>
```

`journey/no-email-path.html`:
```html
<!--
  SCENARIO: no-email-path
  CATEGORY: journey
  SIGNALS TRIGGERED: probeEmailContactPath=fail, contactPathTypes includes 'call' (tel: link present)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [no_email_path, limited_contact_paths]
  EXPECTED GRADE: (no promoted finding; engine grades on findings only)
  NOTES: no_email_path FINDING requires: journeyCodes.has('no_email_path') &&
    !hasContactForm && !contactPathTypes.includes('call'). This page has a tel: link,
    so contactPathTypes includes 'call', blocking the promotion to a finding.
    The probe still detects the missing email path as an observation. This page is
    valuable for testing probeEmailContactPath detection even though no finding fires.
    No mailto: link, no contact form, no /contact page link anywhere on this page.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team serves Hampshire County with
        same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <!-- Tel: link present (adds 'call' to contactPathTypes, blocks no_email_path finding) -->
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <!-- Intentionally no form, no mailto:, no /contact link anywhere on page -->
      <p>We are available by phone during business hours. No online form available at this time.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`journey/no-directions-path.html`:
```html
<!--
  SCENARIO: no-directions-path
  CATEGORY: journey
  SIGNALS TRIGGERED: hasAddressSignal=true, probeDirectionsPath=fail
  EXPECTED FINDINGS: [no_directions_path]
  EXPECTED GRADE: P2
  NOTES: no_directions_path fires when journeyCodes.has('no_directions_path') &&
    signals.hasAddressSignal. Street address is visible on page and in JSON-LD schema
    (hasAddressSignal=true), but there is no Google Maps link, no Apple Maps link,
    and no href matching /directions or /location anywhere on the page.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team serves Hampshire County with
        same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <!-- Address is present (hasAddressSignal=true) but no maps link anywhere on page -->
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <!-- Intentionally no maps link: no google.com/maps, no maps.apple.com, no /directions href -->
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

- [ ] **Step 2: Self-review** &mdash; (a) `no-call-path.html`: confirm no tel: href, no form, no mailto anywhere; (b) `no-email-path.html`: confirm tel: link present, no form, no mailto; (c) `no-directions-path.html`: confirm address visible, schema address present, zero maps links.

- [ ] **Step 3: Commit**

```
git add journey/no-call-path.html journey/no-email-path.html journey/no-directions-path.html
git commit -m "feat: add journey pages for no_call_path, no_email_path, no_directions_path"
```

---

### Task 3: Journey Probe Pages &mdash; Form Failures (3 pages)

**Files:**
- Create: `journey/no-lead-form.html`
- Create: `journey/form-validation-broken.html`
- Create: `journey/form-mobile-blocker.html`

- [ ] **Step 1: Write the files**

`journey/no-lead-form.html`:
```html
<!--
  SCENARIO: no-lead-form
  CATEGORY: journey
  SIGNALS TRIGGERED: probeLeadFormUsability=fail (no <form> element found)
  EXPECTED FINDINGS: [no_lead_form]
  EXPECTED GRADE: P2
  NOTES: no_lead_form fires when probeLeadFormUsability finds no <form> element anywhere
    on the page. Only contact path is a tel: link. Page is otherwise clean.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <!-- Intentionally no <form> element anywhere on page: probeLeadFormUsability finds nothing -->
      <p class="phone-cta">Call us to get started: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p>We're available Monday through Friday 8am&ndash;6pm and Saturday 9am&ndash;3pm.
        Call for a same-day free estimate.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`journey/form-validation-broken.html`:
```html
<!--
  SCENARIO: form-validation-broken
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryFormSatisfiable=false (impossible pattern constraint)
  EXPECTED FINDINGS: [form_validation_broken]
  EXPECTED GRADE: P2
  NOTES: form_validation_broken fires when the primary form has a required field with
    a pattern that no realistic input can satisfy. The name field has
    pattern="^IMPOSSIBLE_PATTERN_XYZ$" required — every normal name input fails
    browser validation. The field is fillable but the constraint is unsatisfiable.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <!-- Intentionally broken: pattern can never be satisfied by a real name -->
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required
               pattern="^IMPOSSIBLE_PATTERN_XYZ$"
               placeholder="Your name">
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

`journey/form-mobile-blocker.html`:
```html
<!--
  SCENARIO: form-mobile-blocker
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryFormMobileBlocked=true (min-width:650px on form container)
  EXPECTED FINDINGS: [form_mobile_layout_blocker]
  EXPECTED GRADE: P2
  NOTES: form_mobile_layout_blocker fires when the primary form container has a
    min-width wider than the mobile viewport (390px). With min-width:650px and
    overflow:visible, fields extend off-screen and are partially unreachable on mobile.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below and we'll get back to you within one business day.</p>
      <!-- Intentionally wide container: min-width:650px overflows 390px mobile viewport -->
      <div style="min-width:650px; overflow:visible">
        <form class="contact-form" action="#" method="post">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required placeholder="Your name">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
          <label for="message">How can we help?</label>
          <textarea id="message" name="message" placeholder="Describe the work you need..."></textarea>
          <button type="submit" class="btn">Send Message</button>
        </form>
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `no-lead-form.html`: confirm zero `<form>` elements on page; (b) `form-validation-broken.html`: confirm impossible pattern is on a `required` field; (c) `form-mobile-blocker.html`: confirm `min-width:650px` is on the form wrapper div, not the form itself.

- [ ] **Step 3: Commit**

```
git add journey/no-lead-form.html journey/form-validation-broken.html journey/form-mobile-blocker.html
git commit -m "feat: add journey pages for no_lead_form, form_validation_broken, form_mobile_layout_blocker"
```

---

### Task 4: Observation Signal Pages &mdash; Isolated Set A (4 pages)

All observation pages go in the new `observations/` top-level directory. They produce `ObservationCode` signals but no promoted `FindingCode` findings.

**Files:**
- Create: `observations/service-clarity-gap.html`
- Create: `observations/about-team-gap.html`
- Create: `observations/trust-signal-gap.html`
- Create: `observations/misleading-submit-label.html`

- [ ] **Step 1: Write the files**

`observations/service-clarity-gap.html`:
```html
<!--
  SCENARIO: service-clarity-gap
  CATEGORY: observations
  SIGNALS TRIGGERED: hasServiceClarity=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [service_clarity_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: hasServiceClarity=false when no h1/h2/h3/nav element text matches SERVICE_RE
    (/\b(service|services|what we do|menu|offerings)\b/i) and body text lacks "services",
    "what we do", "menu", "offerings". All headings use generic phrasing. Page has >120
    words so it is not thin. All other enriched-template signals present.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        <!-- Intentionally vague nav labels: no "Services", "What We Do", etc. -->
        <li><a href="#">How We Help</a></li>
        <li><a href="#">Our Work</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <!-- Intentionally avoids SERVICE_RE words in headings and body -->
      <h2>How We Help Homeowners</h2>
      <p>We work with homeowners throughout Hampshire County to keep their homes running
        smoothly. Our licensed technicians handle everything from routine maintenance to
        emergency repairs, arriving on time with the parts they need to get the job done.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning</li>
        <li>Emergency repairs available 24/7</li>
      </ul>
    </section>
    <section>
      <h2>Our Recent Work</h2>
      <p>We've helped hundreds of families across Northampton, Easthampton, Florence, and
        Amherst with everything from small fixes to full system replacements. Here's what
        some of our recent customers had to say about working with us.</p>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone in the Valley."</p>
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the work."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Our Team</h2>
      <p>Family-owned and locally operated since 2005. Our team of licensed technicians
        brings years of hands-on experience to every job. We are fully insured and stand
        behind every project with a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Get in Touch</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Coverage area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
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

`observations/about-team-gap.html`:
```html
<!--
  SCENARIO: about-team-gap
  CATEGORY: observations
  SIGNALS TRIGGERED: hasAboutTeamSignal=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [about_team_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: hasAboutTeamSignal=false when body text contains none of: "about us", "our story",
    "our team", "family owned", "locally owned", "meet the team", "who we are".
    Page has >120 words (non-thin). All other enriched-template signals including
    hasServiceClarity=true (uses "Services" heading) are present.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        <li><a href="#">Pricing</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <h2>Services</h2>
      <p>We offer a full range of home services throughout Hampshire County. Licensed,
        insured, and available for emergencies around the clock.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning and hydro-jetting</li>
        <li>Emergency service available 24/7</li>
      </ul>
    </section>
    <section>
      <h2>Customer Reviews</h2>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone in the Valley."</p>
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <!-- Intentionally no "about us", "our team", "family owned", "locally owned",
         "meet the team", "our story", or "who we are" language anywhere on page -->
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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

`observations/trust-signal-gap.html`:
```html
<!--
  SCENARIO: trust-signal-gap
  CATEGORY: observations
  SIGNALS TRIGGERED: trustSignalCount=1 (only hasBusinessIdentity=true)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [trust_signal_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: trust_signal_gap fires when trustSignalCount < 2. The 7 trust signals are:
    hasBusinessIdentity, hasAddressSignal, hasHoursSignal, hasTestimonialSignal,
    hasServiceClarity, hasServiceAreaSignal, hasAboutTeamSignal.
    This page has title + h1 (hasBusinessIdentity=true, count=1) but lacks all others:
    no address, no hours, no testimonials, no "services" language, no service area,
    no about-team language. Has a contact form to remain non-thin (>120 words total).
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
  <meta name="description" content="We can help with all your home needs. Call us today.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="We can help with all your home needs.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Pioneer Home Services",
    "telephone": "+14135550100"
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <!-- Intentionally vague: avoids service/area/team language -->
        <li><a href="#">What We Do</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <!-- Intentionally generic: no service/area/team/trust language -->
      <p>We can help with your home. Get in touch today.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <!-- Intentionally avoids all trust signal language -->
      <h2>How It Works</h2>
      <p>Call us or fill out the form below. We will get back to you promptly to
        discuss your needs and schedule a visit at a time that works for you. We aim
        to make the process as straightforward as possible from the first call to job
        completion. Our goal is to leave every customer satisfied with the result.</p>
      <p>We handle all types of work around the home. If you have a question about
        whether we can help with something specific, just give us a call and we will
        let you know right away. We are happy to provide guidance even if the job
        turns out to be outside our current scope.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <!-- Intentionally no address, no hours, no service area -->
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll be in touch.</p>
      <form class="contact-form" action="#" method="post">
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
    <p>&copy; 2025 Pioneer Home Services &mdash; <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`observations/misleading-submit-label.html`:
```html
<!--
  SCENARIO: misleading-submit-label
  CATEGORY: observations
  SIGNALS TRIGGERED: primaryFormSuspiciousSubmitLabel=true
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [misleading_submit_label]
  EXPECTED GRADE: (no promoted finding)
  NOTES: misleading_submit_label fires when the primary form submit button does not
    match FINAL_SUBMIT_RE = /\b(submit|send|send message|request quote|request now|
    book now|place order)\b/i. "Continue" does not match — it implies a multi-step
    flow when this is a single-step form. All other enriched-template signals present.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
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
        <!-- Intentionally misleading label: "Continue" does not match FINAL_SUBMIT_RE -->
        <button type="submit" class="btn">Continue</button>
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

- [ ] **Step 2: Self-review** &mdash; (a) `service-clarity-gap.html`: grep body text for "service", "services", "what we do", "menu", "offerings" &mdash; must find zero; (b) `about-team-gap.html`: grep for "about us", "our team", "family owned", "locally owned" &mdash; must find zero; (c) `trust-signal-gap.html`: confirm no address, hours, testimonials, service area, or about-team language; (d) `misleading-submit-label.html`: confirm submit button text is exactly "Continue".

- [ ] **Step 3: Commit**

```
git add observations/service-clarity-gap.html observations/about-team-gap.html observations/trust-signal-gap.html observations/misleading-submit-label.html
git commit -m "feat: add observation pages for service_clarity_gap, about_team_gap, trust_signal_gap, misleading_submit_label"
```

---

### Task 5: Observation Signal Pages &mdash; Isolated Set B (4 pages)

**Files:**
- Create: `observations/duplicate-contact-fields.html`
- Create: `observations/overconstrained-form.html`
- Create: `observations/business-identity-mismatch.html`
- Create: `observations/pricing-intent-gap.html`

- [ ] **Step 1: Write the files**

`observations/duplicate-contact-fields.html`:
```html
<!--
  SCENARIO: duplicate-contact-fields
  CATEGORY: observations
  SIGNALS TRIGGERED: duplicateContactFieldCount=1
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [duplicate_contact_fields]
  EXPECTED GRADE: (no promoted finding)
  NOTES: duplicate_contact_fields fires when duplicateContactFieldCount > 0.
    The form has two type="email" inputs (email + confirm_email), incrementing the count.
    All other enriched-template signals present. Submit label is "Send Message"
    to avoid triggering misleading_submit_label observation.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <!-- Intentionally duplicate: two type="email" fields increments duplicateContactFieldCount -->
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="you@example.com">
        <label for="confirm_email">Confirm Email Address</label>
        <input type="email" id="confirm_email" name="confirm_email" placeholder="you@example.com">
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

`observations/overconstrained-form.html`:
```html
<!--
  SCENARIO: overconstrained-form
  CATEGORY: observations
  SIGNALS TRIGGERED: primaryFormConstraintScore>=4
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [overconstrained_form, misleading_submit_label, duplicate_contact_fields]
  EXPECTED GRADE: (no promoted finding)
  NOTES: constraintScore breakdown: frictionScore from 6 fields (+2) and 5 required (+1)
    = 3 base; +2 for excessiveRequiredFields (>=5 required); +1 for suspicious submit
    label "Continue"; total = 6 >= 4. Also fires misleading_submit_label and
    duplicate_contact_fields as co-observations. No message/textarea field.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Fill out the form below to request a quote.</p>
      <!-- Intentionally overconstrained: 6 fields, 5 required, confirm-email duplicate,
           no message field, suspicious submit label "Continue" -->
      <form class="contact-form" action="#" method="post">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" required placeholder="Your full name">
        <label for="company">Company Name</label>
        <input type="text" id="company" name="company" required placeholder="Your company">
        <label for="address">Service Address</label>
        <input type="text" id="address" name="address" required placeholder="Street address">
        <label for="zip">ZIP Code</label>
        <input type="text" id="zip" name="zip" required placeholder="01060">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" required placeholder="you@example.com">
        <label for="confirm_email">Confirm Email</label>
        <input type="email" id="confirm_email" name="confirm_email" placeholder="you@example.com">
        <button type="submit" class="btn">Continue</button>
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

`observations/business-identity-mismatch.html`:
```html
<!--
  SCENARIO: business-identity-mismatch
  CATEGORY: observations
  SIGNALS TRIGGERED: hasConsistentBusinessIdentity=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [business_identity_mismatch]
  EXPECTED GRADE: (no promoted finding)
  NOTES: business_identity_mismatch fires when title tokens and H1 tokens share no
    3+ character non-stop-word tokens. Title tokens: [summit, pro, services, northampton].
    H1 tokens: [your, trusted, home, improvement, partner]. Zero tokens in common.
    "summit", "pro", "services", "northampton" do not appear in H1 text.
    "your", "trusted", "home", "improvement", "partner" do not appear in title.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally mismatched: title tokens share no words with H1 tokens -->
  <title>Summit Pro Services &mdash; Northampton, MA</title>
  <meta name="description" content="Reliable home improvement services in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Summit Pro Services">
  <meta property="og:description" content="Reliable home improvement services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Summit Pro Services",
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
      <a href="#" class="site-name">Summit Pro Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <!-- Intentionally mismatched H1: no shared tokens with the <title> -->
      <h1>Your Trusted Home Improvement Partner</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer a full range of home improvement services throughout Hampshire County.</p>
      <ul>
        <li>Kitchen and bathroom remodeling</li>
        <li>Flooring installation and refinishing</li>
        <li>Interior and exterior painting</li>
        <li>Deck and porch construction</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Outstanding craftsmanship and on time every day. Very happy with our new kitchen."</p>
        <cite>&mdash; Linda R., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Professional crew, clean work site, finished on schedule. Highly recommend."</p>
        <cite>&mdash; Carlos M., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Locally owned and operated since 2005. Our team of licensed contractors serves
        Hampshire County with quality workmanship and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe the project you have in mind..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Summit Pro Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`observations/pricing-intent-gap.html`:
```html
<!--
  SCENARIO: pricing-intent-gap
  CATEGORY: observations
  SIGNALS TRIGGERED: primaryCtaType='quote', hasPricingIntent=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [pricing_intent_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: pricing_intent_gap fires when !hasPricingIntent && primaryCtaType==='quote'.
    The hero CTA href="/get-estimate" matches PRICING_RE, scoring it as type='quote'.
    choosePrimaryCta scores the hero link higher than the footer tel: link (hero class
    boost), so the quote-type CTA wins. Body text never uses "quote", "estimate",
    "pricing", "price", "cost", or "rate" so hasPricingIntent=false.
    The tel: link is in footer only (no hero class) to ensure the quote CTA wins.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Contact us today.">
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <!-- Intentionally no pricing words in visible text anywhere on page -->
      <p>Serving Northampton and the Pioneer Valley since 2005. Get in touch today.</p>
      <!-- CTA href matches PRICING_RE (/get-estimate) so primaryCtaType='quote' -->
      <!-- Hero class gives this link higher choosePrimaryCta score than footer tel: -->
      <a href="/get-estimate" class="btn hero">Contact Us Today</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <!-- Intentionally avoids: quote, estimate, pricing, price, cost, rate, fee -->
      <p>We offer a full range of home services throughout Hampshire County. Our team
        handles everything from routine maintenance to emergency repairs with
        professional-grade equipment and licensed technicians.</p>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
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
    <!-- Tel: link in footer only (no hero class) so quote-type hero CTA wins primary scoring -->
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `overconstrained-form.html`: count required fields (must be 5+), confirm submit is "Continue", confirm duplicate email fields; (b) `business-identity-mismatch.html`: verify `<title>` is "Summit Pro Services" and `<h1>` is "Your Trusted Home Improvement Partner" &mdash; no shared 3+ char tokens; (c) `pricing-intent-gap.html`: grep body text for "quote", "estimate", "pricing", "price", "cost", "rate" &mdash; must find zero.

- [ ] **Step 3: Commit**

```
git add observations/duplicate-contact-fields.html observations/overconstrained-form.html observations/business-identity-mismatch.html observations/pricing-intent-gap.html
git commit -m "feat: add observation pages for duplicate_contact_fields, overconstrained_form, business_identity_mismatch, pricing_intent_gap"
```

---

### Task 6: Observation Combo Pages (4 pages)

Each combo page clusters multiple ObservationCodes into a realistic multi-flaw pattern for outreach scoring validation.

**Files:**
- Create: `observations/trust-gap-combo.html`
- Create: `observations/form-friction-combo.html`
- Create: `observations/content-gap-combo.html`
- Create: `observations/identity-gap-combo.html`

- [ ] **Step 1: Write the files**

`observations/trust-gap-combo.html`:
```html
<!--
  SCENARIO: trust-gap-combo
  CATEGORY: observations
  SIGNALS TRIGGERED: hasServiceClarity=false, hasAboutTeamSignal=false, trustSignalCount=2
    (hasBusinessIdentity + hasTestimonialSignal only)
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [service_clarity_gap, about_team_gap, trust_signal_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: Minimal "We can help!" page. Has business name/phone/form (non-thin) but no
    services language, no team content, no address, no hours, no service area.
    trustSignalCount=2: hasBusinessIdentity (title+h1 match) + hasTestimonialSignal.
    trust_signal_gap fires at <2, so count=2 means it does NOT fire here.
    Adjust: remove the testimonial so trustSignalCount=1 and trust_signal_gap fires.
    trustSignalCount=1 (hasBusinessIdentity only, no testimonials, no address, no hours,
    no service area, no service clarity, no about team).
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
  <meta name="description" content="We can help with all your home needs. Get in touch today.">
  <meta property="og:title" content="Pioneer Home Services">
  <meta property="og:description" content="We can help with all your home needs.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Pioneer Home Services",
    "telephone": "+14135550100"
  }
  </script>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <!-- Vague: avoids "Services", "What We Do", "About Us", "Our Team" -->
        <li><a href="#">How We Help</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <!-- Generic: no service/area/team anchors -->
      <p>We can help with your home. Friendly, reliable, and ready to assist.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <!-- Avoids SERVICE_RE and ABOUT_TEAM_RE language throughout -->
      <h2>Getting Started Is Easy</h2>
      <p>Call us or fill out the form below. We will get back to you the same day to
        discuss what you need. Our goal is to make the process simple from the very
        first conversation. We are available during regular business hours and can
        often schedule a visit within a day or two of your initial call.</p>
      <p>We have been helping homeowners for years and take pride in doing good work.
        If you are not happy with the result, we will make it right. That is our
        commitment to every customer, no exceptions.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <!-- No address, no hours, no service area (trust signals absent) -->
      <p class="phone-cta">Call: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form and we'll be in touch shortly.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">What do you need help with?</label>
        <textarea id="message" name="message" placeholder="Describe what you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`observations/form-friction-combo.html`:
```html
<!--
  SCENARIO: form-friction-combo
  CATEGORY: observations
  SIGNALS TRIGGERED: duplicateContactFieldCount=1, excessiveRequiredFields=true,
    primaryFormSuspiciousSubmitLabel=true, primaryFormConstraintScore>=4
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [duplicate_contact_fields, overconstrained_form, misleading_submit_label]
  EXPECTED GRADE: (no promoted finding)
  NOTES: Overbuilt form: confirm-email duplicate, 6 required fields (including company
    and zip), submit says "Continue", no message/textarea.
    constraintScore: frictionScore(6 fields=+2, 5 required=+1) + excessiveRequired(+2)
    + suspiciousLabel(+1) = 6 >= 4. All other enriched-template signals present.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
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
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
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
        <cite>&mdash; Sarah M., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Family-owned and operated since 2005. Our team of licensed technicians serves
        Hampshire County with same-day availability and a 100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Request a Quote</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or complete the form below to request a quote.</p>
      <!-- Overbuilt form: 6 fields, 5 required, confirm-email duplicate, no message, "Continue" submit -->
      <form class="contact-form" action="#" method="post">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" required placeholder="Your full name">
        <label for="company">Company Name</label>
        <input type="text" id="company" name="company" required placeholder="Your company">
        <label for="address">Service Address</label>
        <input type="text" id="address" name="address" required placeholder="Street address">
        <label for="zip">ZIP Code</label>
        <input type="text" id="zip" name="zip" required placeholder="01060">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" required placeholder="you@example.com">
        <label for="confirm_email">Confirm Email</label>
        <input type="email" id="confirm_email" name="confirm_email" placeholder="you@example.com">
        <button type="submit" class="btn">Continue</button>
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

`observations/content-gap-combo.html`:
```html
<!--
  SCENARIO: content-gap-combo
  CATEGORY: observations
  SIGNALS TRIGGERED: hasServiceClarity=false, hasPricingIntent=false (primaryCtaType='quote'),
    hasTestimonialSignal=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [service_clarity_gap, pricing_intent_gap, review_signal_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: Quote-CTA page with generic content. Hero CTA href="/get-estimate" makes
    primaryCtaType='quote'. Body avoids pricing words (hasPricingIntent=false). Section
    headings avoid SERVICE_RE words (hasServiceClarity=false). No testimonials or
    reviews anywhere (hasTestimonialSignal=false, triggers review_signal_gap).
    Tel: link in footer only so quote CTA wins primary scoring.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Home Services &mdash; Northampton, MA</title>
  <meta name="description" content="Reliable home services in Northampton, MA. Get in touch today.">
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
        <!-- Avoids SERVICE_RE: no "Services", "What We Do", "Menu", "Offerings" -->
        <li><a href="#">How We Help</a></li>
        <li><a href="#">Our Work</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <!-- Avoids pricing words: no quote, estimate, pricing, price, cost, rate -->
      <p>Serving Northampton and the Pioneer Valley since 2005. Get in touch today.</p>
      <!-- href="/get-estimate" matches PRICING_RE, sets primaryCtaType='quote' -->
      <a href="/get-estimate" class="btn hero">Contact Us Today</a>
    </section>
    <section>
      <!-- Avoids SERVICE_RE words in heading and body -->
      <h2>How We Help</h2>
      <p>We work with homeowners throughout Hampshire County to keep their homes in top
        condition. Our licensed technicians arrive on time and get the job done right.
        We are available for both scheduled appointments and urgent repair calls.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning</li>
        <li>Emergency repairs available 24/7</li>
      </ul>
    </section>
    <!-- Intentionally no testimonials or reviews section: hasTestimonialSignal=false -->
    <section>
      <h2>About Our Team</h2>
      <p>Locally owned and operated since 2005. Our licensed and insured team brings
        years of hands-on experience to every job. We stand behind every project with a
        100% satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Coverage area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p style="margin-bottom:1.5rem">Fill out the form below and we'll get back to you within one business day.</p>
      <form class="contact-form" action="#" method="post">
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
    <!-- Tel: in footer only (no hero class) so quote CTA wins primary scoring -->
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

`observations/identity-gap-combo.html`:
```html
<!--
  SCENARIO: identity-gap-combo
  CATEGORY: observations
  SIGNALS TRIGGERED: hasConsistentBusinessIdentity=false, hasServiceAreaSignal=false,
    hasAboutTeamSignal=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [business_identity_mismatch, service_area_gap, about_team_gap]
  EXPECTED GRADE: (no promoted finding)
  NOTES: Title/H1 name clash: title says "Ridgeline Property Group", H1 says
    "Your Local Home Repair Experts" — no shared 3+ char tokens. No geographic
    coverage text (hasServiceAreaSignal=false). No team/about language anywhere
    (hasAboutTeamSignal=false). All other signals present.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally mismatched: title tokens [ridgeline, property, group, northampton]
       share no 3+ char tokens with H1 tokens [your, local, home, repair, experts] -->
  <title>Ridgeline Property Group &mdash; Northampton, MA</title>
  <meta name="description" content="Home repair and maintenance in Northampton, MA. Call (413) 555-0100.">
  <meta property="og:title" content="Ridgeline Property Group">
  <meta property="og:description" content="Home repair and maintenance in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Ridgeline Property Group",
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
      <a href="#" class="site-name">Ridgeline Property Group</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <!-- Intentionally mismatched H1 -->
      <h1>Your Local Home Repair Experts</h1>
      <p>Fast, reliable repairs and maintenance for homeowners in the Pioneer Valley.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <h2>Services</h2>
      <!-- Intentionally no service area coverage text -->
      <p>We provide a full range of home repair and maintenance services. Our licensed
        technicians handle everything from small fixes to large repairs with professional
        equipment and a commitment to quality workmanship on every job.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning</li>
        <li>Emergency repairs available 24/7</li>
      </ul>
    </section>
    <section>
      <h2>Customer Reviews</h2>
      <blockquote>
        <p>"Fast, professional, and fairly priced. Would recommend to anyone."</p>
        <cite>&mdash; Sarah M.</cite>
      </blockquote>
      <blockquote>
        <p>"Fixed our water heater same day. Very happy with the service."</p>
        <cite>&mdash; Tom K.</cite>
      </blockquote>
    </section>
    <!-- Intentionally no about-us or team section -->
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <!-- Intentionally no service area: no city/town coverage text -->
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below.</p>
      <form class="contact-form" action="#" method="post">
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
    <p>&copy; 2025 Ridgeline Property Group &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `trust-gap-combo.html`: confirm trustSignalCount=1 (only hasBusinessIdentity); (b) `content-gap-combo.html`: grep for "quote", "estimate", "pricing", "price", "cost", "rate" and SERVICE_RE words in headings &mdash; must find zero; (c) `identity-gap-combo.html`: confirm title tokens and H1 tokens share zero 3+ char words.

- [ ] **Step 3: Commit**

```
git add observations/trust-gap-combo.html observations/form-friction-combo.html observations/content-gap-combo.html observations/identity-gap-combo.html
git commit -m "feat: add observation combo pages for trust, form-friction, content-gap, identity clusters"
```

---

### Task 7: Outreach Composites &mdash; Contact-Path (3 pages)

**Files:**
- Create: `outreach/auto-repair.html`
- Create: `outreach/florist.html`
- Create: `outreach/salon.html`

- [ ] **Step 1: Write the files**

`outreach/auto-repair.html`:
```html
<!--
  SCENARIO: auto-repair
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Phone as plain text, no tel: link               -> FindingCode: no_click_to_call
    2. Nav has 7 links with font-size:11px/line-height:1 -> FindingCode: small_tap_targets
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your phone number can't be tapped on mobile, and your nav links are
    too small for most thumbs — two quick fixes that could mean more calls.
  NOTES: no_click_to_call fires when !hasClickToCall && hasPhone &&
    !hasStrongAlternateContact. hasStrongAlternateContact=false because no email and
    no form (only a hero anchor href="#contact"). small_tap_targets fires when >5 nav
    items are styled below minimum tap-target size.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Metro Auto &amp; Service &mdash; Northampton, MA</title>
  <meta name="description" content="Auto repair and service in Northampton, MA. Call (413) 555-0200 for an appointment.">
  <meta property="og:title" content="Metro Auto &amp; Service">
  <meta property="og:description" content="Auto repair and service in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "AutoRepair",
    "name": "Metro Auto & Service",
    "telephone": "+14135550200",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "45 Industrial Drive",
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
      <a href="#" class="site-name">Metro Auto &amp; Service</a>
      <!-- Intentionally 7 small nav links: font-size:11px + line-height:1 = small_tap_targets -->
      <ul class="nav-links" id="nav-links" style="font-size:11px; line-height:1">
        <li><a href="#">Oil Change</a></li>
        <li><a href="#">Brakes</a></li>
        <li><a href="#">Tires</a></li>
        <li><a href="#">Engine</a></li>
        <li><a href="#">Exhaust</a></li>
        <li><a href="#">Inspections</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Metro Auto &amp; Service</h1>
      <p>Full-service auto repair for domestic and import vehicles in Northampton.</p>
      <!-- No tel: link in hero — only a scroll anchor; hasStrongAlternateContact stays false -->
      <a href="#contact" class="btn">Contact Us</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>ASE-certified technicians. We service all makes and models, foreign and domestic.</p>
      <ul>
        <li>Oil and filter changes</li>
        <li>Brake inspection and replacement</li>
        <li>Tire rotation, balancing, and replacement</li>
        <li>Engine diagnostics and repair</li>
        <li>Exhaust system repair</li>
        <li>Massachusetts state inspections</li>
        <li>Heating and A/C service</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Honest shop, fair prices. They diagnosed a noise three other shops missed."</p>
        <cite>&mdash; Mark D., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Quick turnaround on brakes and rotors. Back on the road the same afternoon."</p>
        <cite>&mdash; Priya S., Amherst</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Metro Auto</h2>
      <p>Family-owned since 1998. Our ASE-certified team has decades of combined experience
        keeping Pioneer Valley vehicles running. We offer a 12-month/12,000-mile warranty
        on all parts and labor.</p>
    </section>
    <section id="contact">
      <h2>Schedule Service</h2>
      <p><strong>Address:</strong> 45 Industrial Drive, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 7:30am&ndash;5:30pm, Sat 8am&ndash;1pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Hampshire County</p>
      <!-- Intentionally plain text: no tel: link anywhere on page -->
      <p class="phone-cta">Call us: <strong>(413) 555-0200</strong></p>
      <p>We are available Monday through Friday and Saturday morning for drop-ins and appointments.
        Call during business hours to schedule same-day or next-day service.</p>
    </section>
  </main>
  <footer>
    <!-- Intentionally plain text phone in footer too -->
    <p>&copy; 2025 Metro Auto &amp; Service &mdash; 45 Industrial Drive, Northampton, MA &mdash; (413) 555-0200</p>
  </footer>
</body>
</html>
```

`outreach/florist.html`:
```html
<!--
  SCENARIO: florist
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. No Google Maps / Apple Maps / /directions link     -> FindingCode: no_directions_path
    2. Copyright year 2023                               -> FindingCode: stale_year
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Customers ready to visit can't tap for directions, and the site looks
    a couple of years out of date.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bloom &amp; Co Florist &mdash; Northampton, MA</title>
  <meta name="description" content="Fresh flowers and floral arrangements in Northampton, MA. Call (413) 555-0300.">
  <meta property="og:title" content="Bloom &amp; Co Florist">
  <meta property="og:description" content="Fresh flowers and floral arrangements in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Florist",
    "name": "Bloom & Co Florist",
    "telephone": "+14135550300",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "88 King Street",
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
      <a href="#" class="site-name">Bloom &amp; Co Florist</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Arrangements</a></li>
        <li><a href="#">Weddings</a></li>
        <li><a href="#">Events</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Bloom &amp; Co Florist</h1>
      <p>Fresh flowers and custom arrangements for every occasion in Northampton.</p>
      <a href="tel:+14135550300" class="btn">Call (413) 555-0300</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>From everyday bouquets to full wedding and event florals, Bloom &amp; Co creates
        arrangements that make every moment memorable.</p>
      <ul>
        <li>Fresh-cut bouquets and arrangements</li>
        <li>Wedding florals &mdash; bridal, ceremony, reception</li>
        <li>Corporate and event arrangements</li>
        <li>Sympathy and funeral flowers</li>
        <li>Same-day delivery in the Pioneer Valley</li>
        <li>Custom orders by request</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"The wedding flowers were absolutely stunning. Every guest asked about them."</p>
        <cite>&mdash; Amanda T., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"I order from Bloom &amp; Co every week for our office. Always fresh, always beautiful."</p>
        <cite>&mdash; James R., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Bloom &amp; Co</h2>
      <p>Family-owned and located in downtown Northampton since 2008. Our team of certified
        floral designers works with locally sourced and imported blooms year-round. We
        offer consultations for weddings and large events at no charge.</p>
    </section>
    <section id="contact">
      <h2>Visit Us or Get in Touch</h2>
      <!-- Address present (hasAddressSignal=true) but no maps link anywhere on page -->
      <p><strong>Address:</strong> 88 King Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 9am&ndash;6pm, Sat 9am&ndash;5pm, Sun 10am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550300">(413) 555-0300</a></p>
      <!-- Intentionally no Google Maps, Apple Maps, or /directions link -->
      <p style="margin-bottom:1.5rem">We're located on King Street in downtown Northampton. Or fill out the form below to ask about availability.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">What can we help with?</label>
        <textarea id="message" name="message" placeholder="Tell us about your event or what you're looking for..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <!-- Intentionally stale year: 2023 triggers stale_year finding -->
    <p>&copy; 2023 Bloom &amp; Co Florist &mdash; 88 King Street, Northampton, MA &mdash;
      <a href="tel:+14135550300">(413) 555-0300</a></p>
  </footer>
</body>
</html>
```

`outreach/salon.html`:
```html
<!--
  SCENARIO: salon
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                              -> FindingCode: seo_title
    2. Phone as plain text, no tel: link                -> FindingCode: no_click_to_call
  EXPECTED GRADE: P1
  OUTREACH ANGLE: Your salon doesn't appear in search results at all, and the phone
    number can't be tapped — two issues that cost you walk-in and call traffic every day.
  NOTES: no_click_to_call fires because !hasClickToCall && hasPhone &&
    !hasStrongAlternateContact. hasStrongAlternateContact=false requires no form AND no
    email. This page has a contact form, which would normally set hasStrongAlternateContact=true
    and block no_click_to_call. To isolate no_click_to_call while keeping the form:
    use mailto: for the form action instead of POST, then remove the form and just have
    a plain-text phone. Actually: per engine logic hasStrongAlternateContact = form OR email.
    Since the form is present, no_click_to_call will NOT fire. Remove the form and keep
    only the plain-text phone. Contact section has address/hours but no form, no mailto.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally missing: no <title> tag -->
  <meta name="description" content="Hair salon in Northampton, MA. Book your appointment at Studio 47 Salon.">
  <meta property="og:title" content="Studio 47 Salon">
  <meta property="og:description" content="Hair salon in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "HairSalon",
    "name": "Studio 47 Salon",
    "telephone": "+14135550400",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "47 Center Street",
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
      <a href="#" class="site-name">Studio 47 Salon</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Studio 47 Salon</h1>
      <p>Full-service hair salon in downtown Northampton. Cuts, color, styling, and more.</p>
      <!-- Intentionally plain text: no tel: link so hasClickToCall=false -->
      <p class="phone-cta" style="font-size:1.1rem;font-weight:bold">Call to book: (413) 555-0400</p>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>Studio 47 offers a full menu of hair services for all hair types and styles.</p>
      <ul>
        <li>Cuts &mdash; women's, men's, and children's</li>
        <li>Color, highlights, and balayage</li>
        <li>Blowouts and styling</li>
        <li>Keratin smoothing treatments</li>
        <li>Bridal and special occasion styling</li>
        <li>Deep conditioning treatments</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Best haircut I've had in years. Exactly what I asked for, and she really listened."</p>
        <cite>&mdash; Rachel H., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"My color looks incredible. I've been coming here for three years and won't go anywhere else."</p>
        <cite>&mdash; Diane W., Florence</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Studio 47</h2>
      <p>Locally owned and operated in downtown Northampton. Our stylists are licensed
        professionals with training from top programs in New England. We use
        professional-grade products and offer a complimentary consultation for new clients.</p>
    </section>
    <section id="contact">
      <h2>Book an Appointment</h2>
      <p><strong>Address:</strong> 47 Center Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Tue&ndash;Fri 9am&ndash;7pm, Sat 9am&ndash;5pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <!-- Intentionally plain text: no tel: link, no form, no email anywhere on page -->
      <!-- hasStrongAlternateContact=false (no form, no email), so no_click_to_call fires -->
      <p>To book, call us at <strong>(413) 555-0400</strong> during business hours. Walk-ins welcome when we have availability.</p>
    </section>
  </main>
  <footer>
    <!-- Intentionally plain text phone in footer -->
    <p>&copy; 2025 Studio 47 Salon &mdash; 47 Center Street, Northampton, MA &mdash; (413) 555-0400</p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `auto-repair.html`: count nav links (must be 7), confirm zero tel: hrefs and zero form elements; (b) `florist.html`: grep for "maps.google", "maps.apple", "/directions" &mdash; must find zero; confirm footer year is 2023; (c) `salon.html`: confirm no `<title>` tag, no tel: hrefs, no `<form>` elements.

- [ ] **Step 3: Commit**

```
git add outreach/auto-repair.html outreach/florist.html outreach/salon.html
git commit -m "feat: add outreach composites for auto-repair (P2), florist (P2), salon (P1)"
```

---

### Task 8: Outreach Composites &mdash; New Trades Batch A (3 pages)

**Files:**
- Create: `outreach/towing.html`
- Create: `outreach/locksmith.html`
- Create: `outreach/appliance-repair.html`

- [ ] **Step 1: Write the files**

`outreach/towing.html`:
```html
<!--
  SCENARIO: towing
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                             -> FindingCode: seo_title
    2. Phone as plain text, no tel: link               -> FindingCode: no_click_to_call
    3. Two broken image srcs (empty src)               -> FindingCode: broken_images
  EXPECTED GRADE: P0
  OUTREACH ANGLE: Three critical issues on an emergency-service site — invisible in
    search, phone untappable, and images broken.
  NOTES: P0 = 3+ critical signals. no_click_to_call fires because no tel: link AND
    no form AND no email (hasStrongAlternateContact=false). broken_images fires when
    brokenImageCount >= 2 (both img srcs are empty strings or point to nonexistent paths).
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally missing: no <title> tag -->
  <meta name="description" content="24/7 towing and roadside assistance in Northampton, MA. Call (413) 555-0500.">
  <meta property="og:title" content="Pioneer Towing &amp; Recovery">
  <meta property="og:description" content="24/7 towing and roadside assistance in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "AutomotiveBusiness",
    "name": "Pioneer Towing & Recovery",
    "telephone": "+14135550500",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "500 Bridge Road",
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
      <a href="#" class="site-name">Pioneer Towing &amp; Recovery</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Towing &amp; Recovery</h1>
      <p>24/7 towing and roadside assistance throughout the Pioneer Valley. Fast response times.</p>
      <!-- Intentionally plain text: no tel: link anywhere on page -->
      <p class="phone-cta" style="font-size:1.1rem;font-weight:bold">Call 24/7: (413) 555-0500</p>
    </section>
    <section>
      <h2>Our Services</h2>
      <!-- Intentionally broken images: src="" fires broken_images when count >= 2 -->
      <img src="" alt="Tow truck on highway" width="600" height="350"
           style="width:100%;max-width:600px;display:block;margin-bottom:1rem">
      <p>Pioneer Towing provides reliable towing and roadside services for passenger vehicles,
        motorcycles, and light trucks throughout Hampshire County.</p>
      <ul>
        <li>Local and long-distance towing</li>
        <li>Jump-starts and battery service</li>
        <li>Flat tire changes</li>
        <li>Lockout assistance</li>
        <li>Fuel delivery</li>
        <li>Accident recovery and scene cleanup</li>
        <li>Motorcycle towing</li>
      </ul>
      <img src="" alt="Roadside assistance truck" width="600" height="350"
           style="width:100%;max-width:600px;display:block;margin-top:1rem">
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Showed up in 20 minutes on a Sunday night. Professional and got us home safely."</p>
        <cite>&mdash; Kevin B., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Locked out at 11pm and they were there within 15 minutes. Highly recommend."</p>
        <cite>&mdash; Elena M., Amherst</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Pioneer Towing</h2>
      <p>Family-owned since 2003. Our drivers are licensed, insured, and trained in safe
        vehicle recovery. We operate 24 hours a day, 365 days a year across Hampshire
        and Franklin counties.</p>
    </section>
    <section id="contact">
      <h2>Call for Service</h2>
      <p><strong>Address:</strong> 500 Bridge Road, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> 24 hours a day, 7 days a week</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Amherst, Florence, Hadley, and all Hampshire County</p>
      <!-- Intentionally no tel: link, no form, no email: hasStrongAlternateContact=false -->
      <p>For immediate service, call us at <strong>(413) 555-0500</strong>. We respond to all calls around the clock.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Towing &amp; Recovery &mdash; 500 Bridge Road, Northampton, MA &mdash; (413) 555-0500</p>
  </footer>
</body>
</html>
```

`outreach/locksmith.html`:
```html
<!--
  SCENARIO: locksmith
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Missing <title> tag                             -> FindingCode: seo_title
    2. No service area language anywhere               -> ObservationCode: service_area_gap
    3. Copyright year 2023                             -> FindingCode: stale_year
  EXPECTED GRADE: P1
  OUTREACH ANGLE: No title tag means no search presence, and there's no mention of
    which towns you cover.
  NOTES: service_area_gap is an observation (not a promoted finding). seo_title and
    stale_year are the two promoted findings producing the P1 grade.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Intentionally missing: no <title> tag -->
  <meta name="description" content="Locksmith services in Northampton, MA. Call (413) 555-0700.">
  <meta property="og:title" content="Capital Lock &amp; Key">
  <meta property="og:description" content="Locksmith services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Locksmith",
    "name": "Capital Lock & Key",
    "telephone": "+14135550700",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "210 Pleasant Street",
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
      <a href="#" class="site-name">Capital Lock &amp; Key</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Capital Lock &amp; Key</h1>
      <p>Professional locksmith services — residential, commercial, and automotive.</p>
      <a href="tel:+14135550700" class="btn">Call (413) 555-0700</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>Capital Lock &amp; Key provides fast, reliable locksmith services for homes,
        businesses, and vehicles. Licensed and insured.</p>
      <ul>
        <li>Residential lockouts and rekeying</li>
        <li>Commercial lock installation and repair</li>
        <li>Automotive lockouts and key duplication</li>
        <li>High-security lock upgrades</li>
        <li>Master key systems</li>
        <li>Safe opening and combination changes</li>
      </ul>
      <!-- Intentionally no service area: no town names, no "we serve X" language -->
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Locked out late at night and they arrived within 30 minutes. Professional and fair."</p>
        <cite>&mdash; Susan C.</cite>
      </blockquote>
      <blockquote>
        <p>"Rekeyed our entire office after a staff change. Fast, thorough, and good value."</p>
        <cite>&mdash; Michael T.</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Capital Lock &amp; Key</h2>
      <p>Locally owned and operated since 2001. Our licensed locksmiths bring 20+ years
        of experience to every job. We carry full liability insurance and back all work
        with a satisfaction guarantee.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 210 Pleasant Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Sat 8am&ndash;6pm, emergency calls 24/7</p>
      <!-- Intentionally no service area text anywhere on page -->
      <p class="phone-cta">Call us: <a href="tel:+14135550700">(413) 555-0700</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe your locksmith need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
  <footer>
    <!-- Intentionally stale year: 2023 triggers stale_year finding -->
    <p>&copy; 2023 Capital Lock &amp; Key &mdash; 210 Pleasant Street, Northampton, MA &mdash;
      <a href="tel:+14135550700">(413) 555-0700</a></p>
  </footer>
</body>
</html>
```

`outreach/appliance-repair.html`:
```html
<!--
  SCENARIO: appliance-repair
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Form field with impossible pattern constraint   -> FindingCode: form_validation_broken
    2. <pre> block with white-space:nowrap             -> FindingCode: layout_overflow
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your quote form rejects every submission, and the page scrolls
    sideways on mobile.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Valley Appliance Repair &mdash; Northampton, MA</title>
  <meta name="description" content="Appliance repair in Northampton, MA. Call (413) 555-0900 for same-day service.">
  <meta property="og:title" content="Valley Appliance Repair">
  <meta property="og:description" content="Appliance repair in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Valley Appliance Repair",
    "telephone": "+14135550900",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "78 Locust Street",
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
      <a href="#" class="site-name">Valley Appliance Repair</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Valley Appliance Repair</h1>
      <p>Factory-trained technicians for major appliance brands throughout the Pioneer Valley.</p>
      <a href="tel:+14135550900" class="btn">Call (413) 555-0900</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We repair all major brands including GE, Whirlpool, Samsung, LG, Bosch, and
        Maytag. Same-day and next-day appointments available.</p>
      <ul>
        <li>Refrigerator and freezer repair</li>
        <li>Washer and dryer repair</li>
        <li>Dishwasher repair</li>
        <li>Oven, range, and cooktop repair</li>
        <li>Microwave repair</li>
        <li>Garbage disposal replacement</li>
      </ul>
      <!-- Intentionally wide: white-space:nowrap forces horizontal scroll at 390px viewport -->
      <pre style="white-space:nowrap; font-size:0.85rem; margin:1rem 0">Valley Appliance Repair &mdash; Factory-certified technicians for GE, Whirlpool, Samsung, LG, Bosch, Maytag, KitchenAid, and Frigidaire</pre>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Fixed our refrigerator same day. The tech was knowledgeable and had the part on the truck."</p>
        <cite>&mdash; Donna P., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Washer wouldn't spin. They diagnosed and fixed it in under an hour. Great service."</p>
        <cite>&mdash; Craig S., Easthampton</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Us</h2>
      <p>Locally owned since 2009. Our factory-certified technicians have the training and
        parts inventory to fix most appliances on the first visit. All repairs carry a
        90-day parts and labor warranty.</p>
    </section>
    <section id="contact">
      <h2>Request a Repair</h2>
      <p><strong>Address:</strong> 78 Locust Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;5pm, Sat 9am&ndash;1pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550900">(413) 555-0900</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below to request a quote.</p>
      <form class="contact-form" action="#" method="post">
        <!-- Intentionally broken: impossible pattern blocks all realistic submissions -->
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required
               pattern="^IMPOSSIBLE_PATTERN_XYZ$"
               placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="appliance">Appliance Type</label>
        <input type="text" id="appliance" name="appliance" placeholder="e.g. Refrigerator, Washer">
        <label for="message">Describe the problem</label>
        <textarea id="message" name="message" placeholder="What is the appliance doing (or not doing)?"></textarea>
        <button type="submit" class="btn">Request Repair</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Valley Appliance Repair &mdash; 78 Locust Street, Northampton, MA &mdash;
      <a href="tel:+14135550900">(413) 555-0900</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `towing.html`: confirm no `<title>`, zero tel: hrefs, zero form elements, two `src=""` images; (b) `locksmith.html`: confirm no `<title>`, footer year 2023, grep for Northampton/Easthampton/Florence/Amherst as service area coverage &mdash; must find zero in body text; (c) `appliance-repair.html`: confirm impossible pattern on required field and pre block with white-space:nowrap.

- [ ] **Step 3: Commit**

```
git add outreach/towing.html outreach/locksmith.html outreach/appliance-repair.html
git commit -m "feat: add outreach composites for towing (P0), locksmith (P1), appliance-repair (P2)"
```

---

### Task 9: Outreach Composites &mdash; New Trades Batch B (2 pages)

**Files:**
- Create: `outreach/catering.html`
- Create: `outreach/moving.html`

- [ ] **Step 1: Write the files**

`outreach/catering.html`:
```html
<!--
  SCENARIO: catering
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. Form container min-width:650px                  -> FindingCode: form_mobile_layout_blocker
    2. No service area language anywhere               -> ObservationCode: service_area_gap
  EXPECTED GRADE: P2
  OUTREACH ANGLE: Your booking form breaks on mobile screens, and there's no mention
    of where you cater.
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Valley Catering Co &mdash; Northampton, MA</title>
  <meta name="description" content="Catering services in Northampton, MA. Call (413) 555-1000 for a quote.">
  <meta property="og:title" content="Valley Catering Co">
  <meta property="og:description" content="Catering services in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FoodEstablishment",
    "name": "Valley Catering Co",
    "telephone": "+14135551000",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "330 Damon Road",
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
      <a href="#" class="site-name">Valley Catering Co</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="#">Menus</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Valley Catering Co</h1>
      <p>Full-service catering for corporate events, weddings, and private parties.</p>
      <a href="tel:+14135551000" class="btn">Call (413) 555-1000</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <!-- Intentionally no service area: no city/town coverage language -->
      <p>Valley Catering Co handles events of all sizes, from intimate gatherings of
        20 to large corporate functions of 500+. Our team manages setup, service,
        and cleanup so you can focus on your guests.</p>
      <ul>
        <li>Corporate lunches and dinners</li>
        <li>Wedding receptions and rehearsal dinners</li>
        <li>Private parties and milestone celebrations</li>
        <li>Boxed lunch and drop-off catering</li>
        <li>Buffet and plated service available</li>
        <li>Dietary accommodations: vegetarian, vegan, gluten-free</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"The food was exceptional and the team handled everything flawlessly. Our guests raved about it."</p>
        <cite>&mdash; Patricia G., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"We use Valley Catering for all our company events. Reliable, delicious, and easy to work with."</p>
        <cite>&mdash; Robert L., Amherst</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Valley Catering</h2>
      <p>Locally owned and operated since 2011. Our team of professional chefs and event
        staff has catered hundreds of events across western Massachusetts. We source
        ingredients locally whenever possible and create custom menus for every event.</p>
    </section>
    <section id="contact">
      <h2>Request a Quote</h2>
      <p><strong>Address:</strong> 330 Damon Road, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 9am&ndash;5pm</p>
      <!-- Intentionally no service area: no towns covered mentioned -->
      <p class="phone-cta">Call us: <a href="tel:+14135551000">(413) 555-1000</a></p>
      <p style="margin-bottom:1.5rem">Fill out the form below to request a catering quote for your event.</p>
      <!-- Intentionally wide container: min-width:650px overflows 390px mobile viewport -->
      <div style="min-width:650px; overflow:visible">
        <form class="contact-form" action="#" method="post">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required placeholder="Your name">
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
          <label for="event_date">Event Date</label>
          <input type="date" id="event_date" name="event_date">
          <label for="guest_count">Estimated Guest Count</label>
          <input type="number" id="guest_count" name="guest_count" placeholder="e.g. 75">
          <label for="message">Tell us about your event</label>
          <textarea id="message" name="message" placeholder="Type of event, venue, dietary needs..."></textarea>
          <button type="submit" class="btn">Request Quote</button>
        </form>
      </div>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Valley Catering Co &mdash; 330 Damon Road, Northampton, MA &mdash;
      <a href="tel:+14135551000">(413) 555-1000</a></p>
  </footer>
</body>
</html>
```

`outreach/moving.html`:
```html
<!--
  SCENARIO: moving
  CATEGORY: outreach
  INTENTIONAL FLAWS:
    1. 7 nav links with font-size:11px/line-height:1   -> FindingCode: small_tap_targets
    2. Form submit says "Continue"                     -> ObservationCode: misleading_submit_label
  EXPECTED GRADE: P3
  OUTREACH ANGLE: Several buttons are too small to tap reliably, and your form's submit
    button doesn't clearly signal "send my request."
-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pioneer Moving Co &mdash; Northampton, MA</title>
  <meta name="description" content="Local and long-distance moving in Northampton, MA. Call (413) 555-1100 for a free quote.">
  <meta property="og:title" content="Pioneer Moving Co">
  <meta property="og:description" content="Local and long-distance moving in Northampton, MA.">
  <meta property="og:type" content="website">
  <link rel="icon" href="/favicon.ico">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "MovingCompany",
    "name": "Pioneer Moving Co",
    "telephone": "+14135551100",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "150 Hatfield Street",
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
      <a href="#" class="site-name">Pioneer Moving Co</a>
      <!-- Intentionally 7 small nav links: font-size:11px + line-height:1 = small_tap_targets -->
      <ul class="nav-links" id="nav-links" style="font-size:11px; line-height:1">
        <li><a href="#">Local Moving</a></li>
        <li><a href="#">Long Distance</a></li>
        <li><a href="#">Packing</a></li>
        <li><a href="#">Storage</a></li>
        <li><a href="#">Commercial</a></li>
        <li><a href="#">Piano Moving</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="hamburger" aria-label="Menu"
        onclick="document.getElementById('nav-links').classList.toggle('open')">&#9776;</button>
    </nav>
  </header>
  <main>
    <section class="hero">
      <h1>Pioneer Moving Co</h1>
      <p>Local and long-distance moving services for homes and businesses in the Pioneer Valley.</p>
      <a href="tel:+14135551100" class="btn">Call (413) 555-1100</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>Pioneer Moving Co offers professional moving services for residential and commercial
        clients. Licensed, insured, and equipped for moves of any size.</p>
      <ul>
        <li>Local moves in Hampshire and Franklin counties</li>
        <li>Long-distance moves statewide and out of state</li>
        <li>Full-service packing and unpacking</li>
        <li>Short and long-term storage</li>
        <li>Commercial and office relocations</li>
        <li>Specialty moving: pianos, antiques, fine art</li>
        <li>Free in-home estimates</li>
      </ul>
    </section>
    <section>
      <h2>What Our Customers Say</h2>
      <blockquote>
        <p>"Three-bedroom move handled in one day. Crew was careful, fast, and professional."</p>
        <cite>&mdash; Barbara H., Northampton</cite>
      </blockquote>
      <blockquote>
        <p>"Moved our office over a weekend with zero downtime. Excellent team."</p>
        <cite>&mdash; Steven N., Amherst</cite>
      </blockquote>
    </section>
    <section>
      <h2>About Pioneer Moving</h2>
      <p>Family-owned since 2007. Our crew of professional movers serves Hampshire and
        Franklin counties with a commitment to careful handling and on-time delivery.
        We carry full cargo insurance and offer binding estimates.</p>
    </section>
    <section id="contact">
      <h2>Get a Free Quote</h2>
      <p><strong>Address:</strong> 150 Hatfield Street, Northampton, MA 01060</p>
      <p><strong>Hours:</strong> Mon&ndash;Fri 8am&ndash;6pm, Sat 9am&ndash;3pm</p>
      <p><strong>Service area:</strong> Northampton, Easthampton, Florence, Amherst, and surrounding Pioneer Valley towns</p>
      <p class="phone-cta">Call us: <a href="tel:+14135551100">(413) 555-1100</a></p>
      <p style="margin-bottom:1.5rem">Or fill out the form below for a free moving quote.</p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" placeholder="(413) 555-xxxx">
        <label for="move_from">Moving From</label>
        <input type="text" id="move_from" name="move_from" placeholder="Current address or city">
        <label for="move_to">Moving To</label>
        <input type="text" id="move_to" name="move_to" placeholder="Destination address or city">
        <label for="message">Additional details</label>
        <textarea id="message" name="message" placeholder="Approximate move date, size of home, special items..."></textarea>
        <!-- Intentionally misleading label: "Continue" does not match FINAL_SUBMIT_RE -->
        <button type="submit" class="btn">Continue</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Moving Co &mdash; 150 Hatfield Street, Northampton, MA &mdash;
      <a href="tel:+14135551100">(413) 555-1100</a></p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Self-review** &mdash; (a) `catering.html`: confirm `min-width:650px` on the wrapper div (not the form element itself); grep for town names as service area coverage &mdash; must find zero in body text; (b) `moving.html`: count nav links (must be 7), confirm submit button text is "Continue".

- [ ] **Step 3: Commit**

```
git add outreach/catering.html outreach/moving.html
git commit -m "feat: add outreach composites for catering (P2), moving (P3)"
```

---

### Task 10: Registry Update &mdash; index.html (31 new entries)

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add Audit Signals entries**

Open `index.html`. Find the `<ul>` under `<h2>Audit Signals</h2>`. Append these 5 entries after the last existing `<li>` in that list:

```html
<li><a href="audit-signals/no-title.html">no-title</a><span>seo_title</span></li>
<li><a href="audit-signals/layout-overflow.html">layout-overflow</a><span>layout_overflow</span></li>
<li><a href="audit-signals/blank-above-fold.html">blank-above-fold</a><span>blank_primary_content</span></li>
<li><a href="audit-signals/script-errors.html">script-errors</a><span>script_errors</span></li>
<li><a href="audit-signals/mixed-content.html">mixed-content</a><span>mixed_content</span></li>
```

- [ ] **Step 2: Add Journey Probe entries**

Find the `<ul>` under `<h2>Journey Probes</h2>`. Append these 6 entries after the last existing `<li>`:

```html
<li><a href="journey/no-call-path.html">no-call-path</a><span>no_call_path + no_click_to_call</span></li>
<li><a href="journey/no-email-path.html">no-email-path</a><span>no_email_path (observation only)</span></li>
<li><a href="journey/no-directions-path.html">no-directions-path</a><span>no_directions_path</span></li>
<li><a href="journey/no-lead-form.html">no-lead-form</a><span>no_lead_form</span></li>
<li><a href="journey/form-validation-broken.html">form-validation-broken</a><span>form_validation_broken</span></li>
<li><a href="journey/form-mobile-blocker.html">form-mobile-blocker</a><span>form_mobile_layout_blocker</span></li>
```

- [ ] **Step 3: Add Outreach Composites entries**

Find the `<ul>` under `<h2>Outreach Composites</h2>`. Append these 8 entries after the last existing `<li>`:

```html
<li><a href="outreach/auto-repair.html">auto-repair</a><span>no_click_to_call + small_tap_targets (P2)</span></li>
<li><a href="outreach/florist.html">florist</a><span>no_directions_path + stale_year (P2)</span></li>
<li><a href="outreach/salon.html">salon</a><span>seo_title + no_click_to_call (P1)</span></li>
<li><a href="outreach/towing.html">towing</a><span>seo_title + no_click_to_call + broken_images (P0)</span></li>
<li><a href="outreach/locksmith.html">locksmith</a><span>seo_title + stale_year + service_area_gap (P1)</span></li>
<li><a href="outreach/appliance-repair.html">appliance-repair</a><span>form_validation_broken + layout_overflow (P2)</span></li>
<li><a href="outreach/catering.html">catering</a><span>form_mobile_layout_blocker + service_area_gap (P2)</span></li>
<li><a href="outreach/moving.html">moving</a><span>small_tap_targets + misleading_submit_label (P3)</span></li>
```

- [ ] **Step 4: Add new Observation Signals section**

Find the closing `</main>` tag. Insert a new section immediately before it:

```html
<section>
  <h2>Observation Signals</h2>
  <ul>
    <li><a href="observations/service-clarity-gap.html">service-clarity-gap</a><span>service_clarity_gap</span></li>
    <li><a href="observations/about-team-gap.html">about-team-gap</a><span>about_team_gap</span></li>
    <li><a href="observations/trust-signal-gap.html">trust-signal-gap</a><span>trust_signal_gap</span></li>
    <li><a href="observations/misleading-submit-label.html">misleading-submit-label</a><span>misleading_submit_label</span></li>
    <li><a href="observations/duplicate-contact-fields.html">duplicate-contact-fields</a><span>duplicate_contact_fields</span></li>
    <li><a href="observations/overconstrained-form.html">overconstrained-form</a><span>overconstrained_form</span></li>
    <li><a href="observations/business-identity-mismatch.html">business-identity-mismatch</a><span>business_identity_mismatch</span></li>
    <li><a href="observations/pricing-intent-gap.html">pricing-intent-gap</a><span>pricing_intent_gap</span></li>
    <li><a href="observations/trust-gap-combo.html">trust-gap-combo</a><span>service_clarity_gap + about_team_gap + trust_signal_gap</span></li>
    <li><a href="observations/form-friction-combo.html">form-friction-combo</a><span>duplicate_contact_fields + overconstrained_form + misleading_submit_label</span></li>
    <li><a href="observations/content-gap-combo.html">content-gap-combo</a><span>service_clarity_gap + pricing_intent_gap + review_signal_gap</span></li>
    <li><a href="observations/identity-gap-combo.html">identity-gap-combo</a><span>business_identity_mismatch + service_area_gap + about_team_gap</span></li>
  </ul>
</section>
```

- [ ] **Step 5: Verify counts**

After editing, count list items in each section:
- Audit Signals: should be 24 (19 original + 5 new)
- Journey Probes: should be 18 (12 original + 6 new)
- Outreach Composites: should be 19 (11 original + 8 new)
- Observation Signals: should be 12 (all new)
- Total `<li>` elements: should be 74

- [ ] **Step 6: Commit**

```
git add index.html
git commit -m "feat: update registry — add 31 new scenario entries and Observation Signals section to index.html"
```

---

## Self-Review Checklist

After all tasks are complete, verify:

- [ ] All 31 new files exist in the correct directories
- [ ] `observations/` directory was created and contains 12 files
- [ ] No page has accidental duplicate signals (run the audit engine on a sample)
- [ ] CSS ordering is correct in `blank-above-fold.html` (`<link styles.css>` → `<link nonexistent.css>` → `<style>`)
- [ ] `florist.html` and `locksmith.html` footers show 2023; all others show 2025
- [ ] `auto-repair.html` and `salon.html` have zero tel: hrefs and zero `<form>` elements
- [ ] `no-email-path.html` has a tel: link (intentional — finding blocked, observation only)
- [ ] `trust-gap-combo.html` has no testimonials (so trustSignalCount stays 1, not 2)
- [ ] index.html total `<li>` count = 74
