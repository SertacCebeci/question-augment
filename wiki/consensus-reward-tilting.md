---
description: "Rewarding agreement with the majority answer under a KL penalty yields an optimum that tilts the reference answer distribution toward its mode, sharpening it and raising the vote margin."
aliases: ["TTRL tilt", "test-time reinforcement learning as tilting", "majority-agreement reward tilt", "exponential tilting of the answer law"]
sources: ["doi-10-48550-arxiv-2510-17472"]
---
# Consensus-reward tilting

Test-time reinforcement learning (TTRL) trains a model on its own rollouts with no labels. Its reward is agreement with the majority: a rollout scores 1 when its answer equals the vote and 0 otherwise. The paper's point is what that reward does to the answer distribution. Maximising the expected reward under a KL penalty to the reference policy has a closed-form optimum, and the paper states it as "The optimal policy is an exponentially tilted distribution": the reference law reweighted by exp(reward/β), normalised.[^c1]

Writing κ = 1/β, the paper shows that the tilt sharpens the answer law around the mode, and that stronger tilting helps certification: "consistently improves the margin and reduces the number of samples required for certification."[^c2] The margin in question is the one defined in [[majority-vote-mode-certificate]]. The SNR of the leader-versus-runner-up margin is non-decreasing in κ, with equality only when the vote is a Dirac delta at a single answer. In my reading, the mechanism is simple: a reward that is 1 on the majority answer multiplies that answer's probability by a constant factor relative to every rival, so the gap widens and the vote needs fewer rollouts, which [[anytime-valid-majority-stopping]] turns into fewer draws.

The paper also introduces two group-level rewards that target this trade-off directly: one based on the margin SNR, and one on negative entropy of the answer distribution. The entropy version is stated to act on answers only: it "sharpens only the distribution of final answers, not the full sequence distribution," so reasoning paths stay diverse. Both are optimised with GRPO: "We post-train our models using the GRPO algorithm." The paper's reason for preferring them to the TTRL reward is that "these yield smoother signals of consensus."[^c3]

The paper compares these objectives with TTRL across Qwen2.5 and Llama-3.1-8B models on AIME 2024, AMC and MATH-500: "We compare the performance of our proposed RL objectives with TTRL." I did not carry the accuracy tables into this note; the claims here are the mechanism and the stated optima.

## Limits

- The tilt is the optimum of an idealised KL-regularised problem over trajectory laws. The experiments optimise a sampled GRPO surrogate, and the gap between that surrogate and the optimum is not analysed in the parts of the text read.
- Sharpening is a bias, not a free gain. The paper says the objective "introduces a controlled bias relative to the original" distribution, "governed by the KL regularisation strength."[^c4] The reward does not check whether the majority is right. My inference: if the reference law's mode is wrong, tilting toward it makes the wrong answer more certain, and the vote certificate will certify it.
- The SNR and entropy quantities are only as good as the model's internal probabilities: "our SNR- and entropy-based quantities rely on the model" for calibration, and the paper flags this as a limitation.[^c5]
- The evaluation is limited to "single-turn reasoning benchmarks".[^c6] Multi-turn dialogue, program synthesis and structured prediction are not tested.
- The entropy reward tempers only the final-answer marginal; the TTRL objective as written acts on whole trajectories. Whether these behave the same on free-text answers, where the answer marginal must first be grouped, is not tested.

## Related

- [[majority-vote-mode-certificate]] — the margin this tilt is meant to enlarge, and the bound that shows why a larger margin lowers the error.
- [[anytime-valid-majority-stopping]] — the stopping rule that turns a larger margin into fewer rollouts.
- [[dpo-implicit-reward]] — the same reference-times-exp(reward/β) form, with a preference reward in place of agreement with the majority.
- [[group-relative-advantage]] — the GRPO-style group update the paper uses to reach these objectives.
- [[retrieval-dissimilarity-novelty-reward]] — another TTRL-derived reward; there the majority pseudo-label is replaced by a retrieved distance.

[^c1]: doi-10-48550-arxiv-2510-17472 — "The optimal policy is an exponentially tilted distribution"
[^c2]: doi-10-48550-arxiv-2510-17472 — "consistently improves the margin and reduces the number of samples required for certification"
[^c3]: doi-10-48550-arxiv-2510-17472 — "these yield smoother signals of consensus"
[^c4]: doi-10-48550-arxiv-2510-17472 — "introduces a controlled bias relative to the original"
[^c5]: doi-10-48550-arxiv-2510-17472 — "our SNR- and entropy-based quantities rely on the model"
[^c6]: doi-10-48550-arxiv-2510-17472 — "Empirically, our evaluation focuses on single-turn reasoning benchmarks"
