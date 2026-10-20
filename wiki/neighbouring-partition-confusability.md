---
description: "When clustering by noisy yes/no same-cluster queries, the hardest wrong answer is always one merge or one split away, so the query cost lower bound is set by neighbouring partitions only."
aliases: ["closest alternative clustering", "min(C) reduction", "most confusing alternative partition"]
sources: ["arxiv-2602-05690"]
---
# Neighbouring-partition confusability

Setting: M items fall into an unknown number K of clusters. An agent may ask, for any pair, whether the two items share a cluster, and gets a noisy bit: 1 with probability p if they do, with probability q if they do not (q < 1/2 < p, both unknown).[^c1] The goal is to name the true partition with error at most delta using as few queries as possible.

## The lower bound and its hard part

Any delta-correct strategy needs, as delta goes to 0, expected queries at least ln(1/delta) divided by D*(C). D* is a sup-inf: the best allocation of queries over pairs, against the wrong partition (with its own p', q') that is hardest to tell apart from the truth, measured by summed KL divergence.[^c2] Taken literally the inner infimum ranges over every other partition, a count that grows super-exponentially in M (the Bell number).[^c3]

## The reduction

The paper proves that the infimum over all wrong partitions equals the infimum over only those reached from the truth by merging two clusters or splitting one in two.[^c4] In words: the partition most easily confused with the truth always has K-1 or K+1 clusters. Only the pairs whose same/different status flips between truth and alternative carry a large KL term, and a single merge or split flips the fewest. This is what makes the optimal allocation computable at all and what a sampling rule can target: spend queries on pairs that separate the true partition from its one-step neighbours.

Where the structure is symmetric the allocation is trivial. If K = 1 or K = M, every pair is equally informative and the optimal rule is uniform over pairs.[^c5] For other K there is no closed form for the optimal allocation.[^c6]

## What it says about asking

The implication is mine, not the paper's. Questions about whether two things belong together are not equally valuable: their value depends on which rival hypothesis is closest. Confirming that two items are in one group matters when the rival is a split of that group, and asking about unrelated pairs wastes queries. The worked example (K = M/2 clusters of two) gives a bound that scales like 1/Delta^2 with Delta = p - q and grows linearly in K.[^c7]

## Limits

Asymptotic in delta to 0 with p, q fixed; it is not a bound at moderate delta and not comparable directly with high-probability bounds of the order M K / Delta^2 from other works, as the authors say.[^c8] Answers are assumed independent Bernoulli with the same p and q for every pair; real oracles (people, models) have pair-dependent and correlated noise. The practical stopping statistic the paper actually runs is a relaxation of the GLR statistic, optimal only up to a constant factor. I read the statements, not the appendix proofs.

## Related

- [[plug-in-glr-stopping-rule]] — the GLR stopping rule that the paper's clustering algorithm uses and relaxes
- [[exploration-certification-trade-off]] — another pairwise-feedback identification problem with intrinsic cost split
- [[pac-best-arm-sample-complexity-lower-bound]] — the single-best-arm lower bound this extends to partitions

[^c1]: arxiv-2602-05690 — "We assume that the number of clusters K is not known beforehand."
[^c2]: arxiv-2602-05690 — "EC [τδ ] D∗ (C) ≥ KL Ber(δ), Ber(1 − δ) ,"
[^c3]: arxiv-2602-05690 — "known as the Bell number [41], grows super-exponentially in M ."
[^c4]: arxiv-2602-05690 — "Theorem 2 shows that if C has K clusters, the closest alternative instance to C must have either K + 1 or K − 1 clusters"
[^c5]: arxiv-2602-05690 — "the optimal sampling rule should follow a uniform sampling across all pairs of items."
[^c6]: arxiv-2602-05690 — "Despite the above simplification, no closed-form solution for Λ∗ (C) exists in general, except in the special case when"
[^c7]: arxiv-2602-05690 — "We compute the expected sample complexity in terms of ∆ = p − q and K on a simple example."
[^c8]: arxiv-2602-05690 — "Nonetheless, direct comparison is not possible due to the normalization ln(1/δ) and the limit as δ → 0."
