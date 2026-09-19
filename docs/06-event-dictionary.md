# Event dictionary

## Overview

Every Operations metric is a count, sum, rate, or clock on **named events**. This dictionary is the data contract for a later source-system map. It does not name LOS tables.

**Rule:** If an event is not stamped, the metric that needs it is unavailable — show it as unavailable, not zero.

Canonical **milestones** and **reason codes** (waiting-on, Fallout, Kickout, defects): [11-milestones-and-reason-codes.md](11-milestones-and-reason-codes.md).

Grain: Loan file unless noted. Channel tells you which events apply.

## File start and disclosure

| Event ID | Name | When it fires | Channel | Used by |
|----------|------|---------------|---------|---------|
| E-START | File start | Setup/registration/intake complete; Loan file is open in Operations | All | M-VOL-01, M-CYC-01/03/05, M-FAL-01, Pipeline membership |
| E-APP | Application taken | Borrower application recorded (TRID application date may differ — store both) | R/W | M-VOL-02, M-CYC-04 start |
| E-TRID-APP | TRID application date | Regulatory application date | R/W | M-CYC-04 start |
| E-LE-INIT | Initial LE sent | First Loan Estimate transmitted | R/W | M-CYC-04 stop, LE miss rate |
| E-LE-SIGN | LE signed / eSign complete | Borrower (or Broker path) completed disclosure eSign | R/W | D14 eSign WIP |
| E-ITP | Intent to proceed | Borrower intends to proceed | R/W | Gate for most settlement-service orders |
| E-REDISC | Redisclosure issued | Subsequent LE (or CD redisclosure if captured here) | R/W | M-QLT-04 |
| E-INTAKE-REJ | Intake rejected | Correspondent package rejected before Submission | Corr | Fallout reason: rejected |

## Processing and third parties

| Event ID | Name | When it fires | Grain | Used by |
|----------|------|---------------|-------|---------|
| E-PROC-ASGN | Processor assigned | Current processor set | File | Capacity queue |
| E-WAIT | Waiting-on party changed | Borrower / Broker-TPO / Vendor / internal | File | M-AGE-05, M-CYC-15 |
| E-UW-SUBMIT | Submitted to UW | Processing complete; file in UW queue | File (R/W) | M-CYC-05 stop, M-CYC-06 start, M-CAP-05 |
| E-PKG-COMPLETE | Package complete | Correspondent analog of UW submit | File (Corr) | D08 funnel |
| E-AUS | AUS run | AUS recommendation stamped | File | Dimension, not a volume metric |
| E-APPR-WAIVE | Valuation waiver | Waiver used; no order | File | M-VOL-15; exclude from M-CYC-08 |
| E-APPR-ORD | Appraisal ordered | Company order placed | Order | M-CYC-08 start, M-VEN-01 |
| E-APPR-RCV | Appraisal received in | Report in (or Broker-ordered received) | Order | M-CYC-08 stop; Broker path may start here |
| E-APPR-REV | Appraisal review complete | Value accepted or rejected | Order/file | M-CYC-08A |
| E-ROV | ROV opened / resolved | Reconsideration of value | Order | M-QLT-05 |
| E-TTL-ORD | Title ordered | Company title order | Order | M-CYC-09 start |
| E-TTL-CMT | Title commitment in | Commitment received | Order | M-CYC-09 stop |
| E-TTL-CUR-OPEN | Curative opened | Exception work started | File | M-QLT-06 |
| E-TTL-CUR-CLR | Curative cleared | Exceptions resolved | File | M-CYC-09A |
| E-HOI-REQ | HOI first requested | | File | M-CYC-16 start |
| E-HOI-OK | HOI accepted | | File | M-CYC-16 stop |
| E-FLOOD | Flood determination in | | Order | Vendor credit/flood |
| E-MI-APP | MI applied | Product requires MI | File | M-CYC-16A start |
| E-MI-CERT | MI certificate in | | File | M-CYC-16A stop |

## Underwriting, conditions, CTC

| Event ID | Name | When it fires | Used by |
|----------|------|---------------|---------|
| E-UW-ASGN | UW assigned | | Queue / M-CAP-02 |
| E-UW-FIRST | First UW decision | First approve / Suspense / deny (R/W) or eligible / conditions / reject (Corr) | M-VOL-04, M-CYC-06, M-QLT-02 |
| E-UW-LATER | Subsequent UW decision | After Suspense or new conditions | Do not overwrite E-UW-FIRST |
| E-COND-ISS | Condition issued | One row per condition, PTD or PTF | M-QLT-01, M-CYC-07 start |
| E-COND-CLR | Condition cleared | That condition accepted | M-CYC-07 stop |
| E-CTC | Clear to Close | First CTC stamp | M-VOL-05, M-CYC-01 stop, M-CYC-02 start |
| E-CTC-REV | CTC revoked | | M-QLT-14 |
| E-PUR-APPR | Purchase approved | Correspondent analog of CTC | M-VOL-05C, D08 forecast |

## Closing, funding, Correspondent purchase

| Event ID | Name | Channel | Used by |
|----------|------|---------|---------|
| E-SCHED | Closing scheduled | R/W | M-AGE-07 inverse |
| E-CD-SENT | Closing Disclosure sent | R/W | D07 / TRID CD (operational, not D14 headline) |
| E-DOCS-OUT | Closing docs out | R/W | M-CYC-17 start |
| E-SIGNED | Signed | R/W | M-CYC-17 stop, M-CYC-18 start |
| E-FUND-ATT | Funding attempted | R/W | M-QLT-15 denominator |
| E-FUND-FAIL | Funding failed | R/W | M-QLT-15 |
| E-FUNDED | Funded | R/W only | M-VOL-06/07, M-CYC-02/03/18 stop, Pipeline end |
| E-SUB | Submission complete | Corr | M-VOL-08, M-CYC-11 start, M-FAL-03 |
| E-PURCHASED | Correspondent purchase | Corr only | M-VOL-09/10, M-CYC-11 stop, Pipeline end |
| E-FALLOUT | Fallout | All | Reason required: withdrawn, denied, expired, rejected. M-FAL-04/05 |

## Post-close and delivery

| Event ID | Name | Used by |
|----------|------|---------|
| E-TRAIL-IN | Trailing document received | Per document type. M-QLT-12, M-CYC-12 |
| E-SHIP-RDY | Ship-ready | Stack complete. M-CYC-12 stop, M-CYC-13 start preferred |
| E-DELIVERED | Delivered | M-VOL-11, M-CYC-13 stop, M-CYC-14 start |
| E-INV-SUSP | Investor suspense | M-AGE-09 |
| E-KICKOUT | Kickout | M-QLT-10/11. Not Fallout |
| E-REDELIVER | Redelivered after Kickout | Footnote on M-QLT-10: file-level ≥1 Kickout |
| E-INV-PURCH | Investor purchase | Purchase advice. M-VOL-12, M-CYC-14 stop |

## Quality, vendor, capacity

| Event ID | Name | Grain | Used by |
|----------|------|-------|---------|
| E-QC-START / E-QC-DONE | Manufacturing QC review | Review | M-QLT-07/08/09 coverage |
| E-DEFECT | Confirmed defect | Finding | Severity required. File-fail = ≥1 critical/major as defined |
| E-ORD-PLACE / E-ORD-DONE / E-ORD-REV | Vendor order | Order | M-VEN-* |
| E-COMPLETE-ROLE | Role completion | File × role | M-CAP-01: processor = E-UW-SUBMIT; UW = E-UW-FIRST; closer = E-FUNDED; post-closer = E-SHIP-RDY; Corr analyst = E-PURCHASED or E-UW-FIRST |
| E-AS-OF | Snapshot | Enterprise | 6:00 a.m. ops calendar. M-VOL-13/14, M-AGE-*, M-VOL-03, M-CAP-02 |

## Minimum viable event set (MVP)

A first semantic layer can ship D01/D02 without every Vendor event. These are **required** for Command Center + Pipeline:

E-START, E-UW-FIRST, E-CTC, E-PUR-APPR, E-FUNDED, E-SUB, E-PURCHASED, E-DELIVERED, E-INV-PURCH, E-KICKOUT, E-FALLOUT (with reason), E-WAIT, Current milestone at E-AS-OF, Lock status at E-AS-OF, Channel, product, team.

Without E-WAIT, hide M-AGE-05 and M-CYC-15. Without role assignment, hide D13.
