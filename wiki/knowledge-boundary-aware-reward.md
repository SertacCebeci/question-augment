---
description: "An online per-group solvability indicator flips the ternary abstention reward's sign, and a two-stage curriculum defers it, so RLVR stops collapsing into an abstention trap."
aliases: ["KAR", "KARL", "Knowledge-Boundary-Aware Reward", "Two-Stage RL Training Strategy"]
sources: ["arxiv-2604-22779"]
---
# Knowledge-boundary-aware reward

> The reward for abstaining should not have a fixed sign — it should flip
> with whatever the policy has just shown, in this rollout batch, that it
> does and does not know.

## Definition / Mechanism

Gao, Huang, Luo et al. (2026) first diagnose why a
static ternary reward ($+1$ correct, $0$ abstain, $-1$ wrong) collapses
[[gated-answerability-rule|GRPO]] training into silence. Sampled response
groups split into types by composition (correct-only, abstain-only,
mixed); early in training, groups containing only incorrect and abstention
responses (no correct sample at all) dominate. Because GRPO's advantage is
normalized within each group, any abstention reward above the wrong-answer
reward makes abstaining the locally best move in every such group: "under
group-normalized advantage, any abstention reward rabs > rneg yields a
consistent positive advantage for abstention in these groups. This creates
an overwhelming structural bias early in training, driving the policy into
an irreversible 'abstention trap' before it can explore correct answers."[^c1]

The fix estimates the [[abstention|knowledge boundary]] online instead of
by an offline pre-labelling pass: for each query, sample $G$ responses
before the policy update and set a binary solvability indicator
$I_{solvable}=1$ iff at least one of the $G$ is correct. The reward then
depends on that indicator, not on a fixed sign: solvable queries reward
correct answers and penalize both wrong answers and abstention equally;
unsolvable queries reward abstention and penalize wrong answers, with no
correct-answer case to reward. "$(r_{pos}, r_{abs}, r_{neg}) = (+1,-1,-1)$,
if $I_{solvable}=1$; $(r_{pos}, r_{abs}, r_{neg}) = (N/A,+1,-1)$, if
$I_{solvable}=0$."[^c2]

A two-stage curriculum keeps this reward from triggering the trap it was
built to avoid. Stage I mixes, per training example, a plain binary reward
($+1$ correct, $0$ otherwise) on an $\alpha$ fraction of the data with the
knowledge-boundary reward on the rest: "since both incorrect answers and
abstentions receive zero reward, they yield zero advantage in the GRPO
update, effectively nullifying gradients from groups that contain only
errors or abstentions." — the binary slice is a deliberate
gradient-killer for exactly the groups that would otherwise dominate.[^c3]

Stage II then
switches every example to the knowledge-boundary reward alone, so that
queries the model still cannot solve after Stage I's exploration get
converted from persistent wrong answers into abstentions, without
re-penalizing the queries it has already learned.

## Why it matters

A trained answerer's abstention threshold is only as good as the reward
that shaped it; a reward blind to what the policy currently knows pushes
either toward blind guessing (binary reward) or toward blanket refusal
(static ternary reward, once the abstain-dominated groups take over).
Making the reward's sign track a per-batch, per-query solvability estimate
— and sequencing exploration before calibration so the estimate has
something to estimate from — buys both ends of the trade-off: "it reduces
the hallucination rate by 38.6% for Llama3.1 and 20.3% for Qwen2.5, while
simultaneously improving accuracy by 4.0% and 3.3%, respectively," against
an unaligned prompting baseline, with the gains transferring to three
out-of-distribution QA datasets and two reasoning benchmarks.[^c4]

## Limits

The reward is still a three-state discretization: "our current reward
mechanism is still coarse, as it only distinguishes among three discrete
states: correct, incorrect, and abstention. As a result, sampled groups
that yield uniform rewards produce zero advantage and contribute no
gradient updates," which the paper notes does not extend to long-form or
open-ended generation without a finer scoring signal.[^c5]

The Stage I/II transition point is a fixed, hand-set schedule, not a
signal read off training progress; ablations vary $\alpha$ and rollout
group size $G$ but do not test the interaction of the two hyperparameters
jointly. Evaluated only on two 7–8B model families (Llama-3.1, Qwen2.5)
and short-form QA plus math/reasoning benchmarks — not verified for
free-form or multi-turn abstention, or for group sizes beyond 16.

## Related

[[gate-saturation-collapse]] · [[knowledge-boundary-aware-self-distillation]] · [[abstention]] · [[gated-answerability-rule]] · [[two-stage-abstention-paradigm]]

[^c1]: arxiv-2604-22779 — "under group-normalized advantage, any abstention reward rabs ą rneg yields a consistent positive advantage for abstention in these groups. This creates an overwhelming structural bias early in training, driving the policy into an irreversible “abstention trap” before it can explore correct answers."
[^c2]: arxiv-2604-22779 — "prpos , rabs , rneg q “ p`1, ´1, ´1q, if Isolvable “ 1, rKAR po, a q “ prpos , rabs , rneg q “ pN/A, `1, ´1q, if Isolvable “ 0."
[^c3]: arxiv-2604-22779 — "The binary reward acts as a safeguard: since both incorrect answers and abstentions receive zero reward, they yield zero advantage in the GRPO update, effectively nullifying gradients from groups that contain only errors or abstentions."
[^c4]: arxiv-2604-22779 — "it reduces the hallucination rate by 38.6% for Llama3.1 and 20.3% for Qwen2.5, while simultaneously improving accuracy by 4.0% and 3.3%, respectively."
[^c5]: arxiv-2604-22779 — "our current reward mechanism is still coarse, as it only distinguishes among three discrete states: correct, incorrect, and abstention. As a result, sampled groups that yield uniform rewards produce zero advantage and contribute no gradient updates."
