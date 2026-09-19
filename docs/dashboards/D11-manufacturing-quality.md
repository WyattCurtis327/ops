# D11 Manufacturing quality

## Purpose and primary decision

See defect rates from manufacturing QC (pre-fund, pre-purchase, post-close) and Kickouts. This is not independent audit QC.

## Audience and genre

Ops QC and Ops risk. Genre: `analytic`.

## Cadence and freshness

Event-dated reviews and Kickouts daily.

## Headline KPIs

M-QLT-07 Pre-fund defect rate (critical as the headline severity, major/minor on the tile menu) · M-QLT-08 Post-close · M-QLT-09 Pre-purchase · M-QLT-10 Kickout rate · M-QLT-03 Rework · M-QLT-13 TPO scorecard · files reviewed vs eligible (sample coverage).

## Layout

1. KPI row with a persistent subtitle: **Manufacturing quality — not audit QC**.
2. Defect rate by severity and Channel.
3. Defect theme mix (taxonomy categories).
4. Kickout reason mix vs internal themes (side-by-side, not a forced join).
5. TPO rolling 90-day defects + Kickouts.
6. Team / UW table for pre-fund fails.
7. Sample coverage: reviewed / eligible.

## Visuals

Severity stacked. Do not average critical with minor into one “defect %” headline. File-fail is headline; finding count is detail.

## Filters

Global plus QC type (pre-fund / pre-purchase / post-close), severity, TPO, UW team, investor (Kickout).

## Drill path

Kickout operational aging → [D10](D10-investor-delivery.md). TPO → [D08](D08-correspondent-operations.md). Rework → [D06](D06-underwriting-and-conditions.md). Vendor-caused appraisal/title defects → [D12](D12-vendor-performance.md).

## Grain and counting

Review grain for rates. Eligible population must be named (random sample vs 100% pre-purchase). Overturned defects excluded from confirmed file-fail if the QC system captures overturns.

## Empty / stale / partial

If audit QC is in the same table, it must be filtered out; if it cannot be, do not ship the KPI — banner the gap. Never mix.

## Out of scope

Independent Quality audit program, compliance testing, vendor contracting.

## Questions this view answers

1. Pre-fund file-fail rate this month vs last, by severity?
2. Do Correspondent pre-purchase fails align with later Kickouts?
3. Which defect themes are rising?
4. Which UW teams or TPOs outlier on confirmed criticals?
5. Rework rate alongside defect rate — are we catching issues late?
6. What share of eligible files were actually reviewed (coverage)?
7. Kickout rate vs internal post-close fail rate (same themes)?
8. Is any Channel’s critical rate above the others?
