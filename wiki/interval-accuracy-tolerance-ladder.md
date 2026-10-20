---
description: "For numeric answers, the share of predictions within k units of the truth, reported at several k, separates near-exact hits from right-period hits, and ignores how far misses fall."
aliases: ["interval accuracy", "IA_k", "within-k accuracy", "tolerance-band hit rate"]
sources: ["arxiv-2512-21337"]
---
# Interval accuracy at a tolerance ladder

Score a numeric answer as correct when it lies within k units of the true value, then report that hit rate for several values of k. The measure is defined in the work as "Interval Accuracy: IAk," the fraction of test items with an absolute error at most k.[^i2] Read as a ladder, the rungs are different questions asked of the same predictor. For the construction-year task the rungs are k = 5, 20, 50 and 100 years.[^i1]

## Mechanism

Each rung is a binary hit per item, averaged over the test set. A rung with a small k asks whether the answer is nearly exact; a rung with a large k asks whether it lands in the right period. The authors give the two readings directly: "IA20 approximates" getting the right architectural period, while "IA5 rewards near exact dating."[^i1]

The ladder is used alongside a mean absolute error. The work reports "Interval Accuracy within" a band next to MAE, so the tolerance band and the average error are read together.[^i4] Because the rungs are bands, a model can score high on IA100 and low on IA5 with no contradiction: its errors are mostly under a century, but few are under five years.

The task is framed as ordinal rather than categorical: the authors "cast the problem as ordinal regression rather than hard classification," so a prediction 20 years off counts as a near miss on the scale, not as a wrong class.[^i3] The ladder gives that near-miss notion a concrete form. The fine rung is also the one used to compute the popularity gap in popularity-stratified-accuracy-gap.

The same idea transfers to any numeric target with a natural unit: pick rungs in that unit, state what each rung certifies, and report the hit fraction at each. What survives the transfer is the banding and the per-rung reading. What does not is the particular rung values, which the work chose for a span of 1001 to 2024.

## Limits

- A hit rate records only whether an error is inside the band. How far the misses fall is invisible to it. Two predictors with the same IA5 can have very different MAE, and this note does not establish which of the two should rank models; the work reports both and does not argue for one (my reading).
- The rung values are the authors' choice. Nothing in the text shows that 5, 20, 50 and 100 years match any user's notion of a good answer, and the band is in absolute years, so it is not scale-free (my inference).
- The ordinal framing is cited to prior work and is not, in the text I read, compared against a classifier scored with the same tolerance bands. The claim that ordinal framing helps the near-miss rungs is therefore the authors' comparison, not a controlled test here.
- Bands assume the error is roughly symmetric around the truth. A skewed predictor, such as one that dates everything too late, can hit a band while being systematically wrong; the measure does not show the sign of the error.
- The metric is defined on one dataset with one target. Its behaviour on heavy-tailed targets, where the rungs are crossed by a few large misses, is not examined.

## Related

- popularity-stratified-accuracy-gap — the fine rung computed inside each popularity bin
- [[exact-match-versus-weighted-agreement]] — another way to credit near misses on an ordinal scale, by distance-weighted agreement instead of a hit band

[^i1]: arxiv-2512-21337 — "IA5 rewards near exact dating."
[^i2]: arxiv-2512-21337 — "Interval Accuracy: IAk"
[^i3]: arxiv-2512-21337 — "we cast the problem as ordinal regression rather than hard classification"
[^i4]: arxiv-2512-21337 — "Metrics include MAE, Interval Accuracy within"
