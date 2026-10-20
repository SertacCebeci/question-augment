---
description: "A score is separable at a threshold when it survives more often on correct predictions than on errors — necessary and sufficient for abstention to raise selective accuracy."
aliases: ["score separability", "separability gap", "accuracy gain theorem"]
sources: ["gu-2026-pause"]
---
# Score separability

> Raising an [[abstention]] threshold only helps if the confidence score is
> systematically higher on correct answers than on wrong ones; the size of
> that gap, not the threshold itself, is what buys the accuracy.

## Definition / Mechanism

Gu, Yu, Partovi Nia & Asgharian (2026) study a system that
aggregates several chain-of-thought paths into one answer with a confidence
score $\nu\in[0,1]$ (the winning answer's share of a quality-weighted vote)
and abstains when $\nu\le\lambda$. Let $S_{cor}(\lambda) := P(\nu>\lambda\mid
\hat y = Y)$ and $S_{err}(\lambda) := P(\nu>\lambda\mid \hat y\neq Y)$ be the
survival functions of the score on correct and incorrect predictions, and
$\Delta(\lambda) := S_{cor}(\lambda) - S_{err}(\lambda)$ the separability gap.
"We call the score separable at λ if ∆(λ) > 0."[^c1]

Their Theorem 1 turns this into an exact accuracy statement: when $\nu$ is
separable at $\lambda$, the selective accuracy $A_c(\lambda)$ among
non-abstained predictions exceeds the unfiltered vote accuracy $p_v$ by an
amount driven entirely by $\Delta(\lambda)$ — "the gain is multiplicatively
driven by the separability gap ∆(λ): a score with ∆(λ) = 0 produces zero
accuracy gain regardless of how many paths are sampled or how aggressively λ
is set."[^c2]

A converse (their Proposition 3.3) makes separability necessary, not merely
sufficient: "If ∆(λ) ≤ 0, then Ac (λ) ≤ pv , with equality iff ∆(λ) = 0. In
particular, a score with ∆(λ) ≤ 0 at every λ > 0 cannot improve selective
accuracy via abstention at any threshold."[^c3]

The gain is also estimable from [[calibration]] data alone — a plug-in predictor
built from the empirical survival functions converges almost surely to the
true selective accuracy (their Corollary 3.2), so a practitioner can predict
the accuracy of a threshold before spending it on a test set.

## Why it matters

Every abstention rule on stall 10 implicitly assumes its confidence score is
discriminative; this theorem names the one quantity, $\Delta(\lambda)$, that
carries that assumption and gives it a sign test and a magnitude. A score
that is well-calibrated in the usual sense (its numeric value matches a
frequency) can still have $\Delta(\lambda)=0$ and buy nothing from
abstaining — separability and calibration are different properties of the
same score. This is the wiki's own reading of the two results together, not
a claim the source states in these terms.[^c4]

## Limits

- Proved for the marginal, unconditional distribution over $(\nu,\hat
  y=Y)$; it says nothing about separability varying by input difficulty or
  subgroup.
- Requires $p_v\in(0,1)$ (both outcomes occur with positive probability);
  degenerates at $p_v\to 0,1$, where the accuracy-gain prefactor $p_v(1-p_v)$
  vanishes regardless of $\Delta(\lambda)$.
- The closed-form gain (Theorem 1, Corollary 3.2) is exact for the specific
  weighted-vote confidence $\nu$ this paper defines; the definition of
  $\Delta(\lambda)$ transfers to any scalar confidence score, but the
  formula's asymptotic convergence rate is stated only under a Glivenko–
  Cantelli argument in the paper's appendix, which this note did not read.

## Related

[[abstention]] · [[crc-confident-error-control]] · [[roc-curve]] · [[semantic-entropy]]

[^c1]: gu-2026-pause — "We call the score separable at λ if ∆(λ) > 0."
[^c2]: gu-2026-pause — "the gain is multiplicatively driven by the separability gap ∆(λ): a score with ∆(λ) = 0 produces zero accuracy gain regardless of how many paths are sampled or how aggressively λ is set."
[^c3]: gu-2026-pause — "If ∆(λ) ≤ 0, then Ac (λ) ≤ pv , with equality iff ∆(λ) = 0. In particular, a score with ∆(λ) ≤ 0 at every λ > 0 cannot improve selective accuracy via abstention at any threshold."
[^c4]: gu-2026-pause — "the gain is multiplicatively driven by the separability gap ∆(λ): a score with ∆(λ) = 0 produces zero accuracy gain regardless of how many paths are sampled or how aggressively λ is set."
