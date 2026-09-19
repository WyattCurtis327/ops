# D09 Post-closing and trailing documents

## Purpose and primary decision

Get Funded and Correspondent-purchased files ship-ready: trailing WIP by document type, aging, missing-trailer rate.

## Audience and genre

Post-close managers. Genre: `analytic`.

## Cadence and freshness

As-of 6:00 a.m. for WIP. Event-dated ship-ready and M-CYC-12 for files that completed.

## Headline KPIs

M-VOL-14 Post-close WIP · M-CYC-12 p50/p90 · M-QLT-12 at 10 and 15 business days · M-AGE-08 (p50 age of WIP) · M-CAP-01 (post-closer) · ship-ready not yet Delivered (gap to D10).

## Layout

1. KPI row.
2. WIP by Channel.
3. Missing document-type matrix (note, recorded instrument, final title, other trailers) × age band.
4. Waiting-on party (title vs TPO vs internal).
5. TPO trailing performance (Correspondent).
6. Completions vs new Funded/purchased (M-CAP-05 post-closer).

## Visuals

Document-type heatmap (missing × age). Recording-delay states should be sliceable by State so internal teams are not blamed for county recording.

## Filters

Global plus document type, Waiting-on party, TPO, state, investor.

## Drill path

Ship-ready → [D10](D10-investor-delivery.md). Quality of trailers → [D11](D11-manufacturing-quality.md). Capacity → [D13](D13-capacity-and-productivity.md).

## Grain and counting

Clock starts at Funded or Correspondent purchase, not at CTC. Required trailer set is product/investor specific; a generic checklist will inflate M-QLT-12 — call that out if the feed is generic.

## Empty / stale / partial

If imaging lags LOS, prefer imaging received-in for trailer-in. Banner if they disagree.

## Out of scope

Investor purchase economics, servicing customer statements, building a document-image app.

## Questions this view answers

1. How large is post-close WIP, by Channel?
2. Trailing cycle p50/p90 versus 15-day ASSUMED SLA?
3. Missing-trailer rate at day 10 and day 15?
4. Which document types dominate aging?
5. Is the wait on county recording, TPO, or internal?
6. Which TPOs are slow on trailers?
7. Ship-ready vs still not Delivered (P11 handoff)?
8. Are post-closer completions keeping up with new Funded/purchased arrivals?
