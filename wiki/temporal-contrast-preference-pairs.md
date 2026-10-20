---
description: "Preference pairs built from one policy's own rollouts at different training steps, the later response counted as preferred; the step gap sets how hard a pair is to tell apart."
aliases: ["temporal contrast", "checkpoint-contrast preference pairs", "earlier-rollout contrast"]
sources: ["doi-10-48550-arxiv-2605-03871"]
---
# Temporal contrast preference pairs

A learned evaluator needs pairs of responses with a known order, and in most work a person supplies that order. Temporal contrast takes the order from the training run instead. Every rollout is stored with the step at which it was drawn. For a question q, a response from the current policy is paired with a response to the same q drawn at an earlier step, and the later one is the preferred one. The premise is that the policy improves during training, so the order of each pair is, on average, an order of quality: the later response "is treated as preferred."[^t1]

The step gap is the difficulty dial. A pair drawn from far-apart steps usually differs clearly; a pair drawn from close steps is subtler. The paper states it directly: "gap produces easy pairs with clear quality differences, while a small gap produces harder" pairs, and those harder pairs "require more fine-grained rubrics."[^t2] Because old responses are replaced as training goes on, the pool of dispreferred examples moves with the policy, so the difficulty curve is not set by hand. The implementation keeps the age window explicit: "The age gap ensures rejected samples come from a sufficiently different policy version" and rejects samples that are too stale.[^t3]

What was measured is modest. Varying the step gap from [5, 20] to [100, 300] moved the policy average by about one point against the default [20, 100]; the authors say the variants "yield policies within 1–2 points of each other."[^t4] The more telling comparison is between sources. Temporal pairs alone gave the best downstream policy among the three preference sources, while the variant with the highest RewardBench-2 score did not produce the best policy: "the variant with the highest RewardBench-2 never" "produces the best policy" in the ablation groups.[^t5] So a rubric that ranks pairs well is not thereby the rubric that trains the policy best.

## Limits

- The order label is an assumption. If the policy regresses on some question, the later response is labelled preferred although it is worse. The paper does not report how often this happens, and it is not checked against a human reference (my inference).
- The construction needs a policy that changes during training. The paper says so in its sequential-training comparison: temporal contrast "requires a changing policy," which is why sequential training could not use this source.[^t6]
- The effect of the step gap is within the spread the authors themselves call comparable, so the paper does not show that the gap matters much on this suite.
- One recipe is measured: Qwen3-8B on Tulu 3 prompts with a 1.7B judge. Whether the same pairs help a policy trained with a different objective is not tested here.

## Related

- [[co-evolving-rubric-generator]] — a rubric writer trained beside the policy, rewarded by the spread of its scores rather than by ranking pairs
- [[preference-consistency-rubric-reward]] — the same ranking reward, but with human-labelled pairs in place of the policy's own history
- [[inferred-question-contrast]] — the other self-generated source, which varies the question rather than the policy's history
- [[rubric-conditioned-contrast]] — the third source, which conditions the policy on the rubric

[^t1]: doi-10-48550-arxiv-2605-03871 — "is treated as preferred"
[^t2]: doi-10-48550-arxiv-2605-03871 — "gap produces easy pairs with clear quality differences, while a small gap produces harder"
[^t3]: doi-10-48550-arxiv-2605-03871 — "The age gap ensures rejected samples come from a sufficiently different policy version"
[^t4]: doi-10-48550-arxiv-2605-03871 — "yield policies within 1–2 points of each other"
[^t5]: doi-10-48550-arxiv-2605-03871 — "the variant with the highest RewardBench-2 never"
[^t6]: doi-10-48550-arxiv-2605-03871 — "temporal contrast requires a changing policy"
