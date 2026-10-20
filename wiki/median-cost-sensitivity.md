---
description: "The median's social cost moves little when the facility shifts past few agents, so the median of a small random sample approximates the full-information social cost to within 1+ε."
aliases: ["sensitivity of the median", "sample median approximation", "sampled median facility location"]
sources: ["doi-10-48550-arxiv-2208-11787"]
---
# Median cost sensitivity

A median mechanism places one facility at the median of the agents' reported locations. On the line it is strategy-proof and minimizes total distance, so the full-information median is the benchmark. Sampling asks whether that benchmark survives when only a random subset of agents is consulted and the facility sits at the median of that subset.

The naive answer is no, because the median as a function is unstable: a single agent switching sides can move it arbitrarily far. The function of the median has an unbounded sensitivity.[^a3] The paper's observation is that the social cost of the median is not unstable: "the social cost of the median exhibits a sensitivity property."[^a1] Moving the facility from the full median to a point x with an α fraction of agents lying between them transfers cost from one side to the other: the cost the agents on one side gain is exactly what the agents on the other side lose, the proof observes that "if we transfer the facility from xm = median(I) to x the cumulative social cost of L and R remains invariant."[^a2] The lemma (Lemma 3.2) therefore bounds the cost at x relative to the optimum by a term of order α/(1−2α), a quantity that stays small whenever few agents separate x from the median.

The sample only has to land near the median in rank. As the number of agents grows, the rank of the sample's median converges to a continuous transformed beta distribution.[^a10] The sample size needed for a 1+ε approximation scales as Θ(1/ε²) for the expected-cost guarantee, which is the confidence-free case of a mechanism whose sample size is Θ(1/(δε)²) for confidence δ.[^a4] The guarantee is stated in expectation and, with the sample size scaled by the confidence level, with high probability.[^a9] The same argument extends to the median on simple open curves and to the coordinate-wise median in (R^d, ‖·‖₁).[^a5] Because the sampled rule is the median of a sample, it inherits strategy-proofness from the median itself.[^a6]

## Limits

- The guarantee is asymptotic in n. The theorems are stated while n goes to infinity, and the bound is on expected social cost relative to the full-information median, not on the location of the facility.
- The property does not extend to trees: "does not extend on trees, as implied by Proposition 3.12."[^a7]
- Sampling with several facilities fails on the line under the percentile mechanism: "sampling cannot provide meaningful guarantees w.r.t. the expected social cost when allocating" at least two facilities.[^a8]
- The sample is drawn uniformly at random. Whether a non-random or adversarial sample keeps the property is not addressed by the text I read; that is my inference, not a result.

## Related

- [[auction-communication-complexity]] — the same sample-then-decide device, used there to choose an auction price so that the bits elicited, not the social cost, are what the sample saves.
- [[asymmetric-price-elicitation]] — the auction version of this sampled step, where the sample's median-like statistic sets each round's price.

[^a1]: doi-10-48550-arxiv-2208-11787 — "the social cost of the median exhibits a sensitivity property"
[^a2]: doi-10-48550-arxiv-2208-11787 — "if we transfer the facility from xm = median(I) to x the cumulative social cost of L and R remains"
[^a3]: doi-10-48550-arxiv-2208-11787 — "the function of the median has an unbounded sensitivity"
[^a4]: doi-10-48550-arxiv-2208-11787 — "to be the size of the sample"
[^a5]: doi-10-48550-arxiv-2208-11787 — "simple approximation yields a social cost arbitrarily close to the optimal for the metric space"
[^a6]: doi-10-48550-arxiv-2208-11787 — "directly inherits its truthfulness from the Median"
[^a7]: doi-10-48550-arxiv-2208-11787 — "does not extend on trees, as implied by Proposition 3.12"
[^a8]: doi-10-48550-arxiv-2208-11787 — "sampling cannot provide meaningful guarantees w.r.t. the expected social cost when allocating"
[^a9]: doi-10-48550-arxiv-2208-11787 — "this guarantee is established both in terms of expectation"
[^a10]: doi-10-48550-arxiv-2208-11787 — "converges to a continuous transformed beta distribution"
