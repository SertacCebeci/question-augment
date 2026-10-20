---
description: "Coupled state/dynamics uncertainty in RL causes super-additive failure — a measured 77% collapse against a 46% additive prediction — so coupled axes cannot be queried independently."
aliases: ["Epistemic Trap", "compound uncertainty"]
sources: ["banerjee-2026"]
---
# Epistemic Trap

## Statement

When two sources of uncertainty are structurally interdependent — an agent
cannot estimate its state without knowing the system's dynamics, and cannot
learn the dynamics without an accurate state estimate — the failure that
results from both being uncertain at once is not the sum of the failures
each would cause alone. Banerjee & Goan (2026) name this
circular dependency the **Epistemic Trap** and measure its effect on a
bipedal locomotion benchmark (Walker2D): "partial observability alone
reduced performance by 19%, and dynamics shift alone by 27%. Under an
independence assumption, the expected combined degradation is approximately
46%. Instead, performance collapsed by 77%, indicating a super-additive
failure far exceeding additive expectations."[^c1]

Across a systematic sweep of 120 configurations, "meaningful super-additive
failure, defined as a compound performance loss exceeding 5% of baseline
beyond the additive prediction, occurred in approximately 13% of cases,"
and was severe when present, reaching 52% above the additive prediction in
the worst case.[^c2]

## Why it stalls asking

The result is a direct counter-example to treating uncertainty as a set of
independent axes to be queried one at a time (stall 2, "which axis first?").
If two axes are epistemically coupled, resolving one in isolation does not
proportionally reduce the failure the pair jointly causes — a selection
criterion that scores axes independently (as [[expected-information-gain]] or a
per-axis [[entropy]] drop does) can undercount the value of an axis that is
only informative jointly with another. The paper's diagnosis is
architectural: conventional passive approaches (robust RL, POMDP state
estimation) assume the two uncertainties are separable and are blind to
their coupling until it produces a collapse.

## Limits

The evidence is a single simulated domain (Walker2D, one RL agent
architecture, 120 configurations) with no comparison against non-RL
question-asking systems; "meaningful super-additive failure" is the
paper's own threshold (>5% of baseline beyond additive), not an externally
fixed one, and the 77%-vs-46% headline figure is one representative
high-severity setting, not the sweep's average.

## Related

- [[compound-uncertainty-coefficient]]
- [[dynamics-information-seeking]]
- [[mutual-information]]
- [[value-of-information]]
- [[expected-information-gain]]

[^c1]: banerjee-2026 — "partial observability alone reduced performance by 19%, and dynamics shift alone by 27%. Under an independence assumption, the expected combined degradation is approximately 46%. Instead, performance collapsed by 77%, indicating a super-additive failure far exceeding additive expectations."
[^c2]: banerjee-2026 — "meaningful super-additive failure, defined as a compound performance loss exceeding 5% of baseline beyond the additive prediction, occurred in approximately 13% of cases"
