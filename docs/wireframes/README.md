# Operations dashboard wireframes

Open [index.html](index.html) in a browser. The kit is organized by **Operations department / subcategory (P01–P15)**, not by dashboard ID. Home is the department directory. Map: [by-department.md](by-department.md). Numbers are **sample only**.

## Recommendation

| Choice | Why |
|--------|-----|
| HTML/CSS wireframes, not generated pictures | KPI names, metric IDs, and layout must be exact. Image models scramble labels. |
| Two genres only | D01 is `static` (one screen, eight tiles). D02–D14 are `analytic` (filters, compare, drill). |
| Stratified layout | Headline KPIs → comparison → detail. Same skeleton on every desk so Ops does not relearn chrome. |
| No gauges, donuts, or traffic-light tiles | IBCS: columns, bars, lines, heatmaps, tables. Semantic color only when up is good or bad. |
| Channel in the chrome, always | Correspondent purchase is never an unlabeled “Funded.” |
| LOS keeps the worklist | D02 may export stuck files. No queue app in BI. |

## Visual system

- **Header:** dashboard ID, decision title, As-of vs event-dated timestamps, SAMPLE banner.
- **Filters:** Channel, period, product, team on every page. Extra filters only where the spec says.
- **KPI tile:** label, value, unit, WoW, vs SLA (if any), time basis, metric ID. Dual clocks (R/W vs Corr) stay two numbers.
- **Actual:** solid fill. **Prior week:** lighter. **ASSUMED SLA:** dashed line. **Forecast:** hatched (not a lighter solid).
- **Drill:** tiles and chart titles are links. Filters persist (simulated in this kit).
- **Stale / partial / unavailable:** banners. Missing event ≠ zero.

## What to review in the kit

Walk **HOME** then the lifecycle: P01 → P02 → P03/P04/P05 → P06 → P07 → P08 → P10 → P11. Correspondent spine is **P09** only.

1. **EXE (D01)** — eight tiles, no loan table, two cycle clocks not averaged.
2. **P15 Pipeline** — heatmap + waiting-on + forecast labeled “expected if they all convert.”
3. **P08 vs P09** — Funded vs Purchased language.
4. **P06 vs P07** — same shipped D06, two department first screens (UW vs conditions).
5. **P05 Insurance/MI** — department wireframe with no D15; tiles land on other desks.
6. **P11 Delivery** — Delivered ≠ Investor purchased.
7. **P01 Disclosure** — calendar-day LE clock and 3-day line.

## Not in this kit

Pixel-perfect theming, real LOS data, Databricks AI/BI widgets, mobile-native apps. Desktop ~1280px is the design target; tiles stack on a narrow viewport for review only.
