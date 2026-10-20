---
description: "Pre-trained VLMs keep a task-specific response length (long on math, short on perception) that looks inherited from pretraining; uniform long-reasoning training overrides it."
aliases: ["implicit response-length prior", "model length prior", "length tendency of a pre-trained model"]
sources: ["arxiv-2511-16670"]
---
# Response-length prior

A pre-trained vision-language model has a habit of how long its answer runs, and that habit depends more on the kind of question than on the individual item. The paper measured four general-purpose VLMs of different sizes, Qwen2.5-VL at 3B and 7B and InternVL3 at 2B and 8B, on a range of visual question-answering tasks. The response lengths of these models are "generally consistent within the same task" while varying across tasks.[^c1] Concretely, the models "consistently generate long responses on mathematical problems," produce medium-length answers for chart understanding and counting, and answer briefly on general perception and OCR questions.[^c2]

The authors call this an implicit prior: "an implicit prior on response length emerges during large-scale pre-training."[^c3] Their figure caption puts the same reading more loosely, "suggesting the presence of an implicit response-length prior inherited from large-scale pre-training."[^c4] The prior is therefore a regularity of the model and the task together. It is not a setting the user chooses, and it is present before any reasoning training.

The paper's point is that standard reasoning training overrides this prior: "most existing reasoning methods override this prior by uniformly encouraging extended reasoning." The result is that such models "rely on long output tokens to get the right answer."[^c5] Length is not free. On MMStar, two reasoning models "significantly underperform the base model with a limited token budget, such as" 100 tokens, and only pull ahead once the budget passes about 250 tokens.[^c6] So the length a model writes is part of how it reaches the answer, and a prior that says how long it will write is a fact about the base model that a training method can read or ignore.

What the prior is not: it is measured as an average response length per task, and the sections read do not use it as a difficulty score for a single item. A long answer on a question is evidence that the model wrote much, not that the question is hard for it, and the paper does not separate those two. This differs from the use of a teacher's answer length as a question-level difficulty proxy (see [[response-length-difficulty-proxy]]), where the length belongs to the data. Here it belongs to the model's own behavior on its own rollouts. The method built on this prior is length-anchored-dual-mode-thinking.

## Limits

- Four models, two families, and coarse task groups (math, chart and counting, perception and OCR). The text read does not test text-only reasoning, other families, or finer task splits.
- "Generally consistent" is the authors' summary of a figure. The sections read give no variance across items or across seeds.
- "Inherited from large-scale pre-training" is the authors' interpretation. No comparison against a pre-training checkpoint or a different training stage was read, so the source of the prior is not established here (my reading).
- A length prior says how much a model tends to write, not whether it is right. Short answers can be correct or wrong, and the sections read do not report accuracy by length within a task (my inference).
- The budget comparison in Fig. 3 uses one benchmark (MMStar) and one curve per model.

## Related

- [[response-length-difficulty-proxy]] — teacher response length as a property of the question, the contrast case
- [[moderate-adaptive-reasoning-length]] — length as a cap on reasoning, where the best cap varies by task
- [[complexity-tiered-strategy-routing]] — prompting strategies that overthink simple tasks, the failure this prior is meant to avoid
- length-anchored-dual-mode-thinking — the method that reads this prior as two thinking modes

[^c1]: arxiv-2511-16670 — "the response lengths of different models are generally consistent within the same task"
[^c2]: arxiv-2511-16670 — "consistently generate long responses on mathematical problems"
[^c3]: arxiv-2511-16670 — "an implicit prior on response length emerges during large-scale pre-training."
[^c4]: arxiv-2511-16670 — "suggesting the presence of an implicit response-length prior inherited from large-scale pre-training."
[^c5]: arxiv-2511-16670 — "most existing reasoning methods override this prior by uniformly encouraging extended reasoning."
[^c6]: arxiv-2511-16670 — "significantly underperform the base model with a limited token budget, such as"
