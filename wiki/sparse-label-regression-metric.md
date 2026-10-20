---
description: "A metric can be composed from many candidate judge criteria by partial least squares on fewer than 100 human labels; the regression weights show which criteria carry the signal."
aliases: ["dynamic metric induction", "AutoMetrics", "regression-composed metric", "PLS-composed evaluator"]
sources: ["arxiv-2512-17267"]
---
# Sparse-label regression metric

An evaluator can be built rather than chosen. The mechanism, as AutoMetrics sets it out: a pool of candidate metrics, some generated as LLM-as-a-judge criteria for the task and some retrieved from an existing bank, is z-scored and combined by a regression fitted to a few human labels, so that the composite tracks the human signal.[^c1][^c2] The estimator is partial least squares. It "projects the metric space onto the direction most predictive of human labels, then regresses labels along that axis."[^c3] PLS is chosen for the shape of the problem: the number of metrics "may be comparable to or larger than the number of observations (data points)", and the metrics are often highly correlated.[^c4] (My inference: the paper states these two conditions; that ordinary least squares fails under them is the standard argument, which this paper does not measure.)

The fit runs in two stages. PLS on all candidates ranks them by the magnitude of their weights; the top n are kept and PLS is refit on that subset.[^c5] Generated metrics that correlate negatively with the human signal are then dropped, "as they are designed to target positive correlation."[^c6] The weights are part of the output: the report gives each metric's importance as a percentage "derived from regression coefficients", so the composite says which criteria carry the human signal and by how much.[^c7]

The candidate pool is what the method relies on. Generation is deliberately broad: "Broad coverage of evaluation criteria allows us to later filter down to what matters most."[^c8] The reported gain is against judges alone. With "fewer than 100 feedback points", Kendall correlation with human ratings rises by up to 33.4%; on EvalGen the paper states that AutoMetrics "improves performance by 33.4% over the closest baseline (LLM Judge)".[^c9][^c10] A sweep over training sizes from N=5 up to 640 found that "only ∼80 feedback points suffice for moderate correlation".[^c11][^c12] The construct test reports sensitivity to degraded outputs "in 81.0-97.8% of cases, depending on the dataset, which is significantly greater than the 50% baseline".[^c13]

## Limits

- The composite generalizes only as far as its labels do: "AutoMetrics may only generalize as far as the provided data enables it."[^c14] The paper's own remedy is to collect representative human data, not to fit fewer weights.
- Many predictors on few points is a known hazard: the paper names it "a high-P low-N regression problem that risks spurious correlations."[^c15] Its guard is a warning in the metric report when the correlation with human judgments has p > 0.05. That flags the problem; it does not remove it.
- The fitted metric is tied to the model that generated it: "producing metrics with one model and running them with another reduces performance."[^c16] A metric fitted with one judge does not carry over to another judge for free.
- Synthetic data can mislead the fit: scaling it "can produce metrics that reflect dataset artifacts rather than system quality", and "domain experts can help remove spuriously correlated metrics which" the automatic filter misses.[^c17][^c18]
- Kendall's τ "checks whether the rank order induced by a metric matches that of human judgments."[^c19] It validates ordering, not the calibrated level of a score.
- The sensitivity and stability tests are the paper's own construction. "Sensitivity measures whether a metric assigns lower scores to degraded outputs"[^c20] is a test designed by the authors, not an external standard.
- The paper "do[es] not conduct a formal user study to demonstrate the adoption" of the method.[^c21] Its evidence is five or six benchmark tasks; the claim that a few dozen labels suffice for a new task is an extrapolation from those (my inference).

## Related

- [[llm-judge-validation-gap]] — a composite built on judges inherits whatever per-criterion validation those judges lack
- [[llm-judge-biases]] — the biases a generated criterion may carry; the regression weights them but does not remove them
- [[three-test-metric-validity-audit]] — another validity audit of metrics, by perturbation and expert agreement
- [[dispersion-redundancy-criterion-weights]] — rubric weights fitted by a least-squares rule, from a different source than human labels
- [[version-dependent-judge-error]] — why a judge fitted to one version may misjudge another

[^c1]: arxiv-2512-17267 — "The filtered pool of candidate metrics must still be combined into a predictive signal for human judgment."
[^c2]: arxiv-2512-17267 — "We normalize all metric scores to their z-scores and fit a Partial Least Squares"
[^c3]: arxiv-2512-17267 — "PLS projects the metric space onto the direction most predictive of human labels"
[^c4]: arxiv-2512-17267 — "comparable to or larger than the number of observations (data points)"
[^c5]: arxiv-2512-17267 — "In the first stage, we fit PLS using all candidate metrics and"
[^c6]: arxiv-2512-17267 — "as they are designed to target positive correlation."
[^c7]: arxiv-2512-17267 — "metric derived from regression coefficients."
[^c8]: arxiv-2512-17267 — "Broad coverage of evaluation criteria allows us to later filter down to what matters most."
[^c9]: arxiv-2512-17267 — "while requiring fewer than 100 feedback points"
[^c10]: arxiv-2512-17267 — "improves performance by 33.4% over the closest baseline (LLM Judge)"
[^c11]: arxiv-2512-17267 — "We vary the train set size from N=5, 10, 20, 40, 80, 160"
[^c12]: arxiv-2512-17267 — "only ∼80 feedback points suffice for moderate correlation"
[^c13]: arxiv-2512-17267 — "in 81.0-97.8% of cases, depending on the dataset, which is significantly greater than the 50%"
[^c14]: arxiv-2512-17267 — "AutoMetrics may only generalize as far as the provided data enables it."
[^c15]: arxiv-2512-17267 — "a high-P low-N regression problem that risks spurious correlations"
[^c16]: arxiv-2512-17267 — "that producing metrics with one model and running them with another reduces performance."
[^c17]: arxiv-2512-17267 — "can produce metrics that reflect dataset artifacts rather than system quality"
[^c18]: arxiv-2512-17267 — "domain experts can help remove spuriously correlated metrics which"
[^c19]: arxiv-2512-17267 — "checks whether the rank order induced by a metric matches that of human judgments."
[^c20]: arxiv-2512-17267 — "Sensitivity measures whether a metric assigns lower scores to degraded outputs."
[^c21]: arxiv-2512-17267 — "we do not conduct a formal user study to demonstrate the adoption"
