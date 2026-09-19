# D03 Processing

## Purpose and primary decision

Run the processing desk: file-complete turn, queue per FTE, and Waiting-on party. Correspondent package completeness appears here only when the company assigns those files to processors; otherwise it lives on D08.

## Audience and genre

Processing managers and team leads. Genre: `analytic`.

## Cadence and freshness

Daily event-dated completions; As-of queue at 6:00 a.m.

## Headline KPIs

M-CYC-05 p50/p90 · M-AGE-01 (processing milestone) · M-AGE-03 (processing SLA-breach) · M-AGE-05 · M-CAP-01 (processor) · M-CAP-02 (processor) · M-CYC-16 (HOI) as a supporting tile · M-CYC-15 queue time if Waiting-on timestamps exist.

## Layout

1. KPI row.
2. Turn-time trend (p50/p90) vs ASSUMED SLA (5 business days).
3. Queue by team / processor: depth and age.
4. Waiting-on party mix.
5. Completions vs arrivals (processing submits vs File starts) — M-CAP-05 for processor role.
6. Table: teams off SLA.

## Visuals

Dual p50/p90 line vs SLA band. Stacked waiting-on. Do not rank individual processors on D01; ranking tables belong here and on D13.

## Filters

Global plus processor, Waiting-on party, income type, Broker (Wholesale).

## Drill path

Appraisal-blocked → [D04](D04-appraisal-and-valuation.md). Title-blocked → [D05](D05-title-escrow-closing-coord.md). Setup/eSign-blocked → [D14](D14-disclosures-and-setup.md). Capacity → [D13](D13-capacity-and-productivity.md). Correspondent-heavy filter → [D08](D08-correspondent-operations.md).

## Grain and counting

Loan file. Completions credited to completing assignee. Wholesale waiting-on Broker must not be coded as borrower.

## Empty / stale / partial

Unassigned queue shown as its own team bucket. If Waiting-on party is >20% blank, banner data quality and still show age.

## Out of scope

UW decision quality, lock desk, vendor scorecards (link to D12).

## Questions this view answers

1. What is start-to-UW-submit p50/p90 versus SLA, by Channel and team?
2. How many processing files are SLA-breach, and who are they waiting on?
3. Which teams exceed queue depth per FTE?
4. Are arrivals outrunning submits?
5. Is self-employed income type driving the tail (p90)?
6. How many files are blocked on HOI?
7. Which Brokers concentrate waiting-on Broker age?
8. Is rework from UW Suspense returning files to this queue (link M-QLT-02/03)?
