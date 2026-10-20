---
description: "Perfectly calibrated per-step confidences need not give calibrated trajectory success; pooled calibration can hide horizon-dependent drift, so agent confidence needs per-position reporting."
aliases: ["calibration does not compose", "horizon-stratified calibration", "TC-ECE"]
sources: ["doi-10-48550-arxiv-2609-07395"]
---
# Step calibration does not compose into trajectory calibration

An agent that asks or answers over many steps can be calibrated at each step and still be miscalibrated about whether the whole trajectory will succeed. Lin et al. separate two targets. Step-level calibration requires Pr(Yt=1 | ct=p)=p for a step label Yt. Trajectory-level calibration requires that a reliability estimate R̂(ht) be calibrated at every checkpoint index t separately, over the trajectories that reach t.[^c1]

## Mechanism

**Non-composition.** Take a two-step agent whose steps both depend on the same fair coin. A constant step confidence of 1/2 is perfectly calibrated at each step. The product is 1/4. The true trajectory success is 1/2 if the outcomes are perfectly correlated and 0 if they are anti-correlated.[^c2] For two steps the joint success is p1p2 + ρ·sqrt(p1(1-p1)p2(1-p2)). So the product of marginals is right only at ρ=0. Early errors tend to induce positive correlation, in which case the product underestimates joint success.[^c3]

**Convention dependence.** The counterexample rests on local step labels. If Yt instead means "the prefix still admits a successful continuation", the product identity holds by construction and the anti-correlated branch dissolves. But that label is not observable mid-run, and estimating it is the trajectory-reliability problem itself. Choosing the label trades local observability against composability.[^c4] The result also assumes absorbing failure. Agents that retry or re-plan do not satisfy it.[^c5]

**Pooling hides drift.** The proposed statistic, TC-ECE, pools all (checkpoint, outcome) pairs before binning. It is strictly weaker than per-checkpoint calibration: overconfidence at t=1 can cancel underconfidence at t=4.[^c6] The protocol therefore adds per-step-index strata (the mean ECE and the worst-stratum ECEmax), signed gaps, a calibrated-null for the ECEmax/pooled ratio because binned ECE is biased upward in small strata, and bootstrap resampling of whole trajectories because checkpoints share one outcome.[^c7]

**Measured.** On 954 checkpoints from 300 ReAct trajectories on HotpotQA, the verbalized confidence had a pooled TC-ECE of 0.125. Its profile across normalized progress was overconfident in the opening quartile, underconfident in the middle and overconfident in the closing quartile. The closing quartile's TC-ECE was 0.233, nearly twice the pooled value, and it is where a monitor would act.[^c8] A causal baseline using only the elapsed step index reached TC-ECE 0.046 with AUROC 0.562, so calibration alone is not informativeness.[^c9]

## Limits

- The formal result is a counterexample (existence), not a rate. How often real agents violate composition is measured only in the small HotpotQA illustration.
- The authors call the HotpotQA comparisons descriptive: after Holm adjustment the differences carrying the reading do not survive, and n=300 with three-step horizons could not detect a modest advantage.[^c10]
- Which step-label convention is right is left open; the finding that agent self-confidence does not beat a position-only baseline is one configuration.
- Whether horizon-stratified reporting changes how an agent should decide to ask or stop is my inference; the paper does not test a stopping rule.

## Related

- [[trajectory-uncertainty-quantification]] — which scorer families rank trajectory success; this note is about calibrating them across positions
- [[calibration]] — the single-turn notion that Definition 1 reuses
- [[semantic-entropy]] — one single-turn signal the paper lists as costly to apply to whole trajectories
- [[verbal-confidence-commit-readiness-dissociation]] — stated confidence versus readiness to commit

[^c1]: doi-10-48550-arxiv-2609-07395 — "The order of the quantifiers matters: calibration is required separately for each t, not after pooling"
[^c2]: doi-10-48550-arxiv-2609-07395 — "Multiplying the two confidence scores gives 41 , even though the true trajectory"
[^c3]: doi-10-48550-arxiv-2609-07395 — "Early errors can affect later decisions and induce positive correlations among"
[^c4]: doi-10-48550-arxiv-2609-07395 — "Choosing a"
[^c5]: doi-10-48550-arxiv-2609-07395 — "Agents that retry a failed tool call, re-issue a query, or re-plan after a wrong step do not satisfy"
[^c6]: doi-10-48550-arxiv-2609-07395 — "Within one bin, overconfidence at t = 1 can therefore offset underconfidence at t = 4."
[^c7]: doi-10-48550-arxiv-2609-07395 — "Confidence intervals should therefore"
[^c8]: doi-10-48550-arxiv-2609-07395 — "whose TC-ECE of 0.233"
[^c9]: doi-10-48550-arxiv-2609-07395 — "reaches a TC-ECE of 0.046,"
[^c10]: doi-10-48550-arxiv-2609-07395 — "We therefore report the HotpotQA comparisons as descriptive"
