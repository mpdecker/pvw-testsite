#!/usr/bin/env python3
"""Generate Expansion 3 new scenario HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEAD = """  <meta charset="UTF-8">
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
  <link rel="stylesheet" href="../styles.css">"""

NAV = """  <header>
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
  </header>"""

CONTACT = """    <section id="contact">
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
    </section>"""

FOOTER = """  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash;
      <a href="tel:+14135550100">(413) 555-0100</a></p>
  </footer>"""

PAGES: dict[str, str] = {}

PAGES["audit-signals/render-incomplete.html"] = f"""<!--
  SCENARIO: render-incomplete
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: blockedCriticalAssetCount>0, brokenImages>1
  EXPECTED FINDINGS: [render_incomplete]
  EXPECTED GRADE: P2
  NOTES: Broken stylesheet plus two broken hero images satisfy render_incomplete promotion.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
  <link rel="stylesheet" href="nonexistent-render.css">
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
      <img src="images/missing-hero-a.jpg" alt="Work photo" width="600" height="200" style="width:100%;max-width:600px;display:block;margin-top:1rem">
      <img src="images/missing-hero-b.jpg" alt="Team photo" width="600" height="200" style="width:100%;max-width:600px;display:block;margin-top:0.5rem">
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["audit-signals/broken-image-single.html"] = f"""<!--
  SCENARIO: broken-image-single
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: brokenImages=1
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [broken_images]
  EXPECTED GRADE: (observation only — finding requires brokenImages>1)
  NOTES: Promotion boundary page for broken_images threshold.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer a full range of home services throughout Hampshire County.</p>
      <img src="images/single-missing.jpg" alt="Service photo" width="600" height="200" style="width:100%;max-width:600px;display:block;margin-top:1rem">
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["audit-signals/small-tap-targets-obs.html"] = f"""<!--
  SCENARIO: small-tap-targets-obs
  CATEGORY: audit-signals
  SIGNALS TRIGGERED: smallTapTargets=4
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [small_tap_targets]
  EXPECTED GRADE: (observation only — finding requires smallTapTargets>5)
  NOTES: Exactly four undersized nav links; below finding promotion threshold.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
  <style>
    .tiny-link {{ font-size: 0.65rem; padding: 0.1rem 0.2rem; display: inline-block; }}
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name tiny-link">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#" class="tiny-link">One</a></li>
        <li><a href="#" class="tiny-link">Two</a></li>
        <li><a href="#" class="tiny-link">Three</a></li>
        <li><a href="#contact" class="tiny-link">Contact</a></li>
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
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["journey/form-field-unusable.html"] = f"""<!--
  SCENARIO: form-field-unusable
  CATEGORY: journey
  SIGNALS TRIGGERED: primaryFormDisabledCriticalField=true
  EXPECTED FINDINGS: [form_field_unusable]
  EXPECTED GRADE: P2
  NOTES: Required phone field is disabled; journey probe classifies field_disabled.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" required disabled placeholder="(413) 555-xxxx">
        <label for="message">How can we help?</label>
        <textarea id="message" name="message" placeholder="Describe the work you need..."></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["journey/quote-path-missing.html"] = f"""<!--
  SCENARIO: quote-path-missing
  CATEGORY: journey
  SIGNALS TRIGGERED: hasQuoteIntent=true, hasContactForm=false
  EXPECTED FINDINGS: [quote_path_missing]
  EXPECTED GRADE: P2
  NOTES: Quote CTA href matches PRICING_RE but links to dead internal page; no contact form.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="/get-estimate" class="btn">Request a Free Estimate</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer plumbing, heating, and general home repairs throughout Hampshire County.</p>
      <ul>
        <li>Plumbing repairs and installation</li>
        <li>Water heater replacement</li>
        <li>Drain cleaning</li>
        <li>Emergency service available 24/7</li>
      </ul>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <p>No online form &mdash; call or use the estimate button above.</p>
    </section>
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["journey/no-email-finding.html"] = f"""<!--
  SCENARIO: no-email-finding
  CATEGORY: journey
  SIGNALS TRIGGERED: probeEmailContactPath=fail, no tel:, no form, no mailto
  EXPECTED FINDINGS: [no_email_path]
  EXPECTED OBSERVATIONS: [limited_contact_paths]
  EXPECTED GRADE: P2
  NOTES: Unlike no-email-path.html, no call path in contactPathTypes so finding promotes.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <p class="phone-cta" style="font-size:1.1rem;font-weight:bold">Call us: (413) 555-0100</p>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer a full range of home services throughout Hampshire County.</p>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p>To reach us, call <strong>(413) 555-0100</strong> during business hours. No email or form available.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; 123 Main Street, Northampton, MA &mdash; (413) 555-0100</p>
  </footer>
</body>
</html>
"""

PAGES["observations/hero-media-blocked.html"] = f"""<!--
  SCENARIO: hero-media-blocked
  CATEGORY: observations
  SIGNALS TRIGGERED: heroMediaBlocked=true
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [hero_media_blocked]
  EXPECTED GRADE: (observation only)
  NOTES: Above-fold hero image 404s during headless pass.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <img src="images/hero-blocked.jpg" alt="Hero" width="390" height="220" style="width:100%;display:block;margin:0.5rem 0">
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["observations/missing-message-field.html"] = f"""<!--
  SCENARIO: missing-message-field
  CATEGORY: observations
  SIGNALS TRIGGERED: hasContactForm=true, primaryFormHasMessageField=false
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [missing_message_field]
  EXPECTED GRADE: (observation only)
  NOTES: Form collects name and phone only; no textarea or message field.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <p class="phone-cta">Call us: <a href="tel:+14135550100">(413) 555-0100</a></p>
      <form class="contact-form" action="#" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required placeholder="Your name">
        <label for="phone">Phone</label>
        <input type="tel" id="phone" name="phone" required placeholder="(413) 555-xxxx">
        <button type="submit" class="btn">Send Message</button>
      </form>
    </section>
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["observations/weak-primary-cta.html"] = f"""<!--
  SCENARIO: weak-primary-cta
  CATEGORY: observations
  SIGNALS TRIGGERED: primaryCtaActionable=false, primaryCtaLabel present
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [weak_primary_cta]
  EXPECTED GRADE: (observation only)
  NOTES: Hero CTA is a button with no href and no click handler.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <button type="button" class="btn">Get Started Today</button>
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["observations/primary-cta-hidden.html"] = f"""<!--
  SCENARIO: primary-cta-hidden
  CATEGORY: observations
  SIGNALS TRIGGERED: primaryCtaVisible=false, contactCtaCount>0
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [primary_cta_hidden]
  EXPECTED GRADE: (observation only)
  NOTES: Hero tel CTA hidden on mobile via CSS; contact form still present below fold.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
  <style>
    @media (max-width: 480px) {{ .hero .btn {{ display: none !important; }} }}
  </style>
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["observations/contact-page-missing.html"] = f"""<!--
  SCENARIO: contact-page-missing
  CATEGORY: observations
  SIGNALS TRIGGERED: contact_page_discovery journey fail
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [contact_page_missing]
  EXPECTED GRADE: (observation only)
  NOTES: Nav Contact link points to /contact.html which 404s on this static site.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
  <header>
    <nav>
      <a href="#" class="site-name">Pioneer Home Services</a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#">Services</a></li>
        <li><a href="contact.html">Contact</a></li>
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
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""

PAGES["observations/booking-path-missing.html"] = f"""<!--
  SCENARIO: booking-path-missing
  CATEGORY: observations
  SIGNALS TRIGGERED: hasBookingIntent=true, no form, remoteContactPathCount=0
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [booking_path_missing]
  EXPECTED GRADE: (observation only — never promoted to finding)
  NOTES: Book Appointment CTA links to dead page; no phone, email, or form on page.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Schedule your appointment online today.</p>
      <a href="/book-appointment" class="btn">Book Appointment</a>
    </section>
    <section>
      <h2>Our Services</h2>
      <p>We offer plumbing and home repair throughout Hampshire County. Visit our booking page to schedule a consultation at a time that works for you.</p>
    </section>
    <section id="contact">
      <h2>Visit Us</h2>
      <p><strong>Address:</strong> 123 Main Street, Northampton, MA 01060</p>
      <p>Online booking is required for all new appointments.</p>
    </section>
  </main>
  <footer>
    <p>&copy; 2025 Pioneer Home Services &mdash; Northampton, MA</p>
  </footer>
</body>
</html>
"""

PAGES["observations/required-fields-excessive.html"] = f"""<!--
  SCENARIO: required-fields-excessive
  CATEGORY: observations
  SIGNALS TRIGGERED: multi_step_form_flow journey fail with required_fields_excessive
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [required_fields_excessive, form_friction]
  EXPECTED GRADE: (observation only)
  NOTES: Step 1 of multi-step form has six required fields before Continue.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
  <style>
    .form-step {{ display: none; }}
    .form-step.active {{ display: block; }}
  </style>
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
    <section id="contact">
      <h2>Request a Quote</h2>
      <form class="contact-form" id="quote-form" action="#" method="post">
        <div class="form-step active" id="step1">
          <p>Step 1 of 2</p>
          <label for="name">Name</label>
          <input type="text" id="name" name="name" required>
          <label for="company">Company</label>
          <input type="text" id="company" name="company" required>
          <label for="address">Address</label>
          <input type="text" id="address" name="address" required>
          <label for="phone">Phone</label>
          <input type="tel" id="phone" name="phone" required>
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required>
          <label for="zip">ZIP Code</label>
          <input type="text" id="zip" name="zip" required>
          <button type="button" class="btn" id="next-btn">Continue</button>
        </div>
        <div class="form-step" id="step2">
          <label for="message">Project details</label>
          <textarea id="message" name="message"></textarea>
          <button type="submit" class="btn">Submit</button>
        </div>
      </form>
    </section>
  </main>
  <script>
    document.getElementById('next-btn').onclick = function() {{
      document.getElementById('step1').classList.remove('active');
      document.getElementById('step2').classList.add('active');
    }};
  </script>
{FOOTER}
</body>
</html>
"""

PAGES["observations/runtime-error-cluster.html"] = f"""<!--
  SCENARIO: runtime-error-cluster
  CATEGORY: observations
  SIGNALS TRIGGERED: runtimeErrorClusterCount=2
  EXPECTED FINDINGS: []
  EXPECTED OBSERVATIONS: [runtime_error_cluster, script_errors]
  EXPECTED GRADE: (observation only — finding requires cluster>=3 + visible breakage)
  NOTES: Two console.error calls; below script_errors finding threshold of 3.
-->
<!DOCTYPE html>
<html lang="en">
<head>
{HEAD}
  <script>
    console.error("Widget init failed");
    console.error("Analytics config missing");
  </script>
</head>
<body>
{NAV}
  <main>
    <section class="hero">
      <h1>Pioneer Home Services</h1>
      <p>Serving Northampton and the Pioneer Valley since 2005.</p>
      <a href="tel:+14135550100" class="btn">Call (413) 555-0100</a>
    </section>
{CONTACT}
  </main>
{FOOTER}
</body>
</html>
"""


def main() -> None:
    for rel, html in PAGES.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8", newline="\n")
        print(f"wrote {rel}")


if __name__ == "__main__":
    main()
