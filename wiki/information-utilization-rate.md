---
description: "In a 32-model agentic clinical benchmark, the fraction of available information an agent actually requests is the strongest measured predictor of accuracy, and it collapses in later rounds."
aliases: ["information utilization", "utilization rate", "information-seeking rate"]
sources: ["braitsch-2026"]
---
# Information utilization rate

> How much of the available evidence an agent bothers to ask for, before it
> commits — measured, and shown to predict whether it gets the answer right.

## Definition / Mechanism

In OncoRounds, an agentic benchmark of 32 frontier LLMs across 20 hematologic
oncology cases and three sequential rounds, information utilization is the
proportion of the round's available clinical data items the model actually
requests before committing to a diagnosis. Across all models and cases, the
utilization rate showed a strong positive correlation with overall diagnostic
accuracy — the single strongest predictor measured in the study, stronger
than model recency (R=0.51) or parameter count (R=0.45): "The utilization
rate (fraction of available clinical information actually obtained) showed a
strong positive correlation with overall accuracy (R = 0.69, p < 0.001 …),
indicating that models gathering more of the available information performed
better."[^c1]

Utilization is not stable across the interaction: it collapses in the final,
most decision-relevant round. "In R1, models obtained 56.8% of available
diagnostics, remaining similar in R2 (56.7%) before dropping to 25.7% in R3,
with several models requesting only 1–2 items in R3 before attempting to
solve, leaving molecular panels and treatment response data unexamined."[^c2]

## Why it matters

This is a direct, quantified link — in a real-stakes domain, not a toy task —
between an agent's willingness to keep opening constraint-slots (stall 2:
which axis next, and whether to ask again at all) and whether the final
answer is right. It is also evidence that the failure is not one of
capability at interpretation: reasoning-trace quality stayed high (91% above
a clinical-reasoning threshold) while utilization and accuracy fell together
in the same round, pointing at the selection/stopping step rather than at
reasoning per se.

## Limits

- Correlational: R=0.69 does not show that forcing more requests raises
  accuracy. A more capable model may both ask more and reason better for
  reasons the correlation does not separate.
- Single domain (hematologic oncology) and single benchmark (OncoRounds);
  `replicated: null` — no independent replication is cited.
- The denominator is a fixed, experimenter-defined list of "available" items
  per round; utilization does not weight items by how decision-relevant they
  are, so it cannot distinguish an agent that asks a lot of low-value
  questions from one that asks the few that matter.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]]

[^c1]: braitsch-2026 — "The utilization rate (fraction of available clinical information actually obtained) showed a strong positive correlation with overall accuracy (R = 0.69, p < 0.001, Supplementary Figure 1b), indicating that models gathering more of the available information performed better."
[^c2]: braitsch-2026 — "In R1, models obtained 56.8% of available diagnostics, remaining similar in R2 (56.7%) before dropping to 25.7% in R3, with several models requesting only 1–2 items in R3 before attempting to solve, leaving molecular panels and treatment response data unexamined."
