---
description: "A cheap classifier's conformal set of labels can replace the full label list shown to an LLM, order the examples by confidence, and skip the LLM when the set holds a single label."
aliases: ["conformal in-context learning", "CICLe", "conformal label-set prompting", "conformal shortlist prompting"]
sources: ["arxiv-2512-05732"]
---
# Conformal candidate prompting

A cheap classifier can decide what an expensive language model is shown. The
base classifier gives a probability for each class, and conformal prediction
turns those probabilities into a set of candidate classes built to contain the
true label with a chosen confidence.[^c1] The language model is not asked to
choose from the whole label space. In the paper's design it is prompted with
the candidate classes and a few labeled examples for each, so the prompt is
shorter and the choice narrower.[^c2][^c3]

The ordering of the examples carries information too. The labeled examples are
presented "ordered from most to least probable according to the base
classifier's confidence scores", so the classes the base model favours appear
first.[^c4] The authors say this implicitly communicates which classes are most
relevant, without listing them. That is a way of stating a ranking inside a
prompt that otherwise carries only labels and examples.

The set can also decide that the language model is not needed. When the
conformal set contains only one class, the system "bypasses the LLM entirely
and outputs the base" classifier's prediction.[^c5] The authors read this as
the source of a cost saving: "This hybrid mechanism not only reduces the
computational cost of" prompting, and also balances the two models' strengths.[^c6]

The measured effects are reported on four benchmarks (AG News, DBpedia14,
Yahoo Answers Topics, GoEmotions) with LLaMA-3.1 at 8B and 70B. The abstract
says CICLe "reduces the number of shots and prompt length by up to 34.45% and
25.16%", a best-case figure for those settings.[^c7] Accuracy is conditional on
data: CICLe improves over its base classifier and beats few-shot prompting when
the base classifier has enough training data, and "performs comparably in low
data regimes."[^c8] The paper also reports that the method is "particularly
advantageous" under heavy class imbalance, which is the case where a linear
base classifier is weakest.[^c9]

What survives the move from statistics to prompting, in my reading: the set is
a calibrated shortlist, and its size is set by the classifier's uncertainty,
not by the number of classes. What does not survive by default is the coverage
claim. Coverage is a property of the set, and the set is used here to decide
what the model sees. If the true label falls outside the set, the language
model never has the chance to name it.

## Limits

- The set is only as good as the base classifier. The paper says linear models
  are "known to degrade in low-data regimes and under" strong class imbalance,[^c10]
  which are the regimes where the gain is claimed. In low data the paper reports
  parity with few-shot prompting, not a gain.[^c8]
- The main experiments fix the miscoverage level: "Unless otherwise specified,
  all experiments use" α = 0.05.[^c11] The part of the text I read does not
  report a sweep over α, so the trade-off between set size and coverage at other
  levels is not shown.
- Coverage of the sets on the test data is not reported in the part I read
  (the text was read to its results section, not beyond). The guarantee is
  marginal, and a single-class set that is wrong is returned without any check
  from the language model. How often that happens is my question, not a figure
  from the paper.
- One base classifier (TF-IDF with logistic regression), two LLM sizes of one
  family, and four English benchmarks. Other base classifiers and other model
  families are not tested in the text I read.
- The paper frames the work as classification with fixed labels. Open-ended
  answers, where the candidate list does not exist in advance, are outside what
  it measures.

## Related

- [[conformal-prediction]] — the set construction used here; this note changes what the set is used for, a prompt rather than a yes-or-no decision
- [[candidate-set-restriction-conformal-prediction]] — the same restriction of a conformal candidate space, over vocabulary tokens rather than classes; the validity condition there, that the truth lies in the restricted set, applies here too
- [[knowno]] — a conformal set from an LLM planner, used to decide when to ask a human instead of what to show a model
- [[expert-shortlist-correction]] — a top-k shortlist from an expert handed to a generalist; no calibrated set, and its ceiling is the shortlist's recall
- [[active-in-context-learning]] — a cheap proxy shortlists before an expensive scorer, by entropy rather than by a calibrated set

[^c1]: arxiv-2512-05732 — "candidate classes that includes the true label with"
[^c2]: arxiv-2512-05732 — "The LLM is prompted only with these"
[^c3]: arxiv-2512-05732 — "candidate classes and with k = 2 few-shot examples from each, thereby reducing the context length"
[^c4]: arxiv-2512-05732 — "examples ordered from most to least probable according to the base"
[^c5]: arxiv-2512-05732 — "bypasses the LLM entirely and outputs the base"
[^c6]: arxiv-2512-05732 — "This hybrid mechanism not only reduces the computational cost of"
[^c7]: arxiv-2512-05732 — "reduces the number of shots and prompt length by up to 34.45% and 25.16%"
[^c8]: arxiv-2512-05732 — "performs comparably in low data regimes"
[^c9]: arxiv-2512-05732 — "for text classification tasks with high class imbalance"
[^c10]: arxiv-2512-05732 — "known to degrade in low-data regimes and under"
[^c11]: arxiv-2512-05732 — "Unless otherwise specified, all experiments use"
