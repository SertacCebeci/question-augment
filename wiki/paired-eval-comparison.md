---
description: "Comparing two models on the same questions cancels the data noise they share, because their per-question scores are correlated; the paired variance is what a significance test should use."
aliases: ["paired analysis", "paired test on shared questions", "paired variance", "all-pairs paired method", "paired standard error"]
sources: ["arxiv-2512-21326"]
---
# Paired comparison on shared questions

Two models scored on one question set are not two independent samples. For the difference A − B, the paired variance is Var[A] + Var[B] − 2Cov[A(x), B(x)], and the covariance term is what pairing buys. The paper states the condition: "are correlated when the same question is used to evaluate both."[^c1] The mechanism is that much of each model's data noise is question difficulty, and the two models share the same questions and so the same difficulty. When both find the same items hard, that shared part cancels from the difference. The paper puts it as "The paired method makes use of prediction differences on the same question to gain more information."[^c2]

An unpaired test throws this away. It treats the two means as if they came from different question sets, so each mean carries its own question-pool term into the difference. The paper's toy example makes the contrast concrete: an unpaired comparison of two exams with "different questions drawn from the same distribution" can reflect only which exam was easier, while on one shared exam "the same 10% difference is more significant."[^c3] Pairing is free in the sense that no new items or runs are needed, only the per-question scores that were already produced.

The paper's claim is that for LLMs the correlation is large: "similar models do similarly on each question, so greatly reduced data noise is possible only with the paired analysis."[^c4] Pairing also combines with averaging. The paper reports that this "combination is 3-6 times and 4 times more powerful" than the unpaired single-prediction analysis in its two worked examples.[^c5]

The all-pairs method applies the paired analysis to every pair in a table of results, so that one set of pairwise measurements gives a noise rule for the whole table. The paper's finding for correctness evals is that "the paired test usually gives a total paired variance similar to the basic variance predicted by the accuracy."[^c6] Concretely, the variance of a difference is about the single-model Bernoulli variance p(1 − p) at the models' accuracy p, which is a rule that needs only the reported accuracy. The reason, in the paper's Beta model, is that the distribution of question-level expected accuracies "fits the empirical distribution of question-level expected accuracies well."[^c7] The rule follows when prediction noise dominates: "When the prediction noise is much greater than the data noise, then total" noise is approximately the prediction noise.[^c8]

The method also rules out a tempting shortcut. Leaderboards that drew per-model error bars from a bootstrap against one fixed reference model were using the wrong object; the paper says that approach "allowed them to obtain per-model confidence intervals but is incorrect."[^c9] In general, "it's not in general possible to have one error bar per model" under the paired method. For the total noise of LLM evals the paper reports the opposite in practice: "at least for the total noise of LLM evals, this work shows that there is almost no such surprises, thus we can compute meaningful error bars."[^c10] The paper also notes that the unpaired standard errors in a major model report "are just a simple function of the accuracy," so they add no information beyond the accuracy.[^c11]

## Limits

- Pairing helps only as far as per-question scores correlate. The paper attributes the correlation to shared training data and methods, and it presents this as a guess: "We speculate that the uniformity of these results comes from the relative similarity among LLMs training on similar data using similar methods."[^c12] A pair of systems built very differently may correlate less, and the gain shrinks with it. My inference, not tested in the paper.
- The total-noise rule has known exceptions. On "guessable evals such as MMLU, when the performance is near random chance," the observed noise departs from the Beta prediction.[^c13] The paper also reports that the total noise still follows the prediction "except for chain-of-thought predictions."[^c14]
- The paper itself says the test of its main claim is incomplete: "More data is needed to further test if this continues to hold," where the data noise exceeds the prediction noise at low temperature.[^c15]
- Pairing needs shared questions. A score reported on a different question set cannot be paired after the fact, and the paper's own illustration is two exams with different questions.[^c3] Published unpaired numbers can be checked only against the accuracy-based rule, not against a paired test.
- Pairing removes the shared question-pool term from a difference, but not the prediction term. Averaging is the remedy for that part, and the two gains are separate. See [[prediction-data-noise-decomposition]].

## Related

- [[prediction-data-noise-decomposition]] — the split this comparison works on: pairing removes the shared data term from a difference, averaging removes the prediction term.
- [[minimum-detectable-effect]] — the paired variance is the input that sets how small a shared-question difference a design can resolve.
- [[run-to-run-spread]] — the same warning against crediting a single-run gap, here applied to the question level rather than to the run level (my reading).

[^c1]: arxiv-2512-21326 — "are correlated when the same question is used to evaluate both"
[^c2]: arxiv-2512-21326 — "The paired method makes use of prediction differences on the same question to gain more information."
[^c3]: arxiv-2512-21326 — "where each exam contains different questions drawn from the same distribution."
[^c4]: arxiv-2512-21326 — "similar models do similarly on each question, so greatly reduced data noise is possible only with the paired analysis."
[^c5]: arxiv-2512-21326 — "This combination is 3-6 times and 4 times more powerful in Example 1 and Example 2b."
[^c6]: arxiv-2512-21326 — "the paired test usually gives a total paired variance similar to the basic variance predicted by the accuracy"
[^c7]: arxiv-2512-21326 — "fits the empirical distribution of question-level expected accuracies well"
[^c8]: arxiv-2512-21326 — "When the prediction noise is much greater than the data noise, then total"
[^c9]: arxiv-2512-21326 — "which allowed them to obtain per-model confidence intervals but is incorrect"
[^c10]: arxiv-2512-21326 — "at least for the total noise of LLM evals, this work shows that there is almost no such surprises, thus we can compute meaningful error bars."
[^c11]: arxiv-2512-21326 — "they are just a simple function of the accuracy"
[^c12]: arxiv-2512-21326 — "We speculate that the uniformity of these results comes from the relative similarity among LLMs training on similar data using similar methods."
[^c13]: arxiv-2512-21326 — "On guessable evals such as MMLU, when the performance is near random chance"
[^c14]: arxiv-2512-21326 — "except for chain-of-thought predictions"
[^c15]: arxiv-2512-21326 — "More data is needed to further test if this continues to hold"
