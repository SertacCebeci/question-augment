---
description: "In extractive question answering, accuracy falls as the gold answer lengthens, and the best model changes with answer length, so length is a difficulty axis of its own."
aliases: ["answer length effect", "answer-length accuracy decline", "span length and accuracy"]
sources: ["arxiv-2512-00323"]
---
# Answer length as a difficulty axis

In extractive question answering a model takes a question and a context and returns a span of the context. The model is given the question and context, and the answer is "answer extraction, where models extract answers from the context".[^c1] The gold answer has a length, counted in words, and that length can be sorted and scored separately from what the question asks. In a benchmark of 47 context-based models on eight datasets, the authors bucketed gold answers by length, "from 1 to 5 words", and computed each model's accuracy within each bucket.[^c2]

The measured result is a decline. The authors "identified a consistent decline in model performance as the answer length increased" for the top model.[^c3] The abstract makes the same claim for the models as a whole: the model's performance "usually decreases with an increase in the answer length".[^c4] The decline is therefore a property of the answer, holding the question-answering setup fixed, and it is visible in accuracy before any architecture is named.

Length also changes which model wins. "The optimal performing model can vary based on the length of the answer."[^c5] The clearest case is short answers: "when predicting answers consisting of only two words" a smaller model reached 55% accuracy, above the overall best model.[^c6] So a single leaderboard position is a statement about one answer-length profile, not about the task.

The paper offers a design reason, not a measured one: "Some models are tailored to pinpoint the precise answer, while others are designed to return more contextual information around the actual answer".[^c7] Its text then says only that "this variation is influenced by factors such as model architecture".[^c8] Which architectural property produces which length profile is not tested. What is measured is the profile itself.

For someone formulating a question, the point is that the expected answer length is part of what the question sets up. A question whose answer is one token and one whose answer is a phrase draw on different parts of the accuracy surface. This is my inference from the table, not a result the paper tests.

## Limits

The length buckets are pooled over eight datasets with different answer distributions. The decline is reported across all datasets together, so a difference in dataset mix can carry part of it. The paper's own figure caption says that as length grows "the models' performance may either decrease or increase",[^c9] which is a weaker statement than the abstract's "usually decreases". The per-length best-model table gives the winning model and accuracy in each cell, but the text does not state how many questions each cell holds, so cells with 0 or 1.0 cannot be read for their reliability.

The ranking itself is not sharply separated. The authors report that "the results indicate no statistically significant difference among the top 11 best-performing models".[^c10] A different winner at a given length is therefore a difference the paper does not show to be reliable.

The work covers extractive models only. It is stated that the models "use a question and context to extract an answer";[^c11] generative or free-form answers are outside the measured range, and whether a length decline holds there is untested.

## Related

- [[answer-source-category]] — where the answer sits in the evidence is a second label on the same extracted answer; it sorts accuracy by location, while this note sorts it by length.
- [[proof-depth-decline-under-shift]] — accuracy falling as a chain of inference lengthens is the same kind of length-indexed decline, measured on deduction rather than span extraction.
- [[answer-evidence-embedding-similarity]] — answer length also confounds a score of grounding, where short answers are scored unfairly by similarity; length is a confound for scoring as well as for accuracy.
- [[extractive-abstractive-verifiability-tradeoff]] — answer form on another axis: how far a cited answer departs from its quotes.

[^c1]: arxiv-2512-00323 — "answer extraction, where models extract answers from the context"
[^c2]: arxiv-2512-00323 — "The answer length spans from 1 to 5 words"
[^c3]: arxiv-2512-00323 — "model performance as the answer length increased"
[^c4]: arxiv-2512-00323 — "usually decreases with an increase in the answer length"
[^c5]: arxiv-2512-00323 — "The optimal performing model can vary based on the"
[^c6]: arxiv-2512-00323 — "when predicting answers consisting of only two words"
[^c7]: arxiv-2512-00323 — "Some models are tailored to pinpoint the precise answer, while others are designed to return"
[^c8]: arxiv-2512-00323 — "This variation is influenced by factors such as model architecture"
[^c9]: arxiv-2512-00323 — "may either decrease or increase"
[^c10]: arxiv-2512-00323 — "The results indicate no statistically significant difference among the top 11 best-performing models"
[^c11]: arxiv-2512-00323 — "We considered models that use a question and context to extract an answer"
