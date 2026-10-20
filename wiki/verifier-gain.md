---
description: "A verifier's worth in rejection sampling is its precision minus the solver's accuracy, an asymptotic bound that predicts test-time gains better than verifier accuracy does."
aliases: ["verifier gain", "verification gain", "precision-minus-solver-accuracy gain"]
sources: ["arxiv-2512-02304"]
---
# Verifier gain

A solver that is asked once answers correctly some fraction of the time. A verifier that judges its answers can be used to filter: draw answers until the verifier accepts one, and keep that one. What the verifier adds is then the change between the solver's raw accuracy and the correctness of the answers that survive the filter. The paper calls this verifier gain and defines it as the verifier's precision minus the solver's accuracy.[^c1]

The mechanism behind the definition is rejection sampling. The solver keeps drawing solutions until the verifier accepts one. "Assuming the solver has a non-zero probability of sampling a correct solution, in the limit of infinite resampling, the expected correctness of the accepted solution converges to the verifier's precision, or the proportion of accepted solutions that are actually correct."[^c2] Gain is therefore the improvement in the accepted answer over the unfiltered one. Because the limit is infinite resampling, the paper treats the metric as a ceiling: "Since this is an asymptotic metric, it serves as a bound on the improvement attainable by verifier-based rejection sampling."[^c3]

The paper argues that the metric is needed because verifier accuracy alone does not say how useful a verifier is at test time: "Verifier accuracy alone provides an incomplete picture of verifier usefulness at test time."[^c4] My reading, not the paper's wording: accuracy pools a verifier's errors on correct and on incorrect solutions, while precision depends on how often the solver is right to begin with. Two verifiers with the same accuracy can therefore differ in the answers they let through, and the solver's own accuracy sets the baseline the gain is measured against.

The metric was checked against an experiment. Over a 12-model subset of the post-trained models, the paper ran rejection sampling with each solver–verifier pair and compared the empirical gain with the theoretical gain. Each point in its figure is one pair, averaged over datasets. "The Pearson correlation (r) strengthens considerably from 3 to 10 attempts, consistent with verifier gain being an asymptotic metric that better predicts performance as the resampling attempts grow."[^c5] When no correct-labelled answer appeared within the attempt limit, the paper "retain[ed] the final attempt", so the empirical gain is measured under a cap.[^c6] The paper's practical claim is that the gain "can be estimated from a single verification round without costly rejection sampling experiments."[^c7]

Used across model families, the metric orders the verification settings. Self-verification gives the smallest gains: "self-verification yields the smallest gains, and more accurate solvers do not exhibit greater self-improvement."[^c8] For the reasoning post-trained models the paper reports that "cross-family verification provides the greatest potential benefits."[^c9] Its explanation for the weak self-verification gains is taken up in [[spontaneous-self-verification]].

## Limits

- The metric is asymptotic. The check against experiment is weaker at 3 attempts than at 10, and the paper's own statement is that it "serves as a bound". It does not say what gain a fixed small budget will reach.
- The bound assumes the solver can produce a correct solution at all. Where that probability is zero, no resampling reaches the precision and the gain does not apply.
- The correlation is between pair-level averages over datasets. The paper does not show that a per-question gain predicts the benefit on that question.
- Precision needs ground-truth labels. The tasks are exact-answer benchmarks (boxed answers, rule-checked puzzles, or multiple choice). The metric's behaviour on open-ended answers, where correctness is hard to label, is not tested here.
- The empirical check used a 12-model subset, not all 37 models, and the figure does not show the per-model spread.
- The gain is a difference, so it can be negative. The axis of the paper's gain figure runs below zero. My reading: a verifier that rejects correct answers more than it rejects wrong ones can lower the accepted precision.

## Related

- [[verifier-noise-self-improvement-condition]] — a sign condition for self-improvement in a generator-verifier loop, derived from noise variances; verifier gain is an empirical, asymptotic quantity for the same kind of benefit, and neither paper compares them
- [[verifier-discrimination-and-calibration]] — the quality of a verifier's ranking and calibration; verifier gain is a different quantity, one that also takes the solver's accuracy into account
- [[test-time-scaling]] — the family of methods that verifier-based rejection sampling belongs to; the gain is the ceiling on what filtering by a verifier adds
- [[solver-verifier-similarity]] — the pairing property that moves verifier gain between verification settings

[^c1]: arxiv-2512-02304 — "we derive verifier gain, a metric that simulates the improvement"
[^c2]: arxiv-2512-02304 — "has a non-zero probability of sampling a correct solution, in the limit of infinite resampling"
[^c3]: arxiv-2512-02304 — "it serves as a bound on the improvement attainable by verifier-based rejection sampling"
[^c4]: arxiv-2512-02304 — "Verifier accuracy alone provides an incomplete picture of verifier usefulness at test time"
[^c5]: arxiv-2512-02304 — "The Pearson correlation (r) strengthens considerably from 3 to 10 attempts"
[^c6]: arxiv-2512-02304 — "we retain the final attempt"
[^c7]: arxiv-2512-02304 — "Crucially, it can be estimated from a single verification"
[^c8]: arxiv-2512-02304 — "self-verification yields the smallest gains, and more accurate solvers do not exhibit greater self-improvement"
[^c9]: arxiv-2512-02304 — "cross-family verification provides the greatest potential benefits"
