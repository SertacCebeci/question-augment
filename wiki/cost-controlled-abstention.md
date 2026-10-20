---
description: "Defers to a human exactly when a Mondrian conformal prediction set is not a singleton, and names the review-cost threshold below which that deferral rule beats a tuned point predictor."
aliases: ["cost-controlled abstention", "break-even review-cost threshold"]
sources: ["singh-2026-cost"]
---
# Cost-controlled abstention

> Chow's rule names a cost and thresholds a posterior; this rule names the
> same kind of cost but thresholds a conformal *set's cardinality* instead,
> and then solves for the cost at which deferring stops paying.

## Definition / Mechanism

Singh, Srikantha & Lakhanpal (2026) build the trigger
for human review directly out of a [[mondrian-conformal-prediction|Mondrian
conformal]] prediction set $\hat C(X)$: "Treating both multi-label
ambiguities and empty set outputs as abstention triggers ensures that any
non-singleton prediction (|$\hat C(X)$| ≠ 1) is safely routed to human
expert review."[^c1]

When the set is a singleton the automated label is used at zero cost if
correct, or at a named cost $C_{FP}$ or $C_{FN}$ if not; when it is not a
singleton, deferral costs $C_{rev}$ (an ideal human) or $C_{rev}+\epsilon_{hum}(\cdot)$
(a fallible one).[^c2]

The paper then asks when this rule is worth it at all, relative to a
single Bayes-optimal probability threshold with no deferral option: "We
derive the critical human review cost threshold $C_{rev}^*$ below which
cost-controlled conformal deferral achieves lower total expected decision
cost than uncalibrated Bayes-optimal threshold tuning."[^c3]

Solving $\mathbb{E}[L_{conf}] < \mathbb{E}[L_{point}]$ for $C_{rev}$ gives
the break-even threshold as the automated-error cost the deferral rule
avoids, divided by how often it defers:
$$C_{rev}^{*}=\frac{(1-\pi_1)C_{FP}(FPR_{\tau^*}-FPR_{conf})+\pi_1 C_{FN}(FNR_{\tau^*}-FNR_{conf})}{r_{abs}}$$[^c4]

so that whenever the actual review cost is below this threshold, "routing
set-valued ambiguities to human experts guarantees a net reduction in
expected financial or clinical decision costs."[^c5]

Averaged over the benchmark's 3,150 runs, the cost-controlled Mondrian
rule cut mean per-instance decision cost from 0.340 (Bayes-tuned point
threshold) to 0.021, at a 71.9% abstention rate.[^c6]

## Why it matters

This gives stall 2's "defer or ask" decision a computable break-even point
that does not require naming a utility function up front, the way
[[value-of-information]] does — only the four cost/error-rate quantities
in $C_{rev}^*$, three of which ($FPR_{\tau^*}$, $FNR_{\tau^*}$, $r_{abs}$)
are estimable on a [[calibration]] split before any deferral decision is made.

## Transfer

| | |
|---|---|
| **In its home field** | A cost-sensitive selective-classification rule for one static binary classifier, evaluated on held-out tabular benchmarks |
| **Here** | Deciding, per question or per case, whether to route to a human asker/answerer instead of committing automatically — the same choice [[abstention]] frames, priced by a break-even cost instead of a fixed risk or coverage target |
| **What survives** | The move of naming the abstention trigger as a set property (non-singleton) rather than a confidence threshold, and solving explicitly for the review cost at which deferral pays off rather than assuming it always does |
| **What does not** | The specific formula — it assumes a binary label, a known asymmetric cost matrix $(C_{FP},C_{FN})$, and error rates measured against ground truth on a calibration set, none of which exist for an open-ended, one-off question |

## Limits

- The break-even formula needs $FPR_{\tau^*}, FNR_{\tau^*}, FPR_{conf}, FNR_{conf}$
  and $r_{abs}$ all estimated from a labelled calibration sample; it is not
  computable when ground truth is unavailable, which is the common case
  for the wiki's open-ended questions.[^c7]
- Reported for a fixed cost matrix ($C_{FP}=1, C_{FN}=10$) and a fixed
  error target ($\alpha=0.10$) on binary tabular tasks; the source does not
  establish the formula for multi-class problems or for costs that vary
  by instance.
- The reported cost reduction is an average across 15 datasets, 7
  classifiers and 3 calibration methods; dataset-specific break-even
  values are reported as varying, but the range is not read in the slices
  taken for this note.
- This is this wiki's reading of the abstention trigger as a general
  defer-vs-ask mechanism; the source frames it only as a classification
  deployment rule, not as a model of asking.

## Related

[[abstention]] · [[mondrian-conformal-prediction]] · [[correctable-set]] · [[value-of-information]]

[^c1]: singh-2026-cost
[^c2]: singh-2026-cost
[^c3]: singh-2026-cost
[^c4]: singh-2026-cost — "(1 − 𝜋1 )𝐶FP (FPR𝜏 ∗ − FPRconf ) + 𝜋1 𝐶FN (FNR𝜏 ∗ − FNRconf )"
[^c5]: singh-2026-cost
[^c6]: singh-2026-cost
[^c7]: singh-2026-cost — "Statistical significance across paired model runs is assessed using two-tailed Wilcoxon signed-rank tests (𝑝 < 0.05), with 95% bootstrap confidence intervals computed over 1,000 resamples."
