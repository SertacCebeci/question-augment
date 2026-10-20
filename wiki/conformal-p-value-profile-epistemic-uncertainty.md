---
description: "Two conformal prediction sets of equal size can differ in epistemic uncertainty; the shape of the sorted conformal p-values, scored by Maximum Mean Imprecision, measures it where set size cannot."
aliases: ["MMI-CP", "epistemic predictive uncertainty in conformal prediction", "Maximum Mean Imprecision for conformal prediction", "conformal credal set imprecision"]
sources: ["arxiv-2602-01667"]
---
# Conformal p-value profile as epistemic uncertainty

The size of a conformal prediction region (CPR) at a fixed level α is the usual proxy for how unsure a conformal predictor is. The paper argues it measures uncertainty about the predicted region, not the difficulty of producing the prediction, and shows two instances with identical sets at α = 0.05 whose p-value profiles differ markedly.[^c1] The alternative is to read the whole profile of conformal p-values over labels.

## Mechanism

1. **Consonance.** A conformal transducer is consonant if its largest p-value is 1. This is automatic in regression with residual scores. In classification it is forced by setting the top p-value to 1, which leaves non-empty sets unchanged.[^c2]
2. **Credal set.** A consonant transducer induces the upper probability P(A) = sup of p-values over A, a plausibility measure. Its core is an implicit set of predictive distributions (a credal set). The (1−α) imprecise highest density region of that upper probability equals the split-conformal region exactly.[^c3] So the region is what every distribution in the credal set agrees on, and the credal set's spread is the model multiplicity.
3. **Maximum Mean Imprecision (MMI).** The largest gap, over a class of test functions, between optimistic and pessimistic expectations; it measures conflicting information in the credal set.[^c4]
4. **Cheap closed forms.** With indicator test functions, MMI equals the second-largest conformal p-value, computed in O(K) instead of O(2^K).[^c5] Using the transducer itself as the test function, MMI integrates over α the largest p-value among labels excluded from the region.[^c6] For K classes this is a sum of consecutive sorted-p-value gaps times the lower p-value.[^c7] A large gap, meaning a skewed profile where few labels get strong support, makes the set-building more decisive and lowers the uncertainty.[^c8]

In the paper's active-learning and selective-classification experiments, the quantified uncertainty gave more informative, finer-grained assessments than set size alone.[^c9]

## Regression collapses

For regression scores where the infimum score outside the region equals the calibration quantile (absolute residual, weighted residual, quantile-regression score), the measure is the same constant for every test input.[^c10] The authors link this to the known weakness of conformal regression at telling instances apart by interval size.[^c11] So the profile idea discriminates in classification but is uninformative for these standard regression scores.

## Limits

- The measure depends on the calibration set and the nonconformity score; it is not a score-free property of the problem.[^c12]
- The credal-set reading needs consonance; in classification this is a construction, not a property of the raw transducer.
- Whether a lower MMI means the model is truly more certain, as against merely better calibrated, is not separated here; "epistemic" has no single formal definition, as the paper itself notes.[^c13]
- Only tabular-style classification and regression tasks were considered. Use for deciding when an agent should ask a clarifying question is my conjecture, not tested.

## Related

- [[conformal-prediction]] — the framework whose p-values are read here
- [[uncertainty-decomposition]] — epistemic versus aleatoric split this measure targets
- [[credal-then-conformalize-interval-decomposition]] — another credal-plus-conformal route to epistemic width
- [[conformal-set-size-calibration-tradeoff]] — set size as the efficiency criterion this note says is insufficient
- [[selective-abstraction]] — downstream task where the measure was tested

[^c1]: arxiv-2602-01667 — "the CPR size at a fixed level α characterises uncertainty about the predicted region itself, rather than the uncertainty encountered when producing that prediction."
[^c2]: arxiv-2602-01667 — "this modification does not affect non-empty prediction sets, retains the marginal coverage guarantee in general"
[^c3]: arxiv-2602-01667 — "IRM α = Cα (x)."
[^c4]: arxiv-2602-01667 — "the MMI measures the degree of conflicting information by the largest discrepancy, over a prescribed class of test functions, between optimistic and pessimistic expectations."
[^c5]: arxiv-2602-01667 — "In classification, computing MMIHTV (Px ) takes only O(K) time, compared to O(2K ) for general"
[^c6]: arxiv-2602-01667 — "aggregates, across all confidence levels, the largest conformal p-values among"
[^c7]: arxiv-2602-01667 — "the discrete “gradients” of the p-value profile, namely the consecutive differences πσ(k−1) − πσ(k)"
[^c8]: arxiv-2602-01667 — "a large gap between consecutive sorted p-values indicates a highly skewed"
[^c9]: arxiv-2602-01667 — "provides substantially more informative and"
[^c10]: arxiv-2602-01667 — "the quantified EPU is constant across any prediction instances x."
[^c11]: arxiv-2602-01667 — "conformal regression is generally poor at"
[^c12]: arxiv-2602-01667 — "the EPU quantified is intrinsically shaped by both the calibration set and the chosen nonconformity"
[^c13]: arxiv-2602-01667 — "EPU does not admit one precise"
