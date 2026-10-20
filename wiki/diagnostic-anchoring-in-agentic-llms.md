---
description: "LLM diagnostic agents keep an incorrect first-round diagnosis more often than they keep a correct one, and the drift is at the level of diagnostic resolution, not disease category."
aliases: ["diagnostic anchoring", "anchoring bias"]
sources: ["braitsch-2026"]
---
# Diagnostic anchoring in agentic LLMs

> Once a model commits to a first-round diagnosis, its later questions and
> conclusions keep orbiting that guess — measured as an asymmetry in how
> often the guess is corrected versus how often it decays.

## Definition / Mechanism

Across 630 model-case pairs with complete round-1 (R1) and round-3 (R3)
diagnoses in the OncoRounds benchmark, incorrect early diagnoses persisted
far more than correct ones degraded: "Of 323 pairs with an incorrect or
partially correct R1 diagnosis, 212 (65.6%) remained incorrect through R3,
yielding a [[recovery-postulate|recovery]] rate of 34.4%. Conversely, of 307 pairs with a correct R1
diagnosis, 156 (50.8%) deteriorated to incorrect or partially correct by
R3."[^c1]

The drift is not a change of disease category but a failure to refine within
it: "Models did not anchor on incorrect disease categories but on an initial
level of diagnostic resolution and failed to update toward the molecular
precision that later-round evidence demanded." Models kept the correct broad
label (e.g. "AML") while failing to integrate the molecular subtype, WHO
classification, or treatment-refractory status that arrived in R3.[^c2]

This trajectory-level pattern matched an independent annotation of reasoning
traces for the named cognitive bias: "Anchoring bias, the most frequent
cognitive bias, appeared across multiple models, consistent with the
diagnostic anchoring observed in the round-level trajectory analysis."[^c3]

## Why it matters

For stall 2, anchoring is a mechanism for *why* an agent keeps asking within
one diagnostic branch instead of switching to the axis that would falsify its
initial guess: once $W$ is provisionally narrowed to a category, later
questions concentrate inside that category rather than testing it, so the
selection step keeps shrinking the wrong sub-space of $W$.

## Limits

- The paper measures diagnosis persistence, not which questions were asked
  next; the claim that anchoring redirects axis-selection specifically (not
  just the final answer) is this wiki's inference from the mechanism, not a
  measurement in the source.
- Case-level variance is large: one case showed 0% deterioration among 30
  correct-R1 models, another 89.7%. Anchoring's strength may depend on how
  much the case's diagnosis changes character between rounds, not on a fixed
  model property.
- Single benchmark, single domain; `replicated: null`.

## Related

[[information-utilization-rate]] · [[bounded-rationality]] · [[value-of-information]]

[^c1]: braitsch-2026 — "Of 323 pairs with an incorrect or partially correct R1 diagnosis, 212 (65.6%) remained incorrect through R3, yielding a recovery rate of 34.4%. Conversely, of 307 pairs with a correct R1 diagnosis, 156 (50.8%) deteriorated to incorrect or partially correct by R3."
[^c2]: braitsch-2026 — "Models did not anchor on incorrect disease categories but on an initial level of diagnostic resolution and failed to update toward the molecular precision that later-round evidence demanded."
[^c3]: braitsch-2026 — "Anchoring bias, the most frequent cognitive bias, appeared across multiple models, consistent with the diagnostic anchoring observed in the round-level trajectory analysis."
