---
description: "Injecting decaying noise into a continuous latent reasoning trajectory to branch it into K paths, then gating the answer on their agreement, cuts error rates from 40-70% to under 15%."
aliases: ["NoisyCoconut", "counterfactual consensus", "noise-perturbed path agreement", "latent-space self-consistency"]
sources: ["jerge-2026"]
---
# Noisy-latent path agreement

> Do not sample new token sequences to check whether a model's answer is
> stable — perturb its continuous latent reasoning state instead, and read
> disagreement among the resulting paths as the signal to abstain.

## Definition / Mechanism

Jerge and Evans (2026) build on Coconut-style continuous
latent reasoning (a model that feeds its own hidden state back as the next
input embedding instead of emitting intermediate tokens). NoisyCoconut
injects a random noise pattern, decaying exponentially and adapted to
trajectory properties, into the hidden-state trajectory at the first latent
step, branching one reasoning process into K independent latent paths from
a common initial state. "NoisyCoconut injects controlled noise into latent
trajectories to generate counterfactual reasoning paths. This enables
[[abstention|selective prediction]] for latent-space methods."[^c1]

The K resulting outputs are aggregated into a consensus answer or an
abstention, gated on how many of the K paths agree (plurality ≥2/5 through
unanimous 5/5 in the reported experiments). This is presented as an
extension of token-space self-consistency to continuous representations:
"measuring agreement among these paths, analogous to how self-consistency
measures agreement across sampled token sequences, we obtain a confidence
signal directly from continuous representations."[^c2]

Across five LLMs and three reasoning benchmarks, stricter agreement
thresholds trade coverage for accuracy monotonically: "As the threshold
increases from a plurality (≥2/5 agreement) through majority requirements
(≥3/5) to unanimous agreement (≥5/5), the [[calibration|reliability]] improves... unanimous
agreement among five noise-perturbed reasoning paths reduces error rates
from 40-70% to below 15%, enabling models to exceed 95% accuracy on
mathematical reasoning tasks through selective abstention."[^c3]

On GSM8K specifically, no baseline model exceeds 75% accuracy, but at the
unanimous threshold every tested model exceeds 90%; DeepSeek-Qwen moves
from 62.0% baseline accuracy to 95.2% at unanimous agreement while
retaining 31.4% coverage.[^c4]

## Why it matters

On stall 2 (selection) and the abstention decision it feeds, this is a
concrete, measured confidence signal an agent can compute for latent
reasoning models without retraining or sampling new token sequences: the
agreement level among noise-perturbed latent paths is a stopping/abstention
gate whose operating point (plurality through unanimous) trades coverage
for reliability in a reported, monotone way, giving a practitioner an
explicit knob rather than a single threshold.

## Limits

The claim rests on Coconut-style architectures that already support
feeding hidden states back as input — it does not apply to standard
token-space generation without that latent-reasoning capability. Noise
scale was tuned per the model's own accuracy-vs-noise curve (σ₀ = 0.2,
chosen from a fit with R² ≥ 0.94), so the operating point is not
architecture-free; whether the same noise scale and K = 5 path count
transfer to models or tasks outside the five LLMs and three benchmarks
tested is untested.[^c5]

## Related

[[abstention]] · [[trajectory-uncertainty-quantification]] · [[semantic-entropy]] · [[black-box-correctness-ceiling]]

[^c1]: jerge-2026 — "NoisyCoconut injects controlled noise into latent trajectories to generate counterfactual reasoning paths. This enables selective prediction for latent-space methods,"
[^c2]: jerge-2026
[^c3]: jerge-2026 — "As the threshold increases from a plurality (≥ 2/5 agreement) through majority requirements (≥ 3/5) to unanimous agreement (≥ 5/5), the reliability improves"
[^c4]: jerge-2026 — "On GSM8K, no baseline model exceeds 75% accuracy, yet at the unanimous (5/5) agreement threshold, all models exceed 90% accuracy, with coverage ranging from 31.1% (Llama3.1-8B) to 53.2% (gpt-oss-20B). The largest accuracy improvement is observed for DeepSeek-Qwen, which improves from 62.0% accuracy at the baseline to 95.2% at unanimous agreement, while maintaining 31.4% coverage."
[^c5]: jerge-2026
