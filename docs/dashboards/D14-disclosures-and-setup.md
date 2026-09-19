# D14 Disclosures and setup

## Purpose and primary decision

Hit TRID initial LE timing and a clean File start. **LE send clocks on this page are TRID general business days** (creditor-open days — Saturday counts only if the company is open). CD waiting period (P08) uses TRID specific business days. Correspondent is off by default (no company LE).

## Audience and genre

Disclosure desk and setup. Genre: `analytic`.

## Cadence and freshness

Event-dated LE sent and File start through prior general business day. In-flight eSign As-of 6:00 a.m.

## Headline KPIs

M-VOL-01 Files started · M-VOL-02 Applications taken · M-CYC-04 p50/p90 (**TRID general business days**) · M-REG-01 initial LE miss rate (share past 3 general business days) · M-QLT-04 Redisclosure rate · eSign incomplete count (Waiting-on borrower/Broker in setup).

## Layout

1. Header callout: **Initial LE send = 3 general business days (creditor-open). Not all calendar days. CD wait = specific business days (Sat yes, Sun/federal holiday no).**
2. KPI row.
3. Distribution of general business days to initial LE vs 3-day line.
4. File start vs application taken (setup lag, business days — labeled).
5. Redisclosure rate trend and reason mix if captured.
6. eSign WIP.
7. Wholesale vs Retail.

## Visuals

Histogram of general business days to LE with a line at 3. Miss rate up-bad. Redisclosure is context (some change is legitimate).

## Filters

Default Channel = Retail + Wholesale. Date range, product, team, LO/Broker, state.

## Drill path

Files started → [D02](D02-pipeline-and-aging.md) / [D03](D03-processing.md). Redisclosure tied to fees/title → [D05](D05-title-escrow-closing-coord.md). If user enables Correspondent, banner: “Correspondent has no company LE; use D08 intake.”

## Grain and counting

M-CYC-04 start is TRID application date unless company policy is intent-to-proceed; the tile must name which. Redisclosure ≠ initial LE. Correspondent must not increment M-VOL-02.

## Empty / stale / partial

If eSign vendor events do not land in LOS, hide eSign WIP rather than show 0. If TRID application date is missing, exclude from M-CYC-04 and banner the exclusion count.

## Out of scope

Closing Disclosure timing as a TRID legal dashboard (CD operational timing is noted on D07, not a second compliance system of record here), lock desk, Sales leads.

## Questions this view answers

1. What share of files missed the 3-calendar-day initial LE clock this week?
2. What is p50/p90 general business days to LE, Retail vs Wholesale?
3. How many applications are not yet File start (setup lag)?
4. Redisclosure rate — rising with a product or team?
5. How many files are stuck on eSign?
6. Did File start volume move WoW by Channel?
7. Are Wholesale registrations creating File start without a company LE when the company is creditor (data-quality check)?
8. How many files were excluded from the LE clock for missing TRID application date?
