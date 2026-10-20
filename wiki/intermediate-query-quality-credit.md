---
description: "Scoring each intermediate search query on novelty (rule-based overlap) and usefulness (judge), then refining failures from the textual diagnosis, lifts search-agent accuracy and efficiency."
aliases: ["Dual-Level Credit Assessment", "SmartSearch query process reward", "process reward-guided query refinement"]
sources: ["openalex-org-w7120272548"]
---
# Intermediate query quality credit

> A search agent's answer is only as good as each query it issues along the way; grade the queries, not only the final answer, and feed the diagnosis back into rewriting the bad ones.

## Mechanism

Wen, Dong and Dou (2026) observe that a single imprecise intermediate query (their example omits the word "actor", so a politician of the same name is retrieved) misleads the reasoning and derails the whole trajectory.[^c1] They grade every query against three principles: novelty (no redundancy with earlier queries), necessity (the intent must advance toward the answer) and relevance (the retrieved documents contain the expected information).[^c2]

The principles are operationalised by two checks. The first is rule-based novelty: a query is redundant (score 0) when more than a threshold K of the documents it retrieves duplicate documents from any earlier step. The second is a model-based usefulness judgment, given the question, the gold answer and the trajectory so far, that returns a 0/1 score and a text explanation. The overall score is a logical conjunction of the two, and the explanations are concatenated.[^c3] The judge is a small student model distilled from a stronger teacher; on 100 trajectories the teacher agreed with humans nearly 90 percent, the student over 85 percent with the teacher and over 80 percent with humans.[^c4]

For each query scored 0, a refiner receives the question, the history and the textual diagnosis and produces a replacement query; the agent then regenerates every later step from that point. The two trajectories differ only in that query, which yields contrastive training data and a rollout strategy.[^c5] The refinement rules map diagnosis to repair: if redundant or unnecessary, pick a more necessary intent; if the results lack the expected information, reformulate, for instance by switching between a full question and a keyphrase query, or by adding or dropping information.[^c6]

Training is a three-stage curriculum: imitation on trajectories filtered by query quality, preference alignment on original-versus-refined pairs, then reinforcement learning with the process reward and refinement inside rollouts. Filtering by query quality instead of only final-answer correctness gave better performance from only 60 percent of the data.[^c7] The authors report more than 7 percent average EM and F1 gain over other process-supervised RL methods, and better search quality and efficiency (fewer wasted rounds).[^c8] The paper's explanation is that outcome-only reward is sparse and leaves intermediate steps unguided.

## Limits

- The usefulness judge is given the gold answer, so the signal exists only at training time on tasks with known answers; it is not a way to grade a query at deployment.
- Novelty is document-identity overlap with a hand-set threshold K, so it cannot tell a deliberately repeated confirmation query from a wasteful one (my inference).
- Binary scores discard degree of quality; the ablation attributes gains jointly to process rewards and refinement, and the 90/85/80 percent agreement figures come from a 100-trajectory sample.
- Only retrieval-based multi-hop question answering with a search engine was tested; whether the three principles carry over to clarifying questions asked of humans is not examined.

## Related

- [[answerability-delta-process-reward]] — another dense per-turn credit for search agents, measured by answer change rather than query criteria
- [[reinforcement-query-refiner]] — an RL-trained rewriter of the user's query, versus repair of the agent's own mid-trajectory queries
- [[competence-aware-credit-assignment]] — related credit assignment across steps
- [[two-tiered-reward-architecture]] — layered rewards with a comparable outcome plus process split

[^c1]: openalex-org-w7120272548 — "low-quality queries can lead to unexpected retrieval results or even"
[^c2]: openalex-org-w7120272548 — "Query Novelty: The query should avoid redundancy with previous queries and introduce novel information."
[^c3]: openalex-org-w7120272548 — "by a logical conjunction of the component scores:"
[^c4]: openalex-org-w7120272548 — "that the teacher model achieves nearly 90% overlap with human"
[^c5]: openalex-org-w7120272548 — "is achieved by systematically identifying and refining low-quality"
[^c6]: openalex-org-w7120272548 — "If the textual feedback indicates that the retrieved results do not"
[^c7]: openalex-org-w7120272548 — "incorporating queryquality filtering enables the model to achieve superior performance"
[^c8]: openalex-org-w7120272548 — "(3) Optimizing the quality of intermediate search queries significantly improves overall"
