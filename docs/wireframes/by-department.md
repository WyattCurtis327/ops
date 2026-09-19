# Wireframes by Operations department

The kit is organized by **subcategory (P01–P15)** and department owner, not by dashboard ID. Open [index.html](index.html) — home is the department directory.

Enterprise Command Center is not a department. It rolls the desks up. Insurance/MI (P05) has no D15; it is still a department wireframe because the work is real.

## Map

| Dept / subcategory | Owner | Wireframe | Ships as | Primary question |
|--------------------|-------|-----------|----------|------------------|
| Enterprise glance | COO / Ops VP | [EXE](index.html#EXE) | D01 | On-time, on-capacity, converting pipeline? |
| P15 Pipeline control | Ops leadership | [P15](index.html#P15) | D02 | Where is WIP, how old, who waits, 7/14/30? |
| P14 Capacity | Ops leadership / workforce | [P14](index.html#P14) | D13 | Do FTE match arrivals and queues? |
| P01 Disclosure and file setup | Disclosure desk | [P01](index.html#P01) | D14 | 3-calendar-day LE and clean File start? |
| P02 Processing | Processor / team lead | [P02](index.html#P02) | D03 | File-complete turn, queue, waiting-on? |
| P03 Appraisal and valuation | Appraisal desk | [P03](index.html#P03) | D04 | Order-to-report, waiver, ROV, AMC on-time? |
| P04 Title, escrow, curative | Title desk | [P04](index.html#P04) | D05 | Commitment, curative, CTC not scheduled? |
| P05 Insurance and MI | Processor / MI desk | [P05](index.html#P05) | Strip on D03/D05/D06 (no D15) | HOI / flood / MI blocking CTC? |
| P06 Underwriting | Underwriter | [P06](index.html#P06) | D06 (UW slice) | First-decision turn and Suspense? |
| P07 Conditions and CTC | Processor + UW | [P07](index.html#P07) | D06 (conditions slice) | Conditions, CTC, revoke, rework? |
| P08 Closing and funding | Closer / funding | [P08](index.html#P08) | D07 | CTC to Funded (Retail/Wholesale only)? |
| P09 Correspondent intake | Correspondent ops | [P09](index.html#P09) | D08 | Submission to purchase by TPO? |
| P10 Post-closing | Post-close | [P10](index.html#P10) | D09 | Trailing WIP ship-ready? |
| P11 Investor delivery | Shipping / delivery | [P11](index.html#P11) | D10 | Delivered vs investor purchased? |
| P12 Manufacturing quality | QC (ops) | [P12](index.html#P12) | D11 | Defects and kickouts (not audit QC)? |
| P13 Vendor management | Vendor management | [P13](index.html#P13) | D12 | AMC/title on-time, concentration? |

## Shared screens (not a second owner)

- **D06** is one shipped dashboard with two department wireframes (P06 and P07) so UW and conditions managers each see their decision first.
- **P05** does not get a 15th enterprise dashboard. Production places its tiles on processing, title, and UW. The P05 page is the department contract.
- **P09** is the only Correspondent manufacturing spine. Other desks slice Channel = Correspondent; they do not clone Retail “Funded.”

## Lifecycle order (how to walk the kit)

Retail/Wholesale: P01 → P02 → P03/P04/P05 → P06 → P07 → P08 → P10 → P11  
Correspondent: P09 → P10 → P11  
Always available: EXE, P15, P14, P12, P13
