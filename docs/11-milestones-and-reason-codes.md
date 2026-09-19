# Milestones and reason codes

## Overview

Aging, stuck files, Fallout, Kickouts, and Waiting-on party only work if codes are **conformed**. This is the canonical list for Operations reporting. Map LOS values here; do not display raw LOS status strings on EXE or P15.

Local LOS names go in the synonym column when discovered. Until then, use these IDs.

## Canonical milestones

Pipeline (M-VOL-13) is files in MS-01 through MS-08 (R/W) or MS-01, MS-09, MS-10 (Corr) that are not yet Funded or Correspondent-purchased. Post-close WIP (M-VOL-14) is MS-11 and MS-12 before Delivered. Delivered-not-purchased is MS-13 (not Pipeline).

| ID | Milestone | Channel | Pipeline? | Desk (wireframe) | ASSUMED age SLA | Stuck after |
|----|-----------|---------|-----------|------------------|-----------------|-------------|
| MS-01 | Setup / intake | All | Yes | P01 / P09 | 1 bd | 2 bd |
| MS-02 | Disclosures | R/W | Yes | P01 | 3 TRID general business days to LE send | 2 bd no LE send |
| MS-03 | Processing | R/W (Corr only if assigned to processors) | Yes | P02 | 5 bd | 3 bd |
| MS-04 | Appraisal outstanding | R/W; Corr if new order | Yes | P03 | 7 bd order-to-report | n/a (order grain) |
| MS-05 | Title outstanding | R/W; Corr if curative | Yes | P04 | 5 bd to commitment | n/a |
| MS-06 | Underwriting | All | Yes | P06 | 2 bd to first decision | 2 bd |
| MS-07 | Conditions | All | Yes | P07 | 5 bd | 3 bd |
| MS-08 | CTC / scheduled | R/W | Yes | P08 | 5 bd to Funded | 2 bd |
| MS-09 | Corr submitted | Corr | Yes | P09 | 2 bd to decision | 2 bd |
| MS-10 | Purchase approved | Corr | Yes | P09 | 1 bd to purchased | 2 bd |
| MS-11 | Post-close / trailing | All after Funded or Corr purchase | No (Post-close WIP) | P10 | 15 bd to ship-ready | 5 bd |
| MS-12 | Ship-ready | All | No (Post-close WIP) | P11 | 2 bd to Delivered | n/a |
| MS-13 | Delivered not investor-purchased | All | No | P11 | 5 bd | 3 bd |

A file has **one** current milestone. Appraisal outstanding and title outstanding are allowed as current only if the LOS uses them as the file’s stage; otherwise they are order states on a file that is still MS-03 or MS-07. **Prefer file milestone = processing/conditions and show third-party blocks via Waiting-on = Vendor.** Use MS-04/MS-05 only if the LOS truly parks the file there.

Do not invent “closing” as separate from MS-08 if CTC and scheduled are the same LOS bucket — split only when E-SCHED exists.

## Waiting-on party codes

Exactly four headline values. Map everything else into these.

| Code | Meaning | Typical examples | Who acts |
|------|---------|------------------|----------|
| WAIT-BOR | Borrower | Docs, eSign, HOI binder, intent to proceed | LO / processor chase |
| WAIT-TPO | Broker or TPO | Wholesale Broker conditions; Correspondent seller conditions or trailers | Channel ops |
| WAIT-VEN | Vendor | AMC, appraiser, title, flood, HOA, MI company | Desk + vendor mgmt |
| WAIT-INT | Internal | Unassigned, UW queue, closer not scheduled, QC hold, funding desk | That desk |

Blank waiting-on is a **data-quality fail**, not a fifth code. P15 should show % blank. If blank > 20%, banner the dashboard.

HOA is Vendor, not borrower. County recording is Vendor (title/jurisdiction), not internal.

## Fallout reason codes

Fallout is **before** Funded (R/W) or Correspondent purchase. Kickout is not Fallout.

| Code | Name | Channel | Counts in M-FAL-04 |
|------|------|---------|-------------------|
| FAL-WDN | Withdrawn | All | Yes |
| FAL-DEN | Denied (credit) | R/W | Yes |
| FAL-REJ | Rejected (package / eligibility) | Corr, intake | Yes — **not** FAL-DEN |
| FAL-EXP | Expired (file or lock with no continuation) | All | Yes |
| FAL-DUP | Duplicate / combined file | All | Yes, but exclude from pull-through denominator if the surviving file continues |
| FAL-INC | Incomplete / unable to contact | R/W | Yes |

Do not add “cancelled” as a code. Map it to withdrawn or expired.

## Kickout / investor suspense reasons

Short list for M-QLT-11. Map investor free text here.

| Code | Name | Usual desk to cure |
|------|------|--------------------|
| KIK-TRL | Trailing / stack / recorded instrument | P10 |
| KIK-COL | Collateral / appraisal / property | P03, P12 |
| KIK-CRD | Credit / income / AUS | P06, P09 |
| KIK-TTL | Title / vesting / lien | P04 |
| KIK-DAT | Data / ULDD / MISMO | P11 |
| KIK-TPO | TPO package (Corr) | P09 |
| KIK-MI | MI / insurance | P05 |
| KIK-OTH | Other | P11 until recoded |

Investor suspense that clears in 1 business day without a Kickout stamp: age on M-AGE-09, do not increment M-QLT-10.

## Manufacturing defect severity

| Severity | Meaning | Stops CTC or purchase? |
|----------|---------|------------------------|
| Critical | Investor-purchasable or compliance-breaking if uncorrected | Yes |
| Major | Likely Kickout or redisclosure if uncorrected | Usually |
| Minor | Process miss, not likely investor-visible | No |

Headline file-fail on P12 = critical (show major/minor in the menu). Finding count is detail.

## Condition class

| Class | When it must clear | Metric split |
|-------|-------------------|--------------|
| PTD | Before docs drawn / before CTC | M-QLT-01 PTD |
| PTF | Before Funded | M-QLT-01 PTF |
| PTP | Before Correspondent purchase | Same catalog, Channel = Corr |

## Trailing document types (P10 heatmap)

| Code | Document |
|------|----------|
| TRL-NOTE | Original note |
| TRL-SEC | Recorded security instrument |
| TRL-TTL | Final title policy |
| TRL-MI | Final MI cert if required |
| TRL-OTH | Other investor-required trailer |

Required set is product × investor. A generic checklist inflates M-QLT-12 — if the feed is generic, footnote it.
