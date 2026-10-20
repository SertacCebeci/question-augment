---
description: "Reward-model biases split by whether one linear direction carries them: length, uncertainty and position are removable by null-space projection; sycophancy and model-style sensitivity are not."
aliases: ["mechanistic reward shaping", "probe nulling", "low- versus high-complexity reward model biases"]
sources: ["doi-10-48550-arxiv-2603-03291"]
---
# Reward-model bias linear tractability

A reward model (RM) scores an answer with a scalar, so it is a judge whose verdict can leak surface features. Fein et al. measured five RMs (one DeBERTa-based, four newer 8B-class and smaller) and found the old biases persist (length, sycophancy, overconfidence) and two new ones appear: position and model-style sensitivity.[^c1]

**The split.** Biases whose dominant signal is roughly one direction in the RM's activations are called low-complexity: length, uncertainty, position. Those that resist a single-direction fix are high-complexity: sycophancy and model-style sensitivity.[^c2] The fix is a difference-of-means probe on final-layer activations, then projection onto its null space (a strength alpha scales it). It needs little labeled data and no policy retraining.[^c3]

**Independent check.** Iterative Nullspace Projection trains a linear classifier, removes its direction, and retrains. For low-complexity biases, separability falls to near chance after one direction (for example AllenAI-Llama-8B length 0.996 to 0.509; Skywork-Qwen-8B position 0.935 to 0.524). Style is only partly separable (AUC 0.659 to 0.850) and sycophancy barely separable (0.491 to 0.771), and removing a direction does not consistently help.[^c4]

**What the persisting biases look like.**
- Sycophancy was tested only on questions the RM answers correctly without a hint. All five RMs still agreed with a wrong user suggestion more than 24% of the time, DeBERTa 63% and AllenAI-Llama-8B 58%.[^c5] A linear intervention could not cut faulty agreement without cutting helpful agreement, so user agreement is entangled with useful signal.[^c6]
- Position bias is statistically significant in every RM, with deviations of 2 to 28% across answer positions, in multiple-choice and free-form formats.[^c7]
- Style sensitivity is measured as a Spearman correlation between reward and a panel-relative per-byte cross-entropy of the answer under other language models.[^c8]

**Cost of the fix.** Mean RewardBench2 accuracy went from 70.1% to 69.3% (length, position, combined), non-inferior at a 5-point margin.[^c9] Under best-of-N on held-out prompts, the within-prompt reward-length correlation fell from 0.10 to 0.04 on AlpacaEval, and GSM8K best-of-N accuracy rose from 62.1% to 62.8%.[^c10] Global length calibration can remove pooled correlation yet miss the prompt-conditioned dependence that drives best-of-N selection.[^c11]

## Limits

- The taxonomy is empirical, and its evidence is the success or failure of linear removal. "High-complexity" means linear methods failed here, not that no method works.
- Probes were fit on narrow labeled sets; the smallest model (Skywork-Qwen-0.6B length, 1.000 to 0.770) kept residual structure, suggesting multi-direction encoding.[^c4]
- Sycophancy was reduced to user agreement with a multiple-choice answer; broader social sycophancy was not tested.
- Reward models are scalar scorers, not generative judges; whether the same split holds for LLM judges is my inference, not tested.
- Non-inferiority was shown at a 5-point margin, so small accuracy losses are not excluded.

## Related

- [[llm-judge-biases]] — the generative-judge counterpart: position and verbosity effects in pairwise grading
- [[mcq-answer-position-bias]] — the same order effect when a model answers rather than scores
- [[masking-vs-mitigating-bias-reduction]] — a projection that lowers a measured bias may mask rather than remove it (my inference)
- [[reward-fairness]] — reward design where unwanted features leak into the signal

[^c1]: doi-10-48550-arxiv-2603-03291 — "we find that issues persist despite prior work with"
[^c2]: doi-10-48550-arxiv-2603-03291 — "simple linear intervention and require more fundamental solutions (sycophancy, model-style sensitivity)."
[^c3]: doi-10-48550-arxiv-2603-03291 — "reduces targeted biases without degrading reward quality and"
[^c4]: doi-10-48550-arxiv-2603-03291 — "consistent with redundant or multi-pathway encoding rather than a single"
[^c5]: doi-10-48550-arxiv-2603-03291 — "all models show agreement rates exceeding 24%, with DeBERTa and AllenAI-Llama-8B reaching 63% and 58% respectively."
[^c6]: doi-10-48550-arxiv-2603-03291 — "suggesting this bias"
[^c7]: doi-10-48550-arxiv-2603-03291 — "with deviations"
[^c8]: doi-10-48550-arxiv-2603-03291 — "Statistically significant non-zero"
[^c9]: doi-10-48550-arxiv-2603-03291 — "All interventions demonstrate statistical non-inferiority to baseline at a"
[^c10]: doi-10-48550-arxiv-2603-03291 — "improves mean bestof-N accuracy from 62.1% to 62.8%"
[^c11]: doi-10-48550-arxiv-2603-03291 — "global length calibration can remove pooled reward–length correlation while still failing to address, or even"
