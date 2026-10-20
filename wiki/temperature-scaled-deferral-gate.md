---
description: "A single temperature fitted on held-out graded data repairs LLM overconfidence, so a confidence threshold can route uncertain answers to a human at a measured coverage and quality."
aliases: ["calibrated human deferral", "temperature scaling plus confidence gate", "CHiL(L)Grader gate"]
sources: ["arxiv-2603-11957"]
---
# Temperature-scaled deferral gate

Instruction-tuned graders are poor judges of their own reliability: "they assign confidence scores near 0.99 even to incorrect predictions, rendering raw confidence unreliable for deferring decisions."[^c1] The gate repairs this in two steps before any routing.

**Step 1, calibrate.** Every candidate grade is scored deterministically by its log-likelihood, and the logits are divided by one learned scalar T. The T is found by sweeping it on a held-out calibration split to minimize expected calibration error (ECE).[^c2] Because one scalar rescales all logits, the argmax does not change, so the grade is unchanged. The paper reports temperature scaling "without altering the model's predictions or QWK."[^c3]

**Step 2, gate.** The calibrated confidence ĉ is compared with a threshold τ. At or above τ the machine grade stands. Below it, the case goes to a human. The paper picks τ by a post-hoc sweep on a fully graded held-out set: "We select the largest τ that satisfies a pre-specified reliability target on the accepted set."[^c4] τ is a deployment dial. On one dataset, raising it from 0.5 to 0.8 cut coverage to 44.6% and lifted quality (QWK) from 0.602 to 0.840, with no retraining.[^c5]

**What was measured.** Temperature scaling cut ECE by 65% on DAMI and 53% on EngSAF, bringing both under 0.1. It cut only 6% on SciEntsBank, whose baseline was already near-calibrated.[^c6] The routing split was visible: accepted DAMI answers reached 0.882 QWK, while rejected ones fell to 0.535 QWK with 3.1 times the MAE.[^c7]

**The right T is not portable.** The optimum sharpened on DAMI (T* = 0.337, so the base model was underconfident there). It smoothed on the other two sets (T* > 1).[^c8] The authors conclude that "fixed temperature cannot generalize across grading domains."[^c8] The gate also recalibrates after each fine-tuning step on the human-corrected cases, because the model that produced the confidences has changed.[^c9]

Why it matters for asking and answering: an answerer's "I am sure" carries no information until it is mapped back to empirical accuracy on cases with known answers. Only then can the decision to ask a human be priced as a coverage-versus-quality trade-off.

## Limits

- Each gate result comes from short-answer grading with a closed set of grades. Nothing here shows the gate works for open-ended generation or free-form question answering.
- ECE below 0.1 was called "acceptable in practice", an external convention and not a proof that the gate is safe.
- The reliability target and the 35–65% coverage range were chosen by the authors on held-out splits. The note does not show the target holds on a shifted test exam. The mid-sequence plateau on SciEntsBank suggests it can drift.
- Temperature scaling fixes only the average miscalibration. It cannot fix a model that is confidently wrong in a way no scalar can reorder (my inference; the paper does not test this).
- The human reviewers are assumed correct. Reviewer error and cost per deferral are not modelled.

## Related

- [[abstention]] — the gate is an abstention rule whose trigger is calibrated confidence.
- [[guarded-threshold]] — a threshold set with a guard on held-out data, as here.
- [[conformal-prediction]] — gives a coverage guarantee, which this heuristic sweep lacks.
- [[confidently-wrong-low-entropy-regime]] — the failure that raw 0.99 confidence exhibits.
- [[selective-answer-finalization]] — the same accept-or-defer structure.

[^c1]: arxiv-2603-11957 — "they assign confidence scores near 0.99 even to incorrect predictions, rendering raw confidence unreliable for deferring decisions"
[^c2]: arxiv-2603-11957 — "The optimal temperature is found by sweeping T ∈ [0.1, 2.0] on"
[^c3]: arxiv-2603-11957 — "without altering the model’s predictions or QWK"
[^c4]: arxiv-2603-11957 — "We select the largest τ that satisfies a pre-specified reliability target"
[^c5]: arxiv-2603-11957 — "raising τ from 0.5 to 0.8 reduces coverage to 44.6%"
[^c6]: arxiv-2603-11957 — "CHiL(L)Grader reduces ECE by 65% on DAMI and 53% on EngSAF"
[^c7]: arxiv-2603-11957 — "the accepted 35% achieve 0.882 QWK, while rejected responses drop to 0.535 QWK with a"
[^c8]: arxiv-2603-11957 — "fixed temperature cannot generalize across grading domains"
[^c9]: arxiv-2603-11957 — "temperature T ∗ is recalibrated on the accepted predictions from the current"
