---
description: "Rationale token learnability: the F1 of a binary token classifier that finds rationale tokens, as a ratio over a majority-label baseline; in one study it does not track sufficiency."
aliases: ["token classification of rationales", "TC metric", "rationale token-F1 ratio", "token-level learnability of rationales"]
sources: ["arxiv-2511-16353"]
---
# Rationale token learnability

Rationale token learnability asks whether a model can tell rationale tokens from their context. A binary token classifier is trained on rationales as token labels, and its performance is compared with a baseline that assigns the majority label to each token.[^t1] The paper's metric, TC, is the ratio of the classifier's token-F1 to the baseline's token-F1, computed per instance and averaged over a dataset.[^t2] A ratio is used so that cross-task comparisons are less arbitrary and relative gains are readable: TC above one means the classifier beats the baseline, and the greater TC, the greater the improvement.[^t3]

On my reading, the metric is a relation between a model and a rationale mask, not a property of the mask alone. Because token labels differ with each model's tokenisation, the baseline is model-specific as well.[^t4] The authors are explicit that the majority baseline is a proxy that places model performance within task-specific complexity, "not for benchmarking purposes."[^t5]

The expected relation is the one the paper tests: informative rationales should be easier to identify, so TC should be high where the contextual impact is low.[^t6] The result is a null. "The learnability of a token classifier does not correlate with CI," and the abstract puts it as "sufficiency and token classification appear to be unrelated."[^t7][^t8]

The comparison across models is also informative. TC is higher for Pythia and GPT-Neo than for BERT on 9 of 14 tasks, and ModernBERT beats the two autoregressive models on at least 10 tasks.[^t9][^t10] So the measure does separate models, even though it does not separate rationales in the way the sufficiency score would suggest.

The paper's proposed reason for the null is that a model can do well on the test data through shortcuts in the context, which gives it high CI despite informative rationales.[^t11] This is an explanation offered by the authors, not a result they measured directly.

## Limits

The evidence is one work on six datasets and four models, three seeds each, with default hyperparameters. The tokenisers differ between models, so the token alignment itself varies and the "same rationale" is not the same set of labels for each model.[^t12] The metric depends on the chosen majority baseline; the paper does not test other baselines, and no claim is made that TC ranks tasks by difficulty beyond the proxy use. The null correlation is a finding about these datasets; it does not show that identifiability and informativeness are unrelated in general.

## Related

- [[contextual-impact-of-rationale]] — the sufficiency-based measure this metric is compared against; the paper finds the two unrelated.
- [[attention-regularization-from-rationales]] — the other paradigm in the same work, which uses the same masks as a loss on attention instead of as token labels.

[^t1]: arxiv-2511-16353 — "assigns the majority label to each token"
[^t2]: arxiv-2511-16353 — "It measures the relative performance of the token classifier T on rationales"
[^t3]: arxiv-2511-16353 — "the greater the improvement"
[^t4]: arxiv-2511-16353 — "since token labels differ due to different tokenisations"
[^t5]: arxiv-2511-16353 — "not for benchmarking purposes"
[^t6]: arxiv-2511-16353 — "for informative rationales, i.e., for rationales where"
[^t7]: arxiv-2511-16353 — "the learnability of a token classifier does not correlate with CI"
[^t8]: arxiv-2511-16353 — "sufficiency and token classification appear to be unrelated"
[^t9]: arxiv-2511-16353 — "higher for Pythia and GPT-Neo on 9 out of"
[^t10]: arxiv-2511-16353 — "ModernBERT outperforms the former two on at least 10 tasks"
[^t11]: arxiv-2511-16353 — "models that perform well on test"
[^t12]: arxiv-2511-16353 — "As different models are pre-trained using different tokenisers"
