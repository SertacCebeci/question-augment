---
description: "A constrained-POMDP gate that decides whether an agent should stay silent, ask, assist, or act, scored by the discounted value gap of the best admissible non-silent action over silence."
aliases: ["intervention advantage", "proactive service intervention", "constrained proactive-service POMDP"]
sources: ["tang-2026"]
---
# Intervention advantage

> Whether to ask is one case of a four-way gate — silent, ask, assist, act —
> and the number that decides it is a value *difference*, not a probability
> of need.

## Definition

Tang et al. (2026) define a non-silent action as a **proactive
service intervention** relative to the current task specification $\iota_t$
when the system autonomously introduces the opportunity, the protocol still
permits silence or another feasible action, the system chooses from beliefs
about goals/environment/consequences, and the objective includes
user-endorsed benefit.[^c1]

They model the decision as a constrained partially observable Markov
decision process $M = \langle S,O,A,T,Z,r,c,\gamma,b_0\rangle$, used "as an
analytical language, without assuming that every existing system explicitly
solves it."[^c2]

An action is a tuple $a_t=(m_t,z_t,\ell_t)$ with mode
$m_t \in \{\text{silent}, \text{ask}, \text{assist}, \text{act}\}$: silent
permits further observation with no visible effect; ask "seeks a goal,
evidence, preference, or authorization"; assist offers rejectable
information or a draft; act invokes tools or changes external state.[^c3]

## The gate

With a Lagrangian-relaxed reward $r_\eta$ trading off task benefit against
interruption, questioning, execution and privacy costs under fixed
multipliers $\eta$, the **intervention advantage** is

$$\Delta_\eta(b_t,\bar\kappa_t) = \max_{a\in A_t^+} Q^*_\eta(b_t,\bar\kappa_t,a) - Q^*_\eta(b_t,\bar\kappa_t,\text{silent})$$

where $A_t^+$ is the admissible non-silent action set. Under conservative
tie-breaking "an optimal agent remains silent when
$\Delta_\eta(b_t,\bar\kappa_t)\le 0$ and otherwise selects the admissible
action with highest value" — and $Q^*_\eta(\cdot,\text{silent})$ already
prices the option to observe longer and intervene later, so silence is not
abandonment.[^c4]

Admissibility is a hard gate, not a soft cost: an action must be permitted
by a verified authorization ledger and keep the tail probability of severe
loss under a threshold; "external execution is inadmissible when
authorization is unknown, although an ask action that requests authorization
can remain admissible."[^c5]

For a one-step question with a [[sufficient-statistic]] answer, the value of
asking decomposes into the expected relaxed reward of the exchange plus the
discounted value after the answer; the authors note that when an answer
changes neither the belief, the authorization ledger, nor a downstream
action's value, "this pure information value cannot be positive" — the same
zero-VoI condition as [[value-of-information]], restated inside a
four-action gate instead of an ask/don't-ask binary.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This survey (proactive agents) | intervention advantage, $\Delta_\eta$ | exact |
| Human–computer interaction (Horvitz, cited by Tang et al.) | mixed-initiative expected-utility comparison | close — an earlier instance restricted to one trichotomy (inaction / dialogue / automated execution) with no explicit belief-state POMDP or authorization gate |
| Decision theory | option value of waiting + value of information, combined | close — $\Delta_\eta$ is VoI's "would the answer change the action" test generalised to four action modes and wrapped in a budget-constrained POMDP, not a new value concept |

## Transfer

| | |
|---|---|
| **In its home field** | Constrained POMDPs and Lagrangian relaxation of cost budgets are standard tools in control and operations research, applied here to service/dialogue agents by Tang et al. (2026) |
| **Here** | An agent choosing, at each decision opportunity, among staying silent, asking, assisting outright, or acting — scored by the same value-difference logic as [[value-of-information]] but over a richer action set and under a hard authorization/risk constraint |
| **What survives** | The invariance test (act only if some admissible non-silent action beats silence); the treatment of authorization as a feasibility constraint rather than a weighted cost; the option value of waiting built into $Q^*_\eta(\cdot,\text{silent})$ |
| **What does not** | The closed-form arithmetic — $T$, $Z$, $r$, $c$ and the multipliers $\eta$ are not written down for an open-ended asking agent, so $\Delta_\eta$ is a specification of what to compute, not a computed number, exactly as with $\mathrm{VoI}$ itself |

## Limits

- $\Delta_\eta$ is defined on the fixed-multiplier Lagrangian relaxation; the
  paper is explicit that "if strong duality or feasibility conditions fail,
  the relaxed gate only yields a candidate policy whose cumulative budgets
  must be checked separately" — the gate does not by itself guarantee the
  original budget-constrained problem is solved.
- The framework is this survey's own synthesis of the field's POMDP,
  mixed-initiative and clarification literatures, not a result independently
  replicated by others; `tang-2026` is a single 2026 arXiv preprint and its
  claims are reported as the source states them.
- The one-step value-of-asking formula (Eq. 14 in the source) assumes the
  answer is observed immediately and is a sufficient statistic for the
  resulting belief update; multi-turn or delayed answers are not covered by
  that special case.

## Related

[[value-of-information]] · [[expected-utility]] · [[bounded-rationality]] · [[reversibility]] · [[abstention]]

[^c1]: tang-2026
[^c2]: tang-2026 — "We use a constrained partially observable Markov decision process as an analytical language, without assuming that every existing system explicitly solves it"
[^c3]: tang-2026 — "at = (mt , zt , ℓt ), mt ∈ {silent, ask, assist, act}"
[^c4]: tang-2026
[^c5]: tang-2026
