# Metric catalog

## Overview

Governed Operations measures. Formulas are business language, not SQL. IDs are stable; names are the words that appear on dashboards.

**Direction:** up good / up bad / context (read with another metric).

**Time basis:** Event-dated (flow) vs As-of (snapshot). Never mix in one unlabeled KPI.

**Cycle time:** Always publish p50 and p90 in business days. Average is optional and never the only number.

**Cohorts:** Pull-through defaults to cohort by File start month (M-FAL-01), lock month (M-FAL-02), or Submission month (M-FAL-03). Rolling 30/90 is allowed only when the dashboard names the window.

**Combined manufacturing-complete units (D01 only):** Funded units (Retail/Wholesale) + Correspondent purchased units. The label must say **Funded + purchased units**. Do not call it Funded.

Source-system mapping is a follow-on job.

## ASSUMED SLA (not company policy)

Regulatory exception: initial LE is 3 **calendar** days.

| Milestone / clock | ASSUMED SLA | Stuck if no milestone change |
|-------------------|-------------|------------------------------|
| Setup / intake | 1 business day | 2 business days |
| Initial LE send | 3 TRID general business days (creditor-open) | n/a |
| Processing to UW submit | 5 business days | 3 business days |
| UW first decision | 1 business day p50 / 2 p90 | 2 business days |
| Condition turn | 2 business days | 3 business days |
| Appraisal order to report | 7 business days | n/a (order grain) |
| Title order to commitment | 5 business days | n/a |
| CTC to Funded | 5 business days | 2 business days |
| Submission to purchase decision | 2 business days | 2 business days |
| Post-close to ship-ready | 15 business days | 5 business days |
| Ship-ready to Delivered | 2 business days | n/a |
| Delivered to Investor purchase | 5 business days | 3 business days |

---

## Volume and flow

| ID | Name | Subcategory | What it measures | Business formula | Grain | Unit | Direction | Time basis | Required dimensions | Owner | Dashboards |
|----|------|-------------|------------------|------------------|-------|------|-----------|------------|---------------------|-------|------------|
| M-VOL-01 | Files started | P01 | New Loan files that completed setup/registration/intake | Count of File start events | Loan file | files | context | Event | Channel, product, team | Setup / Corr ops | D01, D02, D14, D08 |
| M-VOL-02 | Applications taken | P01 | Retail/Wholesale applications | Count of application events. **Exclude Correspondent.** | Loan file | files | context | Event | Channel (R/W only), product | Disclosure desk | D14 |
| M-VOL-03 | Locks in force | P15 | Files currently locked | Count of open files with Lock status = locked | Loan file | files | context | As-of | Channel, product | Ops (dimension from CM) | D01, D02 |
| M-VOL-04 | Underwritten (decisioned) | P06 | First UW decisions | Count of first UW decision events (approve, suspend, deny / Corr reject) | Loan file | files | context | Event | Channel, team, product | UW manager | D06, D13 |
| M-VOL-05 | Clear to close | P07 | CTC stamps | Count of CTC events. Correspondent uses purchase-approved (M-VOL-05C), not this ID. | Loan file | files | up good | Event | Channel (R/W), team | UW / conditions | D01, D06, D07 |
| M-VOL-05C | Purchase approved | P09 | Correspondent approved-to-purchase | Count of purchase-decision approved events | Loan file | files | up good | Event | TPO, product | Correspondent ops | D08 |
| M-VOL-06 | Funded units | P08 | Lender-funded originations | Count of Funded events. **Exclude Correspondent.** | Loan file | units | up good | Event | Channel (R/W), product, team | Closing/funding | D01, D07 |
| M-VOL-07 | Funded volume | P08 | Dollar funded | Sum of funded loan amounts. **Exclude Correspondent.** | Loan file | $ | up good | Event | Channel (R/W), product | Closing/funding | D01, D07 |
| M-VOL-08 | Correspondent submissions | P09 | TPO packages submitted for purchase | Count of Submission-complete events | Loan file | files | context | Event | TPO, product | Correspondent ops | D08, D01 |
| M-VOL-09 | Correspondent purchased units | P09 | Closed loans bought from TPOs | Count of Correspondent purchase events | Loan file | units | up good | Event | TPO, product | Correspondent ops | D01, D08 |
| M-VOL-10 | Correspondent purchased volume | P09 | Dollar purchased | Sum of purchase amounts | Loan file | $ | up good | Event | TPO, product | Correspondent ops | D01, D08 |
| M-VOL-11 | Delivered units | P11 | Loans submitted to an investor | Count of Delivered events | Loan file | units | up good | Event | Channel, investor | Delivery | D01, D10 |
| M-VOL-12 | Investor purchased units | P11 | Loans paid for by the investor | Count of Investor purchase (purchase advice) events | Loan file | units | up good | Event | Channel, investor | Delivery | D01, D10 |
| M-VOL-13 | Pipeline units | P15 | Open files not yet Funded (R/W) or Correspondent-purchased | Count of open Loan files at As-of, Channel-specific end event | Loan file | files | context | As-of | Channel, milestone, team | Ops leadership | D01, D02 |
| M-VOL-14 | Post-close WIP | P10 | Funded or purchased, not yet Delivered | Count of files after Funded/Corr purchase and before Delivered | Loan file | files | context | As-of | Channel, investor | Post-close | D01, D09, D10 |
| M-VOL-15 | Appraisal waiver rate | P03 | Files that used a valuation waiver | Waived files / files that reached a valuation decision | Loan file | % | context | Event | Channel, product | Appraisal desk | D04 |
| M-VOL-16 | Funded + purchased units | P08+P09 | Manufacturing-complete units for D01 | M-VOL-06 + M-VOL-09 | Loan file | units | up good | Event | Channel | Ops VP | D01 only |

---

## Cycle time

All IDs below are the clock. Display as **Name p50** and **Name p90**. Exclude files that have not reached the stop event. Do not treat in-flight age as Cycle time (that is M-AGE-02).

| ID | Name | Subcategory | Clock start → stop | Grain | Unit | Direction | Time basis | Required dimensions | Owner | Dashboards |
|----|------|-------------|--------------------|-------|------|-----------|------------|---------------------|-------|------------|
| M-CYC-01 | Start to CTC | P07 | File start → first CTC | Loan file | business days | up bad | Event (CTC date) | Channel, product, team | Ops leadership | D01, D06 |
| M-CYC-02 | CTC to fund | P08 | First CTC → Funded | Loan file | business days | up bad | Event (Funded date) | Channel (R/W) | Closing | D07, D01 |
| M-CYC-03 | Start to fund | P08 | File start → Funded | Loan file | business days | up bad | Event (Funded date) | Channel (R/W), product | Ops leadership | D01, D07 |
| M-CYC-04 | Disclosure turn | P01 | TRID application date (six pieces) → initial LE sent | Loan file | **TRID general business days** | up bad | Event (LE sent) | Channel (R/W) | Disclosure desk | D14 |
| M-CYC-05 | Processing file-complete | P02 | File start → submitted to UW | Loan file | business days | up bad | Event (submit date) | Channel, team | Processing | D03 |
| M-CYC-06 | UW turn (initial) | P06 | Submitted to UW → first decision | Loan file | business days | up bad | Event (decision date) | Channel, UW team | UW manager | D06, D13 |
| M-CYC-07 | Condition turn | P07 | Condition issued → that condition cleared | Condition | business days | up bad | Event (clear date) | Channel, PTD vs PTF, team | Conditions | D06 |
| M-CYC-07F | Condition turn (file) | P07 | First condition issued → last PTD cleared | Loan file | business days | up bad | Event | Channel, team | Conditions | D06 |
| M-CYC-08 | Appraisal cycle | P03 | Order placed → report in. **Exclude waivers and Correspondent reviews without a new order.** | Order | business days | up bad | Event (report in) | Vendor, state, Channel | Appraisal desk | D04, D12 |
| M-CYC-08A | Appraisal review cycle | P03 | Report in (or package in if no company order) → review complete | Order / file | business days | up bad | Event | Channel, Vendor | Appraisal desk | D04 |
| M-CYC-09 | Title cycle | P04 | Order placed → commitment in | Order | business days | up bad | Event | Vendor, state, Channel | Title desk | D05, D12 |
| M-CYC-09A | Title curative cycle | P04 | Commitment in → curative clear | Order / file | business days | up bad | Event | Vendor, state | Title desk | D05 |
| M-CYC-10 | Closing cycle | P08 | CTC → Funded (same as M-CYC-02; keep M-CYC-10 as the named “closing cycle” on D07) | Loan file | business days | up bad | Event | Channel (R/W) | Closing | D07 |
| M-CYC-11 | Correspondent purchase cycle | P09 | Submission complete → Correspondent purchase | Loan file | business days | up bad | Event (purchase date) | TPO, product | Correspondent ops | D01, D08 |
| M-CYC-11A | Submission to purchase decision | P09 | Submission complete → purchase decision | Loan file | business days | up bad | Event | TPO | Correspondent ops | D08 |
| M-CYC-12 | Trailing-doc cycle | P10 | Funded or Correspondent purchase → ship-ready | Loan file | business days | up bad | Event (ship-ready) | Channel, TPO | Post-close | D09 |
| M-CYC-13 | Delivery cycle | P11 | Funded or Correspondent purchase → Delivered | Loan file | business days | up bad | Event (Delivered) | Channel, investor | Delivery | D10 |
| M-CYC-14 | Investor purchase cycle | P11 | Delivered → Investor purchase | Loan file | business days | up bad | Event (investor purchase) | Investor, Channel | Delivery | D10 |
| M-CYC-15 | Queue time | P02/P06 | Time in milestone with Waiting-on party = internal, until the desk completes. Touch time is the complement when captured. | Loan file | business days | up bad | Event or As-of (label) | Role, team | Ops leadership | D03, D06, D13 |
| M-CYC-16 | HOI accept cycle | P05 | First HOI request → HOI accepted | Loan file | business days | up bad | Event | Channel | Processing | D03, D05 |
| M-CYC-16A | MI cert cycle | P05 | MI apply → MI cert in. Files that do not require MI are out. | Loan file | business days | up bad | Event | Product, MI company | MI desk | D06 |
| M-CYC-17 | Docs out to signed | P08 | Docs out → signed | Loan file | business days | up bad | Event | Channel (R/W) | Closing | D07 |
| M-CYC-18 | Signed to funded | P08 | Signed → Funded | Loan file | business days | up bad | Event | Channel (R/W) | Funding | D07 |

---

## Aging and WIP (As-of)

| ID | Name | Subcategory | What it measures | Business formula | Grain | Unit | Direction | Time basis | Required dimensions | Owner | Dashboards |
|----|------|-------------|------------------|------------------|-------|------|-----------|------------|---------------------|-------|------------|
| M-AGE-01 | Units in milestone | P15 | WIP by milestone | Count of open files in each Current milestone | Loan file | files | context | As-of | Channel, milestone, team | Ops leadership | D02, D01 |
| M-AGE-02 | Age in current milestone | P15 | How long the file has sat here | Business days since milestone entered; show p50/p90 and bands 0–2, 3–5, 6–10, 11+ | Loan file | business days | up bad | As-of | Channel, milestone, Waiting-on party | Desk managers | D02, D03, D06 |
| M-AGE-03 | SLA-breach units | P15 | Files older than ASSUMED SLA for that milestone | Count where M-AGE-02 > SLA | Loan file | files / % | up bad | As-of | Channel, milestone, team | Ops leadership | D01, D02 |
| M-AGE-04 | Stuck files | P15 | No milestone change for N days (see SLA table) | Count of files with no milestone change ≥ stuck threshold | Loan file | files | up bad | As-of | Channel, milestone, Waiting-on party | Desk managers | D02 |
| M-AGE-05 | Waiting-on party mix | P15 | Who WIP is blocked on | Count / % of Pipeline by Waiting-on party | Loan file | files / % | context | As-of | Channel, milestone | Desk managers | D02, D03, D06, D08 |
| M-AGE-06 | Lock expiring before CTC | P15 | Locked files whose lock end is before likely CTC | Count of Pipeline files locked, not CTC, lock end ≤ As-of + remaining expected cycle | Loan file | files | up bad | As-of | Channel, product | Ops + CM | D02, D06 |
| M-AGE-07 | CTC but not scheduled | P07 | CTC without a closing date | Count of files with CTC and no schedule | Loan file | files | up bad | As-of | Channel (R/W), closer | Closing | D02, D07 |
| M-AGE-08 | Funded/purchased not delivered | P10 | Post-close aging | Age in business days since Funded or Correspondent purchase for M-VOL-14 files | Loan file | files / days | up bad | As-of | Channel, TPO, investor | Post-close | D09, D10 |
| M-AGE-09 | Delivered not investor-purchased | P11 | Investor suspense aging | Age since Delivered for files without Investor purchase | Loan file | files / days | up bad | As-of | Investor, Channel, Kickout flag | Delivery | D10 |

---

## Pull-through and fallout

Fallout reason set: withdrawn, denied, expired (lock or file), rejected (Correspondent/intake). Do not put Kickout in Fallout.

| ID | Name | Subcategory | Business formula | Grain | Unit | Direction | Time basis | Cohort default | Owner | Dashboards |
|----|------|-------------|------------------|-------|------|-----------|------------|----------------|-------|------------|
| M-FAL-01 | Pull-through start-to-fund | P15 | Funded / Files started for the same start-month cohort. **Retail/Wholesale only.** | Cohort | % | up good | Event (cohort) | File start month | Ops VP | D01, D02 |
| M-FAL-02 | Lock-to-fund pull-through | P15 | Funded / files that locked, cohort by lock month. **Retail/Wholesale only.** | Cohort | % | up good | Event (cohort) | Lock month | Ops VP | D01 |
| M-FAL-03 | Submission-to-purchase | P09 | Correspondent purchased / Submissions, cohort by Submission month | Cohort | % | up good | Event (cohort) | Submission month | Correspondent ops | D01, D08 |
| M-FAL-04 | Fallout units | P15 | Count of files in the cohort with a Fallout reason | Loan file | files | up bad | Event | Matches the paired pull-through | Ops VP | D02 |
| M-FAL-05 | Fallout rate | P15 | Fallout units / starts (R/W) or / Submissions (Corr) | Cohort | % | up bad | Event (cohort) | Same as M-FAL-01 or 03 | Ops VP | D01, D02, D08 |
| M-FAL-06 | Denial / withdraw / suspend rates | P06 | Denied / starts; withdrawn / starts; first-decision Suspense / decisioned | Cohort or Event | % | up bad | Event | Named on the visual | UW | D06, D02 |
| M-FAL-07 | Broker/TPO pull-through | P09/P15 | M-FAL-01 by Broker or M-FAL-03 by TPO | Cohort | % | up good | Event (cohort) | Same as parent | Channel ops | D08, D03 |

---

## Quality

File-fail rate = files with ≥1 confirmed defect / files reviewed. Finding rate = findings / files reviewed. Dashboards show **file-fail** as the headline; finding rate is a detail.

| ID | Name | Subcategory | Business formula | Grain | Unit | Direction | Time basis | Owner | Dashboards |
|----|------|-------------|------------------|-------|------|-----------|------------|-------|------------|
| M-QLT-01 | Conditions per file | P07 | Count of conditions issued / files decisioned (split PTD, PTF, total) | Loan file | count | up bad | Event | UW / conditions | D06 |
| M-QLT-02 | Suspense rate | P06 | First decision = Suspense / first decisions | Loan file | % | up bad | Event | UW | D06, D02 |
| M-QLT-03 | Rework rate | P07 | Files that return to an earlier Milestone / files that had reached the later Milestone | Loan file | % | up bad | Event | Ops leadership | D06, D11 |
| M-QLT-04 | Redisclosure rate | P01 | Files with ≥1 redisclosure / Files started (R/W) | Loan file | % | up bad | Event | Disclosure | D14 |
| M-QLT-05 | Appraisal revision / ROV rate | P03 | Orders with revision or ROV / appraisal orders | Order | % | up bad | Event | Appraisal desk | D04, D12 |
| M-QLT-06 | Title curative rate | P04 | Files with curative opened / files with commitment | Loan file | % | context | Event | Title desk | D05 |
| M-QLT-07 | Pre-fund QC defect rate | P12 | File-fail among pre-fund QC reviews, split critical/major/minor | Review | % | up bad | Event | Manufacturing QC | D11 |
| M-QLT-08 | Post-close QC defect rate | P12 | File-fail among post-close QC reviews, by severity | Review | % | up bad | Event | Manufacturing QC | D11 |
| M-QLT-09 | Correspondent pre-purchase defect rate | P12 | File-fail among pre-purchase reviews, by severity | Review | % | up bad | Event | Correspondent QC | D08, D11 |
| M-QLT-10 | Investor kickout / suspense rate | P11 | Kickouts (plus investor suspense if not cured in 1 day) / Delivered | Loan file | % | up bad | Event | Delivery / QC | D10, D11, D01 |
| M-QLT-11 | Kickout reason mix | P11 | % of Kickouts by reason code | Kickout | % | context | Event | Delivery | D10, D11 |
| M-QLT-12 | Trailing-doc missing rate | P10 | Files missing any required trailer at N business days after Funded/purchase / files aged ≥ N. Publish N=10 and N=15. | Loan file | % | up bad | As-of | Post-close | D09 |
| M-QLT-13 | TPO scorecard defects | P12 | Rolling 90-day M-QLT-09 and Kickouts attributable to TPO package | TPO | % / index | up bad | Rolling event | Correspondent ops | D08, D11 |
| M-QLT-14 | CTC revoke rate | P07 | CTC revokes / CTC events | Loan file | % | up bad | Event | UW / closing | D06, D07 |
| M-QLT-15 | Funding fail rate | P08 | Funding-fail events / attempted fundings | Loan file | % | up bad | Event | Funding | D07 |

---

## Capacity and productivity

| ID | Name | Subcategory | Business formula | Grain | Unit | Direction | Time basis | Owner | Dashboards |
|----|------|-------------|------------------|-------|------|-----------|------------|-------|------------|
| M-CAP-01 | Units completed per FTE | P14 | Completions in period / productive FTE (role: processor, UW, closer, post-closer, Corr analyst) | Role-day rolled to week | units/FTE | up good | Event / roster | Workforce | D13 |
| M-CAP-02 | Queue depth per FTE | P14 | Assigned open files / productive FTE at As-of | Role As-of | files/FTE | up bad if above SLA | As-of | Workforce | D13, D03, D06 |
| M-CAP-03 | Utilization | P14 | Files touched / capacity plan (plan = company roster target). If no plan, omit and show M-CAP-01/02 only. | Role-day | % | context | As-of + event | Workforce | D13 |
| M-CAP-04 | New vs WIP mix | P14 | New assignments in period vs already-in-queue completions | Role | % | context | Event | Desk managers | D13 |
| M-CAP-05 | Capacity vs arrival | P14 | Completions minus arrivals (starts, UW submits, CTCs, Submissions — named per role) | Role-week | units | up good if ≥ 0 | Event | Ops leadership | D01, D13 |
| M-CAP-06 | After-hours completions | P14 | Completions outside staffed hours / all completions. **Omit if timestamps lack time of day.** | Role | % | context | Event | Workforce | D13 |

---

## Vendor

| ID | Name | Subcategory | Business formula | Grain | Unit | Direction | Time basis | Owner | Dashboards |
|----|------|-------------|------------------|-------|------|-----------|------------|-------|------------|
| M-VEN-01 | Orders placed / completed | P13 | Count of orders placed; count completed | Order | orders | context | Event | Vendor mgmt | D12, D04, D05 |
| M-VEN-02 | Vendor cycle p50/p90 | P13 | Same clocks as M-CYC-08/09 (and credit/flood) by Vendor | Order | business days | up bad | Event | Vendor mgmt | D12 |
| M-VEN-03 | On-time % | P13 | Completed orders with cycle ≤ ASSUMED SLA / completed orders | Order | % | up good | Event | Vendor mgmt | D12 |
| M-VEN-04 | Revision rate | P13 | Orders with ≥1 revision / completed orders | Order | % | up bad | Event | Vendor mgmt | D12, D04 |
| M-VEN-05 | Cost per order | P13 | Sum of AP cost / completed orders. **Omit until Finance shares a joinable feed.** | Order | $ | up bad | Event | Vendor mgmt / Finance | D12 (optional) |
| M-VEN-06 | Concentration | P13 | Orders with Vendor / all orders of that type | Vendor | % | context | Event | Vendor mgmt | D12 |

---

## Forecast (As-of, expected conversions)

Not pull-through. These count files that **already** passed a gate and have not yet Funded or Correspondent-purchased. Label **expected if they all convert** until Q15 says otherwise.

| ID | Name | Business formula | Grain | Unit | Direction | Time basis | Owner | Dashboards |
|----|------|------------------|-------|------|-----------|------------|-------|------------|
| M-FST-01 | Expected funded next 7/14/30 | Count of Retail/Wholesale files with CTC or schedule date in the window, not yet Funded | Loan file | units | context | As-of | Ops leadership | D02, D01 (drill) |
| M-FST-02 | Expected correspondent purchase next 7/14/30 | Count of Correspondent files purchase-approved, not yet purchased, in the window | Loan file | units | context | As-of | Correspondent ops | D02, D08 |
| M-FST-03 | Expected funded + purchased next 7 | M-FST-01 + M-FST-02 for the 7-day window | Loan file | units | context | As-of | Ops VP | D02 |

## Regulatory display (TRID)

| ID | Name | Business formula | Grain | Unit | Direction | Time basis | Owner | Dashboards |
|----|------|------------------|-------|------|-----------|------------|-------|------------|
| M-REG-01 | Initial LE miss rate | Files with E-LE-INIT after E-TRID-APP + 3 **TRID general business days** / files with E-LE-INIT in period. Saturday counts only if the creditor is open. | Loan file | % | up bad | Event | Disclosure | D14 |

---

## D01 headline set (eight KPIs)

Use only these on the Command Center headline row:

1. M-VOL-13 Pipeline units  
2. M-VOL-16 Funded + purchased units  
3. M-CYC-03 p50 (Retail/Wholesale) and M-CYC-11 p50 (Correspondent) — two numbers, labeled  
4. M-VOL-05 CTC count (R/W) + M-VOL-05C (Corr) labeled  
5. M-AGE-03 SLA-breach % of Pipeline  
6. M-FAL-01 and M-FAL-03 pull-through, labeled by Channel  
7. M-QLT-10 Kickout rate  
8. M-CAP-05 Capacity vs arrival (processors + UW combined, with a drill)

---

## Counting rules

- One Loan file counts once in a flow metric for a given event. A second Funded event on the same file is a data-quality incident, not two units.
- Waivers are not appraisal orders.
- Correspondent files never increment M-VOL-06/07 or M-FAL-01/02.
- Retail/Wholesale files never increment M-VOL-08/09/10 or M-FAL-03.
- Kickout is not Fallout.
- Independent audit QC is not M-QLT-07/08/09.
