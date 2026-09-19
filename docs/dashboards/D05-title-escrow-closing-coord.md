# D05 Title, escrow, and closing coordination

## Purpose and primary decision

Clear title in time for CTC and a scheduled closing: commitment turn, curative, HOA/payoff waits, CD figures. Funding itself is D07.

## Audience and genre

Title desk and closing managers. Genre: `analytic`.

## Cadence and freshness

Daily event-dated; open commitment/curative As-of 6:00 a.m.

## Headline KPIs

M-CYC-09 p50/p90 · M-CYC-09A p50 · M-QLT-06 curative rate · M-VEN-03 (title on-time %) · files waiting-on title/HOA (M-AGE-05 filtered) · M-AGE-07 as a supporting tile (CTC not scheduled — coordination failure).

## Layout

1. KPI row.
2. Commitment cycle by title company and state.
3. Open curative list aging (counts, not a LOS replacement).
4. Waiting-on mix for title-related blocks (Vendor vs HOA vs internal).
5. Correspondent panel: package review turn, not new orders.
6. Closing-type mix (wet / hybrid / eClose) as context for D07.

## Visuals

p50/p90 vs 5-day SLA. Curative rate is context (some markets are high). On-time % semantic (up good).

## Filters

Global plus Vendor name (title), state, closing type, Waiting-on party.

## Drill path

Vendor rank → [D12](D12-vendor-performance.md). CTC not scheduled → [D07](D07-closing-and-funding.md). Processing wait → [D03](D03-processing.md).

## Grain and counting

Order grain for M-CYC-09. Broker-opened title: received-to-commitment if order date missing, labeled. Correspondent: review only.

## Empty / stale / partial

If curative never closed in LOS, banner overstated open curative.

## Out of scope

Post-fund recording (D09), wire (D07), legal spend.

## Questions this view answers

1. Commitment p50/p90 versus SLA by title company and state?
2. What share of files opened curative, and how old is open curative?
3. How many files are CTC-blocked on title vs HOA vs payoff?
4. How many CTCs have no schedule?
5. Is eClose mix changing cycle time?
6. Which states are the tail (p90)?
7. Correspondent title-review turn?
8. Title on-time % trend WoW?
