---
description: "A metric is inflated by random scoring when uninformed predictions reach scores near genuine detectors; a random-baseline separation test exposes it, and NAB and Point-Adjust fail."
aliases: ["random-prediction inflation", "anti-randomness of metrics", "chance-level inflation of a metric", "random-guess robustness"]
sources: ["arxiv-2511-18739", "arxiv-2511-17405"]
---
# Random-score inflation

A metric is random-score inflated when an uninformed predictor can reach a score close to that of a genuine detector. The property is tested directly: run a genuine detector and a random predictor against the same labelled series, then ask whether the two sets of scores separate. In a controlled study of time series anomaly detection, metrics differed by up to an order of magnitude on this separation.[^c1] The test rests on two hypotheses: genuine detectors should score significantly higher than random predictions, and scores should rise monotonically as detector quality rises.[^c2]

The average gap can hide the failure, so the separation has to be read as a distribution. For the Point-Adjust F-score the genuine and random averages were 0.842 and 0.433, which the authors call "a modest effect size" of 3.715 with an AUC of 0.930.[^c3] For TD the averages were "almost indistinguishable (0.904 vs. 0.896)", with a high AUC of 0.913 but a monotonicity coefficient that fell to 0.440.[^c4] For NAB the AUC was 0.645 and the effect size negative, so "the metric may even rank random predictions comparably to or better than genuine detectors."[^c5]

The mechanism the authors point to is granularity and admissibility. A metric inflates random scores when isolated or fragmented hits earn credit: the robustness-enhancing designs aim at "preventing artificial score inflation caused by" such hits.[^c6] A metric's resistance "ultimately reflects how rigorously it defines what constitutes a valid detection."[^c7] Fine-grained evaluation also helps, since it "reduces the probability that accidental hits disproportionately influence global performance."[^c8] The clearest case is event-level crediting, taken up in [[point-adjustment]].

Separation is not a constant property of a metric. The discriminative ability of most metrics "exhibits the strongest dependence" on signal-to-noise ratio, and depends much less on anomaly density or series length.[^c9] When the detector's scores are poorly separated from normal scores, genuine and random predictors overlap for any metric, so a flat separation can mean a weak detector rather than a bad metric.

The random baseline is a floor, not a ceiling. Under an oracle attack, "certain metrics may be artificially inflated through targeted" optimisation, so a metric can pass the random test and still be gamed.[^c10]

Transferred to answering, the test asks whether a grader can be passed by an answerer with no information about the question. That transfer is my inference. The work measures only the detection of anomalous points in series; it does not test answers, and the authors' conclusion is that "metric suitability is inherently task-dependent."[^c11]

The same floor sits under multiple-choice benchmarks, where a score can rise by guessing alone. The paper's bound takes a model that answers correctly in open form where it can and guesses uniformly on the rest: its multiple-choice accuracy is the open-form accuracy plus the guessing share, with K options.[^c15] On six-option versions of two open benchmarks, converting to multiple choice gave gains above both the open-ended baseline and that bound.[^c16] That is the chance-floor test applied to a benchmark score rather than to a metric. The transfer is my inference: the paper does not use the term random-score inflation, and its shortcut concerns option information as well as guessing, see [[option-matching-shortcut]].

## Limits

- The evidence is one experimental pipeline: synthetic series with controlled anomalies, plus "three widely-used univariate time series (UTS) anomaly" benchmarks drawn from TimeSeriesBench.[^c12] The random predictors are "various random-prediction strategies", not one canonical random predictor.[^c13]
- The oracle results are explicitly "not used as formal evaluation evidence"; they are a stress test, not a measured bound.[^c10]
- The authors themselves recommend re-running the pipeline over time, because metric discriminability "may shift with new models and datasets."[^c14]
- A random baseline shows only that a metric prefers genuine detectors to chance. It does not show that a high-scoring detector is correct, nor that a low-separation metric is wrong for a task that does not need that separation.
- Whether the test carries to question answering or grading of answers is not established here; that is my inference, flagged above.

## Related

- [[point-adjustment]] — the segment-credit rule behind the largest measured inflation in this study
- [[hubness-in-neural-metrics]] — a different route to the same failure: one input-independent text scores high whatever the reference
- [[ai-score-inflation]] — a different inflation: a gap between take-home and proctored scores, with no chance floor involved
- [[three-test-metric-validity-audit]] — audits a metric by what it should and should not reward; a random-baseline check is one such test

[^c1]: arxiv-2511-18739 — "up to an order of magnitude in distinguishing genuine detectors from random guessing"
[^c2]: arxiv-2511-18739 — "Genuine detectors should yield significantly higher"
[^c3]: arxiv-2511-18739 — "close (0.842 vs. 0.433), resulting in a modest effect size of"
[^c4]: arxiv-2511-18739 — "almost indistinguishable (0.904 vs. 0.896)"
[^c5]: arxiv-2511-18739 — "the metric may even rank random predictions comparably to or better than genuine detectors"
[^c6]: arxiv-2511-18739 — "preventing artificial score inflation caused by"
[^c7]: arxiv-2511-18739 — "how rigorously it defines what constitutes a valid detection"
[^c8]: arxiv-2511-18739 — "Fine-grained evaluation reduces the probability that accidental hits disproportionately"
[^c9]: arxiv-2511-18739 — "the discriminative ability of most metrics exhibits the strongest dependence"
[^c10]: arxiv-2511-18739 — "certain metrics may be artificially inflated through targeted"
[^c11]: arxiv-2511-18739 — "metric suitability is inherently task-dependent"
[^c12]: arxiv-2511-18739 — "three widely-used univariate time series (UTS) anomaly"
[^c13]: arxiv-2511-18739 — "with various random-prediction strategies and multiple tiers"
[^c14]: arxiv-2511-18739 — "We therefore recommend periodically re-running the established experimental pipeline"
[^c15]: arxiv-2511-17405 — "i.e., the model answers correctly on items it can already solve in open-ended form and guesses uniformly on"
[^c16]: arxiv-2511-17405 — "converting to MCQA yields consistently large gains relative to the open-ended"
