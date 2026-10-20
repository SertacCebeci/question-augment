---
description: "The probability an agent puts on \"something I cannot describe will happen\" In the augmented state space (catch-all-consequence) the *sense of ignorance* is the prior mass on the imperfectly describ…"
aliases: ["sense of ignorance", "residual unawareness", "decreasing sense of ignorance", "increasing sense of ignorance"]
sources: ["karni-2017"]
---
# The sense of ignorance

> The probability an agent puts on "something I cannot describe will happen"
> — and Karni & Vierø's result that discovering a new possibility may raise
> it, lower it or leave it alone, with no way to tell which from the discovery
> itself.

## Definition / Mechanism

In the augmented [[possible-worlds|state space]] ([[catch-all-consequence]]) the *sense of[^s1]
ignorance* is the prior mass on the imperfectly describable states,
$\pi(\hat C^A \setminus C^A)$ — the agent's own estimate of how much of the
future is not yet describable.

Karni & Vierø (2017) note three coherent reactions to discovering a new
consequence: fewer consequences remain to be discovered; or the discovery
reveals that the agent was more ignorant than she believed and more remains;
or the discovery says nothing about the prevalence of unknown consequences.
They axiomatise the distinction behaviourally (their axiom A.11): compare the
agent's willingness to bet *on the realisation of an imperfectly describable
state* before and after the discovery. Less inclined afterwards = decreasing
sense of ignorance; more inclined = increasing.

Their Theorem 3 shows this preference pattern holds exactly when

$$\pi_0(\hat C_0^A \setminus C_0^A) \;\geq\; (\leq)\;\; \pi_1(\hat C_1^A \setminus C_1^A)$$

with strict inequality for strictly decreasing (increasing) ignorance and
equality for constant ignorance. The direction is a **primitive of the agent's
preferences**, not a consequence of the discovery.

Combined with the ratio constraints of [[reverse-bayesianism]], the
bookkeeping follows (their §5.2). Under a *constant* sense of ignorance,
probability mass must move from the old fully describable states $C_0^A$ to
the newly describable ones $C_1^A \setminus C_0^A$ **proportionally** — every
old state's probability is reduced equiproportionally. Under an *increasing*
sense of ignorance, some of that mass goes instead to the residual, and then
the net effect of growing awareness on $\pi(C_0^A)$ is, in their word,
unpredictable.

## Why it matters

Every hunting generator on Axes is used as though each axis found
shrinks what is left to find. This result says the sign of that change is free
and has to be supplied: one more discovery is consistent with a strictly
larger residual, and the model gives the asker no way to rule that branch out.
Two consequences for an asker: a count of discovered axes bounds nothing about
the remainder, and the quantity that *would* bound it is elicitable only from
bets that mention the residual, never from the discovery record.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision theory under unawareness (Karni & Vierø 2017) | sense of ignorance | exact — the paper's own term |
| This wiki | residual unawareness | close — this wiki's descriptive name for the same mass; not a term of the paper's |
| Decision theory under unawareness | decreasing / increasing sense of ignorance | exact — the two signs of the change in this quantity, not two quantities |
| Machine learning / statistics | **epistemic uncertainty** ([[uncertainty-decomposition]]) | **not this concept.** Epistemic uncertainty is uncertainty over parameters *inside* a declared model and vanishes with enough data on those parameters; this is mass assigned to states whose descriptions do not exist yet, and more data can increase it |

## Transfer

| | |
|---|---|
| **In its home field** | A subjective probability on a designated event of a derived state space, identified from an agent's bets before and after a discovery |
| **Here** | The asker's own estimate of what share of $W$ its current axis set cannot express — and how that estimate should move when a question returns something the model did not contain |
| **What survives** | The negative result, which needs no numbers: the residual mass can move either way, so no monotone "progress" reading of discovery is licensed. And the proportionality rule under constant ignorance: old worlds are scaled down uniformly, they are not re-ranked |
| **What does not** | Measurement. The quantity is identified from settleable bets on a finite derived state space; an asker with open-ended answers and no resolvable wagers has no procedure that returns this number, and the theorem supplies none |

## Limits

- **The theorem does not predict the direction** — it says which pairs of
  priors are consistent with which betting pattern. The claim above that
  discovery may increase ignorance is a statement about what is *representable*,
  not a measured frequency; no history of discovery in the paper or elsewhere
  here exhibits a residual mass measured before and after.
- **One discovery step.** The result is stated for a pair $C_0 \subset C_1$
  with the corresponding preference relations; nothing here constrains a
  sequence of discoveries or rules out oscillation.
- **Requires non-null residual states.** If the imperfectly describable states
  are null the agent is a standard [[expected-utility|expected utility]] maximiser and the quantity
  is identically zero — the case that describes most models of $W$ actually in
  use.
- **Elicitation is the bottleneck.** Both the axiom and the theorem are
  expressed through bets on imperfectly describable states, which presumes an
  agent that can hold a preference over an event it cannot describe.

## Related

[[catch-all-consequence]] · [[reverse-bayesianism]] · [[partially-specified-bet]] · [[unknown-unknowns]] · [[saturation]] · [[uncertainty-decomposition]]

[^s1]: karni-2017
