---
description: "Trains which tool to call, page to open, or answer to give next with on-policy RL (DAPO, token-masked) and a hand-weighted reward over correctness, retrieval rank, and trajectory discipline."
aliases: ["WikiResearcher-9B", "SearchWiki navigation policy"]
sources: ["singh-2026"]
---
# WikiResearcher-9B RL navigation policy

> The next tool call, page open, or backtrack is not scored by an
> information-theoretic criterion at all — it is whatever a hand-weighted,
> hand-calibrated reward taught the policy to prefer.

## Definition / Mechanism

WikiResearcher-9B (Qwen3.5-9B base) is trained on-policy over live
[[searchwiki-hierarchical-corpus|SearchWiki]] wiki environments with the
DAPO objective (Yu et al. 2025): for each training query, 8 multi-turn
trajectories are sampled and scored, and group-relative advantages replace
a learned value function. Retrieved Token Masking restricts gradient
updates to model-generated tokens — planning, tool calls, and the final
answer — never to the retrieved page text appended to the context, so the
policy is not trained to imitate what it reads.[^c1]

The scalar reward is a weighted sum of three components: answer correctness
(LLM-as-judge), retrieval quality (Read-F1 and page/document rank/NDCG),
and structural rewards for format compliance, discovery-phase heuristics
and parallel-tool use, with penalties for excess turns, duplicate calls, or
answering without using a tool; a rollout that is truncated by the context
or turn budget receives a hard zero regardless of its other components.[^c2]

The weighting is not derived from a criterion — it was calibrated against
observed failure modes: "guessing, retrieval alone incentivizes reading
without answering, and structural shaping alone encourages busywork" if any
one term is used alone.[^c3]

## Why it matters

This is a trained alternative to an explicit selection criterion
([[value-of-information]], [[adaptive-submodularity]]) for stall 2: instead
of computing which axis to query next from a stated objective, the policy
learns which tool/node to visit next from reward-shaped trajectories.
WikiResearcher-9B "leads at 71.35±0.73" on the official ViDoRe v3
LLM-judge accuracy across eight domains, ahead of same-size untrained and
several larger baselines run under the identical harness.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | DAPO/GRPO-family on-policy RL for LLM agents: group-relative advantage estimation and a clipped surrogate objective, developed for domains with a checkable terminal reward. |
| **Here** | Choosing the next tool call, page, or backtrack during multi-turn information seeking — the "which axis first" decision on stall 2. |
| **What survives** | Group-relative advantage estimation and token-masked gradients (train only on generated tokens, not retrieved text) as a stable recipe for long multi-turn trajectories; the two-stage schedule (full reward, then answer-only gradients) that the paper reports is needed to prevent trajectory collapse. |
| **What does not** | Any information-theoretic guarantee. The reward is a hand-weighted sum calibrated against observed failure modes, not a computed quantity like EIG or VoI — nothing in singh-2026 shows the learned policy approximates either, only that it beats untrained and larger baselines on this harness's accuracy and retrieval metrics. |

## Limits

- The reward weights and the two-stage schedule are calibrated on singh-2026's own eight ViDoRe v3 domains and one architecture (Qwen3.5-9B); the paper reports out-of-domain transfer to FinanceBench and three memory benchmarks under the same harness, but not whether the weighting itself would need recalibration for a differently-shaped corpus.
- The correctness component depends on a single external LLM judge (GPT-OSS-120B); no inter-judge agreement is reported, so the reward signal quality rests on that one judge's [[calibration|reliability]].
- No ablation isolates the reward-hacking claim itself (that correctness-only or retrieval-only rewards produce the described failure modes) with a quantified trial; it is reported as the design rationale, not as a controlled comparison in the results tables read for this note.

## Related

[[searchwiki-hierarchical-corpus]] · [[investigative-question-grpo-training]] · [[value-of-information]] · [[adaptive-submodularity]]

[^c1]: singh-2026 — "Gradient updates are restricted exclusively to model-generated tokens (planning, tool calls,"
[^c2]: singh-2026 — "The scalar reward combines answer quality, retrieval quality, and trajectory discipline in"
[^c3]: singh-2026 — "guessing, retrieval alone incentivizes reading without answering, and structural shaping alone encourages busywork (Ng, Harada, and Russell 1999; Amodei et al. 2016;"
[^c4]: singh-2026 — "WikiResearcher-9B outperforms other baselines on endto-end QA accuracy: We report the per-split QA accuracy under the official ViDoRe LLM-as-judge prompt (Loison et al. 2026) (judge model: GPT-OSS-120B) in Table 2. WikiResearcher-9B leads at 71.35±0.73, ahead of"
