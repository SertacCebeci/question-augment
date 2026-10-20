---
description: "In long-form answers, replacing low-confidence atomic claims with less specific, higher-confidence versions trades specificity for reliability and beats deleting the claims."
aliases: ["atom-wise selective abstraction", "specificity-for-reliability trade", "claim abstraction"]
sources: ["arxiv-2602-11908"]
---
# Selective abstraction

Whole-answer abstention is all-or-nothing, and in a long answer that discards much that was sound. Selective Abstraction (SA) instead lets the model "trade specificity for reliability by selectively reducing the detail of uncertain content."[^c1] The unit is the atomic claim, not the response, because one response mixes claims of very different confidence, sometimes inside one sentence.[^c2]

## Mechanism

Atom-wise SA runs four stages. The model first generates a response. It then decomposes the response into atomic claims, "short, standalone statements, each expressing a single piece of information." For each atom below a threshold θ, the model writes an abstraction sequence, each step less specific than the last and ending in ⊤, full abstention. It scores every step. For each atom it keeps the most specific abstraction whose confidence clears θ. Finally it reconstructs the text from the kept pieces.[^c3] An example: "born in Chicago" (70%) becomes "born in Illinois" (80%), then "born in the Midwestern US" (90%), then "born in the US" (95%). Raising θ moves along this ladder. The confidence used is verbalized, but any confidence function can be substituted.[^c4]

## Measuring it

Risk is the fraction of atoms not supported by evidence. Coverage is retained information. Information per claim is the relative entropy reduction, I(c) = 1 − log|Ec| / log|E|, where E is the set of entities of the claim's type and Ec those satisfying the predicate, under a uniform prior.[^c5] The two are summarized by a risk-coverage curve and its area (AURC), as in selective prediction. The correctness labeller was an agent checking Wikipedia, with F1 0.93 against humans on 102 sampled claims.[^c6]

## What was measured

Against redaction (deleting uncertain atoms), atom-wise SA lowered AURC by 17.43% on average on FactScore and 13.77% on LongFact.[^c7] The abstract reports gains of up to 27.73% over claim removal across six open-source models. Prompted baselines (Inline, Self-Revision) sit at single operating points with about 10 percentage points more risk at matched coverage. They land nearer the redaction curve than the SA curve, so they behave "closer to atom deletion than to abstraction."[^c8] A calibration algorithm picks θ from a quantile of per-atom critical thresholds so that risk stays at or below a target α + ε with probability 1 − δ. Empirical risk fell close to target over 100 resamples per model and dataset.[^c9]

The mechanism is my reading: an abstraction is a logically weaker claim that the model is more likely to hold true, so the ladder gives each atom a graded fallback. Redaction has only the last rung.

## Limits

- Evaluated only on factual biography-style benchmarks (FactScore, LongFact-Objects), where risk and information can be defined. The authors say the framework applies more widely but non-factual text has no clean information measure.[^c10]
- The information measure assumes uniform priors within entity sets, which real entities do not follow. Coverage is a proxy.
- Correctness labels come from Wikipedia lookup. Claims with no evidence count as wrong.
- Confidence is mostly verbalized. How much the gain depends on that signal's quality was not isolated here.
- The Inline and Self-Revision baselines are single points, so no AURC comparison with them exists.
- The risk-coverage gain does not show that users find the abstracted text more useful.

## Related

- [[post-hoc-abstention]] — another abstention failure mode, at the action level rather than the claim level
- [[conformal-abstention]] — the calibrated-threshold guarantee in the same family as SA's threshold selection
- [[compression-aware-abstention]] — abstention shaped by what a shorter output keeps

[^c1]: arxiv-2602-11908 — "trade specificity for reliability by selectively reducing the detail of uncertain content"
[^c2]: arxiv-2602-11908 — "Long responses often contain"
[^c3]: arxiv-2602-11908 — "which are short, standalone statements, each expressing a single piece of information"
[^c4]: arxiv-2602-11908 — "However, our method can be used"
[^c5]: arxiv-2602-11908 — "We adopt an information-theoretic perspective and measure the uncertainty associated with each set by comput-"
[^c6]: arxiv-2602-11908 — "yielding an overall F1"
[^c7]: arxiv-2602-11908 — "the average improvement in AURC across models is 17.43%"
[^c8]: arxiv-2602-11908 — "closer to atom deletion than to abstraction"
[^c9]: arxiv-2602-11908 — "Figure 4 shows that the algorithm balances"
[^c10]: arxiv-2602-11908 — "This choice reflects an evaluation constraint rather than a limitation of the proposed method."
