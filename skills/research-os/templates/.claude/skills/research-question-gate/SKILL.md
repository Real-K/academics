---
name: research-question-gate
description: Evaluate whether a proposed finance research question is important, answerable, distinct, falsifiable, and feasible before analysis begins.
context: fork
agent: research-director
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent
---

# Research-question gate

Use the `research-director`, `theory-hypothesis-architect`, `finance-domain-referee`, and `data-architect` perspectives.

## Required artifacts
- `01_question/RESEARCH_QUESTION.md`
- `01_question/CONTRIBUTION_MAP.md`
- `00_admin/KILL_CRITERIA.md`
- initial `00_admin/RISK_REGISTER.md`

## Tests
1. **Importance:** Which finance decision, theory, institution, or allocation problem changes if answered?
2. **Closest substitutes:** What are the three to five closest papers and why is this not replication-by-setting?
3. **Falsifiability:** What observable result weakens the central claim?
4. **Data feasibility:** Are unit, timing, variables, coverage, linkage, and sample size plausible?
5. **Identification route:** Is there at least one credible descriptive or causal estimand without pretending a design exists?
6. **Paper boundary:** Can the question be answered in one coherent paper?

Write a gate memo with PASS, CONDITIONAL PASS, PIVOT, or KILL. A pass requires explicit evidence, not enthusiasm.
