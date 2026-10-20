---
description: "When a conformity score is built from measurements whose noise drifts over time, scores can lose exchangeability even when the data are exchangeable, voiding the usual coverage guarantee."
aliases: ["non-stationary conformity scores", "shot-dependent scores", "time-varying score noise"]
sources: ["arxiv-2511-18225"]
---
# Time-dependent conformity scores

A conformity score is usually a fixed function S(x, y) of a feature-target pair. The score in the quantum setting studied by this paper is not fixed in that way. A parametrised quantum circuit returns measurement outcomes, not one value, so the score needs the whole sample as an input: the model's output is "a stochastic multiset", and the score takes it as an additional argument.[^c1] That sample is drawn from a distribution that depends on the times at which the shots were taken. If the hardware's noise changes over time, the score inherits the time dependence: "the induced scores are inherently time-dependent if the noise of quantum hardware changes across time."[^c2]

The break in exchangeability follows directly. The data pairs (X_i, Y_i) may be exchangeable, but each augmented observation pairs a data point with the sample drawn at its own shot times, and those samples are not exchangeable once the noise drifts. The paper states the consequence plainly: "This breaks the usual exchangeability assumption."[^c3] Split-conformal coverage depends on the rank of the test score being uniform among the calibration scores, and that rank argument needs exchangeable scores: "Without exchangeable scores, we cannot assert that the rank of the test score is uniformly distributed."[^c4] So the marginal guarantee of [[conformal-prediction]] cannot be asserted for the scores as built.

The paper also notes a way out that it does not take. A score could in principle be written to drop the time dependence, since "a hypothetical score function could be constructed to remove the" dependence on the shots.[^c5] The paper does not pursue this, because the quantum conformity score is designed to use the model's output, and that output carries the time dependence. The paper's answer is to change the procedure, not the score, which is the subject of [[adaptive-conformal-inference]].

The earlier guarantees for the quantum procedure already assumed that the noise processes "remain stationary over time." The paper's contribution is to show that this assumption is doing real work: without it, the scores themselves stop being exchangeable, so the assumption cannot be dropped silently.[^c6]

Transfer. The mechanism is general and my inference, not the paper's: any score computed from samples drawn at different times from a process that drifts can break the same rank argument, whatever the field. Examples would be a judge or model whose serving conditions change between calibration and use. The paper does not test any such case, so this is a question for a reader to check, not a result.

## Limits

- The paper establishes that exchangeability can fail and that the guarantee cannot be asserted in that case. It does not show that a given drift produces a coverage failure of a given size. The authors state that "Confidently attributing the greater deviation of QCP from the target coverage level to non-stationary" noise "would require further experimentation."[^c7]
- The empirical evidence is one day of hardware runs. The paper says the evaluation "does not fully characterise longer-term drift or more structured perturbations."[^c8]
- The break is about the score's dependence on time-indexed samples. It does not say that ordinary calibration sets drawn over time are unsafe; that is a different failure, covered by [[contamination-robust-selective-calibration]], where the calibration set itself admits non-exchangeable items.
- A score that is a deterministic function of the data is unaffected by this mechanism; the break needs the score to read a time-dependent sample.

## Related

- [[conformal-prediction]] — the exchangeability premise this note shows can fail inside the score.
- [[adaptive-conformal-inference]] — the online recalibration the paper uses in response to the drift.
- [[contamination-robust-selective-calibration]] — a different way the calibration set, rather than the score, loses exchangeability.
- [[time-uniform-conformal-prediction]] — anytime validity under i.i.d. data, which this drift breaks.

[^c1]: arxiv-2511-18225 — "obtain a stochastic multiset"
[^c2]: arxiv-2511-18225 — "the induced scores are inherently time-dependent if the noise of quantum hardware changes across time"
[^c3]: arxiv-2511-18225 — "This breaks the usual exchangeability assumption"
[^c4]: arxiv-2511-18225 — "Without exchangeable scores, we cannot assert that the rank of the test score is uniformly distributed"
[^c5]: arxiv-2511-18225 — "a hypothetical score function could be constructed to remove the"
[^c6]: arxiv-2511-18225 — "the theoretical guarantees of QCP require a simplifying assumption: that the noise processes within"
[^c7]: arxiv-2511-18225 — "Confidently attributing the greater deviation of QCP from the target coverage level to non-stationary"
[^c8]: arxiv-2511-18225 — "does not fully characterise longer-term drift or more structured perturbations"
