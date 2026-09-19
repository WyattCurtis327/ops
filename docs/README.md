# Operations reporting blueprint

This pack is the business requirements for enterprise Operations dashboards and reporting. It covers loan manufacturing across Retail, Wholesale, and Correspondent, from file start through investor delivery.

**Single-file copy (all sections concatenated):** [../Operations-Reporting-Requirements.md](../Operations-Reporting-Requirements.md). Refresh with `python _consolidate.py` from the repo root.

**Excel workbook:** [../Operations-Reporting-Requirements.xlsx](../Operations-Reporting-Requirements.xlsx). Refresh with `python _to_excel.py` from the repo root.

All files are under this repository. Project index: [../README.md](../README.md).

Read in this order:

1. [Approved plan](00-blueprint-plan.md) — locked scope, taxonomy, and file map.
2. [Domain glossary](../CONTEXT.md) — canonical terms. Use these names in every dashboard and metric.
3. [Scope and taxonomy](01-scope-and-taxonomy.md) — in/out of scope, channels, subcategories, personas, adjacent subject areas.
4. [Operating context](10-operating-context.md) — how Ops runs, systems of record, worked file examples, handoffs.
5. [Processes by subcategory](02-processes-by-subcategory.md) — how the work runs, including channel variants.
6. [Shared dimensions](03-shared-dimensions.md) — conformed slices for every enterprise view.
7. [Metric catalog](04-metric-catalog.md) — governed measures, grains, formulas, direction.
8. [Dashboard inventory](05-dashboard-inventory.md) — the fourteen-dashboard family and drill map.
9. [Dashboard specs](dashboards/) — one spec per dashboard (audience, KPIs, layout, filters, drills).
10. [Wireframe kit](wireframes/index.html) — clickable layouts **by department (P01–P15)**. Map: [wireframes/by-department.md](wireframes/by-department.md).
11. [Event dictionary](06-event-dictionary.md) — named timestamps the metrics require (data contract, no tables).
12. [Requirements traceability](07-requirements-traceability.md) — process → metric → dashboard → event.
13. [Phasing and open questions](08-phasing-and-open-questions.md) — MVP sequence and leadership decisions.
14. [User stories and NFRs](09-user-stories-and-nfr.md) — reporting epics and non-functional rules.
15. [Milestones and reason codes](11-milestones-and-reason-codes.md) — canonical stages, waiting-on, fallout, kickout, defects.
16. [How to use the numbers](12-how-to-use-the-numbers.md) — EXE driver tree, huddle agenda, alerts, staffing read.
17. [Anti-patterns, recon, and validation](13-anti-patterns-and-validation.md) — what not to ship; interview questions.
18. [Research sources](14-research-sources.md) — cited MBA, ICE, ACES, GSE, CFPB sources and pack implications.
19. [Pipeline phases](15-pipeline-phases.md) — each manufacturing phase with metrics and dimensions.
20. [Roles and actions](16-roles-and-actions.md) — who does what in each phase, by Channel.
21. [Gold layer data model](17-gold-layer-data-model.md) — facts, dimensions, metric views for every catalog metric.

## What this pack is not

- Not a Databricks build, metric-view YAML, or source-system map.
- Not Sales, Capital Markets, Servicing, or independent audit QC.
- SLA numbers labeled `ASSUMED SLA` are industry-typical placeholders, not company policy.

## Follow-on work

1. Close [open questions](08-phasing-and-open-questions.md) (especially Q1, Q3, Q4, Q6, Q9).
2. Map [event dictionary](06-event-dictionary.md) IDs to LOS / vendor / delivery tables.
3. Unity Catalog metric views from the [catalog](04-metric-catalog.md).
4. AI/BI dashboards in [phase order](08-phasing-and-open-questions.md) (D01/D02 first).
