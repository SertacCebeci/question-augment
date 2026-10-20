---
description: "A task formalization for a long-lived agent asking now for a reusable user preference the current task does not need but a future session will."
aliases: ["ATR", "Ask-to-Remember", "proactivity gap in long-lived LLM agents"]
sources: ["wu-2026-later"]
---
# Ask-to-Remember

> A long-lived agent serving one user across sessions must decide whether
> to ask, now, for a standing preference the current task does not need —
> because the only alternative is silently missing it later, when the user
> is offline and cannot be asked.

## Definition / Mechanism

Wu, Zou, Wang, Zhao & Shi (2026) name the failure mode
this formalizes: "today's agents keep what a user volunteers but rarely
ask for what stays unspoken, leaving a proactivity gap in long-lived LLM
agents: an agent cannot act on a preference it never obtained."[^c1]

They isolate one controllable slice of this gap as Ask-to-Remember (ATR):
"the agent decides whether to ask a question whose answer is not needed
for the current task but can be reused in a later session with the same
user."[^c2]

The objective is a utility-cost trade-off over the whole session sequence,
not the current task alone: "Vutil (π) = Eτ ∼Du [ U (τ ; I ∗ , π) ] −
C(π), a utility–cost view shared with preference elicitation." Two
properties make the target hard to fix: "the current task does not reveal
which parts of I ∗ − Iˆt are worth asking about, so the target is
underdetermined; and the agent cannot know which tasks Du will draw,
leaving the payoff delayed and uncertain."[^c3]

## Why it matters

This gives stall 2 a case the map's [[value-of-information]] and EIG rows do
not cover: the axis worth asking about is not one the current task's
uncertainty points to at all — its payoff is external to the present
decision and may never be cashed in. A selection rule scored only against
the task in front of the agent (EIG on the current answer, VoI against the
current decision) has no term for this; ATR's objective explicitly nets a
present interaction cost against a distribution over future, unobserved
tasks.

## Transfer

| | |
|---|---|
| **In its home field** | Preference elicitation / decision theory: a utility-minus-cost objective over a policy, the same form as classical value-of-information accounting. |
| **Here** | Whether to spend one question now on a preference the present task does not need, priced against expected use in tasks the agent has not yet seen. |
| **What survives** | The subtractive cost–benefit form ($\mathbb{E}[U] - C$) and the framing of asking as an action with its own price, not a free side-effect of the current turn. |
| **What does not** | The utility term $U(\tau; I^*, \pi)$ is not computable at decision time — it depends on a future task distribution $D_u$ the agent cannot observe, so this objective cannot be evaluated online the way a standard VoI calculation can; the source treats it as a target the benchmark approximates, not a quantity the agent computes directly.[^c4]

## Limits

- The formalization is the source's own framing of a problem it then
  benchmarks; it names the objective $V_{util}$ but does not show any
  policy that computes or estimates it directly — see Wu et al. (2026)'s [[atrbench|ATRBench]] results for what is actually measured.
- `wu-2026-later` is a single 2026 arXiv preprint; status is `queued` in
  `wiki/meta/sources.json` — claims above are stated as the source states
  them, unverified beyond the provisional check made here.
- Defined only for a single user served repeatedly by one agent with a
  shared cross-session context; says nothing about multi-user or
  multi-agent settings.

## Related

[[value-of-information]] · [[pact-ask-or-act]] · [[proactivity-taxonomy]] · [[bounded-rationality]]

[^c1]: wu-2026-later
[^c2]: wu-2026-later — "the agent decides whether to ask a question whose answer is not needed for the current task but can be reused in a later session with the same user."
[^c3]: wu-2026-later
[^c4]: wu-2026-later — "the agent cannot know which tasks Du will draw, leaving the payoff delayed and uncertain."
