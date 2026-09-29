"""Build the Kaya Chairs prototype pages from shared partials.  Run: python3 kaya-chairs/_build.py"""
from pathlib import Path

OUT = Path(__file__).parent

# ---- Brand marks: the original Kaya chair-K ----
# Mark: a K drawn as a chair in side view (back, arm, seat, front leg).
MARK = '<path d="M12 6V34M12 21 28 6M12 21H28V34"/>'
# Wordmark: thin capitals; the K repeats the chair seat, the A's have no crossbar.
WORD = ('<path d="M1 1V17M1 10.5 10.5 1M1 10.5H10.5V17"/><path d="M21 17 27 1 33 17"/>'
        '<path d="M43 1 49 9 55 1M49 9V17"/><path d="M65 17 71 1 77 17"/>')

CHAIRS = {
  "c-rib": "M34 14Q60 8 86 14L84 70H36ZM44 12V70M52 11V70M60 10.5V70M68 11V70M76 12V70M30 70H90L94 82H26ZM30 82L25 132M90 82L95 132M42 82L44 124M78 82L76 124",
  "c-arm": "M36 18Q60 10 84 18V64H36ZM46 15V64M54 14V64M62 14V64M70 14V64M78 16V64M22 46H38M82 46H98M24 46V70M96 46V70M22 64H98L100 78H20ZM24 78L20 132M96 78L100 132M40 78L42 122M80 78L78 122",
  "c-bistro": "M34 62V30Q60 4 86 30V62M35 32H85M34 40H86M34 48H86M34 56H86M28 62H92L90 74H30ZM32 74L26 132M88 74L94 132M44 74L46 124M76 74L74 124",
  "c-stool": "M42 34V18Q60 12 78 18V34M34 34H86L82 44H38ZM40 44L32 134M80 44L88 134M50 44L52 128M70 44L68 128M36 100H84",
  "c-lounge": "M24 70Q24 34 60 32Q96 34 96 70M14 56H28V94H14ZM92 56H106V94H92ZM28 72H92V94H28ZM20 94L16 124M100 94L104 124M40 94V118M80 94V118",
}

ICONS = {
  "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
  "menu": '<path d="M3 7h18M3 12h18M3 17h18"/>',
  "close": '<path d="M6 6l12 12M18 6 6 18"/>',
  "plus": '<path d="M12 5v14M5 12h14"/>',
  "check": '<path d="M20 6 9 17l-5-5"/>',
  "pause": '<path d="M9 5v14M15 5v14"/>',
  "play": '<path d="M7 5l12 7-12 7z"/>',
  "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
  "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
  "mail": '<path d="M3 5h18v14H3z"/><path d="m3 6 9 7 9-7"/>',
  "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  "home": '<path d="M3 11l9-7 9 7v9H3z"/><path d="M9 20v-6h6v6"/>',
  "utensils": '<path d="M5 3v8a3 3 0 0 0 6 0V3M8 3v18M19 15V3c-2.5 1-4 3.5-4 7v5h4zm0 0v6"/>',
  "bed": '<path d="M3 18V7M3 13h18v5M21 18v-3a3 3 0 0 0-3-3h-7v1"/><circle cx="7" cy="10" r="2"/>',
  "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
  "building": '<path d="M4 21V5l8-2v18M12 7h8v14M8 8h.01M8 12h.01M8 16h.01M16 11h.01M16 15h.01M2 21h20"/>',
  "container": '<path d="M2 7h20v11H2z"/><path d="M6 7v11M10 7v11M14 7v11M18 7v11"/>',
  "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6z"/><path d="m9 12 2 2 4-4"/>',
  "factory": '<path d="M2 21V10l6 4V10l6 4V6l8 4v11z"/><path d="M6 17h2M11 17h2M16 17h2"/>',
  "handshake": '<path d="M2 12l4-4 4 2 4-3 4 3 4 2M6 8v6l5 5 2-2M13 17l2 2 3-3M10 14l2 2"/>',
  "layers": '<path d="M12 3 2 8l10 5 10-5z"/><path d="M2 13l10 5 10-5"/>',
  "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6"/>',
  "sparkle": '<path d="M12 3c.5 4 2 6.5 6 7-4 .5-5.5 3-6 7-.5-4-2-6.5-6-7 4-.5 5.5-3 6-7z"/>',
  "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/>',
  "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
  "insta": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6"/>',
  "linkedin": '<path d="M4 9h4v11H4zM6 4.5a1 1 0 1 0 0 .1M10 9h4v2c1-1.5 2.2-2 3.5-2 2 0 2.5 1.5 2.5 3.5V20h-4v-6c0-1-.5-1.5-1.3-1.5S14 13 14 14v6h-4z"/>',
  "whatsapp": '<path d="M4 20l1.4-4A8 8 0 1 1 8 18.6z"/><path d="M9 9c0 3 2.5 6 6 6l1-1.5-2-1-1 .8c-1-.4-2-1.4-2.3-2.3l.8-1-1-2z"/>',
}

SPRITE = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
  + "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
  + "".join(f'<symbol id="{k}" viewBox="0 0 120 140"><path d="{v}"/></symbol>' for k, v in CHAIRS.items())
  + f'<symbol id="kaya-mark" viewBox="0 0 40 40"><g class="mark-stroke" stroke-width="2.6">{MARK}</g></symbol>'
  + f'<symbol id="kaya-word" viewBox="0 0 78 18"><g class="mark-stroke" stroke-width="1.4">{WORD}</g></symbol>'
  + '</svg>')

FAVICON = ("data:image/svg+xml," + (
  "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'><rect width='40' height='40' rx='10' fill='%23F08A1C'/>"
  "<g fill='none' stroke='%231E1E1E' stroke-width='3' stroke-linecap='square'>" + MARK.replace('"', "'") + "</g></svg>").replace(" ", "%20"))


def i(name):
    return f'<svg class="i" aria-hidden="true"><use href="#i-{name}"/></svg>'


def chair(cid, cls="art"):
    return f'<svg class="{cls}" viewBox="0 0 120 140" aria-hidden="true"><use href="#{cid}"/></svg>'


LOGO = ('<a href="index.html" class="logo" aria-label="Kaya Chairs, home">'
        '<svg class="mono" viewBox="0 0 40 40" aria-hidden="true"><use href="#kaya-mark"/></svg>'
        '<span class="logo-rule"></span>'
        '<svg class="word" viewBox="0 0 78 18" aria-hidden="true"><use href="#kaya-word"/></svg></a>')

NAV = [("index.html", "Home"), ("collection.html", "Collection"), ("about.html", "About"), ("contact.html", "Contact")]


def header(active):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
{SPRITE}
<header class="header">
  <div class="container header-inner">
    {LOGO}
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="header-end">
      <a href="contact.html" class="icon-link" aria-label="Your quote list">{i('clipboard')}<span class="quote-count" hidden></span></a>
      <a href="contact.html" class="btn btn-orange">Get a Quote</a>
      <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="mobileMenu" aria-label="Open menu">{i('menu')}</button>
    </div>
  </div>
  <nav class="mobile-menu" id="mobileMenu" aria-label="Mobile" hidden>{links}<a href="contact.html">Get a Quote <span class="quote-count" hidden></span></a></nav>
</header>"""


FOOTER = f"""<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {LOGO}
        <p>Turkish-crafted commercial chairs, supplied wholesale from the San Francisco Bay Area, CA.</p>
        <div class="socials"><a href="#" aria-label="Instagram (link coming)">{i('insta')}</a><a href="#" aria-label="LinkedIn (link coming)">{i('linkedin')}</a><a href="#" aria-label="WhatsApp (link coming)">{i('whatsapp')}</a></div>
      </div>
      <div><span class="label">Collection</span><ul><li><a href="collection.html#dining">Dining</a></li><li><a href="collection.html#bar">Bar &amp; counter</a></li><li><a href="collection.html#lounge">Lounge</a></li><li><a href="collection.html#outdoor">Outdoor</a></li></ul></div>
      <div><span class="label">Wholesale</span><ul><li><a href="collection.html#wholesale">How it works</a></li><li><a href="collection.html#shipping">LCL &amp; FCL shipping</a></li><li><a href="contact.html">Get a quote</a></li></ul></div>
      <div><span class="label">Company</span><ul><li><a href="about.html">About</a></li><li><a href="about.html#lookbook">Lookbook</a></li><li><a href="contact.html#faq">FAQ</a></li></ul></div>
    </div>
    <div class="footer-bottom">© <span class="js-year"></span> Kaya Chairs · San Francisco Bay Area, CA · Prototype with placeholder content</div>
  </div>
</footer>
<script src="assets/kc.js"></script>"""


def page(filename, title, desc, body, active=None):
    (OUT / filename).write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/kc.css">
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
""")
    print("wrote", filename)


def cta_band(title="Furnishing a venue? Get wholesale pricing.", lead="Tell us the models and quantities you need. We reply with pricing, colours and shipping options."):
    return f"""<section class="cta-band pattern">
  <div class="container">
    <span class="eyebrow">Wholesale quote</span>
    <h2 class="h2">{title}</h2>
    <p class="lead">{lead}</p>
    <a href="contact.html" class="btn btn-orange">Request a Quote {i('arrow')}</a>
  </div>
</section>"""


# ================================================================ HOME
home = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Contract · Hospitality <svg class="spark" aria-hidden="true"><use href="#i-sparkle"/></svg></span>
      <h1 class="h-display">Premium <span class="accent">Seating</span>,<br>Wholesale Direct<span class="accent">.</span></h1>
      <p class="lead">Turkish-crafted commercial chairs for restaurants, hotels and events across the San Francisco Bay Area.</p>
      <div class="hero-ctas">
        <a href="collection.html" class="btn btn-orange">Discover Collection</a>
        <a href="collection.html#wholesale" class="play"><span class="play-ring"><svg class="i" aria-hidden="true"><use href="#i-play"/></svg></span>How wholesale works</a>
      </div>
      <div class="proof">
        <ul aria-hidden="true"><li>{i('utensils')}</li><li>{i('bed')}</li><li>{i('spark')}</li><li>{i('building')}</li></ul>
        <p class="small muted">For restaurants, hotels, events and offices</p>
      </div>
    </div>
    <div class="hero-visual">
      <div class="glow"></div>
      <svg class="orbit" viewBox="0 0 500 500" aria-hidden="true">
        <ellipse cx="250" cy="260" rx="235" ry="120" transform="rotate(-24 250 260)" fill="none" stroke="#1E1E1E" stroke-opacity=".35" stroke-width="1.2"/>
        <path d="M58 318l6 -10 6 10 -6 10z" fill="#F08A1C"/><path d="M438 176l6-10 6 10-6 10z" fill="#F08A1C"/>
        <path d="M96 118c3 10 7 14 17 17-10 3-14 7-17 17-3-10-7-14-17-17 10-3 14-7 17-17z" fill="#1F6D6E"/>
        <circle cx="120" cy="352" r="11" fill="#FFFFFF" stroke="#1E1E1E" stroke-opacity=".25"/>
      </svg>
      <div class="hero-chair">{chair('c-arm')}</div>
      <div class="float-card">
        <div class="row-sb"><strong>Rib Armchair</strong><span class="price">From <span class="ph">[$—]</span></span></div>
        <span class="small muted">Stackable · indoor / outdoor</span>
        <hr>
        <div class="row-sb"><span class="small">Colours</span><span class="swatches" aria-label="Anthracite, Sand, Terracotta"><i class="swatch" style="--tint-c:#3B4150"></i><i class="swatch" style="--tint-c:#D9C7A7"></i><i class="swatch" style="--tint-c:#B86B4B"></i></span></div>
      </div>
    </div>
  </div>
</section>

<section class="container cats" aria-label="Shop by type">
  <a class="cat pink" href="collection.html#dining">
    <div><h2 class="h3">Dining Chairs</h2><p class="small muted">Stackable, indoor and outdoor</p><span class="link">Shop now {i('arrow')}</span></div>
    {chair('c-rib')}
  </a>
  <a class="cat blue" href="collection.html#lounge">
    <div><h2 class="h3">Lounge &amp; Bar</h2><p class="small muted">Lobby lounges and bar stools</p><span class="link">Shop now {i('arrow')}</span></div>
    {chair('c-lounge')}
  </a>
</section>

<section class="section">
  <div class="container">
    <div class="section-title"><h2 class="h2">Trending Chairs</h2><p class="muted">Our most requested models for Bay Area restaurants, hotels and event companies.</p></div>
    <ul class="grid four" id="featured"></ul>
    <p class="small muted center" style="margin-top:var(--s5)" id="quoteStatus" role="status" aria-live="polite"></p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <div class="ghost-wrap"><h2 class="ghost-title" data-ghost="Products">Products</h2></div>
      <div class="tabs" role="group" aria-label="Filter products">
        <button type="button" class="tab" data-f="all" aria-pressed="true">All</button>
        <button type="button" class="tab" data-f="dining" aria-pressed="false">Dining</button>
        <button type="button" class="tab" data-f="bar" aria-pressed="false">Bar</button>
        <button type="button" class="tab" data-f="lounge" aria-pressed="false">Lounge</button>
        <button type="button" class="tab" data-f="outdoor" aria-pressed="false">Outdoor</button>
      </div>
    </div>
    <div class="prod-block">
      <div class="prod-feature blue" id="prodFeature"></div>
      <ul class="mini-grid" id="miniGrid"></ul>
    </div>
  </div>
</section>

<section class="banner mint">
  <div class="container banner-inner">
    <div>
      <span class="small muted">Shipped from Türkiye to the Bay Area</span>
      <h2 class="h2" style="text-transform:uppercase;margin-top:var(--s2)">Wholesale orders now open</h2>
      <ul class="banner-points"><li>Plenty of styles</li><li>Reliable &amp; strong</li><li>LCL &amp; FCL shipping</li><li>Made in Türkiye</li></ul>
      <a href="contact.html" class="btn btn-dark">Request a Quote</a>
    </div>
    {chair('c-bistro')}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-title"><h2 class="h2">Guides</h2><p class="muted">Straight answers for buying commercial chairs wholesale.</p></div>
    <ul class="guides">
      <li><a class="guide" href="collection.html#shipping">
        <div class="guide-img pink">{chair('c-rib')}</div>
        <div class="guide-meta"><span>{i('user')} Kaya team</span><span>{i('calendar')} <span class="ph">[Date]</span></span></div>
        <h3 class="h3">LCL or FCL: which shipping fits your order?</h3></a></li>
      <li><a class="guide" href="collection.html#dining">
        <div class="guide-img blue">{chair('c-arm')}</div>
        <div class="guide-meta"><span>{i('user')} Kaya team</span><span>{i('calendar')} <span class="ph">[Date]</span></span></div>
        <h3 class="h3">Choosing stackable chairs for events and restaurants</h3></a></li>
      <li><a class="guide" href="contact.html#faq">
        <div class="guide-img mint">{chair('c-bistro')}</div>
        <div class="guide-meta"><span>{i('user')} Kaya team</span><span>{i('calendar')} <span class="ph">[Date]</span></span></div>
        <h3 class="h3">Caring for outdoor chairs in Bay Area weather</h3></a></li>
    </ul>
  </div>
</section>
"""
page("index.html", "Kaya Chairs — Premium seating, wholesale direct", "Turkish-crafted commercial chairs, supplied wholesale from the San Francisco Bay Area.", home)

# ================================================================ COLLECTION & WHOLESALE
collection = f"""
<section class="page-head blue">
  <div class="container">
    <span class="eyebrow">Collection &amp; Wholesale</span>
    <h1 class="h1">Chairs for every venue</h1>
    <p class="lead">Every model comes in several colours and ships wholesale from Türkiye. Add chairs to your quote as you browse.</p>
  </div>
</section>

<section class="section paper" style="padding-top:var(--s7)">
  <div class="container">
    <div class="section-head" style="margin-bottom:var(--s6)">
      <div class="filters" role="group" aria-label="Filter by type">
        <button type="button" class="chip" data-f="all" aria-pressed="true">All</button>
        <button type="button" class="chip" data-f="dining" aria-pressed="false">Dining</button>
        <button type="button" class="chip" data-f="bar" aria-pressed="false">Bar &amp; counter</button>
        <button type="button" class="chip" data-f="lounge" aria-pressed="false">Lounge</button>
        <button type="button" class="chip" data-f="outdoor" aria-pressed="false">Outdoor</button>
      </div>
      <p class="small muted" id="resultCount" role="status" aria-live="polite"></p>
    </div>
    <ul class="grid" id="collectionGrid"></ul>
    <p class="small muted" style="margin-top:var(--s5)" id="quoteStatus" role="status" aria-live="polite"></p>
    <p class="small muted" style="margin-top:var(--s2)">Model names, materials and colours are placeholders until the real range is added.</p>
  </div>
</section>

<section class="section white" id="wholesale">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Wholesale</span><h2 class="h2">Wholesale, made simple</h2></div><a href="contact.html" class="btn btn-orange">Request a Quote</a></div>
    <ol class="steps paper" style="background:none">
      <li class="step"><h3 class="h3">Choose models &amp; colours</h3><p class="muted">Mix models across your order. Samples available on request.</p></li>
      <li class="step"><h3 class="h3">Get your quote</h3><p class="muted">Pricing by quantity, with LCL or FCL shipping options.</p></li>
      <li class="step"><h3 class="h3">Made in Türkiye</h3><p class="muted">Produced and quality-checked before loading.</p></li>
      <li class="step"><h3 class="h3">Delivered</h3><p class="muted">Shipped to the US and delivered to your venue or warehouse.</p></li>
    </ol>
    <ul class="stats" style="margin-top:var(--s7)">
      <li class="stat"><b><span class="ph">[n]</span></b><span class="small muted">Minimum order (chairs)</span></li>
      <li class="stat"><b><span class="ph">[n]</span> wks</b><span class="small muted">Typical lead time</span></li>
      <li class="stat"><b><span class="ph">[n]</span>+</b><span class="small muted">Colours across the range</span></li>
      <li class="stat"><b><span class="ph">[n]</span> yr</b><span class="small muted">Commercial warranty</span></li>
    </ul>
  </div>
</section>

<section class="section paper" id="shipping">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Shipping</span><h2 class="h2">LCL or FCL: pick what fits your order</h2></div></div>
    <div class="ship">
      <article class="ship-card">
        <span class="code">LCL</span>
        <h3 class="h3">Less than Container Load</h3>
        <p class="muted">Your chairs share a container with other shipments. Best for first orders, single venues and smaller quantities.</p>
        <dl>
          <div><dt>Typical order</dt><dd><span class="ph">[n–n]</span> chairs</dd></div>
          <div><dt>Transit to the Bay Area</dt><dd><span class="ph">[~n]</span> weeks</dd></div>
          <div><dt>Best for</dt><dd>Restaurants, cafés</dd></div>
        </dl>
      </article>
      <article class="ship-card featured">
        <span class="code">FCL</span>
        <h3 class="h3">Full Container Load</h3>
        <p class="navy-text-muted">A 20ft or 40ft container just for your order. The lowest cost per chair for hotels, multi-site groups and large events.</p>
        <dl>
          <div><dt>Capacity</dt><dd><span class="ph">[~n]</span> stacked chairs</dd></div>
          <div><dt>Transit to the Bay Area</dt><dd><span class="ph">[~n]</span> weeks</dd></div>
          <div><dt>Best for</dt><dd>Hotels, events, groups</dd></div>
        </dl>
      </article>
    </div>
  </div>
</section>

{cta_band("Know your models? Get a quote in one step.", "Send your list and quantities. We'll recommend LCL or FCL and reply with full pricing.")}
"""
page("collection.html", "Collection & Wholesale — Kaya Chairs", "Browse Kaya's commercial chairs and learn how wholesale ordering and LCL/FCL shipping work.", collection, "collection.html")

# ================================================================ ABOUT & LOOKBOOK
route = f"""<svg class="route" viewBox="0 0 640 220" role="img" aria-label="Route from Türkiye to the San Francisco Bay Area by sea freight">
  <path d="M60 150 C 200 30, 440 30, 580 150" fill="none" stroke="#F08A1C" stroke-width="1.5" stroke-dasharray="6 6"/>
  <circle cx="60" cy="150" r="7" fill="#F08A1C"/><circle cx="580" cy="150" r="7" fill="#F08A1C"/>
  <g transform="translate(296 44)" fill="none" stroke="#FFFFFF" stroke-width="1.5"><rect x="0" y="0" width="48" height="24"/><path d="M10 0v24M19 0v24M29 0v24M38 0v24"/></g>
  <text x="60" y="185" text-anchor="middle" fill="#FFFFFF">Türkiye</text>
  <text x="60" y="205" text-anchor="middle" fill="#D2E4E4" style="font-size:12px">[Port / city]</text>
  <text x="580" y="185" text-anchor="middle" fill="#FFFFFF">SF Bay Area</text>
  <text x="580" y="205" text-anchor="middle" fill="#D2E4E4" style="font-size:12px">[Warehouse]</text>
  <text x="320" y="96" text-anchor="middle" fill="#D2E4E4" style="font-size:12px">Sea freight · LCL or FCL · [~n weeks]</text>
</svg>"""

about = f"""
<section class="page-head blue">
  <div class="container">
    <span class="eyebrow">About &amp; Lookbook</span>
    <h1 class="h1">From Türkiye to the Bay Area</h1>
    <p class="lead">Kaya brings commercial chairs from Turkish manufacturers straight to venues in California and across the US.</p>
  </div>
</section>

<section class="section paper">
  <div class="container two">
    <div class="stack">
      <span class="eyebrow">Our story</span>
      <h2 class="h2">Why we started Kaya</h2>
      <p class="muted"><span class="ph">[Founding story: who started Kaya, when, and why Turkish-made chairs.]</span></p>
      <p class="muted"><span class="ph">[The manufacturing partner(s): where they are, how long they have made contract seating, certifications.]</span></p>
      <p class="muted">Based in the San Francisco Bay Area, we handle quotes, shipping and delivery locally, so you deal with one team from first sample to final chair.</p>
    </div>
    <div class="navy" style="padding:var(--s6);border-radius:var(--r)">{route}</div>
  </div>
</section>

<section class="section white">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">What we stand for</span><h2 class="h2">Three promises</h2></div></div>
    <ul class="features three">
      <li class="feature"><span class="icon-box">{i('shield')}</span><h3 class="h3">Made to last</h3><p class="muted">Commercial-grade frames and materials, built for daily use in busy venues.</p></li>
      <li class="feature"><span class="icon-box">{i('factory')}</span><h3 class="h3">Direct from the maker</h3><p class="muted">We work straight with Turkish manufacturers, so you pay wholesale, not showroom prices.</p></li>
      <li class="feature"><span class="icon-box">{i('handshake')}</span><h3 class="h3">Local support</h3><p class="muted">A Bay Area team for samples, quotes, delivery and after-sales help.</p></li>
    </ul>
  </div>
</section>

<section class="section" id="lookbook">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">Lookbook</span><h2 class="h2">Kaya chairs in the wild</h2></div><p class="small muted">Placeholder scenes until project photos arrive.</p></div>
    <div class="look">
      <figure class="wide pink">{chair('c-rib')}<figcaption>Restaurant · <span class="ph">[Venue, Oakland]</span></figcaption></figure>
      <figure class="tall blue">{chair('c-lounge')}<figcaption>Hotel lobby · <span class="ph">[Venue, San Jose]</span></figcaption></figure>
      <figure class="mint">{chair('c-stool')}<figcaption>Bar · <span class="ph">[Venue, SF]</span></figcaption></figure>
      <figure class="paper">{chair('c-bistro')}<figcaption>Patio · <span class="ph">[Venue]</span></figcaption></figure>
      <figure class="wide blue">{chair('c-arm')}<figcaption>Event · <span class="ph">[Event, Napa]</span></figcaption></figure>
      <figure class="pink">{chair('c-rib')}<figcaption>Café · <span class="ph">[Venue, Berkeley]</span></figcaption></figure>
    </div>
  </div>
</section>

{cta_band("Want these chairs in your venue?", "Request samples or a full quote. We'll help you choose models and colours.")}
"""
page("about.html", "About & Lookbook — Kaya Chairs", "Kaya brings Turkish-made commercial chairs to the San Francisco Bay Area.", about, "about.html")

# ================================================================ QUOTE & CONTACT
contact = f"""
<section class="page-head blue">
  <div class="container">
    <span class="eyebrow">Quote &amp; Contact</span>
    <h1 class="h1">Request a wholesale quote</h1>
    <p class="lead">Tell us what you need. We reply within <span class="ph">[1 business day]</span> with pricing, colours and shipping options.</p>
  </div>
</section>

<section class="section paper" id="quote">
  <div class="container two" style="align-items:start">
    <div class="white" style="padding:clamp(24px,4vw,40px);border-radius:var(--r);box-shadow:var(--shadow)">
      <form class="form" id="quoteForm" novalidate>
        <div class="error-summary" tabindex="-1" role="alert"></div>
        <fieldset>
          <legend>Your chairs</legend>
          <div class="qlist" id="qlist"></div>
        </fieldset>
        <fieldset>
          <legend>Company</legend>
          <div class="row">
            <div class="field" data-msg="Enter your company or venue name."><label for="f-company">Company / venue <span class="req">*</span></label><input id="f-company" autocomplete="organization" required><span class="err"></span></div>
            <div class="field" data-msg="Choose your business type."><label for="f-type">Business type <span class="req">*</span></label><select id="f-type" required><option value="">Select</option><option>Restaurant / café</option><option>Hotel</option><option>Event company</option><option>Office / campus</option><option>Interior designer</option><option>Retailer / dealer</option><option>Other</option></select><span class="err"></span></div>
          </div>
        </fieldset>
        <fieldset>
          <legend>Contact</legend>
          <div class="field" data-msg="Enter your name."><label for="f-name">Full name <span class="req">*</span></label><input id="f-name" autocomplete="name" required><span class="err"></span></div>
          <div class="row">
            <div class="field" data-msg="Enter your email so we can send the quote."><label for="f-email">Email <span class="req">*</span></label><input id="f-email" type="email" autocomplete="email" required><span class="err"></span></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" type="tel" autocomplete="tel"></div>
          </div>
        </fieldset>
        <fieldset>
          <legend>Delivery</legend>
          <div class="field"><span style="font-size:14px;font-weight:600">Shipping</span>
            <div class="radio-cards" role="radiogroup" aria-label="Shipping">
              <label><input type="radio" name="ship" value="LCL">LCL<span>Smaller orders</span></label>
              <label><input type="radio" name="ship" value="FCL">FCL<span>Full container</span></label>
              <label><input type="radio" name="ship" value="Not sure" checked>Not sure<span>Recommend one</span></label>
            </div>
          </div>
          <div class="row">
            <div class="field" data-msg="Enter the delivery city."><label for="f-city">Delivery city <span class="req">*</span></label><input id="f-city" autocomplete="address-level2" placeholder="e.g. Oakland, CA" required><span class="err"></span></div>
            <div class="field"><label for="f-when">Needed by</label><select id="f-when"><option>Flexible</option><option>Within 1 month</option><option>1–3 months</option><option>3–6 months</option></select></div>
          </div>
          <div class="field"><label for="f-msg">Anything else?</label><textarea id="f-msg" placeholder="Quantities, colours, samples, venue opening date…"></textarea></div>
        </fieldset>
        <button type="submit" class="btn btn-orange btn-block">Request a Quote</button>
        <p class="small muted">Prototype: this form doesn't send yet.</p>
      </form>
      <div class="success" id="quoteSuccess" tabindex="-1">
        <span class="icon-box">{i('check')}</span>
        <h2 class="h2">Quote request received</h2>
        <p class="muted">Thanks. We'll reply within <span class="ph">[1 business day]</span>. (Prototype: nothing was sent.)</p>
        <a href="collection.html" class="link">Back to the collection {i('arrow')}</a>
      </div>
    </div>

    <aside class="aside-sticky">
      <div class="contact-card navy">
        <span class="eyebrow">Contact</span>
        <dl>
          <div>{i('pin')}<span><dt>Location</dt><dd>San Francisco Bay Area, CA</dd><dd class="small navy-text-muted"><span class="ph">[Warehouse / showroom address]</span></dd></span></div>
          <div>{i('phone')}<span><dt>Phone / WhatsApp</dt><dd><span class="ph">[+1 (___) ___-____]</span></dd></span></div>
          <div>{i('mail')}<span><dt>Email</dt><dd><span class="ph">[hello@kayachairs.com]</span></dd></span></div>
          <div>{i('clock')}<span><dt>Hours</dt><dd><span class="ph">[Mon–Fri, 9am–5pm PT]</span></dd></span></div>
        </dl>
        <p class="small navy-text-muted">Showroom visits by appointment.</p>
      </div>
    </aside>
  </div>
</section>

<section class="section white" id="faq">
  <div class="container two" style="align-items:start">
    <div><span class="eyebrow">FAQ</span><h2 class="h2" style="margin-top:var(--s3)">Common questions</h2></div>
    <div class="faq">
      <details><summary>What's the minimum order? {i('plus')}</summary><p class="ans"><span class="ph">[MOQ answer, e.g. n chairs per model or n per order.]</span></p></details>
      <details><summary>What's the difference between LCL and FCL? {i('plus')}</summary><p class="ans">LCL (Less than Container Load) shares a container with other shipments, which suits smaller orders. FCL (Full Container Load) is a 20ft or 40ft container for your order alone, which gives the lowest cost per chair on large projects.</p></details>
      <details><summary>How long does delivery take? {i('plus')}</summary><p class="ans"><span class="ph">[Production time + sea freight + delivery, e.g. n–n weeks in total.]</span></p></details>
      <details><summary>Can I get samples first? {i('plus')}</summary><p class="ans"><span class="ph">[Sample policy: cost, lead time, showroom viewing.]</span></p></details>
      <details><summary>Do you offer custom colours? {i('plus')}</summary><p class="ans"><span class="ph">[Custom colour policy and minimums.]</span></p></details>
      <details><summary>Do you deliver outside the Bay Area? {i('plus')}</summary><p class="ans"><span class="ph">[Delivery coverage: California, US-wide, freight partners.]</span></p></details>
    </div>
  </div>
</section>
"""
page("contact.html", "Quote & Contact — Kaya Chairs", "Request a wholesale quote from Kaya Chairs in the San Francisco Bay Area.", contact, "contact.html")
