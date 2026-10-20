---
description: "Averaging an answer-or-abstain reward over a prior on risk thresholds gives a strictly proper scoring rule for stated confidence; a uniform prior gives the Brier score."
aliases: ["behavioral calibration", "risk-threshold reward averaging", "threshold-averaged proper score"]
sources: ["arxiv-2512-19920"]
---
# Risk-averaged abstention reward

A model that may say "I don't know" faces a decision with a price. Behavioral calibration, the framework that Wu et al. take from Kalai et al., asks that a model adjust its refusal to a user-specified risk threshold t, so that it gives a substantive answer only when its confidence clears that threshold.[^c1] The ideal rule is stated as "if and only if its probability of correctness exceeds the risk tolerance threshold t."[^c2]

Trained directly, this rule is a reward for each threshold. A correct answer scores +1, a wrong answer scores -1, and abstaining scores 2t - 1.[^c3] Under that reward, answering with probability p of being correct is worth 2p - 1, so answering beats abstaining exactly when p > t. This is the one-threshold decision; the difficulty is that a model trained on sampled thresholds receives a different reward on every example, and the paper finds that this does not produce a usable policy (see Limits).

The move that makes the rule trainable is to stop sampling t. The model reports one scalar confidence p, and the decision for any threshold is read off it: "abstain if and only if p < t."[^c4] The reward for that report is the threshold-specific reward averaged over a prior u(t) on the threshold. The averaged reward is maximized, the paper says, when the reported p equals the probability that the answer is valid, and it is strictly proper provided the prior has positive density everywhere.[^c5] The text states this as a verifiable fact and does not show the integral in full.

The choice of prior sets the shape of the reward. With a uniform prior the average is "analogous to the Brier score," and it decomposes into a correctness term and a Brier term on the confidence.[^c6][^c7] With a truncated Beta-type prior that puts weight at the extremes of the threshold range, integrating the reward "yields a cross-entropy style reward function."[^c8] The paper reads that form as penalizing confident errors and timid correct answers more strongly: "This formulation imposes stronger penalties for overconfidence on wrong answers."[^c9] It trained the Beta variant with GRPO because it "discover[ed] improved training stability specifically for this reward design."[^c10]

The contrast is the explicit-threshold strategy. There the threshold is written in the prompt and sampled during training. The paper reports that the "refusal rate and hallucination rate proved insensitive to the specific prompt input t during inference," and that sampling t creates a noisy landscape in which the model "struggles to learn a coherent strategy for adaptive conditions from" t = 0 to t = 1.[^c11][^c12] Moving the threshold out of the prompt and into the scoring rule is the paper's stated remedy.

## Limits

Propriety is asserted, with the proof left to the reader ("one can verify"). The text read here does not carry the integral, so the propriety claim is taken from the authors, not reproduced. The clipped cross-entropy form also replaces p by a clip to a margin epsilon, so the bound on the penalty is set by that margin, a choice the text makes without a sensitivity result I could read.[^c13]

Every experiment in the parts read uses one base model: "We apply behavioral calibration to finetune Qwen-3-4B-Instruct-2507."[^c14] The gain is reported in-domain on a math benchmark and, for factuality, as calibration error rather than the same ratio.[^c15] Other base models, and whether the averaged reward holds its advantage at larger scale, are not tested in what I read.

The reward needs a correctness label for each answer. In the claim-level extension the label comes from a judge: "which is determined by an LLM Judge."[^c16] The response-level label source was not read here, so the reward is only as good as that label.

The prior is itself a modeling decision. The paper says the formulation removes the need to hand-tune a balance between calibration and accuracy, but the choice between a uniform and a Beta prior changes the reward, and the text gives a stability reason, not a reason tied to any user's actual risk distribution. Whether a deployment's threshold distribution resembles either prior is not addressed.

Whether a model trained on the averaged reward changes what it asks, or when it stops asking, is not tested in this work.

## Related

- [[calibration]] — the property the averaged reward is built to make true of the reported confidence.
- [[log-score-verbalized-confidence-reward]] — a log-rule reward on confidence tokens; the cross-entropy form here is a related log-type target, and whether the two coincide is not checked in either note.
- [[confidence-report-repair]] — removes abstention from training and thresholds the confidence only at deployment; the same threshold rule, applied after training.
- [[penalty-invariant-abstention-confidence-action-dissociation]] — a different paper finding the same kind of gap: a prompted cost or threshold that does not move the answer-or-abstain decision.
- [[margin-separated-calibration-reward]] — also concerns how a Brier-type calibration term combines with correctness; this note does not test that interaction.

[^c1]: arxiv-2512-19920 — "Behavioral calibration posits that a trustworthy model should"
[^c2]: arxiv-2512-19920 — "if and only if its probability of correctness exceeds the risk tolerance threshold t."
[^c3]: arxiv-2512-19920
[^c4]: arxiv-2512-19920 — "abstain if and only if p < t."
[^c5]: arxiv-2512-19920 — "A strictly proper scoring rule implies that the expected reward is maximized exactly when"
[^c6]: arxiv-2512-19920 — "reward function is analogous to the Brier score."
[^c7]: arxiv-2512-19920 — "This reward function can be decomposed into the sum of a correctness reward and the Brier score of the"
[^c8]: arxiv-2512-19920 — "over this distribution yields a cross-entropy style reward function"
[^c9]: arxiv-2512-19920 — "This formulation imposes stronger penalties for overconfidence on wrong answers"
[^c10]: arxiv-2512-19920 — "because we discover improved training stability specifically for this reward design."
[^c11]: arxiv-2512-19920 — "refusal rate and hallucination rate proved insensitive to the specific prompt input t during inference."
[^c12]: arxiv-2512-19920 — "optimization landscape where the model struggles to learn a coherent strategy for adaptive conditions from"
[^c13]: arxiv-2512-19920 — "for ϵ < t < 1 − ϵ."
[^c14]: arxiv-2512-19920 — "We apply behavioral calibration to finetune Qwen-3-4B-Instruct-2507"
[^c15]: arxiv-2512-19920 — "Utilizing the Qwen3-4B-Instruct model"
[^c16]: arxiv-2512-19920 — "which is determined by an LLM Judge"
