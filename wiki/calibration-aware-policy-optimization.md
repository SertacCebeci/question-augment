---
description: "Replaces GRPO's reward-only advantage with an AUC-consistent logistic surrogate plus reference-model noise masking, jointly raising calibration and accuracy in RLVR."
aliases: ["CAPO", "Calibration-Aware Policy Optimization"]
sources: ["arxiv-2604-12632"]
---
# Calibration-Aware Policy Optimization

> Fixing the advantage estimator, not adding a penalty term: reward the
> model for ranking correct above incorrect responses by confidence, not
> only for being right.

## Definition / Mechanism

CAPO (Wang, Lou, Wu, Wen & Zhang, 2026) answers
[[reward-only-advantage-miscalibration]] by replacing GRPO's reward-only
advantage with one built from an AUC-*consistent* pairwise loss. Each
response's advantage becomes a sum, over the opposite-labeled responses
in its group, of the derivative of a logistic surrogate
$\phi_\tau(t)=\log(1+\exp(-t/\tau))$ applied to the perplexity gap between
the two — so a correct response's advantage grows with how much *lower*
confidence (higher perplexity) it has than the incorrect responses it is
paired against, and vice versa. Because $\phi_\tau$ is convex,
differentiable and non-increasing with $\phi_\tau'(0)<0$, optimizing it is
provably aligned with raising AUC, unlike GRPO's implicit linear
surrogate.

A second mechanism denoises this signal. Outcome-only binary rewards
cannot tell a correct answer reached by "spurious reasoning" from one
reached properly, or an incorrect answer that was one small slip from
correct — both inject noisy gradient into the advantage. CAPO uses the
frozen reference (base) model's own perplexity as an untrained proxy for
reasoning quality and masks out the suspect cases: "we exclude correct
responses with reference-model PPL exceeding a threshold ref-high
(likely lucky guesses) and incorrect responses with reference-model PPL
below ref-low (likely near-correct reasoning penalized as failure)."[^c2]
The thresholds are set from the reference model's PPL quartiles, adding
no training cost.

Trained this way, "CAPO-1.5B significantly improves calibration by up to
15% while achieving accuracy comparable to or better than GRPO, and
further boosts accuracy on downstream inference-time scaling tasks by up
to 5%."[^c1]

Thresholding a trained model's confidence to abstain below it traces a
precision–coverage curve. "By simultaneously enhancing calibration and
accuracy, our method achieves a more favorable precision–coverage
trade-off, enabling reliable hallucination mitigation with minimal
abstention."[^c3]

## Why it matters

This is a structural fix, not a heuristic one: it changes what the
advantage is a function of (reward *and* a relative-confidence signal)
rather than adding a regularizer or reward bonus on top of a reward-only
objective that a heuristic can only partially counteract. The
denoising step generalizes beyond this paper — a frozen reference
model's own perplexity is a free, already-calibrated signal for
which training examples are safe to trust, usable anywhere a binary
outcome reward risks reinforcing lucky or spuriously-penalized
reasoning.

## Limits

Evaluated only on mathematical reasoning (Qwen2.5-Math-1.5B/7B,
DeepScaler training data, six math benchmarks); the authors state:
"This study mainly evaluates the proposed method on mathematical
reasoning benchmarks... Its effectiveness on other reasoning tasks such
as logical puzzles, commonsense reasoning, and open-domain question
answering, remains to be further validated."[^c4]

The AUC surrogate targets *relative* calibration (ranking); it gives no
guarantee on absolute calibration (whether a stated probability matches
the true correctness rate). The masking thresholds are set from
reference-model PPL quartiles on the same data distribution and are not
shown to transfer across domains without re-tuning.

## Related

[[reward-only-advantage-miscalibration]] · [[calibration]] · [[confidence-report-repair]] · [[gate-saturation-collapse]] · Commitment

[^c1]: arxiv-2604-12632 — "CAPO-1.5B significantly improves calibration by up to 15% while achieving accuracy comparable to or better than GRPO, and further boosts accuracy on downstream inference-time scaling tasks by up to 5%."
[^c2]: arxiv-2604-12632 — "we exclude correct responses with reference-model PPL exceeding a threshold ref-high (likely lucky guesses) and incorrect responses with reference-model PPL below ref-low (likely near-correct reasoning penalized as failure)"
[^c3]: arxiv-2604-12632 — "By simultaneously enhancing calibration and accuracy, our method achieves a more favorable precision–coverage trade-off, enabling reliable hallucination mitigation with minimal abstention."
[^c4]: arxiv-2604-12632
