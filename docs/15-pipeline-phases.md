# Ops pipeline phases — metrics and dimensions

## Overview

This is the manufacturing pipeline, phase by phase. Each phase lists **what happens**, **who owns it**, **which Channel uses it**, then the **metrics** and **dimensions** that belong there.

Two factories share post-close and delivery:

```text
Retail / Wholesale
  MS-01 Setup → MS-02 Disclosures → MS-03 Processing
       ↳ parallel: appraisal (P03), title (P04), insurance/MI (P05)
  → MS-06 UW → MS-07 Conditions → MS-08 CTC / close / Funded
  → MS-11 Post-close → MS-12 Ship-ready → Delivered → MS-13 Investor purchase

Correspondent
  MS-01 Intake → MS-09 Submission → pre-purchase UW/QC
  → MS-10 Purchase approved → Correspondent purchase
  → MS-11 Post-close → MS-12 Ship-ready → Delivered → MS-13 Investor purchase
```

A file has **one current milestone**. Appraisal and title are usually **orders on a file still in processing or conditions**. Use Waiting-on = Vendor unless the LOS actually parks the file in MS-04 / MS-05.

**Always-on dimensions** (every phase, every enterprise view): Channel, product program, loan purpose, occupancy, property type, state, fulfillment team, Event date or As-of date (never mix unlabeled).

**Always-on aging set** when the file is still in Pipeline or Post-close WIP: M-AGE-01, M-AGE-02, M-AGE-03, M-AGE-04, M-AGE-05 (Waiting-on: WAIT-BOR / WAIT-TPO / WAIT-VEN / WAIT-INT).

IDs: [milestones](11-milestones-and-reason-codes.md), [catalog](04-metric-catalog.md), [dimensions](03-shared-dimensions.md), [events](06-event-dictionary.md).

---

## Phase 0 — Cross-cutting control (not a stage)

These run the whole time. They are not a milestone the file “enters.”

| Control | Process | Metrics | Extra dimensions | Wireframe |
|---------|---------|---------|------------------|-----------|
| Pipeline huddle | P15 | M-VOL-13, M-VOL-03, M-AGE-01–07, M-FAL-01–05, M-FST-01–03 | Current milestone, Waiting-on, Lock status | P15 / D02 |
| Capacity | P14 | M-CAP-01–06, M-CYC-15 | Role, team, productive FTE | P14 / D13 |
| Manufacturing QC | P12 | M-QLT-07–13 | QC type, severity, Channel | P12 / D11 |
| Vendor panel | P13 | M-VEN-01–06 | Vendor type, Vendor name, state | P13 / D12 |
| Command Center | EXE | M-VOL-16, M-CYC-03 + M-CYC-11, M-AGE-03, M-FAL-01 + M-FAL-03, M-QLT-10, M-CAP-05 | Channel only on the eight tiles | EXE / D01 |

---

## Phase 1 — File start / setup / intake

**Milestone:** MS-01  
**Process:** P01 (R/W setup), P09 (Corr intake)  
**Owner:** Disclosure / setup desk; Correspondent ops for intake  
**In:** Application received (R/W), registration (Wholesale), TPO intake (Corr)  
**Out:** File start complete; file is in Pipeline (M-VOL-13)

| Channel | What happens |
|---------|----------------|
| Retail | Create Loan file; stamp File start when setup complete. |
| Wholesale | File start = **registration complete**, not “we took the application.” |
| Correspondent | File start = intake complete. **Not** an Application. No company LE. |

**Events:** E-START, E-APP (R/W only), E-INTAKE-REJ (Corr)

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-01 Files started. M-VOL-02 Applications taken (**R/W only**). |
| Cycle | Setup lag: application/registration received → E-START (ASSUMED 1 bd). |
| Aging | M-AGE-01/02/03/04 in MS-01. |
| Quality / fallout | FAL-REJ at intake (Corr). FAL-DUP if combined. |

**Phase dimensions:** Channel, product, team, LO (Retail), Broker (Wholesale), TPO (Corr).  
**Do not:** increment M-VOL-02 for Correspondent. Do not call intake “funded.”

**Wireframe:** P01 (R/W), P09 (Corr intake funnel first step)

---

## Phase 2 — Disclosures (Retail / Wholesale only)

**Milestone:** MS-02  
**Process:** P01  
**Owner:** Disclosure desk  
**In:** TRID application (six pieces: name, income, SSN, property address, estimate of value, loan amount)  
**Out:** Initial LE sent; intent to proceed; file can order most settlement services

| Channel | What happens |
|---------|----------------|
| Retail / Wholesale | Send initial LE within **3 TRID general business days** (creditor-open days). Capture intent to proceed. Redisclose on changed circumstance. |
| Correspondent | **Skip.** TPO already disclosed. |

**Events:** E-TRID-APP, E-LE-INIT, E-LE-SIGN, E-ITP, E-REDISC

| Kind | Metrics |
|------|---------|
| Cycle | M-CYC-04 Disclosure turn (general business days). |
| Quality | M-REG-01 LE miss rate. M-QLT-04 Redisclosure rate. |
| Aging | eSign incomplete = Waiting-on WAIT-BOR or WAIT-TPO. |

**Phase dimensions:** Channel (R/W), product, team, LO/Broker.  
**Clock note:** CD waiting period is a **different** TRID clock (specific business days) and lives in Phase 8, not here.

**Wireframe:** P01 / D14

---

## Phase 3 — Processing (package to decisionable)

**Milestone:** MS-03  
**Process:** P02  
**Owner:** Processor / team lead  
**In:** File start (and ITP on R/W)  
**Out:** Submitted to UW (R/W) or package-complete to pre-purchase (Corr if processors own it)

Work: credit, AUS, income/assets (VOE/VOI/VOA), HOA/condo, chase, third-party orders (Phases 4–6 run in parallel).

| Channel | What happens |
|---------|----------------|
| Retail | Processor collects from borrower and LO; company orders third parties. |
| Wholesale | Split with Broker. Waiting-on is often WAIT-TPO. |
| Correspondent | Not borrower-facing. Package completeness vs TPO; otherwise this work sits on P09. |

**Events:** E-PROC-ASGN, E-WAIT, E-UW-SUBMIT, E-AUS, E-PKG-COMPLETE (Corr)

| Kind | Metrics |
|------|---------|
| Cycle | M-CYC-05 File start → UW submit. M-CYC-15 queue time (WAIT-INT). |
| Aging | M-AGE-01–05 in processing. Waiting-on mix is the huddle slice. |
| Capacity | M-CAP-01/02 processor. M-CAP-05 arrivals = starts, completions = UW submits. |
| Quality | M-QLT-03 rework back into processing after Suspense. |

**Phase dimensions:** Channel, team, processor, Waiting-on, income type (W2 vs self-employed), AUS recommendation, Broker.  
**Wireframe:** P02 / D03

---

## Phase 4 — Appraisal and valuation (parallel order)

**Milestone:** MS-04 only if LOS parks the file here; else order on MS-03/MS-07  
**Process:** P03  
**Owner:** Appraisal desk  
**Grain:** Order (and file for waiver rate)

| Channel | What happens |
|---------|----------------|
| Retail | Waiver test (Value Acceptance / ACE) or order after ITP. Inspection → report → review. ROV if needed. |
| Wholesale | Company-ordered **or** Broker-ordered / transfer. Broker-ordered clock starts at **received-in** if no company order date. |
| Correspondent | Seller appraisal already exists. Review / transfer. Rarely a new order — **exclude from M-CYC-08**. |

**Events:** E-APPR-WAIVE, E-APPR-ORD, E-APPR-RCV, E-APPR-REV, E-ROV

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-15 Waiver rate. M-VEN-01 orders. |
| Cycle | M-CYC-08 order → report (**exclude waivers**). M-CYC-08A report → review. |
| Quality | M-QLT-05 ROV / revision rate. |
| Vendor | M-VEN-02/03/04 by AMC, state. |

**Phase dimensions:** Channel, Vendor name/type, state, property type, **appraisal path** (company-ordered, Broker-ordered, transferred, waived, seller).  
**AIR:** production staff (Restricted Parties) do not pick the appraiser. Desk/AMC independence is a process constraint, not a metric.  
**Wireframe:** P03 / D04 → P13

---

## Phase 5 — Title, escrow, curative (parallel order)

**Milestone:** MS-05 only if LOS parks here  
**Process:** P04  
**Owner:** Title desk / closer  
**Grain:** Order / file

| Channel | What happens |
|---------|----------------|
| Retail | Order title; commitment; curative; payoffs, taxes, HOA; CD figures. |
| Wholesale | Often Broker/borrower already opened title; company reviews. |
| Correspondent | Review existing package; curative before purchase. |

**Events:** E-TTL-ORD, E-TTL-CMT, E-TTL-CUR-OPEN, E-TTL-CUR-CLR

| Kind | Metrics |
|------|---------|
| Cycle | M-CYC-09 order → commitment. M-CYC-09A commitment → curative clear. |
| Quality | M-QLT-06 curative rate (context — ALTA: ~36% of files are “difficult”). |
| Aging | CTC blocked on title/HOA/payoff → M-AGE-05 WAIT-VEN. M-AGE-07 if CTC with no schedule (handoff to Phase 8). |
| Vendor | M-VEN-* by title company, **state** (county recording is the tail). |

**Phase dimensions:** Channel, Vendor, state, closing type (wet / hybrid / eClose).  
**Do not:** treat 5-bd commitment SLA as “title is done.” Curative and recording are longer clocks.  
**Wireframe:** P04 / D05

---

## Phase 6 — Insurance and MI (parallel; no own milestone)

**Process:** P05  
**Owner:** Processor / MI desk  
**Ships as:** tiles on P02, P04, P06 — no D15

| Channel | What happens |
|---------|----------------|
| Retail / Wholesale | Flood determination, HOI accept, MI apply/cert if product/LTV requires. |
| Correspondent | Confirm coverage and transferable MI. |

**Events:** E-HOI-REQ, E-HOI-OK, E-FLOOD, E-MI-APP, E-MI-CERT

| Kind | Metrics |
|------|---------|
| Cycle | M-CYC-16 HOI accept. M-CYC-16A MI cert (**MI-required files only**). Flood order cycle on P13. |
| Aging | CTC-blocked on HOI or MI = M-AGE-05 WAIT-VEN (or WAIT-BOR if borrower has not sent binder). |

**Phase dimensions:** Channel, product (MI vs not), MI company.  
**Wireframe:** P05

---

## Phase 7 — Underwriting (first decision)

**Milestone:** MS-06  
**Process:** P06  
**Owner:** Underwriter  
**In:** E-UW-SUBMIT (R/W) or Submission complete (Corr)  
**Out:** First decision: approve-with-conditions, Suspense, or deny / Corr reject

| Channel | What happens |
|---------|----------------|
| Retail / Wholesale | AUS + overlays + collateral/title status → first credit decision. |
| Correspondent | Eligibility / pre-purchase UW. Outcome is purchase-eligible, conditions-to-TPO, or **reject** (FAL-REJ, not FAL-DEN). |

**Events:** E-UW-ASGN, E-UW-FIRST (immutable), E-UW-LATER

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-04 first decisions. |
| Cycle | M-CYC-06 submit → first decision. M-CYC-15 UW queue time. |
| Quality | M-QLT-02 Suspense rate. M-FAL-06 deny / withdraw / suspend. |
| Capacity | M-CAP-01/02 UW. Completions = first decisions. |

**Phase dimensions:** Channel, UW team, AUS recommendation, product, TPO (Corr).  
**Do not:** overwrite E-UW-FIRST. Do not count AUS as the UW decision.  
**Wireframe:** P06 / D06 UW slice

---

## Phase 8 — Conditions and Clear to Close

**Milestone:** MS-07 then MS-08 (R/W)  
**Process:** P07  
**Owner:** Processor + UW  
**In:** Conditions issued  
**Out:** CTC (R/W) or purchase-approved (Corr analog is Phase 9)

| Channel | What happens |
|---------|----------------|
| Retail | Collect PTD/PTF; UW clears; CTC. |
| Wholesale | Many conditions wait on Broker (WAIT-TPO). |
| Correspondent | Conditions to TPO; **do not stamp M-VOL-05**. Use M-VOL-05C. |

**Events:** E-COND-ISS, E-COND-CLR, E-CTC, E-CTC-REV, E-PUR-APPR (Corr)

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-05 CTC (**R/W only**). |
| Cycle | M-CYC-01 start → CTC. M-CYC-07 condition grain. M-CYC-07F file grain. |
| Quality | M-QLT-01 conditions/file (PTD vs PTF vs PTP). M-QLT-03 rework. M-QLT-14 CTC revoke. |
| Aging | M-AGE-06 lock expiring before CTC. M-AGE-07 CTC not scheduled. |

**Phase dimensions:** Channel, team, PTD vs PTF, Waiting-on, Lock status.  
**Wireframe:** P07 / D06 conditions slice

---

## Phase 9 — Closing and funding (Retail / Wholesale only)

**Milestone:** MS-08  
**Process:** P08  
**Owner:** Closer / funding  
**In:** CTC  
**Out:** Funded → **leaves Pipeline**, enters Post-close WIP  
**Correspondent: skip. Purchase wire is Phase 10.**

**Events:** E-SCHED, E-CD-SENT, E-DOCS-OUT, E-SIGNED, E-FUND-ATT, E-FUND-FAIL, E-FUNDED

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-06 Funded units. M-VOL-07 Funded volume. M-VOL-16 includes these. |
| Cycle | M-CYC-02 / M-CYC-10 CTC → Funded. M-CYC-03 start → Funded. M-CYC-17 docs out → signed. M-CYC-18 signed → Funded. |
| Quality | M-QLT-15 funding fail rate. CD wait = TRID **specific business days**. |
| Aging | M-AGE-07. |
| Capacity | M-CAP-01 closer. Completions = Funded. |
| Pull-through | Cohort that reaches E-FUNDED counts in M-FAL-01 / M-FAL-02. |

**Phase dimensions:** Channel **Retail + Wholesale only**, closer, closing type, state.  
**Do not:** put Correspondent in M-VOL-06.  
**Wireframe:** P08 / D07

---

## Phase 10 — Correspondent submission, pre-purchase, purchase

**Milestones:** MS-09 → MS-10 → purchased  
**Process:** P09  
**Owner:** Correspondent ops  
**In:** TPO registration / Submission  
**Out:** Correspondent purchase → **leaves Pipeline**, enters Post-close WIP  
**Retail/Wholesale: skip.**

**Events:** E-SUB, E-PUR-APPR, E-PURCHASED, E-FALLOUT (FAL-REJ)

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-08 Submissions. M-VOL-05C Purchase approved. M-VOL-09/10 Purchased units/volume. M-VOL-16 includes M-VOL-09. |
| Cycle | M-CYC-11 Submission → purchased. M-CYC-11A Submission → decision. |
| Pull-through | M-FAL-03, M-FAL-05, M-FAL-07 by TPO. |
| Quality | M-QLT-09 pre-purchase defect. M-QLT-13 TPO scorecard. |
| Aging | Approved-not-purchased. Waiting-on WAIT-TPO. M-FST-02. |
| Optional dimension | **Delegated vs non-delegated** (who underwrote at the TPO). Add when the company has both. |

**Phase dimensions:** TPO, product, Channel locked Correspondent.  
**Do not:** say Funded. Registration ≠ Submission.  
**Wireframe:** P09 / D08

---

## Phase 11 — Post-closing and trailing documents

**Milestone:** MS-11  
**Process:** P10  
**Owner:** Post-closer  
**In:** E-FUNDED or E-PURCHASED  
**Out:** E-SHIP-RDY (stack complete)

Work: original note, recorded security instrument, final title, other investor trailers, MERS MIN completeness.

| Channel | What happens |
|---------|----------------|
| Retail / Wholesale | Chase title for recording and final policy. County recording delay = WAIT-VEN, not internal. |
| Correspondent | Many trailers from TPO (WAIT-TPO). |

**Events:** E-TRAIL-IN (per TRL-NOTE / TRL-SEC / TRL-TTL / TRL-MI / TRL-OTH), E-SHIP-RDY

| Kind | Metrics |
|------|---------|
| Flow / WIP | M-VOL-14 Post-close WIP. |
| Cycle | M-CYC-12 Funded/purchased → ship-ready. |
| Aging | M-AGE-08. M-QLT-12 missing at day 10 and 15. |
| Capacity | M-CAP-01 post-closer. Completions = ship-ready. |

**Phase dimensions:** Channel, TPO, investor, document type, state (recording).  
**Clock note:** Ginnie **final certification** (12 months after issue) is **not** this 15-bd ship-ready clock. Do not mix them.  
**Wireframe:** P10 / D09

---

## Phase 12 — Investor delivery

**Milestone:** MS-12 then MS-13  
**Process:** P11  
**Owner:** Shipping / delivery  
**In:** Ship-ready  
**Out:** E-DELIVERED then E-INV-PURCH (or Kickout / suspense)

Same process after Funded or Correspondent purchase. Slice by Channel; do not rename purchase events.

**Events:** E-DELIVERED, E-INV-SUSP, E-KICKOUT, E-REDELIVER, E-INV-PURCH

| Kind | Metrics |
|------|---------|
| Flow | M-VOL-11 Delivered. M-VOL-12 Investor purchased. |
| Cycle | M-CYC-13 Funded/purchased → Delivered. M-CYC-14 Delivered → investor purchase. |
| Aging | M-AGE-09 Delivered not purchased. |
| Quality | M-QLT-10 Kickout rate. M-QLT-11 reason mix (KIK-*). |

**Phase dimensions:** Channel, investor, commitment, Kickout reason.  
**Do not:** call this Funded. Fannie “Purchased and Funded” is **investor** purchase = M-VOL-12.  
**Wireframe:** P11 / D10

---

## Fallout vs Kickout (where they attach)

| When | Code family | Metrics | Not |
|------|-------------|---------|-----|
| Before Funded (R/W) or before Corr purchase | FAL-* | M-FAL-04/05/06 | Kickout |
| After Delivered | KIK-* | M-QLT-10/11 | Fallout |

Phase 1–10 can emit Fallout. Phase 12 emits Kickout. Phase 11 missing trailers often **cause** later KIK-TRL.

---

## Dimension cheat sheet by phase

| Phase | Required extra slices (beyond always-on) |
|-------|------------------------------------------|
| 1 Setup / intake | LO, Broker, TPO |
| 2 Disclosures | LO/Broker; TRID app date |
| 3 Processing | Processor, Waiting-on, income type, AUS |
| 4 Appraisal | Vendor, appraisal path, state |
| 5 Title | Vendor, state, closing type |
| 6 Insurance / MI | MI company, product (MI-required flag) |
| 7 UW | UW team, AUS, first-decision outcome |
| 8 Conditions / CTC | PTD vs PTF, Waiting-on, Lock status |
| 9 Closing / Funded | Closer, closing type; Channel R/W only |
| 10 Corr purchase | TPO, delegated vs non-del if used |
| 11 Post-close | Document type, TPO, state |
| 12 Delivery | Investor, commitment, Kickout reason |
| Control P12 QC | QC type, severity |
| Control P13 Vendor | Vendor type/name |
| Control P14 Capacity | Role, productive FTE |

---

## One-page metric map (phase → headline IDs)

| Phase | Flow | Cycle | Aging / quality |
|-------|------|-------|-----------------|
| 1 Start | M-VOL-01, M-VOL-02 | setup 1 bd | MS-01 aging |
| 2 Disclosures | — | M-CYC-04, M-REG-01 | M-QLT-04 |
| 3 Processing | — | M-CYC-05 | M-AGE-05, M-CAP-01/02 |
| 4 Appraisal | M-VOL-15 | M-CYC-08/08A | M-QLT-05, M-VEN-03 |
| 5 Title | — | M-CYC-09/09A | M-QLT-06, M-AGE-07 |
| 6 Insurance | — | M-CYC-16/16A | WAIT-VEN on HOI/MI |
| 7 UW | M-VOL-04 | M-CYC-06 | M-QLT-02, M-FAL-06 |
| 8 Conditions | M-VOL-05 | M-CYC-01, M-CYC-07 | M-QLT-01/14, M-AGE-06 |
| 9 Funded (R/W) | M-VOL-06/07/16 | M-CYC-02/03/17/18 | M-QLT-15, M-FAL-01 |
| 10 Corr purchase | M-VOL-08/05C/09/10/16 | M-CYC-11/11A | M-FAL-03, M-QLT-09 |
| 11 Post-close | M-VOL-14 | M-CYC-12 | M-QLT-12, M-AGE-08 |
| 12 Delivery | M-VOL-11/12 | M-CYC-13/14 | M-QLT-10/11, M-AGE-09 |
