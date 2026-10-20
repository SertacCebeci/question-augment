---
description: "An RL reward that pays an embodied agent's ask action only inside a fixed per-task budget, trained from environment feedback rather than a labelled information-gain signal."
aliases: ["social reward", "difficulty-conditioned query budget", "environment-grounded reward shaping"]
sources: ["mi-2026"]
---
# Query-budgeted social reward

> Training an embodied agent to ask, not by labelling which question carries
> the most information, but by rewarding the `ask` action itself — capped by
> a fixed budget — from raw environment feedback.

## Mechanism

REAL (Mi, Ma, Yao et al. 2026) trains a VLM mobile-manipulation policy with
a per-step transition reward computed from the difference between the
current and goal World Graph state, rather than a sparse task-completion
signal.[^c1]

Layered on this state-difference reward, the communicative tool `ask` —
which lets the agent query a simulated user when its own RGB exploration
cannot resolve an ambiguous instruction — is paid only within a fixed
per-task budget of at most three queries.[^c2]

The policy (Qwen3-VL-8B) is optimized with Group Sequence Policy
Optimization from a one-epoch supervised-fine-tuning checkpoint, inside an
environment that withholds oracle object lists and category-search APIs, so
an agent that never explores cannot manufacture [[efe-planning-as-variational-inference|ambiguity]] to spend its
budget on.

## Why it matters

On the interaction-heavy split of REAL-Bench (Simulator-User-Loop), the
reinforcement-learning step raises success from 36.9% (SFT-only checkpoint)
to 56.9%, above the strongest zero-shot commercial VLM baselines the paper
tested.[^c3]

The paper reads the mechanism, not just the number, as the result: the
policy learns when to pause and query the simulated user, attributed to
end-to-end environmental feedback rather than static prompt engineering.[^c4]

## Transfer

| | |
|---|---|
| home field | reinforcement learning for embodied/robotic control (state-difference reward shaping) |
| here | the asking-vs-acting decision: whether to interrupt a manipulation episode with a clarifying question |
| what survives | rewarding an `ask` action against a fixed budget, and grading every step — including the decision to ask — from a state-difference signal rather than end-of-episode success alone |
| what does not | the budget's size ($B_{ask}\le3$) and the World-Graph-difference reward presuppose a simulator with an enumerable, automatically diffable goal state; nothing here says how to reward asking where the goal state cannot be checked automatically |

## Limits

- One paper, one benchmark family (REAL-Bench, 241 tasks, one simulator
  built on GRUtopia/GRScenes), one [[backbone-of-a-formula|backbone]] (Qwen3-VL-8B); the 36.9%→56.9%
  comparison is the authors' own ablation on their own benchmark, not
  replicated by an independent group.
- The budget $B_{ask}\le3$ is a task-design choice, not a measurement of the
  cost of asking; the note makes no claim about the right budget outside
  this benchmark.
- The vision encoder is frozen during reinforcement learning, so the gain is
  attributed to the policy's asking/exploration behaviour rather than to
  improved perception — the paper's own manual failure analysis still finds
  object confusion the largest remaining error class (25 of 53 annotated
  failures).
- The reward requires a simulator-computable goal-state diff (the World
  Graph); nothing in the source shows the mechanism transferring to a domain
  where the goal state cannot be checked automatically, e.g. open-ended
  dialogue with no scorable end state.

## Related

[[clarification-benchmarks]] · [[preference-optimization-for-questions]] · [[question-budgets]] · [[value-of-information]]

[^c1]: mi-2026 — "Instead of sparse task-completion signals, we design a transition reward 𝑟𝑡 = R ( 𝑠𝑡 , 𝑎𝑡 , 𝑠𝑡+1 ) grounded in the WG (Section 4.1)."
[^c2]: mi-2026
[^c3]: mi-2026 — "Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate."
[^c4]: mi-2026 — "The policy learns when to pause and query the simulator-user, showing that social interaction emerges from end-to-end environmental feedback rather than static prompt engineering."
