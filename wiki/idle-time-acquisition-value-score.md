---
description: "A weighted, thresholded score over relevance, knowledge gap, incremental value and timeliness that selects which predicted future need an idle agent spends compute acquiring."
aliases: ["candidate value score", "S(z)"]
sources: ["hu-2026-anticipate"]
---
# Idle-time acquisition value score

> Faced with several candidate future needs it has itself predicted, and
> no observable downstream utility to score them against yet, the agent
> ranks candidates by a fixed linear combination of four proxies and
> spends idle-time compute only on the ones that clear a threshold.

## Definition / Mechanism

Hu, Lyu, Kong et al. (2026) motivate the score by
the absence of ground truth: "Because downstream utility is not directly
observable during idle intervals, ProAct uses a candidate-level value
score for acquisition gating: $S(z) = w_r r_z + w_g g_z + w_v v_z + w_\tau
\tau_z$, $w_r + w_g + w_v + w_\tau = 1$. Here, $r_z$ measures user
relevance, $g_z$ measures the knowledge gap, $v_z$ measures incremental
value beyond existing memory, and $\tau_z$ measures timeliness."[^c1]

Each candidate $z$ carries a tuple $(q_z, e_z, c_z, \rho_z)$ — the
anticipated need, its grounding rationale in dialogue history or memory,
a prediction confidence, and a retrieval plan — and the score gates which
candidates proceed to acquisition: "A candidate is acquired only if
$S(z) \geq \theta_{\mathrm{val}}$. Candidates below the threshold may be
retained for later consideration, but they do not consume immediate
evidence-search or artifact-generation budget."[^c2]

Acceptance then branches on how much of the need is already covered in
memory: full reuse if coverage is high, targeted search of the missing
subtopics if partial, and decomposition into sub-questions with iterative
search if coverage is low.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Hu et al. 2026) | candidate-level value score, $S(z)$ | exact |

## Why it matters

This is a selection rule for stall 2 answered without the decision-theory
apparatus (utility function, EIG, VoI) the rest of this map assumes: no
utility is observable at selection time, so the score substitutes four
cheap proxies (relevance, gap, incremental value, timeliness) combined
linearly and thresholded, rather than an [[entropy]] or regret computation
over a belief distribution. It selects which future question to go
investigate rather than which question to ask next in a live exchange —
the axis being chosen is a predicted need, not a slot in $W$ already on
the table.

## Limits

- The four proxies ($r_z, g_z, v_z, \tau_z$) and the weights
  ($w_r, w_g, w_v, w_\tau$) are not defined operationally in the excerpt
  read here — how "user relevance" or "timeliness" is computed from
  $H_t, M_t$ is not established, so the score's behavior cannot be
  reconstructed from this note alone.
- No comparison is reported against an information-theoretic selection
  criterion ([[mutual-information|mutual information]], EIG) on the same candidates, so whether
  the linear score orders candidates the same way those criteria would is
  untested by this paper.
- Reported only within the ProAct system and ProActEval benchmark built
  by the same authors ([[proact-architecture]]); no independent use of
  this scoring rule is cited.

## Related

[[proact-architecture]] · [[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]]

[^c1]: hu-2026-anticipate
[^c2]: hu-2026-anticipate
