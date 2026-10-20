---
description: "A single parameter, identified from choices, for how an agent feels about Karni & Vierø's Theorem 1 gives a subjective expected utility representation over lotteries on the extended acts of catch-a…"
aliases: ["utility of the unknown", "utility of indescribable consequences"]
sources: ["karni-2013", "karni-2017"]
---
# The utility of the unknown

> A single parameter, identified from choices, for how an agent feels about
> discovering something it cannot yet describe — separate from how likely it
> thinks the discovery is, and not computable from any information measure.

## Definition / Mechanism

Karni & Vierø's Theorem 1 gives a subjective [[expected-utility|expected utility]] representation[^s1][^s2]
over lotteries on the extended acts of [[catch-all-consequence]]: preferences
satisfy their axioms (A.1)–(A.7) exactly when there are affine functions $U$
on $\Delta(C)$ and $U^*$ on $\Delta(\hat C)$ that agree on $\Delta(C)$, and a
unique probability measure $\pi$ on $\hat C^A$, with

$$\sum_{s \in C^A} \pi(s)\,U(\varphi_s(\mu)) \;+\; \sum_{s \in \hat C^A \setminus C^A} \pi(s)\,U^*(\varphi_s(\mu))$$

ordering the choices. The representation therefore has **three** parts:
beliefs $\pi$ over states, a Bernoulli utility $u$ over the known
consequences, and a number $u^*(x)$ — the utility of the abstract consequence
"none of the above".

$u^*(x)$ is cardinal, unique up to the same positive linear transformation as
$u$. Comparing two agents, the one with the higher $u^*(x)$ exhibits
*excitement* (optimism) toward the unknown, the one with the lower exhibits
*fear* (pessimism) — that comparative reading is an interpretation of
*differences* in the parameter, not the parameter itself. If the imperfectly
describable states are null, $u^*(x)$ drops out and the agent is a standard
expected utility maximiser.

The parameter has teeth because it can reverse a choice. In Karni & Vierø's
two-medication example, the tried medication $a_1$ is believed never to yield
an unforeseen side effect and the new one $a_2$ may; under their
representation $a_2 \succ a_1$ requires $U(c_1) < U^*(x)$ together with a
condition on the probabilities. And the comparison they draw is sharp: their
earlier model (Karni & Vierø 2013, `karni-2013`), whose [[possible-worlds|state space]] consists
solely of fully describable states, cannot express the distinction between the
event where $a_1$ produces an unforeseen consequence and the event where $a_2$
does, so on the same data the two models can predict **opposite** choices.

## Why it matters

Whether to take the action that might reveal an axis you do not have is, in
this representation, not one question but two: how likely is this action to
reveal something ($\pi$ on the residual states, which differs across actions),
and what is the unknown worth ($u^*(x)$, a taste). [[value-of-information]]
prices a question by the decision change it produces *within a fixed decision
problem* and says of itself that a question opening an unmodelled axis is
outside its bound, not below it. This is the missing half of that sentence: a
number for the unmodelled branch, obtained from revealed preference rather
than from a model of what might be found.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision theory under unawareness (Karni & Vierø 2017) | utility of the unknown, $u^*(x)$ | exact |
| Decision theory under unawareness | utility of indescribable consequences | exact — the paper's keyword for the same parameter |
| Decision theory under unawareness | attitude toward the unknown (fear / excitement) | close — **not an alias of this concept**: it names the comparative notion Karni & Vierø read off *differences* in $u^*(x)$ between two agents, where this note's object is the cardinal parameter of one agent's representation |
| Decision theory (Grant & Quiggin 2015, as reported in karni-2017 §5.5) | favourable / unfavourable **surprise** consequences | close — **not this concept**: there unforeseen consequences are assumed better or worse than every standard consequence, whereas $u^*(x)$ lets the unknown rank anywhere among the known ones |

## Transfer

| | |
|---|---|
| **In its home field** | A cardinal utility parameter in a subjective expected utility representation, unique up to positive linear transformation, identified from preferences over settleable extended acts |
| **Here** | The pull toward asking a question, or taking an action, whose value lies in the chance that it produces something the current axis set cannot name |
| **What survives** | The decomposition: exploration pull = probability of discovery (action-dependent) $\times$ a utility of the unknown (agent-dependent). It explains why two askers with the same model hunt at different rates, and it makes "curiosity" a parameter of the representation rather than a residual |
| **What does not** | The number and its uniqueness. Identification needs an agent whose bets on the residual can be settled and whose preferences satisfy the separability axiom (A.7); with open-ended answering neither holds, so $u^*(x)$ transfers as a distinction, not as a measurement. Nor does it survive as a normative claim — nothing says what $u^*(x)$ *should* be |

## Limits

- **$x$ is structureless, so $u^*(x)$ is one number for everything unknown.**
  It cannot express that some undiscovered consequences would be welcome and
  others catastrophic; the whole residual gets one valuation.
- **It is a taste, not a forecast.** The parameter is identified from choices
  and carries no information about what is actually out there; a high
  $u^*(x)$ is as consistent with a well-founded expectation of gain as with
  wishful thinking.
- **The opposite-prediction claim is internal.** The divergence from
  `karni-2013` is a comparison of two models' representations under stated
  probability conditions, not an experiment: no data is reported that
  discriminates between them.
- **Not needed for belief dynamics.** Karni & Vierø remark that Theorem 2's
  account of how beliefs evolve does not require assigning utility to the
  abstract consequence at all — so this parameter is load-bearing for *choice*
  under unawareness, not for updating.

## Related

[[catch-all-consequence]] · [[value-of-information]] · [[sense-of-ignorance]] · [[expected-utility]] · [[partially-specified-bet]] · [[unknown-unknowns]]

[^s1]: karni-2013
[^s2]: karni-2017
