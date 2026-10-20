---
description: "A retrieval-augmented store of past high-reward agent trajectories, filtered by novelty and a dynamic reward threshold, prepended to the agent's context as a direct action suggestion."
aliases: []
sources: ["lai-2025"]
---
# Experience repository

> Not a fixed few-shot prompt but a growing store of the agent's own
> highest-reward past turns, retrieved per query and refreshed as training
> proceeds.

## Mechanism

Lai et al. (2025) ground Doctor-R1's policy in a repository of
its own prior (state, action, reward) tuples rather than in similarity
retrieval alone: "we introduce an Experiential Agentic Reinforcement
Learning (RL) approach to guide the agent's decisions. We construct an
experience repository that selectively stores and retrieves high-quality
prior trajectories based on their rewards. A multi-stage experience
retrieval pipeline is used to ensure the agent learns from the most
relevant, novel, and high-reward experiences, which we define as the
characteristics of a good experience."[^c1]

Retrieval for a query state $Q$ runs three stages: (I) a bi-encoder scores
every stored state by cosine similarity plus its historical reward,
weighted by $\alpha$, and keeps the top-$N$ candidates; (II) a
cross-encoder reranker reorders that candidate set with token-level
attention; (III) novelty and reward filtering keep only candidates whose
similarity to $Q$ falls below a novelty threshold and whose reward exceeds
a *dynamic* threshold $\tau_\text{dynamic}=\mu_R+\beta_\text{std}\cdot
\sigma_R$, computed from the mean and standard deviation of the reranked
candidates' own rewards. The surviving top-$k$ experiences are prepended to
the query as a direct suggestion for the agent's next action. Storage is
equally selective: after each training batch, only trajectories whose
reward meets a fixed boundary $\tau_\text{reward}$ are added to the
repository.[^c2]

An ablation removing the repository ("w/o Experience") drops the
HealthBench average from 36.29 to 31.69 and MAQuE task-success accuracy
from 60.00 to 56.00 — a larger single-component drop on HealthBench than
removing the process reward (36.29 to 32.61). In expert review, two
licensed physicians rated the retrieved content "Clinically Helpful" in
83.87% of cases for guiding the agent's next action, with 16.13% "Neutral
and Irrelevant" and 0% "Harmful."[^c3]

## Limits

"Good experience" is defined operationally, by the model's own reward
score exceeding a batch-relative dynamic threshold, not by any independent
ground truth of trajectory quality; a systematically miscalibrated reward
model would poison the repository it also selects for. The retrieval
pipeline's two learned components (embedding model, reranker) are not
ablated separately from the novelty/reward filtering, so which stage does
the work is not established. Evidence is one paper, one domain, one base
model family (Qwen3-8B).

## Related

- [[two-tiered-reward-architecture]]
- [[investigative-question-grpo-training]]
- [[preference-optimization-for-questions]]

[^c1]: lai-2025
[^c2]: lai-2025 — "The combined score Scombined (Equation 4) integrates cosine similarity with the historical reward R(Ei ) weighted by α."
[^c3]: lai-2025
