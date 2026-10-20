---
description: "A five-phase protocol where a multi-agent system's own agents interrogate each other and cast structurally weighted votes to localise which component caused a failure."
aliases: ["POIROT", "Peer-Opinion Interrogation and Review Outcome Tracking"]
sources: ["varela-2026"]
---
# POIROT protocol

> When a compound system fails, the agents that ran it — not an external
> judge — interrogate each other and vote on which component is to blame.

## Definition / Mechanism

POIROT represents a multi-agent system as $S=(A,C,H,U)$ — agents,
software, hardware, human actors — and runs five sequential phases per
failure case. Phase I builds an $N$-dimensional hazard space $H_{haz}
\subseteq \mathbb{R}^N$, one axis per component. Phase II has each agent
independently reconstruct its own trajectory and report perceived
anomalies, with no cross-agent influence yet. Phase III is peer
interrogation: agents exchange reports and question each other through an
all-to-all messaging graph (a `poirot_server` node routes `talk_to_{target}`
calls), refining hypotheses with no public vote. Phase IV is private
voting: each agent emits a binary attribution vector $v_i \in \{0,1\}^N$
naming which components it blames, cast without seeing others' votes to
block strategic alignment. Phase V aggregates: each agent's vote is
weighted by $w_i = \beta + \tfrac{1}{2}(1 - d_H(p_i,v_i)/N)$, where $d_H$
is the Hamming distance between the agent's own structural position $p_i$
and its vote and $\beta=0.25$ is a floor so no agent is fully discarded —
so an agent's vote counts most when it accuses components structurally
close to itself. Scores $S_j=\sum_i w_i (v_i)_j$ rank the candidate causes.
[^c1]

On the Who&When benchmark (122 systems, 2-4 agents, single injected
fault), POIROT beat a single-LLM-judge baseline on all four tested models,
and a logistic regression fit across models found the advantage grows with
problem complexity (interaction OR = 1.60, 95% CI [1.13, 2.28], p =
0.008), while its interaction with agent count alone did not reach
significance (OR = 1.55, p = 0.27). On a purpose-built benchmark (CORTEX, a
3-agent clinical exoskeleton system, and TradingAgents, 12 agents), POIROT
beat the same baseline under both single-fault and simultaneous
multi-fault conditions, gains ranging +6.7 to +42.0 percentage points
across models, with one exception (GPT-OSS 120B on multi-fault CORTEX,
−1.3 pp).[^c2]

## Why it matters

The question POIROT answers is not "what is the axis?" (fixed — the
hazard space enumerates it in Phase I) but **who is allowed to answer
it**: the system replaces one external evaluator with the components that
ran the failing episode, and combines their answers by structural
proximity rather than by rank or majority. On this wiki's stall 2 that
substitutes a genuinely different selection move for "score every axis and
ask about the best one" — POIROT does not choose one hazard axis to
investigate before another; it interrogates and privately scores **all**
$N$ axes at once per case, deferring the axis choice to the weighted-vote
outcome rather than to a per-step query criterion.

## Limits

- Every reported effect is a comparison to **one baseline family**
  (single-LLM-as-judge, all-at-once context). No comparison to majority
  voting without distance weighting, or to an adaptive multi-round
  judge, is reported, so the load-bearing claim is "beats one centralised
  judge," not "beats every alternative aggregation."
- The distance weight $w_i$ is a fixed function of structural position in
  $A\cup C\cup H\cup U$, not of demonstrated [[calibration|reliability]]; a reputation
  variant (β updated by past accuracy) was tested and found to change
  results negligibly on the benchmarks used here — that null result does
  not establish it is negligible under adversarial or persistently
  unreliable agents.
- Agents are evaluated in a fixed sequential order with a hard cap of 8
  LLM calls per agent before a forced vote; the protocol's cost and any
  order-dependence of the interrogation phase are not measured.
- The compound-fault (multi-fault CORTEX) sample sizes are small (the
  benchmark's per-model multi-fault columns run in the tens of cases), so
  the one negative result (GPT-OSS 120B, −1.3 pp) is not distinguishable
  from noise with the reported data.[^c3]

## Related

[[multi-agent-clarification]] · [[value-of-information]] · [[possible-worlds]]

[^c1]: varela-2026 — "The weight assigned to the vote of agent Ai is then: ( ) 1 dH (pi , vi ) wi = β + 1− , (8) 2 N"
[^c2]: varela-2026 — "A significant positive interaction (OR = 1.60, 95% CI [1.13, 2.28], p = 0.008) indicates that POIROT’s accuracy advantage over the single-LLM baseline increases reliably with problem complexity."
[^c3]: varela-2026 — "We evaluate a reputation-based extension in which β is updated across successive POIROT evaluations to reflect each agent’s historical attribution accuracy. Empirical results show negligible variation in attribution performance across configurations, indicating that static β captures the necessary regularisation without added complexity."
