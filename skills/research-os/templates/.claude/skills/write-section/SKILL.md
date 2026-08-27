---
name: write-section
description: Draft or revise a publication-quality English manuscript section from verified artifacts and the claims ledger.
argument-hint: "<section and objective>"
context: fork
agent: academic-writer
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Write a manuscript section

Argument: `$ARGUMENTS`

1. Identify the section's argumentative function and required inputs.
2. Read the claims ledger, relevant evidence map, design, and generated results.
3. Outline paragraph jobs before prose.
4. Draft in English with precise finance terminology and claim verbs permitted by the claim ceiling.
5. Keep citations attached to exact claims and numbers synchronized with generated artifacts.
6. Mark missing support as `[EVIDENCE REQUIRED]` and unresolved interpretation as `[INTERPRETATION OPEN]`.
7. Run a consistency pass for terminology, sample, dates, equations, tables, and cross-references.
8. Update the claims ledger for new or revised substantive claims.

Do not use generic significance language, inflated novelty, or unsupported causal transitions.

## Finance presentation norm (rule 10, PI directive 2026-08-15)
Manuscripts present the final logical structure: the adopted specification justified on data-structure and econometric grounds, with alternative designs reported as robustness or appendix analyses. Do not narrate design chronology, use preregistration vocabulary (preregistered, pre-analysis plan, post-result, outcome-blind, frozen, stopping rule), or write confession-style sentences about earlier designs. Never state or imply the adopted model was the only one considered. All findings — including imprecise and unfavorable ones — are still reported. Internal freezes, gates, deviation logs, and decision records remain mandatory and unchanged; they are inputs and replication-package material, not manuscript content.
