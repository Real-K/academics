---
name: literature-map
description: Build a verified, source-linked map of the closest finance literature and identify the precise theoretical, measurement, or identification gap.
argument-hint: "[topic or paper_id]"
context: fork
agent: literature-evidence-auditor
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Literature map

1. Define concepts, aliases, neighboring fields, date range, sources, and inclusion/exclusion criteria in `02_literature/SEARCH_PROTOCOL.md`.
2. Search the existing shared library and Wiki before external discovery.
3. Verify each retained source and populate `LITERATURE_MATRIX.csv` with question, theory, data, design, finding, limitation, and relation to this paper.
4. Build `EVIDENCE_MAP.md` around claims and disagreements; do not write an annotated bibliography narrative.
5. Construct `GAP_MAP.md` with four columns: claimed gap, closest substitute, residual difference, contribution type.
6. Add source registry and Wiki notes with provenance.
7. Run a novelty attack: search alternate terminology and adjacent literatures.

Output a ranked list of closest papers and one defensible gap statement. Mark unresolved access or verification as pending.
