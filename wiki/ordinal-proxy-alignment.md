---
description: "A proxy objective is aligned when it ranks outputs as the stakeholder's true utility does, not when its values match; a weighted-rubric proxy is judged by that ordering."
aliases: ["ordinal equivalence of proxy and true utility", "order-preserving proxy", "functional alignment", "proxy ordinal equivalence"]
sources: ["arxiv-2512-06196"]
---
# Ordinal proxy alignment

A system that optimizes a reward or a rubric optimizes a proxy for what the stakeholder actually values. The usual question is how close the proxy's numbers come to the true utility. This work asks a narrower question: does the proxy order outputs the way the true utility does? It defines a system as functionally aligned when its proxy is "ordinally equivalent to the stakeholder's true utility" across the outputs the joint policy can produce, and it gives the reason that matters for optimization: "optimizing this proxy yields the same optimal policy as optimizing the true utility".[^c1]

The mechanism follows from that definition. If the proxy is a positive monotone transformation of the true utility over the policy's outputs, then the best output under one is the best under the other, and any error in the proxy's scale is harmless. The proxy here is a rubric: a set of criteria, each with a weight and a verifier, whose weighted sum is the score. The rubric is "a set of weighted, verifiable criteria that jointly define a linearly additive proxy utility".[^c2] Under the ordinal test, what a rubric has to get right is the ranking of candidate outputs, not the size of its numbers. This is my reading of the paper's definition, not a result it reports as such.

The same ordering target is used to justify different kinds of supervision. The paper argues that any "strictly proper supervision operator", whether pointwise scores, pairwise comparisons, listwise rankings or rubric evaluations, "identifies the same ordering of U ∗ on the decoding support".[^c4] So the test is about which ordering a signal recovers, not about which format produced it.

Measured effect. The paper reports average true return across 44 held-out tasks, and the ordering claim is tied to that outcome. At one sample per task the mean return "rises modestly from 0.58" with no rubric to 0.62 with a GSPO-trained rubric manager. At best-of-eight, the reported means are 0.6817 for the SFT manager and 0.7460 for the GSPO manager, with a one-sided Wilcoxon test giving "p=0.0182 at N=8" for GSPO against SFT.[^c3] [^c5] The gains are modest and they are measured on the true return, not on the rank agreement that the ordinal definition calls for.

## Limits

- The equivalence is a definition plus an argument the paper says is in its appendix. I did not reproduce that argument, and the claim that order-equivalence survives every supervision format is the authors' statement.
- The condition is required only "across the support of the joint policy". A proxy that ranks well on the outputs it was fit to can rank badly on outputs a changed policy would produce. The text read here does not test that.
- The "true" utility is not observed. In the experiments it is defined by expert-written gold rubrics: "we instantiate O using gold rubrics". The ordinal target is therefore itself a rubric, and the measured gains are gains against that rubric.[^c6]
- The paper's rank-agreement evaluation (its faithfulness question) was not read in this pass; the evidence above is about mean return, which does not by itself show ordering agreement.
- Ordinal equivalence says nothing about how far apart outputs are, so it cannot justify a trade-off that needs magnitudes, such as a fixed quality threshold or a cost-weighted choice.

## Related

- [[reward-overoptimization]] — a proxy that tracks the objective inside the training distribution can separate from it as optimization pushes on it; the ordering test is the condition that has to hold for the proxy to be safe.
- [[within-group-ordinal-utility-aggregation]] — another route that reduces a reward to ordinal judgments over a group of samples, without the rubric.
- [[question-specific-rubric]] — the weighted criteria that the proxy sums, and why partial credit over them differs from a binary verdict.
- [[rubric-formation-gap]] — the same family of work finds that deciding what to check, not how to weight it, is the bottleneck.
- [[difficulty-weighted-clarification-cost]] — the cost term in the same paper's manager objective, which sets how many clarifying questions go into the rubric.

[^c1]: arxiv-2512-06196 — "ordinally equivalent to the stakeholder’s true utility"
[^c2]: arxiv-2512-06196 — "that jointly define a linearly additive proxy utility"
[^c3]: arxiv-2512-06196 — "mean return rises modestly from 0.58"
[^c4]: arxiv-2512-06196 — "identifies the same ordering of U ∗ on the decoding support"
[^c5]: arxiv-2512-06196 — "p=0.0182 at N=8"
[^c6]: arxiv-2512-06196 — "we instantiate O using gold rubrics"
