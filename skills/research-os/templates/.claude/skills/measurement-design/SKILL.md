---
name: measurement-design
description: Design and validate proxies for finance constructs, including event-clock and classification artifacts, before model estimation.
context: fork
agent: measurement-validity-referee
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Measurement design

For every focal construct, complete a measurement chain:
latent construct → institutional record → raw field → cleaning → operational measure → coefficient interpretation.

Audit undercoverage, contamination, misclassification, nonclassical error, strategic/endogenous reporting, timing mismatch, changing definitions, censoring, survivorship, and sample selection. Design at least one validation strategy where feasible: hand-coded gold sample, external benchmark, alternate proxy, simulation, negative control, confusion matrix, or temporal logic check.

Write `04_design/MEASUREMENT_VALIDITY.md`, update `05_data/CONSTRUCT_DICTIONARY.csv`, and register reusable constructs. State how each failure mode biases estimates and which claims remain valid. Do not proceed on a focal measure that has no interpretable mapping to the construct.
