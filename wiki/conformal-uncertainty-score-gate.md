---
description: "A service robot asks only when the average confidence the LLM places on its conformal-prediction candidate set falls below a separately calibrated threshold, not merely when that set is non-singleton."
aliases: []
sources: ["hashimoto-2026"]
---
# Conformal Uncertainty-Score Gate

> Two robots both build a [[conformal-prediction]] set before deciding whether
> to ask. One asks whenever the set is not a singleton. This one asks
> whenever the set's *own average confidence* is low — a scalar, itself
> calibrated on held-out data, standing between the prediction set and the
> decision to speak.

## Definition / Mechanism

Hashimoto et al. (2026) build COIN, a household robot
that infers who owns an object from an LLM's multi-label ownership scores
$s_u(o) \in [0,1]$ over candidate users $u$. Rather than asking whenever
more than one candidate is plausible, the robot first forms a conformal
prediction set and then gates on a second, separately calibrated score
computed from that set.

Split conformal prediction sets a quantile $q_\alpha$ on a [[calibration]] set's
nonconformity scores ($nc = 1 - \max_{u \in U_{true}} s_u(o)$), then builds
$\Gamma(o) = \{u \in U \mid s_u(o) \ge 1-q_\alpha\}$: "Using CP, we obtain a
prediction set Γ(o) ⊆ U for each object o, which represents the set of
plausible owners. The size of this set serves as an uncertainty measure: a
larger set indicates higher uncertainty in the ownership estimation."[^c1]

Set size alone is not the trigger. The robot instead computes an
uncertainty score from the *average confidence inside the set*,
$cp_s(o) = 1 - \frac{1}{|\Gamma(o)|}\sum_{u\in\Gamma(o)} s_u(o)$, and
calibrates a second, independent quantile $q_{cp}$ on the calibration
set's distribution of this score. "We set αcp = 0.05, corresponding to
highly confident cases in the calibration data. During inference, if
cps(o) ≤ qcp, we consider the prediction sufficiently confident and
terminate without further user queries."[^c2]

Only objects whose $cp_s(o)$ exceeds $q_{cp}$ generate a question; the LLM
then phrases it around the top-ranked candidates in $\Gamma(o)$. The
coverage guarantee on the underlying set is separate from, and prior to,
the asking decision: "We set α = 0.2, which guarantees that the true owner
is included in the prediction set with probability at least 80%."[^c3]

Evaluated on a simulated household task (34 objects, 3 users, GPT-4o),
this two-stage gate — CP set, then a calibrated confidence score over that
set — reached "a Subset Accuracy of 0.988 and a Mean Jaccard index of
0.991," beating an information-gain active-questioning baseline (ActOwL,
Subset Accuracy 0.674) and simple recency/frequency heuristics.[^c4]

## Why it matters

This is a second, independently-calibrated stopping rule layered on top of
a conformal prediction set, rather than reading the set's cardinality
directly as the uncertainty signal (as [[knowno]] does for a singleton
test). It shows the "ask iff set size > 1" rule is one point in a larger
family: any scalar functional of the calibrated set — cardinality, or
here, mean confidence over the set — can itself be calibrated to a target
false-quiescence rate and used as the trigger, decoupling *how large the
plausible-answer set is* from *how confident the model is about the
members it contains*.

## Transfer

| | |
|---|---|
| **In its home field** | Split conformal prediction (statistics): a calibration set's nonconformity scores set a distribution-free quantile threshold for a prediction set with a finite-sample coverage guarantee |
| **Here** | Applied twice in sequence — once to build the candidate-owner set $\Gamma(o)$, once more to calibrate a *second* quantile on a scalar (mean confidence) computed from that set, and that second quantile gates whether the robot asks |
| **What survives** | The finite-sample, distribution-free calibration guarantee for each of the two quantiles taken separately (coverage of $\Gamma(o)$ at $1-\alpha$; the $q_{cp}$ quantile's own coverage over calibration-set $cp_s$ values) |
| **What does not** | No joint guarantee is stated or proved for the two-stage procedure together — the paper reports the false-quiescence rate of the composed decision (ask/don't-ask) only empirically, not as a corollary of the two marginal conformal guarantees |

## Limits

This note's claim rests on a single simulated Gazebo household environment
with 3 users, 34 objects and one LLM (GPT-4o); the paper's own accuracy
numbers are for that environment only, not a general property of the gate.
The two-stage calibration ($\alpha=0.2$, $\alpha_{cp}=0.05$) is
hand-chosen, and the paper does not show the composed procedure's
false-quiescence rate is itself bounded the way each individual conformal
step is. `hashimoto-2026` is an arXiv preprint (2026-05-27, not yet
peer-reviewed) and is `unverified` pending the wiki's source verification.

## Related

[[knowno]] · [[calibration]] · [[budgeted-conformal-evidence-acquisition]] · [[value-of-information]] · [[mondrian-conformal-prediction]]

[^c1]: hashimoto-2026 — "Using CP, we obtain a prediction set Γ(o) ⊆ U for each object o, which represents the set of plausible owners. The size of this set serves as an uncertainty measure: a larger set indicates higher uncertainty in the ownership estimation."
[^c2]: hashimoto-2026 — "We set αcp = 0.05, corresponding to highly confident cases in the calibration data. During inference, if cps (o) ≤ qcp , we consider the prediction sufficiently confident and terminate without further user queries."
[^c3]: hashimoto-2026 — "We set α = 0.2, which guarantees that the true owner is included in the prediction set with probability at least 80%."
[^c4]: hashimoto-2026 — "achieving a Subset Accuracy of 0.988 and a Mean Jaccard index of 0.991"
