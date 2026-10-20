---
description: "Decomposes a query's loss into irreducible and reducible components to decide predict, route to an oracle, or abstain, with a proven bound on regret against the best level-set router."
aliases: ["flexible router", "uncertainty-aware router", "prediction-only optimal routing"]
sources: ["peale-2026"]
---
# Uncertainty-aware router

> Three actions, one split: predict cheaply, pay for the oracle, or refuse —
> chosen by how much of the loss a stronger answerer could actually remove.

## Definition / Mechanism

For a weak model $f$ and an oracle $f^*$ giving the true conditional
$y|x$, Peale, Devic & Gopalan (2026) split the weak model's
expected loss $L(f^*(x), f(x))$ into two terms: the **irreducible loss**
$L(f^*(x), f^*(x))$ — the loss the oracle itself still pays, i.e. label
noise the oracle cannot remove — and the **reducible loss**, the gap
between the weak model's loss and the oracle's. "The amount of irreducible
loss and reducible loss precisely characterizes which routing action is
optimal... if the loss is primarily irreducible → abstain (or clarify with
the user); if primarily reducible → route to the oracle; otherwise →
predict using the weak model."[^c1]

Because the true split requires an oracle call to compute, the router
instead estimates it from a **higher-order predictor** $F$: a predictor
over *distributions over labels* rather than labels, built by binning
inputs into level sets and, within each bin, comparing the weak model's
prediction against a k-snapshot mean of several independent labels per
input (a "Bin-and-Estimate" procedure). This gives per-bin estimates
$\widehat{IL}$, $\widehat{RL}$ used to pick the action for a new query.

## Why it matters

The router is **configuration-flexible**: one estimator serves any routing
cost $T=(L,\alpha,\beta)$ — the loss function, the oracle's fixed overhead
$\alpha$, and the [[abstention]] penalty $\beta$ — without retraining, because
the estimate being reused is the loss decomposition, not a policy fit to
one cost. This targets the routing failure the authors name explicitly:
a confidence-only router "needlessly routing to the oracle even when it
would also perform poorly" on inputs whose loss is mostly irreducible.

## Theoretical basis

**Theorem 4.1** (Peale, Devic & Gopalan 2026): if $F$ is
$\epsilon$-higher-order calibrated (its predicted mixtures are within
Wasserstein-1 distance $\epsilon$ of the true Bayes-mixture on every level
set) and shares $f$'s level sets, then the router $r$ built from $F$
satisfies, for any bounded proper loss $L$ with bound $B$ and any
$\alpha,\beta\ge0$: $\mathbb{E}[\mathrm{Cost}(x, r(x,T);T) -
\mathrm{Cost}(x, r_f(x,T);T)] \le B\epsilon$ — regret against $r_f$, the
best router that is a function of $f$'s level sets alone (not against the
unrestricted pointwise-optimal router, which needs $f^*$ itself).[^c2]

## Transfer

| | |
|---|---|
| **Home field** | [[calibration]] theory: higher-order calibration (Ahdritz et al. 2025, cited but not read here) is a guarantee about a predictor's *distributional* outputs matching the true label-generating mixture on every level set |
| **Here** | reused as the estimator that recovers a query's irreducible/reducible loss split without ever calling the oracle at deployment |
| **What survives** | the regret bound: any $\epsilon$-higher-order-calibrated $F$ gives a router within $B\epsilon$ of the best level-set-restricted router, for *every* routing cost simultaneously |
| **What does not** | the guarantee is against $r_f$ (best router using only $f$'s level sets), not the unrestricted pointwise optimum $r^*$, which needs $f^*$; and it assumes $F$'s level sets match $f$'s, a condition the paper notes needs post-hoc calibration to arrange |

## Limits

- The regret bound (Theorem 4.1) is proved for a **proper, bounded loss**
  $L:\Delta Y\times\Delta Y\to[0,B]$; the paper states the general case
  "can be easily reduced to the proper case" but the reduction is not in
  the slice read here.
- The benchmark $r_f$ the theorem competes against is itself restricted to
  $f$'s level sets — a router that could see $f^*$ directly could still
  beat both by more than $B\epsilon$.
- Achieving small $\epsilon$ in practice needs a k-snapshot calibration
  set (multiple independent labels per input), which most deployments do
  not have; the paper's own practical section is post-hoc and bin-based,
  not the calibrated-by-construction predictor the theorem assumes.
- Single arXiv preprint (2026), not verified as peer-reviewed at the time
  of this note.

## Related

[[uncertainty-decomposition]] · [[abstention]] · [[value-of-information]] · [[bayesian-self-escalation]]

[^c1]: peale-2026
[^c2]: peale-2026
