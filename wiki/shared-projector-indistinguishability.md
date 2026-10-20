---
description: "Candidate models that share a projector give identical test statistics, so the statistic cannot pick between them; a normalized projector distance grades separability."
aliases: ["structurally indistinguishable models", "shared projector", "projector separability", "geometric separability"]
sources: ["doi-10-1007-s00190-026-02043-y"]
---
# Shared-projector indistinguishability

In a linear least-squares test, a candidate displacement model enters the statistic only through its projector, the matrix that maps the data onto the range of that model's design. The statistic for a candidate is a quadratic form in the data residuals with that projector in the middle. Two candidates with the same projector therefore give the same statistic. The paper says "We say that two models are structurally indistinguishable" when "they share the same projector," and then that "the test statistics, such as (16), are also identical."[^q1][^q2]

The consequence for selection is that the maximum over candidates "does not isolate a" single group. Two or more candidates tie, and the paper calls this "statistical overlapping."[^q3] Because the statistic depends on the data only through the projector, no choice among tied candidates can be made from that statistic. This is my inference from the formula, and it holds for any statistic of that form, not only the paper's.

The paper turns this into a filter. Among models of the same dimension, any top-dimension set whose members are not mutually distinguishable is dropped, and the top dimension is reduced "until all models are mutually separable, at least in geometrical sense."[^q4]

For the decision between a null of dimension q_j and an alternative of q_(j+1), the paper adds a continuous measure. The normalized distance is the Frobenius norm of the difference of the two W-weighted projectors, divided by the square root of the rank of the alternative projector, and it lies between 0 and 1.[^q5] The normalization "removes the trivial dependence of the Frobenius norm on the" dimension of the alternative, so that the distance reflects geometry and not the number of degrees of freedom.[^q6] At the extremes, a distance of 0 means the two operators coincide, and a distance of 1 means "models produce completely different projection operators in" the observation space.[^q7]

The paper uses the distance as a screen for stages that are "potentially weak" in separability. It says the geometric check is needed at the decision step too, though not sufficient: "selection of alternative models, as in (17), it is not sufficient."[^q8]

## Limits

- Geometric separability does not settle the statistics. The paper says "this geometrical distinction does not guarantee unique statistical outcomes."[^q9] Even distinct projectors can produce overlapping decisions for a given data vector.
- The slices read give no numerical cut-off on the distance below which a stage is refused. The distance is used as a diagnostic that "identifies problematic cases," not as a threshold with a stated value.
- One network is reported with high separability: "SEQCUP benefits from the high geometrical separability of the network," with a mean distance of about 0.82. That single value does not show how the distance behaves across network designs.[^q10]
- The distance is defined for the W-weighted projectors of the paper's mean-shift model on inter-epoch differences. The paper says its approach applies to nonlinear networks "without requiring model linearization,"[^q11] but how the distance should be read for a nonlinear design is not spelled out in the slices read.
- The argument is algebraic about projectors. It says nothing about how often indistinguishable pairs arise in practice; the paper reports that such cases "become very rare once this filter is applied," which is its own observation and not a general rate.[^q12]

## Related

- [[smear-effect]] — shared projectors are one geometric route into masking and swamping; separability is the paper's remedy for that route.
- [[post-selection-monte-carlo-calibration]] — the calibration runs on the pairs that pass this separability check, and its replay is only as good as the candidate set it replays.
- [[hypothesis-testing]] — the null-versus-alternative decision that the normalized distance is meant to make meaningful.

[^q1]: doi-10-1007-s00190-026-02043-y — "We say that two models are structurally indistinguishable"
[^q2]: doi-10-1007-s00190-026-02043-y — "the test statistics, such as (16), are also identical"
[^q3]: doi-10-1007-s00190-026-02043-y — "the maximum of the test statistic in (17) does not isolate a"
[^q4]: doi-10-1007-s00190-026-02043-y — "This process continues until all models are mutually separable, at least in geometrical sense."
[^q5]: doi-10-1007-s00190-026-02043-y — "The normalized distance in (38) also has a clear interpretation at its extremes"
[^q6]: doi-10-1007-s00190-026-02043-y — "removes the trivial dependence of the Frobenius norm on the"
[^q7]: doi-10-1007-s00190-026-02043-y — "models produce completely different projection operators in"
[^q8]: doi-10-1007-s00190-026-02043-y — "selection of alternative models, as in (17), it is not sufficient"
[^q9]: doi-10-1007-s00190-026-02043-y — "this geometrical distinction does not guarantee unique statistical outcomes."
[^q10]: doi-10-1007-s00190-026-02043-y — "SEQCUP benefits from the high geometrical separability of the network"
[^q11]: doi-10-1007-s00190-026-02043-y — "without requiring model linearization"
[^q12]: doi-10-1007-s00190-026-02043-y — "such cases become very rare once this filter is applied"
