# D10 Investor delivery

## Purpose and primary decision

Deliver ship-ready loans and reach Investor purchase. Separate **Delivered** from **Investor purchased**. Manage suspense and Kickouts.

## Audience and genre

Shipping/delivery managers. Genre: `analytic`.

## Cadence and freshness

Event-dated Delivered and Investor purchase. Delivered-not-purchased As-of 6:00 a.m.

## Headline KPIs

M-VOL-11 Delivered units · M-VOL-12 Investor purchased units · M-VOL-14 (inflow) · M-CYC-13 p50/p90 · M-CYC-14 p50/p90 · M-AGE-09 · M-QLT-10 Kickout rate · M-QLT-11 reason mix (headline: top reason).

## Layout

1. KPI row — tiles named Delivered and Investor purchased, never “sold” or “funded.”
2. Funnel: ship-ready → Delivered → Investor purchase; Kickout branch.
3. Aging of Delivered not purchased by investor.
4. Kickout rate and reason mix by investor and Channel.
5. Cycle from Funded/purchase to Delivered vs from Delivered to Investor purchase (two clocks).
6. Channel split (Corr vs R/W) without renaming purchase events.

## Visuals

Two-clock cycle chart. Kickout up-bad. Do not treat Delivered as success if M-AGE-09 is growing.

## Filters

Global plus investor, commitment, Kickout reason, Channel.

## Drill path

Kickout reasons / defects → [D11](D11-manufacturing-quality.md). Trailing incomplete → [D09](D09-post-closing-and-trailing-docs.md). Command Center Kickout tile lands here first.

## Grain and counting

Delivered ≠ Investor purchase. Kickout is not Fallout. Redelivery after Kickout: one Delivered event per attempt if the system stamps them — catalog file-level Kickout rate uses files Delivered in the cohort with ≥1 Kickout, so redelivery does not inflate the denominator twice. State that on the dashboard footnote.

## Empty / stale / partial

If purchase advice lags, M-VOL-12 will trail; banner expected lag by investor if known. Do not backfill Delivered as purchased.

## Out of scope

Gain-on-sale, hedge, pool creation (Capital Markets), servicing.

## Questions this view answers

1. Delivered units vs Investor purchased units this week?
2. How many files are Delivered but not purchased, and how old, by investor?
3. Kickout rate and top reasons by investor and Channel?
4. Is delay in P11 (ship-ready to Delivered) or at the investor (M-CYC-14)?
5. Are Correspondent Kickouts worse than Retail/Wholesale?
6. Which commitments are concentrating suspense?
7. Did Kickout rate move WoW?
8. Is post-close WIP converting to Delivered (link M-VOL-14)?
