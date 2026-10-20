---
description: "Same-model self-verification beats length-normalized likelihood on ARC-Challenge for several models, but is unreliable on TruthfulQA-MC and often loses to unnormalized sum log-likelihood."
aliases: ["Self-Verify", "conditional confidence signal"]
sources: ["arxiv-2605-02915"]
---
# Same-model self-verification as a conditional confidence signal

> Not a general-purpose uncertainty estimator — a signal whose value
> depends on task type, model family, prompt formulation, and, crucially,
> the baseline it must beat.

## Definition / Mechanism

Phalod (2026) scores a multiple-choice answer two
likelihood-based ways: "LL-AVG, which scores an answer using
length-normalized option log-likelihood, and LL-SUM, which uses the
non-length-normalized sum of option log-probabilities." Same-model
**self-verification** ("Self-Verify") adds one extra call: after the model
predicts under LL-AVG, the same model is prompted to judge whether that
predicted answer is correct, and the judgment is scored as a confidence
signal against the same correctness label — an extra verification pass
compared directly to two one-pass baselines rather than assumed useful on
its own.

Compared against LL-AVG, Self-Verify's gain is sharply conditional. On
ARC-Challenge, "the strongest result appears in Qwen-7B, where Self-Verify
improves AUROC from 0.555 to 0.886 under the default prompt and reduces
AURC from 0.364 to 0.143." On TruthfulQA-MC the same signal reverses
for other models: "TinyLlama-1.1B drops by about 0.19 to 0.20 AUROC
relative to LL-AVG, and DeepSeek-R1-Distill-8B drops by about 0.09 to
0.12." Parameter count does not order the effect: DeepSeek-R1-Distill-8B
is similar in scale to Qwen-7B but consistently weak or harmful, so
"scale alone is therefore insufficient to explain self-verification
reliability within the tested set."[^c4]

Against the stronger, unnormalized baseline the practical claim narrows
further: "in several settings, LL-SUM remains the stronger confidence
signal while requiring only a single scoring pass." A second nuance
survives even where Self-Verify ranks better: "in some settings,
Self-Verify improves AUROC or AURC while worsening Brier score or ECE
relative to LL-AVG. Better correctness ranking therefore does not imply
better probability calibration."[^c6]

## Why it matters

A practitioner adding a self-check pass to gate abstention cannot assume
it earns its extra inference cost. It must be validated per task (a
reasoning-heavy benchmark like ARC-Challenge behaved differently from a
truthfulness-focused one), per model family (Qwen improved with scale,
DeepSeek-R1-Distill did not), per prompt wording, and against the
cheapest available one-pass baseline (unnormalized sum
log-likelihood, not only the length-normalized one) — otherwise a second
model call can make abstention worse rather than better.

## Limits

- Multiple-choice only: correctness and the confidence label are both
  cleanly defined; the paper states its findings "should not be taken as
  evidence that same-model self-verification will behave identically in
  open-ended generation, tool use, or long-form reasoning tasks." unverified
- Five models across a small number of families (Phi-2, Qwen-1.5B/7B,
  TinyLlama-1.1B, DeepSeek-R1-Distill-8B); not a scale-law or
  family-level claim.
- Baseline set is two likelihood scores only — no semantic-entropy,
  ensemble, or self-consistency comparison.
- Descriptive, not mechanistic: the paper identifies where the signal
  holds and fails without establishing why family or task drives the
  difference.

## Related

- [[sequence-likelihood-confidence]] — the length-normalized likelihood
  signal this work uses as its primary one-pass baseline (LL-AVG) and
  finds an unnormalized variant (LL-SUM) can beat.
- [[abstention]] — the downstream decision a confidence signal like this
  one is meant to gate.
- [[calibration]] — ranking (AUROC/AURC) and calibration (Brier/ECE) can
  move in opposite directions for the same signal here.
- [[roc-curve]] — the ranking metric (AUROC) used to compare signals.
- [[contradiction-gate]] — another same-model, single extra-call check
  used to gate abstention, on a narrower failure mode (input
  contradiction) than general answer correctness.
- [[entropy]] — an alternative intrinsic confidence signal noted as
  untested here.

[^c4]: arxiv-2605-02915 — "Scale alone is therefore insufficient to explain self-verification reliability within the tested set."
[^c6]: arxiv-2605-02915 — "In some settings, Self-Verify improves AUROC or AURC while worsening Brier score or ECE relative to LL-AVG. Better correctness ranking therefore does not imply better probability calibration."
