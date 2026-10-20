---
description: "A search agent distills a hint-augmented copy of itself, with quadrant-specific KL direction, into its hint-free student to densify a sparse trust/retrieve/abstain reward."
aliases: ["KbSD", "knowledge-boundary aware self-distillation", "quadrant-adaptive self-distillation"]
sources: ["feng-2026"]
---
# Knowledge-boundary aware self-distillation

> Trains the trigger decision — trust parametric memory, retrieve, or abstain
> — by having the same policy teach itself, once with privileged knowledge-
> state hints and once without, so a binary GRPO reward stops being the only
> supervision on *how* the agent reasoned its way to that decision.

## Definition / Mechanism

Feng et al. score each query on two axes computed from the frozen policy's
own behaviour: parametric certainty $\mu(q)$ (the fraction of $N$
hint-free samples matching the ground truth) and a retrieval-quality score
$\hat\rho(q)$. Binarizing both against thresholds sorts every query into one
of four quadrants — Integrated (both reliable), External (retrieval only),
Internal (memory only), Refusal (neither).

The teacher is the same weights conditioned on a privileged prompt (the
quadrant, $\mu$, a stability score, $\hat\rho$) with gradients stopped; the
student sees only the original query and is trained token-by-token to
reproduce the teacher's trajectory. No separate, larger model is trained —
the supervision gap between teacher and student is informational, not one
of capacity: "KbSD constructs a hint-augmented teacher that is
architecturally identical to the student but additionally conditioned"
on the knowledge-boundary signals.[^c1]

Because the four quadrants demand differently shaped target
distributions, the distillation direction is chosen per quadrant: mode-
seeking reverse KL for concentrated Integrated reasoning, mass-covering
forward KL for diverse Refusal patterns, and a closed-form Pareto-optimal
blend of both — no hand-tuned trade-off coefficient — for the mixed
External and Internal quadrants: "reverse KL (mode-seeking) for Quadrant
1's concentrated integration, forward KL (mass-covering) for Quadrant 3's
diverse refusal patterns, and Pareto-optimal bidirectional KL for the
competing precision–coverage trade-off in Quadrants 2 and 4."[^c2]

The distillation loss is added as one term inside a GRPO clipped-objective
training run, alongside the existing sparse outcome reward and a
reference-policy KL penalty.

## Why it matters

Stall 2 is which axis to act on first — here, whether to answer from
memory, issue a search, or refuse. A binary correctness reward only
penalizes the wrong outcome; it says nothing about which of the four
reasoning modes was appropriate or how to reach it. Against KbPO, a prior
sparse-reward baseline sharing the same quadrant taxonomy, adding the dense
distillation supervision reduces the failure rate substantially: on
Qwen2.5-3B "KbSD lowers the average unreliability rate from 64.32 (KbPO)
to 47.60, and on Qwen2.5-7B from 57.99 to 41.18—an absolute reduction of
roughly 17 points in both cases."[^c3]

Unreliability rate is defined as 1 − (F1 + refusal rate), i.e. neither
correct nor honestly refused.

## Transfer

| | |
|---|---|
| **Home field** | Knowledge distillation (Hinton et al. 2015) and on-policy distillation (MiniLLM, GKD): a separately trained, usually larger, teacher supervises a student's own rollouts with a chosen KL direction. |
| **Here** | The "teacher" is the identical policy given privileged, training-only information about its own knowledge state; the KL direction is switched per knowledge-boundary quadrant instead of fixed. |
| **What survives** | The reverse-KL/mode-seeking vs. forward-KL/mass-covering distinction, and the idea of turning a coarse behavioural label into token-level supervision. |
| **What does not** | The capacity gap that classical distillation exploits — this teacher knows more only because it is told more, not because it is a bigger model, so the technique's gain is bounded by how informative the hint is, not by any model-size margin. |

## Limits

The quadrant assignment rests on proxies computed by the model itself —
sampled-response match rate and a retrieval-quality score — against
hand-set thresholds: "The knowledge boundary thresholds are set to
τρ=0.5 and τµ=0.6."[^c4]

A miscalibrated proxy mis-sorts a query into the wrong quadrant before any
distillation happens. Evaluated on one model family at two scales (Qwen2.5
3B/7B), one retriever (E5 over a 2018 Wikipedia dump), and training data
synthesized from two multi-hop QA datasets; comparisons are against a
re-implemented KbPO baseline and other RL agents in the same codebase, not
an independent replication. The scale trend ("the improvement margin
increases with model scale") rests on two data points, not a fitted
scaling law.

## Related

[[savor-calibration-abstention-reward]] · [[calibration-training]] · [[calibration]] · [[abstention]]

[^c1]: feng-2026 — "KbSD constructs a hint-augmented teacher that is architecturally identical to the student but additionally conditioned"
[^c2]: feng-2026
[^c3]: feng-2026 — "KbSD lowers the average unreliability rate from 64.32 (KbPO) to 47.60, and on Qwen2.5-7B from 57.99 to 41.18—an absolute reduction of roughly 17 points in both cases."
[^c4]: feng-2026 — "The knowledge boundary thresholds are set to τρ =0.5 and τµ =0.6."
