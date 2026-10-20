---
description: "Errors of an LLM scorer can peak at the partial-credit middle of the scale rather than at the extremes, an inverted-U that a single agreement figure hides."
aliases: ["inverted-U error pattern", "partial-credit error peak", "stratified scoring error", "score-level error profile"]
sources: ["doi-10-35377-saucis-1835608"]
---
# Intermediate-score error peak

An automated scorer's error is not one number spread evenly over the scale. Split it by the expert score and it can take a shape. A Turkish study of GPT, LLaMA, Gemini and Gemma scoring physics short answers ran "a stratified error analysis (calculating MAE for each score level)" to see how error changes with the true score.[^c1] For most models on the four-level item Q2 the shape was an inverted U, with error rates highest in the middle. The authors put it this way: "error rates tended to peak at the partial credit level (Score 2) rather than at the score boundaries."[^c2] The abstract states the same finding as higher reliability at the extremes, with the models struggling "with evaluating partial knowledge (intermediate scores)."[^c3]

The prompt condition changed how visible the peak was. Relative to zero-shot scoring, the one-shot example lowered error at Score 0 and Score 4, which "made the peak in errors at the partial credit level (Score 2) more distinct, resulting in a clear inverted-U pattern."[^c4] The peak still varied by model. LLaMA 3.1 8B and Gemini 2.0 Flash had the largest errors at Score 2, "with MAE values of approximately 1.40 and 1.15, respectively", while GPT-4.1 and Gemma 2 "flattened this curve, displaying lower error rates across the partial score range."[^c5][^c6]

The binary item Q1 did not show a middle peak. Its error sat in one class. Under zero-shot scoring, GPT-4o and LLaMA 3 70B "exhibited high error rates for correct answers (Score 1)"[^c7], while LLaMA 3.1 8B "showed a high error rate for incorrect answers (Score 0)".[^c8] The level at which a scorer fails depends on the item, so the shape belongs to the multi-level item and is not a general law of scoring.

The study does not say why the middle is hard. One reading, which is mine and untested here: a partial-credit band is defined by conditions a response only partly meets, and the scorer has to decide how many of them hold. At the extremes the decision is closer to all-or-nothing. The Q2 rubric does rely on conditional logic, since it "incorporates conditional logic based on specific physics concepts" to separate partial scores from full mastery.[^c9]

## Limits

- The evidence is two physics questions from one course. The authors say the dataset "is limited to two specific questions in undergraduate physics", and that their findings "may not be directly generalizable to other domains".[^c10]
- The middle peak rests on small cells. Q2 has 145 responses, and the table gives its score distribution as "71 / 6 / 8 / 24 / 36" for scores 0 to 4, so Score 2 has eight responses.[^c11] A peak in MAE over eight answers is a weak estimate, and the sections read give no interval for it.
- "The majority of models" is not all models. The authors note distinct outliers at the extremes, such as GPT-3.5 at Score 4.
- The expert scores are the only reference. The authors "utilized the single set of expert scores provided in the published benchmark dataset" as ground truth, so a stratum's error includes whatever noise that set carries.[^c12]
- The cause of the peak is not tested. The paper reports where error sits, not what makes the middle harder.

## Related

- [[reducible-context-gap-disagreement]] — an inverted U in judge disagreement against completion quality; the same middle-peak shape on a different axis
- [[error-direction-versus-magnitude]] — the sign of error across models; this note adds the score level at which error sits
- [[exact-match-versus-weighted-agreement]] — how the same middle errors look under exact-match accuracy and under a distance-weighted statistic

[^c1]: doi-10-35377-saucis-1835608 — "a stratified error analysis (calculating MAE for each score level) was conducted"
[^c2]: doi-10-35377-saucis-1835608 — "error rates tended to peak at the partial credit level (Score 2) rather than at the score boundaries"
[^c3]: doi-10-35377-saucis-1835608 — "with evaluating partial knowledge (intermediate scores)"
[^c4]: doi-10-35377-saucis-1835608 — "made the peak in errors at the partial credit level (Score 2) more distinct, resulting in a clear inverted-U pattern"
[^c5]: doi-10-35377-saucis-1835608 — "recorded the highest errors at this level, with MAE values of approximately 1.40 and 1.15, respectively"
[^c6]: doi-10-35377-saucis-1835608 — "flattened this curve, displaying lower error rates across the partial score range"
[^c7]: doi-10-35377-saucis-1835608 — "exhibited high error rates for correct answers (Score 1), with MAE values of approximately 0.80 and 0.47, respectively"
[^c8]: doi-10-35377-saucis-1835608 — "showed a high error rate for incorrect answers (Score 0), with an MAE exceeding 0.57"
[^c9]: doi-10-35377-saucis-1835608 — "incorporates conditional logic based on specific physics concepts"
[^c10]: doi-10-35377-saucis-1835608 — "the dataset is limited to two specific questions in undergraduate physics"
[^c11]: doi-10-35377-saucis-1835608 — "71 / 6 / 8 / 24 / 36"
[^c12]: doi-10-35377-saucis-1835608 — "we utilized the single set of expert scores provided in the published benchmark dataset"
