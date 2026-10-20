---
description: "Installs the decide-to-ask and which-question choice into weights by SFT then GRPO on synthetic labels built from entropy and information-gain signals alone, no human preference data."
aliases: ["entropy-driven active clarification training", "uncertainty-driven synthetic clarification data"]
sources: ["yang-2026-claim"]
---
# Uncertainty-driven synthetic clarification training

> A second way to install a question-selection criterion into a model's
> weights, next to [[preference-optimization-for-questions]] — the labels
> come from [[cross-model-answer-disagreement-entropy|cross-model entropy]]
> instead of human preference pairs, and the algorithm is SFT+GRPO, not DPO.

## Definition / Mechanism

Yang, Zhao & Dou (2026): "CLAIM eliminates the need for
explicit human preference annotations by quantifying query uncertainty
through the [[entropy]] induced by answer disagreements across multiple
models... enabling the training of a unified clarification decision model
through a combination of supervised learning and reinforcement learning."[^c1]

```text
1. Compute E1(q) (entropy across k1 models' answers) + an independent
   LLM-based semantic-completeness judgement; an arbitration model
   resolves disagreements between the two into one clarify/don't decision
2. When clarification is needed, generate several candidate clarifying
   questions and rank them by IG = E1(q) - E2(q, candidate, simulated answer)
3. SFT: train one model on (query -> decision + best question) sequences
   built entirely from steps 1-2, no human label
4. GRPO: refine the same policy with a deterministic reward scoring
   decision consistency, semantic plausibility and structural validity,
   focused on queries near the entropy threshold
```

A held-out comparison against GRPO isolates its contribution: "CLAIM
improves ClariLM-test accuracy from 79.60 to 81.85 and CDA from 55.17 to
56.79, and also increases CLAMBER accuracy from 61.99 to 65.18."[^c2]
Against a prior supervised+preference-trained open-domain clarifier
(ClariLM), the paper reports matching or exceeding it "using only
approximately 10k uncertainty-constructed training instances, whereas
ClariLM relies on around 120k supervised and preference-annotated
examples."[^c3]

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| LLM training (this paper) | CLAIM | exact — the system's own name for the whole pipeline |
| LLM training (this paper) | entropy-driven active clarification training | exact — descriptive restatement |

## Why it matters

[[preference-optimization-for-questions]] already shows one route: label
pairs by EIG over an enumerable answer space, train with DPO. This is a
second, independent route to the same role — installing a
question-selection criterion in the weights rather than at prompt time —
that needs no enumerable candidate set and no human preference judgement,
at the cost of needing $k_1$ models to sample from during data
construction. The two results are not compared to each other in either
paper; they are evidence for the same shape from disjoint evidence bases
(closed 8-option guessing game vs. open-domain free-text clarification).

## Transfer

| | |
|---|---|
| **In its home field** | reinforcement learning (GRPO, Shao et al. 2024) used for LLM reasoning policies |
| **Here** | GRPO refines a clarification-decision-plus-question policy, on top of an SFT initialization from entirely synthetic, entropy/IG-derived labels |
| **What survives** | the group-relative advantage and clipped-ratio update, applied unchanged to the clarification action space |
| **What does not** | any task-specific reward shaping guarantee — the reward here is a bespoke deterministic function (decision consistency, semantic plausibility, structural validity) whose own [[calibration]] is not evaluated against a ground-truth clarification label |

## Limits

- One paper, one base model (Meta-Llama-3.1-8B-Instruct), one entropy
  threshold ($\tau = 0.45$) tuned globally rather than per dataset.
- The GRPO reward function is deterministic and self-referential — it
  scores agreement with the synthetic-label pipeline's own output, so GRPO
  can at most sharpen decisions already implicit in that pipeline, not
  correct a systematic bias in it.
- No comparison to DPO-on-EIG-pairs ([[preference-optimization-for-questions]])
  on the same benchmark; the "no human labels, no enumerable answer space"
  advantage is argued, not measured against that alternative.
- 2026-08 arXiv preprint, not peer reviewed at the time of reading.

## Related

[[cross-model-answer-disagreement-entropy]] · [[preference-optimization-for-questions]] · [[expected-information-gain]] · [[clarification-benchmarks]]

[^c1]: yang-2026-claim
[^c2]: yang-2026-claim — "CLAIM improves ClariLM-test accuracy from 79.60 to 81.85 and CDA from 55.17 to 56.79, and also increases CLAMBER accuracy from 61.99 to 65.18."
[^c3]: yang-2026-claim — "this performance is achieved using only approximately 10k uncertainty-constructed training instances, whereas ClariLM relies on around 120k supervised and preference-annotated examples"
