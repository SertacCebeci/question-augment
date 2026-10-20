---
description: "Whatever the individual per-step probabilities, the win probability of the Bruss's Theorem 2 (2000): let $s$ be the optimal threshold of odds-theorem — the index at which the backward odds sum $R_k…"
aliases: ["typical lower bound", "typical lower bound for V(n)"]
sources: ["bruss-2000"]
---
# The odds-theorem's typical lower bound

> Whatever the individual per-step probabilities, the win probability of the
> optimal last-success stopping rule never falls below $R_se^{-R_s}$, where
> $R_s$ is the summed odds at the odds-theorem's threshold $s$ — so the
> recurring "$\approx 1/e$" answer across secretary-problem modifications is
> a consequence of one aggregate number being near 1, not of ranks or
> records.

## Definition / Mechanism

Bruss's Theorem 2 (2000): let $s$ be the optimal threshold of[^s1]
[[odds-theorem]] — the index at which the backward odds sum
$R_k = \sum_{j=k}^n r_j$ first reaches 1, i.e. the output of the
odds-algorithm's step A1 — and $R_s = \sum_{j=s}^n r_j = R$. Then

$$V(n) = \Big(\sum_{j=s}^n r_j\Big)\Big(\prod_{j=s}^n q_j\Big) > Re^{-R},$$

proved by an AM–GM bound on $\prod_{j=s}^n q_j$ in terms of $R$ and the
number $m = n-s+1$ of remaining indices. The floor is stated in $R_s$ alone;
the product $Q_s = \prod_{j=s}^n q_j$ that the exact value $V(n) = Q_sR_s$
(step A2) needs does not enter it. Part (ii): if $R_{s(n)} \to 1$ while the
sum of *squared* odds at the threshold $R^{(2)}_{s(n)} \to 0$ as
$n\to\infty$, then $V(n) \to 1/e$ exactly — with no reference to ranks,
permutations, or a logarithmic record-rate.

## Why it matters

Bruss states the theorem to explain *why* $1/e$ or a value near $1/e$ keeps
appearing in "many modifications of the secretary problem" (§5, citing
Pfeifer 1989, Samuels 1993, Samuel-Cahn 1995) and in the Poisson-arrival
last-success problem of §4.1: it happens whenever the threshold's remaining
summed odds are near 1 with individually small odds — an aggregate,
distribution-free condition, not an artefact of rank-based problems. For a
selection procedure run by the odds-algorithm, the floor is a guarantee
stated from the running odds sum alone: the asker must have run step A1 —
summed the odds backward until the sum crossed 1, which locates $s$ and
gives $R_s$ — and can then assert $V(n) > R_se^{-R_s}$ before, or instead
of, running step A2, the product $Q_s$ of the individual failure
probabilities. The floor spares A2, never A1. Bruss notes the bound is sharp
and that $R_s$ is often close to 1 "not only in asymptotic cases", which is
why $1/e$ can be called a typical lower bound.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Bruss 2000, §5) | typical lower bound (for $V(n)$) | exact — the paper's own name for Theorem 2 |
| Optimal stopping (Bruss 1984) | 1/e-law | **not this concept** — a distinct theorem about an *unknown* number of trials; this bound holds for the same known-horizon rule as [[odds-theorem]] and needs no unknown-$N$ machinery |

## Transfer

| | |
|---|---|
| Home field | Optimal stopping, as a corollary of the Odds-theorem — the same independent-indicator, known-horizon setting, evaluated at the odds-theorem's threshold $s$ |
| Here | A horizon-limited commitment rule that follows the odds-algorithm: the asker lists the remaining opportunities' odds backward, stops summing when the sum reaches 1, and has thereby located $s$ and $R_s$ (step A1) |
| What survives | The floor $R_se^{-R_s}$ as a function of that one summary number — a guarantee the asker can state once A1 is done, without multiplying out the per-step failure probabilities $Q_s$ (step A2); and the diagnosis that an "$\approx 1/e$" success rate is what aggregate odds near 1 produce, so it should not be read as evidence of a ranking or record structure |
| What does not | The asymptotic convergence to $1/e$, which needs $R^{(2)}_{s(n)}\to 0$ — individually small remaining odds, not just their sum near 1; a horizon dominated by one near-certain late opportunity gives a floor far from $1/e$, and the theorem says nothing more about acting there than "the floor is $R_se^{-R_s}$" |

## Limits

The bound is a property of the *optimal* rule's value at the odds-theorem's
own threshold: the asker must have located $s$ by summing odds (A1), and an
asker who does not follow that threshold — e.g. who stops "whenever it
feels close enough" — inherits no floor from Theorem 2 as stated. The floor
saves computing $Q_s$, not locating $s$; and once $s$ is located the exact
value $Q_sR_s$ is one product away, so the floor's use is a statement made
*before* that product, not a substitute for the threshold. It also only
answers how good the achieved probability is, never what to do when $R_s$
is far from 1; and the $1/e$ limit is a statement about a *sequence* of
growing problems ($n\to\infty$), not a property checkable on a single
finite instance without the vanishing-squared-odds condition.

## Related

[[odds-theorem]] · [[value-of-information]] · [[reversibility]] · [[bounded-rationality]]

[^s1]: bruss-2000
