---
description: "A clipped policy-gradient objective normalizing posterior-sensitive turn rewards per decision depth, not per episode, to train belief-conditioned question asking."
aliases: ["ECHO", "Epistemic Credit for History-Conditioned Optimization", "Depth-wise Epistemic Credit Optimization"]
sources: ["nath-2026"]
---
# ECHO (epistemic credit)

> Give each question credit for the belief it moved, not for whether the
> episode it sat in eventually succeeded.

## Definition / Mechanism

Nath & Krishnaswamy (2026) motivate ECHO from
[[epistemic-decision-process|Theorem 3.2]]: aggregate episode return aliases
belief-distinct decisions, so a trajectory-level advantage cannot recover
per-turn epistemic credit. ECHO is a turn-level surrogate for the
belief-conditioned (Bayesian) advantage: like GRPO, it samples $G$ parallel
rollouts and computes a clipped, group-normalized policy-gradient objective,
but unlike trajectory-level GRPO it normalizes a *posterior-sensitive turn
reward* $r_t^{(g)}=u(b_t^{(g)},a_t^{(g)},o_t^{(g)})$ — measuring local
epistemic progress such as information gain or elimination of inconsistent
hypotheses — separately **at each decision depth** $t$ across the active
rollouts $G_t$, rather than normalizing one full-episode return broadcast to
every turn.[^c1]

Because different rollouts diverge into different histories and beliefs by
turn $t$, this is not an exact belief-local advantage after divergence; the
source is explicit that each reward is evaluated relative to its own
rollout's posterior, trading exactness for avoiding exhaustive
same-history branching.[^c2]

In the paper's Clue Selector Game benchmark, an ECHO-trained 1.5B Qwen 2.5
policy reaches a 45.3% resolve rate, exceeding the best frontier
prompting baseline tested (Claude Sonnet 4.6, 43.1%) and substantially
outperforming episodic-return GRPO (14.7%) and per-turn RLOO (13.8%) on the
same reward function; it also has the lowest zero-elimination-question rate
(18.6%) among compared policies, with high elimination quality (0.670) and
groundedness (0.718), and achieves this with almost no explicit reasoning
text (0.9%) — reasoning traces are neither necessary nor sufficient for the
gain, since a ReAct baseline that reasons every turn does not improve
resolution.[^c3]

## Why it matters

ECHO is a concrete answer to "how do you train a selector to act on the
belief state, not the transcript": normalize the credit signal at the
decision depth where the belief actually changed, instead of at the episode
boundary. For stall 2 it is a training-time mechanism, not a scoring rule
computed at inference — it changes which questions a policy learns to ask,
rather than ranking candidate questions directly the way
[[expected-information-gain]] or [[value-of-information]] do.

## Transfer

| | |
|---|---|
| **In its home field** | GRPO's clipped, group-relative policy-gradient objective is standard for single-turn RLHF-style LLM training, normalizing one reward per completed episode |
| **Here** | Multi-turn LLM information seeking, where the interesting variation is *within* an episode, across decision depths |
| **What survives** | The clipped trust-region ratio and group-relative normalization mechanics of GRPO |
| **What does not** | Episode-level reward broadcasting — the normalization group is the set of rollouts sharing a decision depth, not the whole trajectory, and the resulting advantage is only an approximate, not exact, belief-local advantage once rollouts diverge |

## Limits

- Demonstrated in one controlled benchmark (the Clue Selector Game) built by
  the same authors to have an explicit, measurable posterior; transfer to
  open-ended natural-language information-seeking tasks without an explicit
  [[possible-worlds|hypothesis space]] is not shown.
- The turn reward $u(b_t,a_t,o_t)$ requires a computable posterior or a
  proxy for one at training time — the method assumes the belief state (or
  an encoding of it) is available to the reward function, which is a
  stronger requirement than the trajectory-level reward it replaces.
- Results are a single 2026 arXiv preprint's own comparison against
  baselines it also implemented; no independent replication.

## Related

[[epistemic-decision-process]] · [[expected-information-gain]] · [[value-of-information]] · [[investigative-question-grpo-training]]

[^c1]: nath-2026 — "Like GRPO [59], ECHO uses group-normalized advantages and a clipped policy-gradient objective [55]; unlike trajectory-level GRPO, it normalizes posterior-sensitive turn rewards rather than full episode returns."
[^c2]: nath-2026
[^c3]: nath-2026 — "Table 1 shows that ECHO achieves the strongest learned-policy performance in CSG. Its resolve rate of 45.3% exceeds the best frontier baseline, Claude Sonnet 4.6 (43.1%), and substantially outperforms episodic-return GRPO (14.7%), RLOO per-turn (13.8%), and all base/prompting baselines."
