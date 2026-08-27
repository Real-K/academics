---
name: identification-tournament
description: Compare multiple empirical designs against the same estimand, red-team assumptions, and select or reject a primary identification strategy.
context: fork
agent: causal-identification-referee
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent
---

# Identification tournament

Generate at least three feasible routes when the problem permits, including a credible noncausal benchmark. For each route, score:

- source of variation and assignment mechanism;
- counterfactual quality;
- assumptions and institutional realism;
- anticipation, spillovers, composition, and measurement stability;
- estimator validity under timing and heterogeneity;
- power and overlap;
- data implementation cost;
- strongest falsification test;
- maximum defensible claim.

Have `causal-identification-referee` attack each route independently. Write the comparison and decision to `04_design/IDENTIFICATION_STRATEGY.md` and threats to `THREATS_TO_VALIDITY.md`. Select the simplest design that answers the estimand credibly. KILL causal framing when no route survives; preserve a valuable descriptive paper when appropriate.
