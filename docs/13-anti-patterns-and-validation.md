# Anti-patterns, recon, and validation

## Overview

How Operations numbers go wrong, how to recon them, and questions to ask each desk so this pack is validated rather than installed.

## Anti-patterns (do not ship)

| Anti-pattern | What it does | Correct |
|--------------|--------------|---------|
| One tile named Funded for all channels | Mixes E-FUNDED, E-PURCHASED, E-INV-PURCH | M-VOL-16 labeled **Funded + purchased**; split on drill |
| Average cycle time only | Hides the stuck tail | p50 **and** p90 |
| Cycle time includes in-flight files | Mixes age with completed clocks | Completed = M-CYC-*; in-flight = M-AGE-02 |
| Average R/W start-to-fund with Corr purchase cycle | Unlike clocks | Two numbers on EXE |
| Kickout in Fallout | Punishes delivery for a sold loan | M-QLT-10 vs M-FAL-04 |
| Correspondent reject as credit deny | Wrong Fallout mix | FAL-REJ |
| Waiver files in appraisal order-to-report | Fake Vendor misses | Exclude E-APPR-WAIVE from M-CYC-08 |
| Broker-ordered appraisal with no received-in date, dropped | Understates Wholesale | Label received-to-report or unavailable |
| Waiting-on blank treated as internal | Blames the desk | % blank as data quality |
| Pipeline includes post-close | Double-counts manufacturing vs delivery | M-VOL-13 vs M-VOL-14 |
| Partial week unlabeled on EXE | Fake WoW | Partial banner |
| Missing events shown as 0 | Fake “perfect” kickout rate | Unavailable |
| Gauge / donut / RAG tile for Pipeline | Implies up is bad | Neutral context |
| LOS worklist rebuilt in BI | Two queues | P15 export only |
| Audit QC on P12 | Wrong owner | Filter out or hide KPI |
| TPO on the Vendor dashboard | Wrong scorecard | P09 / P12 |
| TRID initial LE as calendar days | False misses if Sat/Sun counted while offices closed | General business days (creditor-open) on P01; specific business days only for CD wait |
| Finance recon to M-VOL-16 only | Corr and Retail will never match GL the same way | Recon M-VOL-06 and M-VOL-09 separately |

## Recon checks (before calling a dashboard “done”)

Tolerance is a leadership choice. Until then, treat **any unexplained gap** as a defect.

| Check | Left | Right | Grain |
|-------|------|-------|-------|
| R1 | M-VOL-06 Funded units | Finance / warehouse origination fundings | Event-dated week, Channel R/W |
| R2 | M-VOL-09 Corr purchased units | Purchase advice to TPO / warehouse buys | Event-dated week |
| R3 | M-VOL-11 Delivered | Investor delivery extracts | Event-dated week |
| R4 | M-VOL-12 Investor purchased | Purchase advice from investor | Event-dated week |
| R5 | M-VOL-13 Pipeline | LOS open-file count using canonical milestones | Same As-of timestamp |
| R6 | M-VOL-01 Files started | LOS new-file count per File start definition | Event-dated week |
| R7 | Sum of M-AGE-01 across milestones | M-VOL-13 + (optional setup) | As-of; investigate remainder |
| R8 | M-FAL-04 + remaining Pipeline + Funded/purchased of that start cohort | M-VOL-01 of that cohort | Cohort month; allow in-flight |

R8 is the **cohort identity**: starts = still in Pipeline + Fallout + Funded/purchased (for that Channel). If it does not add up, File start or Fallout coding is wrong — do not go live on pull-through.

## Validation interviews (one hour per desk)

Ask the process owner. Capture LOS field names in the synonym column of [milestones and reasons](11-milestones-and-reason-codes.md). Do not redesign the taxonomy in the room unless they prove a Channel is missing.

**Every desk**

1. What is a file “in your queue” in the LOS today (status name)?
2. When do you consider it no longer yours?
3. Who are you usually waiting on? Map to WAIT-*.
4. What SLA do you actually manage to (ignore our ASSUMED if they have one)?
5. Show one file that would break our clock.

**P01** — TRID application date vs LOS application date vs intent to proceed?  
**P02** — When is “submitted to UW” stamped? Can it fire with an incomplete package?  
**P03** — Broker-ordered vs company-ordered: where is received-in?  
**P04** — Is curative a flag or a free-text note?  
**P05** — HOI received vs accepted? MI-required population?  
**P06** — Is first decision overwritten? AUS vs UW?  
**P07** — PTD vs PTF in the LOS? CTC revoke event?  
**P08** — Funded date vs disbursement vs “docs back”? Table-fund vs lender-fund?  
**P09** — Registration vs Submission vs purchased vs investor purchased?  
**P10** — Required trailer list by product/investor, or one generic checklist?  
**P11** — Delivered vs purchased in the same field? Kickout vs suspense?  
**P12** — Manufacturing vs audit in one table? Severity values?  
**P13** — Conformed Vendor names? Staff appraisers in the AMC list?  
**P14** — Productive FTE source? PTO? Dual assignment?  
**P15** — What do they call stuck today?

## Prototype acceptance (add to phase 1 exit)

Phase 1 is not done until:

1. R5 (Pipeline vs LOS) holds at one As-of.
2. R8 holds for the last complete start-month cohort (R/W and Corr separately).
3. A Wholesale Broker-ordered appraisal file does not vanish from P03 or get a fake order-to-report.
4. A Correspondent purchased file does not appear in M-VOL-06.
5. P15 stuck export opens and the same loan is the LOS queue item.

## What not to add next

- Servicing, lock-desk P&L, lead CPL, construction-draw dashboard, HELOC-only EXE.
- Pixel mockups that rename Funded.
- Metric-view YAML before Q3 (File start) and R1/R2 recon owners are named.
