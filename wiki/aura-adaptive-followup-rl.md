---
description: "AURA picks a chatbot's next follow-up type by an epsilon-greedy TD update over a discretized engagement state, rewarded by a composite quality score, reset every session."
aliases: ["AURA", "Adaptive Understanding through Reinforcement learning for Assessment"]
sources: ["tang-2026-driven"]
---
# AURA: within-session adaptive follow-up selection

> A tabular, session-scoped bandit that picks the next follow-up
> question's *type*, not its wording, from a live quality signal —
> and discards everything it learned when the conversation ends.

## Definition / Mechanism

Tang (2026) introduces AURA for a campus-climate
survey chatbot: within a single conversation, it adapts which class of
follow-up to ask next — validate, specify, reflect (elaboration), probe
(topic), or continuation — using an automated quality signal computed
after every exchange. The state is a discretization of the current
composite quality score and its trend (five states: low/medium/high ×
improving/stable), initialized from expected-value (EV) estimates over
96 prior conversations (467 exchanges), then updated online during the
live session with a temporal-difference rule, reward $r_t = \Delta Q_t$
(the change in composite quality between exchanges) and $\alpha = 0.3$:
"This standard temporal-difference update … occurs at exchange t after
observing the outcome of action $a_{t-1}$ selected in state $s_{t-1}$."[^c1]

The next action is chosen $\epsilon$-greedy ($\epsilon=0.30$ in the
recommended configuration): explore uniformly at random with probability
$\epsilon$, otherwise exploit $\arg\max_a \mathrm{EV}(s,a)$. All
within-session updates are discarded at session end; the next user
starts from the population prior again.[^c2]

## Known as

| Field | Name there | Match |
|---|---|---|
| This paper (Tang 2026) | AURA | exact — this note's object |
| This paper (Tang 2026), expansion | Adaptive Understanding through Reinforcement learning for Assessment | exact — the acronym's full name |

## Why it matters

In a controlled comparison (n = 20 conversations per condition) against
the non-adaptive prior chatbot, "AURA achieved a +0.12 mean gain in
composite response quality with a statistically significant improvement
over non-adaptive baselines (p = 0.044, d = 0.66), driven by a 63%
reduction in specification prompts and a 10× increase in validation
behavior."[^c3]

A comparison of three exploration settings found that "only moderate
exploration (ϵ = 0.30) maintained performance gains across all
conversation phases. Conservative exploration (ϵ = 0.15) led to
late-phase degradation through premature convergence, while decaying
exploration schedules introduced excessive early variability that
prevented effective learning."[^c4]

This is a measured instance of adapting *which axis to ask next* purely
from an online quality signal, with no explicit information-theoretic
objective (no EIG, no [[entropy]] term) and no gradient-trained policy
network — a different route to the same stall than a GRPO-trained
question-generator.

## Transfer

| | |
|---|---|
| **In its home field** | Tabular reinforcement learning: an $\epsilon$-greedy policy over a discrete state-action table, updated by a TD(0) rule — a formalism built for settings with many repeated visits to each state-action pair. |
| **Here** | Five follow-up-type actions, five discretized engagement states, updated for 10–15 exchanges inside one conversation, initialized from a population EV table and then discarded. |
| **What survives** | The exploration/exploitation logic itself, and the qualitative finding that moderate exploration outperforms both low and decaying exploration in a short horizon. |
| **What does not** | Any convergence guarantee. Tabular TD's asymptotic guarantees assume many visits per state-action pair; here the "learning" is a handful of TD updates layered on a prior estimated from only 96 conversations (17 of 25 state–action pairs had any prior data), so the online policy is only ever a small correction to that prior, not a converged value function. |

## Limits

- Single domain and deployment (a campus-well-being chatbot), n = 20
  conversations per exploration condition — a small controlled
  evaluation, not shown to generalize to other question-asking settings.
- The reward is the composite quality proxy [[lsde-response-quality-signal|LSDE]],
  not a validated measure of the answer's actual value to a downstream
  decision; the paper itself flags that "AURA's exploration can be
  locally suboptimal in early exchanges and LSDE is a proxy that may
  reflect dataset biases."[^c5]
- Learning is discarded at session end by design (for privacy), so no
  claim here is about a policy that improves across users — only about
  within-session adaptation from a fixed prior.

## Related

[[investigative-question-grpo-training]] · [[expected-information-gain]] · [[value-of-information]] · [[constraint-seeking]] · [[lsde-response-quality-signal]]

[^c1]: tang-2026-driven — "This standard temporal-difference update [37] occurs at exchange t after observing the outcome of action at−1 selected in state st−1 at the previous exchange, increasing EV when the observed reward exceeds the prior estimate and decreasing it when the action underperforms."
[^c2]: tang-2026-driven
[^c3]: tang-2026-driven — "AURA achieved a +0.12 mean gain in composite response quality with a statistically significant improvement over non-adaptive baselines (p = 0.044, d = 0.66), driven by a 63% reduction in specification prompts and a 10× increase in validation behavior."
[^c4]: tang-2026-driven — "only moderate exploration (ϵ = 0.30) maintained performance gains across all conversation phases. Conservative exploration (ϵ = 0.15) led to late-phase degradation through premature convergence, while decaying exploration schedules introduced excessive early variability that prevented effective learning."
[^c5]: tang-2026-driven — "AURA’s exploration can be locally suboptimal in early exchanges and LSDE is a proxy that may reflect dataset biases."
