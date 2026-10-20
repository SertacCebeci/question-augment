---
description: "Trains claim-level confidence via DPO on corrected pairs, kept structurally separate from a later token-masked GRPO factuality stage, since a joint reward collapses to overconfidence."
aliases: ["CURE", "claim-Aware Reasoning protocol", "Claim-level Uncertainty-aware REasoning"]
sources: ["arxiv-2604-12046"]
---
# Decoupled claim-level calibration training

> Confidence per claim, not per response — and trained in a different
> stage than correctness, because training both at once teaches the
> model to just say 0.98 every time.

## Definition / Mechanism

Liu & Wang (2026) structure a long-form response into a
`<think>` block that reasons about uncertainty and a `<decompose>` block
that emits atomic, independently-verifiable claims each carrying a
confidence: "the reasoning is then transformed into a structured set of
atomic claims via a decompose stage: {(ci , pi )}iN=1, where each ci is
independently verifiable and pi denotes its confidence. This
representation grounds uncertainty in interpretable, claim-level units,
enabling claim-level localization of uncertainty."[^c1]

Calibrating this confidence is not folded into the same reward as
factual correctness. The authors first tried a single GRPO reward that
adds a Brier-score term for confidence to the correctness term, and it
fails: "the model tends to assign high confidence (often close to 1) to
most generated claims during training... approximately 95% of predicted
confidence scores exceed 0.9, indicating a collapse of the confidence
distribution toward high values regardless of claim correctness."[^c2]
The diagnosed cause is that GRPO computes advantage over whole rollouts,
so "reward differences are mainly determined by content quality (i.e.,
claim correctness), while the intended calibration signal remains weak
[and noisy]."[^c3]

The fix is to train confidence and correctness in separate stages, using
a different optimizer for each. Calibration becomes a preference problem:
given a rollout's claims and their correctness labels, an external LLM
revises only the confidence reasoning and scores — leaving the claims
themselves untouched — to produce a corrected rollout preferred over the
original, and DPO is run on this pair: "We treat yw as preferred over yl
and optimize the model using DPO... Since yw and yl share common claim
content and differ in confidence reasoning and estimates, the preference
signal is cleanly isolated." Only after this does a factuality-only
GRPO stage run, and it protects the calibration just learned by masking
the reward off the confidence tokens: "rewards are applied exclusively
to the tokens corresponding to the semantic content of the claims...
the tokens representing confidence reasoning and numerical confidence
values are masked during advantage assignment."[^c5]

At inference the calibrated per-claim confidence drives selective
prediction: "we apply a confidence threshold τ to retain only the
highly certain claims {ci | pi ≥ τ}," with the retained confidence
scores appended to the answer for the user to see.[^c6]

## Why it matters

On FactBench, decoupled training (DPO calibration then masked-GRPO
factuality) raises AUROC from 0.563 to 0.667 and beats the strongest RL
factuality baseline by "9.4% relative improvement in claim-level factual
accuracy," with similar relative gains of 13.6% on LongFact and 39.9% on
Biography, "accompanied by improved calibration, as reflected by a 16.0%
increase in AUROC on FactBench." The ablation isolates why the
staging matters, not merely the extra reward term: GRPO-only calibration
(no DPO, no decoupling into a preference step) "remains insufficient,"
while DPO-based calibration substantially improves performance even
before the factuality stage is added. The result generalizes across
model families (Llama3.1-8B and Qwen3-4B), and factual recall is
preserved rather than traded away for the accuracy gain.

## Limits

The correctness labels that drive both the DPO preference pairs and the
GRPO reward come from an automated claim verifier (VeriScore) and an
external LLM doing confidence correction, not from ground truth — the
calibration target is only as good as that pipeline. The threshold τ
and the per-claim length penalty ϵ are hand-set (ϵ = 0.6) rather than
learned, and selective prediction trades recall for precision by
dropping low-confidence claims outright rather than hedging their
wording. The method is demonstrated only on biography- and fact-style
long-form generation, where claims decompose cleanly into short,
independently checkable atoms; whether the decomposition holds for
argumentative or open-ended prose is not tested.

## Related

- [[abstention]] — the general reject-option mechanism this claim-level
  threshold instantiates.
- [[calibration]] — the property (confidence tracks correctness) this
  pipeline optimizes for directly.
- [[reliability-aware-dpo]] — another DPO-trained reliability score used
  for training-time selection and inference-time abstention, at the
  response level rather than the claim level.
- [[certainty-weighted-grpo-reward]] — a GRPO reward that also scales by
  the model's own belief certainty, but multiplies it into a single
  reward rather than isolating calibration into a separate stage.
- [[grpo-clarifier-selective-abstention]] — GRPO trained selective
  abstention in a different setting (clarification), a comparison point
  for what GRPO alone can and cannot calibrate.

[^c1]: arxiv-2604-12046
[^c2]: arxiv-2604-12046
[^c3]: arxiv-2604-12046
[^c5]: arxiv-2604-12046 — "rewards are applied exclusively to the tokens corresponding to the semantic content of the claims. Crucially, the tokens representing confidence reasoning and numerical confidence values are masked during advantage assignment"
[^c6]: arxiv-2604-12046
