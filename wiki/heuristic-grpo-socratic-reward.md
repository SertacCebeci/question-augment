---
description: "A three-term GRPO reward trains a 7B tutor from direct-answering toward Socratic questioning, but its leakage-suppression term degrades results as a training signal."
aliases: ["HeuristicEdu", "SocraticEdu", "composite heuristic reward", "Rtotal"]
sources: ["wang-2026-beyond"]
---
# Heuristic GRPO Socratic reward

> Score each tutor turn on how much it raises cognitive demand and how much
> curiosity it sustains, train a 7B model against that score with GRPO, and
> a separate penalty meant to stop the model naming the answer turns out to
> fight the other two terms rather than help them.

## Definition / Mechanism

Wang et al. (2026) align Qwen2.5-7B-Instruct toward
[[staged-socratic-hint-policy|Socratic]] tutoring with SFT warm-up on 797 reconstructed dialogues (SocraticEdu)
followed by GRPO under a composite reward with three terms, weighted
α, β, γ: "where α, β, γ ≥ 0 control the relative weight of each component.
Section 7 shows that γ = 0 is optimal in practice."[^c1]

Cognitive depth is turn-to-turn Bloom-level change, judged by a separate
LLM: "A Qwen-turbo judge independently assigns Bloom's Taxonomy levels
b ∈ {1, . . . , 6} (remember → create) to the preceding student query qt−1
and the current model response rt," giving a normalized lift
"bresponse − bquery ∈ [−1, 1]" over 5.[^c2]

Curiosity engagement is a learned surface-cue detector, not a judge:
"we score each tutor turn rt with an Engagement Proxy Model (EPM) that
detects surface cues correlated with child follow-up in our logs, including
rhetorical questions, analogical framing, extreme-value language, and
open-ended hypothesis starters."[^c3]

Directness penalizes only vocabulary the tutor introduces, not vocabulary
the student already used: "We penalize only novel leakage—terms in rt that
were not introduced by the student."[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| LLM training (this paper, pipeline name) | HeuristicEdu | `exact` — the two-phase SFT+GRPO pipeline |
| LLM training (this paper, dataset name) | SocraticEdu | `close` — the 797-trajectory training corpus, not the reward itself |
| LLM training (this paper, §4) | composite heuristic reward / Rtotal | `exact` — the reward function this note describes |

**Not this concept.** SocraticEdu is the training corpus the reward is
applied to, not the reward — kept as an alias here only because the paper
uses it interchangeably with the pipeline name; it names no independently
measured object for this wiki.

## Why it matters

On 30 held-out questions, the trained model shifted measurably from
answering to questioning: "the best GRPO variant improves SE from 30.0% to
63.3% and lowers keyword leakage from 30.0% to 13.3%."[^c5]

The best variant is the one that *drops* the directness term from
training. Adding it back hurts both outcomes it was meant to help: "Adding
Rdir with γ=0.2 reduces SE by 0.200 and raises leakage by 10 percentage
points relative to γ=0. We attribute this to an optimization conflict:
Rdir applies a gradient signal that suppresses high-frequency scientific
vocabulary broadly, which in turn reduces the model's ability to use
precise terminology as scaffolding cues."[^c6]

Scale alone does not substitute for the alignment: "Qwen-72B without
task-specific alignment achieves 0% SE and 96.7% leakage... explicit
optimization against a pedagogical objective is necessary."[^c7]

This separates two things a training-for-asking mechanism usually bundles:
rewarding a question for raising cognitive demand and engaging curiosity,
versus explicitly punishing it for naming the answer. The ablation is
evidence that stacking a content-suppression term onto a behavior-shaping
reward can cancel the behavior it is meant to protect.

## Transfer

| | |
|---|---|
| **In its home field** | GRPO trains against a scalar reward with group-relative advantage estimation and no learned critic, developed for domains with a checkable, verifiable reward signal. |
| **Here** | The reward has no ground truth to check against: cognitive lift is an LLM judge's estimate, engagement is a learned proxy model's score, directness is a rule-based keyword count — three heterogeneous terms summed into one scalar. |
| **What survives** | Group-relative advantage estimation, and the result that RL training beats SFT-only and prompt-engineering on the targeted behavior (SE 0.633 vs 0.500 SFT vs 0.400 PE-GRPO, same 7B [[backbone-of-a-formula|backbone]]). |
| **What does not** | The assumption that adding a constraint term targeting exactly the failure mode you want to suppress is safe — here that term interacts with another reward term and net-degrades both, a failure mode with no analogue in a single-objective verifiable-reward setting. |

## Limits

- SE and CD are scored by an LLM-simulated student and an LLM judge, not
  real children; the authors' own check matches simulated turns to real
  held-out follow-ups at a moderate similarity ("the mean score is
  0.449 ± 0.220, indicating on-topic but non-duplicate behavior"), which
  bounds but does not remove the simulation gap.
- N = 30 test questions: "per-run SE variance of roughly ±0.10, margins
  below 0.10 are treated as indicative" — the headline gaps clear this
  margin, but smaller ablation comparisons sit closer to it.
- One base model (Qwen2.5-7B-Instruct), one language (Chinese), one
  domain (seven elementary-science clusters); the directness-engagement
  conflict is shown at one weighting grid, not derived analytically, so
  its generality across weightings or domains is unmeasured.
- The judge and simulator models (Qwen-turbo, Qwen-plus) are themselves
  unvalidated against independent human raters in the slices read here.

## Related

[[investigative-question-grpo-training]] · [[gated-socratic-scaffolding]] · [[staged-socratic-hint-policy]] · [[socratic-method]]

[^c1]: wang-2026-beyond — "where α, β, γ ≥ 0 control the relative weight of each component. Section 7 shows that γ = 0 is optimal in practice."
[^c2]: wang-2026-beyond
[^c3]: wang-2026-beyond
[^c4]: wang-2026-beyond
[^c5]: wang-2026-beyond — "the best GRPO variant improves SE from 30.0% to 63.3% and lowers keyword leakage from 30.0% to 13.3%."
[^c6]: wang-2026-beyond
[^c7]: wang-2026-beyond — "Qwen-72B without task-specific alignment achieves 0% SE and 96.7% leakage"
