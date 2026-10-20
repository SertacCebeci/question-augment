---
description: "A fixed conformal rule's deployment behavior (commit, hedge, abstain, error rates) is fixed by its region-by-class table, not by coverage; coverage-matched rules can differ."
aliases: ["operational profile of a conformal rule", "region-class label table", "Calibrate-and-Audit"]
sources: ["arxiv-2602-18045"]
---
# Region-class label table as the operational profile

Coverage says how often the true label lands in the answer set. It does not say how often a deployed rule commits to one answer, hedges, or abstains, nor where its decisive errors fall. Zwart (2026) argues that these deployment quantities are fixed by a different object: the joint table of region and true class for the frozen rule.[^c1]

## The mechanism

Calibration fixes thresholds; the thresholds cut the score space into a finite set of regions. In the binary case a point is labeled by whether each class passes its threshold, giving four regions: singleton-0, hedge, singleton-1, and abstention. The deployed rule is then seen through the pair (region, label).[^c2] Its cell probabilities sum to one, so changing thresholds only moves mass between cells.[^c3]

Any deployment rate (abstention, singleton error, coverage itself) is a 0/1 indicator on a cell, so it is a linear projection of the table. In the paper's words: "estimate the table once, then obtain policy-level KPIs by projection."[^c4]

Because mass is conserved, KPIs are coupled. With probability-normalized scores the two class scores sum to one, which creates a regime boundary at the sum of the two thresholds equal to one: above it hedges can occur and abstentions cannot; below it the reverse; on it, only singletons.[^c5] Thresholds are "mass-reallocation boundaries, not independent class-wise knobs."[^c6] Crossing the boundary changes which outputs are feasible at all, so sweeping calibration settings can produce discontinuous changes in profile.

## What the table decides

If a downstream action uses only the region, the best action in each region minimizes expected loss under that region's label mix. Whether a convention is rational is therefore set by the audited within-region label frequencies, not by marginal coverage.[^c7] The paper adds that coverage-matched settings can give different, even disjoint, cost-ratio pricing envelopes.[^c8]

## Auditing and its guarantee

Calibrate-and-Audit freezes the rule and estimates the table on an independent audit split. For KPIs declared in advance at that one fixed rule, exact Binomial inference applies; sweeps, Pareto views and leave-one-out proxies are planning tools, not simultaneous certification.[^c9]

A companion piece, the Small-Sample Beta Correction, picks the least conservative calibration grid point whose realized coverage meets a calibration-conditional PAC-style request (alpha, delta). In simulation at calibration size 100 and delta 0.10, the violation rate was 0.4075 for nominal split conformal, 0.0004 for a DKWM correction, and 0.0960 for the correction.[^c10]

My inference, not tested in the paper: for question answering, the same view suggests asking not only "is the answer set valid" but "what fraction of questions end in a single answer, a hedge, or a refusal, and how often is a committed answer wrong."

## Limits

- Scope is binary split conformal under exchangeability with one fixed deployed rule; multiclass and distribution shift are outside it.
- The exact guarantees cover only pre-declared KPIs at one fixed rule; the paper itself calls sweeps and Pareto views planning tools.[^c9]
- The four-region geometry rests on probability-normalized scores; other score types are not covered by the regime boundary argument.
- Evidence is simulation plus molecular toxicity and solubility data, not language-model question answering.
- Audit data must be separate from calibration, which costs samples where classes are rare.

## Related

- [[mondrian-conformal-prediction]] — class-conditional thresholds are the same two-threshold setup the table is built on
- [[conformal-set-size-calibration-tradeoff]] — another case where equal coverage hides different set behavior
- [[coverage-gated-abstention-rate]] — an abstention rate that depends on something other than the headline guarantee
- [[time-uniform-conformal-prediction]] — a different route to finite-window guarantees

[^c1]: arxiv-2602-18045 — "Those quantities affect throughput and risk,"
[^c2]: arxiv-2602-18045 — "which under the set inclusion policy πSI correspond to singleton-0, hedge,"
[^c3]: arxiv-2602-18045 — "Because the cells (r, y) form a finite partition, the table sums to one and changing θ reallocates mass across"
[^c4]: arxiv-2602-18045 — "In words: estimate the table once, then obtain policy-level KPIs by projection."
[^c5]: arxiv-2602-18045 — "Hedging regime (τ0 + τ1 > 1): 11 may occur and 00 cannot (singletons + hedges; no abstention)."
[^c6]: arxiv-2602-18045 — "therefore mass-reallocation boundaries, not independent class-wise knobs."
[^c7]: arxiv-2602-18045 — "a region-based action convention is justified by"
[^c8]: arxiv-2602-18045 — "coverage-matched settings can induce different, even disjoint, pricing envelopes because the region composition changes."
[^c9]: arxiv-2602-18045 — "planning tools rather than simultaneous certification statements."
[^c10]: arxiv-2602-18045 — "violation rate is 0.4075 for nominal split conformal, 0.0004 for DKWM, and 0.0960 for SSBC, close to the"
