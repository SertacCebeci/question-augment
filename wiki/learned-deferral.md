---
description: "Training a classifier to output a third class (deferral) directly, instead of thresholding a binary classifier's confidence after the fact, so ambiguous examples shape the learned boundary."
aliases: ["learned deferral", "TBD class", "bounded decision control", "EvaluatorDPT"]
sources: ["chandrasekaran-2026"]
---
# Learned deferral

> A reject-threshold classifier decides to abstain after it has already
> learned a binary boundary; this trains the deferral boundary itself.

## Definition / Mechanism

Chandrasekaran (2026) contrasts two ways a
classifier can produce a third, deferral outcome. In the standard
reject-threshold design, "a binary classifier first estimates
pθ(y ∈ {YES, NO} | x) and then abstains when confidence, [[entropy]], or margin
fails a threshold. Deferral is therefore an operating rule applied after the
classifier has learned a binary decision boundary." The alternative studied
here makes deferral "part of the supervised decision space": the training
objective includes examples labeled TBD, so the model "can assign
probability mass directly to an insufficient-evidence outcome."[^c1]

A deployment threshold can still be layered on top of the resulting
three-way distribution afterward — the two mechanisms are not exclusive —
but the paper's claim is that a learned TBD class lets "ambiguous or
insufficient contexts... be labeled TBD during training," so the decision
boundary itself is shaped by deferral examples rather than only by the
YES/NO boundary the threshold is later cut against. Related work is named
explicitly: "In many such systems [selective classification, [[abstention|reject-option]]
models], abstention is applied after prediction using confidence
thresholds. Here, the model instead learns a deferral label directly while
still preserving threshold sweeps for operating-point selection."[^c2]

The paper reports one trained instance (EvaluatorDPT, a BERT-base encoder
with a three-class decision head) on a held-out test split of 44,597
examples built from NLI and stance-detection corpora: "Accuracy = 0.8260
and Macro F1 = 0.8252, with per-class F1 of 0.8314 (YES), 0.8486 (NO), and
0.7956 (TBD)," alongside a [[calibration]] error of "ECE = 0.0338 on
validation."[^c3]

## Why it matters

On stall 2, every criterion that scores "ask vs. don't ask" over a
candidate axis ([[mutual-information]], GBS, [[adaptive-submodularity]])
treats the stop/defer decision as a threshold cut on a score computed for
another purpose. This source names the alternative directly: build a
labeled corpus of the cases that should trigger deferral and let them
participate in what the decision boundary looks like, rather than
inferring deferral only from how uncertain the YES/NO call already is.
The paper also motivates the asymmetry a threshold-only view can miss:
"confusing a true TBD case with YES or NO can be more costly than routing a
true YES or NO case to TBD, because over-commitment may trigger an
unsupported action while false deferral usually triggers review."[^c4]

## Limits

- The paper reports the learned-TBD model's own performance; it does not
  run a controlled ablation training a matched binary classifier and
  comparing it against a post-hoc threshold on the same data and
  architecture, so "learned beats thresholded" is the paper's motivating
  claim, not a measured effect size in this extract.
- The training corpus is constructed from SNLI, MultiNLI, and
  SemEval-style rumor/stance material with entailment/contradiction/neutral
  mapped onto YES/NO/TBD — the paper itself says this "should be
  interpreted as a research and evaluation corpus," not "a universal
  production benchmark," and TBD's meaning here (semantic insufficiency)
  is domain-specific to that mapping.
- The auxiliary value and emotion/sentiment channels described as future
  routing signals are disabled for the reported evaluation; no empirical
  claim about them is made in this source.

## Related

[[abstention]] · [[selection-abstention-asymmetry]] · [[post-hoc-abstention]] · [[reversibility]]

[^c1]: chandrasekaran-2026
[^c2]: chandrasekaran-2026 — "In many such systems, abstention is applied after prediction using confidence thresholds. Here, the model instead learns a deferral label directly while still preserving threshold sweeps for operating-point selection."
[^c3]: chandrasekaran-2026 — "On the held-out test split (n=44,597), the model achieves Accuracy = 0.8260 and Macro F1 = 0.8252, with per-class F1 of 0.8314 (YES), 0.8486 (NO), and 0.7956 (TBD). The evaluation record also includes calibration evidence (ECE = 0.0338 on validation)"
[^c4]: chandrasekaran-2026 — "confusing a true TBD case with YES or NO can be more costly than routing a true YES or NO case to TBD, because over-commitment may trigger an unsupported action while false deferral usually triggers review."
