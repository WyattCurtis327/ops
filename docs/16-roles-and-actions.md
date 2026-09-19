# Job roles and actions by pipeline phase

## Overview

Who does what, in order, on a Loan file. **Ops roles** manufacture the file. **Counterparties** (borrower, LO, Broker, TPO) and **Vendors** act on the file but are not Ops employees. **Adjacent** (Capital Markets lock desk, Finance wire, Servicing) touch the file at named handoffs only.

Channel changes *who* performs an action, not the name of the action. Correspondent does not close with the borrower; it **purchases** a closed loan.

Companion: [pipeline phases](15-pipeline-phases.md) (metrics/dimensions), [processes](02-processes-by-subcategory.md).

## Role roster

### Operations (internal)

| Role | Typical home phase | Job in one sentence |
|------|--------------------|---------------------|
| Setup / registration specialist | 1 | Opens the Loan file in the LOS and stamps File start. |
| Disclosure specialist | 2 | Issues and rediscloses TRID LE; captures intent to proceed and eSign. |
| Processor | 3, 6, 8 | Collects a decisionable package, chases Waiting-on, orders/tracks third parties, works conditions. |
| Processing team lead | 3, 0 | Assigns queue, runs huddle for processing, escalates stuck files. |
| Appraisal desk specialist | 4 | Decides waiver vs order, places AMC order, tracks report, routes review and ROV. **Not** production staff picking an appraiser (AIR). |
| Title desk / escrow coordinator | 5 | Orders or confirms title, tracks commitment and curative, feeds CD figures. |
| MI desk / specialist | 6 | Applies for MI, clears MI UW, confirms cert. Often a processor with MI queue. |
| Underwriter | 7, 8 | First credit (or Corr eligibility) decision; clears or issues conditions; exceptions. |
| UW team lead | 7 | Assigns UW queue, Suspense policy, overlay questions. |
| Conditions clerk / processor (conditions) | 8 | Publishes PTD/PTF list, collects evidence, resubmits to UW. |
| Closer | 9 | Schedules, draws docs, CD, signing coordination. |
| Funder | 9, 10 | Clears PTF, wires, stamps Funded (R/W) or purchase wire (Corr). |
| Correspondent ops analyst | 1, 10 | Intake, Submission completeness, TPO conditions, purchase decision routing. |
| Pre-purchase underwriter / QC reviewer | 7, 10, QC | Corr eligibility and manufacturing QC before purchase. |
| Post-closer | 11 | Trailing checklist, note, recording, final policy, MERS, ship-ready. |
| Delivery / shipping specialist | 12 | ULDD, stack, deliver, suspense, Kickout cure, investor purchase advice. |
| Manufacturing QC reviewer | QC overlay | Prefund / pre-purchase / post-close sample; defects; not independent audit. |
| Vendor manager | Vendor overlay | Panel, SLAs, concentration; does not order the individual appraisal (AIR). |
| Ops manager / huddle lead | Overlay | Daily P15 stuck list; does not work the file in the LOS for the desk. |

### Counterparties (not Ops, but they act)

| Role | Who they are | Typical actions |
|------|----------------|-----------------|
| Borrower | Retail (and sometimes Wholesale via Broker) | Apply, eSign, send docs, HOI, attend signing. |
| Loan officer (LO) | Retail salesperson | Takes application, helps collect, does **not** order appraisals (AIR Restricted Party). |
| Broker / Broker processor | Wholesale originating company | Takes application, often orders appraisal/title, clears Broker-side conditions. |
| TPO | Correspondent seller | Originated and closed the loan; submits package; clears purchase conditions; sends trailers. |
| Appraiser / AMC | Vendor | Accept order, inspect, report, respond to ROV. |
| Title / escrow / closing attorney | Vendor | Search, commitment, curative, closing table, recording, final policy. |
| Flood / credit / tax / HOA | Vendor | Determinations, reports, estoppels. |
| MI company | Vendor | MI UW and cert. |
| Investor / custodian | Secondary | Edits, certify, purchase advice, Kickout. |

### Adjacent (handoff only)

| Role | When they act | Ops does not own |
|------|----------------|------------------|
| Capital Markets lock desk | Lock, extension, commitment assignment | Lock price, note rate, gain-on-sale. |
| Treasury / warehouse | Wire at Funded or Corr purchase | Warehouse P&L; Ops owns the Funded/purchase **event**. |
| Servicing | After boarding package | Delinquency, escrow after boarding. |
| Independent audit QC | Sample after the fact | P12 manufacturing QC. |

**AIR (Appraiser Independence):** LO, Broker LO, and anyone paid on closing (**Restricted Parties**) must not select, retain, or substantively communicate with the appraiser/AMC on value. Processors/UWs may order if they are not Restricted Parties and do not report into production. Appraisal desk / AMC selects the appraiser.

---

## Phase 1 — File start / setup / intake (MS-01)

**Ops owner:** Setup specialist (R/W) or Correspondent ops analyst (Corr).

### Retail

| Role | Actions |
|------|---------|
| LO | Collects six TRID pieces (name, income, SSN, property address, estimate of value, loan amount). Submits application to Ops. Does not open manufacturing File start. |
| Setup specialist | Creates Loan file in LOS. Validates product/program. Stamps **E-APP** and **E-START** when setup is complete (not when the lead arrived). Assigns fulfillment team. Hands to disclosure. |
| Borrower | Signs application / eConsent as required. |

### Wholesale

| Role | Actions |
|------|---------|
| Broker | Takes borrower application; submits **registration** package to the company. |
| Setup / registration specialist | Registers the file. File start = **registration complete**, not “we took the application.” Stamps **E-START**. Does not count this as company-originated Application unless an application event exists. |

### Correspondent

| Role | Actions |
|------|---------|
| TPO | Sends intake / registration of a **closed** (or about-to-close) loan. |
| Corr ops analyst | Checks TPO eligibility, commitment/lock status (reads CM), package completeness. Stamps **E-START** (intake). **Rejects** incomplete/ineligible packages (**E-INTAKE-REJ**, FAL-REJ — not credit deny). Hands complete files toward Submission (Phase 10). |

**Handoff out:** R/W → Phase 2 disclosures. Corr → Phase 10 (skip disclosures).

---

## Phase 2 — Disclosures (MS-02) — Retail / Wholesale only

**Ops owner:** Disclosure specialist.

| Role | Actions |
|------|---------|
| Disclosure specialist | Sets **E-TRID-APP**. Builds fee worksheet. Issues initial **LE** within 3 **general business days** (creditor-open). Sends via eSign (**E-LE-INIT**). Tracks **E-LE-SIGN**. Issues redisclosure on changed circumstance (**E-REDISC**). Does **not** issue CD (that is the closer in Phase 9). |
| Borrower (Retail) or Broker (Wholesale) | eSigns LE. Indicates **intent to proceed** (**E-ITP**). Without ITP, processor must not order most settlement services. |
| Compliance (policy) | Owns LE content rules; not the send timestamp. |
| Processor | May not proceed to third-party orders until ITP (except credit report). |

Correspondent: **no action**. TPO already disclosed.

**Handoff out:** ITP + File start → processor (Phase 3).

---

## Phase 3 — Processing (MS-03)

**Ops owner:** Processor. Team lead owns the queue.

| Role | Actions |
|------|---------|
| Processing team lead | Assigns processor (**E-PROC-ASGN**). Watches queue depth. Sets Waiting-on if the processor left it blank. Escalates stuck files in the huddle. |
| Processor (Retail) | Pulls/refreshes credit. Runs or refreshes AUS (**E-AUS**). Collects income, assets, VOE/VOI/VOA, tax transcripts. Orders or confirms appraisal, title, flood (Phases 4–6). Requests HOA/condo docs. Updates **Waiting-on** every time the blocker changes. When the package is decisionable, stamps **E-UW-SUBMIT**. |
| Processor (Wholesale) | Same checklist, but **chases the Broker** first. Confirms whether appraisal/title are Broker-ordered. Does not re-order blindly. Waiting-on = WAIT-TPO when the Broker holds the ball. |
| Processor / Corr analyst | If Corr files sit on processing: completeness vs seller checklist, not borrower chase. Prefer P09. |
| LO (Retail) | Helps borrower send missing docs. Does not change UW decision. Does not pick the appraiser. |
| Broker processor | Sends documents and Broker-ordered reports. |
| Borrower | Sends docs; signs authorizations. |

**Handoff out:** E-UW-SUBMIT → underwriter (Phase 7). Third-party orders continue in parallel (Phases 4–6).

---

## Phase 4 — Appraisal and valuation (parallel)

**Ops owner:** Appraisal desk. Underwriter reviews value. AMC/appraiser executes.

| Role | Actions |
|------|---------|
| Processor | After ITP, requests valuation. Does **not** select the appraiser if Restricted Party rules apply. |
| Appraisal desk | Tests **waiver** (Value Acceptance / ACE). If waived, stamps **E-APPR-WAIVE** — no order. If not, places order with AMC (**E-APPR-ORD**). Tracks assignment, inspection, **E-APPR-RCV**. Routes to review. Opens **ROV** with a defined turn-time message; does not coach value. |
| AMC | Selects appraiser (AIR). Manages panel, fee, rush. Returns report and revisions. |
| Appraiser | Inspects, reports, responds to ROV with a revised report. |
| Underwriter | Completes **appraisal review** (**E-APPR-REV**). Accepts value or requests ROV / second appraisal. Cannot CTC without an accepted value or valid waiver. |
| Broker (Wholesale) | May have already ordered. Appraisal desk records **received-in**, not a fake company order date. |
| Corr analyst / UW | Reviews seller appraisal / transfer eligibility. Rarely a new order. |
| LO / Broker LO | **Forbidden:** selecting, retaining, or value-influencing communication with appraiser/AMC. May request factual correction through the desk. |

**Handoff out:** Value accepted or waived → UW/conditions can CTC on collateral.

---

## Phase 5 — Title, escrow, curative (parallel)

**Ops owner:** Title desk; closer uses the output.

| Role | Actions |
|------|---------|
| Processor or title desk | Orders title/escrow after ITP, or confirms Broker-opened order. |
| Title desk | Tracks **commitment in** (**E-TTL-CMT**). Inventories exceptions. Opens **curative** (**E-TTL-CUR-OPEN**): liens, judgments, vesting, survey. Collects payoffs, taxes, HOA estoppel. Clears (**E-TTL-CUR-CLR**). Delivers figures for CD. Sets closing type (wet / hybrid / eClose). |
| Title/escrow company | Search, commitment, curative work, closing table, later recording and final policy (Phase 11). |
| Closer | Uses commitment and figures; cannot schedule a clean CD without them. |
| HOA | Returns estoppel (WAIT-VEN). |
| Corr analyst | Reviews existing title/closing package; curative **before purchase**, not a new borrower close. |

**Handoff out:** Clear-to-close from title → conditions/CTC and closer.

---

## Phase 6 — Insurance and MI (parallel)

**Ops owner:** Processor; MI desk if specialized.

| Role | Actions |
|------|---------|
| Processor | Orders **flood determination**. Requests HOI binder with mortgagee clause (or condo master). Distinguishes HOI **received** vs **accepted**. If MI required, applies (**E-MI-APP**) and tracks cert (**E-MI-CERT**). |
| Borrower / Broker | Provides HOI. WAIT-BOR or WAIT-TPO until binder is acceptable. |
| Flood vendor | Returns determination. |
| MI company | MI UW; extra conditions may return to Phase 8. Issues cert. |
| Underwriter | Cannot CTC without HOI accepted and MI cert if required. |
| Corr analyst | Confirms coverage and transferable MI on the purchased loan. |

**Handoff out:** Insurance/MI complete flag for CTC.

---

## Phase 7 — Underwriting, first decision (MS-06)

**Ops owner:** Underwriter. Team lead owns the queue.

| Role | Actions |
|------|---------|
| UW team lead | Assigns file (**E-UW-ASGN**). Watches Suspense rate and queue/FTE. |
| Underwriter (Retail/Wholesale) | Reads package + AUS + overlays. Checks appraisal/title/MI status. Issues **first decision** (**E-UW-FIRST** — never overwrite): approve with conditions, **Suspense**, or **deny**. Writes PTD/PTF conditions. Requests exceptions through designated authority. |
| Underwriter (Correspondent) | Eligibility / pre-purchase. Approve to purchase, conditions to TPO, or **reject** (FAL-REJ). |
| Processor | On Suspense: returns to Phase 3, collects the missing piece, resubmits. Waiting-on updated. |
| Exception authority | Grants or denies overlay exceptions. |
| MI underwriter | Concurrent MI decision when needed. |
| Manufacturing QC (prefund sample) | May review before CTC; critical defect can stop the file. Independent of this UW if practical (GSE). |

**Handoff out:** Approve-with-conditions → Phase 8. Deny → Fallout. Corr reject → Fallout, not “credit deny” on Retail reports.

---

## Phase 8 — Conditions and CTC (MS-07 / MS-08)

**Ops owner:** Processor (collect) + underwriter (clear / CTC).

| Role | Actions |
|------|---------|
| Processor | Publishes condition list. Collects evidence. Updates Waiting-on (borrower vs Broker vs Vendor vs internal). Resubmits each item. |
| Underwriter | Accepts or rejects each condition (**E-COND-CLR**). When PTD + valuation + title + insurance gates are green, stamps **CTC** (**E-CTC**). Revokes CTC if something breaks (**E-CTC-REV**). |
| Broker / TPO | Clears their conditions. Dominant Waiting-on on Wholesale/Corr. |
| Borrower | Sends remaining docs (Retail). |
| Closer | May not draw docs until CTC (PTD). Sees PTF still open. |
| Capital Markets | Does not stamp CTC. Ops watches lock expiration (**M-AGE-06**) and asks CM for extension if Ops can still CTC. |
| Corr ops / UW | Stamps **purchase approved** (**E-PUR-APPR**), not CTC. |

**Handoff out:** CTC → closer (Phase 9). Purchase approved → funder/Corr ops (Phase 10).

---

## Phase 9 — Closing and funding (MS-08) — Retail / Wholesale only

**Ops owner:** Closer then funder.

| Role | Actions |
|------|---------|
| Closer | Schedules closing (**E-SCHED**). Issues **CD** on TRID **specific business days** (Sat counts; Sun/federal holiday do not). Draws and sends docs (**E-DOCS-OUT**). Coordinates wet / hybrid / eClose. Confirms vesting and figures with title. |
| Title/escrow / signing agent | Hosts signing (**E-SIGNED**). Returns executed package. |
| Borrower | Signs. |
| Broker (Wholesale) | Often coordinates the table; company still must accept CD and receive signed package. |
| Funder | Clears **PTF**. Initiates wire (**E-FUND-ATT**). On success stamps **Funded** (**E-FUNDED**). On fail stamps **E-FUND-FAIL** and reasons (wire, vesting, expired payoff). |
| Treasury / warehouse | Moves money; Ops owns the Funded **event**. |
| Processor / UW | Last-minute conditions; CTC revoke returns file to Phase 8. |

**Correspondent does not perform this phase** (borrower already closed at TPO).

**Handoff out:** Funded → post-closer (Phase 11). File **leaves Pipeline**.

---

## Phase 10 — Correspondent submission, pre-purchase, purchase

**Ops owner:** Correspondent ops analyst + pre-purchase UW/QC + funder.

| Role | Actions |
|------|---------|
| TPO | Completes **Submission** (closed-loan package). Clears conditions to purchase. Sends trailing docs later (Phase 11). |
| Corr ops analyst | Confirms Submission complete (**E-SUB**). Routes to pre-purchase review. Tracks TPO conditions. Coordinates purchase advice to TPO. |
| Pre-purchase UW | Eligibility decision (Phase 7 analog). |
| Pre-purchase QC | Manufacturing review before acquisition (GSE “prior to acquisition”). Defects → TPO conditions or reject. |
| Funder | Wires purchase proceeds to TPO. Stamps **Correspondent purchase** (**E-PURCHASED**). **Never** M-VOL-06 Funded. |
| Capital Markets | Lock/commitment on the acquired loan (dimension). |

**Delegated TPO:** TPO already underwrote; company still reviews eligibility/QC. **Non-delegated:** company UW is the credit decision.

**Handoff out:** Purchased → post-closer (Phase 11). File **leaves Pipeline**.

---

## Phase 11 — Post-closing and trailing documents (MS-11)

**Ops owner:** Post-closer.

| Role | Actions |
|------|---------|
| Post-closer | Opens trailing checklist from product × investor (TRL-NOTE, TRL-SEC, TRL-TTL, TRL-MI, TRL-OTH). Receives original note. Tracks recorded security instrument. Requests final title policy. Completes MERS registration / MIN (MOM often within **7 calendar days** of note/funding per investor guides). Stamps **ship-ready** (**E-SHIP-RDY**) when the stack can be delivered. |
| Title company | Records mortgage; issues final policy. County delay = WAIT-VEN, not a post-closer miss. |
| TPO (Corr) | Sends missing trailers. WAIT-TPO. |
| Delivery specialist | Will not Deliver a file that is not ship-ready unless policy allows early delivery (must be labeled). |
| MERS | System of record for MIN; post-closer executes registration/transfer. |

**Handoff out:** Ship-ready → delivery (Phase 12). Still **Post-close WIP**, not Pipeline.

---

## Phase 12 — Investor delivery (MS-12 / MS-13)

**Ops owner:** Delivery / shipping specialist. Capital Markets assigns investor; Ops executes.

| Role | Actions |
|------|---------|
| Capital Markets | Assigns investor / commitment (adjacent). |
| Delivery specialist | Builds ULDD/stack. Submits to Loan Delivery / investor portal (**E-DELIVERED**). Watches edits. Works **investor suspense** (**E-INV-SUSP**). On Kickout (**E-KICKOUT**) codes KIK-* and routes cure to the owning desk (trailing → post-close, collateral → appraisal, TPO package → Corr ops). Redelivers (**E-REDELIVER**). Captures **purchase advice** (**E-INV-PURCH**). |
| Document custodian | Certifies note package (GSE whole loan: often next-morning after clean data). |
| Investor | Purchase advice or Kickout/suspense reasons. |
| Post-closer / UW / Corr ops | Cure the Kickout reason; they do not “re-fund.” |
| Manufacturing QC | Kickout is an external defect signal on P12. |

**Handoff out:** Investor purchase → Servicing boarding (out of Operations headlines). Warehouse line releases (Treasury).

---

## Overlay roles (every phase)

| Role | Recurring actions |
|------|-------------------|
| Processing / UW / closing **team lead** | Assignment, huddle, SLA-breach, stuck export — work remains in the LOS. |
| Manufacturing QC reviewer | Prefund sample before CTC; Corr pre-purchase before acquisition; post-close sample after Funded/purchase. Same defect taxonomy. Critical stop. |
| Vendor manager | Monthly on-time / p90 / revision / concentration. Does not pick the appraiser for a file. |
| Ops manager | Daily P15: who are we waiting on, which milestone moved. Weekly EXE only. |
| BI / reporting | Does not change Waiting-on or milestones; maps LOS statuses to MS-* / WAIT-*. |

---

## Who may change Waiting-on

The **current manufacturing owner** (usually processor pre-CTC, closer post-CTC, post-closer after Funded, Corr analyst on P09) must set WAIT-BOR / WAIT-TPO / WAIT-VEN / WAIT-INT whenever the blocker changes. Blank is a data-quality fail, not “internal.”

## Who may stamp the money events

| Event | Who stamps | Who must not |
|-------|------------|--------------|
| E-FUNDED | Funder (R/W) | Corr ops, delivery, LO |
| E-PURCHASED | Funder / Corr ops | Closer (no borrower close) |
| E-INV-PURCH | Delivery (from purchase advice) | Funder |

---

## Swimlane (happy path, one line each)

**Retail:** LO takes app → setup opens file → disclosure sends LE → borrower ITP → processor builds package and orders third parties → appraisal desk/AMC values → title desk clears title → processor/MI certifies insurance → UW decision → processor+UW clear conditions → CTC → closer schedules/docs → parties sign → funder wires **Funded** → post-closer trailers → delivery **Delivers** → investor **purchases**.

**Wholesale:** Broker takes app and often orders appraisal/title → registration starts file → company LE if creditor → processor chases **Broker** → same UW/CTC/fund as Retail.

**Correspondent:** TPO already closed → Corr analyst intake → TPO Submission → pre-purchase UW/QC → purchase approved → funder **purchases from TPO** → post-closer trailers from TPO → same delivery.
