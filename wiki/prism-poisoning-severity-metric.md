---
description: "A continuous, five-claim-type-weighted metric for how much of a deep-research report's reasoning weight has been compromised by adversarial evidence, replacing binary attack-success rate."
aliases: ["PRISM", "Poisoning Report Impact Severity Metric"]
sources: ["pan-2026"]
---
# PRISM (Poisoning Report Impact Severity Metric)

> Whether a poisoned claim appears in a report at all is a binary that
> misses the question that matters for asking — how much of the report's
> own reasoning now rests on it.

## Definition / Mechanism

PRISM answers whether what a deep-research agent returns is still, in
aggregate, a genuine constraint or has been compromised: "Binary ASR is too
coarse for long-form poisoning: it records whether a claim appears in the
report, but not how much of the reasoning has been distorted. PRISM
replaces binary success with a continuous weighted score over five claim
types ordered by cognitive influence on reader belief, capturing coverage
and severity of contamination."[^c1]

The five types — factual, prescriptive, evaluative, causal, framing — carry
increasing weights (4 to 8) reflecting hypothesized cognitive influence,
with causal and framing claims weighted highest because "causal claims
tend to persist in reasoning even after correction... and framing claims
carry the broadest scope by defining the interpretive lens for all
subsequent content."[^c2]

Computation is a three-stage pipeline: "PRISM is computed in three stages.
We first extract claim sets from both sides (10j claims from P, with 10 per
document, and a fixed nr = 30 claims from R). A [...] evaluator then
assigns each report claim a type ... and judges whether it semantically
matches any claim in P; the matching judgment is binary, with no similarity
threshold. PRISM is the resulting weighted fraction of infected report
claims."[^c3]

The classification step was checked against people: "Appendix C validates
the classification step against human judgment (92.7% overall agreement;
84.5% on causal claims), and Appendix D confirms PRISM is stable across
evaluator models and alternative weighting schemes."[^c4]

## Why it matters

On stall 5 (is what came back actually a constraint?), PRISM is a worked
example of grading an answer's trustworthiness by *type* of claim rather
than by presence/absence: a report can pass a binary success check while
still having its causal and framing claims — the ones with most downstream
influence — disproportionately compromised. It gives a template for a
graded, type-weighted readout of contamination rather than a pass/fail one.

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-security | PRISM | exact |
| agent-security | Poisoning Report Impact Severity Metric | exact — the acronym's expansion |
[^c5]

## Limits

- The five-type weight ordering (4–8) "are a design choice, and [[calibration]]
  against human reader-perception data is left to future work" — the metric
  is stable across alternative weightings, but the weights themselves are
  not independently validated against how much readers are actually
  influenced.[^c6]
- Claim matching is binary with no similarity threshold, so a report claim
  that partially overlaps a poisoned claim is scored the same as one that
  exactly restates it.
- The primary evaluator is one LLM (Gemini-3.1-Flash-Lite); cross-model
  stability is checked but not cross-framework PRISM comparability, which
  the paper says is not directly portable across retrieval architectures.

## Related

[[forge-trajectory-hijacking]] · [[root-query-anchoring]] · [[surprisal]]

[^c1]: pan-2026 — "Binary ASR is too coarse for long-form poisoning: it records whether a claim appears in the report, but not how much of the reasoning has been distorted. PRISM replaces binary success with a continuous weighted score over five claim types ordered by cognitive influence on reader belief, capturing coverage and severity of contamination."
[^c2]: pan-2026 — "causal claims tend to persist in reasoning even after correction (Lewandowsky et al., 2012), and framing claims carry the broadest scope by defining the interpretive lens for all subsequent content."
[^c3]: pan-2026 — "PRISM is computed in three stages. We first extract claim sets from both sides (10j claims from P, with 10 per document, and a fixed nr = 30 claims from R)."
[^c4]: pan-2026 — "Appendix C validates the classification step against human judgment (92.7% overall agreement; 84.5% on causal claims), and Appendix D confirms PRISM is stable across evaluator models and alternative weighting schemes."
[^c5]: pan-2026 — "we introduce PRISM (Poisoning Report Impact Severity Metric), which weights infected report claims by"
[^c6]: pan-2026 — "this ordering is a design choice, and calibration against human reader-perception data is left to future work"
