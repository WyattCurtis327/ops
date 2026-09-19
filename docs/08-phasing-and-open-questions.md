# Phasing and open questions

## Overview

Fourteen dashboards should not go live on one day. This is the recommended manufacturing-reporting rollout and the questions Operations leadership must answer before SLAs and local names are treated as policy.

## MVP (phase 1) — Command and pipeline

**Ship:** D01, D02, plus Channel / product / team filters.

**Why first:** Leadership can run a huddle. Desk dashboards without an enterprise spine create competing truths.

**Required events:** [MVP event set](06-event-dictionary.md#minimum-viable-event-set-mvp).

**Required metrics:** M-VOL-01, M-VOL-05, M-VOL-05C, M-VOL-06, M-VOL-08, M-VOL-09, M-VOL-11, M-VOL-12, M-VOL-13, M-VOL-14, M-VOL-16, M-CYC-03, M-CYC-11, M-AGE-01–07, M-FAL-01, M-FAL-03, M-FAL-05, M-QLT-10, M-CAP-05 (even if FTE is coarse), M-FST-01.

**Exit:** COO uses D01 in the weekly Ops meeting; desk leads use D02 stuck export.

## Phase 2 — Money clocks (funding and purchase)

**Ship:** D07 (Retail/Wholesale), D08 (Correspondent), D06 (UW/conditions — CTC is the gate).

**Why:** Start-to-fund and submission-to-purchase on D01 need a place to drill. Mixing them in one “closing” dashboard is the failure mode this phase prevents.

**Exit:** Funded units on D07 match secondary/finance funded counts within a documented tolerance; D08 purchased units match warehouse/purchase advice.

## Phase 3 — Third parties and TRID

**Ship:** D03, D04, D05, D12, D14.

**Why:** Waiting-on Vendor and 3-day LE are the usual unexplained D01 cycle-time misses.

**Depends:** AMC/title order timestamps; TRID application date.

## Phase 4 — After fund

**Ship:** D09, D10, D11.

**Why:** Post-close WIP and kickouts are enterprise (already on D01) but the cure is desk-level.

**Depends:** Trailer checklist by product/investor; kickout reason codes.

## Phase 5 — Capacity

**Ship:** D13 (and M-CAP-* quality).

**Depends:** Productive FTE roster. Without it, keep only M-CAP-05 on D01 (arrivals vs completions, no FTE).

## Out of this product until a new subject-area pack

Sales leads/CPL, lock-desk economics, servicing, independent audit QC, construction-draw desk, HELOC-only dashboards.

---

## Open questions for Operations leadership

Until answered, the pack uses the stated default.

| ID | Question | Default in this pack | Blocks |
|----|----------|----------------------|--------|
| Q1 | What are company SLA targets by milestone (replace `ASSUMED SLA`)? | Industry-typical table in the catalog | D01 SLA-breach color as policy |
| Q2 | What is the official ops calendar / timezone / holiday list? | LOS business timezone | All cycle times |
| Q3 | File start definition per Channel (which LOS milestone is E-START)? | Setup complete / registration complete / intake complete | M-VOL-01, pull-through |
| Q4 | Is TRID clock from application date or intent to proceed? | TRID application date | M-CYC-04, D14 |
| Q5 | Are Wholesale appraisals/title primarily Broker-ordered or lender-ordered? | Both paths supported | D04/D05 received-in clocks |
| Q6 | Does Correspondent pre-purchase review sit on the processing team or a dedicated Corr team? | Dedicated (D08); D03 only if assigned to processors | D03 vs D08 queues |
| Q7 | 100% pre-purchase QC or sample? | Assume high-touch / near-100% for Corr | M-QLT-09 coverage |
| Q8 | Who owns investor commitment assignment — Ops delivery or Capital Markets? | CM assigns; Ops executes delivery | D10 filters |
| Q9 | Productive FTE source (roster vs HRIS) and PTO treatment? | Roster if it exists; else hide D13 | D13 |
| Q10 | May huddle export include borrower name, or loan number only? | Loan number, no SSN, name optional | NFR-5 |
| Q11 | Local names for fulfillment center / pod / team? | Generic “team” | All filters |
| Q12 | Are HELOC, construction, reverse in-scope volume? | Product dimension only | Extra processes |
| Q13 | Independent QC: dual-report with a qualifier, or never on D11? | Never on D11 | D11 |
| Q14 | Finance join for Vendor cost (M-VEN-05)? | Omit until join exists | D12 cost tile |
| Q15 | Forecast method: CTC + scheduled + purchase-approved as-is, or a pull-through haircut? | No haircut; label **expected if they all convert** | M-FST-* |
| Q16 | Does Correspondent split delegated vs non-delegated? | Dimension on P09 only if both exist | P09 filters |

## Suggested working session

One 90-minute workshop: Q1, Q3, Q4, Q6, Q9. Those five change grains and dashboard defaults. The rest can be email.

---

## Definition of done (reporting product)

A phase is done when:

1. Every headline KPI on the shipped dashboards resolves to a catalog ID and an event ID.
2. Channel filter is present and Correspondent cannot increment Funded.
3. p50 and p90 ship for every cycle KPI.
4. Unavailable ≠ zero for missing events.
5. A desk lead can walk File start → Funded or Submission → purchased on D02 without a side spreadsheet.
