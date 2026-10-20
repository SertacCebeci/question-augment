---
description: "A sparse probe over eleven scale-invariant features of a token's per-layer MLP-update trajectory that beats max-softmax confidence at ranking LLM errors for abstention."
aliases: ["layer-wise trajectory probe"]
sources: ["eusebi-2026"]
---
# Trajectory-geometry uncertainty probe

> Confidence is usually read off the final layer. This method reads the
> *path* the answer-token representation took to get there, and uses the
> shape of that path — not just its endpoint — as the uncertainty signal
> that would tell an answerer whether to commit or defer.

## Definition / Mechanism

At each transformer block $\ell$, the MLP sub-layer writes an update vector
$m_\ell(x)$ into the residual stream at the answer position; the partial
sums $s_\ell(x)=\sum_{k\le\ell} m_k(x)$ trace a discrete trajectory through
representation space. Eusebi, Herzog, Liang, Vasek, Mariconti & Cavallaro (2026)
extract eleven scale-invariant geometric descriptors of this trajectory —
grouped as depth allocation (front- vs. back-loaded computation), local
shape (consecutive-update cosine, curvature, agreement with running state),
endpoint alignment (how each layer's state or update relates to the final
direction $\hat s_L$, including a signed *contradictory support* term for
layers that oppose the endpoint), and path efficiency (net displacement
over total path length) — and feed them, interacted with the model's max
softmax probability (MSP), to a sparse elastic-net logistic probe trained
to predict the error indicator.[^c1]

Evaluated under selective [[abstention]] (AURC, area under the risk–coverage
curve) across 9 instruction-tuned LLMs (Qwen, Llama, DeepSeek families,
3B–72B parameters) on five multiple-choice tasks, the probe outperforms
the MSP baseline, with the margin scaling with how miscalibrated MSP
already is on that model — up to 21 AURC points on the worst case
(Llama-3.2-3B on MMLU) and near zero or slightly negative on the
best-calibrated models.[^c2]

Because every feature has a closed-form geometric meaning, the fitted
coefficients are read as locating *where* an error takes shape along
depth — which layers commit early, which contradict the running state,
where the trajectory drifts from its endpoint — rather than only flagging
that an error is likely.[^c3]

## Why it matters

This is a concrete uncertainty estimate that could gate an answerer's
commit-or-defer decision (stall 10): a scalar score, cheaper to compute
than sampling multiple generations, that ranks a single forward pass's
error probability better than the default confidence readout. It answers
"how would the answerer know to ask instead of assert" with a signal
computed from information already produced.

## Limits

The claim rests on white-box access to per-layer hidden activations (it
needs the model's own MLP write-vectors, not just logits), on multiple-
choice framing (four-option classification, which the paper uses precisely
to neutralise the [[semantic-entropy|semantic-uncertainty]] component and isolate factual
error), and on a fixed final answer-token position — none of this is shown
to transfer to open-ended generation. The improvement over MSP is uneven
across models: it is large exactly where MSP is already badly miscalibrated
and negligible or slightly negative (DeepSeek-67B, -0.20) where MSP is
already well behaved, so the method does not dominate the baseline
uniformly.[^c4]

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]]

[^c1]: eusebi-2026 — "We extract eleven scale-invariant geometric features, tracing the cumulative path of per-layer MLP updates, and feed them to a sparse linear probe."
[^c2]: eusebi-2026 — "The probe outperforms MSP under selective abstention, with gains scaling with baseline miscalibration up to 21 AURC points."
[^c3]: eusebi-2026 — "each feature has a closed-form geometric meaning, and its coefficients reveal not only whether the model is likely to err but also how, which layers commit prematurely, which contradict the running state, and where trajectories drift away from their endpoint."
[^c4]: eusebi-2026 — "▼0.20"
