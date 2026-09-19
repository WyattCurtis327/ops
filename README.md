# Operations reporting blueprint

Enterprise Operations dashboard and reporting requirements for a multi-channel non-bank mortgage company (Retail, Wholesale, Correspondent). Loan manufacturing from file start through investor delivery.

All deliverables live in this repository. Interactive wireframes: [docs/wireframes/index.html](docs/wireframes/index.html).

## Open first

| What | Path |
|------|------|
| **Single requirements document** | [Operations-Reporting-Requirements.md](Operations-Reporting-Requirements.md) |
| **Excel workbook** | [Operations-Reporting-Requirements.xlsx](Operations-Reporting-Requirements.xlsx) |
| This index | [README.md](README.md) |
| Domain glossary | [CONTEXT.md](CONTEXT.md) |
| How to read the pack | [docs/README.md](docs/README.md) |
| Clickable wireframes by department | [docs/wireframes/index.html](docs/wireframes/index.html) |
| Operating context (how Ops runs) | [docs/10-operating-context.md](docs/10-operating-context.md) |
| Milestones and reason codes | [docs/11-milestones-and-reason-codes.md](docs/11-milestones-and-reason-codes.md) |
| How to use the numbers | [docs/12-how-to-use-the-numbers.md](docs/12-how-to-use-the-numbers.md) |
| Research sources | [docs/14-research-sources.md](docs/14-research-sources.md) |
| Pipeline phases (metrics × dimensions) | [docs/15-pipeline-phases.md](docs/15-pipeline-phases.md) |
| Roles and actions by phase | [docs/16-roles-and-actions.md](docs/16-roles-and-actions.md) |
| Gold layer data model | [docs/17-gold-layer-data-model.md](docs/17-gold-layer-data-model.md) |

## Inventory

```
ops/
  README.md                          ← you are here
  CONTEXT.md                         ← glossary
  docs/
    00-blueprint-plan.md             ← approved plan (copy of the working spec)
    README.md
    01-scope-and-taxonomy.md
    10-operating-context.md          ← how Ops runs, systems, worked files
    02-processes-by-subcategory.md
    03-shared-dimensions.md
    04-metric-catalog.md
    05-dashboard-inventory.md
    06-event-dictionary.md
    07-requirements-traceability.md
    08-phasing-and-open-questions.md
    09-user-stories-and-nfr.md
    11-milestones-and-reason-codes.md
    12-how-to-use-the-numbers.md     ← driver tree, huddles, alerts
    13-anti-patterns-and-validation.md
    14-research-sources.md           ← cited industry/GSE/CFPB sources
    15-pipeline-phases.md            ← phase → metrics → dimensions
    16-roles-and-actions.md          ← who does what in each phase
    dashboards/                      ← D01–D14 specs
    wireframes/
      index.html                     ← open in a browser
      wireframe.css
      README.md
      by-department.md               ← P01–P15 map
```

## Wireframes by department

Open `docs/wireframes/index.html`. Navigation is P01–P15 (desks) plus EXE (command center). Map: [docs/wireframes/by-department.md](docs/wireframes/by-department.md).
