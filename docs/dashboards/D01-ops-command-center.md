# D01 Ops Command Center

## Purpose and primary decision

Decide whether manufacturing is healthy this week: Pipeline converting to Funded and Correspondent purchase, cycle time and SLA in control, delivery not backing up, capacity matching arrivals.

## Audience and genre

COO / Ops VP. Genre: `static` stratified glance. One screen; drills for detail. Not an analyst workbench.

## Cadence and freshness

Daily. Event-dated KPIs through prior business day. Pipeline, SLA-breach, locks in force: As-of 6:00 a.m. ops calendar. Show both timestamps in the header.

## Headline KPIs

Exactly these eight ([catalog](../04-metric-catalog.md) headline set):

| Slot | Metric | Label on tile |
|------|--------|----------------|
| 1 | M-VOL-13 | Pipeline units |
| 2 | M-VOL-16 | Funded + purchased units |
| 3 | M-CYC-03 p50 and M-CYC-11 p50 | Start-to-fund p50 (R/W) · Submission-to-purchase p50 (Corr) |
| 4 | M-VOL-05 and M-VOL-05C | CTC · Purchase approved |
| 5 | M-AGE-03 | SLA-breach % of Pipeline |
| 6 | M-FAL-01 and M-FAL-03 | Pull-through start-to-fund · Submission-to-purchase |
| 7 | M-QLT-10 | Kickout rate |
| 8 | M-CAP-05 | Completions minus arrivals (processor + UW) |

Each tile: value, unit, WoW, versus ASSUMED SLA if applicable, time basis.

Header context (not a ninth tile): M-VOL-03 Locks in force. Pull-through tile may toggle M-FAL-02 lock-to-fund (Retail/Wholesale) without adding a tile.

## Layout

1. Header: As-of time, event-dated-through date, Channel filter.
2. Eight KPI tiles in two rows.
3. Comparison strip: three small trend charts — Funded + purchased (daily, last 6 weeks), Pipeline by Channel stacked, SLA-breach %.
4. Footer links: D02, D13, D10, D11.

No loan-level table on D01.

## Visuals

- KPI tiles with WoW delta.
- Sparkline under Funded + purchased and Pipeline (not a second dashboard).
- Do not combine M-CYC-03 and M-CYC-11 into one average.

## Filters

Channel, date range (default last complete week + MTD toggle, labeled), product program, fulfillment team.

## Drill path

| From | To |
|------|----|
| Pipeline, SLA-breach, pull-through | [D02](D02-pipeline-and-aging.md) |
| Start-to-fund p50 | [D07](D07-closing-and-funding.md) and [D06](D06-underwriting-and-conditions.md) |
| Submission-to-purchase p50 | [D08](D08-correspondent-operations.md) |
| Kickout rate | [D10](D10-investor-delivery.md) |
| Capacity vs arrival | [D13](D13-capacity-and-productivity.md) |
| CTC | [D06](D06-underwriting-and-conditions.md) |

## Grain and counting

Enterprise roll-up of Loan files. M-VOL-16 is the only combined manufacturing-complete count; never labeled Funded. One file once per event.

## Empty / stale / partial

If a Channel has no volume, show 0 and keep the tile (do not hide Correspondent when Retail-only week). If As-of snapshot failed, show event-dated tiles and mark snapshot tiles stale. Partial week labeled Partial.

## Out of scope

Lock desk P&L, lead/CPL, servicing, independent audit QC, loan-level worklist.

## Questions this view answers

1. Did Funded + purchased units rise or fall versus last week?
2. Is Pipeline growing while SLA-breach % rises (capacity problem) or while pull-through falls (fallout problem)?
3. Is Retail/Wholesale start-to-fund p50 off SLA while Correspondent purchase cycle is not (or the reverse)?
4. Are we clearing CTC / purchase-approved enough to support next week’s funds/purchases?
5. Is Kickout rate within tolerance?
6. Are processor + UW completions keeping up with arrivals?
7. Which Channel is carrying the Pipeline?
8. Is MTD on track versus the last complete week run-rate?
