---
description: "A design criterion that picks the next noisy sample by how much it is expected to shrink the total misclassified volume of a level set, not by the surrogate's variance alone."
aliases: ["SUR", "integrated stepwise uncertainty reduction", "integrated SUR", "gradient stepwise uncertainty reduction", "gSUR"]
sources: ["doi-10-1007-s11222-021-10014-w"]
---
# Stepwise uncertainty reduction

Stepwise uncertainty reduction (SUR) scores a candidate sample by the expected drop in the uncertainty about a level set after that one sample is taken. The uncertainty is the posterior error E: the expected volume of misclassified inputs under the surrogate. The criterion was first proposed by Bect et al. (2012) for this purpose, and it aims "to maximize the global learning rate about S."[^s1]

The mechanism is a one-step look-ahead. For a candidate input x, the integrated criterion subtracts from the current error the expected error after observing a new value at x. The expectation runs over the predictive distribution of that observation. The formal version is I_SUR(x) = E^(n) − E_Y(x)[E^(n+1) | x_{n+1} = x], with the look-ahead error computed from the updated posterior mean and standard deviation.[^s2] Read in words: the sample is chosen to make the sign estimate as settled as possible, one step ahead. The motivation is to minimise the expected one-step-ahead posterior error, which the paper says corresponds to a one-step Bayes-optimal design.[^s2]

Two approximations make the criterion usable. First, the integral over the input space is replaced by a sum over a finite grid: the paper replaces "the integral over D" with "a sum over a finite subset."[^s3] Second, the exact expectation exists only for one case: "That computation does not work with non-Gaussian noise, or for Cl-GP and TP."[^s4] The paper therefore uses an approximate look-ahead standard deviation, and reports that this version "performs generally better, being less sensitive to the" noise structure.[^s5]

A cheaper local variant, gSUR, keeps the same one-step idea but "dropping the computationally intensive integral over D," so that it measures only the gain in information about the contour near the candidate. It is related to the knowledge-gradient strategy of Frazier et al. (2008), modified for contours.[^s6]

What the comparison shows is a dependence on dimension, not a single winner. In lower dimensions the paper concludes that "there is little benefit to using the more sophisticated" SUR, while "for higher-dimensional problems, SUR" is significantly better than the other criteria.[^s7] The cheaper targeted MSE criterion "appears to be an adequate and cheaper choice."[^s8] For a t-process surrogate under misspecified noise in higher dimensions, the paper finds "SUR is the best choice among all designs for t-GP."[^s9]

## Limits

- The exact one-step expectation is closed-form only for Gaussian noise and a Gaussian surrogate. Outside that case the criterion runs on an approximation, and the paper's comparison is between two approximations, not against the exact value.
- The integral is replaced by a finite candidate set, so the criterion is only as good as that grid. The next input is the maximiser over the discretised set, and the answer can depend on its spacing; the paper does not measure this sensitivity.
- SUR carries more overhead than the cheaper heuristics, which the paper weighs against its gains. Its advice is that tMSE, which works "without requiring look-ahead variance," is preferred when the problem is low-dimensional and the overhead matters.[^s10]
- The benefit is reported for dimensions up to six and for the paper's benchmark functions. Its advantage in higher dimensions is an empirical finding, not a theorem, and the paper's own remark is that the "user ought to thoughtfully pick the combination of sequential design and metamodel."[^s11]
- Myopic one-step look-ahead can under-explore when the payoff is delayed; the paper does not test multi-step criteria. This is a general limit of the one-step family, my inference rather than the paper's result.

## Related

- [[noisy-level-set-estimation]] — the problem SUR is designed for; its loss is the misclassified volume
- [[student-t-observation-likelihood]] — the surrogate paired with SUR in the misspecified-noise results
- [[expected-information-gain]] — the general expected-gain family; SUR targets the error on the set, not information about f
- [[bayesian-experimental-design]] — the one-step-ahead expected-value framing SUR belongs to

[^s1]: doi-10-1007-s11222-021-10014-w — "the SUR strategy aims to maximize the global learning rate about S"
[^s2]: doi-10-1007-s11222-021-10014-w — "behind SUR is to minimize the expected one-step-ahead"
[^s3]: doi-10-1007-s11222-021-10014-w — "with a sum over a finite subset"
[^s4]: doi-10-1007-s11222-021-10014-w — "not work with non-Gaussian noise, or for Cl-GP and TP"
[^s5]: doi-10-1007-s11222-021-10014-w — "performs generally better, being less sensitive to the"
[^s6]: doi-10-1007-s11222-021-10014-w — "dropping the computationally intensive integral over D"
[^s7]: doi-10-1007-s11222-021-10014-w — "while for higher-dimensional problems, SUR"
[^s8]: doi-10-1007-s11222-021-10014-w — "tMSE appears to be an adequate and cheaper choice"
[^s9]: doi-10-1007-s11222-021-10014-w — "in higher dimensions with misspecified noise, SUR is the best"
[^s10]: doi-10-1007-s11222-021-10014-w — "in particular without requiring look-ahead variance"
[^s11]: doi-10-1007-s11222-021-10014-w — "user ought to thoughtfully pick the combination of sequential design and metamodel"
