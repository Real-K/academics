---
name: pre-analysis-freeze
description: Validate and cryptographically freeze the primary design, hypotheses, measures, sample rules, models, inference, and claim ceiling before confirmatory estimation.
argument-hint: "<paper_id>"
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash
---

# Pre-analysis freeze

Before freezing, require completed and internally consistent:
- `ESTIMAND_CARD.md`;
- hypothesis registry and mechanism map;
- identification and measurement-validity memos;
- data manifest, construct dictionary, and sample rules;
- `PRE_ANALYSIS_PLAN.md` and `SPECIFICATION_GRID.yaml`;
- power/precision assessment;
- kill criteria and planned robustness matrix.

Run specialist reviews and resolve blocking issues. Then execute:

```bash
python scripts/freeze_paper.py --paper $ARGUMENTS
```

The command writes a hash manifest and lock. Afterward, changes to protected design files must use `unfreeze_paper.py --reason ...`, which records a deviation. A freeze is not proof of design quality; it is a commitment and audit boundary.

**Scope (rule 10):** the freeze is an *internal* audit boundary governing analysis conduct and the project record. It creates no obligation to narrate design chronology, preregistration status, or gate outcomes in the manuscript; finance manuscripts present the final specification on its merits. Freeze discipline itself is unchanged.
