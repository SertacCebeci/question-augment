---
description: "Radial Dispersion Score sums the ℓ1 distances of unit-normalized sample embeddings from their mean: a training-free, model-agnostic reading of how far an LLM's sampled answers spread."
aliases: ["RDS", "radial dispersion", "total radial dispersion", "ℓ1 centroid dispersion"]
sources: ["arxiv-2512-04351"]
---
# Radial dispersion score

Sample one prompt N times, embed each generation with an external sentence encoder, and divide each embedding by its length. The results are unit vectors on a hypersphere. Their mean, the empirical centroid ū, is one point inside that sphere. The radial dispersion score is the total ℓ1 distance of the points from that centroid:[^r1] RDS(x) = Σᵢ ‖uᵢ − ū‖₁. A tight set of answers stays near its centroid and scores near zero. Answers that scatter across the sphere score high. The authors say the score measures "the radial dispersion of sampled generations in embedding space",[^r2] so it reads spread of meaning as spread of position, not as the mass a model puts on discrete answers.

The design point that separates it from the clustering family is that it "avoids semantic clustering, does not access hidden states, and requires no calibration or" model internals.[^r3] There is no entailment model and no cluster boundary to tune. The cost is that the geometry belongs to the encoder: two answers are "close" only where the chosen sentence embedder puts them close.

**The weighted form.** RDSw weights each sample by a normalized likelihood pᵢ, estimated from the average negative log-likelihood of the generation, and measures dispersion around the weighted mean ūw = Σ pᵢuᵢ. The stated purpose is to emphasize "high-probability outputs while reducing the impact of low-probability, potentially noisy" generations.[^r4] The authors identify RDSw with the 1-Wasserstein distance between the sampled distribution and its barycenter, and argue this gives "a geometric foundation for its stability and sensitivity".[^r5] The closed form is what makes it cheap: "This closed-form expression makes RDSw computationally trivial (no optimization required)".[^r6]

**Why the unsquared sum.** The paper's Proposition 1 places RDS above the trace-based score EigenEmbed (the mean squared distance from the centroid). "Equality in (2) holds if and only if all ui are identical",[^r7] so the ℓ1 sum is strictly larger wherever the samples differ. The authors choose ℓ1 because it "responds more strongly to large deviations in the embedding space".[^r8] They also state that "Theoretically, RDS lower-bounds the trace of the embedding" covariance, and so keeps a monotonic link to differential entropy.[^r9] That link is conditional on treating the embeddings as Gaussian: the entropy formula is written for the case "Approximating the conditional distribution of embedding vectors as Gaussian".[^r10]

**What was measured.** The evaluation asks how well each score ranks correct against incorrect greedy answers: "we measure the ability of each uncertainty score to separate correct from incorrect greedy generations".[^r11] Over 16 model–dataset pairs (four open-weight models, four free-form QA and maths datasets, N = 10 samples by default), "On average, RDSw achieves the highest AUC of 79.7%, followed by RDS and RDSℓ2 at 78.9% and 78.2%".[^r12] The margin over the next best baseline, EigenEmbed, is 2.1 points for RDSw and 1.3 for RDS. The largest gains are on the arithmetic sets, where answers differ by a single character and the paper argues the trace-based score fails to register that separation.

The sample-count ablation shows the weighted form holding up as N grows: on GPQA, "RDSw shows essentially no degradation and achieves the" highest AUC at N = 40, while the clustering baselines peak at N = 10 and fall.[^r13] The encoder ablation finds the weighted form stable: "RDSw remains highly stable on SVAMP".[^r14]

## Limits

- **Discrimination, not calibration.** The reported quantity is AUC for separating right from wrong answers. The sections read report no calibration of RDS as a probability, and none of the thresholds a user would act on.
- **Small average margins.** The gap to the best baseline is one to two AUC points averaged over 16 settings. The paper says RDSw "ranks first in 10 out of 16 settings",[^r15] so it is not first in six. The text reports no variance over seeds or resamples.
- **Encoder dependence is only partly settled.** Larger sentence encoders, on the paper's own account, lower the scores on GPQA while the weighted form stays stable on SVAMP. The GPQA degradation is not a null result; it means the choice of encoder moves the number, and the authors offer no rule for picking one.
- **The N ablation is narrow.** It runs on one model (Falcon3-7B) and two datasets: "we use Falcon3-7B for experiments over two representative datasets: GPQA and SVAMP".[^r16] The paper's claim that RDS-based metrics are "uniquely tolerant to noisy generations"[^r17] rests on that setting.
- **Black-box applicability is argued, not run.** The text says the metric is "compatible with any black-box" LLM.[^r18] Every experiment uses open-weight models, with probabilities available, so the black-box case is untested here.
- **Greedy correctness as the target.** The score is judged against correctness of the greedy answer. Whether high dispersion predicts the wrongness of a single user-facing answer, rather than the greedy one, is the paper's assumption.
- **Ranking and selection are untested.** The authors name them as the next use: "Future work could extend RDS to" broader comparison, ranking and consensus tasks.[^r19]
- **Meaning is not measured.** The paper equates geometric dispersion on the sphere with semantic variability. That is the encoder's claim about meaning, which the paper does not validate against human judgments of equivalence (my inference from the evaluation, which uses only correctness labels).

## Related

- [[centroid-cancellation]] — why the trace-based score saturates where this one keeps growing
- [[semantic-entropy]] — the clustering measure this score is offered as an alternative to
- [[vendi-score]] — another effective-count reading of a sample set, from its similarity spectrum rather than from centroid distances
- [[paraphrase-group-hallucination-dispersion]] — dispersion across rewordings of a prompt, where this note's dispersion runs across samples of one prompt
- [[entropy]] — the quantity the score is said to track, and only through the Gaussian approximation above

[^r1]: arxiv-2512-04351 — "the total ℓ1 distance from the empirical centroid, i.e., the mean embedding"
[^r2]: arxiv-2512-04351 — "measures the radial dispersion of sampled generations in embedding space"
[^r3]: arxiv-2512-04351 — "avoids semantic clustering, does not access hidden states, and requires no calibration or"
[^r4]: arxiv-2512-04351 — "high-probability outputs while reducing the impact of low-probability, potentially noisy"
[^r5]: arxiv-2512-04351 — "providing a geometric foundation for its stability and sensitivity"
[^r6]: arxiv-2512-04351 — "This closed-form expression makes RDSw computationally trivial (no optimization required)"
[^r7]: arxiv-2512-04351 — "Equality in (2) holds if and only if all ui are identical"
[^r8]: arxiv-2512-04351 — "it responds more strongly to large deviations in the embedding space"
[^r9]: arxiv-2512-04351 — "Theoretically, RDS lower-bounds the trace of the embedding"
[^r10]: arxiv-2512-04351 — "Approximating the conditional distribution of embedding vectors as Gaussian"
[^r11]: arxiv-2512-04351 — "we measure the ability of each uncertainty score to separate correct from incorrect greedy generations"
[^r12]: arxiv-2512-04351 — "On average, RDSw achieves the highest AUC of 79.7%"
[^r13]: arxiv-2512-04351 — "RDSw shows essentially no degradation and achieves the"
[^r14]: arxiv-2512-04351 — "RDSw remains highly stable on SVAMP"
[^r15]: arxiv-2512-04351 — "RDSw ranks first in 10 out of 16 settings"
[^r16]: arxiv-2512-04351 — "we use Falcon3-7B for experiments over two representative datasets: GPQA and SVAMP"
[^r17]: arxiv-2512-04351 — "Overall, RDS-based metrics are uniquely tolerant to noisy generations"
[^r18]: arxiv-2512-04351 — "compatible with any black-box"
[^r19]: arxiv-2512-04351 — "Future work could extend RDS to"
