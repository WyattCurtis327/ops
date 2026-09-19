# D08 Correspondent operations

## Purpose and primary decision

Run Correspondent manufacturing: Submissions, pre-purchase cycle, purchase, TPO conditions, TPO quality. Do not use Retail “Funded” language on this page.

## Audience and genre

Correspondent ops managers. Genre: `analytic`. Default Channel = Correspondent (fixed).

## Cadence and freshness

Event-dated Submissions and purchases through prior business day. Approved-not-purchased As-of 6:00 a.m.

## Headline KPIs

M-VOL-08 Submissions · M-VOL-09 Purchased units · M-VOL-10 Purchased volume · M-VOL-05C Purchase approved · M-CYC-11 p50/p90 · M-CYC-11A p50 · M-FAL-03 Submission-to-purchase · M-FAL-05 Fallout rate · M-QLT-09 Pre-purchase defect rate · M-QLT-13 TPO scorecard.

## Layout

1. KPI row (purchased units/volume labeled **Purchased**, never Funded).
2. Funnel: intake → Submission → purchase approved → purchased → rejected/fallout.
3. Cycle p50/p90 by TPO vs 2-day decision SLA.
4. TPO table: volume, pull-through, cycle p90, defect rate, Kickouts (M-QLT-10 filtered to Channel).
5. Conditions-to-TPO aging (Waiting-on TPO).
6. M-FST-02 7/14-day purchase forecast from purchase-approved not yet purchased (label **expected if they all convert**).

## Visuals

Funnel one-file-once. TPO table sortable. Do not color purchased $ independently of units.

## Filters

Channel locked to Correspondent. Date range, product, TPO, fulfillment team, investor (downstream).

## Drill path

Defects → [D11](D11-manufacturing-quality.md). After purchase → [D09](D09-post-closing-and-trailing-docs.md). Delivery → [D10](D10-investor-delivery.md). Pipeline → [D02](D02-pipeline-and-aging.md) with Channel preserved.

## Grain and counting

Submission-complete, not registration, for M-VOL-08. Purchase event is Correspondent purchase, not Funded, not Investor purchase. Registration-only files are Pipeline (intake milestone), not Submissions.

## Empty / stale / partial

If TPO names are not conformed, group “Unmapped TPO” and banner. Never drop those units.

## Out of scope

Retail/Wholesale Funded, TPO’s borrower closing, lock desk pricing, treating TPO as an AMC Vendor (D12).

## Questions this view answers

1. Submissions vs purchased units this week, and pull-through by Submission-month cohort?
2. Submission-to-decision and decision-to-purchase — which clock is slow?
3. Which TPOs are high-volume and high-defect?
4. Which TPOs are slow to clear conditions (Waiting-on TPO)?
5. What is approved but not yet purchased (wire lag)?
6. Fallout reason mix: rejected vs withdrawn vs expired lock?
7. 7/14-day purchase forecast?
8. Are Kickouts after delivery tracing back to the same TPOs as pre-purchase defects?
