# Research sources and implications

## Overview

Cited industry, GSE, and regulatory sources that support, challenge, or refine this Operations pack. Numbers below are **benchmarks from named studies**, not company targets. `ASSUMED SLA` in the catalog stays unlabeled policy until Q1.

**Pack correction from this research:** Initial Loan Estimate timing is **not** calendar days. See [TRID](#trid-two-business-day-definitions).

## Source families to keep on the shelf

| Family | What it is good for | Access |
|--------|---------------------|--------|
| MBA Quarterly / Annual Mortgage Bankers Performance Report | IMB cost to originate, pull-through, productivity per FTE | Subscription; public charts on MBA Newslink |
| MBA + STRATMOR Peer Group Roundtables (PGR) | Channel-level cost, pull-through, processor/UW units per FTE | Membership |
| MBA Wholesale Lending Survey | Broker and non-delegated correspondent **turn times** and pull-through | Public charts; survey is MBA |
| ICE Origination Insight / Mortgage Monitor | Days-to-close, app-to-lock, lock-to-close, closing/pull-through rates | ICE publications |
| ACES Mortgage QC Industry Trends | Post-close **critical defect rate** and defect mix | Quarterly PDF |
| Fannie Mae Selling Guide (esp. D1-2, C1-2, B4-1) | Prefunding QC sample, ULDD/delivery, ROV, Value Acceptance | Public |
| CFPB Regulation Z / KBYO small-entity guide | TRID clocks and two definitions of business day | Public |
| Freddie Mac Cost to Originate studies | Efficiency spread (top vs bottom quartile cost) | Public PDF |

Vendor blogs (AMC turn times, LOS KPI listicles) are **secondary**. Use them only to confirm process steps, not as SLA policy.

---

## Independent mortgage banks and cost

MBA’s 2025 Annual Mortgage Bankers Performance Report: IMBs and bank mortgage subsidiaries averaged **$785 net production profit per loan** in 2025 (up from $443 in 2024). Average production volume **$2.5 billion / 7,273 loans** per company. Refi share of study originations **21%** (MBA estimates industry refi share **34%**). Average first-mortgage balance **$371,965**. Walsh: rising wages, third-party charges, and **reduced application pull-through** kept per-loan costs from falling when volume rose. ([MBA Newslink, 20 Apr 2026](https://newslink.mba.org/servicing-newslink/2026/april/mba-servicing-newslink-tuesday-april-21-2026/mba-imbs-post-improved-net-production-profits-in-2025/))

Q1 2026 quarterly report: pre-tax production profit **$727/loan (16 bps)**; production expenses **336 bps / $11,898 per loan**; volume 1,729 loans per company. The series also publishes **productivity and pull-through**. ([MBA, 15 May 2026](https://www.mba.org/news-and-research/newsroom/news/2026/05/15/imbs-production-profits-remain-flat-in-first-quarter-of-2026))

MBA/STRATMOR PGR, retail channel 2025: independents’ cost to originate **$12,209**; depositories **$16,320**, with sales 42% and corporate/production-support allocations 38% of depository cost. ([MBA Newslink, 18 Jun 2026](https://newslink.mba.org/mba-newslinks/2026/june/mba-newslink-monday-june-22-2026/chart-of-the-week-retail-production-channel-cost-to-originate-a-loan/))

Freddie Mac 2024 Cost to Originate (Q3 2023 statements): industry ~**$11,600**; top quartile ~**$6,900**; bottom quartile ~**$16,500**. ([Freddie Mac PDF](https://sf.freddiemac.com/docs/pdf/cost-to-originate-full-study-2024.pdf))

**Implication for this pack:** Cost per loan and gain-on-sale stay **out of Operations EXE** (Finance / Capital Markets). Ops still owns the **drivers** MBA says are hurting cost: pull-through, third-party cycle, and FTE productivity (M-FAL-*, M-VEN-*, M-CAP-*). Do not put $11,898 on D01.

---

## Pull-through (Retail)

MBA + STRATMOR PGR: Retail pull-through fell 2021 through 1H 2025. **Depositories 55%**, **independents 69%** in 1H 2025 — independents’ lowest since 2012, depositories’ lowest in the PGR series since 2000. Definition: closings / applications in the period (not a lock cohort). Including leads/preapprovals would be lower. Reasons cited: multi-app shopping, qualification, payment shock (taxes/insurance/HOA), home condition, process complexity. ([MBA Newslink, 31 Oct 2025](https://newslink.mba.org/mba-newslinks/2025/october/mba-newslink-tuesday-nov-4-2025/chart-of-the-week-retail-channel-mortgage-pull-through/); [National Mortgage News, 20 Oct 2025](https://www.nationalmortgagenews.com/news/mba-says-productivity-origination-pull-through-is-falling))

**Implication:** Keep M-FAL-01 as a **start-month cohort**, not a same-period closings/apps ratio. The PGR ratio is a different clock (period mix). Label both if leadership wants a PGR-comparable tile. 69% IMB retail is a **sanity band**, not a target. Our 71% sample on the wireframe is in-family.

---

## Cycle time and Channel clocks

**MBA Wholesale Lending Survey, Q1 2025** ([MBA Newslink, 30 Jun 2025](https://newslink.mba.org/mba-newslinks/2025/june/mba-newslink-tuesday-july-1-2025/chart-of-the-week-average-turn-times-for-the-broker-wholesale-non-delegated-correspondent-production-channels-in-q1-2025/)):

| Channel | Clock (their definition) | Average | 20th pct (faster) | 80th pct |
|---------|--------------------------|---------|-------------------|----------|
| Broker wholesale | Application (RESPA six pieces) to **closing** (calendar days; closing ≠ funding) | **33.8 days** | ≤ 30.6 | ≥ 36.0 |
| Non-delegated correspondent | **Registration to funding** | **39.0 days** | ≤ 33.3 | ≥ 46.0 |

Broker channel 8.7 days faster than the Q3 2021 high (42.5). Non-del dispersion is wide (~13 days 20th-to-80th).

**ICE:** purchase close time **36.8 days** in March 2026 (fastest since ICE began tracking in 2019); all origination types **38.2 days**; typical purchase **11 days application → lock**, **26 days lock → close**. 2021 ICE OIR prints showed **49–58 days**. ([Real Cost Report citing ICE Mortgage Monitor May 2026](https://www.realcostreport.com/mortgage/mortgage-process/closing-timeline/); historical OIR e.g. [April 2021 PDF](https://static.elliemae.com/pdf/origination-insight-reports/ICE_OIR_APR2021.pdf))

**The Mortgage Collaborative Insights, Feb 2026:** member **app-to-CTC 34.8 days** (flat); best **19–23**, laggards **56–64**; funded loans per FTE **1.92**. Industry cost-to-originate still **> $11,000**. (TMC Insights PDF, Feb 2026.)

**STRATMOR (2018 PGR, still the public FTE grain):** Retail processors **9.4 loans/month/FTE**; consumer-direct **10.8** but CD pull-through **50.8%** vs Retail **71.6%** — CD processors spend more time on files that never close. Retail UW **19.2 loans/month/FTE**. ([STRATMOR, 2019](https://www.stratmorgroup.com/how-productive-is-your-origination-team/))

**Implication:**

- Keep **two EXE clocks**. MBA itself uses different definitions by Channel (app-to-close vs registration-to-funding). Averaging them is the anti-pattern we already banned.
- ICE “days to close” is **application → closing**, often **calendar**, and **closing ≠ Funded**. Map to M-CYC-03 only with a footnote (our clock is File start → Funded, business days).
- Wholesale 33.8 **calendar** days app-to-**close** is in the same neighborhood as our 25–28 **business-day** start-to-fund ASSUMED band if you convert (~20–25 bd). Do not paste 33.8 onto M-CYC-03 unlabeled.
- P14 units/FTE: STRATMOR processor ~9.4/month is a **monthly** grain; our weekly M-CAP-01 must not be compared raw (9.4/month ≈ 2.2/week). TMC 1.92 funded/FTE looks like a different FTE definition (all staff vs role). **Never mix those denominators.**

---

## TRID: two business-day definitions

Regulation Z, [12 CFR 1026.2(a)(6)](https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-A/section-1026.2):

1. **General business day** (default): a day the creditor’s offices are open to the public for substantially all business functions.
2. **Specific business day**: all calendar days **except Sundays and listed federal holidays**.

**Initial Loan Estimate send** — § 1026.19(e)(1)(iii)(A): deliver or mail no later than the **third general business day** after application (six pieces: name, income, SSN, property address, estimate of value, loan amount). CFPB KBYO guide § 6.14. ([CFPB small-entity guide v4](https://files.consumerfinance.gov/f/documents/kbyo_smallentitycomplianceguide_v4_10072016.pdf))

**Mailed LE deemed received** and **Closing Disclosure waiting period** use the **specific** definition (Saturdays count; Sundays/federal holidays do not).

**Pack was wrong** to call initial LE a **calendar-day** clock (weekends always count). Correct rule: **creditor-open days**. If the company is closed Saturday, Saturday does not count toward the 3-day **send** clock.

**Implication:** M-CYC-04 and M-REG-01 must use the company’s **general business-day calendar**, not “all calendar days.” CD timing on P08 uses **specific business days**. Keep them on different tiles. Application = six RESPA pieces, which is why E-TRID-APP can differ from LOS “application date.”

---

## Appraisal, waivers, ROV

Fannie Mae **Value Acceptance** (appraisal waiver): DU offer; no appraisal if exercised; SFC 801 at delivery; offer not more than four months old at note date. Alternatives include Value Acceptance + Property Data (SFC 774) and hybrid appraisal. ([Fannie Value Acceptance](https://singlefamily.fanniemae.com/property-valuation/value-acceptance); Selling Guide B4-1.4-10)

Industry summaries: traditional appraisal often **5–10 business days**; waivers cited as **7–10 days** shorter close and **$500–$700** borrower savings; UPD/property-data collection often **2–3 days**. ([HousingWire, 29 Oct 2024](https://www.housingwire.com/articles/property-data-collection-based-appraisal-waivers-upd-and-the-future-of-appraisals/)) AMC marketing (not a benchmark): ~5 business-day average; rural longer. AIR/Dodd-Frank: production staff must not pick the appraiser.

Fannie **Reconsideration of Value**: lender must have borrower-initiated ROV procedures; complete appraisal review before ROV; designate UW or appraisal SME; max five additional comps; defined turn-time in the appraiser communication; AIR-aligned. ([Selling Guide B4-1.3-12](https://selling-guide.fanniemae.com/sel/b4-1.3-12/appraisal-quality-matters))

**Implication:** P03 waiver path (M-VOL-15, exclude from M-CYC-08) matches Value Acceptance / ACE. ROV is a **required process**, not a nice-to-have exception — keep M-QLT-05. Do not use AMC “5 days” as company SLA; keep ASSUMED 7 bd until Q1.

---

## Correspondent / TPO

MBA Wholesale Survey treats **non-delegated correspondent** as registration → **funding**, with much wider lender dispersion than broker wholesale (see cycle table). ICE TPO Connect (vendor): claims ~498 minutes saved per acquired loan and ~1 day faster funding cycle — **vendor ROI, not a benchmark**. ([ICE datasheet](https://mortgagetech.ice.com/publicdocs/mortgage/datasheet-tpo-connect-correspondent-lenders.pdf))

Example investor scorecard (The Money Source, seller version): **lock-to-purchase** and **deliver-to-purchase** days, FICO mix vs peers, geographic mix, **top conditions by loan type**. ([TMS scorecard guide PDF](https://kiss.themoneysource.com/docs/Correspondent_Lender_Scorecard_Guide_Seller_Version.pdf))

PennyMac public comments distinguish **delegated correspondent** vs **TPO/broker** vs consumer-direct — three factories, not one “TPO” tile. ([NMN / Digital Mortgage 2025](https://www.nationalmortgagenews.com/video/digital-mortgage-2025/an-interview-with-pennymac-tpo-chief-kim-nichols))

**Implication:** Our P09 “Correspondent” is the **purchase** factory. If the company has **delegated vs non-delegated**, add that as a dimension on P09 (not a 16th subcategory until volume justifies it). TPO scorecards should include lock-to-purchase **and** defect/kickout — we already have both. Do not use ICE’s “funding cycle” wording for Correspondent purchase.

---

## Manufacturing quality and GSE QC

**ACES Q4 2025 / CY 2025 QC Industry Trends** (post-close critical defects, net): Q4 2025 **1.38%** (down from 1.79% in Q3); CY 2025 average **1.50%** vs CY 2024 **1.52%**. Legal/Regulatory/Compliance led Q4 2025 (24.66% of defects). Income/Employment 21.52%. FHA defect share **30.86%** vs review share (elevated). Refinance defect share **32.20%** of defects vs 21.04% of reviews. 2021–22 range was **1.84%–2.70%**. ([ACES Q4 2025 PDF](https://www.acesquality.com/uploads/reports/Q4_2025_ACES_Mortgage_QC_Industry_Trends.pdf); [PROGRESS in Lending, 20 May 2026](https://mymortgagemindset.com/aces-report-shows-critical-defect-rate-falls-to-annual-low/))

**Fannie Mae Selling Guide D1-2-01** (04/01/2026): written **prefunding QC** plan; reviews **prior to closing** or, for delegated third-party acquisitions, **prior to acquisition**; independent of production if practical; sample from **each production channel**. Fannie materials state a **minimum prefunding sample of 10% of prior month originated/closed/acquired or 750 loans** (lesser), with a government-correspondent exclusion when the TPO underwrote and obtained the government insurance/guarantee. ([D1-2-01](https://selling-guide.fanniemae.com/sel/d1-2-01/lender-prefunding-quality-control-review-process); [Fannie PFQC worksheet](https://www.fanniemae.com/content/tool/qc-self-assessment-worksheet.pdf))

Use the **same defect taxonomy** for prefunding and post-close (Fannie QC best-practice).

**Implication:** P12 coverage tile is not optional for a GSE seller. 10% (or 750) is a **floor**, targeted not only random. Correspondent **pre-purchase** QC is the “prior to acquisition” path — keep M-QLT-09 separate from Retail pre-fund M-QLT-07. ACES ~1.5% critical is a **post-close industry print**, not a P12 target; still useful as a sanity band (our wireframe 1.8% is in-family). Slice FHA and refi on P12.

---

## Investor delivery

ULDD is the GSE common delivery dataset (Phase 5 specs on Fannie’s site). Loan Delivery is the submission app (edits, DU-to-delivery compare, certification status). Whole-loan purchase proceeds: clean delivery data by **9:00 p.m. ET**, custodian complete package **first-morning delivery next day**, then status **Purchased and Funded**. Late data → next business day. ([Fannie C1-2](https://selling-guide.fanniemae.com/sel/c1-2/loan-delivery-overview); [C2-2-04](https://selling-guide.fanniemae.com/sel/c2-2-04/timing-distribution-whole-loan-purchase-proceeds); [ULDD](https://singlefamily.fanniemae.com/delivering/uniform-mortgage-data-program/uniform-loan-delivery-dataset))

MBA Chart (MBFRF, ~500 IMBs): repurchase/indemnification UPB vs new originations averaged **0.07% (2018–21)** vs **0.22% (2022–23)**. ([MBA Newslink, 4 Mar 2024](https://newslink.mba.org/servicing-newslink/2024/march/mba-newslink-friday-may-9-2022/mba-chart-of-the-week-imb-average-upb-of-repurchased-indemnified-loans/))

**Implication:** P11 must keep **Delivered ≠ Investor purchased**. Fannie’s “Purchased and Funded” is **investor** purchase — never M-VOL-06. Kickout/suspense aging (M-AGE-09) is the operational cousin of repurchase risk; repurchase $ is Finance/QC, not an EXE tile.

---

## What this does **not** change

- Channel as a required filter.
- Correspondent purchase ≠ Funded.
- p50 and p90, not average-only.
- Manufacturing QC ≠ independent audit.
- Lock desk out of Operations process metrics.

## Follow-on source work (when someone has MBA login)

1. Pull the latest **MBA Quarterly Performance Report** pull-through and loans-closed-per-fulfillment-FTE (role grain).
2. Pull **Wholesale Lending Survey** latest broker vs non-del turn and pull-through.
3. Subscribe or request **ACES** quarterly PDF for defect mix vs our KIK-/QC categories.
4. Confirm the company’s TRID **general business-day** calendar (Saturday open or not) for M-CYC-04.
