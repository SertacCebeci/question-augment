---
description: "Subgroup ECE minus background ECE exposes calibration disparity that a model's aggregate calibration error and its ranking AUC both hide entirely."
aliases: []
sources: ["surana-2026"]
---
# Calibration-fairness gap

> A classifier can be almost perfectly calibrated overall and still be
> wrong about exactly the subgroup a fairness check cares about.
> Surana (2026) names the diagnostic that catches this.

## Definition / Mechanism

Surana (2026) defines the calibration-fairness gap as
subgroup ECE minus background ECE, computed with 15 equal-width bins and
paired bootstrap 95% CIs (n=1000): "We introduce the calibration-fairness
gap (subgroup ECE minus background ECE)."[^c1]

On a DistilBERT toxicity classifier trained by empirical risk minimisation
on Civil Comments: "ERM achieves overall AUC 0.940, ECE 0.013... Despite
overall ECE 0.013, every identity subgroup has significantly higher ECE
than background (Table 3, all CIs exclude zero). The gap reaches +0.134 on
jewish and +0.087 on gay/lesbian." The paper states this is "a fairness
violation BPSN [ranking-AUC] cannot detect: a prediction of p = 0.85 on
white-mentioning content does not correspond to the same accuracy as
p = 0.85 on background."[^c2]

The gap is not fixed by a fairness-motivated training change: "Reweighted
ERM amplifies the disparity: background ECE rises modestly to 0.025, while
subgroup gaps reach +0.232 on white and +0.230 on black, approximately 3×
ERM's gaps." Group DRO closes it only by uniform failure: "Group DRO
eliminates subgroup disparity (every gap CI crosses zero) but only by
becoming uniformly miscalibrated everywhere (background ECE 0.118)."[^c3]

## Why it matters

[[calibration]] establishes that aggregate calibration is a silent
precondition under every information measure this wiki uses; this metric
shows aggregate calibration can itself be a silent aggregate that hides a
subgroup-level failure invisible to both ECE and to ranking metrics like
BPSN/BNSP AUC. A stopping or [[abstention]] rule that reads confidence as
reliable everywhere because the *overall* ECE is low is reading a number
that does not hold on the content the rule most needs to be right about;
see [[subgroup-abstention-gap]] for the downstream effect on deferral.

## Limits

- Computed with 15 equal-width ECE bins; the paper reports "alternative
  binning would shift absolute ECE values but not the qualitative ordering
  of methods or the significance of calibration-fairness gaps," but this is
  the paper's own claim, not independently checked here.[^c4]
- Small subgroups (jewish n=83, gay/lesbian n=129) carry wide bootstrap
  CIs; the point estimates of the gap for these groups are less certain
  than for larger subgroups (white n=276, female n=566).
- Measured on one classifier family, one dataset, one binary task
  (toxicity); the paper makes no claim the specific gap magnitudes
  transfer to other domains, only that subgroup decomposition of ECE is
  the diagnostic that reveals disparity aggregate ECE conceals.
- The metric presumes a labelled validation sample per subgroup to compute
  ECE at all; it does not apply where no such ground truth exists.

## Related

[[calibration]] · [[subgroup-abstention-gap]] · [[abstention]] · [[semantic-entropy]]

[^c1]: surana-2026 — "We introduce the calibration-fairness gap (subgroup ECE minus background ECE)."
[^c2]: surana-2026 — "ERM achieves overall AUC 0.940, ECE 0.013"
[^c3]: surana-2026
[^c4]: surana-2026 — "Alternative binning would shift absolute ECE values but not the qualitative ordering of methods or the significance of calibration-fairness gaps."
