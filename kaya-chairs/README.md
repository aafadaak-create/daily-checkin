# Kaya Chairs — prototype

Static site for Kaya Chairs (SF Bay Area wholesaler of Turkish-made commercial chairs).
Vela colours (navy `#0E1726`, gold `#C9A56B`) with Hulics-style outline branding.

| Page | File | Combines |
|---|---|---|
| Home | `index.html` | Hero, scrolling strip, brand tiles, featured chairs, who we supply, wholesale steps |
| Collection & Wholesale | `collection.html` | Chair range with colours and "Add to quote", wholesale steps, LCL vs FCL shipping |
| About & Lookbook | `about.html` | Story, Türkiye → Bay Area route, values, lookbook |
| Quote & Contact | `contact.html` | Quote form (pre-filled from chairs you added), contact details, FAQ |

- Edit pages in `_build.py`, then run `python3 kaya-chairs/_build.py`.
- Chair data lives in `assets/kc.js` (`CHAIRS`); names, colours and drawings are placeholders.
- `[Bracketed]` highlighted text marks details still to fill in.
- Forms validate but don't send anything (prototype).
