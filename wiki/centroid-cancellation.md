---
description: "When sampled answers split into groups pointing in opposite directions, their mean embedding cancels toward zero, so a trace-of-covariance score saturates while the actual spread keeps growing."
aliases: ["mean-vector cancellation", "antipodal saturation", "opposing-cluster saturation"]
sources: ["arxiv-2512-04351"]
---
# Centroid cancellation

Take N sampled answers, embed each one and scale it to unit length. A set of unit vectors has a mean, the centroid, and the length of that mean depends on how the vectors are arranged. If the answers form one tight group, the mean keeps nearly full length. If they form two or more tight groups pointing in roughly opposite directions, the mean shrinks toward zero. The paper's description of this regime is that "multiple tight semantic clusters lie in roughly opposite directions on the hypersphere, resulting in a strong cancellation of the" mean vector.[^x1]

The measure that suffers is the one built from distances to the centroid in squared form. The paper calls it EigenEmbed: the EigenScore of Chen et al. computed on external embeddings instead of hidden states. EigenScore is "the trace of the covariance", which for unit vectors equals the average squared distance from the mean.[^x2][^x3] It behaves well at the low end, since it "approaches 0 when embeddings collapse (low uncertainty)".[^x4] At the high end it stops moving. When the centroid is at zero, "the embeddings form a perfectly" balanced configuration around the origin, and the score sits at its ceiling of 1.[^x5] The paper's phrase for the effect is that the score is "causing EigenEmbed to saturate near 1 despite growing structural" disagreement.[^x6]

The mechanism is arithmetic, not a fitted property. Once the centroid is near zero, the squared-distance sum is pinned at its maximum no matter how much further apart the groups move, because the mean already absorbs the separation. An unsquared ℓ1 sum of distances does not share this ceiling in the same way. The paper states that "RDS scales with the magnitude of these opposing directions",[^x7] which is why it is offered as the replacement in [[radial-dispersion-score]].

The regime is also a signature in its own right. The paper shows that a zero centroid forces the average pairwise cosine to be negative, and reads this as the geometry of disagreement: "This negative-average structure is a geometric signature of semantic disagreement".[^x8] So the cancellation is not only a failure of one estimator; it marks samples whose members point against each other, which is the case the paper calls "a prevalent failure mode in which LLMs produce" overconfident but contradictory answers.[^x9]

## Limits

- **The saturation is shown in the extremal case.** The ceiling at 1 is an analytic result for a zero centroid, and Figure 1 illustrates it with ten two-dimensional vectors. The paper does not show with real LLM samples how often the centroid actually reaches zero, or how much accuracy the saturation costs.
- **"Prevalent" is asserted.** The claim that opposing clusters are a common failure is made in the framing; the sections read give no frequency measurement for it.
- **The gain is modest in the reported results.** The paper names EigenEmbed as the "next best" method on average, "surpassing the next best (EE)",[^x11] and the ℓ1 variant leads it by 1.3 AUC points for RDS and 2.1 for RDSw. Whether the saturation is the reason is the paper's reading, not a controlled ablation.
- **Weighting changes the centroid.** The probability-weighted variant uses a weighted mean, so its cancellation depends on the weights as well as the geometry. The paper does not analyse this case separately (my inference from the definitions).
- **The geometry is encoder-specific.** Whether two answers sit on opposite sides of the sphere depends on the sentence embedder. A different encoder can move answers into or out of opposition, and the paper reports only a few encoders.
- **Entropy link is conditional.** The trace is said to be proportional to differential entropy under a Gaussian approximation, which the paper states as an assumption, not a result about LLM output distributions.[^x10]

## Related

- [[radial-dispersion-score]] — the ℓ1 dispersion built to keep growing where this score saturates
- [[entropy]] — the quantity the trace is a proxy for, under the Gaussian approximation
- [[semantic-entropy]] — the clustering route, which avoids cancellation by discrete grouping and pays with the brittleness of cluster boundaries

[^x1]: arxiv-2512-04351 — "roughly opposite directions on the hypersphere, resulting in a strong cancellation of the"
[^x2]: arxiv-2512-04351 — "uses the trace of the covariance"
[^x3]: arxiv-2512-04351 — "EigenScore equals the average squared"
[^x4]: arxiv-2512-04351 — "it approaches 0 when embeddings collapse (low uncertainty)"
[^x5]: arxiv-2512-04351 — "When the centroid is at zero, the embeddings form a perfectly"
[^x6]: arxiv-2512-04351 — "causing EigenEmbed to saturate near 1 despite growing structural"
[^x7]: arxiv-2512-04351 — "RDS scales with the magnitude of these opposing directions"
[^x8]: arxiv-2512-04351 — "This negative-average structure is a geometric signature of semantic disagreement"
[^x9]: arxiv-2512-04351 — "a prevalent failure mode in which LLMs produce"
[^x10]: arxiv-2512-04351 — "Approximating the conditional distribution of embedding vectors as Gaussian"
[^x11]: arxiv-2512-04351 — "surpassing the next best (EE)"
