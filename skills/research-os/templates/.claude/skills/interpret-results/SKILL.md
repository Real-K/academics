---
name: interpret-results
description: Interpret verified estimates in economic and statistical terms, test mechanisms without overclaiming, and set the paper claim ceiling.
context: fork
agent: research-director
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent
---

# Interpret results

1. Use only registered, reproducible run outputs.
2. State the estimand, effect size, unit, uncertainty interval, baseline scale, and economically meaningful benchmark.
3. Distinguish statistical uncertainty, design uncertainty, measurement uncertainty, and external-validity uncertainty.
4. Evaluate whether results discriminate the focal mechanism from alternatives; heterogeneity alone is not mechanism proof.
5. Explain nulls using power and precision rather than binary significance language.
6. Reconcile contradictions and specification sensitivity.
7. Update the claims ledger with evidence IDs, run IDs, permitted verbs, and caveats.
8. Set a claim ceiling: descriptive association, predictive relation, local causal effect, mechanism-consistent evidence, or broader theoretical implication.

Do not draft conclusions before this audit is complete.

## Finance presentation norm (rule 10, PI directive 2026-08-15)
Manuscripts present the final logical structure: the adopted specification justified on data-structure and econometric grounds, with alternative designs reported as robustness or appendix analyses. Do not narrate design chronology, use preregistration vocabulary (preregistered, pre-analysis plan, post-result, outcome-blind, frozen, stopping rule), or write confession-style sentences about earlier designs. Never state or imply the adopted model was the only one considered. All findings — including imprecise and unfavorable ones — are still reported. Internal freezes, gates, deviation logs, and decision records remain mandatory and unchanged; they are inputs and replication-package material, not manuscript content.
