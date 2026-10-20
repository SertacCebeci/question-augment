---
description: "An agent's decision to pursue a question is a weighted sum of immediate uncertainty reduction, cost, delayed return and the value of leaving it open, with the weights drifting from experience."
aliases: ["inquiry value function", "curiosity value function", "single-agent inquiry policy", "curiosity policy weights"]
sources: ["monosov-2026"]
---
# Curiosity value function

> Which question an agent pursues is decided by a four-term weighted value, not
> by uncertainty reduction alone — and the weights on those four terms move
> with the agent's own recent experience.

## Definition / Mechanism

For agent $i$ deciding whether to pursue question $q$ at time $t$, the private
value is $V_i(q,t) = \psi_i(t)\,\mathbb{E}[I_i] - \lambda_i(t)\,\mathbb{E}[C_i] + \tau_i(t)\,\mathbb{E}[L_i] - \phi_i(t)\,\mathbb{E}[O_i]$,
where $I_i$ is the immediate value of reducing uncertainty, $C_i$ is the cost
of asking, $L_i$ is the delayed return the answer may unlock later, and $O_i$
is the value of *not* resolving the question yet — kept for flexibility or
because the information is actively unwanted.[^c1]

The weights $\theta_i(t) = (\psi_i,\lambda_i,\tau_i,\phi_i)$ are not fixed:
they update through a drift operator $\theta_i(t+1) = \theta_i(t) + \Delta\theta_i(X_i(t), M_t)$,
where $X_i(t)$ is a smoothed trace of the agent's own recent inquiry (cost,
speed, uncertainty reduction, [[question-generativity|generativity]], reusability of what it has just
resolved) and $M_t$ is the surrounding ecology (tool costs, peers' questions,
the shared knowledge stock). One concrete implementation treats each quickly
answered question as a small frequent reward and lets reinforcement learning
reshape the weights over longer timescales.[^c2]

The paper works out when this drift tips an agent from a costly, generative
"frontier" question toward a cheap, low-generativity one: drift favors the
cheap question exactly when $(\Delta I)\Delta\psi_i + (\Delta L)\Delta\tau_i > (\Delta C)\Delta\lambda_i$ — a repeated diet of fast, cheap answers pushes a person toward more of
the same only in an ecology where the cost weight itself rises with that
experience ("habituation"); in an ecology where cheap answers are abundant
enough that effort stops binding, the same history can leave frontier
questions just as attractive.[^c3]

## Why it matters

Every other criterion on this stall ([[mutual-information|mutual information]], EIG, VoI) scores a
question by one term — uncertainty reduction or decision-relevant value —
computed fresh each time. This framework adds two things those criteria lack:
a term for the value of *not* resolving a question yet, and a mechanism by
which the scoring itself changes as a function of the asker's own history,
not the question's content.

## Transfer

| | |
|---|---|
| Home field | reinforcement learning / behavioral economics (habit-formation preference drift, e.g. Ryder & Heal 1973; small-reward RL updates) |
| Here | the weights on an asking-agent's four-term value function, updated after each resolved question |
| What survives | the update structure — a target set by a smoothed experience trace and an ecology summary, weights relaxing toward it with a learning rate |
| What does not | no convergence or regret guarantee; the paper states the update is one "plausible implementation" among others, not derived or fit to data |

## Limits

The model is a toy conceptual framework: $I_i$, $C_i$, $L_i$, $O_i$, and the
drift target function $W$ are left unspecified beyond illustrative forms, and
no parameter is estimated from data. The habituation/abundance sign analysis
is a worked example inside the model's own algebra, not an empirical finding
about real agents. [monosov-2026] is a single-author arXiv preprint,
unverified beyond provisional confirmation of its listing.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[question-generativity]] · [[bounded-rationality]]

[^c1]: monosov-2026 — "Vi (q, t) = ψi (t) Ei,t [Ii (q, t)] − λi (t) Ei,t [Ci (q, t)] + τi (t) Ei,t [Li (q, t)] − ϕi (t) Ei,t [Oi (q, t)]."
[^c2]: monosov-2026 — "θi (t + 1) = θi (t) + ∆θi Xi (t), Mt ."
[^c3]: monosov-2026 — "The drift strengthens the pull toward the cheap question only when (∆I) ∆ψi + (∆L) ∆τi > (∆C) ∆λi ."
