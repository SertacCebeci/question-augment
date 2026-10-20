---
description: "A dense agentic-search reward: the policy answers as if stopping at each state, and the turn-to-turn change in that answer's score becomes the credit, with the policy co-trained as its own evaluator."
aliases: ["OASES", "Outcome-Aligned Search-Evaluation Co-Training", "outcome-aligned process reward", "search-evaluation co-training"]
sources: ["arxiv-2604-03675"]
---
# Answerability-delta process reward

> Score not the search action but what the agent could already answer without it, then reward the difference the next search turn makes.

## Definition / Mechanism

Given a multi-turn search trajectory over states $s_0,\dots,s_T$ (each $s_t$ the question plus everything retrieved through turn $t$), the same policy that is searching is also prompted, once per state, to answer the original question using only the information in $s_t$ — no further search. Each such stopped-here answer $\tilde y_t$ is scored by the ordinary verifiable outcome metric $\gamma_t = R(\tilde y_t, y)$ against the gold answer, exactly as the trajectory's real final answer $\hat y$ is scored as $\gamma_{out}=R(\hat y,y)$. Since $\tilde y_t$ is generated from $s_t$ alone, $\gamma_t$ measures how well that state alone supports the answer.[^c1]

The process reward assigned to the $t$-th search turn is not $\gamma_t$ itself but its increase over the previous state, $r_t^{proc}=\alpha(\gamma_t-\gamma_{t-1})$: the turn is credited only for the answerability it adds, and because the rewards are literal differences they telescope — summed across the trajectory they reduce exactly to the outcome improvement $\gamma_T-\gamma_0$ redistributed turn by turn, so no credit is invented or lost, only relocated to the turns that earned it.[^c2]

A frozen or separately-trained evaluator would drift from the policy's own evolving search behavior and start mis-scoring states it was not trained on. OASES avoids this by having the search policy and the state-evaluator be the same weights: the evaluation rollouts (state, stopped-here answer, its score) are added to the same PPO buffer as the search rollouts, so every gradient step that changes what the policy searches for also retrains it on how well it can already answer from what it has found.[^c3]

Because only the search policy is used at inference — the self-evaluation prompt is a training-time device — the mechanism adds no serving-time cost.[^c4]

## Why it matters

Every other way to price an intermediate search step either guesses relevance (heuristics, coverage), trusts a separately-trained judge that goes stale as the policy changes, or approximates information gain through likelihood shifts that can be inaccurate under partial evidence. Asking the policy "if you had to answer right now, how would you do?" turns a proxy question into the literal outcome question, asked early — the same instrument (a verifiable outcome score) is applied at every state instead of a different one at training versus test time. On five multi-hop QA benchmarks this outcome-aligned, co-trained reward, from Zhang et al. (2026), beat the strongest RL, agentic-search and process-supervision baselines by an average of 4.08 F1 and 3.25 EM.[^c5]

## Limits

The self-evaluation call assumes the policy can meaningfully attempt an answer from a truncated, mid-trajectory state — a capability the paper does not separately validate outside the multi-hop QA setting it tests (HotpotQA, 2WikiMultihopQA, NQ, Bamboogle, MuSiQue), all retrieval tasks with a checkable exact-match or F1 gold answer; it is `[?]` whether the same self-scoring signal stays informative on tasks without a cheap verifiable metric, where $\gamma_t$ itself would need a learned judge and the whole motivation for avoiding a separate evaluator would partly return. The co-training doubles the rollout cost of ordinary RLVR (one evaluation rollout per search state per trajectory), traded for the removed cost of maintaining a frozen reward model.

## Related

[[expected-information-gain]] · [[competence-aware-credit-assignment]] · [[amortised-sequential-information-gathering]] · [[value-of-information]]

[^c1]: arxiv-2604-03675 — "Since ỹt is generated using only the information in st , γt measures how well the current search state supports answering the original question."
[^c2]: arxiv-2604-03675 — "Because the process rewards are defined by score differences γt − γt−1 , they telescope over the search trajectory and form an outcome-consistent redistribution of answerability improvement."
[^c3]: arxiv-2604-03675
[^c4]: arxiv-2604-03675 — "At inference time, only the search policy is executed, so OASES introduces no additional inference-time cost."
[^c5]: arxiv-2604-03675 — "On average, OASES improves over the strongest baseline by 4.08 F1 and 3.25 EM, with particularly clear gains on HotpotQA and 2WikiMultihopQA."
