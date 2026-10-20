---
description: "In multiple-choice RLVR, the empirical attractiveness of wrong options, not their number, decides whether the reward trains reasoning or guessing; training-test option counts must also match."
aliases: ["distractor strength", "Iterative Distractor Curation", "empirical distractor strength"]
sources: ["arxiv-2603-12826", "arxiv-2511-18305"]
---
# Distractor strength as reward-signal quality

A multiple-choice question used as a verifiable reward can be solved without reasoning: by chance (limited answer space) or by eliminating obviously wrong options.[^c1] The work measures which property of the option set controls this, holding the stem fixed.

## Mechanism

**Strength is measured, not judged.** A distractor's empirical strength is the share of a reference model's wrong answers that land on it, estimated by sampling trajectories; a high value marks a strong trap for the model.[^c2] Strong distractors compete with the ground truth and give high-contrast feedback; weak ones are trivial to reject even with flawed reasoning.[^c3]

**Strength matters more than count.** The authors report that the effect of the number of options is overestimated: guess rate falls from 25% (4-way) to 10% (10-way), yet the effect on RLVR training is limited. Even 2-way questions, with a 50% chance of a correct guess, train effectively if the distractors are high quality.[^c4] In the 2-choice ablation (MMLU-Pro), they compare a random, the strongest and the weakest distractor, and find substantial performance differences by strength (Finding 1).[^c5]

**Count must match between training and test.** Performance peaks when the training and test option counts agree, declines as the mismatch grows, and falls more steeply when training has fewer options than test.[^c6] The authors read this as the model learning patterns tied to the option-count distribution.[^c7]

**Curation loop (IDC).** Keeping the stem and correct answer fixed, a filling phase adds generated distractors with non-zero strength until the pool is full; a replacement phase swaps out the weakest distractor only if a new candidate is stronger.[^c8] The model itself can generate these options. On medical sets, average accuracy rose from 39.39 to 42.62 (Qwen2-7B) and 48.63 to 51.90 (Llama-3.1-8B), against the original MCQs and against converting to open-ended form (Table 3 shows these conversions at roughly 40.4–40.9 and 49.5–50.9).[^c9] A known failure of generated distractors is semantic collapse, where one becomes equivalent to the gold answer (4.44% of 5,000 questions); an equivalence check replaces them.[^c10]

A second paper builds the option set from the same kind of statistic, with no curation loop. It samples K rollouts from the base model, and the options are formed "by selecting the k most frequent categories," with the ground truth forced in.[^c11][^c12] Frequency among a model's own samples is close to the share-of-wrong-answers estimate used above, though that paper does not define strength, so the match is my reading. Its CUB ablation varies only how the options are sampled: options from the base model's own top-k "achieved a substantial classification accuracy gain of 12% on base classes and 6.9% on novel classes compared to base model," and "our proposed top-k as options proves significantly more effective" than options from a text-embedding model.[^c13][^c14] That is a vision-classification setting, outside the medical sets above.

## Why it bears on asking

The result relocates quality from the question stem to the offered answer set: converting MCQs to open form discards the contrast that expert distractors carry, and a closed set is only as informative as its strongest wrong option. The mapping to answerers other than RL policies is my inference, not tested here.

## Limits

- Strength is relative to a reference policy; options strong for one model may be weak for another, and the loop is tied to the current policy (the authors note self-generated options likely depend on it).
- Experiments are mostly on medical MCQs with two 7–8B models; one PubMedQA result does not favor IDC (77.6 vs 78.8 for Rewrite on Llama), and gains are about 3 points.
- Option-count mismatch is shown for RLVR training; whether it transfers to humans or other answerers is not tested.
- The explanation (learned dependence on option-count distribution) is the authors' interpretation.

## Related

- [[item-writing-guidelines]] — human-test rules also demand plausible distractors; here plausibility is measured by model choice frequency.
- [[question-as-partition]] — the option set as the partition the answerer selects among.
- [[question-evaluation-method]] — a finished-question appraisal; strength is one such measurable.

[^c1]: arxiv-2603-12826 — "Elimination strategies: models can"
[^c2]: arxiv-2603-12826 — "a higher ŝj indicates that oj acts as"
[^c3]: arxiv-2603-12826 — "whereas weak distractors are"
[^c4]: arxiv-2603-12826 — "Even in 2-way questions (with a 50% chance of"
[^c5]: arxiv-2603-12826 — "Finding 1: Distractor strength is critical for"
[^c6]: arxiv-2603-12826 — "(1) performance"
[^c7]: arxiv-2603-12826 — "model learns patterns tied to the distribution of option counts"
[^c8]: arxiv-2603-12826 — "and replace it with a newly generated candidate"
[^c9]: arxiv-2603-12826 — "from 39.39% to 42.62% (+3.23%) and from"
[^c10]: arxiv-2603-12826 — "(35,000 IDC generation rounds)"
[^c11]: arxiv-2511-18305 — "by selecting the k most frequent categories"
[^c12]: arxiv-2511-18305 — "To ensure that the correct answer is always an option during"
[^c13]: arxiv-2511-18305 — "achieved a substantial classification accuracy gain of 12% on base classes and 6.9% on novel classes compared to base model"
[^c14]: arxiv-2511-18305 — "our proposed top-k as options proves significantly more effective"
