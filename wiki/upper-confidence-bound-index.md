---
description: "UCB1 picks the option maximizing mean plus a Hoeffding confidence radius; regret grows only logarithmically in plays, uniformly over time, with no distribution knowledge beyond bounded support."
aliases: ["UCB1", "upper confidence bound", "optimism in the face of uncertainty", "index policy"]
sources: ["auer-2002"]
---
# Upper-confidence-bound index

Setting: K options (arms) each yield independent rewards with unknown means. A policy chooses the next option from past plays; its regret is the expected loss from not always playing the best one.[^c1] The index policy scores each option by an upper confidence index and plays the highest. UCB1's index is the sum of two terms: the current average reward, plus a term tied to the size of the one-sided Chernoff-Hoeffding confidence interval within which the true mean falls with overwhelming probability.[^c2] An option is therefore tried either because it looks good or because it has been tried too little to rule out that it is good; exploration is not a separate step, it is the width of the interval.

## What was proved

- For any reward distributions with support in [0, 1], UCB1's expected regret after any number n of plays is bounded by a term of order 8 ln n / Δ_i per suboptimal option i (Δ_i = gap to the best mean) plus a constant.[^c3] The claim is "uniformly over n", not only asymptotically, and needs no preliminary knowledge of the distributions.[^c4]
- Lower bound context (Lai and Robbins): any allocation strategy must play each suboptimal machine about ln n / D(p_j || p*) times asymptotically, so logarithmic regret is the best possible order.[^c5]
- The UCB1 constant 8/Δ² is worse than Lai-Robbins' 1/D; the paper notes D ≥ 2Δ², so a constant near 1/(2Δ²) is the target. UCB2, which plays in exponentially growing epochs, brings the leading constant arbitrarily close to 1/(2Δ²), at the price of a second constant that blows up as its parameter alpha goes to 0.[^c6]
- Fixed-rate random exploration (epsilon-greedy with constant epsilon) gives linear regret. Letting epsilon decay as 1/n restores a logarithmic bound, but that proof needs a known lower bound d on the gap between the best and second-best option.[^c7]
- With normally distributed rewards of unknown mean and variance, an analogous index (UCB1-NORMAL) also gets logarithmic regret, though the proof rests on tail bounds verified only numerically (stated as conjectures).[^c8]
- Replacing the radius with one using the empirical variance (UCB1-TUNED) performed substantially better than UCB1 in the paper's experiments, but no regret bound was proved.[^c9]

## Limits

Rewards are assumed independent and identically distributed per option, stationary, independent across options, and bounded in [0, 1]; nothing is shown for drifting or adversarial rewards, or for option sets that change. The bounds hold in expectation, so a single run may do worse. The logarithm hides a constant that grows as gaps shrink (1/Δ²), so the guarantee is weak when options are nearly equal or the horizon is short. Reward must be observed immediately after each play. Whether any of this transfers to choosing which question to ask (where the reward of a question is not a scalar payoff) is my inference, not something the paper addresses. The UCB1-NORMAL result rests on unproved conjectures; UCB1-TUNED's advantage is empirical only.

## Related

- [[thompson-sampling]] — the Bayesian alternative; its Bayesian regret is bounded by that of any UCB rule built from the same confidence sets
- [[value-of-information]] — UCB gets exploration from interval width without computing information value
- [[information-directed-sampling]] — trades regret against information gain rather than using optimism
- [[information-ratio]] — a regret-versus-information quantity used for the same bandit regret analyses
- [[regret-based-clarification-evaluation]] — uses regret as the success measure

[^c1]: auer-2002 — "Thus the regret is the expected loss due to the fact that the"
[^c2]: auer-2002 — "The index of this policy"
[^c3]: auer-2002 — "Theorem 1. For all K > 1, if policy UCB1 is run on K machines having arbitrary reward"
[^c4]: auer-2002 — "achieving logarithmic"
[^c5]: auer-2002 — "Lai and Robbins also proved that this regret is"
[^c6]: auer-2002 — "we can bring"
[^c7]: auer-2002 — "the constant exploration probability ε causes a linear (rather than logarithmic) growth in"
[^c8]: auer-2002 — "achieves logarithmic regret uniformly over n without knowing means and variances of the"
[^c9]: auer-2002 — "performs substantially better than UCB1 in essentially"
