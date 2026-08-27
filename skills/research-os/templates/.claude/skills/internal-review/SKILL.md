---
name: internal-review
description: Run an editor-and-referee simulation with independent methodology, domain, identification, measurement, reproducibility, and writing assessments.
context: fork
agent: research-director
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, Agent
---

# Internal review

Freeze the submitted draft snapshot, then commission non-overlapping reviews:
- finance-domain contribution;
- econometric and identification credibility;
- measurement validity;
- statistical/reproducibility audit;
- writing and claim consistency;
- devil's-advocate premise attack.

Each reviewer must classify issues as fatal, major, minor, or optional and cite artifact locators. The research director constructs `09_review/REVIEW_MATRIX.csv`, resolves conflicts by evidence and severity, and issues an editorial recommendation: READY, MINOR, MAJOR, REFRAME, or KILL.

Do not let reviewers silently edit the manuscript during assessment. Revisions require a response matrix linking every change or reasoned disagreement to evidence.

## Finance presentation norm (rule 10, PI directive 2026-08-15)
Manuscripts present the final logical structure: the adopted specification justified on data-structure and econometric grounds, with alternative designs reported as robustness or appendix analyses. Do not narrate design chronology, use preregistration vocabulary (preregistered, pre-analysis plan, post-result, outcome-blind, frozen, stopping rule), or write confession-style sentences about earlier designs. Never state or imply the adopted model was the only one considered. All findings — including imprecise and unfavorable ones — are still reported. Internal freezes, gates, deviation logs, and decision records remain mandatory and unchanged; they are inputs and replication-package material, not manuscript content.
