---
description: "Formalizes an agent's stop-or-continue decision as a POMDP over {ANSWER, ABSTAIN, ACT}; 13 agent systems on 28,000+ tasks abstain late or not at all."
aliases: ["Agentic Abstention", "agentic abstention"]
sources: ["luo-2026"]
---
# Agentic Abstention

> Whether to stop acting is not a single-turn answer-or-abstain choice; it is
> a decision revisited every turn, and the evidence that abstention is
> warranted can arrive only after the agent has already acted.

## Definition / Mechanism

Luo, Wen & Wang (2026) define Agentic Abstention as "the problem
of deciding when an agent should stop acting under uncertainty. Unlike
standard LLM abstention, which is usually evaluated as a single-turn
answer-or-abstain decision, agentic abstention is a sequential decision
problem: an agent can answer, abstain, or gather more information at each
turn, and the need to abstain may only become clear after interacting with
the environment."[^c1]

They formalize it as a POMDP $M=(S,A,O,T,\Omega,R)$ with action space
$A=\{\text{ANSWER}, \text{ABSTAIN}, \text{ACT}\}$: ACT is non-terminal and
returns a new observation, ANSWER and ABSTAIN are terminal, and a
[[clarification-request|clarification request]] to the user is counted as an instance of ABSTAIN. Each
instance carries a binary label $y\in\{0,1\}$ for whether it is
"abstain-warranted" — unsolvable "even after appropriate use of the allowed
actions."[^c2]

Across 13 LLM-as-agent systems and 2 agent scaffolds on more than 28,000
tasks spanning web shopping, terminal execution and QA, "agentic abstention
is very difficult, with most systems achieving less than 50% average
abstention recall," and "all models we test achieve less than 40% average
timely recall" (AbsRec@1 — abstaining at the earliest turn the evidence
supports it, versus AbsRec@K, cumulative recall by turn $K$). The gap is
largest on Environment-based instances, where the instruction looks feasible
until a tool call reveals otherwise (e.g. no matching item in stock).[^c3]

Scaling and reasoning do not close the timely gap: "larger models achieve
higher overall recall, while timely recall changes only slightly," and for
one model tested at multiple reasoning efforts, added reasoning "improves
timely recall but lowers overall recall" — it helps only when the model
abstains at its first opportunity, not once that moment has passed. Over-
abstention on solvable tasks also grows with turn count in the web setting
(up to 34% by turn 10 for one model).[^c4]

## Why it matters

On stall 2, this separates two decisions the wiki's other selection criteria
treat as one: recognizing that no further question or action will help
([[abstention]]'s single-shot reject option) versus recognizing it *in time*,
before spending turns on evidence that will not change the verdict. A
criterion that scores only whether an agent eventually stops (as most static
abstention benchmarks do) misses the timing failure this paper isolates as
the dominant one.

## Transfer

| | |
|---|---|
| Home field | control theory / sequential decision-making: POMDP with a reward function $R$ optimized over a policy |
| Here | an LLM agent choosing ACT/ANSWER/ABSTAIN each turn under partial observability of whether the task is solvable |
| What survives | the state/observation/transition structure, the terminal-vs-non-terminal action split, history-dependent policy $\pi(a_t\mid h_t)$ |
| What does not | reward optimization as the objective — the authors state "although a reward function R is part of the standard formulation, we do not treat reward optimization as the objective in our setting" |

[^c5]

## Limits

- The claim that scaling and reasoning fail to close the timely-abstention
  gap rests on a handful of model families (Qwen3 across four sizes; one
  reasoning-effort sweep on GPT-5.4-mini and Qwen3-235B) — not a controlled
  scaling law, and the authors do not claim it generalizes beyond the models
  tested.
- Abstain-warranted labels are assigned by the benchmark's construction
  procedure (filtered AbstentionBench items plus synthetic WebShop/Terminal-
  Bench perturbations), not by an independent adjudicator; a labeling error
  would inflate or deflate every recall number reported.
- All findings are single-run per task per model; stochastic agent rollouts
  carry unmeasured run-to-run variance.
- The action space collapses "ask for clarification" and "state the task is
  unsolvable" into one ABSTAIN action; the paper's numbers cannot distinguish
  an agent that asks from one that gives up.

## Related

[[abstention]] · [[agentabstain-paired-benchmark]] · [[convolve-context-evolution]] · [[reversibility]]

[^c1]: luo-2026 — "We define Agentic Abstention, the problem of deciding when an agent should stop acting under uncertainty. Unlike standard LLM abstention, which is usually evaluated as a single-turn answer-or-abstain decision, agentic abstention is a sequential decision problem: an agent can answer, abstain, or gather more information at each turn, and the need to abstain may only become clear after interacting with the environment."
[^c2]: luo-2026
[^c3]: luo-2026 — "agentic abstention is very difficult, with most systems achieving less than 50% average abstention recall"
[^c4]: luo-2026 — "larger models achieve higher overall recall, while timely recall changes only slightly"
[^c5]: luo-2026 — "although a reward function R is part of the standard formulation, we do not treat reward optimization as the objective in our setting"
