---
description: "Using a model's predicted value as if it were the observed outcome shifts the estimand and drops prediction uncertainty, so inference is biased and too narrow even when predictions are accurate."
aliases: ["naive plug-in with predicted outcomes", "treating predictions as observed data", "single imputation of predicted outcomes", "inference with predicted data (IPD) naive analysis"]
sources: ["arxiv-2512-05456"]
---
# Predicted-outcome substitution

Scientists often lack the outcome they want to study. A pretrained model can supply a predicted value Ŷ in its place, and the naive analysis then runs the usual estimator on Ŷ as if it had been observed. The review that names this case locates the failure on two axes, bias and variance. Both appear "when predictions systematically shift the estimand or distort relationships" and when uncertainty is ignored.[^p1]

**Bias: the substitution changes the target.** The naive estimator aims at a functional of the predicted outcome, not of the true one, so the naive target and the scientific estimand differ. The review splits the total bias in two. "The first component, estimation bias, arises when" the naive estimator fails to estimate its own target. This happens because the prediction is itself a finite-sample estimate, and because the same data are often used to build the prediction and to test a difference between groups, which is the winner's curse.[^p2] The second part, estimator bias, is the one that survives unlimited data: "even with infinite data, the naive estimator converges to the" wrong quantity.[^p3] The reason given is that a predictor is fitted to approximate the outcome pointwise: "Predictive models are typically trained to approximate Y pointwise, rather than preserve its specific structure".[^p4] A predictor can therefore be accurate on average and still change the shape of the relationship between the outcome and the covariates that the downstream model reads. Using predicted outcomes as conditioning variables adds a further route, a collider bias, since "outcomes as conditioning variables can create a collider bias."[^p5]

Accuracy does not repair this. The abstract states the consequence directly: "accuracy does not guarantee valid downstream inference."[^p6]

**Variance: the substitution discards uncertainty.** The naive analysis treats the prediction as fixed, so it "ignores variability from both the prediction model" and from the true data-generating mechanism.[^p7] Two components are lost, the residual noise around the fitted function and the finite-sample error of the fitted function itself. Replacing the outcome with a predicted value is a single imputation, and single imputation "underestimates uncertainty about the underlying data generating mechanism."[^p8] The practical consequence is standard errors that are too small, "Ignoring this leads to underestimated standard errors and anticonservative inference."[^p9]

**What a small case shows.** The review illustrates both failures with a stylized linear design: ten standard normal predictors and an outcome that is their sum plus noise, with "the inferential goal is the marginal slope of Z1 on Y".[^p10] Four random forests, trained on an independent sample, produce four predicted outcomes, and each is regressed on Z1. A rule that excludes Z1 gives a slope near zero, "the estimated slope is near zero despite high overall predictive fit."[^p11] A rule that includes Z1 recovers the slope, but "the residual variance is badly underestimated, producing anticonservative intervals."[^p12] The point the authors draw is that "Predictive accuracy can be high in all four cases," and the inferential behaviour still differs.[^p13] A second case, estimating turnout by race from predicted race in voter files, shows the same pattern: the two-step pipeline can "alter the association structure (bias), as well as omit uncertainty from the prediction step."[^p14]

**Not every substitution fails.** The review grants that "there are cases where predicted data can improve precision."[^p15] The gain is conditional: "efficiency gains, however, are conditional and fail when the residual correlation is weak."[^p16] When the parameter does not depend on the marginal distribution of the covariates, "no amount of additional predicted data can add information."[^p17]

**The remedy the review points to.** The natural repair uses a small labelled set: "A natural solution leverages a small labeled set with gold-standard" outcomes to calibrate the inference on the large predicted sample.[^p18] The calibrated estimators, and how they order by efficiency, are in [[calibrated-judge-estimator-efficiency-ordering]]. Those estimators correct the naive mean of a judge's scores; the same substitution is what they repair.

## Limits

- The review is a survey with illustrations, not a set of theorems with proofs given in the body. The stylized and voter-turnout examples are simulations. The analytic biases and standard errors for the stylized case are in its Appendix A, which was not read here.
- The split into estimation bias and estimator bias is the review's bookkeeping. The sections read do not show that the two parts can be measured separately in a real analysis.
- The claim that estimation bias shrinks with more data is a tendency, not a guarantee: it shrinks "as training data grow larger and more representative," and "in small or moderate samples, or in settings of heterogeneity," the review warns of a "no free lunch" trade-off.[^p19][^p20]
- The review cites a count of fifty scientific settings where predicted data enter analyses. That table was not read here, so the prevalence of the substitution is not measured in this note.
- The collider mechanism is attributed to Ogburn et al. (2021) and is not reproduced here.
- Whether the variance failure is worse for the heavy-tailed, heteroskedastic errors that modern predictors produce is raised by the review and not measured in the sections read.

## Related

- [[calibrated-judge-estimator-efficiency-ordering]] — the calibrated estimators that correct the naive judge mean; this note states the failure, that one orders the fixes by efficiency.
- [[simulated-respondent-variance-deficit]] — another case where a model stands in for observed data and the spread is lost. The mechanism there is not tested, and the link is my inference.

[^p1]: arxiv-2512-05456 — "when predictions systematically shift the estimand or distort relationships"
[^p2]: arxiv-2512-05456 — "a form of post-selection bias known as the"
[^p3]: arxiv-2512-05456 — "even with infinite data, the naive estimator converges to the"
[^p4]: arxiv-2512-05456 — "Predictive models are typically trained to approximate Y pointwise, rather than preserve its specific structure"
[^p5]: arxiv-2512-05456 — "outcomes as conditioning variables can create a collider bias"
[^p6]: arxiv-2512-05456 — "accuracy does not guarantee valid downstream inference"
[^p7]: arxiv-2512-05456 — "observed and fixed, which ignores variability from both the prediction model"
[^p8]: arxiv-2512-05456 — "which underestimates uncertainty about the underlying data generating mechanism"
[^p9]: arxiv-2512-05456 — "Ignoring this leads to underestimated standard errors and anticonservative inference"
[^p10]: arxiv-2512-05456 — "The inferential goal is the marginal slope of Z1 on Y"
[^p11]: arxiv-2512-05456 — "the estimated slope is near zero despite high overall predictive fit"
[^p12]: arxiv-2512-05456 — "the residual variance is badly underestimated, producing anticonservative intervals"
[^p13]: arxiv-2512-05456 — "Predictive accuracy can be high in all four cases"
[^p14]: arxiv-2512-05456 — "association structure (bias), as well as omit uncertainty from the prediction step"
[^p15]: arxiv-2512-05456 — "At the same time, there are cases where predicted data can improve precision."
[^p16]: arxiv-2512-05456 — "efficiency gains, however, are conditional and fail when the residual correlation is weak"
[^p17]: arxiv-2512-05456 — "no amount of additional predicted data can add information"
[^p18]: arxiv-2512-05456 — "A natural solution leverages a small labeled set with gold-standard"
[^p19]: arxiv-2512-05456 — "shrink as training data grow larger and more representative"
[^p20]: arxiv-2512-05456 — "in small or moderate samples, or in settings of heterogeneity"
