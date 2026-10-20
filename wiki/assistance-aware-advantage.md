---
description: "Under step-dependent reward decay, a correct answer's normalized advantage is never negative, is larger the earlier the correction, and vanishes once nearly everyone succeeds at that step."
aliases: ["Assistance-Aware Advantage", "Theorem 1 (SocraticPO)"]
sources: ["liu-2026-socraticpo"]
---
# Assistance-aware advantage

> A formal guarantee about how much credit a training signal should give an
> answer that only came after help: never punish it, but always credit a
> question answered earlier over the same question answered later, and let
> the credit collapse once help stops distinguishing anyone.

## Definition / Mechanism

Liu et al. (2026) decay the reward of a correct
answer by the historical average success rate of samples still active at
that step, then normalize it into an advantage
$\hat a_i^{(k)} = (r_i^{(k)} - \mu_t)/(\sigma_t + \epsilon)$, and prove three
properties of it (Theorem 1): "(Non-negativity) If sample i is correct at
step k... then â_i^(k) ≥ 0... (Monotonicity) If t ≥ 2 and samples i, j are
correct at step k, l (k < l)... then â_i^(k) > â_j^(l)... ([[saturation|Saturation]] decay)
Let p_k be the correction rate among active samples. Then if p_t → 1, we
have â_i^(t) → 0."[^c1]

The first property means an assisted-but-correct trajectory is never
trained against: "reward decay does not discard assisted successes; it
keeps them as valid positive learning signals."[^c2]

The third property is the anti-reward-hacking guarantee: once a round of
guidance makes almost every active sample correct, that round stops being
informative and its advantage collapses toward zero, "prevent[ing] the
student policy from gaining excessive advantage merely by relying on
teacher intervention."[^c3]

## Why it matters

This is a formal answer to "how much is a constraint worth once it arrived
late, with help": correctness alone is not enough credit — the theorem
prices an answer by *when* it stopped being needed, giving a training-time
counterpart to a [[value-of-information]] argument that decays with delay,
without invoking a utility function.

## Transfer

| | Home field (RL for LLMs) | Here (asking) |
|---|---|---|
| Object | training advantage of a token sequence | value credited to a constraint (answer) |
| Formalism | mean/std-normalized advantage over a decayed, step-indexed reward | a schedule that discounts a late, assisted answer relative to an early, independent one |
| Survives | the ordering guarantee (earlier beats later) and the saturation-to-zero property, for any step-indexed, batch-normalized reward, not just this RL loss | same |
| Does not survive | the guarantee is proved for one decay rule ($\mu_{k-1}\cdot\delta_i^{(k)}$) and one normalization; it is not a general theorem about information value, and does not show the schedule is optimal | same
[^c4.1][^c4]

## Limits

The proof (Appendix A of the source, not read here) is stated for this
exact decay rule and normalization; the note asserts only the three named
properties, not that this is the best or only such schedule. The paper
gives no result for how the decay rate should be set when steps are not
homogeneous (e.g. guidance of very different quality across rounds).

## Related

[[socraticpo]] · [[value-of-information]] · [[expected-information-gain]]

[^c1]: liu-2026-socraticpo
[^c2]: liu-2026-socraticpo — "reward decay does not discard assisted successes; it keeps them as valid positive learning signals."
[^c3]: liu-2026-socraticpo — "prevent the student policy from gaining excessive advantage merely by relying on teacher intervention."
[^c4.1]: liu-2026-socraticpo — "we introduce a reward decay mechanism for assisted correctness. We further characterize its normalized-advantage properties, showing non-negativity, monotonicity, and saturation decay."
[^c4]: liu-2026-socraticpo
