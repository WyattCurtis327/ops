# Operating context

## Overview

The rest of this pack says *what* to measure. This document is the *situation* those measures sit in: how a non-bank mortgage Operations group typically runs, which systems stamp which events, how a file is counted on each Channel, and which neighboring teams hand work in or out.

Company-specific names (LOS, fulfillment center, SLA policy) are still unknown. Where this file states a default, it is labeled **ASSUMED**. Replace those with local fact; do not silently invent a different operating model in a dashboard.

Related: [glossary](../CONTEXT.md), [scope](01-scope-and-taxonomy.md), [events](06-event-dictionary.md), [open questions](08-phasing-and-open-questions.md).

## Why this context is required

Without it, BI will ship a “funded” tile that mixes three different cash events, a cycle time that averages unlike clocks, and a Correspondent team staring at Retail closing funnels.

The reporting product exists because Operations currently answers “are we on time?” from **ASSUMED** current state:

- A LOS pipeline screen that does not match Finance’s funded count.
- A huddle spreadsheet with aging but no Waiting-on party.
- Correspondent purchases labeled funded.
- Cycle time as an average of completed files only, hiding the stuck tail.
- Vendor portals that do not join cleanly to the Loan file.

If leadership says that current state is wrong, update this section first; the metric catalog stays.

## Operating model (ASSUMED)

- **Creditor:** The company is the creditor on Retail and Wholesale. On Correspondent, the TPO was the creditor; the company becomes investor/aggregator after Correspondent purchase.
- **Fulfillment:** Centralized manufacturing (pods/teams), not in-branch processing. Branch and LO are dimensions, not the queue owner.
- **Lock desk:** Capital Markets. Operations consumes Lock status and lock-expiration risk.
- **Secondary:** Capital Markets assigns investor/commitment. Operations executes delivery.
- **Quality:** Manufacturing QC sits in Operations. Independent audit QC is a different subject area.
- **Servicing:** In-house or subservicer — unknown. Operations ends at Investor purchase plus a complete boarding package; it does not own delinquency.

Channel mix, unit volume, and whether Wholesale is a large share are unknown. **Channel remains a required filter** even if one channel is 90% of units.

## Decision cadence

| Cadence | Owner | Wireframe | Question |
|---------|-------|-----------|----------|
| Daily huddle (morning, after 6:00 a.m. As-of) | Desk leads | P15, then the desk | What is stuck, who are we waiting on, what must move today? |
| Weekly Ops | COO / Ops VP | EXE (D01) | Did we convert, did cycle/SLA/kickouts move, is capacity matching arrivals? |
| Weekly channel | Correspondent ops; Retail/Wholesale ops | P09 vs P08 | Purchase vs Funded — never one unlabeled number |
| Monthly | Vendor mgmt, QC, workforce | P13, P12, P14 | Panel, defect themes, FTE vs queue |

The LOS is the system of action in every meeting. Dashboards select; they do not replace the queue.

## Systems landscape (generic)

No table names. This is which **system class** is the system of record for which events. Map to real products in a later data-discovery job.

| System class | Owns | Events (examples) | Used on |
|--------------|------|-------------------|---------|
| LOS | Loan file, Milestone, conditions, CTC, Funded, assignments | E-START, E-UW-FIRST, E-CTC, E-FUNDED, E-WAIT | Almost every metric |
| eSign / disclosure | LE/CD send and sign | E-LE-INIT, E-LE-SIGN, E-REDISC | P01 |
| AUS (DU/LP or equivalent) | Recommendation, not the UW decision | E-AUS | Dimension on P06 |
| AMC / appraisal portal | Orders, report in, ROV | E-APPR-ORD, E-APPR-RCV, E-ROV | P03, P13 |
| Title / closing platform | Commitment, CD figures, docs out, signed | E-TTL-*, E-DOCS-OUT, E-SIGNED | P04, P08 |
| Flood / credit / tax vendors | Order cycle | E-FLOOD, credit orders | P05, P13 |
| MI portal | Apply and cert | E-MI-APP, E-MI-CERT | P05, P06 |
| TPO portal | Registration, Submission, TPO conditions | E-SUB, Corr File start | P09 |
| Wire / treasury | Wire success/fail | E-FUND-ATT, E-FUND-FAIL, Corr purchase wire | P08, P09 |
| Imaging | Trailing document in | E-TRAIL-IN | P10 |
| Shipping / investor portal | Delivered, suspense, purchase advice, Kickout | E-DELIVERED, E-KICKOUT, E-INV-PURCH | P11 |
| QC module | Reviews and defects | E-QC-*, E-DEFECT | P12 |
| Roster / HRIS | Productive FTE | Daily FTE | P14 |
| Capital Markets (lock/commitment) | Lock and investor assignment | Lock status at As-of | Dimension only |

If a class has no feed, the KPIs that need its events render **unavailable**, not zero.

## Worked files (how counting actually works)

Sample IDs. Not company data. Use these when arguing a metric definition.

### Retail — purchase, conventional

1. Application taken **Tue** → File start **Tue** (E-START, E-APP). M-VOL-01 and M-VOL-02 +1.
2. Initial LE sent **Thu** (2 general business days after a Tuesday application, if Wed–Thu are open). Counts toward M-CYC-04; not an M-REG-01 miss.
3. Intent to proceed **Fri**. Appraisal ordered next business day.
4. Submitted to UW day 6. First decision **approve with conditions** same day. M-VOL-04 +1; not Suspense.
5. CTC day 18. M-VOL-05 +1. Start-to-CTC clock stops (M-CYC-01).
6. Funded day 22. M-VOL-06 +1, M-VOL-16 +1. **Leaves Pipeline.** Enters Post-close WIP.
7. Delivered day 30. M-VOL-11 +1. Leaves Post-close WIP.
8. Investor purchase day 34. M-VOL-12 +1.

This file **never** increments M-VOL-08/09 or M-FAL-03.

### Wholesale — rate/term refinance, Broker-ordered appraisal

1. File start = **registration complete**, not “application taken by the company.” M-VOL-01 +1. M-VOL-02 +1 only if an application event exists on the file.
2. LE: company issues if it is the creditor (usual). Clock is TRID general business days (P01).
3. Appraisal path = Broker-ordered. **No E-APPR-ORD.** M-CYC-08 uses received-in → report, labeled received-to-report. Do not drop the file from Vendor on-time if there is no company SLA clock — exclude or label.
4. Waiting-on party is often **Broker**, not borrower. Aging without that slice will blame Processing.
5. Funded is still company Funded (M-VOL-06). Closing may occur at the Broker’s title company; the Funded event is still the company’s wire.

### Correspondent — FHA, TPO already closed

1. Intake Monday = File start. **Not** an Application. M-VOL-01 +1. M-VOL-02 **does not** increment.
2. Submission complete Wednesday. M-VOL-08 +1. Purchase cycle starts (M-CYC-11).
3. Pre-purchase QC fail → conditions to TPO. Waiting-on = TPO. Not Suspense in the Retail sense if the decision was “conditions to purchase.”
4. Purchase approved Friday (M-VOL-05C). **Not** CTC (M-VOL-05).
5. Wire Monday = Correspondent purchase. M-VOL-09 +1, M-VOL-16 +1. **Not** M-VOL-06 Funded.
6. Trailing docs from TPO (P10). Then Delivered and Investor purchase (P11) like any other channel.

If this file appears in a Funded tile, the dashboard is wrong.

## Handoff contracts

Minimum fields the other subject area must supply or consume. Not a schema.

**Sales → Operations (at File start)**  
Loan file ID, Channel, product, purpose, property state, LO or Broker, application datetime (R/W). Not lead source, not CPL.

**Operations ↔ Capital Markets**  
Ops reads: Lock status, lock expiration, investor/commitment when assigned.  
Ops does not write: lock price, note rate, gain-on-sale.  
Ops writes: CTC/Funded/purchase dates that CM uses for pull-through — those remain Operations metrics.

**Operations → Servicing**  
After Funded or Correspondent purchase: first-payment date, MERS MIN if used, completed trailing stack or a documented exception. Servicing boarding SLA is not an Operations headline.

**Operations → Finance**  
Event-dated Funded units/volume (R/W) and Correspondent purchased units/volume, separately and as M-VOL-16 with that exact label. Finance P&L is out of scope; unit recon is in scope.

**Operations → independent Quality**  
Sample frame and file IDs. Audit defect rates do not land on P12 unless dual-tagged.

## Regulatory and investor context that changes clocks

| Rule | Effect on this pack |
|------|---------------------|
| TRID initial LE (3 general business days) | P01 / M-CYC-04 / M-REG-01. Creditor-open days. Saturday counts only if offices are open. CD wait uses specific business days. |
| TRID CD timing | Operational on P08; not a second compliance system of record in v1. |
| Appraisal independence / HPML second appraisal | Second appraisal is an exception path on P03, not a separate dashboard. |
| AUS is not an UW decision | E-AUS is a dimension; E-UW-FIRST is the measure. |
| ULDD / investor delivery | P11. Kickout reasons should be mapped to a short list, not free text only. |
| MERS | Stack completeness on P10, not a servicing KPI. |
| MI required by product/LTV | M-CYC-16A denominator is MI-required files only. |

## Who owns a number

| Role | Owns definition | Consumes |
|------|-----------------|----------|
| Ops VP | EXE headlines, pull-through, SLA-breach | Weekly Ops |
| Desk manager (P01–P11) | That desk’s turn times and queues | Daily huddle |
| Correspondent ops | M-VOL-08/09/10, M-FAL-03, TPO scorecard | P09 |
| Manufacturing QC | File-fail rates, severity taxonomy | P12 |
| Vendor management | On-time %, concentration | P13 |
| Workforce planner | FTE productive definition | P14 |
| BI | Event mapping, grain integrity | Catalog |
| Capital Markets | Lock and commitment dimensions | Not lock-desk KPIs |
| Finance | Optional M-VEN-05; recon to M-VOL-06/09 | Not P&L tiles |

If two owners disagree, the [catalog](04-metric-catalog.md) wins until an ADR changes it. Do not “fix” a tile in the dashboard SQL.

## What “healthy” looks like (qualitative)

Until [Q1](08-phasing-and-open-questions.md) replaces ASSUMED SLA:

- Pipeline is not growing while SLA-breach % and p90 rise together (capacity).
- Pull-through is stable by cohort month, not juiced by counting only easy files.
- Correspondent purchase cycle and Retail start-to-fund are both in view, never averaged.
- Kickouts are explained by a reason mix that QC already saw internally — or QC sampling is too light (coverage tile).
- Waiting-on internal is the minority of aged files. If it is the majority, the desk owns the miss.

## Context still missing from the company

Do not block the MVP on these, but do not pretend they are known:

1. Real LOS, AMC, title, TPO portal, and shipping product names (systems table above).
2. Official File start milestone per Channel (Q3).
3. Whether fulfillment is truly centralized (changes team dimension).
4. Typical Channel mix and whether Correspondent is material.
5. In-house vs subservicer (boarding handoff).
6. Investor mix (GSE vs whole loan vs private) — Kickout reason lists differ.
7. Productive FTE source (Q9).

Workshop those with the five questions already listed in the phasing doc (Q1, Q3, Q4, Q6, Q9).
