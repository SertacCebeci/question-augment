---
description: "A margin between the correct option and the strongest distractor under a reference model finds decision-ambiguous items, including correct ones that misclassification-based mining misses."
aliases: ["DAS", "decision-ambiguous samples", "decision-ambiguity mining", "probability-margin sample selection"]
sources: ["arxiv-2512-24591"]
---
# Decision-ambiguous sample mining

Training items can be ranked by how close a model's top two answer options are, not only by whether its answer is right. Take a reference model (in the paper, the supervised fine-tuned model), read off its probability for the correct option and for the strongest wrong option, and take the absolute gap between them. The paper calls that gap the ambiguity score, written Δ(x). Items whose gap falls below a threshold τ are "decision-ambiguous samples" (DAS): the model may well be right on them, but it sits close to a decision boundary.[^c1] The paper sets τ = 0.2 by default.[^c2]

The selector is defined against hard-example mining, which the authors describe as relying "on misclassification as the criterion." That criterion misses items that are predicted correctly while still ambiguous.[^c3] The authors state that DAS are "neither equivalent to misclassified samples nor" caused by annotation noise, and that they reflect an intrinsic ambiguity in the task.[^c4] The supporting observation is a histogram of the reference model's margins on its own predictions. The paper reports that a large portion of prediction errors fall in the small-margin region, which it reads as a strong association between errors and elevated ambiguity.[^c5]

Once mined, the DAS subset becomes the training set of a group-relative policy optimization stage. For each ambiguous input the policy samples several answers, each is scored 1 if it matches the label and 0 otherwise, and the rewards are standardized within the group. The stated effect is that this "highlights informative gradients when" correct answers appear among strong distractors.[^c6] The reward needs no labels beyond the existing answer key, and "DARFT requires neither additional human annotations nor" an external reward model.[^c7] The reference model plays two roles: it scores the ambiguity, and it serves as the anchor for a KL penalty during the RL stage, "acting as a reference policy for KL".[^c8]

So the mechanism has two parts. A pre-rollout selector uses the margin under a fixed reference to decide which items are worth rolling out. Within each group, the standard group-relative advantage then compares candidate answers that the margin has already identified as competitive. The second part is ordinary group-relative optimization. What is specific here is the first part.

On QAG-360K with Qwen2.5-VL-3B, trained on 0.5K and 2K few-shot subsets, the paper reports gains over SFT under greedy decoding. The largest gain is on Change Ratio: "Change Ratio shows the most substantial improvement."[^c9] Under 20 samples per item, it also reports higher mean accuracy and majority-vote accuracy, and it reads the majority-vote gain as "more consistent predictions", which it takes to show decision stability.[^c10]

## Limits

- One backbone (Qwen2.5-VL-3B) and one benchmark (QAG-360K), at two few-shot sizes. "We evaluate DARFT on QAG-360K"[^c11], and the backbone is "the Qwen2.5-VL-3B model"[^c14]. The text I read has no run on another model, another dataset, or a task without a fixed option set.
- The margin depends on the reference model and on how its probabilities are read out. Here the option probability is the probability of one letter token, over a list where "we retain the complete option space" of 23 candidates.[^c15] A different reference, prompt, or option format changes Δ and so changes the DAS set. The text does not vary any of these (my inference: the selection is only as stable as the reference).
- The reference is fit on the training set and then "scores each" training sample.[^c16] So Δ on training items measures a model that has already seen them. Whether the same items remain ambiguous for a held-out reference is not reported (my inference).
- The threshold is a default: "Unless otherwise specified, we set" τ = 0.2.[^c2] The text I read contains no sweep over τ, so the size of the DAS subset, and how much it matters, is not characterized.
- Association is not shown to be causal. Errors clustering at small margins does not show that training on those items produces the gain. The text I read has no control against an equal-sized random subset or against a misclassification-selected subset (my reading).
- The paper calls the drops "minor drops on a small number of categories in certain regimes."[^c12] Table I's 2K row for Change to What reads "46.45 (-6.69)"[^c13], which is a larger drop than "minor" suggests.
- For open-ended answers there is no fixed set of competing options, so the margin as defined does not apply directly (my inference).

## Related

- [[zero-variance-group-waste]] — another pre-rollout selector for group-relative RL. It ranks prompts by predicted within-group reward variance, not by a reference margin; this paper does not compare the two.
- [[self-consistency-difficulty-score]] — also keeps items near the capability boundary, but from agreement across the solver's own sampled answers rather than one reference model's margin.
- [[vote-margin-gate]] — the same margin between two leading options, used at inference to decide when to answer, not in training to choose which items to learn from.

[^c1]: arxiv-2512-24591 — "we regard the sample as a decision-ambiguous sample (DAS),"
[^c2]: arxiv-2512-24591 — "Unless otherwise specified, we set"
[^c3]: arxiv-2512-24591 — "mining usually relies on misclassification as the criterion, and"
[^c4]: arxiv-2512-24591 — "DAS are neither equivalent to misclassified samples nor"
[^c5]: arxiv-2512-24591 — "portion of prediction errors concentrate in regions with small"
[^c6]: arxiv-2512-24591 — "highlights informative gradients when"
[^c7]: arxiv-2512-24591 — "DARFT requires neither additional human annotations nor"
[^c8]: arxiv-2512-24591 — "acting as a reference policy for KL"
[^c9]: arxiv-2512-24591 — "Change Ratio shows the most substantial improvement"
[^c10]: arxiv-2512-24591 — "This demonstrates that DARFT leads to more consistent predictions"
[^c11]: arxiv-2512-24591 — "We evaluate DARFT on QAG-360K"
[^c12]: arxiv-2512-24591 — "minor drops on a small number of categories in certain regimes"
[^c13]: arxiv-2512-24591 — "46.45 (-6.69)"
[^c14]: arxiv-2512-24591 — "We implement our DARFT framework based on the Qwen2.5-VL-3B model"
[^c15]: arxiv-2512-24591 — "we retain the complete option space"
[^c16]: arxiv-2512-24591 — "training sample using the reference policy"
