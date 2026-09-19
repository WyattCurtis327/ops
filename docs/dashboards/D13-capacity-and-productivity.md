# D13 Capacity and productivity

## Purpose and primary decision

Match productive FTE to arrivals and WIP so queues do not age. Role-level: processor, underwriter, closer, post-closer, Correspondent analyst.

## Audience and genre

Ops leadership and workforce planners. Genre: `analytic`. Employee-day grain rolled to week.

## Cadence and freshness

Daily roster + LOS completions. As-of queue at 6:00 a.m. Default period: last complete week plus this week Partial.

## Headline KPIs

M-CAP-01 units/FTE by role · M-CAP-02 queue/FTE by role · M-CAP-05 completions minus arrivals by role · M-CAP-04 new vs WIP mix · M-AGE-03 (enterprise, for context) · M-CYC-15 queue time if Waiting-on timestamps exist · M-CAP-06 only if time-of-day exists.

## Layout

1. KPI row with a role toggle.
2. Arrivals vs completions by day (role-specific event: File start/submit, UW submit/decision, CTC/Funded, Submission/purchase, Funded/ship-ready).
3. Queue depth per FTE vs ASSUMED SLA band.
4. Team table: FTE, queue, units/FTE, SLA-breach files.
5. Channel mix of queue (Retail vs Wholesale vs Corr) to catch mis-aligned staffing.
6. M-CAP-03 utilization only if a capacity plan exists; otherwise omit.

## Visuals

Paired bars arrivals vs completions. Queue/FTE vs band. Do not rank employees on D01; this page may rank **teams**. Individual rank is optional and manager-only if HR agrees — default to team.

## Filters

Global plus role, team, manager. Channel still required (queue mix).

## Drill path

Processor role → [D03](D03-processing.md). UW → [D06](D06-underwriting-and-conditions.md). Closer → [D07](D07-closing-and-funding.md). Post-close → [D09](D09-post-closing-and-trailing-docs.md). Corr analyst → [D08](D08-correspondent-operations.md). Aging overflow → [D02](D02-pipeline-and-aging.md).

## Grain and counting

Productive FTE excludes PTO if the roster can; otherwise footnote “payroll FTE.” Completions credit completing assignee. Dual assignment: count queue on current assignee only.

## Empty / stale / partial

If roster is weekly only, do not fake daily FTE. If role is blank, “Unmapped role” bucket.

## Out of scope

Compensation, HR performance ratings, overtime dollars unless hours exist, Sales capacity.

## Questions this view answers

1. For each role, did completions keep up with arrivals this week?
2. Which teams are above queue-depth ASSUMED SLA?
3. Units per FTE trend vs WIP age (D02) — productivity down and aging up?
4. Is Correspondent queue growing while FTE still sits on Retail processing?
5. New vs WIP mix — are we only working old files?
6. Is this week Partial looking worse only because of one day?
7. After-hours completions (if captured) — hidden overtime?
8. What FTE would bring queue/FTE back into band (narrative; not an auto-optimizer)?
