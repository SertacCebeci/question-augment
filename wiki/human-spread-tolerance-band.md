---
description: "A tolerance band around a reference boundary can be calibrated from how far annotators stray from the rest, giving conformal half-widths that are wider where human disagreement is larger."
aliases: ["human-calibrated tolerance", "conformal human-spread band", "annotator-calibrated tolerance"]
sources: ["doi-10-48550-arxiv-2609-06646"]
---
# Human-spread tolerance band

A boundary task needs a tolerance: a prediction counts as correct when it lies within some distance of the reference. The usual choice is a convention, fixed by the benchmark's authors. This work takes the width from the annotators themselves. For each boundary type, one annotator is held out at a time, and the nonconformity score is the distance between that annotator's boundary and the median of the matched boundaries of the remaining annotators: "we hold out one annotator at a time and compute the nonconformity score r".[^t1] Scores are pooled over events and held-out annotators, and the half-width is the conformal quantile, "the half-width calibrated to cover a" fraction of held-out human boundaries at the chosen level.[^t2]

The result is asymmetric, because the human spread is. At α = 0.1 the band is "wider at offsets, +/-0.727 s, than onsets, +/-0.5 s".[^t3] The band therefore inherits the offset asymmetry from the data rather than imposing one: the metric is "lenient where humans themselves are least certain".[^t4]

Scoring a prediction works in two parts. The band score is the fraction of a prediction's matched boundaries that fall within the half-width of the human median. Predicted events that overlap no human event contribute no boundary to it, so spurious events are penalized elsewhere: "punished by the soft-IoU term instead".[^t5] The band is thus a term in a composite protocol, not a standalone score.

The band also changes what ties mean. Scored alone, it declares "67% of adjacent-tier pairs tied" on synthetic systems of known quality, and the authors argue this is the right behaviour: an evaluation aligned with human ambiguity should refuse "to rank differences smaller than human disagreement".[^t6] When it does decide, it "decides correctly 85% of the time".[^t7] The composite, which averages the soft-IoU and the band, keeps the ranking reliability of the soft-IoU alone.

Calibration was checked along one axis. "calibrating on five annotators and testing on the sixth" gives coverage close to the 0.90 target, "approximately calibrated, with mild" under-coverage at the extremes.[^t8][^t9]

## Limits

- Coverage is marginal. The guarantee holds on average over the pooled residuals, "coverage is marginal", not per video or per annotator.[^t10]
- The residuals are not exchangeable in the sense the method needs: "pooling treats residuals as exchangeable although they cluster within videos", and within annotators and events. Only the annotator axis was verified empirically.[^t11]
- The widths belong to one pool and one protocol: "so their widths should not be interpreted as universal".[^t12]
- A model's band is not a coverage guarantee. "band is a human-calibrated tolerance, not a coverage guarantee", because a model's residuals need not match human ones.[^t13]
- The band needs event boundaries to calibrate on. For continuous dimensional traces, "there the perspectivist argument still applies", but only through other mechanisms.[^t14]
- Transfer beyond laughter is a claim, not a result. "Although we instantiate it on laughter" the authors say the protocol transfers to other multi-rater event segments, and expect "with the tolerances re-calibrated per task".[^t15][^t16]

## Related

- single-reference-evaluation — why the band is calibrated on the annotator spread rather than on one reference annotator.
- [[conformal-prediction]] — the general conformal machinery; the band is one use of it, with human leave-one-out residuals as the calibration data.
- [[structured-annotator-disagreement-on-harm]] — the same logic of rater spread, in harm ratings, where the spread also varies with the item.

[^t1]: doi-10-48550-arxiv-2609-06646 — "we hold out one annotator at a time and compute the nonconformity score r"
[^t2]: doi-10-48550-arxiv-2609-06646 — "the half-width calibrated to cover a"
[^t3]: doi-10-48550-arxiv-2609-06646 — "wider at offsets, +/-0.727 s, than onsets, +/-0.5 s"
[^t4]: doi-10-48550-arxiv-2609-06646 — "lenient where humans themselves are least certain"
[^t5]: doi-10-48550-arxiv-2609-06646 — "punished by the soft-IoU term instead"
[^t6]: doi-10-48550-arxiv-2609-06646 — "to rank differences smaller than human disagreement"
[^t7]: doi-10-48550-arxiv-2609-06646 — "decides correctly 85% of the time"
[^t8]: doi-10-48550-arxiv-2609-06646 — "calibrating on five annotators and testing on the sixth"
[^t9]: doi-10-48550-arxiv-2609-06646 — "approximately calibrated, with mild"
[^t10]: doi-10-48550-arxiv-2609-06646 — "coverage is marginal"
[^t11]: doi-10-48550-arxiv-2609-06646 — "pooling treats residuals as exchangeable although they cluster within videos"
[^t12]: doi-10-48550-arxiv-2609-06646 — "so their widths should not be interpreted as universal"
[^t13]: doi-10-48550-arxiv-2609-06646 — "band is a human-calibrated tolerance, not a coverage guarantee"
[^t14]: doi-10-48550-arxiv-2609-06646 — "there the perspectivist argument still applies"
[^t15]: doi-10-48550-arxiv-2609-06646 — "Although we instantiate it on laughter"
[^t16]: doi-10-48550-arxiv-2609-06646 — "with the tolerances re-calibrated per task"
