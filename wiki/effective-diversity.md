---
description: "Diversity counted only over outputs that pass a utility check: the number of distinct high-utility items in a generated set, which can differ from the raw count of distinct items."
aliases: ["effective diversity", "utility-restricted diversity", "distinct high-utility count"]
sources: ["arxiv-2512-23601", "arxiv-2511-19942"]
---
# Effective diversity

A generated set can be diverse in two different senses. Raw diversity counts the distinct items in the set whether or not they work. Effective diversity counts only the distinct items that pass a utility check: it is the diversity of the high-utility subset, where an item has utility 1 only if it is valid, comprehensible and relevant to its context. In the words of the paper, "Intuitively, it measures the number of distinct high-utility tasks."[^e1]

The mechanism is two filters applied in order. First the set is cut down to the items that pass the utility test, which for generated programming tasks means three checks: "Utility(P) = 1 if the task P satisfies all three criteria."[^e2] Validity is checked by running a generated solution against the task's evaluation guide, while context relevance and comprehensibility are judged.[^e3] Then the survivors are counted for distinctness. Because the two counts come apart, a generator can look diverse by producing many distinct items that fail, and a method that is diverse on the raw count may have few distinct valid items once failures are removed.

The paper reports both counts across K generated tasks (its Figure 3). Its diversity-promoting method keeps nearly all its raw diversity under the utility cut: at K = 50 it reaches "about 12 distinct tasks when restricted to high-utility tasks only," against about 13 on all tasks.[^e4][^e17] The two baselines, which prompt for theme and concept together, reach "about 8 distinct high-utility tasks" at the same K.[^e5] The abstract puts the overall gain at "about 1.6×" the baselines in distinct high-utility tasks.[^e15]

Distinctness is itself measured in two ways. The automatic way is the Vendi score over task embeddings, described in [[vendi-score]]. The human way is expert clustering: an evaluator sorts the tasks into clusters by semantic similarity, opening a new cluster when a task fits none, and "The number of final clusters provides an expert-annotated measure of task diversity."[^e6] On the expert count the same method reaches "about 16 clusters at K = 50," which the paper sets against a baseline of about 9.[^e7][^e16] The expert counts run higher than the automatic ones, so the absolute number of effective diversity depends on the instrument, while the ordering of methods is the same.[^e8]

The same restriction appears in an RL analysis of answer sampling, where diversity is counted only over the correct set: "we only care about diversity over correct (high reward) trajectories."[^e18] That paper measures diversity as a normalised variance of the policy's probabilities over the correct solutions, not as a count of distinct items. The restriction carries over; the measure does not (my inference).

## Limits

- The utility judge is a language model, not a test. "For scalability, we use an LLM-as-a-judge approach."[^e9] The paper uses a judge from a different model family than the generator, because "Using a model from a different family than the generator also avoids self-preference bias."[^e10] Its error rate on the two non-execution criteria is not reported here, so the count is only as sound as that judge.
- The utility cut is binary. An item that barely passes and one that is clearly good count the same, and an item that fails for a small reason is removed entirely. The measure says nothing about graded quality.
- The evaluation is one generator (Qwen3-235B-A22B), one domain (introductory Python), and 20 task contexts built from 4 themes and 5 concepts.[^e11] The authors list extension to harder problems and other subjects as open.[^e12]
- The expert part is small: three evaluators, each given a different theme, so "inter-rater agreement measures are not applicable."[^e13]
- The paper says that "encouraging diverse outputs can conflict with the utility constraints," and cites that conflict to prior work rather than measuring it on its own sets.[^e14] So the result that the cut costs the method little is one case, not a general fact about diversity and utility.

## Related

- [[vendi-score]] — the automatic distinctness count that the effective count is built on
- [[divergent-convergent]] — the prompting split the paper uses to raise the count
- [[innovation-correctness-tradeoff-in-problem-generation]] — the conflict between novelty and correctness in a different setting, where the tradeoff was not avoided
- [[questioning-diversity]] — a raw distinctness diagnostic for question sets, with no utility filter
- [[curriculum-collapse]] — generated questions drifting onto a few types, the failure this count is meant to expose
- [[selection-reinforcement-bias]] — the RL account in which diversity is restricted to correct trajectories and then narrows there
- [[solution-multiplicity]] — a per-problem count of distinct correct solutions, the answer-side analogue of counting distinct high-utility items

[^e1]: arxiv-2512-23601 — "Intuitively, it measures the number of distinct high-utility tasks."
[^e2]: arxiv-2512-23601 — "Utility(P) = 1 if the task P satisfies all three criteria"
[^e3]: arxiv-2512-23601 — "executed against Peval to verify Task Validity"
[^e4]: arxiv-2512-23601 — "about 12 distinct tasks when restricted to high-utility tasks only"
[^e5]: arxiv-2512-23601 — "In contrast, both C OT and BASE generate about 8 distinct high-utility tasks"
[^e6]: arxiv-2512-23601 — "The number of final clusters provides an expert-annotated measure of task diversity"
[^e7]: arxiv-2512-23601 — "evaluators created about 16 clusters at K = 50"
[^e8]: arxiv-2512-23601 — "effective diversity perceived by experts has a similar pattern but is generally higher than the automated Vendi Score"
[^e9]: arxiv-2512-23601 — "For scalability, we use an LLM-as-a-judge approach"
[^e10]: arxiv-2512-23601 — "different family than the generator also avoids self-preference bias"
[^e11]: arxiv-2512-23601 — "We use a set of 20 task contexts"
[^e12]: arxiv-2512-23601 — "extending this framework to other educational domains, such as mathematics or science, would demonstrate its generalizability"
[^e13]: arxiv-2512-23601 — "inter-rater agreement measures are not applicable"
[^e14]: arxiv-2512-23601 — "This objective is challenging because encouraging diverse outputs can conflict with the utility constraints"
[^e15]: arxiv-2512-23601 — "produces significantly more distinct high-utility tasks (about 1.6×) than baselines"
[^e16]: arxiv-2512-23601 — "compared to about 9 clusters for C OT"
[^e17]: arxiv-2512-23601 — "generates about 13 distinct tasks (dashed blue line)"
[^e18]: arxiv-2511-19942 — "we only care about diversity over correct (high reward) trajectories"
