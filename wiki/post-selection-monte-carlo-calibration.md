---
description: "A test whose alternative was picked from the data keeps its error rate only if its critical value is simulated by replaying the same selection rule under the current null."
aliases: ["Monte Carlo post-selection calibration", "selection-replaying critical value", "post-selection Type I error control"]
sources: ["doi-10-1007-s00190-026-02043-y"]
---
# Post-selection calibration by replaying the selection

When the alternative in a test is chosen from the data, the reference distribution of the test statistic changes. The paper states it for its own setting: "the null model no longer follows its classical asymptotic distribution because the model under test depends on the data."[^p1] The consequence is an inflated error rate. If nominal critical values are used anyway, "the actual post-selection Type I error can exceed the user-defined significance level."[^p2]

The fix the paper uses is to simulate the whole selection under the current null. Epoch one is generated without displacement and epoch two with the displacement estimated at the previous stage. The statistic is computed for every admissible group of points, the maximum is selected, and the statistic of that selected model is stored. This is repeated M times, and the critical value is the empirical (1 − α) quantile of the stored statistics.[^p3] The point of the replay is that it "reproduces the post-selection mechanism and does not" involve a hypothesis test at the selection step.[^p3]

The paper states the general principle as "replicating the same selection rule applied in the sequential" procedure.[^p4] Its calibration at each stage conditions on the model chosen at the previous stage, "conditional on the data-driven model selected at the previous stage."[^p5]

What was measured: the paper reports that "the false-alarm rate at later stages does not inflate and" stays at or below the nominal level, and it says so as an empirical finding: "we show empirically."[^p6]

Where the idea comes from: the paper places it inside a known literature, noting that "consequence is well documented in the statistical literature on post-selection inference."[^p7] The resampling and exact-inference methods it cites address the same selection problem. What survives the transfer is the replay logic: any pipeline that selects a model from data and then tests it can, in principle, be calibrated by running the selection again under the null. What does not transfer as written is the paper's particular statistic, a quadratic form in Gaussian errors, with the selection taken as a maximum over projector-defined groups. Another test would need its own replay.

## Limits

- The validity claim is empirical in the text read. No theorem for the replay is stated in the slices read; "we show empirically" is the strength of the evidence.[^p6]
- The replay plugs in an estimated displacement vector, "with the associated displacement vector" from the previous stage.[^p8] Estimation error in that vector enters the simulated null. The slices read do not measure how much it moves the critical value.
- An error at an earlier stage is carried forward. The calibration is conditional on the earlier selection, so it does not correct a wrong early choice; it only keeps the later test honest about it.
- The error model is Gaussian with a stated covariance (the epoch distributions in eq. 25). A misspecified covariance would move the critical value, and this was not tested in the slices read.
- Cost is not analysed. The number of replications differs across the paper's experiments: "were obtained using M = 5,000,000 Monte Carlo simulations" for one table,[^p9] and 5,000 for others. The trade-off between replication count and critical-value precision is not discussed.

## Related

- [[hypothesis-testing]] — the nominal α this calibration protects once the alternative is chosen from the data.
- [[smear-effect]] — the identification problem inside which the calibrated test runs; the calibration controls the false-alarm rate, not the masking and swamping it leaves open.
- [[turn-valid-coverage]] — another post-selection correction, which reweights the selected query distribution by a likelihood ratio rather than replaying the selection.
- [[shared-projector-indistinguishability]] — decides which pairs of models the calibrated test is allowed to compare.

[^p1]: doi-10-1007-s00190-026-02043-y — "the null model no longer follows its classical asymptotic distribution because the model under test"
[^p2]: doi-10-1007-s00190-026-02043-y — "can exceed the user-defined significance level."
[^p3]: doi-10-1007-s00190-026-02043-y — "reproduces the post-selection mechanism and does not"
[^p4]: doi-10-1007-s00190-026-02043-y — "replicating the same selection rule applied in the sequential"
[^p5]: doi-10-1007-s00190-026-02043-y — "conditional on the data-driven model selected at the previous stage"
[^p6]: doi-10-1007-s00190-026-02043-y — "that the false-alarm rate at later stages does not inflate and"
[^p7]: doi-10-1007-s00190-026-02043-y — "consequence is well documented in the statistical literature on post-selection inference"
[^p8]: doi-10-1007-s00190-026-02043-y — "with the associated displacement vector"
[^p9]: doi-10-1007-s00190-026-02043-y — "were obtained using M = 5,000,000 Monte Carlo simulations"
