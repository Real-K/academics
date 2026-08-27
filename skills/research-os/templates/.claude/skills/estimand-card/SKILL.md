---
name: estimand-card
description: Define the exact target quantity, population, timing, treatment or exposure, contrast, outcome, and permitted interpretation before selecting an estimator.
context: fork
agent: econometrician
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Estimand card

Complete `01_question/ESTIMAND_CARD.md` before discussing models.

Required fields:
- scientific question and decision relevance;
- unit and target population;
- treatment/exposure and assignment time;
- comparison and counterfactual;
- outcome and measurement horizon;
- estimand in words and notation;
- aggregation/weighting;
- intercurrent events, attrition, and interference;
- identifying assumptions;
- estimator candidates and why each maps to the estimand;
- descriptive versus causal claim ceiling;
- falsification and sensitivity plan.

The card fails if the same words can map to materially different target quantities. Update it when the question changes; after freeze, changes require a deviation record.
