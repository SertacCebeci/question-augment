---
description: "Keep the softmax maximum as the confidence, but learn a residual-risk predictor and a per-input gate deciding how far to trust it; this ranks correct above wrong answers better than a fixed blend."
aliases: ["Adaptive Confidence Refinement", "ACR", "residual risk head with confidence gating"]
sources: ["arxiv-2602-04924"]
---
# Input-adaptive confidence refinement

Maximum softmax probability (MSP) is the usual score for deciding whether to answer or abstain. The work shows it is the ideal score only under a strong condition, then repairs it without discarding it. The work states: "the Maximum Softmax Probability (MSP) is Bayes-optimal only under strong calibration, a condition usually not met in deep neural networks, particularly in multimodal models."[^c1]

## Mechanism

Adaptive Confidence Refinement (ACR) keeps MSP as the primary signal and adds two learned heads on a frozen answering model. A Residual Risk Head (RRH) "exploits intermediate multimodal features to model uncertainty beyond MSP, especially in overconfident failure cases." A Confidence Gating Head (CGH) "determines when to apply residual risk corrections, enabling the input-adaptive fusion."[^c2] The final confidence is a per-input convex mix: α(x)·C_M(x) + (1 − α(x))·C_R(x), where C_M is MSP and C_R the residual estimate.[^c3]

Training is two-stage. The answerer is trained normally and frozen. Then both heads are trained jointly with binary cross-entropy against whether the answer was correct, so the score approximates P(correct | x). Because the backbone is frozen, confidence learning does not disturb the classifier, and accuracy is unchanged. Only the ranking of answers by confidence changes.[^c4]

## What is claimed

Theory (proved in the work's appendix, under assumptions): a fixed blend of two estimators with the optimal weight beats either alone in mean squared error. If the best weight varies across inputs, no single fixed weight is optimal, because input-dependent weights enlarge the class of confidence functions.[^c5] The authors also check that the learned weights do not collapse to 0 or 1, which would mean the gate was doing nothing.[^c6]

Empirical setting: audio-visual question answering, where audio, vision and language can conflict. On MUSIC-AVQA, the strong QA-TIGER model reaches over 77% accuracy yet with MSP "can answer only about 14% of questions to maintain a 1% error rate."[^c7] ACR is reported to give the best risk-coverage trade-offs against MSP, Monte Carlo dropout, temperature-style calibration and Doctor across three datasets and three backbones, including distribution shift and biased splits.[^c8]

An ablation found that the heads work best on the final fused multimodal features. Feeding every modality's features in degraded results, which the authors attribute to cross-modal misalignment.[^c9] Head architecture mattered less than input features and the training objective.[^c10]

## Limits

- The gains are measured on three audio-visual QA datasets only. Whether a learned residual helps for text-only question answering or open-ended generation is not tested here.
- The theorems assume the optimal weight is representable and that the two estimators' errors are sufficiently spread apart; the authors check this empirically, not in general.
- Coverage at low risk stays far from an oracle: the gap at 1% risk exceeds 60 points, so the method narrows but does not close the problem.[^c11]
- It needs correctness labels for a training set and a frozen model; it is not a zero-shot confidence.
- My inference: the per-input gate is the useful idea, since it lets the score defer to MSP where MSP is already trustworthy. The work's ablations of fixed versus adaptive weights are not reproduced here.

## Related

- [[calibration]] — MSP's optimality requires calibration, which is what fails here
- [[hy-hybrid-confidence-estimator]] — another fusion of two weak confidence signals, with fixed rather than input-dependent weights
- [[selective-abstraction]] — same risk-coverage evaluation, applied to claims in long answers

[^c1]: arxiv-2602-04924 — "the Maximum Softmax Probability (MSP) is Bayes-optimal only under strong"
[^c2]: arxiv-2602-04924 — "The CGH determines when to apply residual risk corrections, enabling the input-adaptive fusion."
[^c3]: arxiv-2602-04924 — "CACR (x) = α† (x)CM (x)+(1−α† (x))CR (x)"
[^c4]: arxiv-2602-04924 — "By freezing the backbone, we decouple confidence estimation from"
[^c5]: arxiv-2602-04924 — "input-adaptive fusion expands hypothesis class of confidence estimators"
[^c6]: arxiv-2602-04924 — "confirming"
[^c7]: arxiv-2602-04924 — "method can answer only about 14% of questions to maintain"
[^c8]: arxiv-2602-04924 — "ACR consistently achieves stateof-the-art risk-coverage trade-offs"
[^c9]: arxiv-2602-04924 — "feeding all modalities into ACR (last row) degrades performance due to cross-modal misalignment"
[^c10]: arxiv-2602-04924 — "rather than on the architecture’s complexity alone."
[^c11]: arxiv-2602-04924 — "Tab. 1 shows C@1%"
