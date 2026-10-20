---
description: "A model can read a joint distribution over its own final reward and remaining length from unused output logits at every token, adding no forward pass."
aliases: ["ZIP-RC", "zero-overhead introspection", "introspective reward-cost prediction", "reserved-logit reward-length head"]
sources: ["arxiv-2512-01457"]
---
# Joint reward-cost prediction

At every token a language model generates, a small block of its output logits can be given a second job. The block is reserved, or simply unused, since most of the vocabulary is never the right next token. Its logits are read as the parameters of a softmax over a grid: one axis bins the final reward of the completion the current prefix will become, the other bins how many tokens remain.[^j1] Before sampling, these logits are masked out of the decoding distribution, so the next token is chosen as before.[^j16] The grid comes out of the same forward pass that produces the next-token probabilities, with "no extra models, architecture change, or inference overhead".[^j15]

Training supervises that block alone. For each prefix of a finished rollout, the target is the grid cell that the rollout's reward and remaining length fall into, and the auxiliary term is cross-entropy on that cell.[^j2] The reward is not ground truth in the formulation. The expected terminal reward is approximated by a realized score "from a learned verifier".[^j14] In the experiments, each rollout is labelled for correctness against the ground-truth answer, over "roughly 100k rollouts in total".[^j3][^j13]

**Why a joint, not a scalar.** A probability of correctness on a prefix says how likely success is. It does not say what success will cost. The authors' point is that the two trade off: "a low-confidence trajectory may be worthwhile if nearly finished".[^j4] The joint also gives the marginal value of another sample. The earlier early-stopping and pruning methods "do not quantify the marginal benefit of drawing more samples".[^j5] When the predicted reward has high variance, "samples can substantially increase the expected maximum reward".[^j6] From the joint, the expected maximum reward of a set of samples, their expected total compute and their expected latency can be estimated. A linear combination of these is a sampling utility. The utility is maximized over meta-actions, such as which prefixes to continue and when to start new samples.[^j7]

The reported effect is on mixed-difficulty math benchmarks, with three small models: the utility-driven sampler improved accuracy "by up to 12% over majority voting at equal or lower average cost".[^j8] The mechanism is that the predicted distribution, not its mean, drives the decision: a high-variance prefix is worth branching from, and a near-deterministic one is worth stopping early (my inference from the utility's form).

## Limits

- The calibration check is narrow. At the start of generation no ground-truth label exists, so the predicted joint was compared by total variation against an estimate "derived with 256 rollouts from Qwen3-1.7B", on AMC 2023 and AIME 2024.[^j9] The summary that "the predictions are calibrated and relatively accurate" rests on a visual check of "the 10 random examples" per benchmark, not on a metric across all problems.[^j10][^j17]
- Only math was tested, with three models of 350M to 1.7B parameters. Whether a grid of this kind can be learned where the reward is an open-ended judgement, not a checked answer, is not tested (my inference).
- The gains depend on the samples being different. The authors state the limit: the method "rely[ies] on LLMs achieving sufficient diversity of samples during inference".[^j11] If new samples repeat old ones, no selection rule, this one included, can beat a fixed budget of samples.
- The utility is computed with a simplification: "we use a single shared horizon ht for all active prefixes".[^j12] Per-prefix horizons would change the pruning schedule; the size of that change is not reported.
- Zero overhead is an inference-time claim. Training needs the labelled rollouts and an auxiliary loss on the base model. The paper also mentions a variant that keeps the model frozen, in its appendix (section A.3), which this note does not assess.
- Whether a model's predicted success tracks what a human would call a good answer, rather than a verifier's score, is not established (my inference). For the asker's side of the wiki the readout bears on stopping and commitment, not on the quality of the question.

## Related

- [[prefix-correctness-readout]] — the scalar version: a correctness head on partial generations. This note adds the remaining-length axis and reads it from reserved logits.
- [[test-time-scaling]] — the setting: deciding how many samples to draw, and when to stop drawing them.
- [[verifier-gain]] — the verifier's worth. Here the reward head predicts a verifier's score, so the verifier's quality bounds what the readout can say (my inference).
- [[cost-priced-joint-selection-and-stopping]] — a similar benefit-minus-cost halting rule, applied to which question to ask in retrieval rather than to sampling.
- [[calibration]] — the property the paper checks, by total variation at the start of generation and by threshold accuracy at the end.
- [[logit-magnitude]] — another uncertainty readout from logits in the same forward pass, aggregated over a prefix.

[^j1]: arxiv-2512-01457 — "At each decoding step, unused vocabulary logits parameterize a joint distribution over final reward and remaining generation length"
[^j2]: arxiv-2512-01457 — "Finally, we train with cross-entropy"
[^j3]: arxiv-2512-01457 — "label each rollout for correctness against the ground-truth answer"
[^j4]: arxiv-2512-01457 — "a low-confidence trajectory may be worthwhile if nearly finished"
[^j5]: arxiv-2512-01457 — "do not quantify the marginal benefit of drawing more samples"
[^j6]: arxiv-2512-01457 — "samples can substantially increase the expected maximum reward"
[^j7]: arxiv-2512-01457 — "combination of the expected maximum reward, total compute, and latency of set"
[^j8]: arxiv-2512-01457 — "accuracy by up to 12% over majority voting at equal or lower average cost"
[^j9]: arxiv-2512-01457 — "derived with 256 rollouts from Qwen3-1.7B"
[^j10]: arxiv-2512-01457 — "the predictions are calibrated and relatively accurate"
[^j11]: arxiv-2512-01457 — "rely on LLMs achieving sufficient diversity of samples during inference"
[^j12]: arxiv-2512-01457 — "we use a single shared horizon ht for all active prefixes"
[^j13]: arxiv-2512-01457 — "yielding roughly 100k rollouts in total"
[^j14]: arxiv-2512-01457 — "from a learned verifier"
[^j15]: arxiv-2512-01457 — "no extra models, architecture change, or inference overhead"
[^j16]: arxiv-2512-01457 — "Before sampling, these logits are masked to"
[^j17]: arxiv-2512-01457 — "From the 10 random examples"
