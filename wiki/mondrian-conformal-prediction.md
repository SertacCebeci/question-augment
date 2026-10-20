---
description: "Splits the conformal calibration set by class label and computes a per-class non-conformity quantile, restoring the coverage guarantee marginal conformal prediction loses on rare classes."
aliases: ["Mondrian conformal prediction", "class-conditional conformal prediction"]
sources: ["singh-2026-cost", "arxiv-2512-14221"]
---
# Mondrian conformal prediction

> Marginal [[conformal-prediction|conformal prediction]] is valid on average — which, under class
> imbalance, means it is valid for the majority class and silently invalid
> for the class that mattered.

## Definition / Mechanism

Standard (marginal) conformal prediction calibrates one non-conformity
quantile $q_{marg}$ over the whole [[calibration]] set, so its $1-\alpha$
coverage guarantee holds only averaged across the population — under
severe imbalance the quantile is dominated by the majority class and the
minority class's own coverage can collapse. [[singh-2026-cost|Singh,
Srikantha & Lakhanpal (2026)]] report this dropping to "as low as below 1%
coverage" on the most extreme class ratios in their benchmark.[^c1]

Mondrian (class-conditional) conformal prediction resolves this by
splitting the calibration set into per-class subsets and calibrating a
separate quantile $q_y$ on each: "Class-conditional (Mondrian) conformal
prediction solves this problem by calculating separate non-conformity
quantiles per class label, guaranteeing 1−𝛼 coverage within every class."[^c2]

A test point's prediction set is then built by comparing its
non-conformity score against its own class's quantile, so the guarantee
$P(Y\in\hat C(X)\mid Y=y)\ge 1-\alpha$ holds *for every class independently*,
not just on average.[^c3]

Across 3,150 experimental runs (15 imbalanced tabular datasets × 7
classifiers × 3 calibration methods × 10 seeds), Mondrian CP raised
minority-class coverage by an average of 61.7 percentage points over
marginal CP ($p<10^{-80}$), at the cost of larger, more often multi-label
prediction sets.[^c4]

| Method | Minority coverage | Avg. set size | [[abstention|Abstention]] rate |
|---|---|---|---|
| Marginal CP | 30.5% | 1.04 | 12.5% |
| Mondrian CP (raw sets) | 92.2% | 1.36 | 38.3% |

[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Conformal prediction (Vovk et al., cited in singh-2026-cost) | Mondrian conformal prediction | exact |
| Applied ML / imbalanced classification (Singh et al. 2026) | class-conditional conformal prediction | exact — same per-class quantile construction |

## Why it matters

On this stall, the coverage a prediction set claims to have is itself a
constraint on $W$ — an asker (or its automated front end) that trusts a
marginal set's stated $1-\alpha$ believes the minority-relevant slice of
$W$ is as constrained as the majority-relevant slice, when under imbalance
it can be almost entirely unconstrained. Mondrian CP makes the coverage
claim honest per class before anything downstream (a threshold, a defer
rule) is allowed to use it.

## Transfer

| | |
|---|---|
| **In its home field** | A finite-sample, distribution-free coverage guarantee for exchangeable calibration/test data, split by a pre-declared category (Mondrian taxonomy) |
| **Here** | Deciding, per class or per subgroup of $W$, whether an answer's stated confidence set can be trusted before it is used to narrow $W$ or trigger a defer decision |
| **What survives** | The finite-sample guarantee, now stated separately for each subgroup, and the diagnosis that a single pooled guarantee hides subgroup-level failure |
| **What does not** | Marginal CP's smaller, more efficient sets — Mondrian sets are on average larger (1.36 vs. 1.04 labels) and trigger far more abstention (38.3% vs. 12.5%), a cost this note's source treats as necessary, not incidental |

## Limits

- The category used to split the calibration set (here, the true class
  label) must be known at calibration time; the method says nothing about
  subgroups discovered only at test time.[^c6]
- Reported on 15 tabular OpenML benchmarks with binary labels; the source
  does not test multi-class or non-tabular data in the slices read for
  this note.
- The 61.7-point figure is an average over datasets, classifiers and
  calibration methods pooled together; per-dataset variance is not
  established here.
- Splitting by group starves small groups. When the group is a missingness
  pattern rather than a class, the split-by-pattern route is costly: the
  paper says the CP-MDA-Exact selection "is infeasible in small-sample
  regimes."[^c7] [[imputation-reweighted-conformal]] keeps one calibration
  pool and corrects it by a pattern-wise likelihood ratio instead.

## Related

[[sequence-level-conformal-prediction]] · [[cost-controlled-abstention]] · [[abstention]] · [[calibration]] · [[imputation-reweighted-conformal]]

[^c1]: singh-2026-cost
[^c2]: singh-2026-cost
[^c3]: singh-2026-cost — "This construction guarantees finite-sample class-conditional validity for both classes independently"
[^c4]: singh-2026-cost
[^c5]: singh-2026-cost
[^c6]: singh-2026-cost — "Mondrian conformal prediction restores coverage for rare classes by splitting 𝐷cal into class-specific subsets"
[^c7]: arxiv-2512-14221 — "is infeasible in small-sample regimes"
