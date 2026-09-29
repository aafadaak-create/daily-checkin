# Kaya check-in — design proposals (not final)

Three directions for the daily check-in page. Each one keeps every feature of `wife_checkin_2.html` and uses the same saved data, so you can open any of them on the same day.

| File | Direction | Feel |
|---|---|---|
| `a-atelier.html` | **A · Atelier** | Editorial, furniture-showroom: serif headlines, hairline rules, square checks, sharp corners |
| `b-soft-living.html` | **B · Soft Living** | Calm and warm: rounded cards, green header card, progress ring, pill buttons |
| `c-bold-daily.html` | **C · Bold Daily** | High energy: dark header, big uppercase type, habit tiles (2 columns on wider screens) |

**Colours are placeholders.** Each file's `:root` block is marked `PLACEHOLDER palette`; swap in Kaya's logo colours there. The `KAYA` wordmark in the header is a logo slot, so replace it with the real logo image.

Changes from the original, in all three:
- SVG line icons instead of emoji
- Checklist items and food sections are real buttons, so they work with the keyboard and screen readers
- Saving now shows a message if the browser blocks storage
- Today's date uses local time instead of UTC, so late-evening check-ins land on the right day
