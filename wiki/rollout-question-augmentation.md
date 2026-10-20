---
description: "Rewording a question and noising its image before each rollout group gives the policy several prompts per question, aiming to make the group's rewards differ rather than all agree."
aliases: ["GDQA", "Group Diversity Question Augmentation", "rollout-time prompt augmentation", "query rewriting for group diversity"]
sources: ["arxiv-2512-19512"]
---
# Rollout-time question augmentation

In group-relative RL the group of responses sampled for one prompt is the unit of learning. If the policy answers that prompt the same way every time, the group holds no contrast to learn from. Anatomy-R1 answers this on the question side. Each prompt is rewritten into "semantically equivalent, targeted variants", and each variant then generates its own responses, so a group draws on several wordings of the question instead of one canonical query.[^c1] The authors call this Group Diversity Question Augmentation (GDQA).

## Mechanism

GDQA has two operators. A textual operator rewrites the prompt into several syntactically diverse questions, and the rewrites "retain the original intent and answer, but shift the focus or phrasing".[^c2] A visual operator "applies controlled modifications to" the image, for example noise injection, "while preserving critical visual cues necessary for reasoning".[^c3] Each textual variant may be paired with a transformed image, so the group is built from multimodal prompt variants.

The stated purpose is to change the reward distribution inside the group. For each expanded prompt the policy generates a response, and the method "intentionally increases the variance within the response group", which the authors expect to give "a broader and more informative reward distribution".[^c4] The reasoning runs through the zero-advantage problem described in [[zero-variance-group-waste]]: a group in which every answer agrees carries no [[group-relative-advantage]] signal, so spreading the prompts is meant to break that agreement. The paper hedges the link itself: the augmentation "could help to mitigate the vanishing gradient phenomenon".[^c5]

## What was measured

On SGG-VQA, the ablation in Table 2 removes each operator in turn. The full method reaches Avg@5 47.32%; without the text rewrite Avg@5 falls to 46.21%, and without image augmentation to 45.34%.[^c6] The authors summarise the pattern: "text or image augmentation leads to a clear decline across" all metrics.[^c7] The mechanism claim is supported by invalid-gradient curves for four anatomies: on a hard anatomy the plain policy is wrong in every response of a group, leaving no signal,[^c10] and GRPO-GDQA "consistently maintains a notably lower proportion of invalid gradients".[^c8] The authors read the drop as "reducing invalid gradients caused by entirely incorrect groups".[^c9]

## Limits

- Semantic equivalence is asserted, not checked, in the sections read. Nothing reports that a rewrite keeps the answer for each question, and a rewrite that shifts the question's target would add noise, not diversity (my inference).
- The image operator changes the input itself, so the ablation cannot separate two explanations: that the policy explores more reasoning paths, or that noisy images act as extra augmentation for the same answer. A control in which the canonical prompt is resampled as often as the variants is not in the sections read. (my inference)
- The ablation is on one benchmark, SGG-VQA. The invalid-gradient evidence covers four anatomies, not the whole training distribution.
- Avg@5 is scored by a clinical expert on a 1–5 scale; the scoring protocol and the number of raters are not in the sections read, so the headline gains cannot be re-scored.
- The paper measures invalid-gradient proportions, not the within-group reward variance it is meant to raise. The link from one to the other is the authors' reading.

## Related

- [[prompt-variant-augmentation]] — the training-time counterpart: rewordings are used as data so that a model is robust to wording. Here the rewordings are used at rollout time to shape the reward spread within one group; the two mechanisms are different and neither tests the other.
- [[zero-variance-group-waste]] — the selection-side remedy for the same zero-advantage groups: pick prompts whose rollouts are likely to disagree, instead of varying the prompt.
- [[permutation-consistency-training]] — the other within-group device in this area, where a reward over reorderings enforces invariance; GDQA instead widens the set of prompts the group is drawn from.

[^c1]: arxiv-2512-19512 — "transforms each prompt into semantically equivalent, targeted variants"
[^c2]: arxiv-2512-19512 — "These rewrites retain the original intent and answer, but shift the focus or phrasing"
[^c3]: arxiv-2512-19512 — "while preserving critical visual cues necessary for reasoning"
[^c4]: arxiv-2512-19512 — "intentionally increases the variance within the response group"
[^c5]: arxiv-2512-19512 — "This could help to mitigate the vanishing gradient phenomenon"
[^c6]: arxiv-2512-19512 — "Table 2: The ablation study of GDQA on SGG-VQA"
[^c7]: arxiv-2512-19512 — "text or image augmentation leads to a clear decline across"
[^c8]: arxiv-2512-19512 — "consistently maintains a notably"
[^c9]: arxiv-2512-19512 — "thereby reducing invalid gradients caused by entirely incorrect groups"
[^c10]: arxiv-2512-19512 — "For difficult-to-recognize anatomy, the policy consistently fails, incorrectly identifying the structure in all M"
