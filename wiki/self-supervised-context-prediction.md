---
description: "Predicting the tokens before or after a span of activations needs no labels, so training an activation verbalizer can scale to any text corpus and add diversity beyond supervised data."
aliases: ["context prediction task", "self-supervised activation context prediction", "previous and next token prediction from activations"]
sources: ["arxiv-2512-15674"]
---
# Self-supervised context prediction

The task takes a short span of text, passes its activations to a model, and asks the model to predict the tokens that come just before or just after that span. Because the target is the text itself, the training data costs nothing to label: "enabling unlimited training data generation from any text corpus."[^c1] For each example, K contiguous tokens are sampled "from a 50-50 mix of pretraining and conversational data," and the model is trained to predict the previous or next J tokens, with K and J drawn uniformly from 1 to 20.[^c2]

The design choice that carries the mechanism is that the answer is withheld from the question. "The input and target tokens do not overlap," so the model cannot copy the target from its prompt and must draw on the activations.[^c3] The task is one of three in the training mixture of the activation oracle (see [[activation-oracle]]), next to a supervised system-prompt set and binary classification.

What was measured. The authors ran a controlled comparison on Qwen3-8B at fixed sample counts, "we run a controlled ablation on Qwen3-8B," and tried to separate diversity from quantity, which they say "partially disentangles these two factors."[^c4][^c5] A 400k-example mixture in which 60% of the budget went to context prediction, "the truncated full mixture allocates 60% of its budget to the self-supervised context prediction," still "improves over the SPQA + Classification baseline on most evaluation metrics."[^c6][^c7] The authors read this as showing that the task "increases the diversity of activation-verbalization signals," and the full one-million-example mixture did better still: "the full 1M-example mixture outperforms the truncated mixture."[^c8][^c9] Their summary is that "Both diversity and quantity of training data improve performance."[^c10]

The mechanism claim is therefore comparative. Adding unlabeled context prediction to a supervised mix improved held-out generalization in one model at equal sample count. It is not shown that the task alone yields the oracle's gains, since the truncated mixture also contained less supervised question-answer data.

## Limits

The controlled comparison runs on one model. The authors state that "the value of added diversity is model and task dependent," so the gains seen on Qwen3-8B do not carry over automatically.[^c11] The separation of diversity from quantity rests on this single ablation.

The task's own scope is narrow: its targets are the adjacent tokens, which tests whether the activations carry local text, not whether they carry the knowledge the auditing tasks ask for. The authors note that their datasets "remain relatively small and limited in scope," and that they are "particularly interested in self-supervised objectives that" could scale, which they did not test here.[^c12][^c13] Whether prediction of nearby text transfers to the out-of-distribution knowledge in the auditing games is an empirical question the paper answers only through the full mixture (my reading).

## Related

- [[activation-oracle]] — the verbalizer this task is one training signal for.
- [[self-supervised-answer-model]] — also builds labels from unlabeled data, there from a model's own answers; here the labels are the corpus's adjacent tokens (my reading of the analogy).

[^c1]: arxiv-2512-15674 — "enabling unlimited training data generation from any text corpus"
[^c2]: arxiv-2512-15674 — "a 50-50 mix of pretraining and conversational data"
[^c3]: arxiv-2512-15674 — "The input and target tokens do not overlap"
[^c4]: arxiv-2512-15674 — "we run a controlled ablation on Qwen3-8B"
[^c5]: arxiv-2512-15674 — "partially disentangles these two factors"
[^c6]: arxiv-2512-15674 — "the truncated full mixture allocates 60% of its budget to the self-supervised context prediction"
[^c7]: arxiv-2512-15674 — "the truncated full mixture improves over the SPQA + Classification baseline on most evaluation metrics"
[^c8]: arxiv-2512-15674 — "increases the diversity of activation-verbalization signals"
[^c9]: arxiv-2512-15674 — "the full 1M-example mixture outperforms the truncated mixture"
[^c10]: arxiv-2512-15674 — "Both diversity and quantity of training data improve performance"
[^c11]: arxiv-2512-15674 — "diversity is model and task dependent"
[^c12]: arxiv-2512-15674 — "our datasets remain relatively small and limited in scope"
[^c13]: arxiv-2512-15674 — "We are particularly interested in self-supervised objectives that"
