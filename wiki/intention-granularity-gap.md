---
description: "Inferring a speaker's communicative intention degrades as the label set grows finer and multi-select; in recommendation dialogue, LLMs labelled coarse intents far better than fine ones."
aliases: ["granularity gap in intention inference", "fine-grained intent discrimination", "coarse versus fine intention accuracy"]
sources: ["arxiv-2511-22275"]
---
# Intention granularity gap

The same utterance can be given an intention at more than one level of specificity: a coarse class such as a request or a recommendation, or a fine subclass such as requesting preferences, seeking feedback or asking a clarifying question. The two levels are not equally hard for a language model, and the difference is measured, not only argued. RecToM, a benchmark built on REDIAL movie-recommendation dialogues, asks the intention of each utterance at both levels. The fine level offers 10 categories for the recommender and 16 for the seeker.[^c9] The paper's summary of its results is that "While LLMs perform well on coarse-grained intention classification, their performance drops notably on finegrained tasks."[^c1]

The drop is large in the reported numbers. For GPT-4o on the seeker side, coarse accuracy was 64.22%[^c2] and fine accuracy 28.84%.[^c3] Averaged over the models, fine-grained intention reasoning for the recommender role was 27.74%, on items where the answer type is multiple choice.[^c4] Coarse intention is therefore close to usable, while fine intention is not, at least for the models and prompts tested.

The fine items differ from the coarse ones in two ways at once. They are finer labels, and they are multi-select: "An utterance from either the recommender or seeker may express multiple distinct intentions within a single sentence."[^c5] The paper's own reading of the pattern is that the granularity gap "reveals fundamental representational deficits"[^c6], and it also writes that LLM ability to infer participants' intentions "deteriorates as the choice space becomes more complex."[^c7] The benchmark includes a Fine2Coarse score, "the accuracy of mapping fine-grained intentions to their predefined coarse-grained categories".[^c8] That score would separate the two steps, a fine label and its coarse parent, but I did not read its values, so I do not report what it shows.

For asking, the point is that a label set is part of the question. An intention asked at fine grain is a harder question than the same utterance asked at coarse grain, so a score on a benchmark depends on its label granularity as well as on the model. This is my inference from the two levels; the paper does not test it as a design claim.

## Limits

- One benchmark, one domain (movie recommendation dialogues). The main results evaluate "on five state-of-the-art LLMs from diverse sources",[^c11] so the gap is shown for a handful of models, not for the field.
- Granularity, option count and multi-select are confounded in the fine items. No ablation separates them, so the gap cannot be attributed to label granularity alone.
- The "representational deficit" reading is the authors' interpretation. The paper does not probe internal representations.
- Prompting did not close the gap. Chain-of-thought "yields only marginal improvements in this CRS context".[^c10] The paper tested only one CoT prompt, and a different elicitation may behave differently.
- The labels are the annotators' categories. Whether a finer category is a real distinction users would recognise, or a boundary the annotators drew, is not tested here.

## Related

- [[option-matching-shortcut]] — another way closed candidate options change which process answers a question; there the options are removed, here they are the difficulty
- [[planning-theory-of-mind-elicitation-gap]] — the same family of conversational mental-state questions, but about eliciting states by asking, not labelling an utterance's intention

[^c1]: arxiv-2511-22275 — "While LLMs perform well on coarse-grained intention classification, their performance drops notably on finegrained tasks."
[^c2]: arxiv-2511-22275 — "GPT-4o: 64.22% for seeker"
[^c3]: arxiv-2511-22275 — "28.84% for seeker"
[^c4]: arxiv-2511-22275 — "averaging only 27.74% of fine-grained intention reasoning for the recommender role"
[^c5]: arxiv-2511-22275 — "may express multiple distinct intentions within a single sentence"
[^c6]: arxiv-2511-22275 — "reveals fundamental representational deficits"
[^c7]: arxiv-2511-22275 — "deteriorates as the choice space becomes more complex"
[^c8]: arxiv-2511-22275 — "Fine2Coarse intention reflect the accuracy of mapping fine-grained intentions to their predefined coarse-grained categories"
[^c9]: arxiv-2511-22275 — "fine-grained categories for the recommender and 16 for the seeker"
[^c10]: arxiv-2511-22275 — "marginal improvements in this CRS context"
[^c11]: arxiv-2511-22275 — "on five state-of-the-art LLMs from diverse sources"
