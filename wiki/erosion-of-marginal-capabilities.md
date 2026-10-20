---
description: "In a multi-turn scientific-inquiry loop, an LLM agent's critical judgment on injected fake results degrades relative to its own decontextualized baseline as the interaction lengthens."
aliases: ["Erosion of Marginal Capabilities", "cognitive tunneling"]
sources: ["cui-2026"]
---
# Erosion of marginal capabilities

> A model's critical judgment is not a fixed capability it carries into a
> long interaction: measured in-loop it can fall below the same judgment
> measured in isolation, and the gap does not shrink as the trajectory
> grows.

## Definition / Mechanism

[[inquitree]] probes this by injecting **Fake Results**: at a Study→Result
transition the environment can stochastically return a plausible but
incorrect outcome that contradicts the source paper's ground truth,
controlled by an integer randomness level `a`. "We parameterize this by an
integer randomness level a, meaning a fake result is returned with
probability 10 ∗ a%."[^c1]

Cui (2026) names the resulting failure mode directly: "agents exhibit an
'Erosion of Marginal Capabilities': during long-horizon interactions, they
develop 'cognitive tunneling,' where critical judgment and anomaly
detection degrade relative to their intrinsic baselines."[^c2]

The degradation is not explained by miscalibrated caution alone: "As
randomness increases, models trigger redo study more often, yet their hit
rate on fake results can remain limited. Moreover, relative to a
decontextualized control where validity judgments are near chance,
performance can further degrade in the inquiry loop."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Agent evaluation (Cui 2026, the paper's own label) | Erosion of Marginal Capabilities | exact |
| Cognitive science (borrowed term, same paper) | cognitive tunneling | close — the mechanism the paper proposes for the erosion, not independently measured |

## Why it matters

Stall 2 asks which axis to probe next; this finding says the judgment
doing that choosing is itself a moving target across the interaction, not
a constant the selection policy can assume. It also bears on stall 7
(stopping): the same degraded judgment decides whether to redo a study or
draw a conclusion, so a stopping rule that trusts the agent's own
confidence is trusting a signal shown to erode with trajectory length.

## Limits

One benchmark, one domain (30 neuroscience papers, CNS-level venues), one
injection mechanism (Fake Results at a single randomness parameter); the
paper does not isolate context length from task complexity as the driver
of the degradation, so "long-horizon" and "harder cumulative task" are
confounded in this result.

## Related

[[inquitree]] · [[interpolation-extrapolation-boundary]] · [[sycophantic-capitulation]] · [[bounded-rationality]]

[^c1]: cui-2026 — "We parameterize this by an integer randomness level a, meaning a fake result is returned with probability 10 ∗ a%."
[^c2]: cui-2026
[^c3]: cui-2026
