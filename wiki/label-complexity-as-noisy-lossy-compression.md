---
description: "Pool-based active learning maps to noisy lossy compression, so label complexity gets a finite-blocklength lower bound: a rate term plus a dispersion term separating overfitting from bias mismatch."
aliases: ["pool-based active learning as noisy lossy compression", "finite blocklength label complexity bound"]
sources: ["arxiv-2602-05333"]
---
# Label complexity as noisy lossy compression

A pool-based learner sees an unlabeled pool, chooses which instances to label, and trains. The work recasts this as noisy lossy compression: the learning target is the source symbol, the pool is a noisy observation of it through a channel, the selected labeled subset is the codeword (selection is encoding), and the learning algorithm is the decoder.[^c1] Standard lossy compression has one encoding step; noisy lossy compression splits it into channel transmission and encoding of the noisy symbol, which matches splitting data acquisition into pool observation and selection.[^c2]

## The quantity bounded

Label complexity is the minimum number of labels needed for a target error.[^c3] Here it is n*, the smallest training-set size for which some selection strategy keeps the probability that distortion exceeds d at or below epsilon, for a fixed (possibly randomized) learning algorithm A and pool size m.[^c4] The rate-distortion function R(m, d, A) is the minimum mutual information between pool and hypothesis, taken over selection strategies that meet average distortion d.[^c5]

## The bounds

Theorem 4.3 says epsilon cannot fall below the probability that the "tilted information" exceeds the labeled-data size (in bits) plus a slack gamma, minus e^-gamma, whatever the selection strategy.[^c6] Tilted information is a per-instance quantity whose expectation equals R(m, d, A); it is read as the minimum number of selected samples needed to get a hypothesis from this pool, with a correction term that grows when the hypothesis misses distortion d.[^c7]

Theorem 4.4 then gives, for any k, m, d, epsilon and A, R(k, m, d, epsilon, A) at least R(m, d, A) plus sqrt(V/k) Q^-1(epsilon) plus O(log k / k), where V is the variance of the tilted information (the rate-dispersion function).[^c8] So the minimum number of labels is a mean term (average difficulty of learning with A) plus a fluctuation term that shrinks as 1/sqrt(k) and grows with how strict the tolerated failure probability is.

## Decomposing the dispersion

V splits by the law of total variance into V_in, the expected within-target variance, and V_bet, the variance across targets of the conditional mean.[^c9] The authors read V_in as the overfitting or instability of A under variation in pool, training set and algorithmic randomness, and V_bet as the mismatch between the task and the inductive bias of A.[^c10] They connect components to overfitting measures in information-theoretic generalization bounds and to stability theory.[^c11] The reading of V_in as instability assumes the selection itself is nearly deterministic, because the optimal strategy picks optimal data.[^c12]

For the mechanism: a learner whose labels-needed varies a lot from pool to pool (unstable) or whose bias fits some targets and not others needs a larger safe label budget than its average suggests. This is the work's interpretation of the two variance terms; the proofs establish the bound, not the causal reading (my gloss).

## Limits

- It is a lower bound for a fixed algorithm under its optimal selection strategy; it does not give a practical selection rule or an achievability result in this text, and no empirical label savings were measured in the parts I read.
- It assumes an optimal strategy attaining the infimum exactly (Assumption III), finite third moment of tilted information and d inside (d_min, d_max).[^c13] These may not hold for real learners.
- The bound is asymptotic in k with an O(log k / k) remainder, so tightness at small label counts is not shown.
- The overfitting and inductive-bias interpretations are heuristic readings of variance terms.
- The mapping to question asking in general (human or LLM questioners) is my inference, not the paper's claim.

## Related

- [[rate-distortion-theory]] — the lossy-coding framework whose finite-blocklength refinement is used here
- [[mutual-information]] — R(m, d, A) is a constrained minimum of mutual information between pool and hypothesis
- [[source-coding-theorem]] — the lossless floor that the rate term generalizes to noisy, lossy settings
- [[optimal-question-asking]] — another information-theoretic account of how few queries suffice

[^c1]: arxiv-2602-05333 — "data selection to compression, and learning to decoding."
[^c2]: arxiv-2602-05333 — "This decomposition aligns with the requirement to split the"
[^c3]: arxiv-2602-05333 — "is to characterize label complexity, defined as the minimum number of labels required for a target error."
[^c4]: arxiv-2602-05333 — "is the minimum number of labels satisfying this condition,"
[^c5]: arxiv-2602-05333 — "R(m, d, A) denotes the minimum rate as k → ∞"
[^c6]: arxiv-2602-05333 — "This theorem demonstrates a fundamental limit: for"
[^c7]: arxiv-2602-05333 — "Thus, ȷ̃W ;U represents the required"
[^c8]: arxiv-2602-05333 — "referred to as the rate-dispersion function."
[^c9]: arxiv-2602-05333 — "V (m, d, A) = Vin (m, d, A) + Vbet (m, d, A),"
[^c10]: arxiv-2602-05333 — "as the degree of overfitting of A, and Vbet as the degree of"
[^c11]: arxiv-2602-05333 — "of R(m, d, A) and V (m, d, A) correspond to overfitting"
[^c12]: arxiv-2602-05333 — "that the randomness of the selection itself is minimal, since"
[^c13]: arxiv-2602-05333 — "has a finite absolute third moment."
