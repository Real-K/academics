---
name: create-paper
description: Create a new independent finance paper workspace from the standard skeleton, register it, and initialize its Wiki page.
argument-hint: "<working title> [--activate]"
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit
---

# Create a paper

Run:

```bash
python scripts/new_paper.py --title "$ARGUMENTS"
```

Then inspect the generated folder and complete these first, without inventing content:

- `00_admin/PAPER_CHARTER.md`
- `01_question/RESEARCH_QUESTION.md`
- `00_admin/KILL_CRITERIA.md`
- `00_admin/HYPOTHESIS_BUDGET.md`

Do not begin model estimation until the research-question and data-feasibility gates are passed. The command registers the paper but does not make it active unless `--activate` is provided.
