---
description: "A conditional-mutual-information metric, κ = I(s;θ|b_t), measuring how tightly two uncertainty sources are coupled, that triggers active querying once coupling crosses a threshold."
aliases: ["Compound Uncertainty Coefficient", "kappa (κ)"]
sources: ["banerjee-2026"]
---
# Compound Uncertainty Coefficient

## Definition / Mechanism

Banerjee & Goan (2026) define the [[epistemic-trap|Compound Uncertainty]]
Coefficient as the conditional [[mutual-information|mutual information]] between an agent's state
$s$ and its dynamics parameter $\theta$, given its current joint belief
$b_t$: "We formalize this metric as the Compound Uncertainty Coefficient
(κ): κ = I (s; θ | bt )".[^c1]

κ partitions the agent's regime into three bands with two calibrated
thresholds. Below the low threshold, "uncertainties act as independent
noise terms, solvable by standard robust or POMDP modules"; above the high
threshold, "the transition function becomes fundamentally unidentifiable
from passive observations. This signals that passive observation strategies
will fail" — the paper's operational marker for when to stop asking
passively (waiting on natural variation) and start probing.[^c2]

Because the joint belief $b_t(s,\theta)$ is intractable to maintain exactly
in continuous systems, the paper derives a tractable upper-bound proxy from
the [[entropy]] [[chain-rule|chain rule]] and reports it validated against the exact ordering
on their benchmark: "I (s; θ | bt ) ≈ κ = σθ + σs", where $\sigma_\theta$ is
a normalized dynamics-prediction-ensemble disagreement and $\sigma_s$ a
state-observability deficit.[^c3]

## Why it matters

On stall 2, κ gives axis coupling a number: rather than scoring each
candidate uncertainty axis for its own [[expected-information-gain|expected information gain]], κ prices
the *joint* unidentifiability between two axes and uses that price as the
switch that decides whether they must be resolved together. This is a
different selection object than a per-axis criterion like EIG or VoI — it
answers "are these two axes separable at all" before either is asked about.

## Transfer

| | |
|---|---|
| Home field | Information theory (conditional mutual information) via safety-critical RL |
| Here | A trigger for switching a question-asking policy from passive to active, scored per pair of uncertainty axes rather than per axis |
| Survives | Conditional MI as a coupling measure between two uncertainty sources; monotone thresholds separating "independently resolvable" from "must be jointly probed" |
| Does not survive | The tractable proxy (Gaussian-ensemble disagreement plus an observability-deficit term) is fit to continuous-control state/dynamics variables; it has no established analogue for discrete question sets or natural-language uncertainty axes |

## Limits

The thresholds $\tau_{low}, \tau_{high}$ are calibrated per-domain from the
baseline and isolated-stressor κ distributions on one benchmark (Walker2D),
so the specific values are not portable; the proxy's monotonicity argument
rests on assumptions of isotropic Gaussian posteriors and monotone
co-variation that the paper states but does not test outside this domain.

## Related

- [[epistemic-trap]]
- [[mutual-information]]
- [[expected-information-gain]]
- [[value-of-information]]

[^c1]: banerjee-2026 — "We formalize this metric as the Compound Uncertainty Coefficient (κ): κ = I (s; θ | bt )"
[^c2]: banerjee-2026 — "uncertainties act as independent noise terms, solvable by standard robust or POMDP modules"
[^c3]: banerjee-2026 — "I (s; θ | bt ) ≈ κ = σθ + σs"
