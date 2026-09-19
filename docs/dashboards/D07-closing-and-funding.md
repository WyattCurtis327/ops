# D07 Closing and funding

## Purpose and primary decision

Convert CTC to Funded: schedule, docs out, signing, PTF, wire. **Correspondent is off by default.** Correspondent purchase wire is D08.

## Audience and genre

Closing and funding managers. Genre: `analytic`.

## Cadence and freshness

Event-dated Funded through prior business day. Scheduled and CTC-not-scheduled As-of 6:00 a.m.

## Headline KPIs

M-VOL-06 Funded units · M-VOL-07 Funded volume · M-CYC-02 / M-CYC-10 p50/p90 · M-CYC-17 · M-CYC-18 · M-AGE-07 · M-QLT-15 funding fail rate · M-QLT-14 (supporting) · M-CAP-01 (closer).

## Layout

1. KPI row.
2. CTC → docs out → signed → Funded funnel (counts, same week vs in-flight).
3. Cycle p50/p90 vs 5-day CTC-to-fund SLA.
4. Calendar: scheduled this week vs funded this week.
5. Funding fail reasons (top N).
6. Wholesale vs Retail split (Channel is on, Correspondent off).

## Visuals

Funnel with one-loan-once. Fail rate semantic up-bad. Volume $ is context next to units — do not color $ green independently of units.

## Filters

Global with default Channel = Retail + Wholesale. Closer, closing type (wet/hybrid/eClose), state.

## Drill path

Conditions still open → [D06](D06-underwriting-and-conditions.md). Title/CD → [D05](D05-title-escrow-closing-coord.md). After Funded → [D09](D09-post-closing-and-trailing-docs.md). Capacity → [D13](D13-capacity-and-productivity.md). If user turns Correspondent on, banner: “Use D08 for purchase; Funded metrics exclude Correspondent.”

## Grain and counting

Funded event only. Table-fund vs lender-fund: metric is company Funded. One file once.

## Empty / stale / partial

Wire-system fail events: if missing, show M-QLT-15 as unavailable, not zero.

## Out of scope

Correspondent purchase, investor delivery, servicing first-payment, lock desk.

## Questions this view answers

1. CTC-to-fund p50/p90 versus SLA, Retail vs Wholesale?
2. How many CTC files are unscheduled?
3. Docs-out-to-signed and signed-to-funded — where is the tail?
4. Funding fail rate and top reasons this week?
5. Scheduled this week versus actually Funded?
6. Units per closer FTE?
7. Did CTC revoke steal from this week’s Funded (M-QLT-14)?
8. eClose vs wet cycle difference?
