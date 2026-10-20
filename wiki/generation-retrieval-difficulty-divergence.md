---
description: "A text query can be hard for a text-to-image generator yet easy for a retriever: human-judged performance correlates only weakly across the two tasks."
aliases: ["generation vs retrieval prompt difficulty", "cross-task query difficulty", "task-dependent prompt difficulty"]
sources: ["doi-10-48550-arxiv-2406-04746"]
---
# Generation and retrieval difficulty diverge

A text query has two difficulties, one for each task it serves: how hard it is for a text-to-image generator to produce relevant images, and how hard it is for a text-to-image retriever to find them. In the PQPP benchmark both were measured on the same 10,200 texts with human relevance judgments, and the two are only weakly related. The Pearson correlation between generation performance (HBPP) and retrieval performance (P@10) is 0.135, and with reciprocal rank it is 0.072. Kendall's tau is 0.093 and 0.048.[^c1] The paper's own Table 2 gives these as the first two rows. Reading the flattened table, the two retrieval measures correlate far more strongly with each other (Pearson 0.560), so the weak link lies between the tasks, not between the metrics. The authors call the correlation "a very low correlation between the two tasks", and conclude that the tasks are "rather orthogonal".[^c2][^c3]

The correlations are significant but small. The paper reports them as "statistically significant", which here means they are distinguishable from zero, not that they are large.[^c4] The point of the result is that a difficulty estimate taken from one task is a poor guide to the other. Which task is meant has to be named before the question "is this prompt hard?" has an answer.

## What the examples show

The authors inspected prompts in four cells: high or low performance in each task. The illustrative examples point to task-specific causes rather than a single shared difficulty.

- Prompts with an animate subject doing something in a place are easy in both tasks. "The queries usually refer to an animate object performing an action in a location."[^c5] Retrieval finds many matches and generation has few constraints to satisfy.
- Prompts with specific attributes on inanimate objects are the reverse. "Generative models seem to handle many specific attributes rather well", while retrieval must find an existing image that matches the same description.[^c6]
- Prompts about a person performing a sport action are easy to retrieve, since the image collection has many such pictures. Generators, however, "struggle to generate a person in a" specific pose that involves an object.[^c7]
- Groups of people doing uncommon actions in specific places, and rare or misspelled objects, are hard for both.[^c8]

The authors summarize the contrast as "task-specific characteristics placing prompt and query performance prediction at opposite poles".[^c9]

My extension, which the paper does not test: retrieval difficulty is bounded by what the image pool contains, while generation difficulty is bounded by what the model can compose. On that reading, a retrieval difficulty says something about coverage of the pool, and a generation difficulty about compositional demand. The two would then need different features. This follows from the examples but is not measured here.

## Limits

- One benchmark, two generators (SDXL and GLIDE), two retrievers (CLIP and BLIP-2) and one image pool (MS COCO). The low correlation is a property of this pairing as measured. Another generator or another corpus could give a different number. The paper's cross-model experiments would show that, and I did not read them.
- The correlations are small. Their significance is against random chance, which shows they are not zero, not that the tasks are unrelated in any strong sense.
- The categories come from manual inspection of illustrative captions (Figure 3). The paper gives no count of prompts per cell, so how common each pattern is remains unestablished.
- The retrieval relevance sets are capped at 2,000 candidate images per query.[^c10] A query whose relevant images were cut off by the cap could look harder for retrieval than it is. This is my inference, not something the paper reports.
- The row-to-value mapping of Table 2 is my reading of flattened text. The values themselves are the paper's.

## Related

- [[query-performance-prediction]] — the measure of prompt and query performance, and the predictors, that these correlations are computed over.

[^c1]: doi-10-48550-arxiv-2406-04746 — "Pearson and Kendall τ correlation coefficients between"
[^c2]: doi-10-48550-arxiv-2406-04746 — "there is a very low correlation between the two tasks"
[^c3]: doi-10-48550-arxiv-2406-04746 — "are rather orthogonal, confirming that image generation requires the development of dedicated prompt performance"
[^c4]: doi-10-48550-arxiv-2406-04746 — "the correlations are statistically significant"
[^c5]: doi-10-48550-arxiv-2406-04746 — "the queries usually refer to an animate object performing an action in a location"
[^c6]: doi-10-48550-arxiv-2406-04746 — "Generative models seem to handle many specific attributes rather well"
[^c7]: doi-10-48550-arxiv-2406-04746 — "generative models struggle to generate a person in a"
[^c8]: doi-10-48550-arxiv-2406-04746 — "which are rather uncommon"
[^c9]: doi-10-48550-arxiv-2406-04746 — "placing prompt and query performance prediction at opposite poles"
[^c10]: doi-10-48550-arxiv-2406-04746 — "restrict the number of retrieved images to 2,000 per query"
