---
description: "An RL rollout gets a teacher's corrective guidance after a wrong student attempt, and reward for post-guidance correctness is decayed so help is never a free path to reward."
aliases: ["SocraticPO", "Socratic Policy Optimization"]
sources: ["liu-2026-socraticpo"]
---
# SocraticPO

> A policy-gradient framework where, mid-rollout, a wrong student attempt
> triggers a teacher's diagnostic natural-language correction before the
> student answers again — and the reward for that later, guided correctness
> is discounted so the policy is trained to need the help less over time.

## Definition / Mechanism

Liu et al. (2026) insert a teacher into an RL
rollout only when the student is wrong: "During rollout, the student first
answers independently; if the answer is incorrect, a teacher diagnoses the
attempt and provides concise corrective guidance, after which the student
continues under the expanded context."[^c1]

The reward for a correct answer reached after guidance is scaled down, and
scales down further the more guidance rounds were needed: "this guidance is
paired with reward decay: correct answers obtained after teacher
intervention only receive decayed rewards, preventing the policy from
treating teacher help as a free path to reward."[^c2]

The framework changes only which trajectories are sampled, not the training
objective, so it plugs into an existing policy-gradient backend
(Reinforce++) and can use a black-box teacher that emits only text, not
logits: "SocraticPO only modifies the rollout process while leaving the
standard expected-reward objective intact... because the teacher provides
only text-level guidance, SocraticPO can leverage stronger black-box
teacher models without requiring access to logits or distribution
matching."[^c3]

On four SciKnowEval reasoning domains, with Qwen3.5-27B as teacher,
SocraticPO raised average accuracy from 0.7388 (Reinforce++) to 0.7624,
best among RL baselines (Reinforce++, GRPO, GSPO) and a self-distillation
baseline (SDPO).[^c4]

An ablation that removes the teacher's diagnosis and substitutes a fixed
retry prompt underperforms full SocraticPO, "especially on Biology and
Material," showing the gain is not from extra attempts alone but from
guidance conditioned on the actual mistake.[^c5]

## Why it matters

This is a training-time answer to "how much should a corrective question
or hint be worth once it changes the answer": the framework treats a
teacher's guidance as an information source whose value to the trainee
depends on when it arrived, not just whether the final answer became
correct — a policy that leans on help retains a lower credit for doing so.

## Limits

The claim rests on one task family (undergraduate scientific reasoning,
SciKnowEval, four domains) and one teacher-student pairing per run; the
paper reports the mechanism is necessary in ablation but not that it
generalizes outside verifiable-answer, single-turn-correction settings
(open-ended tasks with no ground-truth checker are outside the evaluated
scope). The comparison is to RL and self-distillation baselines the
authors chose, not an exhaustive baseline set.

## Related

[[investigative-question-grpo-training]] · [[heuristic-grpo-socratic-reward]]

[^c1]: liu-2026-socraticpo — "During rollout, the student first answers independently; if the answer is incorrect, a teacher diagnoses the attempt and provides concise corrective guidance, after which the student continues under the expanded context."
[^c2]: liu-2026-socraticpo — "this guidance is paired with reward decay: correct answers obtained after teacher intervention only receive decayed rewards, preventing the policy from treating teacher help as a free path to reward."
[^c3]: liu-2026-socraticpo
[^c4]: liu-2026-socraticpo — "With Qwen3.5-27B as the teacher, SocraticPO achieves the best average accuracy, improving from 0.7388 with Reinforce++ to 0.7624."
[^c5]: liu-2026-socraticpo
