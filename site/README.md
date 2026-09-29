# Kaya website — draft (not final)

Static HTML/CSS/JS. Open `index.html` in a browser, no build step needed.

| Page | File |
|---|---|
| Products (landing page; filter by room/material, sort; `#dining` deep links) | `index.html` |
| Single product (finish, quantity, dimensions; `#sora-dining-table`) | `product.html` |
| Our story | `about.html` |
| Contact (form, showroom details, FAQ) | `contact.html` |

A showcase for potential buyers. Forms validate and show a success screen but don't send anything.

- **Design tokens** (colour, Helvetica Neue type scale, 4–64px spacing, radii) are at the top of `assets/kaya.css`.
- **Products** are placeholder data in `assets/kaya.js` (`PRODUCTS`). Line drawings stand in for photography.
- **Placeholders** for facts we don't have yet are marked like `[this]` with a grey highlight.
- **Logo:** original draft (chair-K mark + wordmark) in `assets/logo/` as SVG; used in the header, footer and browser-tab icon.
