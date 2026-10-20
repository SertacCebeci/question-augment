---
description: "Summing two agents' confidences in log-odds overcounts when their signals are correlated; a validation-fitted shared discount below 1 improves calibration and leaves the ranking unchanged."
aliases: ["shared dependence discount", "log-odds fusion discount", "dependence correction for log-odds pooling", "logit-space evidence discount"]
sources: ["doi-10-48550-arxiv-2606-13591"]
---
# Log-odds dependence discount

Two confidences can be pooled by converting each to log-odds, ℓ = log(c / (1 − c)), and adding the results. For two streams that agree on an answer, the pooled value σ(ℓ1 + ℓ2) is the posterior probability that the shared answer is right, and this reading holds only "given agreement under independent evidence."[^c1] When the streams disagree, the rule keeps the more confident stream and reports the posterior that it is the correct one.[^c2] The arithmetic is that of independent Bayesian updates, and its premise is the weak point. In a debate, the two agents have read each other's reasoning, so the premise fails. "Naive fusion treats the two streams as independent evidence."[^c3]

The work states the failure directly: "multiagent interaction inevitably introduces information redundancy and correlated errors."[^c4] Its correction is a single shared discount parameter w, applied to the pooled evidence: σ(w(ℓ1 + ℓ2)) for agreement and σ(w|ℓ1 − ℓ2|) for disagreement. The authors say the parameter "scales the total log-odds evidence,"[^c5] and that w < 1 "indicates that the two agents partly repeat" the same evidence.[^c6] Because the same positive w multiplies both streams, the order of examples is unchanged, so the authors "expect no change in discrimination (AUARC)" while calibration improves.[^c7] With T = 1/w, the correction is an output temperature, which the authors note: "Mathematically, this can be viewed as a post hoc temperature."[^c8]

The mechanism was measured on validation data. The discount factor was fitted "on validation data" rather than derived.[^c9] Across 30 model pairs, two confidence estimators and two fused protocols, "the fitted value was below 1 in 118 of 120 settings," with a median of 0.65.[^c10] For the gated protocol CGF, raw ECE falls "from 0.100 to 0.055 under sequence probability" and "from 0.112 to 0.063 under self-report."[^c11] Across the same settings the AUARC moves by at most "0.00148,"[^c12] and the authors report the correction "without changing the final decisions."[^c13] The reading the authors give is that dependence "affects calibration rather than discrimination,"[^c14] and that the cost of the violated assumption is "a one-scalar confidence-scale" error.[^c15]

## Limits

- The setting is two agents and one round. "This work is limited to the two-agent, one-round" setting.[^c16] The authors say the fusion rule "can extend to more streams" (three agents, for example), but they "leave a systematic study of larger and multi-round" systems to future work.[^c17] Neither extension was measured here.
- The discount can only shrink evidence, since w is restricted to (0, 1]. This is by construction, not a finding. The fitted values landed below 1 in almost every setting, which is consistent with the restriction but does not test it.
- The discount cannot change the ranking. A system whose confidences discriminate poorly is not repaired by it. The work's own ablation puts the gain in gating and fusion, not in the discount.
- The 0.65 median describes these 30 pairs and two estimators. Whether a w fitted on one benchmark transfers to other models or tasks is not shown in the parts read. Reading it as a constant of nature would be my inference, not the authors' claim.
- What transfers from the older pooling literature is the arithmetic. The work places its rule among "logarithmic pooling, which combines probabilities in log space,"[^c18] and its probability reading (the posterior) is what breaks under debate. My inference: the sum and the one-scalar fix survive the transfer; the claim that the sum is a posterior does not survive without the independence the debate removes.
- The premise is stated as an assumption: "Naive log-odds fusion treats the surviving confidence streams as conditionally" independent.[^c19] The work measures the consequence (miscalibration) but does not measure the size of the correlation between the two agents directly.

## Related

- [[likelihood-ratio]] — additive log-odds accumulation under the same independence premise; the discount is a scalar correction to that sum
- [[surprisal]] — additivity of evidence needs independence; correlated answers double-count
- [[redundancy-over-diversity-in-evidence-aggregation]] — repeated evidence read as if it were independent
- [[accuracy-error-correlation-coupling]] — correlated errors make agreement weaker evidence than a headcount suggests
- [[confidence-gated-fusion]] — the gated protocol whose surviving streams this discount corrects
- [[confidence-weighted-debate-submartingale]] — confidence-weighted counting in debate under a different model

[^c1]: doi-10-48550-arxiv-2606-13591 — "given agreement under independent evidence"
[^c2]: doi-10-48550-arxiv-2606-13591 — "reports the posterior probability that Stream 1"
[^c3]: doi-10-48550-arxiv-2606-13591 — "Naive fusion treats the two streams as independent evidence"
[^c4]: doi-10-48550-arxiv-2606-13591 — "multiagent interaction inevitably introduces information redundancy and correlated"
[^c5]: doi-10-48550-arxiv-2606-13591 — "scales the total log-odds evidence"
[^c6]: doi-10-48550-arxiv-2606-13591 — "w < 1 indicates that the two agents partly repeat"
[^c7]: doi-10-48550-arxiv-2606-13591 — "we expect no change in discrimination (AUARC)"
[^c8]: doi-10-48550-arxiv-2606-13591 — "Mathematically, this can be viewed as a post hoc temperature"
[^c9]: doi-10-48550-arxiv-2606-13591 — "fitting a shared discount factor w on validation data"
[^c10]: doi-10-48550-arxiv-2606-13591 — "the fitted value was below 1 in 118 of 120 settings"
[^c11]: doi-10-48550-arxiv-2606-13591 — "raw ECE drops from 0.100 to 0.055 under"
[^c12]: doi-10-48550-arxiv-2606-13591 — "maximum absolute AUARC change of 0.00148"
[^c13]: doi-10-48550-arxiv-2606-13591 — "changing the final decisions"
[^c14]: doi-10-48550-arxiv-2606-13591 — "affects calibration rather than discrimination"
[^c15]: doi-10-48550-arxiv-2606-13591 — "the main cost of the violated independence assumption is a one-scalar confidence-scale"
[^c16]: doi-10-48550-arxiv-2606-13591 — "This work is limited to the two-agent, one-round"
[^c17]: doi-10-48550-arxiv-2606-13591 — "we leave a systematic study of larger and multi-round"
[^c18]: doi-10-48550-arxiv-2606-13591 — "logarithmic pooling, which combines probabilities in log space"
[^c19]: doi-10-48550-arxiv-2606-13591 — "Naive log-odds fusion treats the surviving confidence streams as conditionally"
