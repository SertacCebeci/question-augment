---
description: "Scoring a free-form forecast by the probability given to its one named answer: a correct answer earns 1-(q-1)^2, a wrong one -q^2, a proper rule that rewards truthful confidence."
aliases: ["Brier score for free-form responses", "multi-class Brier score for short answers", "Damani-style Brier reward", "open-ended Brier reward"]
sources: ["arxiv-2512-25070"]
---
# Free-form Brier score

A forecast in this setting is a short answer y and a probability q that y is the true outcome. The question is open: the answer is a name or a place, not a pick from a fixed list. The paper adapts "the multi-class Brier scoring rule" to such responses.[^c1] A correct answer at confidence q earns 1 − (q − 1)², and an incorrect one earns −q².[^c2] Equivalently, the reward is −q² + 1[correct]·2q; that expansion is my algebra, checked against the paper's own reward line.

Correctness is not string equality. A language model tests "for semantic equivalence", so that a full name and its short form count as the same answer.[^c3]

## Mechanism

The score is built so that confidence has to be earned. With q = 0 the score is 0 whatever the answer, so a model that declines to commit gains nothing. Confidence on a correct answer pays, confidence on a wrong answer costs, and the cost grows with q. The paper says the score matches the reward used by Damani et al. (2025), and that it is a proper scoring rule, "incentivizing both high accuracy and truthful reporting of probability" on the answer the model thinks most likely.[^c4] The proper-scoring property is cited to Section A of the paper and I did not check that derivation in the extract read here.

The paper's ablation shows why the Brier term needs company. Training on accuracy alone "leads to negative brier scores", worse than a constant baseline of 0.[^c5] Training on the Brier score alone raises accuracy less, and the Brier-only model answers "Unknown" with near-zero confidence on many items, "due to low reward for correct yet low-confidence guesses, which hurts exploration".[^c6] The paper therefore trains on accuracy plus the Brier score, and reports that this combination "leads to the best performance on both metrics" on its validation set.[^c7] The reasoning is that on a hard question a low-confidence guess that turns out right still gets a large reward from the accuracy term, while the Brier term keeps the confidence honest.

## Limits

- Measured on Qwen3 thinking models (4B and 8B) with one validation set of 207 questions. The reward comparison was made on validation, not on the held-out test set, which the authors say they did not look at until the end.
- Grading is by a model judge. The paper reports two judges agreeing on about 97 percent of responses and says "manual validation ensures they are accurate" on most cases.[^c8] The score inherits judge error, and the judge-error rate on the Brier term is not separated out.
- The score rates one named answer and the confidence on it. It does not score a spread of probability over alternatives. This is my inference from the formula, not something the paper tests.
- It covers short answers only. The paper says "We also do not consider long-form forecasts", because it is unclear how to grade them.[^c9]
- For binary questions the paper uses the Brier score alone, so the composite is specific to free-form data. See [[delayed-outcome-brier-reward]] for the binary-outcome Brier reward applied to a live agent.

## Related

- [[delayed-outcome-brier-reward]] — the same negative-Brier reward on yes/no events, backfilled after resolution; the free-form version here adds an answer-matching term
- [[calibration]] — what a calibrated probability is and how calibration is measured; the Brier score mixes calibration with discrimination
- [[news-synthesized-forecasting-questions]] — where the questions scored by this rule come from
- [[answer-string-leakage]] — why the answer must not appear in the question, or the confidence term is trivially earned

[^c1]: arxiv-2512-25070 — "We adapt the multi-class Brier scoring rule"
[^c2]: arxiv-2512-25070 — "Predicting an event with a probability q = 0 returns a baseline score of 0"
[^c3]: arxiv-2512-25070 — "using another language model to test for semantic equivalence"
[^c4]: arxiv-2512-25070 — "incentivizing both high accuracy and truthful reporting of probability"
[^c5]: arxiv-2512-25070 — "leads to negative brier scores"
[^c6]: arxiv-2512-25070 — "due to low reward for correct yet low-confidence guesses"
[^c7]: arxiv-2512-25070 — "leads to the best performance on both metrics"
[^c8]: arxiv-2512-25070 — "manual validation ensures they are accurate"
[^c9]: arxiv-2512-25070 — "We also do not consider long-form forecasts"
