# Processes by subcategory

## Overview

Each subcategory below is a manufacturing process (or a control process) inside Operations. Metrics IDs refer to the [metric catalog](04-metric-catalog.md). Dashboard IDs refer to the [inventory](05-dashboard-inventory.md).

Channel variants are required on P01–P11. Correspondent does not “skip” manufacturing; it manufactures a **purchase**, not an origination closing.

`ASSUMED SLA` values are industry-typical placeholders, not company policy. TRID initial LE **send** timing is regulatory (**general business days**, creditor-open), not assumed. CD waiting period uses TRID **specific business days**.

---

## P01 Disclosure and file setup

### Purpose

Open a Loan file in Operations and, for Retail and Wholesale, issue the initial Loan Estimate and capture intent to proceed. This process creates the File start event every volume and pull-through metric depends on.

### In / out of scope

In: file creation, TRID application date, initial LE, redisclosure, intent to proceed, eSign of origination disclosures, Wholesale registration, Correspondent intake completeness.

Out: lock desk pricing, Sales lead capture, Closing Disclosure timing (P08), TPO’s own TRID (already occurred).

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Company takes the application (six RESPA pieces), sets TRID application date, issues LE within 3 general business days, captures intent to proceed, starts the file. |
| Wholesale | Broker takes the application. If the company is the creditor, the company issues the LE. File start is registration complete, not “application taken” by the company. Redisclosure is coordinated with the Broker. |
| Correspondent | No company LE. File start is intake/registration. Work is eligibility and closed-loan package completeness, not borrower disclosure. |

### Actors

Disclosure specialist, setup processor, Broker (Wholesale), TPO ops contact (Correspondent), compliance support (policy, not the dashboard owner).

### Trigger, inputs, outputs

Trigger: Retail application received; Wholesale registration package received; Correspondent intake request.

Inputs: application or registration data, AUS if run at origination, fee worksheet, product/program.

Outputs: Loan file ID, File start timestamp, initial LE sent timestamp (R/W), intent-to-proceed timestamp (R/W), intake-complete timestamp (Corr).

### Happy path

1. Receive application (Retail), registration (Wholesale), or intake (Correspondent).
2. Create the Loan file in the LOS; stamp File start when setup/registration/intake is complete.
3. Retail/Wholesale: determine TRID application date (six pieces); issue initial LE within 3 general business days; send for eSign.
4. Retail/Wholesale: capture intent to proceed before ordering most settlement services.
5. Hand the file to Processing (P02) or, for Correspondent, to pre-purchase review (P09).

### Exception paths

- Redisclosure on fee, rate, product, or settlement-service change (M-QLT-04).
- eSign incomplete; waiting-on party = borrower or Broker.
- Changed circumstance vs. tolerance cure.
- Correspondent package rejected at intake (Fallout reason: rejected) — never labeled “denied credit.”

### Systems of record

LOS (file, milestones, disclosure events); eSign vendor; fee engine. Correspondent TPO portal for intake.

### Timestamps / events

File start; TRID application date; initial LE sent; LE signed; intent to proceed; redisclosure issued; intake complete; intake rejected.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Application (TRID six pieces) to initial LE sent | 3 general business days (creditor-open) | Regulatory, not assumed |
| File start (setup complete) from application/registration received | 1 business day | ASSUMED SLA |
| Correspondent intake complete from package received | 1 business day | ASSUMED SLA |

### Metrics produced

M-VOL-01, M-VOL-02, M-CYC-04, M-REG-01, M-QLT-04, M-AGE-01 (setup milestone).

### Reporting questions

- What share of Retail/Wholesale files missed the 3-general-business-day LE send clock this week?
- How many files are waiting on eSign, by Channel?
- What is File start volume versus last week, by Channel and product?

### Data-quality risks

Backdated File start; TRID application date not equal to LOS application date; Wholesale files counted as Applications taken by the company; Correspondent intake counted as Applications taken; redisclosure events not distinguished from initial LE.

**Dashboards:** [D14](dashboards/D14-disclosures-and-setup.md), [D01](dashboards/D01-ops-command-center.md) (starts), [D02](dashboards/D02-pipeline-and-aging.md).

---

## P02 Processing

### Purpose

Collect a decisionable package: credit, income, assets, third-party orders, AUS, HOA/condo, and a complete submission to underwriting. Processing is the primary owner of Waiting-on party while the file is pre-UW and again while conditions are outstanding (shared with P07).

### In / out of scope

In: document collection, credit pull, VOE/VOI/VOA, tax transcripts, AUS runs, HOA/condo, fraud/SSA alerts routing, package-to-UW, chase.

Out: the underwriting decision (P06), appraisal review decision (P03), CTC (P07).

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Processor collects from the borrower and LO; company orders most third parties after intent to proceed. |
| Wholesale | Split collection with the Broker. Processor may chase the Broker rather than the borrower. Appraisal/title may already be ordered by the Broker. |
| Correspondent | Not borrower-facing. Processor/analyst checks seller package completeness and issues conditions to the TPO (P09). |

### Actors

Processor, processing team lead, LO (Retail), Broker processor (Wholesale), TPO (Correspondent).

### Trigger, inputs, outputs

Trigger: File start complete (or Correspondent intake complete).

Inputs: application/package, credit, AUS, third-party order status.

Outputs: submitted-to-UW timestamp (R/W); package-complete timestamp; Waiting-on party current value.

### Happy path

1. Assign processor and team.
2. Run or refresh credit and AUS.
3. Order or confirm appraisal, title, flood, insurance (P03–P05).
4. Collect income, assets, HOA/condo, and program-specific docs.
5. Mark processing complete and submit to underwriting (R/W) or to pre-purchase review (Corr).

### Exception paths

- Waiting-on borrower, Broker/TPO, Vendor, or internal — must be stamped, not inferred only from milestone age.
- Self-employed / tax-transcript delay.
- Condo/project ineligible; HOA questionnaire late.
- File returned from UW as Suspense (Rework into processing).

### Systems of record

LOS; credit vendor; AUS; HOA/condo tools; document imaging.

### Timestamps / events

Processor assigned; processing complete / submitted to UW; each Waiting-on party change; document received; AUS run.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| File start to submitted to UW (complete package) | 5 business days | ASSUMED SLA |
| Waiting-on borrower/Broker chase cycle | 2 business days between touches | ASSUMED SLA |

### Metrics produced

M-CYC-05, M-AGE-01–05, M-CAP-01 (processor), M-QLT-03 (rework into processing).

### Reporting questions

- How many files are in processing, by age band and Waiting-on party?
- What is p50/p90 File start to UW submit, by Channel and team?
- Which processors are above queue-depth per FTE?

### Data-quality risks

Milestone left in processing after UW submit; Waiting-on party blank; Wholesale waiting-on Broker coded as borrower; Correspondent package review mixed into Retail processing queues.

**Dashboards:** [D03](dashboards/D03-processing.md), [D02](dashboards/D02-pipeline-and-aging.md), [D13](dashboards/D13-capacity-and-productivity.md).

---

## P03 Appraisal and valuation

### Purpose

Establish a supportable value, or a valid waiver, in time for underwriting and CTC. This is an order-grain process that rolls up to the Loan file.

### In / out of scope

In: waiver decision (PIW/ACE or equivalent), order, assignment, inspection, report in, appraisal review, ROV, second appraisal, transfer of appraisal (Wholesale/Correspondent).

Out: AMC contracting (P13), CU/LCA risk as Capital Markets/credit policy except as a review flag.

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Company orders after intent to proceed unless waived. |
| Wholesale | Broker-ordered or lender-ordered. Transfer of appraisal is common. Both paths must be visible. |
| Correspondent | Seller appraisal already exists. Work is review, transfer eligibility, and defect — rarely a new order. |

### Actors

Appraisal desk, AMC, appraiser, underwriter (review), processor.

### Trigger, inputs, outputs

Trigger: intent to proceed (R/W) or package in (Corr); or waiver eligible.

Inputs: property data, product, AUS waiver eligibility, prior appraisal if transfer.

Outputs: waiver used (yes/no); order placed; report in; reviewed; value accepted; ROV opened/closed.

### Happy path

1. Test waiver eligibility; if waived, stamp waiver and skip order.
2. Place order with AMC or staff appraiser; capture order datetime.
3. Inspection scheduled and completed.
4. Report in; desk or UW review.
5. Accept value; file can CTC from a valuation standpoint.

### Exception paths

- ROV (M-QLT-05).
- Second appraisal (jumbo, ROV unresolved, or program rule).
- Transfer rejected; new order.
- Appraiser revision without formal ROV (count as revision in Vendor metrics).
- Rural assignment delay; dual-track with UW on other conditions.

### Systems of record

AMC portal; LOS appraisal fields; CU/collateral tools as supporting.

### Timestamps / events

Waiver decision; order placed; accepted by appraiser; inspection; report in; review complete; ROV submitted; ROV resolved; second order.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Order to report in | 7 business days | ASSUMED SLA |
| Report in to review complete | 1 business day | ASSUMED SLA |
| ROV open to resolved | 5 business days | ASSUMED SLA |
| Correspondent appraisal review | 1 business day from package in | ASSUMED SLA |

### Metrics produced

M-CYC-08, M-CYC-08A (order to reviewed), M-VOL-15 (waiver rate), M-QLT-05, M-VEN-01–04 (AMC).

### Reporting questions

- What is p50/p90 order-to-report by AMC, state, and property type?
- What share of files used a waiver, by Channel and product?
- Which AMCs have high revision or ROV rates?

### Data-quality risks

Order date missing when ordered outside LOS; Broker-ordered appraisals with no company order timestamp (use received-in date and label it); waiver files included in order-to-report (exclude); Correspondent reviews counted as new orders.

**Dashboards:** [D04](dashboards/D04-appraisal-and-valuation.md), [D12](dashboards/D12-vendor-performance.md).

---

## P04 Title, escrow, and curative

### Purpose

Produce a clear title path to close (Retail/Wholesale) or a purchasable title package (Correspondent), including payoffs, taxes, HOA, and Closing Disclosure figures.

### In / out of scope

In: title order, search, commitment, curative, payoffs, tax/HOA, CD number collaboration, wet vs hybrid vs eClose coordination.

Out: recording after funding (P10), independent legal opinions except as curative.

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Company (or its closer) orders title/escrow. |
| Wholesale | Often title/escrow already opened by Broker or borrower; company reviews and coordinates CD. |
| Correspondent | Title and closing already happened. Review commitment, policy, and curative before purchase. |

### Actors

Title desk, closer, title/escrow company, HOA, processor.

### Trigger, inputs, outputs

Trigger: intent to proceed (R/W) or package in (Corr).

Outputs: order placed; commitment in; curative cleared; CD figures ready; clear-to-close from title.

### Happy path

1. Order or confirm title/escrow.
2. Receive commitment; inventory exceptions.
3. Curative: liens, judgments, name/vesting, survey if required.
4. Collect payoffs, taxes, HOA estoppel.
5. Deliver figures for CD; confirm closing type (wet/hybrid/eClose).

### Exception paths

- Curative that threatens CTC (M-QLT-06).
- Late HOA estoppel.
- Payoff expirations requiring redisclosure (feeds P01/P08).
- eClose not eligible; fall back to wet.

### Systems of record

Title portal; LOS; closing platform.

### Timestamps / events

Order; commitment in; curative opened/cleared; payoff received; HOA received; CD figures delivered; closing type selected.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Order to commitment in | 5 business days | ASSUMED SLA |
| Commitment in to curative clear (no exceptional liens) | 5 business days | ASSUMED SLA |
| Correspondent title-package review | 1 business day | ASSUMED SLA |

### Metrics produced

M-CYC-09, M-CYC-09A (commitment to clear), M-QLT-06, M-VEN-* (title).

### Reporting questions

- Which title companies miss commitment SLA by state?
- What share of files have open curative past SLA?
- How many CTCs are blocked on title versus appraisal versus UW conditions?

### Data-quality risks

No order date on Broker-opened title; curative never closed in LOS; CD timing attributed to title when the delay is UW.

**Dashboards:** [D05](dashboards/D05-title-escrow-closing-coord.md), [D12](dashboards/D12-vendor-performance.md).

---

## P05 Insurance and MI

### Purpose

Confirm hazard (and flood) coverage acceptable to the investor, and obtain mortgage insurance when the product requires it. This process has no dedicated dashboard; its KPIs sit on D03, D05, and D06.

### In / out of scope

In: HOI binder, mortgagee clause, flood determination, flood insurance, condo master policy, MI application and certificate, MI UW conditions.

Out: Force-placed insurance after boarding (Servicing); MI pricing as a Capital Markets/product topic except as “MI cert in.”

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Processor orders flood, collects HOI, applies for MI. |
| Wholesale | Broker often collects HOI; company still must accept it and obtain MI if needed. |
| Correspondent | Confirm coverage and transferable MI on the closed loan. |

### Actors

Processor, MI desk/underwriter, flood vendor, insurance carriers.

### Trigger, inputs, outputs

Trigger: intent to proceed or UW requires MI; Correspondent package in.

Outputs: flood determination; HOI accepted; MI cert in.

### Happy path

1. Flood determination.
2. Collect and accept HOI (or master policy).
3. If MI required: apply, satisfy MI UW, receive cert.
4. Stamp insurance/MI complete for CTC.

### Exception paths

- High-cost flood; insufficient coverage; condo master gaps.
- MI refer/ineligible; extra conditions (feeds P07).
- Correspondent MI not transferable.

### Systems of record

Flood vendor; LOS insurance screens; MI portal.

### Timestamps / events

Flood ordered/received; HOI received/accepted; MI applied; MI cert in.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Flood determination | 1 business day | ASSUMED SLA |
| HOI accepted from first request | 5 business days | ASSUMED SLA |
| MI apply to cert (standard) | 3 business days | ASSUMED SLA |

### Metrics produced

M-CYC-16 (HOI accept), M-CYC-16A (MI cert), M-AGE-05 when waiting-on is insurance.

### Reporting questions

- How many files are CTC-blocked on HOI or MI cert?
- What is MI cert turn by MI company?

### Data-quality risks

Flood determination not stored as an order; HOI “received” vs “accepted”; Correspondent confirmations mixed with new MI applications.

**Dashboards:** D03, D05, D06 (no D15). Department wireframe: [P05](wireframes/index.html#P05).

---

## P06 Underwriting

### Purpose

Issue the first credit decision on a Retail/Wholesale file, or an eligibility/pre-purchase decision on a Correspondent file. Decision includes approve-with-conditions, Suspense, or deny.

### In / out of scope

In: AUS plus overlays, manual UW, exceptions, MI UW coordination, first decision, subsequent decisions after Suspense.

Out: CTC stamp (P07), lock exceptions (Capital Markets), independent audit QC (Quality).

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Full origination UW. |
| Wholesale | Same credit decision; overlays may treat Broker-originated files differently — still one metric, sliced by Channel. |
| Correspondent | Eligibility and pre-purchase UW, not origination CTC. Outcome is purchase-eligible, conditions-to-TPO, or reject. |

### Actors

Underwriter, UW manager, MI underwriter, exception authority.

### Trigger, inputs, outputs

Trigger: submitted to UW (R/W) or Submission complete (Corr).

Outputs: first decision timestamp and outcome; exception flag.

### Happy path

1. Queue assignment (auto or manager).
2. AUS plus overlay review; collateral and title status checked.
3. Decision: approve with conditions, or deny.
4. Issue conditions into P07 (R/W) or TPO conditions (Corr).

### Exception paths

- Suspense (M-QLT-02) — file returns toward processing completeness.
- Exception/overlay grant or deny.
- CTC later revoked (M-QLT-14) — counted in P07 but caused here or in P08.

### Systems of record

LOS UW screens; AUS; exception log.

### Timestamps / events

Submitted to UW; UW assigned; first decision; subsequent decision; exception requested/granted.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Submitted to first decision | 1 business day (p50), 2 business days (p90) | ASSUMED SLA |
| Correspondent pre-purchase decision | 2 business days from Submission | ASSUMED SLA |

### Metrics produced

M-VOL-04, M-CYC-06, M-QLT-02, M-CAP-01 (underwriter).

### Reporting questions

- What is UW turn p50/p90 by team and Channel?
- What is first-decision Suspense rate, and is it rising for a product or TPO?
- Units decisioned per UW FTE versus arrivals?

### Data-quality risks

First decision overwritten by later decision (need first-decision event); auto-AUS counted as UW decision; Correspondent reject counted as credit deny in Retail fallout.

**Dashboards:** [D06](dashboards/D06-underwriting-and-conditions.md), [D13](dashboards/D13-capacity-and-productivity.md), [D08](dashboards/D08-correspondent-operations.md) for Corr.

---

## P07 Conditions and Clear to Close

### Purpose

Clear PTD and PTF conditions and stamp Clear to Close (Retail/Wholesale) or approved-to-purchase (Correspondent). This is the control point between credit approval and closing or purchase.

### In / out of scope

In: condition inventory, condition Turn time, CTC, CTC revoke, rework loops.

Out: drawing docs (P08), purchase wire (P09).

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Processor collects; UW clears; CTC. |
| Wholesale | Many conditions wait on the Broker. Waiting-on party is critical. |
| Correspondent | Conditions to TPO; no CTC. Analog event is Purchase decision approved. |

### Actors

Processor, underwriter, Broker/TPO, closer (PTF).

### Trigger, inputs, outputs

Trigger: UW issues conditions.

Outputs: each condition cleared; CTC timestamp; purchase-approved timestamp (Corr).

### Happy path

1. Publish condition list (PTD vs PTF).
2. Collect evidence; UW (or designated clearer) accepts.
3. When PTD and valuation/title/insurance gates are green, stamp CTC (R/W) or purchase-approved (Corr).
4. PTF conditions continue into P08/P09.

### Exception paths

- Rework: new conditions after CTC (M-QLT-03, M-QLT-14).
- CTC revoke.
- Lock expiring before CTC (M-AGE-06) — operations risk, lock desk is Capital Markets.

### Systems of record

LOS condition records (one row per condition, with issue/clear timestamps).

### Timestamps / events

Condition issued; condition cleared; CTC; CTC revoke; purchase approved (Corr).

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Condition issued to cleared | 2 business days | ASSUMED SLA |
| Last PTD clear to CTC stamp | 0–1 business day | ASSUMED SLA |

### Metrics produced

M-VOL-05, M-CYC-01, M-CYC-07, M-CYC-07F, M-QLT-01, M-QLT-03, M-QLT-14, M-AGE-06, M-AGE-07. Correspondent analog of CTC volume is M-VOL-05C (owned by P09).

### Reporting questions

- Conditions per file (PTD vs PTF) by Channel and UW team?
- What share of CTCs were revoked?
- How many files are CTC but not scheduled (M-AGE-07)?

### Data-quality risks

Conditions without issue timestamps; PTD/PTF mis-tagged; CTC without a timestamp; multiple CTC stamps without revoke events; Correspondent purchase-approved labeled CTC.

**Dashboards:** [D06](dashboards/D06-underwriting-and-conditions.md), [D02](dashboards/D02-pipeline-and-aging.md).

---

## P08 Closing coordination and funding

### Purpose

For Retail and Wholesale only: schedule the closing, draw documents, sign, clear PTF, wire, and reach Funded. Correspondent purchase wire is P09, not this process.

### In / out of scope

In: CD timing, calendar, docs out, signing, funding conditions, wire, Funded event.

Out: lock desk, servicing boarding KPIs, Correspondent purchase.

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail | Company closer owns calendar, CD, docs, funding. |
| Wholesale | Closing often at Broker’s title/attorney; company still must accept CD, receive signed package, and fund. |
| Correspondent | Out of this process. |

### Actors

Closer, funding desk, title/escrow, borrower, Broker (Wholesale).

### Trigger, inputs, outputs

Trigger: CTC.

Outputs: scheduled; CD sent; docs out; signed; Funded; funding failed.

### Happy path

1. Schedule closing; confirm CD timing (TRID specific business days — Saturdays count, Sundays and federal holidays do not).
2. Draw and send docs.
3. Signing (wet/hybrid/eClose).
4. Clear PTF; wire; stamp Funded.
5. Hand to post-close (P10).

### Exception paths

- Funding fail / delayed funding (M-QLT-15): wire, vesting, last-minute curative, expired payoff.
- Reschedule; CD redisclosure.
- CTC revoke returns file to P07.

### Systems of record

LOS; closing platform; wire system (event only: success/fail time).

### Timestamps / events

Scheduled; CD sent; docs out; signed; funding initiated; Funded; funding failed.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| CTC to scheduled | 1 business day | ASSUMED SLA |
| CTC to Funded | 5 business days | ASSUMED SLA |
| Docs out to signed | 2 business days | ASSUMED SLA |
| Signed to Funded | 1 business day | ASSUMED SLA |

### Metrics produced

M-VOL-06, M-VOL-07, M-CYC-02, M-CYC-03, M-CYC-10, M-CYC-17, M-CYC-18, M-QLT-15, M-CAP-01 (closer).

### Reporting questions

- CTC-to-fund p50/p90 by Channel (Retail vs Wholesale only)?
- Funding fail rate and top reasons?
- Closings scheduled versus funded this week?

### Data-quality risks

Funded date vs disbursement date; Wholesale table-funded vs lender-funded confusion (metric is company Funded); Correspondent purchases in the funded count; CD sent used as docs out.

**Dashboards:** [D07](dashboards/D07-closing-and-funding.md). Default Channel filter excludes Correspondent.

---

## P09 Correspondent intake and pre-purchase

### Purpose

Take in a TPO closed loan, decide whether to buy it, and complete Correspondent purchase. This is the Correspondent manufacturing spine.

### In / out of scope

In: TPO eligibility, registration, Submission, pre-purchase QC/UW, conditions to TPO, purchase decision, purchase advice to TPO, wire to TPO.

Out: TPO’s origination and borrower closing; lock desk pricing; investor delivery (P11).

### Channel variants

Correspondent only. Retail and Wholesale files must not appear on D08 except as a company-wide comparison explicitly labeled.

### Actors

Correspondent ops analyst, pre-purchase underwriter, QC reviewer, TPO, funding/wire.

### Trigger, inputs, outputs

Trigger: TPO registration or Submission.

Outputs: File start (intake); Submission complete; purchase decision; Correspondent purchase.

### Happy path

1. Confirm TPO eligibility and commitment/lock (Lock status from Capital Markets).
2. Intake File start; receive Submission.
3. Pre-purchase QC and eligibility UW.
4. Conditions to TPO; TPO clears.
5. Purchase decision approved; wire; Correspondent purchase stamp.
6. Hand to P10 and P11.

### Exception paths

- Rejected at intake or after review (Fallout, not credit deny).
- High-defect TPO; suspend TPO (counterparty action, not a loan Milestone).
- Purchase delayed on trailing docs that should have been in the stack.

### Systems of record

TPO portal; LOS Correspondent screens; QC checklist; wire.

### Timestamps / events

Intake; Submission; QC complete; conditions issued/cleared; purchase decision; purchased; rejected.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Intake to Submission-complete (package) | TPO-owned; monitor only | Not an internal SLA |
| Submission to purchase decision | 2 business days | ASSUMED SLA |
| Purchase decision to purchased (wire) | 1 business day | ASSUMED SLA |

### Metrics produced

M-VOL-08, M-VOL-05C, M-VOL-09, M-VOL-10, M-CYC-11, M-CYC-11A, M-FAL-03, M-FAL-07, M-QLT-09, M-QLT-13.

### Reporting questions

- Submission-to-purchase p50/p90 and pull-through by TPO?
- Which TPOs drive pre-purchase defects and rejects?
- Purchase forecast next 7/14 days from approved-not-purchased?

### Data-quality risks

Registration counted as Submission; purchased labeled Funded; lock expiration treated as Fallout without a reason code; TPO name not conformed.

**Dashboards:** [D08](dashboards/D08-correspondent-operations.md), [D11](dashboards/D11-manufacturing-quality.md).

---

## P10 Post-closing and trailing documents

### Purpose

Complete the stack after Funded or Correspondent purchase so the loan can be Delivered. Original note, recorded security instrument, final title policy, and trailing conditions.

### In / out of scope

In: trailing inventory by document type, aging, MERS/MIN completeness as stack items, trailing from TPO.

Out: investor delivery decision (P11), servicing customer contact.

### Channel variants

| Channel | What changes |
|---------|----------------|
| Retail / Wholesale | Company closing package; chase title for recording and final policy. |
| Correspondent | Many trailers come from the TPO; Waiting-on party = TPO is common. |

### Actors

Post-closer, title/escrow, TPO, MERS ops.

### Trigger, inputs, outputs

Trigger: Funded or Correspondent purchase.

Outputs: each required trailer in; stack-complete / ship-ready.

### Happy path

1. Open trailing checklist from product/investor.
2. Receive original note, recorded instrument, final policy, remaining trailers.
3. Stamp ship-ready; hand to P11.

### Exception paths

- Recording delay by jurisdiction (age is real; blame is not internal).
- Lost original note; reconstruction.
- TPO unresponsive (M-QLT-12).

### Systems of record

LOS post-close; imaging; MERS.

### Timestamps / events

Funded/purchased; each trailer received; ship-ready.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Funded/purchased to ship-ready (no long-record states) | 15 business days | ASSUMED SLA |
| Critical trailers (note, mortgage) | 10 business days | ASSUMED SLA |

### Metrics produced

M-CYC-12, M-AGE-08, M-QLT-12, M-VOL-14, M-CAP-01 (post-closer).

### Reporting questions

- Trailing WIP by document type and age?
- Missing-trailer rate at 10 and 15 business days, by Channel and TPO?
- Ship-ready versus Delivered gap (handoff to P11)?

### Data-quality risks

Checklist not product-specific (false missing); recording states mixed into “internal delay”; ship-ready not stamped so delivery cycle looks worse than post-close.

**Dashboards:** [D09](dashboards/D09-post-closing-and-trailing-docs.md).

---

## P11 Investor delivery

### Purpose

Deliver the loan to the committed investor and reach Investor purchase. Suspense and Kickout live here.

### In / out of scope

In: commitment/eligible investor, ULDD, stack, Delivered event, investor suspense, purchase advice, Kickout, resubmit.

Out: gain-on-sale, pool formation economics (Capital Markets); servicing.

### Channel variants

Same delivery process after Funded or Correspondent purchase. Correspondent may aggregate. Slice by Channel; do not use different metric names.

### Actors

Shipping/delivery, Capital Markets (commitment assignment — adjacent), post-close.

### Trigger, inputs, outputs

Trigger: ship-ready (or parallel if policy allows early delivery).

Outputs: Delivered; Investor purchase; Kickout opened/cured.

### Happy path

1. Assign investor/commitment (Capital Markets may own assignment; Operations owns execution).
2. Build ULDD/stack; deliver.
3. Receive purchase advice; stamp Investor purchase.

### Exception paths

- Investor suspense (M-AGE-09).
- Kickout (M-QLT-10, M-QLT-11); cure and resubmit.
- Commitment mismatch; redelivery.

### Systems of record

LOS investor screens or shipping system; investor portals.

### Timestamps / events

Delivered; suspense; Kickout; resubmitted; Investor purchase.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Ship-ready to Delivered | 2 business days | ASSUMED SLA |
| Delivered to Investor purchase (no suspense) | 5 business days | ASSUMED SLA |

### Metrics produced

M-VOL-11, M-VOL-12, M-CYC-13, M-CYC-14, M-AGE-09, M-QLT-10, M-QLT-11.

### Reporting questions

- What is not Delivered, and what is Delivered but not Investor-purchased?
- Kickout rate and reason mix by investor and Channel?
- Delivery cycle p50/p90 from Funded or Correspondent purchase?

### Data-quality risks

Delivered = Investor purchase in the LOS; Kickout overwritten; Channel lost at delivery; early delivery before ship-ready unlabeled.

**Dashboards:** [D10](dashboards/D10-investor-delivery.md), [D11](dashboards/D11-manufacturing-quality.md) for Kickouts.

---

## P12 Manufacturing quality

### Purpose

Find and score defects during manufacturing: pre-fund QC, Correspondent pre-purchase QC, post-close QC, and Kickouts. This is not independent audit QC.

### In / out of scope

In: sample selection for manufacturing QC, defect taxonomy (critical/major/minor), TPO scorecard defects, Kickout as an external defect signal.

Out: independent Quality audit, compliance testing programs unless dual-tagged.

### Channel variants

Retail/Wholesale: pre-fund and post-close samples. Correspondent: pre-purchase (often 100% or high-touch) and post-purchase.

### Actors

QC reviewer (ops), UW (dispute), TPO (Corr), delivery (Kickout).

### Trigger, inputs, outputs

Trigger: policy sample at UW/CTC, at purchase, after Funded, or Kickout received.

Outputs: defect findings with severity; pass/fail; TPO rolling score.

### Happy path

1. Select sample (or 100% pre-purchase).
2. Review against taxonomy.
3. Record defects; feed rework (P07) or TPO conditions (P09).
4. Roll defects to scorecards (P13 counterpart for TPO; Vendor for AMC/title).

### Exception paths

- Critical defect stops CTC or purchase.
- Dispute/overturn — catalog should count net confirmed defects; show overturn rate as a data-quality metric if captured.

### Systems of record

QC module or checklist in LOS; Kickout reasons from investor.

### Timestamps / events

QC started/completed; defect logged; severity; Kickout reason.

### ASSUMED SLA

| Clock | Target | Basis |
|-------|--------|-------|
| Pre-fund QC complete before CTC | Same day as assignment | ASSUMED SLA |
| Pre-purchase QC inside purchase-decision SLA | See P09 | ASSUMED SLA |
| Post-close QC | 5 business days from Funded/purchased | ASSUMED SLA |

### Metrics produced

M-QLT-07 through M-QLT-13, M-QLT-10/11 (Kickout).

### Reporting questions

- Defect rate by severity, Channel, team, and TPO?
- Do Kickout reasons match internal defect themes?
- Is pre-purchase defect rate improving for a TPO?

### Data-quality risks

Audit QC mixed into manufacturing sample; severity not standardized; multiple findings on one file double-counted in file-level rates (catalog defines both finding-count and file-fail rate).

**Dashboards:** [D11](dashboards/D11-manufacturing-quality.md).

---

## P13 Vendor management

### Purpose

Measure third-party order performance (AMC, appraiser, title, credit, flood, tax, QC vendor). TPO performance is a counterpart scorecard on D08/D11, not a Vendor metric.

### In / out of scope

In: on-time, cycle, revisions, concentration, optional cost per order.

Out: TPO as Vendor; Broker as Vendor; employee appraisers as FTE (capacity), though staff-appraiser turn can sit next to AMC for comparison if labeled.

### Channel variants

Same Vendor types. Correspondent rarely new-orders; when it does, use the same metrics.

### Actors

Vendor manager, desks in P03–P05, procurement/finance for cost.

### Trigger, inputs, outputs

Trigger: order placed.

Outputs: completed order; on-time flag vs ASSUMED SLA; revision count.

### Happy path

1. Route order to panel Vendor.
2. Track cycle versus SLA.
3. Score monthly; manage concentration and poor performers.

### Exception paths

- Reassignment after Vendor decline.
- Revision/ROV.
- Cost data unavailable — omit M-VEN-05 until Finance shares it.

### Systems of record

AMC/title/credit/flood portals; LOS order records.

### Timestamps / events

Order placed, accepted, completed, revised.

### ASSUMED SLA

Use P03–P05 clocks. Credit: 1 business day. Tax: 2 business days.

### Metrics produced

M-VEN-01 through M-VEN-06.

### Reporting questions

- On-time % and p90 by Vendor and state?
- Is order share too concentrated in one AMC or title company?
- Revision rate outliers?

### Data-quality risks

Vendor names not conformed; Broker-ordered work without company SLA clock; cost from AP not joinable to orders.

**Dashboards:** [D12](dashboards/D12-vendor-performance.md).

---

## P14 Capacity, productivity, and queues

### Purpose

Match staffed FTE to arrivals and WIP so queues do not age. Employee-day grain, rolled to role and team.

### In / out of scope

In: units completed per FTE, queue depth per FTE, utilization versus plan, arrivals versus completions, new vs WIP mix.

Out: HR performance management, compensation, overtime dollars unless an hours feed exists (M-CAP-06 only if captured).

### Channel variants

Queues are Channel-aware. Correspondent analysts are not “processors” unless the company truly uses that role title — keep role names honest.

### Actors

Ops leadership, team managers, workforce planner.

### Trigger, inputs, outputs

Trigger: daily. Inputs: roster FTE, files assigned, completions. Outputs: capacity vs arrival.

### Happy path

1. Snapshot FTE by role (productive FTE, not just on payroll).
2. Snapshot queue depth and completions.
3. Compare arrivals (File starts, UW submits, CTCs, Submissions) to completions.

### Exception paths

- Surge in one Channel with staff still aligned to another.
- Hidden WIP in “unassigned.”

### Systems of record

LOS assignment; HRIS or roster for FTE (dimension source only).

### Timestamps / events

Daily roster; assignment changes; completion events (already defined in P02–P11).

### ASSUMED SLA

| Signal | Target | Basis |
|--------|--------|-------|
| Queue depth per processor FTE | Company-set; placeholder 15–25 files | ASSUMED SLA |
| Queue depth per UW FTE | Placeholder 8–12 files | ASSUMED SLA |

### Metrics produced

M-CAP-01 through M-CAP-06.

### Reporting questions

- Are UW completions keeping up with UW arrivals this week?
- Which teams are above queue-depth SLA?
- Units per FTE trending down while WIP ages up?

### Data-quality risks

FTE includes PTO as productive; dual-assigned files double-count; completions credited to current assignee not the person who did the work (state the rule: completing assignee).

**Dashboards:** [D13](dashboards/D13-capacity-and-productivity.md).

---

## P15 Pipeline control

### Purpose

Enterprise view of WIP, aging, stuck files, and 7/14/30-day Funded and Correspondent-purchase forecast. Not a team; a control process for huddles.

### In / out of scope

In: Pipeline units, milestone mix, aging bands, stuck definition, waiting-on mix, CTC not scheduled, lock expiring before CTC, fund/purchase forecast.

Out: Sales funnel, lock desk P&L.

### Channel variants

Retail/Wholesale Pipeline ends at Funded. Correspondent Pipeline ends at Correspondent purchase. Post-close WIP is a separate bucket (M-VOL-14).

### Actors

Ops VP, desk managers (daily huddle).

### Trigger, inputs, outputs

Trigger: As-of snapshot (recommend 6:00 a.m. local ops calendar).

Outputs: huddle pack; stuck-file export.

### Happy path

1. Snapshot open files by Channel and Milestone.
2. Band age; flag SLA-breach and stuck.
3. Forecast next 7/14/30 from CTC, scheduled, purchase-approved.
4. Drill to desk dashboards.

### Exception paths

- Forecast misses because CTC revoke or funding fail — track as forecast quality later if leadership asks; not in v1 catalog.

### Systems of record

LOS As-of. No separate system.

### Timestamps / events

Uses everyone else’s timestamps. Stuck = no Milestone change in N business days (table below).

### ASSUMED SLA (stuck and aging)

| Milestone | Age SLA | Stuck if no change |
|-----------|---------|--------------------|
| Setup / intake | 1 business day | 2 business days |
| Processing | 5 business days | 3 business days |
| UW | 2 business days | 2 business days |
| Conditions | 5 business days | 3 business days |
| CTC / scheduled | 5 business days to Funded | 2 business days |
| Corr purchase-approved | 1 business day to purchased | 2 business days |
| Post-close | 15 business days to ship-ready | 5 business days |
| Delivered not purchased | 5 business days | 3 business days |

### Metrics produced

M-VOL-13, M-VOL-14, M-AGE-01 through M-AGE-09, M-FAL-* (cohort, not As-of).

### Reporting questions

- Where is the Pipeline, how old, who are we waiting on?
- What is expected to Fund or Correspondent-purchase in 7/14/30 days?
- Which stuck files are internal versus Vendor versus borrower/Broker/TPO?

### Data-quality risks

As-of mixed with Event-dated on D01 without labels; Correspondent open files in “not funded” Pipeline; Milestone backdating clears stuck flags.

**Dashboards:** [D02](dashboards/D02-pipeline-and-aging.md), [D01](dashboards/D01-ops-command-center.md).

---

## If offered: construction draws, HELOC, reverse

These are product-dimension values, not additional Operations subcategories in this pack. If the company originates them:

- Construction: draw desk Cycle time and inspection Vendor metrics can be added later as P03-like orders.
- HELOC: often shorter CTC clock; still use the same metric IDs.
- Reverse: appraisal and title still P03/P04; UW overlays differ.

Do not build separate dashboards until volume justifies them.
