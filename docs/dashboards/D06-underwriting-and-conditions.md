# D06 Underwriting and conditions

## Purpose and primary decision

Decision files on time, with controlled Suspense, condition load, CTC, and rework. Correspondent eligibility decisions also appear when Channel includes Correspondent; purchase economics stay on D08.

## Audience and genre

UW and conditions managers. Genre: `analytic`.

## Cadence and freshness

Event-dated decisions and CTC daily. Queue As-of 6:00 a.m.

## Headline KPIs

M-VOL-04 · M-CYC-06 p50/p90 · M-QLT-02 Suspense rate · M-QLT-01 conditions per file (PTD/PTF) · M-CYC-07 p50 · M-CYC-07F (file-level condition clock) · M-VOL-05 CTC · M-QLT-14 CTC revoke · M-QLT-03 Rework · M-CAP-02 (UW) · M-AGE-06 · M-CYC-16A (MI cert) as a supporting tile.

## Layout

1. KPI row (two rows if needed; CTC revoke and rework on row 2).
2. UW turn p50/p90 vs SLA by team.
3. First-decision mix: approve / Suspense / deny (R/W) and eligible / conditions / reject (Corr).
4. Conditions per file trend, PTD vs PTF.
5. Condition turn distribution.
6. CTC vs revoke.
7. Queue depth per UW FTE.

## Visuals

Decision mix 100% stacked. Turn vs SLA band. Conditions per file as a line, not a vanity “lower always” without product mix — slice by product.

## Filters

Global plus underwriter/team, AUS recommendation, PTD vs PTF, TPO (when Channel = Correspondent).

## Drill path

Capacity → [D13](D13-capacity-and-productivity.md). CTC → [D07](D07-closing-and-funding.md). Correspondent → [D08](D08-correspondent-operations.md). Defects on conditions → [D11](D11-manufacturing-quality.md). Aging of conditions queue → [D02](D02-pipeline-and-aging.md).

## Grain and counting

First-decision event must be preserved (later decisions do not overwrite). M-CYC-07 is condition grain; M-CYC-07F is file grain — show both, labeled. Correspondent must not increment M-VOL-05.

## Empty / stale / partial

If condition issue timestamps are missing, hide M-CYC-07 and banner. Do not compute turn from file age.

## Out of scope

Exception policy authorship, lock exceptions, independent audit QC.

## Questions this view answers

1. UW first-decision p50/p90 versus SLA by team and Channel?
2. Is Suspense rate rising, and for which product or TPO?
3. Conditions per file PTD vs PTF versus last month?
4. Condition turn p50 — are we or the borrower/Broker/TPO the delay (Waiting-on)?
5. CTC volume versus revoke rate?
6. Rework rate after CTC or after Suspense?
7. Queue depth per UW FTE versus arrivals (M-CAP-05)?
8. How many files are lock-expiring before CTC?
