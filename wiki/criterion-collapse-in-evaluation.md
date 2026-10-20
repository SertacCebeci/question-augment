---
description: "Readers asked to score several separate criteria of a language model's answer merge them into one overall impression, so the score tracks feeling and the criteria stop being separate measurements."
aliases: ["criteria collapse", "criteria distortion", "global impression scoring", "dimension confusion"]
sources: ["arxiv-2512-16750"]
---
# Criterion collapse in evaluation

A rubric can list several criteria, and the scores a reader gives do not stay separate. The study reports that "Evaluators often confuse different criteria, making it challenging to quantitatively assess chatbot performance."[^d1] Its abstract puts the same point as "human judgement collapses analytical distinctions into intuitive heuristics shaped by form and fluency."[^d2]

**Mechanism.** The authors mapped how each original criterion was reinterpreted by the evaluators in the first two rounds (their Table 2). One of the entries is "Relevance being confused with Agreement or Consistency."[^d3] The general pattern is compression: "Evaluators collapsed criteria through intuition."[^d4] "In practice evaluators compressed them into a handful of global impressions"[^d5], and the score follows the impression: the final score is driven by an overall feeling "rather than by systematic application of the individual criterion."[^d6]

Removing the labels did not remove the merging. In the second round the criteria columns were taken off the form, "dimensions and criteria columns were removed from the evaluation form, retaining only the questions about them".[^d10] The authors still found that "Although the criteria in R2 are provided only as questions, confusion between dimensions persisted."[^d7]

The same score can also hide different reasons. In the third round, "each evaluator provided a different point of view for the same score"[^d8], even when all of them gave the same rating.

What this adds (my inference): a single number from a multi-criterion instrument is not the sum of separate judgments. It is one global judgment with the criteria's names attached. Any per-criterion figure then describes what the reader felt, and a reader who cannot separate groundedness from fluency will report a single figure for both. The study does not show that this holds beyond its evaluators.

## Limits

- The mapping in Table 2 is the analysts' reading of the scores and comments. In the part of the text I read, the paper reports no agreement statistic for it.
- The instrument changed between rounds. "This option was used in the first and second rounds, whereas in the third round a binary scale (Yes/No)" was used.[^d9] The collapse persisted across a Likert scale and a binary one, but these are different instruments compared across months, not a controlled comparison.
- Three evaluators is a small group, and the study reports individual differences in how they read the same criterion. The statements about "evaluators" as a group rest on those three people.
- The study does not test a remedy. Whether separate scoring passes, training or a different order of criteria would reduce the merging is not reported (my inference from the text read).

## Related

- [[rater-effects-latent-score-model]] — models rater strictness and consistency as stable parameters; criterion collapse is a change in what a rater measures, which such a model does not see.
- [[plausibility-masks-error]] — the same reader, with fluency as the criterion that absorbs the others.
- [[llm-judge-biases]] — an automated judge's preferences are another source of one score overriding separate criteria.

[^d1]: arxiv-2512-16750 — "Evaluators often confuse different criteria, making it challenging to quantitatively assess chatbot performance"
[^d2]: arxiv-2512-16750 — "human judgement collapses analytical distinctions into intuitive heuristics shaped by form and fluency"
[^d3]: arxiv-2512-16750 — "Relevance being confused with Agreement or Consistency"
[^d4]: arxiv-2512-16750 — "Evaluators collapsed criteria through intuition."
[^d5]: arxiv-2512-16750 — "in practice evaluators compressed them into a handful of global impressions"
[^d6]: arxiv-2512-16750 — "rather than by systematic application of the individual criterion"
[^d7]: arxiv-2512-16750 — "Although the criteria in R2 are provided only as questions, confusion between dimensions persisted"
[^d8]: arxiv-2512-16750 — "each evaluator provided a different point of view for the same score"
[^d9]: arxiv-2512-16750 — "This option was used in the first and second rounds, whereas in the third round a binary scale (Yes/No)"
[^d10]: arxiv-2512-16750 — "dimensions and criteria columns were removed from the evaluation form, retaining only the questions about them"
