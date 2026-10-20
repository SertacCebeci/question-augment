---
description: "During RL, a rubric pool is refreshed from search evidence and sibling rollouts, and criteria whose scores do not vary across rollouts are dropped, so the reward keeps separating the policy's answers."
aliases: ["evolving rubrics", "rubric buffer", "RLER rubric pool", "active rubric buffer", "variance-pruned rubric pool"]
sources: ["arxiv-2511-19399"]
---
# Evolving rubric buffer

A rubric reward scores a rollout by a weighted sum of criteria, each judged by a model that outputs 0, 0.5 or 1.[^d1] If the criteria are written once before training, they go stale as the policy changes: the same items get met by more and more answers and stop telling them apart. The DR Tulu paper keeps a per-question buffer of criteria and rewrites it during training. At each training step, a rubric model is given the question, the sampled answers with their search traces, and the criteria already in the buffer, and it proposes new ones.[^d2] It is asked for two kinds. Positive criteria capture "strengths or new, relevant knowledge" that the current policy has found and the buffer does not yet reflect. Negative criteria "summarize common undesirable behaviors, such as reward hacking".[^d14]

The buffer is then cut back. After each rollout group, every active criterion is scored on every response. A criterion "with zero variance in their corresponding rewards" is removed, because it cannot separate the answers. The remaining criteria are ranked by their standard deviation, and "we retain only the top Kmax rubrics" with the largest values.[^d4] The pool therefore stays small, and what it holds is whatever currently splits the policy's answers. Negative criteria are the paper's answer to reward hacking: its example is verbatim copying of retrieved text to raise citation precision, which can be "identified and suppressed by negative rubrics."[^d5]

The new criteria are better than static ones because of what the rubric model can see. The paper's stated intuition is "providing the rubric generator with privileged information that is unavailable to the policy during generation", which it calls "thereby creating a generation–verification gap."[^d6] The privileged information has two parts: external knowledge from search rollouts, and "multiple independently sampled model responses, which provide contrastive signals for assessing relative quality."[^d7] The buffer starts from the same source. "Before training, we initialize the rubric buffer with search-based rubrics," written from web results for the question alone.[^d8]

What was measured is modest. Removing the evolving updates and keeping the search-based criteria fixed gives "up to a 2-point drop in average performance", and the gap widens over training.[^d9] The authors read the widening as "evolving rubrics capture new knowledge the model explores."[^d10] A separate table reports that "Search-based static rubrics work best" against general and closed-book static rubrics.[^d11] The headline gains of 6.4 to 16.0 points over the finetuned model belong to the whole recipe, not to the evolution step alone.

## Limits

- The 2-point figure is one ablation, on the paper's training setup. The parts I read report no spread across seeds, so the size of the effect is not established beyond that run (my reading).
- The rubric model is prompted, not trained, as far as the text describes it (my reading). Its choice matters: a Qwen3-8B judge and generator "only underperforms using GPT models by 1.3 points", against 4.4 points above the SFT checkpoint.[^d12] The open model gives up some of the gain, so the buffer's quality is tied to the model that writes it.
- Pruning by zero variance removes a criterion that every rollout fails as well as one every rollout meets. A criterion the whole group fails, and the policy has not yet learned, is dropped at the first step where it cannot split the group. This is my inference from the rule as written; the paper does not discuss it.
- Ranking by standard deviation favours criteria that split the group. A split on a feature unrelated to quality also has spread. The paper reports no check that the kept criteria are valid, only that the training reward rises.
- Training reward did not track evaluation. The authors observe that the highest-reward models "did not necessarily achieve the highest downstream evaluation performance", and attribute part of this to a judge mismatch that "can lead to reward hacking toward preferences specific to the training-time judge."[^d13]

## Related

- [[co-evolving-rubric-generator]] — the same idea that the rubric has to move with the policy, but there the generator is a trained second model paid for score spread; here the generator is prompted and spread only decides which criteria stay
- [[generation-verification-gap]] — the gap the search and sibling-rollout evidence is meant to open between the rubric writer and the policy
- [[retrieval-grounded-rubric-synthesis]] — retrieval there supplies past rubrics as exemplars; here it supplies web evidence for new criteria
- [[question-specific-rubric]] — the per-question target this buffer is kept for
- [[rubric-difficulty-evolution]] — the same saturation problem, answered by extending a fixed rubric from reference answers instead of rewriting the pool

[^d1]: arxiv-2511-19399 — "Each rubric is evaluated by a judge LM that outputs"
[^d2]: arxiv-2511-19399 — "the prompt x, all sampled responses"
[^d3]: arxiv-2511-19399 — "positive rubrics, which capture strengths or new"
[^d14]: arxiv-2511-19399 — "negative rubrics, which summarize common undesirable behaviors, such as reward hacking"
[^d4]: arxiv-2511-19399 — "with zero variance in their corresponding rewards are removed as they offer no discriminative value"
[^d5]: arxiv-2511-19399 — "identified and suppressed by negative rubrics"
[^d6]: arxiv-2511-19399 — "providing the rubric generator with privileged information that is unavailable to the policy during generation"
[^d7]: arxiv-2511-19399 — "multiple independently sampled model responses, which provide contrastive signals for assessing relative quality"
[^d8]: arxiv-2511-19399 — "Before training, we initialize the rubric buffer with search-based rubrics."
[^d9]: arxiv-2511-19399 — "Removing evolving rubrics results in up to a 2-point drop in average performance"
[^d10]: arxiv-2511-19399 — "evolving rubrics capture new knowledge the model explores"
[^d11]: arxiv-2511-19399 — "Search-based static rubrics work best."
[^d12]: arxiv-2511-19399 — "only 1.3 points behind the GPT-judge configuration"
[^d13]: arxiv-2511-19399 — "did not necessarily achieve the highest downstream evaluation performance"
