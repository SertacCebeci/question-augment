---
description: "Ranking all candidate answers by summed token log-probability and scoring the ranking with average precision reads multi-valued factual recall; scores fall as true answers multiply."
aliases: ["rank-based factual probing", "log-probability candidate ranking", "surface-set ranking", "mean average precision over log-probabilities"]
sources: ["arxiv-2512-11110"]
---
# Candidate-ranking average precision

Factual probing usually either asks a model to generate an answer and checks it against a gold answer, or ranks a fixed set of candidates. The closed version does not generate. It fixes a surface set, which "includes all possible answers across all subjects," and scores each candidate by the probability the model assigns to it. The paper analyzes "the model" through its assigned probabilities, not through text it writes: "Instead of generating new tokens, we analyze the model."[^c1]

**How a candidate is scored.** The log-probability of a multi-token candidate is built token by token. The log-probability of the first token "is obtained and appended to the original" prompt; the prompt is then extended by the scored tokens, and the next token is scored against this longer prompt.[^c2][^c3] The candidates are ranked by their cumulative score, and the ranking is what gets evaluated.

**How the ranking is scored.** Average precision (AP) is the metric. Its core statement in the paper is that "Average Precision measures how well relevant items" are retrieved and ranked.[^c4] Concretely, it is the mean of precision@k over the ranks where a gold answer appears, divided by the number of gold answers |G|. The paper uses mean average precision (mAP) over prompts, subjects, languages and models.[^c5] The authors chose AP over the precision@k that LAMA used, to "account for multi-entity answers and to more accurately" score the ranking.[^c6][^c7]

**What it shows for multi-valued answers.** With several true answers per question, the question is whether all of them rise to the top. The paper's result is that the model "performs worse when multiple correct answers exist, making it more difficult to maintain factual consistency across all entities."[^c8] The effect is tied to entity count: mAP "increases when the average entity count decreases."[^c9] The reading is that a ranker which places one gold answer high can still lose the others, and AP registers that where a single top-k hit does not.

Language and model size move mAP too, but the text gives two English figures: one passage reports "mean average precision is observed for English (35%)," and another gives "(MAP) of 38%" for the same language.[^c10][^c11] The paper also reports that Gemma-3-4B "achieves the lowest performance in terms of mean average precision."[^c12]

## Limits

- The candidate pool is closed. Scoring is "restricted to entities explicitly included in our" dataset.[^c13] A correct answer that is not in the pool cannot be credited, so the score measures recall within a curated list, not open recall.
- The text does not say whether the cumulative log-probability is normalised by candidate length. Multi-token candidates may score lower for that reason alone. This is my reading; the paper does not test it.
- The two English mAP figures conflict, and the text does not reconcile them. Comparisons across tables need care.
- The paper argues for AP over precision@k in one sentence. In the sections I read it does not run both metrics on the same items, so the choice is argued rather than measured.
- The analysis "is limited to three languages" and to models of 3B to 8B.[^c14] Whether the ranking tracks generated answers is left open: the authors say the task "can be extended to open-ended text" generation.[^c15]

## Related

- [[factual-inference-bias]] — the same candidate probabilities, read for a language-driven preference rather than for recall.
- [[recall-only-partial-credit]] — a multi-answer score that counts only coverage. My inference: AP also penalises a wrong candidate ranked above a gold one, which a recall-only score does not see.
- [[single-answer-training-prior]] — another multi-answer setting where recall lags, here because training gave one answer per query.

[^c1]: arxiv-2512-11110 — "Instead of generating new tokens, we analyze the model"
[^c2]: arxiv-2512-11110 — "first token is obtained and appended to the original"
[^c3]: arxiv-2512-11110 — "to this new prompt. This process continues until all the"
[^c4]: arxiv-2512-11110 — "Average Precision measures how well relevant items"
[^c5]: arxiv-2512-11110 — "It is computed as the mean"
[^c6]: arxiv-2512-11110 — "employs Precision@k as its evaluation metric"
[^c7]: arxiv-2512-11110 — "account for multi-entity answers and to more accurately"
[^c8]: arxiv-2512-11110 — "performs worse when multiple correct answers exist"
[^c9]: arxiv-2512-11110 — "average entity count decreases."
[^c10]: arxiv-2512-11110 — "mean average precision is observed for English (35%),"
[^c11]: arxiv-2512-11110 — "(MAP) of 38%"
[^c12]: arxiv-2512-11110 — "achieves the lowest performance in terms of mean average precision"
[^c13]: arxiv-2512-11110 — "restricted to entities explicitly included in our"
[^c14]: arxiv-2512-11110 — "our analysis is limited to three languages"
[^c15]: arxiv-2512-11110 — "This task can be extended to open-ended text"
