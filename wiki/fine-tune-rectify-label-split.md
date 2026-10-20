---
description: "Splitting labels between fitting a surrogate and correcting it trades a power-law learning curve against the correction sample; the best fitting share falls as the noise floor rises."
aliases: ["fine-tune-then-rectify allocation", "FT+PPI sample allocation", "fitting-versus-correction label split", "single-fit sample splitting"]
sources: ["arxiv-2511-19486"]
---
# Label split between fitting and correcting a surrogate

Suppose a model is to stand in for a human outcome, and a fixed budget of n labelled cases is available. The labels can do two jobs. Some fit the model, which lowers its error. The rest correct the model's remaining errors on the labelled set, as a prediction-powered estimator does. [[residual-variance-fine-tuning-objective]] covers which error the fitting should minimize. This note covers how many labels each job should get.

The paper's design is single-fit: "each labeled sample enters exactly one stage."[^c1] With s labels for fitting and n − s for correction, the variance of the final estimate is governed mainly by the residual variance of the fitted model divided by n − s. Two forces then pull against each other. Giving more labels to correction shrinks the 1/(n − s) factor. Giving more labels to fitting lowers the residual variance, because the fitted model is better. The split is a trade-off, and no single rule puts all labels on one side.

The second ingredient is a learning curve. The paper assumes the residual variance follows a power law in the fitting size, of the form a·s^(−α) + b, where "a" and "α" are positive, b is non-negative, and "are task-specific constants."[^c2] The term b is an error floor that more labels cannot remove. Minimizing (a·s^(−α) + b)/(n − s) over s gives an interior optimum, characterized by an equation the paper solves numerically.

The optimum has a readable shape. Its fitting share rises with a, the size of the reducible error, since the optimal share "is nondecreasing in a".[^c17] It falls with b: "The parameter b can be interpreted as the noise floor," and "optimal to allocate fewer samples for fine-tuning" as it rises.[^c3][^c4] Without a floor, b = 0, the fitting share is the constant α/(α + 1), "which depends solely on the power-law exponent."[^c5] With a floor, the share shrinks as n grows and tends to zero in the limit. So with a floor the best split moves with the budget; the constant share is the idealized case, my reading of the paper's Proposition 1.

The paper also gives a yes-or-no test. Against the plain sample mean, the split beats it in variance "if and only if" the fitted model's variance-based goodness of fit, R²(s), is larger than the fraction s/n of labels spent on fitting. The text puts it as: "exceeds the fraction of labeled data consumed by fine-tuning."[^c6] Here R²(s) is one minus the ratio of the residual variance to Var(Y). My reading: the surrogate's variance reduction must outweigh the cost of having fewer labels for correction. Under the scaling law, the feasibility condition is easier to meet when the total budget is larger: "making it easier for the condition to hold."[^c7] A high floor relative to the outcome's variance can make the split useless, which is why the condition involves b.

The measured evidence is from one task. The authors report that the scaling law holds for the variance-based objective, and that "optimum derived from the scaling law accurately guides the optimal sample allocation."[^c8] Against the sample mean, the method "reduces the labeling budget by 48% to 54%" for the same accuracy, on the Wine Reviews mean estimate.[^c9]

What transfers beyond this setting is the trade-off, not the constants. Any estimate that uses a fitted model and a fixed labelled sample for correction faces the same tension, and a power-law learning curve with a floor is a common shape for error against sample size. What does not transfer is the numerical split: α, a and b are task-specific, and the paper estimates them from a pilot sequence, not from theory. The paper says that "these parameters can be estimated from a data-driven" ramp-up procedure.[^c10]

## Limits

- The variance criterion assumes many unlabelled samples. "Proposition 2 assumes an asymptotic regime where the number of unlabeled samples" grows without bound, which drops the second variance term.[^c11] The text says finite-sample terms can be added; I did not find that carried out in the sections I read.
- The optimum is derived assuming the scaling-law constants are known. In practice they come from a ramp-up fit. The paper says that "the optimality of the data-driven ramp-up strategy could be further investigated."[^c12] I did not find a sensitivity analysis of the allocation to errors in the fitted constants.
- The model size is held fixed, because size options are "typically constrained" by cost and by the base models available.[^c13] Whether a size choice would change the split is not tested.
- When the fitting data are not identically distributed, the paper handles the difference only by changing the scaling-law parameters: "the non-identical setting simply through changes in scaling law parameters" is its own admission that the transfer case is open.[^c14]
- The empirics are one mean-estimation corpus and one regression. "Empirical results also confirm that our theoretically derived allocation closely" matches the empirical optimum, but on that data only.[^c15]
- The condition for beating the sample mean is stated against a noise floor relative to the outcome's variance. "If the irreducible error b is too high relative to the inherent" data variance, the split does not help.[^c16] The gain is therefore conditional, and a practitioner cannot read it from the sample size alone.

## Related

- [[residual-variance-fine-tuning-objective]] — the fitting objective whose residual variance enters the split; the allocation assumes that objective is used.
- [[calibrated-judge-estimator-efficiency-ordering]] — the prediction-powered estimators that the correction stage uses; the split here is in front of that estimator, not inside it.
- [[asymmetric-calibration-allocation]] — the other labelled-data split, between the two true-label classes of a judge's calibration set, for a Rogan–Gladen interval.

[^c1]: arxiv-2511-19486 — "sample enters exactly one stage"
[^c2]: arxiv-2511-19486 — "are task-specific constants"
[^c3]: arxiv-2511-19486 — "The parameter b can be interpreted as the noise floor"
[^c4]: arxiv-2511-19486 — "optimal to allocate fewer samples for fine-tuning"
[^c5]: arxiv-2511-19486 — "which depends solely on the power-law exponent"
[^c6]: arxiv-2511-19486 — "exceeds the fraction of labeled data consumed by fine-tuning"
[^c7]: arxiv-2511-19486 — "making it easier for the condition to hold"
[^c8]: arxiv-2511-19486 — "optimum derived from the scaling law accurately guides the optimal sample allocation"
[^c9]: arxiv-2511-19486 — "reduces the labeling budget by 48% to 54%"
[^c10]: arxiv-2511-19486 — "these parameters can be estimated from a data-driven"
[^c11]: arxiv-2511-19486 — "Proposition 2 assumes an asymptotic regime where the number of unlabeled samples"
[^c12]: arxiv-2511-19486 — "the optimality of the data-driven ramp-up strategy could be further investigated"
[^c13]: arxiv-2511-19486 — "foundation model as fixed, because size choices are typically constrained"
[^c14]: arxiv-2511-19486 — "the non-identical setting simply through changes in scaling law parameters"
[^c15]: arxiv-2511-19486 — "Empirical results also confirm that our theoretically derived allocation closely"
[^c16]: arxiv-2511-19486 — "If the irreducible error b is too high relative to the inherent"
[^c17]: arxiv-2511-19486 — "is nondecreasing in a"
