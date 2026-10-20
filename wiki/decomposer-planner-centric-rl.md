---
description: "Trains a planner policy to emit typed-DAG research plans via staged RL, rewarding plan structure and query decomposition apart from answer synthesis, lifting long-form benchmarks 5.1-8.0 points."
aliases: ["DecomposeR", "structure-aware reward", "planner-centric reinforcement learning", "structure-aware reward modeling"]
sources: ["hussain-2026"]
---
# DecomposeR (planner-centric structure-aware reward)

> A deep-research agent's flat ReAct-style trajectory gives one terminal
> scalar reward to every action, so a weak final answer cannot say which
> sub-question was wrong. DecomposeR makes the plan an explicit, typed,
> separately rewarded object, and trains the policy that decides *which
> sub-questions to ask* apart from the policy that answers them.

## Definition / Mechanism

Hussain, Wu & Lu (2026) replace the flat rollout
$\tau_{flat}=(x,m_1,o_1,\dots,m_T,o_T,y)$, where "a single scalar reward
$R(x,y)$ is propagated through every $m_t$ for policy update," with a
factored one in which a [[planner-dynamic-stopping|planner]] policy $\pi_P$ emits an explicit plan $G$
that an answerer policy $\pi_A$ consumes: "$\tau=(x,G_0,Z,G_1,F,O_{1:K},y)$"
— an initial plan, retrieved search observations, a revised plan, fetched
documents, answerer outputs in topological waves, and the final answer.
The plan is "a typed directed acyclic graph (DAGs), allowing planning to
be made explicit, structured, and rewardable," with search nodes (a query
plus the evidence it should return), aggregate nodes (a synthesis brief),
and exactly one terminal answer node.[^c1]

Training is staged: a planner-RL phase first refines only the plan-emitting
adapter, then an answerer-RL phase refines execution against the fixed
learned plan — "training the two roles sequentially, Planner RL optimises
rewards that depend only on $G_1$ and never on answerer output, so plan
quality is isolated from execution noise." Planning is itself two-turn:
"$G_0$ is generated from $x$ alone," then "the second turn closes the
planning loop with retrieval reality, letting the planner drop ineffective
subqueries, add new subqueries inspired by retrieved snippets, and
concentrate full-page fetching on the URLs most likely to support the
synthesis" — so which sub-question gets asked next is revised against what
the web actually returned, not fixed at plan time.[^c2]

The planner reward scores three plan-quality dimensions independently
before combining them: "semantic coverage of the user's information need,
retrieval quality of the search queries, and structural expressiveness of
the DAG." Coverage is rubric-based: a frontier LLM generates query-specific
criteria from the query and retrieved context in advance, and coverage is
each criterion's best cosine similarity to any non-answer plan-node field.
Search quality rewards on-topic queries and penalizes redundancy among
them (via mean pairwise similarity). Structural expressiveness rewards
diverse inputs to the final answer, cross-branch evidence reuse, and
search breadth.[^c3]

## Why it matters

Both RL stages use GRPO (Shao et al. 2024) — see Transfer. Staged,
structure-addressable reward is an answer to stall 2 (which axis/sub-query
first) that trains the selection policy itself, rather than scoring
candidate questions at inference time as EIG or VoI do: "Compared with
Qwen3-8B + Search, DecomposeR improves by 7.4 points on DRBench, 22.2
points on HealthBench, and 14.4 points on ResearchQA-Mini, despite using
the same [[backbone-of-a-formula|backbone]] scale" and overall "DecomposeR-8B improves over strong
comparable open baselines by 5.1–8.0 points on popular long-form
benchmarks."[^c4]

An ablation isolates the value of staging the planner and answerer apart,
rather than crediting a joint policy from one trajectory-end reward: "the
top half of Table 2 shows that staged training outperforms joint training
by 3.7–4.7 points across benchmarks. The gap is largest on DRBench, whose
general-domain queries produce the longest rollouts and therefore suffer
most from sparse trajectory-end credit assignment."[^c5]

## Transfer

| | |
|---|---|
| Home field | Reinforcement learning: Group Relative Policy Optimization (Shao et al. 2024), a group-baselined policy-gradient method developed for outcome-verifiable reasoning RL. |
| Here | Used twice — once to train the planner adapter to emit better typed-DAG plans, once to train the answerer adapter to execute them — with "token-level masking that excludes environment observations from the policy gradient." |
| What survives | The group-relative advantage estimate (rollouts of the same query scored against each other rather than an absolute baseline) and masking retrieved/environment tokens out of the gradient. |
| What does not | GRPO's usual single task-native outcome reward does not transfer as-is: the planner reward is a hand-built composite of embedding-similarity rubric coverage, pairwise-diversity search scores and structural-count terms with fixed scalar weights, not a reward the environment supplies directly — the paper does not show this composite is [[calibration]]-free across domains. |

## Limits

This wiki's claim that DecomposeR is an answer to *which sub-question
first* rests on the paper's own framing of planning as sub-query and
DAG-node emission; the reward composite (rubric coverage, search
diversity, structural counts) is scored by sentence embeddings and an
external LLM judge, so its numbers inherit whatever bias those scorers
carry, and the paper reports this only on a single 8B backbone (Qwen3-8B)
with two LoRA adapters, not across model scales. The 5.1–8.0 point gain
and the 3.7–4.7 point staging gap are both benchmark-score deltas on three
long-form benchmarks (DeepResearchBench, ResearchQA-Mini, HealthBench)
judged by rubric- or LLM-judge scoring, not a controlled measurement of
question quality in isolation from answer synthesis quality.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[adaptive-submodularity]] · [[investigative-question-grpo-training]] · [[optimal-decision-tree]]

[^c1]: hussain-2026 — "a single scalar reward R(x, y) is propagated through every mt for policy update"
[^c2]: hussain-2026 — "training the two roles sequentially, Planner RL optimises rewards that depend only on G1 and never on answerer output, so plan quality is isolated from execution noise"
[^c3]: hussain-2026
[^c4]: hussain-2026 — "DecomposeR-8B improves over strong comparable open baselines by 5.1–8.0 points on popular long-form benchmarks due to improved planning and answering capabilities."
[^c5]: hussain-2026
