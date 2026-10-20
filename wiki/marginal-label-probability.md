---
description: "A generative classifier's confidence in a label is the total probability of all output sequences containing it, summed over paths rather than read at one token or one string."
aliases: ["marginal probability", "marginal probability of a label", "token-level marginalization", "path-summed label probability"]
sources: ["arxiv-2511-22312"]
---
# Marginal label probability

A generative classifier returns text, not a score per class. Asked whether a message falls under "S1" or "S3", a model writes "unsafe" followed by label names, and nothing in that output is a probability for either label. The mechanism here recovers one by summing over output strings. The probability of a label is the sum of the probabilities of every output sequence that contains it, "considering all possible sequences containing that label, given an input X".[^m1] A sequence's probability is the product of its token probabilities, each conditioned on the input and the tokens before it.[^m1b] The paper keeps this apart from two cheaper readings of the same softmax values: "The distinction between conditional, joint, and marginal probabilities is crucial".[^m2]

The first reading is conditional probability. It is the probability of a label token at one generation step, taken directly from that step's softmax, and it "computes the likelihood of a label" at the point where it appears.[^m3] The second is joint probability, the chain product of token probabilities up to a position, which in practice scores a whole label string: "Joint probability assesses the confidence of the entire predicted label string."[^m4] The marginal reading differs in what it counts. It attempts to capture "overall likelihood of a label independent of its exact position or co-occurrence with other specific" tokens in the output.[^m5] A label reached through many surface forms gets the mass of all of them.

The sum is the hard part. Taken over every sequence, it is intractable: "this formulation is computationally intractable due to the exponential size of" the set of sequences that include the label.[^m6] The method therefore approximates it with a depth-first search from the input, titled "Compute Marginal Probability of Label via Beam-like DFS with Max Token Cutoff".[^m7] The search follows the most probable next tokens at each step, caps the generation depth, and stops at an end-of-sequence token. Whenever a continuation ends with a label, the accumulated path probability is added to that label's total. The authors summarise the trade as follows: "This approximation balances tractability with fidelity".[^m8]

For labels that span several tokens, the paper does not sum over the label's pieces. It takes a proxy: when "S1" is tokenised as 'S' and '1', the probability of the final token "is used as a proxy for the label" in the per-token reading.[^m9]

What was measured. On LLaMA Guard, across a synthetic multi-label set and the BeaverTails benchmark, the authors report that marginal probability "provides the most robust and accurate" confidence scores of the three estimators they propose and of the uncertainty baselines they compare with, crediting "its ability to aggregate probabilities across multiple paths".[^m10] The same reading was applied to LLaMA 3.1-8B-Instruct, a model not tuned for safety, and beat plain greedy decoding in their table, "even without explicit safety fine-tuning".[^m11] The motivation is that the generative architecture "lacks direct class-level probabilities, which hinders model confidence assessment and performance interpretation", and that this "complicates the setting of dynamic thresholds for content moderation".[^m12][^m13]

What transfers. The formal object, a probability over output strings reduced to a probability over a fixed label set, is not specific to safety. For someone answering a question, my inference (not the paper's) is that an answer reached through many surface phrasings carries more mass than any one phrasing of it, so the single most likely string is a poor measure of how firmly the model holds that answer. Whether this carries to open-ended answers is not tested here: the reduction presupposes a closed, enumerable label set, which the paper has and most questions do not.

## Limits

- The paper's metrics are "F1-score and AUCROC".[^m14] The authors say that leveraging logits "significantly improves the interpretability and reliability of generative classifiers";[^m15] but the sections read contain no calibration measure. Whether a marginal of 0.8 means the label is right about 80 % of the time is not shown. That is my reading of what is missing, not a claim the paper makes.
- The evaluation is on synthetic data: "evaluations were performed on synthetic" sets, which the authors themselves say may not reflect the ambiguity of real harmful content.[^m16]
- The marginal is approximate: the authors say it "is approximate and does not explore the full space of" generation paths.[^m17] Because the search sums only the paths it visits, my inference is that the estimate is biased low, and that the size of the bias depends on the cut-offs. The paper lists how decoding choices affect robustness as future work.
- Cost: "the marginal probability method incurs" token-level overhead from multiple path explorations, which the authors say may hinder real-time use.[^m18]
- The comparison is narrow: greedy decoding and a few uncertainty estimators, on a single model family plus one additional model.
- Transfer to question answering or to agents' own answers is not tested in this work.

## Related

- [[answer-label-confidence-filter]] — the same kind of label probability, read at one next-token step over option labels; the marginal instead adds up every path that ends in the label.
- [[logit-magnitude]] — records the argument that softmax normalisation "may discard the absolute strength" of the model's evidence; the marginal reading is built on softmax probabilities and so inherits that question (my inference).
- [[generative-likelihood-evaluation]] — uses the same sequence probability, but to score one text against a source, not to sum over a class of texts.
- [[calibration]] — the property a "reliable" confidence would need; the paper's measures do not test it.
- [[token-regeneration-probability-confidence]] — a token-probability signal as a model's confidence in its own answer; not compared with the marginal reading in this paper.

[^m1]: arxiv-2511-22312 — "considering all possible sequences containing that label, given an input X"
[^m1b]: arxiv-2511-22312 — "The joint probability of each sequence"
[^m2]: arxiv-2511-22312 — "The distinction between conditional, joint, and"
[^m3]: arxiv-2511-22312 — "This approach computes the likelihood of a label"
[^m4]: arxiv-2511-22312 — "Joint probability assesses the confidence of the entire predicted label string."
[^m5]: arxiv-2511-22312 — "overall likelihood of a label independent of its exact position or co-occurrence with other specific"
[^m6]: arxiv-2511-22312 — "this formulation is computationally intractable due to the exponential size of"
[^m7]: arxiv-2511-22312 — "Compute Marginal Probability of Label via Beam-like DFS with Max Token Cutoff"
[^m8]: arxiv-2511-22312 — "This approximation balances tractability with fidelity"
[^m9]: arxiv-2511-22312 — "is used as a proxy for the label"
[^m10]: arxiv-2511-22312 — "its ability to aggregate probabilities across multiple paths, provides the most robust and accurate"
[^m11]: arxiv-2511-22312 — "even without explicit safety fine-tuning"
[^m12]: arxiv-2511-22312 — "lacks direct class-level probabilities, which hinders model confidence assessment and performance interpretation"
[^m13]: arxiv-2511-22312 — "This limitation complicates the setting of dynamic thresholds for content moderation"
[^m14]: arxiv-2511-22312 — "metrics for multi-label classification: F1-score and AUCROC"
[^m15]: arxiv-2511-22312 — "significantly improves the interpretability and reliability of generative classifiers"
[^m16]: arxiv-2511-22312 — "evaluations were performed on synthetic"
[^m17]: arxiv-2511-22312 — "approximate and does not explore the full space of"
[^m18]: arxiv-2511-22312 — "the marginal probability method incurs"
