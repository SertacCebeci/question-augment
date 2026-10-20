---
description: "Confidence-based abstention that clears risk on background text leaves double-digit residual risk on identity-mentioning text — the same coverage buys unequal safety across subgroups."
aliases: []
sources: ["surana-2026"]
---
# Subgroup abstention gap

> Abstaining on low-confidence predictions is supposed to be a safety net.
> Surana (2026) measures a toxicity classifier where the net
> has holes that line up with which identity group the text mentions.

## Definition / Mechanism

Surana (2026) fine-tunes DistilBERT on Civil Comments under
three training objectives (ERM, reweighted ERM, Group DRO) and applies
confidence-based abstention — retaining the top-$c$ fraction of predictions
by $\max(p, 1-p)$ and computing error on the retained set (a risk–coverage
curve) — per identity subgroup rather than in aggregate. "Confidence-based
deferral helps background content far more than identity-mentioning
content."[^c1]

Under ERM, "on background, ERM drives risk near zero by coverage 0.5. On
the white subgroup, residual risk persists at ≥ 14% at every coverage level
for all three methods." Muslim and gay/lesbian subgroups fall between these
extremes, and "muslim, female, and male gaps close under ERM abstention;
the white gap persists."[^c2]

The mechanism is not abstention alone: it is coupled to the training
objective. Under Group DRO, "the curve rises with deferral because its ECE
of 0.134 structurally decouples confidence from correctness: deferring
low-confidence predictions does not preferentially defer wrong ones. Group
DRO and abstention do not compose."[^c3]

The paper's own summary: "the training-method choice determines which
subgroup receives safe deferral."[^c4]

## Why it matters

[[abstention]] treats the answer/abstain choice as a selection function $g$
over a coverage or risk target, measured as one risk–coverage curve. This
result shows that curve is not one object across a population: the same
coverage level can mean "risk eliminated" for one subgroup and "risk
persists" for another, because the errors that survive the confidence
filter on identity-mentioning text are confidently wrong rather than
genuinely uncertain — so the confidence score itself is not doing the same
job in every subgroup. An abstention-based ask-for-review mechanism
evaluated only on its aggregate risk–coverage curve can look safe while
being unsafe for exactly the content a fairness-motivated deferral policy
exists to protect. See [[calibration-fairness-gap]] for the [[calibration]]
disparity this abstention gap rides on.

## Limits

- One model family (DistilBERT-base) and one dataset (Civil Comments,
  English); the paper states the mechanisms "likely reflect
  training-objective properties rather than architecture, but replication
  on larger models is needed."[^c5]
- Minority subgroups are small (jewish n=83, gay/lesbian n=129, black
  n=146), so the per-subgroup risk-coverage estimates carry wide
  bootstrap CIs.
- The abstention rule tested is coverage-based (retain top-$c$ fraction),
  not the certified-threshold rule of [[abstention]]'s SGR algorithm; the
  two are related but not identical mechanisms, so a risk bound proved for
  one does not transfer to the other.
- The finding is specific to a fixed-label toxicity classifier with ground
  truth available for evaluation; whether it holds for open-ended LLM
  clarification-style deferral, where no such ground truth exists, is this
  wiki's extrapolation, not a measurement in the source.

## Related

[[abstention]] · [[demographic-conditioned-mirage]] · [[calibration-fairness-gap]] · [[clarification-request]]

[^c1]: surana-2026 — "Confidence-based deferral helps background content far more than identity-mentioning content."
[^c2]: surana-2026 — "On background, ERM drives risk near zero by coverage 0.5. On the white subgroup, residual risk persists at ≥ 14% at every coverage level for all three methods."
[^c3]: surana-2026
[^c4]: surana-2026 — "The training-method choice determines which subgroup receives safe deferral."
[^c5]: surana-2026 — "The mechanisms we document likely reflect training-objective properties rather than architecture, but replication on larger models is needed."
