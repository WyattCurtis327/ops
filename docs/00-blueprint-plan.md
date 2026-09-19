# Operations Subject Area — Enterprise Dashboard & Reporting Blueprint

> **For agentic workers:** This is a documentation job, not a software build. Do not create Databricks dashboards, metric views, apps, or SQL. Write the markdown pack below, then stop.

**Goal:** Capture business requirements for enterprise Operations dashboards and reporting at a multi-channel non-bank mortgage company (retail, wholesale, correspondent), covering loan manufacturing from application/intake through post-closing, trailing documents, and investor delivery.

**Architecture:** Three-layer documentation pack in the `ops` repo: (1) a narrative requirements BRD, (2) a governed metric + dimension catalog, (3) per-dashboard reporting specs. Domain language lives in root `CONTEXT.md`. Company-neutral; no loanDepot branding.

**Tech stack:** Markdown only. No Databricks, no YAML metric views, no HTML/PDF user-guide build unless a later job asks.

**Spec:** This plan *is* the spec. Execution writes the files listed under File Map.

## Locked decisions

- **Channels in scope:** Retail (consumer-direct), Wholesale (broker), Correspondent (closed-loan purchase).
- **Lifecycle in scope:** File setup / intake → disclosures (retail/wholesale) → processing → valuation → title/escrow → insurance/MI → underwriting → conditions / CTC → closing & funding (or correspondent purchase) → post-closing / trailing docs → investor delivery / purchase advice.
- **Out of scope subject areas:** Sales/lead intake, lock desk and secondary marketing (Capital Markets), servicing, independent enterprise QC/audit as a separate Quality org, Finance P&L, HRIS except as a dimension source for capacity.
- **In scope quality:** Manufacturing quality only — pre-funding QC, correspondent pre-purchase QC, post-close QC, defects, investor kickouts/suspense. Independent audit QC is adjacent, not owned here.
- **Lock desk:** Not an Operations process. Lock status, expiration, and extension *are* Operations dimensions and CTC/funding dependencies.
- **Deliverable depth:** Full reporting blueprint (requirements + glossary + metric catalog + per-dashboard specs). No wireframe images; markdown specs are the wireframes.

## Assumptions (flag in every doc; replace when Ops leadership provides local names)

- Typical non-bank origination: conventional, FHA, VA, USDA, jumbo; purchase and refinance. HELOC/construction/reverse appear only as product-dimension values plus a short “if offered” process note.
- Cycle times in **business days** unless the metric names a TRID clock. Initial LE send uses TRID **general business days** (creditor-open). CD wait uses TRID **specific business days**. (Corrected after [14-research-sources.md](14-research-sources.md); do not use calendar days for the LE send clock.)
- Primary grain is the **loan file**. Order/event grain for appraisal, title, insurance, QC findings. Employee-day grain for capacity.
- Snapshot metrics (pipeline, aging, WIP) are as-of; flow metrics (funded, delivered, turns completed) are event-dated.
- SLA targets in the pack are **industry-typical placeholders** labeled `ASSUMED SLA` — not company policy.
- LOS is the system of record for file/milestone; vendor portals for appraisal/title; shipping/delivery system or LOS investor screen for delivery.

## Out of this job

- Building dashboards, Genie spaces, or Unity Catalog metric views
- Source-system mapping to real tables (call that out as a follow-on data discovery job)
- Servicing, Capital Markets, Sales, or enterprise audit QC subject areas
- Pixel mockups / Figma / Streamlit / Databricks Apps

---

## File map

```
CONTEXT.md
docs/
  README.md
  01-scope-and-taxonomy.md
  02-processes-by-subcategory.md
  03-shared-dimensions.md
  04-metric-catalog.md
  05-dashboard-inventory.md
  dashboards/
    D01-ops-command-center.md
    D02-pipeline-and-aging.md
    D03-processing.md
    D04-appraisal-and-valuation.md
    D05-title-escrow-closing-coord.md
    D06-underwriting-and-conditions.md
    D07-closing-and-funding.md
    D08-correspondent-operations.md
    D09-post-closing-and-trailing-docs.md
    D10-investor-delivery.md
    D11-manufacturing-quality.md
    D12-vendor-performance.md
    D13-capacity-and-productivity.md
    D14-disclosures-and-setup.md
```

---

## Document templates (use these exactly)

### Process section (inside `02-processes-by-subcategory.md`)

For each subcategory:

1. Purpose (2–4 sentences)
2. In / out of scope
3. Channel variants (Retail / Wholesale / Correspondent — what changes)
4. Actors
5. Trigger, inputs, outputs
6. Happy-path steps (numbered)
7. Exception paths (ROV, curative, suspense, kickout, redisclosure, etc.)
8. Systems of record (generic: LOS, AMC portal, title portal, …)
9. Timestamps / events the metrics need
10. `ASSUMED SLA` targets
11. Metrics produced (IDs from the catalog)
12. Reporting questions this process must answer
13. Data-quality risks (missing order date, milestone backdating, …)

### Metric catalog row (`04-metric-catalog.md`)

Every metric is a table row with: ID, Name, Subcategory, What it measures, Business formula, Grain, Unit, Direction (up good / up bad / context), Time basis (event vs as-of), Required dimensions, Owner role, Dashboards.

Group the catalog by metric family, not by dashboard. Families: Volume & flow · Cycle time · Aging & WIP · Pull-through & fallout · Quality · Capacity · Vendor.

### Dashboard spec (`docs/dashboards/Dxx-*.md`)

1. Purpose and primary decision
2. Audience and genre (`static` exec glance vs `analytic` drill)
3. Cadence and freshness (intraday vs daily; snapshot time)
4. Headline KPIs (metric IDs)
5. Layout: stratified (KPIs on top, comparison row, detail)
6. Visuals (what chart/table, what comparison: vs SLA, WoW, vs plan)
7. Filters (must include Channel; others as listed per dashboard)
8. Drill path (to which dashboard or loan-level export)
9. Grain and “one loan counted once” rules
10. Empty / stale / partial data notes
11. Out of scope for this view

---

## Locked Operations taxonomy

Fifteen subcategories. Cross-cutting views (pipeline, capacity, vendor, quality) are still Operations, not other subject areas.

| ID | Subcategory | Typical owner | Retail / Wholesale | Correspondent |
|----|-------------|----------------|--------------------|---------------|
| P01 | Disclosure & file setup | Disclosure desk / setup | TRID LE, intent to proceed, redisclosure, eSign, file start | Registration/intake of TPO file; seller disclosures already exist — eligibility + package completeness |
| P02 | Processing | Processor / team lead | Doc collection, AUS, credit, VOE/VOI/VOA, HOA/condo, milestone chase | Package completeness vs seller; conditions to TPO; not borrower-facing processing |
| P03 | Appraisal & valuation | Appraisal desk | Order, waiver (PIW/ACE), inspection, report, review, ROV, 2nd appraisal | Review of seller appraisal / transfer; rarely a new order |
| P04 | Title, escrow & curative | Title desk / closer | Order, commitment, curative, payoffs, CD collab, HOA estoppel | Review of existing title/closing package; curative before purchase |
| P05 | Insurance & MI | Processor / MI desk | HOI, flood, master policy, MI order/cert | Confirm coverage and MI on purchased loan |
| P06 | Underwriting | Underwriter | Initial decision, overlays, exceptions, MI UW, suspense | Pre-purchase UW / eligibility review |
| P07 | Conditions & CTC | Processor + UW | PTD/PTF conditions, CTC, rework loops | Conditions to purchase |
| P08 | Closing coordination & funding | Closer / funding | Schedule, docs out, signing, funding conditions, wire, fund | **Purchase funding** (wire to TPO) — not borrower closing |
| P09 | Correspondent intake & pre-purchase | Correspondent ops | n/a | TPO eligibility, registration, submission, pre-purchase QC, purchase decision |
| P10 | Post-closing & trailing docs | Post-close | Original note, recorded security instrument, final title, trailing conditions | Trailing docs from TPO after purchase |
| P11 | Investor delivery | Shipping / delivery | Stack, ULDD, deliver, purchase advice, investor suspense | Same after purchase; may aggregate |
| P12 | Manufacturing quality | QC (ops) | Pre-fund QC, post-close QC, defects | Pre-purchase QC, post-purchase QC, TPO defect scoring |
| P13 | Vendor management | Ops vendor mgmt | AMC, appraisers, title, credit, flood, tax | TPO as “vendor” plus same third parties when re-ordered |
| P14 | Capacity, productivity & queues | Ops leadership | Staffing, units/FTE, queue depth | Same, plus TPO queue |
| P15 | Pipeline control | Ops leadership | Cross-cutting WIP, aging, stuck, fund forecast | Purchase forecast + delivery forecast |

**Channel is a required dimension on every enterprise view.** Do not build channel-siloed metric definitions; define once, slice by channel.

### Channel process variants (must be explicit in P01–P11)

**Retail:** Company originates and manufactures. Ops owns borrower collection, disclosure, appraisal order, title order, UW, CTC, closing, funding.

**Wholesale:** Broker originates. Ops is fulfillment: registration, UW, conditions split with broker, valuation/title often broker-ordered or lender-ordered (both paths documented), closing often title/broker coordinated, lender funds.

**Correspondent:** TPO originates *and closes*. Ops is intake → pre-purchase review → purchase → post-purchase trailing docs → investor delivery. Appraisal/title/closing already happened; the manufacturing work is eligibility, QC, purchase, and delivery.

---

## Shared dimensions (content for `03-shared-dimensions.md`)

Conformed dimensions used across the subject area. Each gets a one-line definition, grain, and “do not confuse with” note.

**Always available (enterprise filters):**
- Channel (Retail, Wholesale, Correspondent)
- Loan purpose (Purchase, Rate/term refi, Cash-out, Streamline/IRRRL)
- Product program (Conv, FHA, VA, USDA, Jumbo, Non-QM, Other)
- Occupancy, property type, state
- Investor / commitment
- Current milestone / status
- Fulfillment center / pod / team
- Lock status (Locked, Expired, Not locked, Float) — dimension only
- As-of date / event date (never mix in one chart without labeling)

**People / org:**
- Loan officer / branch (retail)
- Broker / TPO (wholesale / correspondent)
- Processor, underwriter, closer, post-closer (current and originating)
- Manager / team

**File characteristics (bands, not raw PII):**
- Loan amount band, LTV/CLTV band, FICO band
- Occupancy, units, condo/PUD/site-built
- Self-employed vs W2 (income type)
- AUS recommendation (Approve/Eligible, Refer, Ineligible, …)
- Occupancy of milestone (who the file is waiting on: borrower, broker/TPO, vendor, internal)

**Vendor:**
- Vendor type (AMC, appraiser, title, closing attorney, credit, flood, tax, QC vendor)
- Vendor name
- Order type (appraisal, title, flood, …)

**Time:**
- Event date (PST or company ops calendar — state the choice)
- Business-day calendar
- Milestone entered/exited timestamps

**Explicit non-dimensions for this subject area:** marketing channel, lead provider, CPL/ROM (Sales subject area); note rate / lock price (Capital Markets).

---

## Metric families and must-have metrics

IDs are stable. Names are business language. Formulas in the catalog are business formulas, not SQL.

### Volume & flow (event-dated unless noted)

| ID | Metric | Formula (business) | Notes |
|----|--------|--------------------|-------|
| M-VOL-01 | Files started | Count of files with setup/registration complete | Channel-specific start event |
| M-VOL-02 | Applications taken | Count of applications | Retail/wholesale; correspondent uses submissions |
| M-VOL-03 | Locks in force (as-of) | Count of files currently locked | Dimension from CM; not a lock-desk KPI |
| M-VOL-04 | Underwritten (decisioned) | Count of first UW decisions | Include approve, suspend, deny |
| M-VOL-05 | Clear to close | Count of CTC events | |
| M-VOL-06 | Funded units | Count of lender-funded originations | Retail/wholesale only |
| M-VOL-07 | Funded volume | Sum of funded loan amounts | Retail/wholesale |
| M-VOL-08 | Correspondent submissions | Count of TPO packages submitted | Correspondent |
| M-VOL-09 | Correspondent purchased units | Count of loans purchased from TPO | Correspondent “funding” |
| M-VOL-10 | Correspondent purchased volume | Sum of purchase amounts | |
| M-VOL-11 | Delivered units | Count delivered to investor | All channels after purchase/fund |
| M-VOL-12 | Investor purchased units | Count purchased by investor (purchase advice) | |
| M-VOL-13 | Pipeline units (as-of) | Open files not yet funded/purchased | Define “open” per channel |
| M-VOL-14 | Post-close WIP (as-of) | Funded/purchased, not yet delivered | |

### Cycle time (business days; report p50 and p90, not only average)

| ID | Metric | Clock start → stop |
|----|--------|--------------------|
| M-CYC-01 | Start to CTC | File start → first CTC |
| M-CYC-02 | CTC to fund | CTC → fund |
| M-CYC-03 | Start to fund | File start → fund (retail/wholesale) |
| M-CYC-04 | Disclosure turn | Application/ITP → initial LE sent |
| M-CYC-05 | Processing file-complete time | Start → processing complete / submitted to UW |
| M-CYC-06 | UW turn (initial) | Submitted to UW → first decision |
| M-CYC-07 | Condition turn | Condition issued → condition cleared (median per file and per condition) |
| M-CYC-08 | Appraisal cycle | Order → report in (and order → reviewed) |
| M-CYC-09 | Title cycle | Order → commitment in (and commitment → clear) |
| M-CYC-10 | Closing cycle | CTC → docs out → signed → funded |
| M-CYC-11 | Correspondent purchase cycle | Submission → purchase decision → purchased |
| M-CYC-12 | Trailing-doc cycle | Fund/purchase → last required trailing doc in |
| M-CYC-13 | Delivery cycle | Fund/purchase → delivered |
| M-CYC-14 | Investor purchase cycle | Delivered → investor purchase advice |

Also: **touch time vs queue time** where timestamps exist (time in status waiting on party X).

### Aging & WIP (as-of snapshot)

| ID | Metric |
|----|--------|
| M-AGE-01 | Units in milestone (by milestone) |
| M-AGE-02 | Age in current milestone (p50/p90, bands 0–2, 3–5, 6–10, 11+ business days) |
| M-AGE-03 | SLA-breach units (age > assumed SLA for that milestone) |
| M-AGE-04 | Stuck files (no milestone change in N days — N by milestone) |
| M-AGE-05 | Waiting-on party mix (borrower / broker-TPO / vendor / internal) |
| M-AGE-06 | Lock-expiring-before-CTC (risk set) |
| M-AGE-07 | CTC but not scheduled |
| M-AGE-08 | Funded not delivered (aging) |
| M-AGE-09 | Delivered not purchased (investor suspense aging) |

### Pull-through & fallout

| ID | Metric | Formula |
|----|--------|---------|
| M-FAL-01 | Pull-through start-to-fund | Funded / files started (cohort by start month) |
| M-FAL-02 | Lock-to-fund pull-through | Funded / locked (cohort by lock month) — retail/wholesale |
| M-FAL-03 | Submission-to-purchase | Purchased / submitted (correspondent) |
| M-FAL-04 | Fallout units | Withdrawn + denied + expired + rejected (channel-specific codes) |
| M-FAL-05 | Fallout rate | Fallout / starts (or submissions) |
| M-FAL-06 | Denial rate, withdraw rate, suspend rate | Split fallout reasons |
| M-FAL-07 | Broker/TPO pull-through | Same metrics by broker/TPO |

Cohort by origination month *and* offer a rolling 30/90 day mix. Catalog must say which default each dashboard uses.

### Quality

| ID | Metric |
|----|--------|
| M-QLT-01 | Conditions per file (PTD, PTF, total) |
| M-QLT-02 | Suspense rate (first UW decision = suspend) |
| M-QLT-03 | Rework rate (file returns to prior milestone) |
| M-QLT-04 | Redisclosure rate |
| M-QLT-05 | Appraisal revision / ROV rate |
| M-QLT-06 | Title curative rate |
| M-QLT-07 | Pre-fund QC defect rate (critical / major / minor) |
| M-QLT-08 | Post-close QC defect rate |
| M-QLT-09 | Correspondent pre-purchase defect rate |
| M-QLT-10 | Investor kickout / suspense rate |
| M-QLT-11 | Kickout reason mix |
| M-QLT-12 | Trailing-doc missing rate at N days after fund |
| M-QLT-13 | TPO scorecard defects (rolling) |

### Capacity & productivity

| ID | Metric |
|----|--------|
| M-CAP-01 | Units completed per FTE (by role: processor, UW, closer, post-close) |
| M-CAP-02 | Queue depth per FTE |
| M-CAP-03 | Utilization (files touched / capacity plan) |
| M-CAP-04 | New vs WIP mix |
| M-CAP-05 | Capacity vs arrival (starts vs completions) |
| M-CAP-06 | Overtime / after-hours completions (if captured) |

### Vendor

| ID | Metric |
|----|--------|
| M-VEN-01 | Orders placed / completed |
| M-VEN-02 | Vendor cycle p50/p90 vs SLA |
| M-VEN-03 | On-time % |
| M-VEN-04 | Revision rate |
| M-VEN-05 | Cost per order (if finance will share; else omit and note dependency) |
| M-VEN-06 | Concentration (share of orders by vendor) |

**Headline enterprise KPIs** (Command Center only — keep to ~8): Pipeline units, Funded + purchased units, Start-to-fund / submission-to-purchase p50, CTC count, SLA-breach %, Pull-through, Kickout rate, Capacity vs arrival.

---

## Dashboard family (14 specs)

Genre from dashboard-patterns: exec = `static` stratified; the rest = `analytic` with Channel + date + product + team filters.

| ID | Dashboard | Primary audience | Primary question | Genre |
|----|-----------|------------------|------------------|-------|
| D01 | Ops Command Center | COO / Ops VP | Are we on-time, on-capacity, and converting pipeline to funds/purchases/deliveries? | static |
| D02 | Pipeline & aging | Ops managers | Where is the pipeline stuck, how old, who are we waiting on, what funds/purchases in 7/14/30 days? | analytic |
| D03 | Processing | Processing managers | File completeness, processor turn, queue, waiting-on borrower/broker | analytic |
| D04 | Appraisal & valuation | Appraisal desk | Order-to-report, waivers, ROV, vendor on-time, purchase-file appraisal defects | analytic |
| D05 | Title, escrow & closing coord | Title desk / closing managers | Commitment turn, curative, CD timing, schedule-to-close | analytic |
| D06 | Underwriting & conditions | UW / conditions managers | UW turn, suspend, conditions per file, CTC, rework | analytic |
| D07 | Closing & funding | Closing/funding managers | CTC-to-fund, docs out, signing, funding fails, wires | analytic |
| D08 | Correspondent operations | Correspondent ops | Submissions, pre-purchase cycle, purchase, TPO scorecard, conditions to TPO | analytic |
| D09 | Post-closing & trailing docs | Post-close managers | Trailing WIP, aging by doc type, complete-to-ship ready | analytic |
| D10 | Investor delivery | Shipping / secondary ops (delivery) | Delivered, not purchased, suspense aging, kickouts | analytic |
| D11 | Manufacturing quality | QC / Ops risk | Defects, kickouts, rework, TPO defects — not independent audit | analytic |
| D12 | Vendor performance | Vendor mgmt | On-time, cycle, revisions, concentration by AMC/title/credit | analytic |
| D13 | Capacity & productivity | Ops leadership / workforce | Units/FTE, queue/FTE, arrivals vs completions by role | analytic |
| D14 | Disclosures & setup | Disclosure desk | LE timing, redisclosure, eSign, file-start quality (TRID calendar days) | analytic |

**Navigation:** D01 is the only enterprise home. Every other dashboard is a drill target. D02 is the default drill from any volume/aging KPI. Channel toggle is global.

**Not a dashboard in this pack:** loan-level worklist in the LOS (mention as operational system of action; BI may offer a stuck-file export, not a servicing-style queue app).

---

## Key processes by subcategory (content outline for `02-`)

Write the full happy path + exceptions in the doc. This outline is the checklist — do not drop a row.

**P01 Disclosure & file setup**
- Retail: application → TRID application date → LE within 3 calendar days → intent to proceed → redisclosure on fee/rate/program change → CD timing handoff to closing
- Wholesale: broker submission → lender LE if lender is creditor → redisclosure shared with broker
- Correspondent: TPO registration + closed-loan package intake; TRID already occurred at TPO
- Metrics: M-VOL-01/02, M-CYC-04, M-QLT-04, D14

**P02 Processing**
- Order third parties, collect income/assets/credit, AUS, HOA/condo, package to UW, chase conditions
- Waiting-on party is first-class
- Metrics: M-CYC-05, M-AGE-*, M-CAP-01 (processor), D03

**P03 Appraisal & valuation**
- Need vs waiver, order, assignment, inspection, report in, review, ROV, value recon, 2nd appraisal, transfer of appraisal (wholesale/corr)
- Metrics: M-CYC-08, M-QLT-05, M-VEN-* (AMC), D04

**P04 Title, escrow & curative**
- Order, search, commitment, liens/curative, payoffs, taxes, HOA, CD numbers, wet vs hybrid vs eClose
- Metrics: M-CYC-09, M-QLT-06, D05

**P05 Insurance & MI**
- HOI binder, mortgagee clause, flood determination, MI application/cert, cancellable vs non
- Light dashboard presence: KPIs on D03/D05, not a 15th dashboard

**P06–P07 Underwriting & conditions**
- Submit → AUS + manual overlays → decision (approve/suspend/deny) → conditions PTD/PTF → CTC → CTC revoke
- Correspondent: eligibility + pre-purchase conditions
- Metrics: M-VOL-04/05, M-CYC-06/07, M-QLT-01/02/03, D06

**P08 Closing & funding (retail/wholesale)**
- Schedule, CD, docs out, signing, funding conditions, wire, fund, first-payment/MERS handoff into post-close
- Correspondent analog is purchase wire in P09
- Metrics: M-VOL-06/07, M-CYC-02/10, D07

**P09 Correspondent intake & pre-purchase**
- TPO eligibility, registration, lock (CM), submission, pre-purchase QC/UW, conditions to TPO, purchase decision, purchase advice to TPO, wire
- Metrics: M-VOL-08/09/10, M-CYC-11, M-FAL-03, M-QLT-09/13, D08

**P10 Post-closing & trailing docs**
- Stack completeness, original note, recorded instrument, final policy, trailing conditions, MERS, trailing from TPO
- Metrics: M-CYC-12, M-AGE-08, M-QLT-12, D09

**P11 Investor delivery**
- Eligible investor/commitment, ULDD, stack, ship/deliver, suspense, purchase advice, kickout, resubmit
- Metrics: M-VOL-11/12/14, M-CYC-13/14, M-QLT-10/11, D10

**P12–P15** Quality, vendor, capacity, pipeline — supporting processes: sample selection, defect taxonomy, vendor scorecards, staffing plan vs arrivals, daily huddle on stuck files.

---

## Personas and questions the pack must answer

Write a short “who uses this” section in `01-scope-and-taxonomy.md`:

- COO / Ops VP: Are cycle time, pull-through, and delivery healthy vs last week and vs SLA?
- Processing / UW / Closing / Post-close managers: Where is my queue, who is waiting, which teams are off SLA?
- Appraisal / title desks: Which vendors and states are slow or high-revision?
- Correspondent ops: Which TPOs are high-defect or slow to clear purchase conditions?
- Capacity planner: Do we have enough processors/UWs/closers for this week’s arrivals?
- Delivery / shipping: What is not sold, aging in suspense, kicked out?
- BI / analytics: What is the canonical metric name, grain, and direction?

Each dashboard spec lists 5–8 concrete questions it answers (e.g. “What share of CTCs aged out of SLA by channel this week?”).

---

## Writing sequence

Write in this order so terms and metric IDs exist before dashboards reference them.

### Task 1: Domain glossary

**Files:** Create `CONTEXT.md`

- Operations, Channel, Loan file, Milestone, Clear to Close, Funded, Correspondent purchase, Delivered, Investor purchase, Fallout, Pull-through, Condition (PTD/PTF), Suspense, Kickout, Trailing document, Vendor, Cycle time, Pipeline (WIP), Manufacturing quality
- Opinionated `_Avoid_` list (e.g. avoid “account” for loan file; avoid “funding” for correspondent purchase without qualifier; avoid “QC” without pre-fund vs post-close vs independent audit)
- Keep to domain-modeling format. No implementation details.

### Task 2: Scope, taxonomy, README

**Files:** Create `docs/README.md`, `docs/01-scope-and-taxonomy.md`

- README is a map of the pack (what to read first)
- Scope in/out, channel definitions, lifecycle diagram in mermaid (retail/wholesale vs correspondent)
- Taxonomy table (P01–P15)
- Personas
- Dashboard family table (D01–D14) with links
- Adjacent subject areas and handoffs (Sales → Ops at application; Ops → Capital Markets on lock; Ops → Servicing at boarding; Ops → Quality audit)

### Task 3: Processes by subcategory

**Files:** Create `docs/02-processes-by-subcategory.md`

- One H2 per P01–P15 using the process template
- Channel variants required on P01–P11
- P05 stays a full process section even without its own dashboard

### Task 4: Dimensions and metric catalog

**Files:** Create `docs/03-shared-dimensions.md`, `docs/04-metric-catalog.md`

- Every metric in the families above, plus any timestamp-driven metrics implied by process sections
- Do not invent SQL
- Mark `ASSUMED SLA` separately (a small SLA table by milestone)

### Task 5: Dashboard inventory + D01–D07

**Files:** Create `docs/05-dashboard-inventory.md` and `docs/dashboards/D01` through `D07`

- Inventory: purpose, audience, grain, cadence, drill map
- Full spec template for each
- D01 uses only the eight headline KPIs
- Global filters: Channel, date range, product, fulfillment team

### Task 6: Dashboards D08–D14

**Files:** Create `docs/dashboards/D08` through `D14`

- D08 must not reuse retail “funded” language — use purchased/submitted
- D10 distinguishes delivered vs investor-purchased
- D11 manufacturing quality vs independent audit (out)
- D14 TRID clocks in calendar days, called out explicitly

### Task 7: Consistency pass

- Every metric ID in a dashboard exists in the catalog
- Every process cites metrics and dashboards
- CONTEXT terms match the BRD
- No servicing, lock-desk, or lead-intake KPIs
- No TODOs / TBDs except the labeled `ASSUMED SLA` and “source-system mapping is a follow-on job”

---

## Success criteria

- A BI lead can build a semantic layer from `03` + `04` without inventing grains
- An Ops VP can see which dashboard answers which decision from `05` + D01
- A process owner can recognize their work in `02` including channel differences
- Correspondent is never described as “just another retail channel”
- Glossary prevents “funding” vs “purchase” vs “investor purchase” confusion

## Follow-on jobs (do not do now)

1. Data discovery: map timestamps and grains to LOS / vendor / delivery tables
2. Unity Catalog metric views from `04-metric-catalog.md`
3. AI/BI (Lakeview) dashboards from D01–D14
4. Servicing, Capital Markets, Sales subject-area packs
