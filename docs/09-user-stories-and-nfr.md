# User stories and reporting requirements

## Overview

Stories are for the reporting product, not for changing the LOS. Acceptance is in metric IDs and dashboard specs. Non-functional requirements apply to every dashboard.

## Epic A — Enterprise glance

1. As the COO, I want Pipeline, Funded + purchased, cycle p50, CTC/purchase-approved, SLA-breach %, pull-through, kickout rate, and capacity vs arrival on one screen (D01), so that I can tell whether manufacturing is healthy before the huddle.
2. As the COO, I want Retail/Wholesale start-to-fund p50 and Correspondent submission-to-purchase p50 shown as two labeled numbers, so that I do not compare unlike clocks.
3. As the COO, I want WoW on every D01 tile, so that I see movement without opening a desk dashboard.
4. As the COO, I want to click a D01 tile and land on D02 or the owning desk with Channel preserved, so that I can explain the movement.

## Epic B — Pipeline control

5. As an Ops manager, I want WIP by milestone, age band, and Waiting-on party (D02), so that I know whether delay is borrower, Broker/TPO, Vendor, or internal.
6. As an Ops manager, I want stuck files per the N-day rule and a loan-level export, so that the huddle works the same list the LOS will action.
7. As an Ops manager, I want 7/14/30-day Funded and Correspondent-purchase forecasts from CTC, scheduled, and purchase-approved (M-FST-*), so that I can staff the week.
8. As an Ops manager, I want lock-expiring-before-CTC as a risk set, so that Capital Markets lock issues show up as Operations risk without building a lock-desk dashboard.

## Epic C — Desk operations

9. As a processing manager, I want start-to-UW-submit p50/p90 and queue per FTE (D03), so that I can balance chase vs new files.
10. As the appraisal desk, I want order-to-report p50/p90 by AMC and state, waiver rate, and ROV rate (D04), so that valuation is not the silent CTC delay.
11. As the title desk, I want commitment cycle, open curative age, and CTC-not-scheduled (D05), so that title and calendar failures are distinct.
12. As a UW manager, I want first-decision turn, Suspense rate, conditions per file, CTC, and CTC revoke (D06), so that I can see speed vs quality.
13. As a closing manager, I want CTC-to-fund, docs-out-to-signed, signed-to-funded, and funding fail rate on Retail/Wholesale only (D07), so that Correspondent purchase is not in my funded count.
14. As Correspondent ops, I want submissions, purchase-approved, purchased units, pull-through by TPO, and pre-purchase defects (D08), so that I run a purchase factory, not a retail clone.
15. As a post-close manager, I want trailing WIP by document type and missing-trailer rate at day 10 and 15 (D09), so that ship-ready is predictable.
16. As delivery, I want Delivered vs Investor purchased, suspense aging, and kickout reason mix (D10), so that “sold” is never an unlabeled mashup.

## Epic D — Quality, vendors, capacity, TRID

17. As Ops QC, I want pre-fund, pre-purchase, and post-close file-fail rates by severity, separate from audit QC (D11), so that manufacturing defects are visible.
18. As vendor management, I want on-time %, p90, revision rate, and concentration by Vendor type (D12), so that I can manage the panel. TPO is not a Vendor on this page.
19. As a workforce planner, I want completions minus arrivals and queue per FTE by role (D13), so that I add FTE where the queue is aging.
20. As the disclosure desk, I want LE turn in TRID general business days and the share of files past 3 creditor-open days (D14), so that TRID send timing is not mixed with ops-calendar cycle time or with the CD waiting period.

## Epic E — Trust and self-serve

21. As a BI analyst, I want a metric ID, grain, formula, direction, and event ID for every KPI, so that I do not invent a second definition.
22. As a desk manager, I want a stale/partial banner when the As-of snapshot failed or the week is incomplete, so that I do not manage to a partial number.
23. As any user, I want Channel on every view, so that I never mix Correspondent purchase into Funded.

## Non-functional requirements

| ID | Requirement |
|----|-------------|
| NFR-1 | Refresh: event-dated through prior business day; As-of snapshot 6:00 a.m. ops calendar. Freshness printed on every dashboard header. |
| NFR-2 | If a required event is missing, the KPI renders **unavailable**, not zero. |
| NFR-3 | Cycle time always p50 and p90; average optional. |
| NFR-4 | Row access: team managers default to their fulfillment team; Ops VP sees all. Loan-level export is team-scoped. |
| NFR-5 | Loan-level export may include loan number, Channel, milestone, age, waiting-on, assignee, TPO/Broker. No SSN, no full borrower name required for huddle export. |
| NFR-6 | Semantic color only for direction-known metrics (up good / up bad). Context metrics (Pipeline, orders) are not red because they are large. |
| NFR-7 | Filters persist on drill. D07 and D14 default Channel exclude Correspondent; D08 locks Correspondent. |
| NFR-8 | Time zone labeled (ops calendar). Initial LE tiles labeled TRID general business days; CD wait labeled specific business days. |
| NFR-9 | `ASSUMED SLA` lines are visually distinct from regulatory 3-calendar-day LE until leadership replaces them. |
| NFR-10 | Do not build a LOS worklist replacement. Export + LOS is the action path. |
