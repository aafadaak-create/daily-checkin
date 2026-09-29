# Kaya website — draft (not final)

Static HTML/CSS/JS. Open `index.html` in a browser, no build step needed.

| Page | File |
|---|---|
| Homepage | `index.html` |
| Product catalog (filter by room/material, sort; `#dining` deep links) | `catalog.html` |
| Single product (finish, quantity, dimensions; `#sora-dining-table`) | `product.html` |
| Wholesale quote request (multi-product lines, file upload) | `wholesale.html` |
| About / Our story | `about.html` |
| Contact (form, showroom details, FAQ) | `contact.html` |

- **Design tokens** (colour, Helvetica Neue type scale, 4–64px spacing, radii) are at the top of `assets/kaya.css`.
- **Products** are placeholder data in `assets/kaya.js` (`PRODUCTS`). Line drawings stand in for photography.
- **Placeholders** for facts we don't have yet are marked like `[this]` with a grey highlight.
- **Forms** validate and show success states but are not connected to email/WhatsApp yet.
- **Logo:** original draft concepts in `assets/logo/` (SVG) and on `logos.html`. Concept A is used in the header, footer and browser-tab icon.
