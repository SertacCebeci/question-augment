---
description: "Fit a surrogate that a prediction-powered estimate will correct by minimizing the variance of its residuals, not their mean squared error; a constant bias with no spread costs the estimator nothing."
aliases: ["residual variance objective", "variance-based fine-tuning loss", "rectification-aware fine-tuning objective"]
sources: ["arxiv-2511-19486"]
---
# Residual variance as a fine-tuning objective

A language model can stand in for a human outcome Y and be corrected afterwards. The correction is a [[calibrated-judge-estimator-efficiency-ordering|prediction-powered]] estimate: the model is treated as "a potentially biased black box"[^c1] and its errors are measured on a labelled sample. The question this note addresses is which quantity the model should be fitted to minimize when it is going to be corrected this way. The paper's answer is the variance of the residual, Var(Y − f(X)), where f is the fine-tuned predictor. The conventional answer, mean squared error, is a different quantity.

The reason lies in the variance of the estimator. The estimate averages the labelled residuals Y − f(X) and adds the model's average over a large unlabelled set. The text states that "Because we have a large unlabeled dataset, the second term is small when m is large."[^c2] What remains is the variance of the labelled residuals, so the model's job is to make that spread small.

The sharpest illustration is a predictor that always under-predicts by the same constant. Its mean squared error is the square of that constant, which may be large. Its residual variance is zero. The paper's wording: "bias can still be optimal for the prediction-powered estimator, provided that the bias is a constant".[^c3] My reading: the correction step removes a constant offset, so only the spread of the error reaches the final variance. My own identity, not the paper's: MSE equals residual variance plus the squared mean residual, so the two objectives differ exactly by the level of the error.

For mean estimation the two objectives coincide under one condition. When the model class allows an additive shift, "minimizing MSE implicitly also minimizes the residual variance."[^c4] The paper then says that outside that idealized case they "can behave differently in more practical settings where data is not" large enough, or where training uses mini-batches, regularization or early stopping.[^c5]

For general M-estimation the objectives are, in the paper's words, "generally not equivalent."[^c6] The reason it gives is that the residual "that governs downstream precision is weighted by each observation" by its influence on the estimand.[^c7] When that weight varies across observations, a shift of the surrogate changes the weighted residual by an amount that depends on the observation, so a free intercept no longer aligns MSE with the quantity that governs the estimator's precision.

The measured gain comes from one experiment: on the Wine Reviews mean-estimation task, replacing the MSE fine-tuning objective with the variance objective "brings 22% to 42% variance reduction across different data budget settings."[^c8] The comparison holds the rest of the two-stage procedure fixed.

Standard fine-tuning is the contrast. It typically minimizes next-token cross-entropy, and such an objective "is not tied to the downstream rectification stage at all."[^c9] Combining the labelled sample with cross-fitting does not remove the choice: the paper says cross-fitting "does not eliminate the need to choose a new fine-tuning objective."[^c10]

The paper places the idea beside the empirical efficiency maximization literature, saying its use of residual variance is "conceptually similar to the empirical efficiency maximization" line of work.[^c11] My reading, not the paper's wording: a nuisance model is scored by the variance of the estimator that uses it, rather than by its own prediction error. That much transfers beyond LLMs. The MSE–variance equivalence does not transfer automatically, because it depends on the estimand's weights, as the M-estimation case shows.

## Limits

- The gain is measured on one corpus for the mean and one regression. The 22% to 42% range belongs to that setup and its budgets; another model, prompt or dataset could give a different size or sign. The paper's appendix repeats checks on other datasets, which I did not read.
- The variance argument is asymptotic in the number of unlabelled samples. It says nothing about small-sample interval coverage, which the paper treats in a separate inference section I did not read.
- My inference, not tested in the text as I read it: the residual variance is itself estimated from the labelled sample. A flexible model tuned to minimize that estimated spread could overfit it. The cross-fitting discussion addresses sample splitting, and I did not check whether it covers this.
- The claim is about one fine-tuning procedure. Whether the variance objective keeps its advantage under other training losses is not shown in the sections I read.

## Related

- [[calibrated-judge-estimator-efficiency-ordering]] — the prediction-powered estimators whose variance this objective targets; that note's ordering is for a fixed predictor.
- [[fine-tune-rectify-label-split]] — how the labelled budget divides between fitting this objective and correcting with it.
- [[asymmetric-calibration-allocation]] — a different labelled-data split, between the two true-label classes of a judge's calibration set, not between fitting and correcting.

[^c1]: arxiv-2511-19486 — "while treating the prediction model as a potentially biased black box"
[^c2]: arxiv-2511-19486 — "the second term is small when m is large"
[^c3]: arxiv-2511-19486 — "bias can still be optimal for the prediction-powered estimator, provided that the bias is a constant"
[^c4]: arxiv-2511-19486 — "minimizing MSE implicitly also minimizes the residual variance"
[^c5]: arxiv-2511-19486 — "the two objectives can behave differently in more practical settings where data is not"
[^c6]: arxiv-2511-19486 — "the objectives are generally not equivalent"
[^c7]: arxiv-2511-19486 — "that governs downstream precision is weighted by each observation"
[^c8]: arxiv-2511-19486 — "brings 22% to 42% variance reduction across different data budget settings"
[^c9]: arxiv-2511-19486 — "is not tied to the downstream rectification stage at all"
[^c10]: arxiv-2511-19486 — "does not eliminate the need to choose a new fine-tuning objective"
[^c11]: arxiv-2511-19486 — "conceptually similar to the empirical efficiency maximization"
