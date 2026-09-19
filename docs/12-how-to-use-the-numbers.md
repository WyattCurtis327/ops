# How to use the numbers

## Overview

Job aids for EXE, the daily huddle, alerts, and a simple staffing read. Metric IDs are in the [catalog](04-metric-catalog.md). Codes are in [milestones and reasons](11-milestones-and-reason-codes.md).

## EXE driver tree (diagnose a tile in order)

Do not stare at eight tiles equally. Read top to bottom.

```text
Funded + purchased (M-VOL-16)
├─ Retail/Wholesale Funded (M-VOL-06)  → P08
└─ Correspondent purchased (M-VOL-09) → P09

If M-VOL-16 is down:
  1. Pull-through (M-FAL-01 / M-FAL-03) down? → Fallout mix on P15, not a speed problem
  2. Pipeline (M-VOL-13) down? → starts (M-VOL-01) — Sales handoff, not Ops speed
  3. CTC / purchase-approved down? → P07 / P09
  4. Cycle p50 up? → which clock (M-CYC-03 vs M-CYC-11); never average them
  5. SLA-breach % up with stable volume? → P15 aging + Waiting-on
  6. Completions − arrivals (M-CAP-05) negative? → P14 capacity
  7. Kickout rate up? → P11 then P12 (do not call it Fallout)
```

**Two-signal rule:** Pipeline up **and** SLA-breach % up → capacity or Vendor. Pipeline up **and** pull-through down → Fallout. Pipeline down **and** Funded + purchased down → not enough starts (Sales), unless CTC is also down (Ops gate).

## Daily huddle (30 minutes) — P15

As-of is 6:00 a.m. Export stuck files; work them in the LOS.

| Minute | Look at | Action |
|--------|---------|--------|
| 0–5 | SLA-breach % and stuck count by Channel | Name the milestone that moved overnight |
| 5–12 | Waiting-on mix for that milestone | If WAIT-INT is majority, the desk owns it. If WAIT-VEN, name the Vendor. If WAIT-TPO, name the Broker/TPO. |
| 12–20 | Stuck export (top 15 by age) | Assign a next action in LOS, not in BI |
| 20–25 | Lock expiring before CTC (M-AGE-06) | Ping CM only for files Ops can still CTC |
| 25–30 | 7-day expected fund+purch (M-FST-03) | If hatched bar >> staffed closings/wires, flag P08/P09 today |

Do not use EXE in the daily huddle. EXE is weekly.

## Weekly Ops (45 minutes) — EXE

1. M-VOL-16 vs last week (Channel split).
2. Two cycle p50s (R/W vs Corr) vs ASSUMED SLA.
3. SLA-breach % and M-CAP-05.
4. Kickout rate — one sentence from P11.
5. One drill only: the tile that moved. Park the rest.

## Recommended alerts (ASSUMED until Q1)

Alerts fire on the **last complete week** or on the morning As-of, never on a partial weekday without a Partial label.

| Alert | Metric | Fire when | Notify |
|-------|--------|-----------|--------|
| A-SLA | M-AGE-03 | SLA-breach % of Pipeline > 20% As-of | Ops VP + desk of the hottest milestone |
| A-STK | M-AGE-04 | Stuck files WoW +25% and n ≥ 20 | P15 owner |
| A-CAP | M-CAP-05 | Completions − arrivals < 0 for 3 consecutive business days (processor or UW) | P14 + that desk |
| A-KIK | M-QLT-10 | Kickout rate > 4% on last 20+ Delivered | P11 + P12 |
| A-LE | M-REG-01 | LE miss rate > 5% on last complete week | P01 |
| A-FAL | M-FAL-05 | Fallout rate +5 pp vs prior complete week, same Channel | Ops VP |
| A-LCK | M-AGE-06 | Lock-expiring-before-CTC > 50 files | P07 + CM (count only; no lock-desk KPI) |
| A-VEN | M-VEN-03 | AMC or title on-time % < 70% and volume ≥ 30 orders | P13 + P03/P04 |

Do not alert on Pipeline units up. That is context.

## Staffing read (P14) — back of the envelope

Not a workforce optimizer. For one role (example: processor):

1. Arrivals this week = File starts that will need a processor (R/W) or Submissions (Corr analysts).
2. Completions this week = E-UW-SUBMIT (or E-PURCHASED for Corr analysts).
3. M-CAP-05 = completions − arrivals. Negative means queue will grow.
4. Queue / FTE = M-CAP-02. If above the ASSUMED band (processors 15–25, UW 8–12) **and** M-CAP-05 is negative, add capacity or refuse new Channel mix.
5. Units / FTE (M-CAP-01) falling while queue/FTE rises = productivity + arrival problem, not “we need more dashboards.”

Credit completions to the completing assignee. Do not divide Pipeline by payroll headcount.

## Industry-typical bands (context only)

Not targets. Not Q1 answers. Use to sanity-check a prototype, then hide or replace.

| Signal | Rough non-bank origination band | If you are far outside |
|--------|--------------------------------|------------------------|
| Start-to-fund p50 (purchase, conventional, Retail) | ~20–35 business days | Check File start definition and CTC-to-fund |
| UW first-decision p50 | same day to 2 business days | Check what “submitted to UW” means |
| Correspondent submission-to-purchase p50 | 2–5 business days | Check Submission vs registration |
| Kickout rate | low single digits | Check if suspense is counted as Kickout |
| LE miss rate | should be rare | TRID operational risk — P01 |

If a prototype shows start-to-fund p50 of 4 days, the clock is probably CTC-to-fund or you are on Correspondent purchase.

## Seasonality (do not hide in WoW)

Purchase files lengthen when appraisal/title vendors congest (spring). Refinance mix shortens processing but can spike redisclosure. Always slice WoW by **loan purpose** before declaring a process miss. EXE may stay mixed; the drill must split.
