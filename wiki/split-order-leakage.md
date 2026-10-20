---
description: "Split-order leakage: building input-output windows before partitioning lets future values reach training and inflate the score, most under 10-fold CV with longer lags."
aliases: ["data leakage in time series", "temporal leakage", "pre-split sequence generation", "window-before-split leakage"]
sources: ["arxiv-2512-06932", "doi-10-48550-arxiv-2608-24850"]
---
# Split-order leakage

A forecasting score is honest only if test data never reaches the training examples. Split-order leakage breaks that boundary through the order of operations, not through any reuse of test labels. A windowed model learns from examples cut out of a series: an input of the last *w* values and a target a *lag* of steps ahead. If the windows are cut from the full series before it is partitioned, a window whose input lies in the training period can carry a target from the test period. The source puts it this way: sequence windows generated before partitioning embed future values in the training set through overlapping temporal context.[^c1] The flaw sits in how the examples are built; the model never receives the test file as such.

The clean ordering reverses the steps. The data are split first into training, validation and test subsets, and sequences are then generated within each partition.[^c2] The source calls the leaky ordering a methodological flaw that lets future information unintentionally influence training.[^c3]

**How the bias is measured.** The study runs the same pipeline twice, once leaky and once clean, and reports the relative change in RMSE: RMSE Gain is "the relative change in RMSE attributable to leakage," computed as (RMSE_clean − RMSE_leaky) / RMSE_clean.[^c4] A positive value means the leaky setup looks better. The source reads it as "an apparent performance improvement under leaky conditions."[^c5] The measure is a paired difference, so it does not need the true error of either pipeline (my reading). It does need both arms to be run on the same data and settings (my reading).

**What it did.** On a daily climate series of 1,462 records, with a single LSTM layer of 64 units,[^c6][^c7] the sequential 10-fold configuration at lag 2 had a clean RMSE of 2.0868 and a leaky RMSE of 1.6841, a gain of 19.29%. At lag 3 the reported gain was 20.51%.[^c8] The authors summarise the 10-fold result as "RMSE Gain values up to 20.5%".[^c9] The 2-way split at the base configuration moved only 0.16%, with clean 1.6596 and leaky 1.6569.[^c10]

Two sequence parameters change the size of the bias. Longer lag steps raised it. Smaller windows raised it as well, and the abstract puts it as "smaller windows and longer lags increase the risk of leakage, whereas larger windows help reduce it."[^c11] In the Phase II sweep, 10-fold gains were 4.81% at window size 3 ("Smaller windows (e.g., size 3) showed an RMSE decrease")[^c20] and 7.17% at window size 7 ("also exhibited leakage-induced RMSE reduction from 1.7607 to 1.6347").[^c21]

**Why the validation design matters.** The same leak was much larger under 10-fold cross-validation than under the 2-way and 3-way splits. The authors attribute this to "repeated fold reuse across temporally adjacent windows."[^c12] I take a narrower reading as my own inference, not the source's: a 2-way split has one cut, so only windows straddling that cut can leak, while a 10-fold split makes a cut at each fold boundary. The study did not test this.

Gains can also be negative. "a negative RMSE Gain suggests performance degradation or stochastic variability."[^c13] One 2-way value at lag 2 was −2.46%, which the authors call "likely reflecting stochastic noise rather than genuine."[^c14] A gain of a few percent therefore sits close to run-to-run variance (my inference from those values).

The ordering rule is wider than windows. A detection-methodology review gives the same rule for every step fitted on the whole dataset before the split: "Each one inflates every number downstream of it." It calls these boundary steps "the defects most often found in published detection work."[^c22][^c23] Its example is a scaler: "a paper that fits a scaler on the whole dataset before splitting reports numbers" that later rigour cannot repair.[^c24] The review gives no size for this effect, so the windowed-LSTM gains above do not carry over to a scaler (my inference). Which test items a split draws, as distinct from when the split is made, is a separate matter treated in [[question-matched-split]].

## Limits

- **One dataset, one model.** The evidence is a single univariate series and one architecture: "use the Climate dataset and a univariate LSTM model."[^c15] The source mentions Transformers only as context.[^c16] Whether the size of the bias carries over to other series, horizons or architectures is not tested.
- **One configuration carried the sweep.** The window and lag sweep ran on Experiment 5 alone, chosen because it was the most leakage-sensitive baseline: "Experiment 5 was selected for in-depth."[^c17] Choosing the most sensitive case shows that large gains are possible; it does not give the typical gain.
- **The leaky arm is defined by one step.** The leaky pipeline differs from the clean one only in when sequences are generated: "generating input-output sequences prior to dataset partitioning."[^c18] Other pre-split steps are not separated out in what I read. Whether they add to this effect is my open question, not a finding.
- **Noise is not separated from gain.** The repeated runs were unseeded, "without fixing random seeds to capture variability."[^c19] The text I read gives no significance test for the Phase III gains, and the authors set one negative value aside as noise. Gains of a few percent should not be read as established.
- **The mechanism is the authors' explanation.** The fold-reuse account of the 10-fold result is offered, not isolated by an experiment.

The concept transfers as a pipeline ordering problem. What does not transfer is the 20% figure, which depends on the lag, window and validation scheme that produced it. This is distinct from test-set reuse during development, the kind of contamination catalogued in [[evaluation-questionable-research-practices]]: split-order leakage can occur with no tuning on the test set at all.

## Related

- [[evaluation-questionable-research-practices]] — the broader taxonomy; its "contamination" is test information reaching development, which split-order leakage does not require
- [[cross-generator-cross-corpus-split]] — another way train and test are kept apart by design, for synthetic benchmarks, where pipeline correlation remains
- [[benchmark-contamination-convergent-audit]] — estimates contamination of a finished benchmark, not a leak inside one training pipeline

[^c1]: arxiv-2512-06932 — "allowing future values to be embedded in the training set"
[^c2]: arxiv-2512-06932 — "generating sequences independently within each partition"
[^c3]: arxiv-2512-06932 — "input-output sequences are constructed prior to dataset partitioning, allowing future information to unintentionally influence training"
[^c4]: arxiv-2512-06932 — "This metric captures the relative change in RMSE attributable to leakage"
[^c5]: arxiv-2512-06932 — "A positive RMSE Gain indicates an apparent performance improvement under leaky conditions"
[^c6]: arxiv-2512-06932 — "Experiments use the Daily Climate dataset comprising 1,462"
[^c7]: arxiv-2512-06932 — "The architecture includes a single LSTM layer with 64 units"
[^c8]: arxiv-2512-06932 — "the RMSE decreased from 2.0868 (clean) to 1.6841 (leaky) at lag = 2"
[^c9]: arxiv-2512-06932 — "10-fold cross-validation exhibits RMSE Gain values up to 20.5%"
[^c10]: arxiv-2512-06932 — "showed only a 0.16% RMSE difference between clean (1.6596)"
[^c11]: arxiv-2512-06932 — "smaller windows and longer lags increase the risk of leakage, whereas larger windows help reduce it"
[^c12]: arxiv-2512-06932 — "repeated fold reuse across temporally adjacent windows"
[^c13]: arxiv-2512-06932 — "a negative RMSE Gain suggests performance degradation or stochastic variability"
[^c14]: arxiv-2512-06932 — "likely reflecting stochastic noise rather than genuine"
[^c15]: arxiv-2512-06932 — "use the Climate dataset and a univariate LSTM model"
[^c16]: arxiv-2512-06932 — "While recent architectures such as Transformers have gained attention"
[^c17]: arxiv-2512-06932 — "Experiment 5 was selected for in-depth"
[^c18]: arxiv-2512-06932 — "generating input-output sequences prior to dataset partitioning"
[^c19]: arxiv-2512-06932 — "fixing random seeds to capture variability"
[^c20]: arxiv-2512-06932 — "Smaller windows (e.g., size 3) showed an RMSE decrease"
[^c21]: arxiv-2512-06932 — "also exhibited leakage-induced RMSE reduction from 1.7607 to 1.6347"
[^c22]: doi-10-48550-arxiv-2608-24850 — "Each one inflates every number downstream of it"
[^c23]: doi-10-48550-arxiv-2608-24850 — "the defects most often found in published detection work"
[^c24]: doi-10-48550-arxiv-2608-24850 — "a paper that fits a scaler on the whole dataset before splitting reports numbers"
