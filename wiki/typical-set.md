---
description: "Almost all probability mass concentrates on a small subset of possible For i.i.d. $X_1,\\dots,X_n \\sim p$ over a finite alphabet $\\mathcal{X}$,"
aliases: ["epsilon-typical set", "weakly typical set"]
sources: ["shannon-1948", "cover-2006"]
---
# Typical set

> Almost all probability mass concentrates on a small subset of possible
> worlds.

The **asymptotic equipartition property (AEP)** is the convergence theorem;[^s1][^s2]
the **typical set** is the object that theorem defines. This note is about
the set, and states the theorem only as far as the set needs it.

## Definition

For i.i.d. $X_1,\dots,X_n \sim p$ over a finite alphabet $\mathcal{X}$, the
AEP states

$$-\frac{1}{n}\log p(X_1,\dots,X_n) \to H(X) \quad \text{in probability.}$$

The $\varepsilon$-typical set $A_\varepsilon^{(n)}$ is the set of sequences
whose empirical log-probability is within $\varepsilon$ of $H(X)$. Each of
its members has probability $\approx 2^{-nH}$, its total probability tends
to 1, and its size is $\approx 2^{nH}$.

The concentration result is Shannon (1948); the modern statement of the AEP
and of the typical set, with the bounds on $|A_\varepsilon^{(n)}|$, is
Chapter 3 of Cover & Thomas (2006).

## Known as

| Field | Name there | Relation |
|---|---|---|
| information theory | $\varepsilon$-typical set | exact |
| information theory | weakly typical set | exact — as against the *strongly* typical (letter-typical) set, which is a different set |
| information theory | asymptotic equipartition property, AEP | close — the AEP is the limit theorem, this set is what it defines; the two are cited together and are not the same object |

## The hard consequence

There are $|\mathcal{X}|^n$ possible sequences but only $\approx 2^{nH}$
carrying the mass. As long as $H < \log|\mathcal{X}|$, the ratio goes to
zero exponentially (Cover & Thomas 2006, ch. 3).

## Why it matters

The point coverage arguments miss: **most [[possible-worlds|possible worlds]] are already
irrelevant.**

```text
Combinatorially possible designs  :  astronomical
Actually coherent and plausible   :  a tiny subset
```

This softens the goal of "sweeping the entire question space": what needs
sweeping is not the whole space but the region carrying the mass.

**Conjecture (this wiki, not in the sources):** a generative model's prior
is already roughly concentrated on the typical set of its training
distribution, which would be why model-generated questions cluster in the
"plausible" region; and on an axis the model has never represented there is
no learned notion of typicality at all, so that axis stays invisible.
This is an inference from the theorem by analogy, with no measurement
behind it here; it belongs in its own `type: conjecture` note.

## Transfer

| | In its home field | Here |
|---|---|---|
| Object | an i.i.d. sequence $X_1..X_n$ over a finite alphabet | one design, many decisions — no $n$, no i.i.d. structure |
| $2^{nH}$ | size of the typical set | undefined — no $n$, no $H$ |
| What survives | that combinatorial size is a bad proxy for where the mass is: sweep the mass, not the space | |
| What does not | the count, the exponential rate, the $\to 1$ probability guarantee, and any claim about *which* worlds are typical | |

## Limits

- The theorem as stated assumes i.i.d. draws and a finite alphabet (so $H$
  is finite), and gives convergence **in probability** — the weak AEP. Not
  pointwise, not almost-sure; the almost-sure and stationary-ergodic
  versions are separate results this note does not carry a source for and
  does not use.
- Asymptotic in $n$. A design is one object, not a long i.i.d. sequence, so
  the numbers do not transfer; only the qualitative claim in Transfer does.
- The "plausible designs" reading is an analogy, and the marked paragraph in
  *Why it matters* is this wiki's conjecture, not a consequence of the
  theorem.
- That conjecture is self-undercutting as a guide: if a model's prior
  concentrates on its typical set, that concentration is the very mechanism
  hiding unmodelled axes.

## Related

[[entropy]] · [[possible-worlds]] · [[semantic-entropy]] ·
[[source-coding-theorem]]

[^s1]: shannon-1948
[^s2]: cover-2006
