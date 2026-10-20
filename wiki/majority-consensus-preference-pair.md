---
description: "With no gold label, a closed answer gives a training pair by taking the majority of many samples as preferred and a random different answer as dispreferred."
aliases: ["majority-vote preference pair", "consensus-labelled preference pair", "self-consistency preference labels", "majority-filtered synthetic pairs"]
sources: ["arxiv-2512-05145"]
---
# Majority-consensus preference pair

For a question with a closed answer (a choice, a number, a short phrase), a preference pair can be built with no label at all. Sample the same model many times on one input, take the answer most samples agree on as the preferred one, and pair it with a different answer drawn at random as the dispreferred one.[^m1] The construction treats the model's own consistency as the supervision. "we generate N responses from the base model" and the response chosen by the majority is the preferred side; the rest of the pair is a sampled alternative.[^m2]

The consensus has to be strong before it is used. The authors keep only "examples where at least 5 responses are identical, filtering out cases with greater diversity."[^m3] In the reasoning and VQA experiments the sample count is 16: "we sample 16 times, and pick" the majority as the preferred answer.[^m4]

The reason for not simply planting a wrong answer is stated in the text. Changing the answer directly "as the resulting pairs can be trivially easy when the wrong answer is obviously incorrect."[^m5] A dispreferred answer that the model itself produced is harder to reject than a planted one, so the pair carries more of the discrimination the judge must learn. This reading is mine; the paper states the problem with planted answers, not the advantage of sampled ones.

The construction is the closed-ended branch of a judge-training pipeline. Its open-ended branch edits a response instead, as [[controlled-error-injection]] describes. The two branches differ in where the known direction comes from: a vote for closed answers, an edit for open-ended ones.

## What it did against gold labels

The paper compares the majority construction with filtering the same pairs by the dataset's correct answers. On the closed-ended dimensions, "using majority voting to filter the synthetic pairs yields better performance after a few iterations."[^m6] The reported size of the gap is "synthetic pairs constructed via majority voting yield 8.6% and 9.5% average improvement over correctness-filtered" pairs, on VLRB-Reasoning and MMRB-VQA.[^m7]

The authors offer a volume account: "the judge model consistently samples a greater number of data points per iteration when using majority."[^m8] The account is only partial. When the majority set is cut to the size of the correct set, its advantage falls, but "reduces the performance of the original majority set" and a gap remains, which the authors attribute to reasoning quality rather than to size.[^m9] Gold filtering is described as the point of comparison, and the paper says that majority voting "filters samples more efficiently and achieves even greater performance gains."[^m11]

## Limits

- The preferred label is a consensus, not a fact. The authors state that "the majority answer may not be correct, especially in areas when the model struggles."[^m10] A model that is consistently wrong gets a consistently wrong label, and the pair cannot show that error. The construction teaches the judge the model's own agreement.
- The threshold of at least 5 identical out of 16 is a single setting. The text I read does not vary it, so how the margin rule trades pair count against label error is not measured here. The bound in [[majority-vote-mode-certificate]] is the nearest formal account of how a margin reduces the error of a sampled mode; the paper does not use it.
- The comparison covers two dimensions (VLRB-Reasoning and MMRB-VQA) and one base model, Llama-3.2-11B-Vision-Instruct. The text does not test other models or other closed-answer formats.
- The gold-label comparison concerns correctness of the answer, not human preference over responses. A pair built on consensus is a proxy for correctness that is only as good as the model's agreement with itself.

## Related

- [[majority-vote-mode-certificate]] — the error bound for a sampled majority; this construction takes the mode as its preferred label without the bound.
- [[consensus-reward-tilting]] — the same majority pseudo-label, used there as a reward in test-time reinforcement learning rather than as a training pair.
- [[controlled-error-injection]] — the open-ended branch of the same pipeline, where the known direction comes from an edit.
- [[verdict-gated-reasoning-trace]] — what the judge is trained on once a pair is known: its own reasoning, kept only when its verdict matches the pair.

[^m1]: arxiv-2512-05145 — "pair the majority answer with a random alternative"
[^m2]: arxiv-2512-05145 — "we generate N responses from the base model"
[^m3]: arxiv-2512-05145 — "examples where at least 5 responses are identical, filtering out cases with greater diversity."
[^m4]: arxiv-2512-05145 — "we sample 16 times, and pick"
[^m5]: arxiv-2512-05145 — "as the resulting pairs can be trivially easy when the wrong answer is obviously incorrect."
[^m6]: arxiv-2512-05145 — "using majority voting to filter the synthetic pairs yields better performance after a few iterations."
[^m7]: arxiv-2512-05145 — "synthetic pairs constructed via majority voting yield 8.6% and 9.5% average improvement over correctness-filtered"
[^m8]: arxiv-2512-05145 — "consistently samples a greater number of data points per iteration when using majority"
[^m9]: arxiv-2512-05145 — "reduces the performance of the original majority set"
[^m10]: arxiv-2512-05145 — "be correct, especially in areas when the model struggles."
[^m11]: arxiv-2512-05145 — "more efficiently and achieves even greater performance gains."
