---
name: theory-to-hypotheses
description: Convert a finance mechanism into discriminating, falsifiable hypotheses with boundary conditions and competing explanations.
context: fork
agent: theory-hypothesis-architect
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Theory to hypotheses

1. Define actors, incentives, information, constraints, sequence of actions, and equilibrium/behavioral response.
2. Verify institutional and legal availability of the mechanism in the sample period.
3. Draw the mechanism chain in `03_theory/MECHANISM_MAP.md`.
4. For each hypothesis, record in `HYPOTHESIS_REGISTRY.csv`:
   - hypothesis ID and status;
   - theoretical source;
   - mechanism and sign/shape;
   - observable variables and timing;
   - boundary conditions;
   - competing mechanism and discriminating test;
   - falsifier;
   - planned analysis ID.
5. Update `CONCEPTUAL_MODEL.md` and the hypothesis budget.
6. Reject hypotheses that merely restate a coefficient sign or use post-hoc theory.

End with a coherence audit: hypotheses must jointly form one paper rather than a catalog of available outcomes.
