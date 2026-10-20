---
description: "Choose the next action — evaluate an objective or elicit a preference in one of several modalities — by maximizing expected decision-quality gain divided by that action's cost."
aliases: []
sources: ["burnat-2026"]
---
# VOI-per-cost modality selection

> Do not fix a query schedule or a query type in advance: at every step, price
> every available action — an expensive objective evaluation as much as a
> cheap or costly preference query — by the decision-quality it is expected
> to buy per unit of its own cost, and take the cheapest path to a better
> decision.

## Definition / Mechanism

Burnat (2026)'s QUIVER controller picks the next action
$a$ from a heterogeneous set $\{\mathrm{Eval}, \mathrm{PS}, \mathrm{IA}\}$ —
evaluate a candidate's objectives, ask a cheap pairwise preference statement,
or ask a costlier indifference adjustment — by

$$a^\star = \arg\max_a \frac{\mathbb{E}[\Delta Q \mid a, \mathcal{H}_t]}{c(a)}$$

using one shared decision-quality proxy $Q$: for preference queries, $\Delta
Q$ is the expected [[entropy]] reduction of the preference posterior
(information gain); for an objective evaluation, $\Delta Q$ is the expected
improvement in posterior [[expected-utility|expected utility]] among evaluated points. "Although
IG and VOCeval measure different quantities (entropy reduction vs. utility
improvement), both are proxies for the same underlying goal: reducing
recommendation regret. The cost-normalized ratio in Eq. (9) compares their
expected contributions to this shared objective, making cross-modality
comparison meaningful."[^c1]

A direct corollary prices the two query modalities against each other:
QUIVER selects the costlier indifference-adjustment query over a pairwise
statement exactly when its information-per-cost exceeds the pairwise
query's — "QUIVER selects IA over PS if and only if
$\mathrm{IG}_{IA}/c_{IA} > \mathrm{IG}_{PS}/c_{PS}$. This follows directly
from Eq. (9)... For the empirically grounded cost ratio $c_{IA}/c_{PS} =
1.15$, QUIVER requires IA to provide at least 15% more information than PS
to justify selection."[^c2]

On the WFG benchmark suite under synthetic decision-maker models this policy
outperformed every fixed-schedule and single-modality baseline: "QUIVER
achieves the lowest final utility regret on challenging WFG problems
(utility regret of 2.14 on WFG4, 2.82 on WFG9: a 25% improvement over
baselines), outperforming all single-modality baselines."[^c3]

## Why it matters

Stall 2 asks which axis (here, which action on the preference model) to
take up next; this policy answers it with a ratio rather than a subtraction
or a fixed order, and — unlike [[expected-information-gain]] used within one
action type — it prices actions of genuinely different kinds (spending on
the world vs. spending on the decision-maker, and within the latter, a cheap
noisy signal vs. a costlier precise one) against each other on one scale,
because it fixes the denominator to the action's own cost rather than
assuming all actions cost the same unit.

## Transfer

| | |
|---|---|
| **Home field** | Decision-theoretic [[value-of-information]] / cost-sensitive Bayesian optimization, where an acquisition function ranks candidates of one type (evaluations) by information or improvement per cost |
| **Here** | Interactive multi-objective optimization, where the action set spans objective evaluation and two structurally different preference-query modalities under one shared budget |
| **What survives** | The ratio form itself — maximize expected quality gain divided by cost — and the corollary it induces: a threshold on the *ratio* of information rates, not on either quantity alone, decides which modality to use |
| **What does not** | The commensurability the ratio needs — that entropy reduction and utility improvement are "proxies for the same underlying goal" — is asserted by the paper, not derived, so the cross-type comparison inherits an unproven assumption (see[^c1] above) |

## Limits

- The commensurability of $\Delta Q$ across action types (entropy reduction
  vs. utility improvement) is this paper's working assumption, not a proven
  identity — see Transfer above.
- Validated only against synthetic decision-makers with a known linear
  utility over objectives, simulated with Bradley-Terry and Gaussian noise
  models on DTLZ/WFG benchmarks; no human-subject elicitation is reported.
- The $c_{IA}/c_{PS} = 1.15$ cost ratio the modality threshold is calibrated
  to comes from a single external study of 83 roofing professionals, not
  from this paper's own subjects.
- Regret is measured against the analytic Pareto-optimum for these
  benchmarks; the paper itself cautions that absolute regret values are not
  comparable across different optimization backbones.

## Related

[[expected-information-gain]] · [[cross-type-eig]] · [[value-of-information]] · [[current-solution-strategy]]

[^c1]: burnat-2026 — "Although IG and VOCeval measure different quantities (entropy reduction vs. utility improvement), both are proxies for the same underlying goal: reducing recommendation regret. The cost-normalized ratio in Eq. (9) compares their expected contributions to this shared objective, making cross-modality comparison meaningful."
[^c2]: burnat-2026
[^c3]: burnat-2026 — "QUIVER achieves the lowest final utility regret on challenging WFG problems (utility regret of 2.14 on WFG4, 2.82 on WFG9: a 25% improvement over baselines), outperforming all single-modality baselines."
