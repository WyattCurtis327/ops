# D12 Vendor performance

## Purpose and primary decision

Score third-party orders: on-time, cycle, revisions, concentration. TPO and Broker are not Vendors.

## Audience and genre

Ops vendor management and desk leads. Genre: `analytic`. Order grain.

## Cadence and freshness

Event-dated completed orders. Open orders As-of 6:00 a.m.

## Headline KPIs

M-VEN-01 placed / completed / open · M-VEN-03 on-time % · M-VEN-02 p50/p90 (by type) · M-VEN-04 revision rate · M-VEN-06 concentration (top vendor share) · M-VEN-05 cost per order **only if Finance feed exists** (otherwise omit the tile).

## Layout

1. KPI row by Vendor type selector (default AMC).
2. Rank table: Vendor name, volume, on-time %, p50, p90, revision %, concentration.
3. State × Vendor p90 heatmap for AMC and title.
4. Open orders past SLA.
5. Trend of on-time % by top Vendors.

## Visuals

Rank table first (analytic). Heatmap second. Do not use pie charts for concentration; use a bar of share.

## Filters

Global plus Vendor type, Vendor name, order type, state, appraisal path.

## Drill path

AMC detail clocks → [D04](D04-appraisal-and-valuation.md). Title → [D05](D05-title-escrow-closing-coord.md). Defects tagged to Vendor → [D11](D11-manufacturing-quality.md).

## Grain and counting

One order once. Reassignment = new order if the portal stamps a new order ID; footnote it. Staff appraisers can appear as a labeled comparison row, not as a Vendor scorecard equal to AMCs unless leadership says so.

## Empty / stale / partial

Unmapped Vendor names → “Unmapped” bucket, banner. M-VEN-05 hidden until Finance joins AP to orders — do not show $0.

## Out of scope

TPO scorecards (D08/D11), Broker scorecards as Vendors, contract legal, lead providers.

## Questions this view answers

1. Which AMCs miss on-time % at meaningful volume?
2. Title company p90 by state?
3. Is revision/ROV concentrated in a few Vendors?
4. Is order share too concentrated (top Vendor %)?
5. How many open orders are past SLA, by type?
6. Did on-time % move WoW for the top five Vendors?
7. Credit/flood on-time (if those orders are in the feed)?
8. Cost per order only when Finance data exists — otherwise, is the gap still blocking a scorecard?
