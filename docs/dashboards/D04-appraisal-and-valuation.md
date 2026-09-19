# D04 Appraisal and valuation

## Purpose and primary decision

Keep valuation off the CTC critical path: order-to-report, review, waivers, ROV, and AMC on-time. Correspondent is mostly review/transfer, not new orders.

## Audience and genre

Appraisal desk. Genre: `analytic`. Order grain for cycles; file grain for waiver rate.

## Cadence and freshness

Daily event-dated orders and reports. Open-order aging As-of 6:00 a.m.

## Headline KPIs

M-CYC-08 p50/p90 · M-CYC-08A p50 · M-VEN-03 (AMC on-time %) · M-VOL-15 waiver rate · M-QLT-05 revision/ROV rate · M-VEN-01 open vs completed · open orders past SLA (order-grain analog of M-AGE-03).

## Layout

1. KPI row.
2. Cycle p50/p90 by AMC and by state.
3. Path mix: company-ordered, Broker-ordered, transferred, waived, seller (Corr).
4. ROV/revision trend.
5. Correspondent panel: review cycle M-CYC-08A only (no fake order-to-report).
6. Table: AMCs by volume, on-time %, p90, revision rate.

## Visuals

Bar p90 by Vendor (honest scale from 0). Waiver rate is context, not green-by-default (waivers can be good for cycle and bad if CU later fails — do not color).

## Filters

Global plus Vendor name, Vendor type (AMC/appraiser), state, appraisal path, property type.

## Drill path

Vendor table → [D12](D12-vendor-performance.md). Files blocked in processing on appraisal → [D03](D03-processing.md). Value defects → [D11](D11-manufacturing-quality.md).

## Grain and counting

Waivers excluded from M-CYC-08. Broker-ordered: clock from received-in if order placed is missing; label **received-to-report**. Seller appraisals (Corr) never enter M-CYC-08.

## Empty / stale / partial

If AMC portal lag, mark report-in stale. Empty states with no orders omitted from Vendor rank but not from state SLA if they have open files.

## Out of scope

Appraiser licensing HR, AMC contract legal, CU as a Capital Markets hedge tool.

## Questions this view answers

1. What is order-to-report p50/p90 versus 7-day ASSUMED SLA?
2. Which AMCs and states miss on-time %?
3. What share of files used a waiver, by Channel and product?
4. Is ROV/revision rising?
5. How many open orders are past SLA?
6. What is Correspondent review turn (no new order)?
7. Are Broker-ordered transfers slower than company orders?
8. Is volume concentrated in one AMC (preview of M-VEN-06)?
