---
description: "The maximum next-token entropy over a solver's first five answer tokens, percentile-ranked in a rolling window, is a difficulty signal that stays informative when answer agreement collapses."
aliases: ["STE"]
sources: ["doi-10-48550-arxiv-2606-27376"]
---
# Solver token entropy

A learner that proposes questions for its own solver needs a difficulty signal that does not depend on labels. The usual choice is answer agreement: sample the solver under several rephrasings of a question and measure how much its answers disagree, as in [[self-consistency-difficulty-score]]. That signal has a blind spot the paper names directly: "Hsc can collapse (all framings yield the same answer) even when the model is uncertain, producing weak curriculum signals."[^c1] Here Hsc is the entropy of the answer votes across framings, so unanimity drives it to zero whatever the solver's internal confidence happens to be.

Solver Token Entropy (STE) reads the same solver one level lower, at the token. At each decoding step the solver's next-token distribution has an [[entropy]]; for an answer the signal is the maximum of these values over its first five tokens, and the paper states that this maximum is its default aggregation.[^c2] The max is meant to catch one decisive uncertain token, such as a count, a colour, a relation or a negation, inside a short answer.[^c3] The raw value is then turned into a difficulty score in [0, 1] by percentile rank within a rolling window of recent values.[^c4] The window keeps the score comparable across training as the solver's confidence distribution moves.[^c5]

STE is never used alone. The Proposer's reward is a weighted sum of the STE difficulty and an agreement term centred on a running target, and STE is added "to prevent reward degeneracy when Hsc ≈ 0".[^c6] The Solver is rewarded for agreement with its modal answer, so STE enters only the Proposer's reward.[^c7] The paper is explicit that STE is a scalar read off the solver, not a token-matching objective.[^c8]

The evidence offered is a diagnostic figure and one ablation. The figure splits questions by answer behaviour and reports that sample-level entropy stays near zero when the solver is consistently correct and when it is consistently wrong: "Sample-level self-consistency entropy remains close to zero" in both cases, "but also when it is consistently wrong", while STE "separates these two cases more clearly".[^c9][^c10][^c11] The paper reads the two signals as complementary: "self-consistency captures framing-level robustness while STE detects token-level uncertainty".[^c12] In the ablation, "Removing STE reduces MMMU by −1.8 and MMBench by −1.6".[^c13]

## Limits

- The setting is short answers. The paper reports that "the normalized Solver answers are short" in its BLIP3o rollouts.[^c14] A five-token window therefore covers nearly the whole answer there. For long free-form answers the maximum sees only a prefix; that consequence is my inference, not something the paper tested.
- The paper's main runs all use the max. A mean aggregation exists as a control: "all reported main runs use max aggregation".[^c15] The effect of the alternative is not part of the evidence offered.
- Token entropy measures uncertainty, not correctness. A solver that is confidently wrong has low entropy at each token, so STE should not be expected to flag it. This is my inference; the figure says STE separates the groups "more clearly", not that it separates them cleanly. See [[confidently-wrong-low-entropy-regime]].
- The signal needs the solver's output distributions. A black-box model that returns only sampled answers cannot supply it. This is my inference and is untested in the paper.
- Percentile ranking discards the absolute level. STE says how uncertain a question is relative to the recent window, so the same raw entropy can score differently at different training stages. Also my inference.
- The evidence is one paper on LoRA post-training of frozen backbones. The method "better aligns existing latent capabilities of a frozen unified model",[^c17] and the paper disclaims that a frozen backbone "can learn unlimited new visual primitives from arbitrarily large unlabeled pools".[^c16] STE is therefore a tuning signal for what the model can already do, not evidence of new capability.

## Related

- [[self-consistency-difficulty-score]] — the sample-level agreement score that STE backs up when it collapses
- [[entropy]] — the Shannon entropy applied here per token
- [[thinking-chain-entropy]] — entropy over a whole reasoning chain rather than the first answer tokens
- [[logit-magnitude]] — another token-level uncertainty read, from logit norms rather than the full distribution
- [[uncertainty-peaked-challenge-reward]] — a label-free questioner reward on majority agreement, the difficulty target STE also feeds
- [[question-answer-fidelity-reward]] — the same solver's answers, used on the generation side to score images

[^c1]: doi-10-48550-arxiv-2606-27376 — "Hsc can collapse (all framings yield the same answer) even when the model is uncertain, producing weak curriculum signals."
[^c2]: doi-10-48550-arxiv-2606-27376 — "The default Solver Token Entropy signal is the maximum full-softmax"
[^c3]: doi-10-48550-arxiv-2606-27376 — "The max operator targets decisive uncertain content tokens in short answers"
[^c4]: doi-10-48550-arxiv-2606-27376 — "by taking its percentile rank within a rolling window"
[^c5]: doi-10-48550-arxiv-2606-27376 — "the rolling-window normalization makes STE comparable across training"
[^c6]: doi-10-48550-arxiv-2606-27376 — "we add STE difficulty"
[^c7]: doi-10-48550-arxiv-2606-27376 — "The Solver is trained to answer consistently across framings by rewarding agreement with the modal answer"
[^c8]: doi-10-48550-arxiv-2606-27376 — "STE is a scalar uncertainty score from the Solver"
[^c9]: doi-10-48550-arxiv-2606-27376 — "Sample-level self-consistency entropy remains close to zero"
[^c10]: doi-10-48550-arxiv-2606-27376 — "but also when it is consistently wrong"
[^c11]: doi-10-48550-arxiv-2606-27376 — "STE separates these two cases more clearly"
[^c12]: doi-10-48550-arxiv-2606-27376 — "self-consistency captures framing-level robustness while STE detects token-level uncertainty"
[^c13]: doi-10-48550-arxiv-2606-27376 — "Removing STE reduces MMMU by −1.8 and MMBench by −1.6"
[^c14]: doi-10-48550-arxiv-2606-27376 — "the normalized Solver answers are short"
[^c15]: doi-10-48550-arxiv-2606-27376 — "all reported main runs use max aggregation"
[^c16]: doi-10-48550-arxiv-2606-27376 — "backbone can learn unlimited new visual primitives from arbitrarily large unlabeled pools"
[^c17]: doi-10-48550-arxiv-2606-27376 — "post-training that better aligns existing latent capabilities of a frozen unified model"
