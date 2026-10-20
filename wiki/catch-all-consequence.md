---
description: "One named cell for \"none of the outcomes I have listed\" — the device that Karni & Vierø (2017) build the state space from primitives rather than assuming it: a finite set of basic actions $A$,"
aliases: ["catch-all consequence", "none of the above", "abstract consequence ¬C"]
sources: ["karni-2017"]
---
# The catch-all consequence

> One named cell for "none of the outcomes I have listed" — the device that
> makes an admittedly incomplete axis set into a space that is exhaustive by
> construction, and can therefore carry a probability and be bet on.

## Definition / Mechanism

Karni & Vierø (2017) build the [[possible-worlds|state space]] from primitives rather than[^s1]
assuming it: a finite set of basic actions $A$, a finite set of **feasible
consequences** $C$ the decision maker is aware of, and one abstract
consequence $x = \neg C$, read *"none of the above"*. With
$\hat C := C \cup \{x\}$ the **augmented conceivable state space** is

$$\hat C^A := \{\, s : A \to \hat C \,\}$$

— every assignment of an extended consequence to each action — and is
exhaustive by definition. It splits in two:

- **fully describable** states $C^A = \{s : A \to C\}$: every action's outcome
  is one the agent can name;
- **imperfectly describable** states $\hat C^A \setminus C^A$: at least one
  action yields $x$.

Their worked case — two medications, two known outcomes — gives nine states of
which four are fully describable. $x$ is deliberately structureless: there may
be one unknown consequence, any finite number, infinitely many, or none at
all, and $x$ covers all of these at once.

The second restriction is what keeps the construction honest. *Conceivable
acts* $F = \{f : \hat C^A \to C\}$ pay only nameable consequences, because a
bet paying "$x$" in a state where nothing is discovered could never be
settled. *Extended conceivable acts* are

$$F^* := \{\, f^* : \hat C^A \to \hat C \;\mid\; f^{*-1}(x) \subseteq \hat C^A \setminus C^A \,\}$$

— you may promise to deliver a newly discovered consequence **only in the
states where a discovery occurs**, since there the promise can be kept. This
is the boundary of what can be meaningfully committed to about the unknown.

Karni & Vierø's §5.4 states the matching negative result: bolting a catch-all
outcome onto a model that takes the state space as a *primitive* (Savage,
Anscombe–Aumann) does not reproduce this. Such a model must let the catch-all
be received for sure — a constant act paying $\hat x$ — which an unknown
unknown by definition cannot be described well enough to be; and with the
space fixed it can assign no probability to a discovery and represent no
change in the agent's ignorance afterwards.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision theory under unawareness (Karni & Vierø 2017) | catch-all consequence | exact |
| Decision theory under unawareness | "none of the above", abstract consequence $\neg C$ | exact — the paper's own reading of the same element |
| Decision theory (Machina 2003, as reported in karni-2017 n. 5) | catch-all **state** labelled "none of the above" | close — **not this concept**: it labels an unspecified *state*, whereas $x$ is an unspecified *consequence*, which is what lets the state space refine when a discovery occurs |

## Transfer

| | |
|---|---|
| **In its home field** | Choice theory in which the state space is *derived* from finite sets of actions and consequences, and every act must be settleable once uncertainty resolves (revealed preference) |
| **Here** | $C$ is the asker's list of outcomes on an axis of $W$, $x$ is the admission that the list is incomplete, and an "act" is a commitment made before the answers arrive |
| **What survives** | The construction: one extra cell makes an incomplete space formally exhaustive, and the describable / non-describable partition is then an event that can carry probability ([[sense-of-ignorance]]) and a price ([[utility-of-the-unknown]]). The settlement rule survives too — it says exactly where a commitment about the unknown is meaningful |
| **What does not** | The identification. $A$ and $C$ must be finite and known, and pinning down $\pi$ needs a rich family of settleable bets, which an asker facing open-ended answers does not have. And it does not survive as a *generator*: $x$ names the residual, it does not describe it, so nothing here produces the missing axis |

## Limits

- **The construction is a placeholder, not a hunt.** $x$ has no internal
  structure, so this note's claim is only that the residual becomes
  quantifiable and priceable — it supports no distinction inside the residual
  and therefore no question that would open the missing axis. Everything
  [[unknown-unknowns]] says about criteria defined over a represented space
  still applies inside $C$.
- **Consequences only.** Karni & Vierø (2017) treat the discovery of new
  consequences; the discovery of new basic *actions* refines the space
  differently and is explicitly left aside in this paper.
- **Exhaustiveness is definitional.** $\hat C^A$ is exhaustive because $x$ is
  defined as the complement of $C$ — that is a property of the representation,
  not evidence that the agent's list plus one cell covers what can happen.
- **No settleable bets, no content.** An asker whose commitments are never
  resolved ex post has no analogue of $F^*$, and the restriction that makes
  preferences over $x$ meaningful then has nothing to restrict.

## Related

[[unknown-unknowns]] · [[possible-worlds]] · [[utility-of-the-unknown]] · [[reverse-bayesianism]] · [[sense-of-ignorance]] · [[maximum-entropy-principle]]

[^s1]: karni-2017
