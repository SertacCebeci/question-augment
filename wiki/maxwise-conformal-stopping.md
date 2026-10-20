---
description: "Calibrating a halting threshold on the per-trace maximum of a running uncertainty score, using only well-posed traces, bounds early-stopping false positives at alpha in finite samples."
aliases: ["maxwise conformal stopping", "uncertainty keyword early stopping", "conformal early stopping for reasoning"]
sources: ["arxiv-2602-13935"]
---
# Maxwise conformal stopping

A reasoning model that is given an ill-posed query tends to keep generating. The rule studied by Xie et al. halts it when a running uncertainty score crosses a threshold. The threshold is calibrated only on traces from well-posed queries, so the practitioner never has to enumerate the ways a query can be ill-posed.

## Mechanism

**Signal.** Uncertainty keywords (for example "impossible to determine") are found in the visible reasoning trace. They come from comparing traces on 400 well-posed and ill-posed GSM8K pairs.[^c1] The score at prefix length l is the keyword count divided by l.[^c2] It needs only the text, so it works with black-box APIs.

**Calibration.** Each calibration trace is scored at token-bin boundaries. Its maximum over the boundaries is M_i. The threshold is the k-th smallest M_i, with k = ceil((n+1)(1-alpha)). At test time generation stops at the first boundary where the score exceeds that threshold.[^c3]

**Guarantee.** Proposition 2.1: if the test trace's maximum is exchangeable with the calibration maxima, then P(some boundary exceeds the threshold) = P(M_{n+1} > threshold) <= alpha.[^c4] This is a finite-sample, distribution-free bound on halting a well-posed query. Taking the maximum over prefixes removes the need for a multiplicity correction. It is the same move as in [[simultaneous-prefix-risk-certificate]], applied to a stopping time instead of a set of actions.

**Any score will do.** The framework accepts any scalar sequence along the trajectory. The paper swaps in a DEER confidence score and an answer-space entropy and keeps everything else fixed.[^c5] A length-only baseline uses the same quantile construction.[^c6]

**Parametric sibling.** The Renewal rule treats keyword arrivals as a renewal process. It standardises the arrival count and halts when it exceeds a normal quantile, with a Sidak correction for repeated checks.[^c7] The authors call this "a practical approximation rather than an exact guarantee", because the independence assumption fails and the maximum trace length is unknown.[^c8] Only the conformal rule carries a finite-sample guarantee.

## What was measured

- Against an oracle classifier trained on ill-posed examples, the two rules reach slopes of 0.8238 (Renewal) and 0.8532 (Maxwise) in a no-intercept regression of detection power. That is about 82 to 85% of the oracle's power.[^c9] The authors call the oracle a soft bound, since a learned classifier need not be optimal.
- Under identical conformal logic, DEER and entropy signals showed much higher FPR on MiP and MMLU than keywords. The authors read this as brittleness of logit signals under distribution shift.[^c10]

## Limits

- Exchangeability between calibration and test well-posed traces is assumed. The paper tests shift empirically, across domains, but a bound under shift is not proved. The guarantee also covers only the false-positive side. Power is measured, not guaranteed.
- The keyword list comes from math pairs. It may not transfer to domains where models hedge in other words. Appendix tables on scientific reasoning are reported but not examined here.
- The Renewal rule's validity is approximate (see above).
- The oracle is a soft bound. The oracle comparison used only two folds, because some datasets have as few as 52 samples.[^c11]
- The note does not show that the keyword signal is better than logits in general. The measured gap is on the shifted benchmarks named above.

## Related

- [[conformal-prediction]] — the rank-quantile argument used here
- [[simultaneous-prefix-risk-certificate]] — the same maximum-over-candidates trick for actions
- [[sprt]] — sequential testing, the classical alternative the Renewal rule approximates
- [[repeated-significance-testing]] — why the Renewal rule needs a multiplicity correction
- [[persistent-homology-ill-posedness-detection]] — another detector for ill-posed queries
- [[conformal-uncertainty-score-gate]] — conformal gating on an uncertainty score

[^c1]: arxiv-2602-13935 — "This set consists of 400 pairs of"
[^c2]: arxiv-2602-13935 — "u(T ; ℓ) = #{arrivals of keywords in T [1 : ℓ]}/ℓ."
[^c3]: arxiv-2602-13935 — "For a new query T at test-time, we monitor"
[^c4]: arxiv-2602-13935 — "This controls the probability of early stopping on a well-posed query at level α."
[^c5]: arxiv-2602-13935 — "Maxwise conformal framework in Algorithm 1 applies to any scalar-valued sequence of"
[^c6]: arxiv-2602-13935 — "Under exchangeability conditions, this method effectively controls the false positive rate (FPR)"
[^c7]: arxiv-2602-13935 — "we adjust"
[^c8]: arxiv-2602-13935 — "rather than an exact guarantee."
[^c9]: arxiv-2602-13935 — "82-85% of the oracle’s detection power."
[^c10]: arxiv-2602-13935 — "MMLU, compared to our keyword-based Maxwise rule, pointing to the greater brittleness of logits-based"
[^c11]: arxiv-2602-13935 — "We use two folds because some datasets are small, with as few as 52 samples"
