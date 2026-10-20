---
description: "A split-conformal band around a binary classifier's probability, from a squared-error score scaled up near 0.5, with its width set by a held-out quantile instead of ensemble spread."
aliases: ["CCI", "Conformal-Calibrated Interval", "Conformal Calibration Interval", "conformal probability interval"]
sources: ["arxiv-2511-18334"]
---
# Conformal-calibrated interval

> Keep the classifier's probability as it is, and wrap it in a band whose
> width is a held-out quantile of a score. The band comes with a
> finite-sample coverage statement; the spread of the model does not set it.

A fitted classifier gives p = f(x), a probability for the positive class.
The method leaves p alone and puts a band around it. The label is first moved
to a class centre on the probability scale, y' = 0.25 + 0.5·y, so the positive
class sits at 0.75 and the negative class at 0.25. In the paper's words, "This
scaling creates distinct interval centers corresponding to each class."[^c1]

The nonconformity score is a squared error between the centre and p, divided
by a scale σ(p) = 1 + (1 − |p − 0.5|). The scale is largest at p = 0.5 and
falls toward the extremes, since "the predicted probability (p) approaches the
decision threshold at 0.5, where the classifier is least confident."[^c2]
The quantile q̂ is the (1 − α) empirical quantile of the scores on a held-out
calibration set (Eq. 4). For a new input the centre is chosen by predicted
class, "assigning the closest class center to the predicted probability."[^c3]
The interval is then the set of probabilities whose score against that centre
is at most q̂ (Eq. 5). This is the same [[conformal-prediction]] construction
as the set-valued version, applied to a scalar probability and a
hand-chosen score.

Two things follow from the equations, and they are my reading, not the
paper's. First, the paper says the score "penalizes larger deviations in
regions of high uncertainty (near p = 0.5)."[^c4] Dividing by σ makes a
deviation near 0.5 cheaper, not dearer. The band is wider there because the
inversion (c − p)² ≤ q̂·σ(p) admits more values of p when σ is larger, so the
sentence describes the penalty the wrong way round. Second, because the centre
is fixed by predicted class, the band is not built around p̂: p̂ only chooses
the side. Read literally, Eq. 5 puts the band's location on the class and its
width on q̂ and σ. The equations are garbled in the extracted text, so this
should be checked against the appendix proof before it is relied on.

The guarantee is stated as "Assuming that the calibration and test data are
exchangeable,"[^c5] and the band then contains the transformed label with
probability at least 1 − α. The paper's summary is that the method "ensures
valid marginal coverage under exchangeability."[^c6] The object covered is the
class centre y', not the 0/1 label.

## Use as a decision

The band is read as a three-way output. The paper's rule says that "When the
prediction interval overlaps the decision boundary and neither tail shows
strong certainty, the model abstains."[^c7] This is the reject option of
[[abstention]], with the interval rather than a scalar confidence as the gate.

On 117 labelled days from eight homes, averaged over 20 runs, the band
abstains "far less (0.22 vs. 0.73)" than the naive baseline and gives
"much tighter prediction intervals (0.20 vs. 0.60)."[^c8][^c9][^c10] The
accuracy and F1 differences from logistic regression are small against the
run-to-run spread (accuracy 0.72 ± 0.16 against 0.69 ± 0.15), so the gain the
paper claims is mostly in abstention and width, not in the classifier.

The naive baseline takes the mean of a random forest's tree probabilities
and the standard deviation of those probabilities, clipped to [0, 1]; it is
built from "the raw ensemble output from a Random Forest classifier."[^c11]
The paper says it carries no coverage guarantee, since "these intervals do not
provide any formal statistical guarantees of coverage,"[^c12] and that it can
become "overly wide and unreliable when tree predictions are highly variable
or skewed."[^c13] That is the same gap between an ensemble's spread and its
error that [[surrogate-uncertainty-sharpness-for-query-selection]] reports for
acquisition functions.

## Limits

- **Marginal, not conditional.** The guarantee averages over the exchange of
  calibration and test days. The main text reports accuracy, precision, recall,
  F1, abstention and width. It reports no empirical coverage rate, so the
  guarantee is proved, not checked on the 117 days.
- **Exchangeability is assumed, not tested.** The days come from the same eight
  people, one after another for a year. The text does not discuss temporal
  dependence between days; that is the usual way exchangeability fails (my
  inference). See [[conformal-prediction]] for the general limit.
- **The guarantee is about the class centre,** not the UTI label, and the
  equations above suggest the band does not contain p̂ by construction.
- **The baseline comparison is confounded.** The naive band is read from a random
  forest, while CCI calibrates "a pre-trained probabilistic classifier (e.g.,
  logistic regression or neural network)."[^c14] Part of the gap in width and
  abstention may come from the base model rather than from the interval method.
- **Small calibration set.** The text says "all results are averaged over 20
  independent runs"[^c15] and allocates "10% of the entire data for testing, 40%
  of the remaining for calibration."[^c16] That leaves about 40 calibration days
  per run (my arithmetic), so the 0.9 quantile is set by a handful of the largest
  scores.
- **The survey measures readability, not decisions.** The 42 nurses answered
  "two openended questions and six Likert-scale items,"[^c17] and the CCI plots
  "were consistently rated as clear."[^c18] One respondent asked for "Would like
  to see outcomes data,"[^c19] which the study does not supply.
- **Calibration here means a band, not a probability.** The method takes the
  classifier as given and does not check whether p̂ is itself calibrated. See
  [[calibration]] for that separate question.

## Related

- [[conformal-prediction]] — the framework whose quantile and exchangeability assumption this note uses; the change here is the score and the object covered
- [[abstention]] — the reject rule that reads the band and abstains when it straddles the decision boundary
- [[conformal-abstention]] — also thresholds an uncertainty score with a conformal quantile, but for a bound on correctness, not a band around a probability
- [[credible-interval-undercoverage]] — LLM-stated intervals undercover until conformally recalibrated; the same fix applied to a different interval source
- [[surrogate-uncertainty-sharpness-for-query-selection]] — ensemble variance underestimates uncertainty, the failure the naive baseline shares
- [[calibration]] — recalibrating probabilities is a different job from wrapping a probability in a calibrated band

[^c1]: arxiv-2511-18334 — "This scaling creates distinct interval centers corresponding to each class"
[^c2]: arxiv-2511-18334 — "the predicted probability (p) approaches the decision threshold at 0.5, where the classifier is least confident"
[^c3]: arxiv-2511-18334 — "assigning the closest class center to the predicted probability"
[^c4]: arxiv-2511-18334 — "It penalizes larger deviations in regions of high uncertainty (near p = 0.5)"
[^c5]: arxiv-2511-18334 — "Assuming that the calibration and test data are exchangeable"
[^c6]: arxiv-2511-18334 — "ensures valid marginal coverage under exchangeability"
[^c7]: arxiv-2511-18334 — "When the prediction interval overlaps the decision boundary and neither tail shows strong certainty, the model abstains"
[^c8]: arxiv-2511-18334 — "abstaining far less (0.22 vs. 0.73)"
[^c9]: arxiv-2511-18334 — "producing much tighter prediction intervals (0.20 vs. 0.60)"
[^c10]: arxiv-2511-18334 — "Our dataset includes 117 samples from eight participants"
[^c11]: arxiv-2511-18334 — "raw ensemble output from a Random Forest classifier"
[^c12]: arxiv-2511-18334 — "these intervals do not provide any formal statistical guarantees of coverage"
[^c13]: arxiv-2511-18334 — "the constructed intervals may become overly wide and unreliable when tree predictions are highly variable or skewed"
[^c14]: arxiv-2511-18334 — "calibrate a pre-trained probabilistic classifier (e.g., logistic regression or neural network)"
[^c15]: arxiv-2511-18334 — "all results are averaged over 20 independent runs"
[^c16]: arxiv-2511-18334 — "allocating 10% of the entire data for testing, 40% of the remaining for calibration"
[^c17]: arxiv-2511-18334 — "They answered two openended questions and six Likert-scale items"
[^c18]: arxiv-2511-18334 — "the calibrated conformal interval (CCI) plots were consistently rated as clear"
[^c19]: arxiv-2511-18334 — "Would like to see outcomes data"
