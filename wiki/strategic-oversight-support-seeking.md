---
description: "Online algorithm that thresholds an estimated value-of-support score with randomised exploration, bounding the empirical missed-support error at a chosen target, distribution-free."
aliases: ["SOS", "Strategic Oversight for Support-seeking", "Algorithm 1 (Kiyani et al. 2026)"]
sources: ["kiyani-2026"]
---
# Strategic Oversight for Support-seeking (SOS)

> The online counterpart to [[value-of-support]]'s population-optimal
> threshold: since the value of support is unknown in practice, SOS
> estimates a score for it, thresholds the score with a small forced-exploration
> probability, and debiases the threshold round by round so the realised
> missed-support rate tracks a declared target — with no assumption on how
> the data or the agent behave.

## Definition / Mechanism

At round $t$, the agent produces an unsupported output $y_0^t$, computes a
score $s_t = s_{\theta_t}(x_t, y_0^t) \in [0,1]$ meant to approximate the
value of support, and the algorithm sets the support-seeking probability
"pt ← µ + (1 − µ) 1{st ≥ λt }" before it "Sample[s] at ∼ Bernoulli(pt)" —
so support is always sought above the current threshold $\lambda_t$, and
still sought with small probability $\mu$ below it, purely to obtain
feedback about whether support would have helped. Only on rounds where
support was sought is the benefit label $g_t$ observed, and the threshold
is updated by an importance-weighted, stochastic-quantile-tracking step
using $g_t$, the realised action $a_t$, and $p_t$; an optional
[[calibration]]-on-the-fly step simultaneously updates the score parameters
$\theta_t$ by gradient descent toward $g_t$.[^c1]

Theorem 4.1 bounds the resulting empirical missed-support error
$\widehat{\mathrm{MSE}}(T)$: run with constant step size, fixed exploration
$\mu$, target $\alpha \in (0, 1-\mu)$; then "for any δ ∈ (0, 1), w.p. at
least 1 − δ over the algorithm's randomness, [MSE(T ) ≤ α + ∆(Ng (T ), δ)"
— the target is met up to a finite-sample correction term that shrinks as
the number of beneficial-support rounds $N_g(T)$ grows, with no
distributional assumption on the input stream, the agent, or the support
mechanism.[^c2]

## Why it matters

This is a concrete, task-agnostic recipe for the "ask or act" decision on
this stall: it needs no known distribution over how often support helps
and no calibration set fixed in advance, only a bound on the target
missed-support rate the operator is willing to tolerate, traded against how
often support gets called.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | online stochastic approximation / quantile tracking under partial (bandit-style) feedback | deciding, round by round, whether an AI agent should call for external support |
| What survives | the importance-weighted correction for observing the error signal only on acted-upon rounds, and the resulting high-probability finite-sample bound | unchanged — Theorem 4.1 is proved directly for this threshold-update rule |
| What does not | classical regret bounds optimise a reward; here nothing is optimised beyond meeting a declared error target $\alpha$ while reducing support calls, and the bound is stated in $N_g(T)$ (beneficial-support rounds observed), not in total rounds $T$ |

## Limits

The guarantee holds for constant step size $\eta$ and fixed exploration
$\mu$; the bound's terms trade $\mu$ against both tightness of error
control and how often support is called, so the target $\alpha$ and $\mu$
must be chosen together, not read off a single "right" value. The bound
degrades (the correction term $\Delta$ grows) when $N_g(T)$, the number of
rounds on which support would actually have helped, stays small — a rare-benefit
regime is the hardest case, and the paper offers no separate finite-sample
analysis for it. Calibration-on-the-fly changes the score's quality but the
validity guarantee "does not rely on calibration-on-the-fly," so a
mis-specified score family costs support calls, not error-rate validity.
`kiyani-2026` is a 2026 arXiv preprint, not yet peer-reviewed. [?]

## Related

[[value-of-support]] · [[bayesian-self-escalation]] · [[sprt]] · [[value-of-information]]

[^c1]: kiyani-2026 — "pt ← µ + (1 − µ) 1{st ≥ λt }"
[^c2]: kiyani-2026 — "for any δ ∈ (0, 1), w.p. at least 1 − δ over the algorithm’s randomness,"
