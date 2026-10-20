---
description: "A two-stage gate — screen a confidence signal's response validity with three contingency-table indices before computing any calibration or abstention metric from it."
aliases: ["validity screen", "VRS Table", "Stage A screening", "L Fp RBS protocol"]
sources: ["arxiv-2604-17714"]
---
# Validity-screening protocol

> Before asking whether a confidence signal is well calibrated, ask whether
> it carries any item-level signal at all — a question with its own test,
> borrowed from clinical psychometrics' validity scales.

## Definition / Mechanism

Cacioli (2026e) transfers the ordered validity-screening
sequence that the MMPI-3 and PAI run before interpreting a clinical profile
into a two-stage architecture for any benchmark that pairs a correctness
label with a confidence judgement.

"Stage A: Validity Screening. Is the confidence signal non-degenerate and
item-informative? Compute validity indices. Apply tiered thresholds. Report
the VRS Table."
[^c1]

Only a signal that clears Stage A proceeds to Stage B, where ordinary
substantive metrics — meta-d'/M-ratio, ECE, Type-2 AUROC, [[abstention]] or
risk-coverage curves — are computed.

"Stage A is not optional. No confidence analysis is interpretable without
it."
[^c2]

The screen needs only a 2x2 contingency table built from N items' binary
correctness and a binarised high/low confidence judgement (a = correct+high,
b = incorrect+high, c = correct+low, d = incorrect+low). Three indices,
borrowed one-for-one from named clinical validity scales, decompose the
table into separately actionable failure modes. Blanket confidence:

"L = b / (b + d) = P(high confidence | incorrect). Under-reporting:
maintaining confidence despite errors."
[^c3]

Blanket withdrawal:

"Fp = c / (a + c) = P(low confidence | correct). Over-reporting: assigning
low confidence to correct answers."
[^c4]

Directional inversion:

"RBS = Fp - (1 - L). Inverted monitoring: low confidence on correct items
exceeds low confidence on incorrect items."
[^c5]

A structural indicator (TRIN, fixed-responding rate) and a diagnostic
statistic (the item-level point-biserial r(confidence, correct)) are
reported but do not independently trigger a verdict.

Six ordered steps against fixed, logically derived thresholds (Fp >= 0.50,
L >= 0.95, RBS > 0) sort a model into one of three tiers. Invalid:

"Clear threshold violation with narrow confidence interval. The confidence
signal is uninformative. Do not interpret substantive metrics."
[^c6]

Indeterminate, when the point estimate crosses a threshold but its
confidence interval does not; or Valid:

"No threshold violations. CIs do not include threshold values. Proceed to
Stage B."
[^c7]

The Indeterminate tier is load-bearing: a two-way Invalid/Valid split forces
a premature call on threshold-straddling cases, so the protocol reports the
instability itself as information rather than resolving it.

The construct transfers. Run on an independent published dataset, the
frozen screen recovered the same structure:

"11 models across 10 benchmarks … One model (Qwen 1.5-7B-chat) was
classified Invalid (L = .990, AUROC = .503). All 10 remaining models were
classified Valid (mean AUROC = .624). The per-model-dataset correlation
between L and AUROC was .894."
[^c8]

Probe format changes the verdict, not the construct: on the same 20 models,
three classified Invalid under a binary KEEP/WITHDRAW probe reclassified as
Valid under verbalized 0–100 confidence, because

"the binary probe is the harder test. A model that passes the binary
KEEP/WITHDRAW screen will pass the verbalized confidence screen. The
reverse is not true."
[^c9]

## Why it matters

A discrimination metric like AUROC cannot distinguish blanket confidence,
blanket withdrawal, random responding and directional inversion — all four
can sit at AUROC = 0.50, yet each calls for a different fix. The protocol
replaces "is this confidence signal good?" with a prior, cheaper question —
"is this confidence signal interpretable at all?" — and refuses to let a
degenerate signal's downstream metrics (calibration curves that fit noise,
selective-prediction gains that cannot exist) be reported as if they were
informative.

## Limits

Validity here means response validity — item-level dependence on
correctness — never [[calibration]], metacognitive sensitivity, or an
optimal abstention policy; passing says nothing about those, which remain
Stage B questions. The fixed thresholds come from one 20-model, 524-item
derivation battery and one companion benchmark; independent confirmation is
flagged as still needed. Binarising a continuous confidence score loses
ordinal information, and the tier a model receives is a property of the
model-probe-task triple, not a stable model trait — the same model can be
Invalid on one probe format and Valid on another. Cross-family threshold
comparison is unvalidated: a training regime that systematically elevates
confidence (RLHF is named as a candidate) can fail a model that is
well-monitored within its own family.

## Related

- [[abstention]]
- [[calibration]]
- [[score-separability]]
- [[conformal-prediction]]
- [[same-model-self-verification-conditional-confidence]]

[^c1]: arxiv-2604-17714 — "Stage A: Validity Screening. Is the confidence signal non-degenerate and item-informative? Compute validity indices. Apply tiered thresholds. Report the VRS Table."
[^c2]: arxiv-2604-17714 — "Stage A is not optional. No confidence analysis is interpretable without it."
[^c3]: arxiv-2604-17714 — "L = b / (b + d) = P(high confidence | incorrect). Under-reporting: maintaining confidence despite errors."
[^c4]: arxiv-2604-17714 — "Fp = c / (a + c) = P(low confidence | correct). Over-reporting: assigning low confidence to correct answers."
[^c5]: arxiv-2604-17714 — "RBS = Fp - (1 - L). Inverted monitoring: low confidence on correct items exceeds low confidence on incorrect items."
[^c6]: arxiv-2604-17714 — "Invalid. Clear threshold violation with narrow confidence interval. The confidence signal is uninformative. Do not interpret substantive metrics. Criteria: Fp >= 0.50 with Wilson CI lower bound above 0.40; L >= 0.95 with Wilson CI lower bound above 0.90; RBS reliably positive (CI excludes zero) with point estimate above 0.05."
[^c7]: arxiv-2604-17714 — "Valid. No threshold violations. CIs do not include threshold values. Proceed to Stage B."
[^c8]: arxiv-2604-17714 — "et al. (2024): 11 models across 10 benchmarks (MMLU, ARC, TruthfulQA, HellaSwag, WinoGrande, GSM8K, among others) with verbalized confidence (0-100), binarised at the median. One model (Qwen 1.5-7B-chat) was classified Invalid (L = .990, AUROC = .503). All 10 remaining models were classified Valid (mean AUROC = .624). The per-model-dataset correlation between L and AUROC was .894 (p < .000001)."
[^c9]: arxiv-2604-17714 — "Third, the binary probe is the harder test. A model that passes the binary KEEP/WITHDRAW screen will pass the verbalized confidence screen. The reverse is not true."
