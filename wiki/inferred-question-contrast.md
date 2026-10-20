---
description: "A dispreferred answer can be made by inferring the question a good answer seems to address and then answering a different one, so the pair isolates whether an evaluator checks relevance."
aliases: ["inferred question contrast", "IQ contrast", "question-inferred negatives"]
sources: ["doi-10-48550-arxiv-2605-03871"]
---
# Inferred-question contrast

Preference pairs for training an evaluator usually differ in quality. This construction makes the two responses differ in fit to the question. Given a preferred response a+ to a question q, the policy first reads a+ and works out the question it seems to answer: the policy "infers what question a+ appears to address," producing a question q̂.[^i1] A dispreferred response is then written for q̂ rather than for q. The result can be fluent and on topic and still answer the wrong question, while a+ answers the one that was asked.

The paper states the purpose of the pair: "This provides signal about whether the rubric captures question-relevance," and rubrics "that check whether the response addresses" the intended question should score a+ higher.[^i2] The logic, which is mine and not the paper's wording, is that a rubric rewarding polish, length or tone cannot separate the two when both are polished. Only a criterion that tests the asked question can. The pair therefore measures one property, relevance to q, with the quality of the prose held roughly constant.

The measured effect is mixed. In the ablation over preference sources, the inferred-question pairs alone gave a RewardBench-2 score of 48.1 and a downstream policy average of 68.6, against 46.0 and 69.3 for temporal pairs (my reading of the paper's Table 7, whose layout is hard to follow). So this source raised the rubric's accuracy on the benchmark while lowering the policy. Combined with the other two sources, it gave the lowest policy average of the combinations tried. The paper does not explain this, and this note cannot either.

The idea transfers to asking and answering in one respect. Recovering the question an answer answers is the reverse of the act of stating a question's constraints: an asker fixes the question, and here the question is recovered from the answer to test the answer against it. What does not transfer is the reliance on a language model's guess at q̂ as ground truth.

## Limits

- The paper does not check whether q̂ is the question the answer really addresses, nor whether the dispreferred answer to q̂ is fluent. The construction assumes both (my inference).
- It is one source among three, in one recipe: Qwen3-8B, Tulu 3 prompts and a 1.7B judge. Its effect on other judges or tasks is not measured.
- Relevance is one criterion among many. A rubric trained on these pairs learns question fit; the paper's gains come from the full training pipeline, not from this pair type alone.
- Standalone it did not beat the temporal source on the policy average, so the paper does not show it adds value by itself.

## Related

- [[temporal-contrast-preference-pairs]] — the other self-generated pair source in the same paper, which varies the policy over time instead of the question
- [[co-evolving-rubric-generator]] — the rubric writer these pairs train, in a different setting
- [[rubric-conditioned-contrast]] — the source that conditions the policy on the rubric instead of inferring the question

[^i1]: doi-10-48550-arxiv-2605-03871 — "infers what question a+ appears to address"
[^i2]: doi-10-48550-arxiv-2605-03871 — "rubrics that check whether the response addresses"
