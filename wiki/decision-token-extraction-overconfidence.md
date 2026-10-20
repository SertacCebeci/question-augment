---
description: "In reasoning LLMs the final decision token only extracts the trace's conclusion, so its probability is near 1 even when wrong; RLVR finds no calibrated rollouts, and a decision-token loss fixes it."
aliases: ["decision token as extraction step", "calibration-aware GRPO decision-token loss", "RLVR overconfidence from extraction"]
sources: ["arxiv-2601-13284"]
---
# Decision-Token Extraction Overconfidence

When a reasoning model ends with a single decision token and its confidence is read as that token's probability, the number measures how firmly the reasoning trace points at a label, not how likely the label is to be true.

## Mechanism

Confidence is defined as the probability of the final decision token given the trace.[^c1] The authors hypothesize that "the decision token functions more as an extraction step than as an evaluation."[^c2]

Two probes support this on Qwen3-1.7B/4B/8B, with CommonsenseQA and OpenAI Moderation:

- Sampling 64 generations per query from the base model, 94.62% to 99.85% have decision-token probability above 0.99, whether or not the decision is correct.[^c3] The model therefore offers no spread of confidence levels for reinforcement learning to upweight. In the authors' words: "there are no "calibrated" rollouts which could be sampled from the model for RL to upweight."[^c4]
- In a reasoning-swap test, the model's reasoning is replaced with reasoning for the opposite label. The decision flips in 92% to 100% of cases, and "the decision token is still assigned probability extremely close to 1."[^c5]

Hence RLVR (reinforcement learning with verifiable rewards, here GRPO) raises accuracy while leaving confidence saturated. SFT, by contrast, gave lower ECE than GRPO in the tables read (for example CSQA, Qwen3-1.7B: ECE 7.36 for SFT against 24.39 for GRPO).

## The repair

Apply the GRPO loss to all tokens except the decision token, and add a cross-entropy loss on the decision token alone. Its target is one-hot if the generation is correct and uniform over the candidate labels if it is wrong, so L = L_GRPO + λ L_CE.[^c6] The decision-token probability is kept within [1/|C|, 1] so that the greedy label does not flip, which would make the reasoning and the decision disagree and make the reward inconsistent.[^c7] The authors report that the method preserves RLVR's accuracy and reduces ECE by up to 9 points.[^c8] The reading is that calibration has to be intervened on at the decision-token level, not through trajectory-level reward.

## Limits

- Only short-answer classification with a single decision token was tested: multiple choice and binary safe/unsafe. Open-ended generation and verbalized confidence are out of scope.
- Three Qwen3 sizes were used, with 500 training examples per task. Other model families were not tested.
- The extraction-step account rests on correlational probes (saturation and swap flips), not on an intervention on model internals. The causal reading is the authors' hypothesis.
- The method does not always reach SFT's calibration; the authors say it does not always match it.
- A uniform target for wrong answers is a design choice. No comparison with other targets was read by me.
- The method needs ground-truth correctness at training time.

## Related

- [[calibration]] — the general notion this measures with ECE.
- [[rlvr-answering-bias]] — another side effect of verifiable-reward training.
- [[reward-only-advantage-miscalibration]] — a different diagnosis: the advantage depends on reward only.
- [[calibration-aware-policy-optimization]] — CAPO fixes the advantage; here the loss is on the decision token.
- [[calibration-training]] — the family of training-time remedies.

[^c1]: arxiv-2601-13284 — "Throughout this paper, we define the model’s confidence as the probability assigned to the decision token."
[^c2]: arxiv-2601-13284 — "We hypothesize that the decision token functions more as an extraction step than as an evaluation."
[^c3]: arxiv-2601-13284 — "almost all sampled trajectories have decision tokens whose probabilities are extremely close to 1, regardless of whether the decision is correct."
[^c4]: arxiv-2601-13284 — "there are no “calibrated” rollouts which could be sampled from the model for RL to upweight."
[^c5]: arxiv-2601-13284 — "the decision token is still assigned probability extremely close to 1"
[^c6]: arxiv-2601-13284 — "LCE is a cross-entropy loss on the decision token with either a one-hot target (if correct) or a uniform target (if incorrect)"
[^c7]: arxiv-2601-13284 — "we constrain the probability of the decision token to remain within the range [1/|C|, 1]"
[^c8]: arxiv-2601-13284 — "Our method preserves RLVR’s accuracy level while mitigating overconfidence, reducing ECE scores up to 9 points."
