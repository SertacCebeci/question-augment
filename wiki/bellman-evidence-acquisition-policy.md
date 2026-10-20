---
description: "A finite-lattice Bellman recursion over a small evidence set picks the next source to query or to stop, proved globally optimal for fixed terminal risks and costs."
aliases: ["Bayesian Selective Latent Inference", "BSLI", "Bellman selective-evidence router", "cost-calibrated Bellman policy", "calibrated finite-lattice acquisition oracle"]
sources: ["zhang-2026-bayesian"]
---
# Bellman evidence-acquisition policy

> Which evidence source to query next, and when to stop, is solved exactly —
> not approximated — when the set of possible sources is small enough that
> its subset lattice fits in memory.

## Definition / Mechanism

Zhang, Song, Wang, Bhatt & Huang (2026) pose wastewater-first influenza monitoring as
choosing, at each observed evidence subset $S$ of a small modality set $M$
(here $|M|=4$: ED visits, hospitalizations, lab positivity, source-policy
evidence), whether to stop or to query one more modality. A calibrated
terminal risk $\tilde R_t(S)$ (built from a Bayesian posterior's free energy)
and calibrated per-modality costs $\tilde c_m$ define the value function
$$V(S) = \min\Big(\tilde R_t(S),\ \min_{m\in M\setminus S}\big[\tilde c_m + V(S\cup\{m\})\big]\Big),$$
solved by exact backward induction over the finite subset lattice $2^{|M|}$.
"The calibrated query/stop value is the exact Bellman solution on the finite
evidence lattice."[^c1]

The paper's Theorem 2 proves this: for fixed terminal risks and fixed
nonnegative calibrated costs, the recursion returns the globally optimal
stop/query policy among all finite acquisition trajectories on $M$ — the
abstract states the authors "prove the key variational, answerability,
Bellman-optimality, and one-dimensional cost-calibration" properties of the
policy.[^c2]

## Why it matters

On stall 2 this is a case where exact optimal ordering is *not* out of
reach: [[optimal-decision-tree]] shows constructing the optimal test order
is NP-complete in general, and greedy is the guaranteed fallback. Here the
combinatorial object being optimized is not the space of hypotheses but the
space of evidence *sources* — bounded and small ($2^4=16$ states) — so the
exact Bellman solution is tractable and the "do not search for the perfect
order" lesson does not bind.

## Transfer

| | |
|---|---|
| In its home field | Dynamic programming / optimal control: backward induction over a finite, enumerated [[possible-worlds|state space]] with a terminal cost and per-step action costs |
| Here | Deciding which of a small set of external evidence sources to query next, or to stop, given a Bayesian posterior's calibrated risk |
| What survives | Exact backward-induction optimality (Theorem 2) whenever terminal risks and costs are fixed and the state space is finite and small; the value function's stop-or-query structure |
| What does not | Scalability — the state space is $2^{|M|}$, so it inherits the same exponential blow-up as [[optimal-decision-tree]]'s NP-hard case once the number of possible sources grows; the paper's tractability rests on $|M|=4$, not on a general result |

## Limits

- Theorem 2's optimality holds only for *fixed* terminal risks and
  costs — i.e. after the posterior surrogate is fit and frozen and the
  cost-energy multiplier is set; it says nothing about whether the learned
  surrogate or multiplier is itself correct.
- The lattice is finite and searchable only because $|M|=4$ in this
  deployment; nothing in the proof bounds how the method behaves as $|M|$
  grows.
- Read from the arXiv preprint (Zhang et al. 2026); not yet peer-reviewed — [?].

## Related

[[optimal-decision-tree]] · [[value-of-information]] · [[abstention]] · [[adaptive-submodularity]]

[^c1]: zhang-2026-bayesian — "The calibrated query/stop value is the exact Bellman solution on the finite evidence lattice:"
[^c2]: zhang-2026-bayesian — "We prove the key variational, answerability, Bellman-optimality, and one-dimensional cost-calibration"
