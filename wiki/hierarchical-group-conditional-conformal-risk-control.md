---
description: "A post-hoc calibration procedure that certifies simultaneous risk bounds for every node of a group hierarchy, so abstention is safe for every subgroup, not just on average."
aliases: ["HG-CRC", "Hierarchical Group-Conditional Conformal Risk Control"]
sources: ["salem-2026"]
---
# Hierarchical Group-Conditional Conformal Risk Control

> Standard (marginal) [[crc-confident-error-control|conformal risk control]] bounds the average error rate
> of a selective predictor, but a threshold that keeps the average safe can
> still expose one subgroup to an unbounded error rate. HG-CRC calibrates
> one threshold per node of a declared group hierarchy so that every group,
> not just the population, is certified.

## Definition / Mechanism

Given a group hierarchy $H$ (a rooted tree of nested membership masks over
the input space, root = everyone), HG-CRC calibrates a threshold $\tau_v$
at every node $v$ from a held-out [[calibration]] set, then answers a test
example by walking its ancestry path leaf to root: "$v^*(x)$ is the deepest
certified ancestor of x whose threshold the example satisfies ... and
Abstain is returned if no such node exists."[^c1]

Each node's confidence level is corrected for testing $|H|$ nodes at once:
"Direct application of the union bound gives the required per-node
confidence level: $\hat\delta = \delta/|H|$" — each node's Clopper-Pearson
upper risk bound $U_v(\tau)$ must clear $\hat\delta$, and a node with fewer
than $N_{min}=30$ calibration examples is pruned rather than certified. A
descendant "claims" the calibration examples it answers; an ancestor node
is calibrated only on its *residual* (the examples its certified
descendants did not answer), which keeps the calibration and deployment
populations of each node aligned.[^c2]

For the split variant (each hierarchy depth calibrated on a disjoint data
fold), the guarantee is unconditional: "for each node $v \in H$,
$P(R_v(\tau_v^*) > \alpha \mid \rho_v(x)=1) \le \hat\delta$ ... By the union
bound, $P(\exists v \in H : R_v(\tau_v^*) > \alpha) \le |H|\cdot\hat\delta =
\delta$" (Proposition 1). The deployed default reuses all calibration data
at every node ("in-sample") instead of splitting it, which is only exact
under a test-point-augmentation argument (Proposition 2); the plain
deployed procedure (no augmentation) is valid up to a measured slack:
"$P(R_v(\tau_v^*) > \alpha \mid \rho_v(x)=1) \le \hat\delta + \epsilon_n$,
$P(\exists v : R_v > \alpha) \le \delta + |H|\epsilon_n$" (Lemma 1), where
$\epsilon_n$ is the probability a single calibration point's inclusion
flips a routing decision — measured below 0.5% mean, under 1% at the 95th
percentile, across the paper's models and benchmarks.[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| Salem, Pontes, Böhm & Ferrugem (2026), Abstract/§3 | HG-CRC | exact — the paper's own abbreviation |
| Salem et al. (2026), §3.4 | leaf-first selection policy | exact — the routing rule internal to HG-CRC, not a separate concept |

## Why it matters

It is a measured counter-example to treating a marginal risk bound as
sufficient for a [[abstention|selective-prediction]] system: "under mild distributional
shift in group composition, standard CRC violates the risk budget in up to
47% of evaluation trials," and HG-CRC "achieves an empirical 0% violation
rate and WGER = 0 on ARC Challenge for models with sufficiently high base
accuracy" — where WGER (Worst-Group Excess Risk) is $\max_v \max(R_v -
\alpha, 0)$ (Corollary 2.1). For an agent deciding whether to answer or
abstain/ask, this names the mechanism (and its cost) for making that
decision equitably certified across the populations it serves, not merely
correct in aggregate.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | Split conformal risk control gives a single distribution-free, finite-sample marginal risk bound for one threshold via the Clopper-Pearson upper confidence bound (Angelopoulos et al., 2023) |
| **Here** | Applied once per node of a declared group hierarchy, with a Bonferroni correction over nodes and a leaf-first residual-calibration policy so the guarantee holds simultaneously, not just on average |
| **What survives** | The distribution-free, finite-sample coverage-style bound at each node, conditional on that node's residual population; the split variant keeps this unconditionally |
| **What does not** | Marginal validity does not need the hierarchy to be shallow or well-separated to hold, but participation pays for it — the deployed in-sample variant is only exact up to a measured slack, not unconditionally, and splitting costs participation relative to global CRC |
[^c5]

The paper measures the participation cost of that trade-off directly:
splitting costs "between 0.6 pp ... and 5.5 pp ... of participation
depending on the model" on ARC Challenge, and "the participation cost
relative to global CRC ranges from 22 to 37 percentage points for the two
primary pairs under residual calibration."[^c6]

## Limits

The guarantees rest on calibration/test exchangeability within each node's
residual population — a mismatch (e.g. the deployment mixture drifting
from the calibration mixture) is outside the bound. The deployed default
(in-sample calibration) is not exactly valid; it inherits the slack
$\epsilon_n$ of Lemma 1, governed by Assumption 1 (threshold regularity),
which the paper itself calls "the only place we step outside the
distribution-free regime." The empirical 0% violation results are upper
bounds at the paper's evaluation resolution (500 bootstrap trials, so a
true rate up to ~0.6% is consistent with an observed zero) rather than
certified zeros, and the method degrades on a model whose uncertainty
scores are poorly calibrated for the task (Gemma-3-4B on MMLU-Pro), where
it abstains more rather than violating the budget.

## Related

[[round-wise-regret-conformal-acceptance]] · [[confidence-calibrated-cascade-judgment]] · [[calibration]] · [[abstention]]

[^c1]: salem-2026 — "v ∗ (x) is the deepest certified ancestor of x whose threshold the example satisfies (s(x) ≤ τv∗ ), and Abstain is returned if no such node exists."
[^c2]: salem-2026
[^c3]: salem-2026
[^c4]: salem-2026 — "under mild distributional shift in group composition, standard CRC violates the risk budget in up to 47% of evaluation trials"
[^c5]: salem-2026
[^c6]: salem-2026 — "splitting costs between 0.6 pp ([−2.1, 3.3], indistinguishable from zero) and 5.5 pp ([3.7, 7.4]) of participation depending on the model"
