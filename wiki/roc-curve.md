---
description: "The map of the trade-off between detection and false alarm. The locus of $(P_{FA}, P_D)$ traced as a threshold $\\tau$ is swept over a **scalar detector score**. Peterson,"
aliases: ["receiver operating characteristic", "ROC"]
sources: ["peterson-1954", "green-1966", "fawcett-2006"]
---
# ROC curve

> The map of the trade-off between detection and false alarm.

## Definition

The locus of $(P_{FA}, P_D)$ traced as a threshold $\tau$ is swept over a[^s1][^s2][^s3]
**scalar detector score**. Peterson, Birdsall & Fox (1954) introduced it as the
*receiver operating characteristic* of an optimum receiver; Green & Swets (1966) carried it into psychophysics, where its point is that an observer's
response rate mixes two separable things — sensitivity and where the criterion
sits. In the machine-learning restatement (Fawcett 2006) the axes are false
positive rate and true positive rate, the diagonal $y = x$ "represents the
strategy of randomly guessing a class", and the top-left corner is perfect.

The **area under the curve** (AUC) reduces the whole curve to one scalar: the
probability that a randomly drawn positive is scored above a randomly drawn
negative (Fawcett 2006, §7, after Hanley & McNeil 1982). It is a summary *of*
this object, not this object — see below.

## Known as

| Field | Name there | Relation |
|---|---|---|
| detection theory | receiver operating characteristic | exact — the original name (Peterson et al. 1954) |
| machine learning, medicine | ROC | exact — the abbreviation of the same curve |
| machine learning | AUC, area under the curve | **close, not this concept** — a scalar summary of this object. Many different curves share one AUC, and Fawcett (2006, §7) shows a high-AUC classifier can be *worse* than a low-AUC one in a specific region of ROC space. Curve and area are measurably different quantities; AUC deserves its own note |

## The key point

The curve is a property of the detector **across all thresholds**; which point
on it you occupy is a cost choice. Fawcett (2006, §6, following Provost &
Fawcett 1998) makes the cost explicit: two points in ROC space have equal
expected cost exactly when they lie on an *iso-performance line* of slope

$$m = \frac{c(\mathbf{Y},\mathbf{n})\,p(\mathbf{n})}{c(\mathbf{N},\mathbf{p})\,p(\mathbf{p})}$$

— false-alarm cost times negative prior, over miss cost times positive prior.
Change the costs and the slope turns; the best point slides along the *same*
curve. Two separate decisions:

1. How good is the detector? → the curve
2. Where should it operate? → the cost structure

Because both axes are single-column ratios, the curve does not move when the
class mix changes (Fawcett 2006, §4.2) — only the choice of point on it does.

## Why it matters

This distinction is what the "should I ask" decision needs:

```text
Curve      :  how well does the agent detect uncertainty?
Operating  :  at what level of uncertainty should it interrupt the user?
point
```

The second is purely about costs:

- User time expensive → raise the threshold, ask less
- Wrong design expensive → lower the threshold, ask more

One questioner interrupts rarely, another constantly. *This wiki's reading, not
a result of detection theory:* that difference is **consistent with** a
difference of operating point rather than of quality, so "which one is better"
cannot be settled from interrupt rate alone. Nothing here is measured, and the
reading rests on an assumption stated under Limits.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | a labelled trial — signal-plus-noise or noise — carrying a scalar detector score | an asking episode with no ground-truth label ("did this question need asking") and no scalar uncertainty score |
| Threshold $\tau$ | a scalar cut on the score, swept from $+\infty$ to $-\infty$ to trace the curve | an implicit interrupt policy — not a number anyone can sweep |
| What survives | the separation of discriminative power (the curve) from the cost-chosen operating point (Fawcett 2006, §6), and the fact that moving the threshold trades misses against false alarms rather than improving both | |
| What does not | AUC as a measurable quantity, any ordering of two questioners by curve, and every optimality claim — there are no labels, no score, and asking is not a binary detect / don't-detect | |

## Limits

- Needs a scalar score and ground-truth labels. "Did this question need
  asking" has no ground truth outside benchmarks.
- The operating-point reading assumes both questioners lie on the **same**
  curve. Without labels there is no way to check that, so a difference in
  interrupt rate is not evidence that quality is equal — only that quality and
  operating point are not separable from the rate alone.
- AUC summarises across thresholds most of which will never be used, and
  Fawcett (2006, §7) shows the higher-AUC detector can lose in the very region
  you operate in.
- The "should I ask" reading treats asking as binary detection and ignores
  what is asked.
- `peterson-1954` and `green-1966` are cited from their bibliographic records,
  not from full text read here [?]; `fawcett-2006` was read in full.

## Related

[[hypothesis-testing]] · [[neyman-pearson-lemma]] · [[value-of-information]] · [[stopping-rules]]

[^s1]: peterson-1954
[^s2]: green-1966
[^s3]: fawcett-2006
