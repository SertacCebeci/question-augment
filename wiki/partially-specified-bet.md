---
description: "A pair of choices that reveals whether someone believes their own picture of Karni & Vierø (2017,"
aliases: ["partially specified bet", "bet on partially describable events"]
sources: ["karni-2017"]
---
# The partially specified bet

> A pair of choices that reveals whether someone believes their own picture of
> the possibilities is incomplete — without ever asking them, and without them
> being able to say what is missing.

## Definition / Mechanism

Karni & Vierø (2017, §5.3) face a methodological problem their own theory[^s1]
raises: the theory presumes the agent is aware of her unawareness, so how can
an observer infer *from behaviour* that she is? Their answer is a bet whose
payoffs are specified only on part of the [[possible-worlds|state space]].

Given the augmented state space of [[catch-all-consequence]], define
$B := \{\, b : C^A \to C \,\}$ — bets whose domain is only the **fully
describable** states and whose payoffs are nameable consequences. In their
two-medication example, $b_1$ pays $c_1$ in the states where $a_1$ succeeds
and $c_2$ otherwise; $b_2$ is the same construction for $a_2$. Nothing in the
description of $b_1$ or $b_2$ mentions any partially describable state.

If the agent were aware only of the fully describable states, $b_1$ and $b_2$
would be exact replicas of the acts $a_1$ and $a_2$, so her ranking of the
bets and of the acts would have to coincide. Two patterns therefore give her
away:

| Pattern | What is observed | What it shows |
|---|---|---|
| 1 | $b_1 \sim b_2$ but $\neg(a_1 \sim a_2)$ | the acts differ somewhere the bets do not mention |
| 2 | $b_i \succ b_j$ but $a_j \succeq a_i$ | the ranking reverses off the described part |

Either pattern means the agent is taking into account events that are not
fully describable. Their illustration: a decision maker who bets that the new,
untried medication is more likely to succeed than the old one, yet chooses the
old one anyway, is acting on the possibility of side effects she cannot name —
and the pattern also shows she thinks such events are more likely under one
action than under the other.

## Why it matters

Every informant-facing generator on Axes asks the informant to
*produce* structure — [[grand-tour-question]] asks for their account of it,
[[objectives-generation-deficit]] measures how much of it they fail to
produce. This is the one probe that needs no production at all: it detects the
agent's own belief that her list is short from a preference reversal between a
bet and an act with identical described payoffs. It is a test for the
precondition of hunting, applicable to a person or to a model, and it is
scored on choices, not on reports.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision theory under unawareness (Karni & Vierø 2017) | partially specified bet | exact |
| Decision theory under unawareness | bet on partially describable events | close — the same instrument named by the event it leaves unmentioned rather than by its specification |
| Decision theory / statistics | **partially specified (imprecise) probabilities** | **not this concept.** That is a representation of belief by a *set* of measures on a fixed space; this is a single bet whose payoffs are written down on only part of the space, used as a diagnostic |

## Transfer

| | |
|---|---|
| **In its home field** | A revealed-preference diagnostic: two menus over a finite derived state space, compared to detect that the agent's subjective space is larger than the described one |
| **Here** | A two-item probe put to an informant (or an agent) before eliciting axes, to find out whether they believe their own outcome list is complete |
| **What survives** | The design principle — hold the *described* payoffs identical and vary only what is left unmentioned, then read the incompleteness off the disagreement between the two rankings. No naming of the missing axis is required at any point |
| **What does not** | The inference's strength. It is valid only if the bets and acts really are replicas on the described part, which needs an enumerated, finite outcome set; and Karni & Vierø report no experiment, so what survives is a design, not a validated instrument |

## Limits

- **It detects existence, not content.** A positive pattern says the agent
  treats the undescribed part as non-null. It identifies no axis, and gives no
  generator for one — the same boundary [[unknown-unknowns]] draws.
- **The replica assumption is the whole argument.** If the bet and the act
  differ for any other reason — different stakes, different framing, a
  presumption about who settles the bet — the pattern appears without any
  unawareness. Karni & Vierø note (n. 22) that the partial specification is
  deliberately left for the agent to complete "in any way she can imagine",
  which is exactly the degree of freedom that makes the diagnosis fragile.
- **Proposed, not run.** The two patterns are presented as choice behaviour
  that *would* indicate awareness of unawareness; this note claims only that,
  and Karni & Vierø point at Schipper (2013) for the detection problem itself.
- **Needs settleable stakes.** The probe is built out of bets; an asker whose
  interlocutor never faces a resolvable wager has to substitute something for
  them, and nothing in the source says what.

## Related

[[catch-all-consequence]] · [[sense-of-ignorance]] · [[utility-of-the-unknown]] · [[grand-tour-question]] · [[objectives-generation-deficit]] · [[elicitation-protocols]]

[^s1]: karni-2017
