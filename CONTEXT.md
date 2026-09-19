# Operations

The Operations context is loan manufacturing at a non-bank mortgage company: the work that takes a file from intake through investor delivery. This glossary is the language for Operations dashboards, reports, and metric definitions.

## Subject area

**Operations**:
The function that manufactures a mortgage from file start (or correspondent intake) through investor delivery.
_Avoid_: Servicing, origination (when that means Sales), fulfillment (when used as a synonym for the whole subject area without naming the channel)

**Channel**:
How the loan entered manufacturing: Retail, Wholesale, or Correspondent.
_Avoid_: Source, lead source, marketing channel

**Retail**:
A Channel in which the company originates with the borrower and manufactures the loan through funding.
_Avoid_: Consumer-direct as a separate Channel; treat consumer-direct as Retail unless leadership splits it

**Wholesale**:
A Channel in which a broker originates with the borrower and the company manufactures and funds the loan.
_Avoid_: TPO for this Channel (TPO is the Correspondent seller; the Wholesale originator is a Broker)

**Correspondent**:
A Channel in which a TPO originates and closes the loan, and the company buys the closed loan.
_Avoid_: Wholesale, brokered, purchased (unqualified)

**Loan file**:
The unit of manufacturing work. One Loan file is one application or one correspondent submission in process.
_Avoid_: Account, deal, loan (when you mean the in-process file rather than the closed instrument)

## Channel counterparties

**Broker**:
The originating company on a Wholesale Loan file.
_Avoid_: TPO, correspondent, LO (the LO is a person; the Broker is the company)

**TPO**:
The originating and closing company that sells a closed loan on the Correspondent Channel.
_Avoid_: Broker, vendor (a TPO is a seller, not an appraisal or title Vendor)

**Loan officer**:
The originating salesperson on a Retail Loan file.
_Avoid_: Broker, processor

## Lifecycle events

**File start**:
The event that opens a Loan file in Operations. Retail: setup complete. Wholesale: registration complete. Correspondent: intake/registration complete.
_Avoid_: Application taken (that is a later or parallel Retail/Wholesale event), lead received

**Application**:
A Retail or Wholesale borrower's application as used for TRID and manufacturing. Correspondent uses Submission, not Application, as the manufacturing start analog.
_Avoid_: Using Application for a Correspondent package

**Submission**:
A TPO's closed-loan package presented for Correspondent purchase review.
_Avoid_: Application, registration (registration is File start; Submission is the package for purchase)

**Clear to Close**:
The underwriting authorization that a Retail or Wholesale Loan file may proceed to closing. Correspondent analog is Purchase decision (approved to purchase).
_Avoid_: Approved (that is an Underwriting decision, which may still have conditions), CTC as a funding event

**Funded**:
The lender has disbursed origination proceeds on a Retail or Wholesale loan.
_Avoid_: Funded for Correspondent purchase or Investor purchase; closed (closing is signing, not disbursement)

**Correspondent purchase**:
The company has bought a closed loan from a TPO.
_Avoid_: Funded, funding, Investor purchase

**Delivered**:
The company has submitted the loan to an investor for purchase.
_Avoid_: Shipped as the metric name (Shipping is the team); Investor purchase; sold (ambiguous)

**Investor purchase**:
The investor has paid the company for a Delivered loan, evidenced by a purchase advice.
_Avoid_: Funded, Correspondent purchase, Delivered

**Fallout**:
A Loan file that started manufacturing and did not reach Funded (Retail/Wholesale) or Correspondent purchase, for a defined reason set (withdrawn, denied, expired, rejected).
_Avoid_: Pull-through inverted without naming the cohort; cancelled as the only reason code

**Pull-through**:
The share of a defined start cohort that reached Funded or Correspondent purchase.
_Avoid_: Conversion (Sales language); close rate (ambiguous between closing and funding)

## Manufacturing states

**Milestone**:
A named manufacturing stage the Loan file is in right now. Canonical IDs are MS-01 through MS-13.
_Avoid_: Status as a synonym when Status also means lock, AUS, or condition status; stage when Milestone is the canonical name; raw LOS status strings on the Command Center

**Pipeline**:
The set of open Loan files not yet Funded (Retail/Wholesale) or not yet Correspondent-purchased.
_Avoid_: Funnel (Sales); booked; volume (volume is dollars)

**Post-close WIP**:
Funded or Correspondent-purchased Loan files not yet Delivered.
_Avoid_: Pipeline (Pipeline ends at Funded or Correspondent purchase)

**Waiting-on party**:
Who the Loan file is blocked on in the current Milestone: borrower, Broker or TPO, Vendor, or internal staff.
_Avoid_: Occupancy (that is a property attribute); owner (ambiguous)

**Condition**:
A requirement that must be satisfied before Clear to Close or funding (Retail/Wholesale) or before Correspondent purchase.
_Avoid_: Stip, task, checklist item as the metric name

**Prior-to-documents condition**:
A Condition that must be cleared before closing documents are drawn.
_Avoid_: PTD as unexplained jargon in executive views; use the full name once, then PTD

**Prior-to-funding condition**:
A Condition that must be cleared before Funded.
_Avoid_: PTF as unexplained jargon in executive views; use the full name once, then PTF

**Suspense**:
An underwriting decision that the file is not decisionable yet, usually because the package is incomplete or inconsistent.
_Avoid_: Denied; suspended lock; investor suspense (that is Kickout-related)

**Rework**:
A return of the Loan file to an earlier Milestone after it had already passed that Milestone.
_Avoid_: Touch; recycle as the metric name

**Kickout**:
An investor rejection or investor suspense of a Delivered loan that prevents Investor purchase until cured.
_Avoid_: Fallout (Fallout is pre-Funded / pre-Correspondent-purchase); defect (a defect may cause a Kickout, but they are not the same)

**Trailing document**:
A document required after Funded or Correspondent purchase to complete the stack for delivery.
_Avoid_: Condition (conditions are pre-close/pre-purchase); trailing as a Milestone name

## Valuation, title, vendors

**Vendor**:
A third party performing an ordered service (appraisal, title, credit, flood, tax, QC vendor). A TPO is not a Vendor; a Broker is not a Vendor.
_Avoid_: Partner, provider (lead provider is Sales)

**Appraisal cycle**:
The ordered valuation work from order (or waiver decision) through report-in and review.
_Avoid_: Appraisal as a synonym for the report only when you mean the whole cycle

**Reconsideration of value**:
A request to the appraiser or AMC to reconsider the appraised value.
_Avoid_: Appeal; ROV as unexplained jargon in executive views

**Title curative**:
Work to clear exceptions on the title commitment so the file can close or be purchased.
_Avoid_: Title as a synonym for curative only

## Quality and time

**Manufacturing quality**:
Defects found in pre-funding QC, Correspondent pre-purchase QC, post-close QC, and Kickouts.
_Avoid_: QC without a qualifier; independent audit QC (that is the Quality subject area)

**Cycle time**:
Elapsed business days between two named events on the same Loan file or order, unless the metric name says calendar days.
_Avoid_: Turn time as a different concept (Turn time is a Cycle time for a desk); average-only reporting (p50 and p90 are required)

**Turn time**:
Cycle time for a single desk or Vendor (for example underwriting Turn time).
_Avoid_: Cycle time when you mean one desk; SLA as the elapsed value (SLA is the target)

**As-of**:
A snapshot of Pipeline, aging, or locks in force at a point in time.
_Avoid_: Mixing As-of counts with event-dated Funded counts in one unlabeled number

**Event-dated**:
A flow metric attributed to the date the event happened (Funded, Delivered, decisioned).
_Avoid_: Booking date, application date, or As-of date as silent substitutes

**Lock status**:
Whether the Loan file currently has a rate lock: locked, expired, not locked, or float. Lock desk work belongs to Capital Markets.
_Avoid_: Lock price, note rate, or pull-through of the lock desk as Operations process metrics

## Decisions, clocks, and stack

**Purchase approved**:
The Correspondent decision that the company will buy the loan, analogous to Clear to Close on Retail/Wholesale.
_Avoid_: CTC, Funded, Underwritten (first decision may still have conditions)

**Ship-ready**:
The Post-close WIP state in which required trailing documents are in and the file may be Delivered.
_Avoid_: Delivered; complete (ambiguous); stacked (team jargon)

**Purchase advice**:
The investor’s notice that it has paid for a Delivered loan. That notice is the Investor purchase event.
_Avoid_: Funding advice (Correspondent purchase wire is a different event)

**Intent to proceed**:
The Retail/Wholesale borrower confirmation used as a gate before most settlement-service orders.
_Avoid_: File start; application taken

**Redisclosure**:
A subsequent Loan Estimate (or CD redisclosure) after the initial LE.
_Avoid_: Counting redisclosure as the initial LE clock

**Automated underwriting system recommendation**:
The AUS finding (Approve/Eligible, Refer, Ineligible, and equivalents). It is a dimension, not the underwriting decision.
_Avoid_: UW decision, CTC

**File-fail**:
A reviewed Loan file with at least one confirmed manufacturing defect at the headline severity.
_Avoid_: Finding count as the headline; mixing independent audit fails

**Productive FTE**:
Staffed manufacturing capacity in role, excluding time the roster treats as not productive when that flag exists.
_Avoid_: Payroll headcount as a silent substitute; using unassigned files as FTE

**Business day**:
A day on the company operations calendar, used for Cycle time unless the metric name says calendar days.
_Avoid_: Using business days for TRID initial LE

**TRID general business day**:
A day the creditor’s offices are open to the public for substantially all business functions. Used to count the three-day initial Loan Estimate **send** clock (§ 1026.19(e)(1)(iii); § 1026.2(a)(6) first sentence).
_Avoid_: Calendar day; assuming Saturday always counts

**TRID specific business day**:
All calendar days except Sundays and the federal holidays in 5 U.S.C. 6103(a). Used for Closing Disclosure waiting period and mailed-LE deemed receipt.
_Avoid_: Using this definition for the initial LE send clock

**Calendar day**:
A consecutive calendar day, including weekends.
_Avoid_: Using calendar days as the initial LE send clock (see TRID general business day)

**ULDD**:
The investor delivery dataset required to Deliver a loan. Incomplete ULDD is a delivery defect, not Fallout.
_Avoid_: Using ULDD as the name of the Delivered event
