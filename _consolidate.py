"""One-off: merge ops markdown artifacts into a single requirements document."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
OUT = ROOT / "Operations-Reporting-Requirements.md"

FRONT = """# Operations subject area — enterprise dashboard and reporting requirements

**Document type:** Business requirements (single-file consolidation)  
**Subject area:** Operations (loan manufacturing) at a multi-channel non-bank mortgage company  
**Channels:** Retail, Wholesale, Correspondent  
**Lifecycle:** File start / intake through post-closing, trailing documents, and investor delivery  
**Status:** Working requirements. `ASSUMED SLA` is not company policy.  
**Companion (not inlined):** interactive wireframe kit at `docs/wireframes/index.html`

This file consolidates the Operations reporting blueprint: glossary, scope, operating context, pipeline phases, roles, processes, metrics, dimensions, events, dashboards, stories, phasing, anti-patterns, and research sources.

**Reporting principles (non-negotiable)**

1. Never mix Funded, Correspondent purchase, and Investor purchase in one unlabeled “funded” number.
2. Cycle time is p50 and p90, not average alone.
3. Pull-through is a named cohort (start month, lock month, or submission month).
4. As-of Pipeline and event-dated Funded are different questions; label the time basis.
5. Waiting-on party is a first-class aging slice.
6. Initial Loan Estimate **send** uses TRID **general business days** (creditor-open). Closing Disclosure wait uses TRID **specific business days**.
7. Missing events render **unavailable**, not zero.

"""

PARTS: list[tuple[str, Path]] = [
    ("1. Glossary", ROOT / "CONTEXT.md"),
    ("2. Scope and taxonomy", DOCS / "01-scope-and-taxonomy.md"),
    ("3. Operating context", DOCS / "10-operating-context.md"),
    ("4. Pipeline phases, metrics, and dimensions", DOCS / "15-pipeline-phases.md"),
    ("5. Job roles and actions by phase", DOCS / "16-roles-and-actions.md"),
    ("6. Processes by subcategory", DOCS / "02-processes-by-subcategory.md"),
    ("7. Milestones and reason codes", DOCS / "11-milestones-and-reason-codes.md"),
    ("8. Shared dimensions", DOCS / "03-shared-dimensions.md"),
    ("9. Metric catalog", DOCS / "04-metric-catalog.md"),
    ("10. Event dictionary", DOCS / "06-event-dictionary.md"),
    ("11. Requirements traceability", DOCS / "07-requirements-traceability.md"),
    ("12. Dashboard inventory", DOCS / "05-dashboard-inventory.md"),
]

DASH_DIR = DOCS / "dashboards"
DASH_ORDER = [
    "D01-ops-command-center.md",
    "D02-pipeline-and-aging.md",
    "D03-processing.md",
    "D04-appraisal-and-valuation.md",
    "D05-title-escrow-closing-coord.md",
    "D06-underwriting-and-conditions.md",
    "D07-closing-and-funding.md",
    "D08-correspondent-operations.md",
    "D09-post-closing-and-trailing-docs.md",
    "D10-investor-delivery.md",
    "D11-manufacturing-quality.md",
    "D12-vendor-performance.md",
    "D13-capacity-and-productivity.md",
    "D14-disclosures-and-setup.md",
]

AFTER_DASH: list[tuple[str, Path]] = [
    ("14. Wireframes by department", DOCS / "wireframes" / "by-department.md"),
    ("15. User stories and non-functional requirements", DOCS / "09-user-stories-and-nfr.md"),
    ("16. How to use the numbers", DOCS / "12-how-to-use-the-numbers.md"),
    ("17. Anti-patterns, recon, and validation", DOCS / "13-anti-patterns-and-validation.md"),
    ("18. Phasing and open questions", DOCS / "08-phasing-and-open-questions.md"),
    ("19. Research sources", DOCS / "14-research-sources.md"),
]


def demote_headings(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.startswith("#"):
            hashes = len(line) - len(line.lstrip("#"))
            rest = line[hashes:]
            hashes = min(hashes + 1, 6)
            line = "#" * hashes + rest
        out.append(line)
    return "\n".join(out)


def rewrite_links(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        label, url = m.group(1), m.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if "wireframes/index.html" in url.replace("\\", "/"):
            return f"{label} (see `docs/wireframes/index.html`)"
        return label

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def strip_leading_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines)


def body(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    raw = strip_leading_h1(raw)
    raw = rewrite_links(raw)
    return demote_headings(raw).strip() + "\n"


def main() -> None:
    chunks: list[str] = [FRONT]
    toc = ["## Contents\n"]
    for title, _ in PARTS:
        toc.append(f"- {title}")
    toc.append("- 13. Dashboard specifications (D01–D14)")
    for title, _ in AFTER_DASH:
        toc.append(f"- {title}")
    toc.append("")
    chunks.append("\n".join(toc))

    for title, path in PARTS:
        if not path.exists():
            raise SystemExit(f"missing {path}")
        chunks.append(f"\n---\n\n## {title}\n\n")
        chunks.append(body(path))

    chunks.append("\n---\n\n## 13. Dashboard specifications (D01–D14)\n\n")
    chunks.append(
        "Each specification is the reporting contract for one dashboard: audience, KPIs, layout, filters, drills, grain, and empty/stale rules. Interactive layouts: `docs/wireframes/index.html` (organized by department P01–P15 plus EXE).\n"
    )
    for name in DASH_ORDER:
        path = DASH_DIR / name
        if not path.exists():
            raise SystemExit(f"missing {path}")
        chunks.append(f"\n### {name.replace('.md', '')}\n\n")
        chunks.append(body(path))

    wf_note = """
Interactive HTML/CSS kit (not duplicated here as HTML):

- Open `docs/wireframes/index.html` in a browser.
- Navigation is by Operations department (P01–P15) plus EXE Command Center.
- Visual system: stratified KPI tiles, IBCS-style actual/SLA/forecast marks, no gauges.
- Sample numbers only.
"""
    chunks.append(wf_note)

    for title, path in AFTER_DASH:
        if not path.exists():
            raise SystemExit(f"missing {path}")
        chunks.append(f"\n---\n\n## {title}\n\n")
        chunks.append(body(path))

    chunks.append(
        """
---

## Source files

This document was generated from the modular pack in this repository (`CONTEXT.md` and `docs/`). The modular files remain for editing. If they diverge, treat **this file** as the review copy leadership asked for, then refresh it from the modules.

Wireframe implementation files not inlined: `docs/wireframes/index.html`, `docs/wireframes/wireframe.css`.
"""
    )

    text = "".join(chunks)
    # collapse extra blank runs
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(text):,} chars, {text.count(chr(10))+1} lines)")


if __name__ == "__main__":
    main()
