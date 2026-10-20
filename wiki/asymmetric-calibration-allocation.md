---
description: "Splitting a fixed human-label budget between judge-correct and judge-incorrect calibration items by the judge's error ratio and raw positive rate shortens the Rogan-Gladen interval."
aliases: ["error-ratio allocation", "adaptive calibration allocation", "label-type allocation for judge calibration", "asymmetric calibration sample split"]
sources: ["arxiv-2511-21140"]
---
# Asymmetric calibration allocation

A judge-based rate is corrected with two numbers measured on a human-labelled calibration set. The first is the judge's sensitivity q1, the probability that it calls a truly correct response correct. The second is its specificity q0, the probability that it calls a truly incorrect response incorrect.[^a1] Each is estimated only from the calibration items of its own true label. So the calibration budget is in effect two budgets, one for each label type, and how it is divided is a design choice.

The two label types need not be equally costly to pin down. The paper defines the error ratio κ = (1 − q̃0)/(1 − q̃1), which compares the judge's error on incorrect responses with its error on correct ones.[^a2] It states that the two label types "typically contribute asymmetrically to the overall uncertainty", so an unequal split can give a shorter interval for the same total number of labels.[^a3]

The paper gives a closed-form guide for the split. Its Proposition 5.2 says that, when q̃0 and q̃1 are close to 1, the confidence interval is shortest when the incorrect-label count m0 is about (1/p̃ − 1)·κ times the correct-label count m1, where p̃ is the adjusted raw positive rate on the test set. The direction is explicit in the text: "more calibration samples should be allocated to estimating q̃1" when the judge is weaker on correct responses (small κ) or when the raw rate is large.[^a4] My reading of the rule, not the paper's words: the label type whose judge error is smaller and harder to pin down receives more labels, and the raw positive rate shifts the balance further.

The paper turns this into a procedure. A small pilot set, about ten labels per label type, gives preliminary q̃0 and q̃1; "It then computes the empirical error ratio" and combines it with the test-set rate to set (m0, m1).[^a5] In the Monte Carlo setting with q0 = 0.7 and q1 = 0.9 and a fixed budget of m = 200, the authors report that the allocation "gives shorter confidence intervals" than an equal split.[^a6]

What the closed form does not change is the sample-size scale. For a symmetric split at q̂0 = 0.7 and q̂1 = 0.9, the paper reads off that an interval under 0.1 needs about 200 calibration examples when the raw rate is 0.3.[^a7] The allocation rule reshapes that budget; it does not lower the total it needs.

## Limits

- The closed form is stated for judges whose sensitivity and specificity are close to 1. The simulated judge has q0 = 0.7, which is not close to 1, so the rule is an approximation checked at one judge pair, not a derivation that covers the case it is applied to.
- The pilot estimate of κ rests on about ten labels per type. The paper does not test how the allocation degrades when the pilot is badly off, nor how often a pilot would reverse the direction of the split.
- The optimality is for the length of the Rogan–Gladen interval. The closed form is specific to that estimator's variance. My inference: the same split is not justified for the prediction-powered estimators, whose variance has a different form, and the text does not check them.
- An unequal split presumes a handle on label composition. The paper says that "its label composition can sometimes be influenced through sampling strategies"; if the calibration set is a fixed random sample, there is nothing to allocate.[^a8]
- The allocation rests on the judge's errors depending only on the true label. The paper names the threat: the invariance may fail if "nuisance factors such as response length, style, or prompt type affect the LLM judge differently across datasets".[^a9] A split tuned to one stratum of responses can be wrong for another.
- Transfer from diagnostic testing: the two-rate correction and the split idea come from the sensitivity and specificity setting of medical tests, where the error rates are assumed to be properties of the test. What survives is the two-class error structure. What does not is any guarantee that a judge's error rates are stable across the populations it is applied to, which the paper's own limit above concedes.

## Related

- [[calibrated-judge-estimator-efficiency-ordering]] — the Rogan–Gladen and prediction-powered estimators whose interval the split shortens; the efficiency ordering there is the setting in which this allocation applies
- [[llm-judge-validation-gap]] — why the human calibration set is small and costly enough that dividing it matters

[^a1]: arxiv-2511-21140 — "Let q1 and q0 denote the probabilities that the LLM correctly judges"
[^a2]: arxiv-2511-21140 — "we define the error ratio κ"
[^a3]: arxiv-2511-21140 — "the two label types typically contribute asymmetrically to the overall uncertainty"
[^a4]: arxiv-2511-21140 — "more calibration samples should be allocated to estimating q̃1"
[^a5]: arxiv-2511-21140 — "It then computes the empirical error ratio"
[^a6]: arxiv-2511-21140 — "The proposed allocation gives shorter confidence intervals."
[^a7]: arxiv-2511-21140 — "achieving an interval shorter than 0.1 requires m ≈ 200 calibration examples"
[^a8]: arxiv-2511-21140 — "its label composition can sometimes be influenced through sampling strategies"
[^a9]: arxiv-2511-21140 — "nuisance factors such as response length, style, or prompt type affect the LLM judge differently across datasets"
