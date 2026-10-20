---
description: "At a **fixed sample size**, measured by the **error exponent**, whether Nitinawarat,"
aliases: []
sources: ["nitinawarat-2013"]
---
# Causal control advantage in multihypothesis testing

> At a **fixed sample size**, measured by the **error exponent**, whether
> adapting the next sensing action (design) to evidence gathered so far ever
> beats a schedule fixed in advance depends on how many hypotheses are in
> play: with two, the best open-loop schedule already attains the causal
> optimum (Proposition 1); with three or more, causal control can strictly
> beat every open-loop schedule. The adaptive-stopping (sequential) case is
> a different comparison — see [[multihypothesis-chernoff-test]].

## Definition / Mechanism

Nitinawarat, Atia & Veeravalli (2013) model $M$-ary [[hypothesis-testing|hypothesis testing]] with[^s1]
**controlled sensing**: at each step $k$ a controller picks $u_k$ from a
finite alphabet $\mathcal{U}$, and the next observation $Y_k$ is then drawn
(conditionally i.i.d. given the true hypothesis $i$ and the chosen control)
from a distribution $p_i^{u_k}$. For a *fixed* sample size $n$, they compare
two policy classes: **open-loop** control, where the whole sequence
$u^n$ is fixed (or randomised) independently of the data before observing
anything, and **causal** control, where $u_{k+1}$ may depend on all past
observations and controls.

**Theorem 1** (open-loop, $M>2$): the largest error exponent achievable by
open-loop control has a closed max–min–max form over control weightings $q$
and hypothesis pairs, and is attained by a *pure* (non-randomised),
stationary schedule — no benefit from randomising the schedule.

**Proposition 1** ($M=2$, fixed $n$, error exponent): for binary hypothesis
testing the open-loop optimum equals the causal optimum exactly, and both
equal $\max_u C(p_0^u, p_1^u)$, the maximum **Chernoff information** over the
choice of control. Past information and randomisation buy nothing *in the
fixed-sample-size exponent* when there are only two hypotheses. This is not
a statement about the sequential test: there, even at $M=2$, the control
law of [[multihypothesis-chernoff-test]] depends on the current
maximum-likelihood hypothesis, because the control maximising
$D(p_0^u \| p_1^u)$ and the one maximising $D(p_1^u \| p_0^u)$ can differ
when the divergences are asymmetric.

**The $M=3$ separation (Section V).** With three hypotheses (an event at one
of three locations, one sensor per location, $\epsilon$-parametrised
distributions), the best open-loop exponent is
$\beta_{OL} = \tfrac{2}{3}C(p,\bar p) = -\tfrac{2}{3}\log(2\sqrt{\epsilon(1-\epsilon)})$,
while a causal policy that always queries the sensor separating the two
currently most-likely locations achieves
$\beta_C \ge -\log\big(\epsilon^{1/3}(1-\epsilon)^{2/3}+\epsilon^{2/3}(1-\epsilon)^{1/3}\big)$
— strictly larger than $\beta_{OL}$ for every $\epsilon \in (0,\tfrac12)$.
Theorem 2 supplies general (not always tight) lower and upper bounds on the
causal-control exponent for any $M>2$; the exact value for general $M$ is
left open.

## Why it matters

For a stall-2 practitioner picking which axis to probe next inside a
**fixed** [[question-budgets|question budget]], the theorem bounds what adaptivity can buy. With
exactly two live candidate designs, adapting the probe order to answers
cannot improve the fixed-budget error exponent: a precomputed order attains
the same exponent (Proposition 1). That is a bounded statement — it does not
say adaptivity is useless at two candidates. When stopping is adaptive
(decide as soon as the evidence suffices), the control law still depends on
the current leading hypothesis, and adaptivity can change the *expected
number of questions* even at $M=2$ ([[multihypothesis-chernoff-test]]).
Once there are three or more live candidates, even the fixed-budget warrant
disappears: there exist configurations (proved by the $M=3$ example, not
merely suspected) where no fixed schedule matches the exponent of a policy
that re-scores the next probe against the current leading guess.

## Transfer

| | |
|---|---|
| **In its home field** | $M$ fully specified statistical hypotheses, each with a known observation density per control value, a finite control alphabet, a fixed sample size $n$, and an exponent defined as $n\to\infty$ |
| **Here** | candidate values along a design/question axis stand in for hypotheses; the "control" is which sub-question or probe to pose next; the fixed budget is a fixed number of questions; no density is written over natural-language answers |
| **What survives** | the qualitative separation *at fixed budget*: two branches, adapting cannot improve the fixed-budget exponent; three or more, adapting can strictly help — and the shape of the winning rule: re-score against the *current* leading candidate, not the whole remaining set |
| **What does not** | the numeric exponents and the Chernoff-information optimisation, which need explicit densities $p_i^u$; the asymptotic regime ($n\to\infty$), which says nothing about a small fixed budget; and any conclusion about the adaptive-stopping case, where the two-hypothesis equivalence does not carry over |

## Limits

- Proposition 1 and the $M=3$ separation are large-sample **exponent**
  statements; neither says anything about finite-$n$ performance.
- The $M\ge3$ separation is established by an explicit worked example plus
  general bounds that need not be tight — the paper states outright that the
  exact optimal causal-control exponent for general $M>2$ is unresolved, so
  "causal beats open-loop for $M\ge3$" is an existence claim, not a claim
  that it holds for every $M\ge3$ instance.
- Everything here is the **fixed-sample-size** setting (decide after exactly
  $n$ observations). "Adapting buys nothing at $M=2$" is *only* a claim
  about that setting's error exponent; the sequential setting, where $N$
  itself is chosen adaptively, is a different comparison in which the
  control law is data-dependent even at $M=2$ — see
  [[multihypothesis-chernoff-test]].
- Needs conditionally i.i.d. observations given (hypothesis, control) at
  each step and a finite control alphabet (the source's assumptions (1)-(2)).

## Related

[[multihypothesis-chernoff-test]] · [[sprt]] · [[generalized-binary-search]] · [[bayesian-experimental-design]] · [[kl-divergence]]

[^s1]: nitinawarat-2013
