# D02 Pipeline and aging

## Purpose and primary decision

See where WIP sits, how old it is, who it is waiting on, which files are stuck, and what should Fund or Correspondent-purchase in 7/14/30 days. Default drill from D01 volume/aging.

## Audience and genre

Ops managers and desk leads. Genre: `analytic`.

## Cadence and freshness

As-of 6:00 a.m. ops calendar (primary). Forecast uses CTC, schedule, and purchase-approved as of that snapshot. Fallout/pull-through panels are event-dated cohorts (labeled).

## Headline KPIs

M-VOL-13 Pipeline units · M-VOL-14 Post-close WIP · M-VOL-03 Locks in force · M-AGE-03 SLA-breach % · M-AGE-04 Stuck files · M-AGE-05 Waiting-on mix (internal % as the headline slice) · M-AGE-06 Lock expiring before CTC · M-FST-03 expected funded + purchased next 7 (M-FST-01/02 in the 7/14/30 chart; label **expected if they all convert**).

## Layout

1. KPI row.
2. Milestone funnel / bar: M-AGE-01 by Current milestone, stacked by Channel.
3. Age heatmap: milestone × age band (0–2, 3–5, 6–10, 11+).
4. Waiting-on party stacked bar by milestone.
5. Forecast bar: 7/14/30 expected Funded (R/W) and Correspondent purchase, separate series.
6. Optional export: stuck-file list (loan number, Channel, milestone, age, waiting-on, assignee). Action remains in the LOS.

## Visuals

Heatmap for age (semantic: older is worse). Do not color Pipeline units red because the number is large. Forecast vs actual last 7 days as a small comparison (forecast quality is not a v1 catalog metric; show actuals only if cheap).

## Filters

Global plus Current milestone, Waiting-on party, Lock status, Broker/TPO, investor.

## Drill path

Milestone = processing → [D03](D03-processing.md). UW/conditions → [D06](D06-underwriting-and-conditions.md). CTC/closing → [D07](D07-closing-and-funding.md). Correspondent intake/purchase → [D08](D08-correspondent-operations.md). Post-close → [D09](D09-post-closing-and-trailing-docs.md). Export is the loan-level drill.

## Grain and counting

One open Loan file once. Pipeline ends at Funded (R/W) or Correspondent purchase (Corr). Post-close WIP is excluded from M-VOL-13 and shown as M-VOL-14.

## Empty / stale / partial

If snapshot is stale, banner the page. Empty milestone columns stay visible.

## Out of scope

Sales funnel, lock pricing, servicing, building a replacement LOS worklist UI.

## Questions this view answers

1. Which milestone holds the most units, and is that Channel-specific?
2. What share of each milestone is 11+ business days old?
3. Is age driven by borrower/Broker/TPO, Vendor, or internal?
4. How many files are stuck per the N-day rule?
5. How many locks will expire before likely CTC?
6. How many CTCs have no closing date?
7. What is expected to Fund vs Correspondent-purchase in 7/14/30 days?
8. Did Fallout in the current start-month cohort jump (detail panel M-FAL-04/05)?
