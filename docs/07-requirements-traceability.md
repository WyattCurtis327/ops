# Requirements traceability

## Overview

Maps each subcategory to the metrics it produces and the dashboards that consume them. If a dashboard KPI is not in this table, it is a defect in the pack.

IDs: [processes](02-processes-by-subcategory.md), [catalog](04-metric-catalog.md), [dashboards](05-dashboard-inventory.md), [events](06-event-dictionary.md).

## Process → metrics → dashboards

| Process | Primary metrics | Primary dashboards | Critical events |
|---------|-----------------|--------------------|-----------------|
| P01 Disclosure and setup | M-VOL-01, M-VOL-02, M-CYC-04, M-QLT-04, M-REG-01 | D14, D01 (starts), D02 | E-START, E-APP, E-TRID-APP, E-LE-INIT, E-REDISC |
| P02 Processing | M-CYC-05, M-AGE-01–05, M-CAP-01/02, M-CYC-15, M-CYC-16 | D03, D02, D13 | E-UW-SUBMIT, E-WAIT, E-PROC-ASGN |
| P03 Appraisal | M-CYC-08/08A, M-VOL-15, M-QLT-05, M-VEN-01–04 | D04, D12 | E-APPR-WAIVE, E-APPR-ORD, E-APPR-RCV, E-APPR-REV, E-ROV |
| P04 Title | M-CYC-09/09A, M-QLT-06, M-VEN-* | D05, D12 | E-TTL-ORD, E-TTL-CMT, E-TTL-CUR-* |
| P05 Insurance and MI | M-CYC-16, M-CYC-16A | D03, D05, D06 | E-HOI-*, E-FLOOD, E-MI-* |
| P06 Underwriting | M-VOL-04, M-CYC-06, M-QLT-02, M-CAP-01 | D06, D13, D08 | E-UW-FIRST (immutable) |
| P07 Conditions and CTC | M-VOL-05, M-CYC-01/07/07F, M-QLT-01/03/14, M-AGE-06/07 | D06, D02, D07 | E-COND-*, E-CTC, E-CTC-REV |
| P08 Closing and funding | M-VOL-06/07, M-CYC-02/03/10/17/18, M-QLT-15 | D07 | E-SCHED, E-DOCS-OUT, E-SIGNED, E-FUNDED, E-FUND-FAIL |
| P09 Correspondent | M-VOL-08/05C/09/10, M-CYC-11/11A, M-FAL-03/07, M-QLT-09/13 | D08, D01, D11 | E-SUB, E-PUR-APPR, E-PURCHASED |
| P10 Post-close | M-VOL-14, M-CYC-12, M-AGE-08, M-QLT-12 | D09 | E-TRAIL-IN, E-SHIP-RDY |
| P11 Investor delivery | M-VOL-11/12, M-CYC-13/14, M-AGE-09, M-QLT-10/11 | D10, D11, D01 | E-DELIVERED, E-KICKOUT, E-INV-PURCH |
| P12 Manufacturing quality | M-QLT-07–13 | D11 | E-QC-*, E-DEFECT, E-KICKOUT |
| P13 Vendor management | M-VEN-01–06 | D12 | E-ORD-* |
| P14 Capacity | M-CAP-01–06 | D13, D01 | E-COMPLETE-ROLE, roster, E-AS-OF |
| P15 Pipeline control | M-VOL-13/14/03/16, M-AGE-01–09, M-FAL-01–07, M-FST-01–03 | D02, D01 | E-AS-OF, all lifecycle ends |

## Persona → dashboard → decision

| Persona | Home | Must-answer questions (from specs) |
|---------|------|-------------------------------------|
| COO / Ops VP | D01 | Health of conversion, cycle, SLA, kickouts, capacity |
| Desk managers | D02 then D03/D06/D07/D09 | Queue, age, waiting-on, stuck |
| Appraisal / title | D04, D05, D12 | Vendor on-time, ROV, curative |
| Correspondent ops | D08 | Purchase pull-through, TPO defects |
| Delivery | D10 | Delivered vs investor purchased |
| QC | D11 | Manufacturing defects vs kickouts |
| Workforce | D13 | FTE vs arrivals |
| Disclosure | D14 | 3-calendar-day LE |
| BI | Catalog + events | Grain, direction, event IDs |

## Counting collisions (traceability of rules)

| Risk | Rule | Where enforced |
|------|------|----------------|
| Correspondent in Funded | M-VOL-06/07 exclude Corr | Catalog counting rules, D07 default filter |
| Funded used for TPO buy | Use E-PURCHASED / M-VOL-09 | CONTEXT, D08 copy |
| Delivered = investor purchased | Separate E-DELIVERED and E-INV-PURCH | D10 |
| Kickout as Fallout | Kickout is post-delivery | CONTEXT, M-QLT-10 vs M-FAL-04 |
| Waiver in appraisal cycle | Exclude E-APPR-WAIVE from M-CYC-08 | D04 |
| First UW overwritten | Persist E-UW-FIRST | D06 |
| Audit QC in manufacturing | Filter QC type | D11 |
| As-of mixed with event-dated | Label every tile | D01 header |
