---
description: "The expected information gain from asking a question. The central quantity **Assumptions.** $X$ and $Y$ range over discrete (finite or countable) alphabets; a joint distribution $p(x,y)$ exists;"
aliases: ["I(X;Y)", "transinformation"]
sources: ["shannon-1948", "cover-2006", "quinlan-1986"]
---
# Mutual information

> The expected information gain from asking a question. The central quantity
> of this wiki.

## Definition (Shannon 1948; Cover & Thomas 2006, ch. 2)

**Assumptions.** $X$ and $Y$ range over discrete (finite or countable)[^s1][^s2][^s3]
alphabets; a joint distribution $p(x,y)$ exists; $H(X)$ and $H(Y)$ are
finite. Everything below is stated under those assumptions.

$$I(X;Y) = H(X) - H(X\mid Y) = H(Y) - H(Y\mid X)$$

This identity is Shannon's *rate of transmission* $H(x) - H_y(x)$ (Shannon 1948, part I) under the name mutual information; the equivalent
[[kl-divergence]] form between the joint and the product of marginals is the
standard modern statement (Cover & Thomas 2006, ch. 2):

$$I(X;Y) = D_{KL}\big(p(x,y)\ \|\ p(x)p(y)\big)$$

For continuous variables $H$ becomes **differential [[entropy]]**: it is no
longer a count of [[possible-worlds|possible worlds]] and can be negative, so the reading below
("how few worlds remain") does not transfer, and $I \geq 0$ then rests on the
joint being absolutely continuous with respect to the product of the
marginals.

## Properties

Under the assumptions above:

- $I(X;Y) \geq 0$ — **information is never negative** (in expectation)
- $I(X;Y) = I(Y;X)$ — symmetric
- $I(X;Y) = 0 \iff X \perp Y$ — an irrelevant question yields zero

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | mutual information $I(X;Y)$ | exact |
| Bayesian experimental design | expected information gain | close — [[expected-information-gain]] is this functional indexed by a design $q$ and maximised over $q$: a selection criterion |
| Machine learning (trees) | information gain of a split | close — exact as a functional, but what a tree computes is the **empirical plug-in** estimate at a node, biased upward for high-arity splits; the reason Quinlan (1986) introduced gain ratio |
| Active learning | uncertainty-sampling objective | close — greedy, one step |

## Why it matters

Let $X$ be the **unknown** — the state of $W$, written $\theta$ in the
Bayesian notes — and $Y$ the answer to a question $q$:

$$I(X;Y) = \underbrace{H(X)}_{\text{current uncertainty}} - \underbrace{H(X\mid Y)}_{\text{what remains after}}$$

So **the informational value of a question is how few possible worlds are
expected to remain after asking it.** This quantity, indexed by a design $q$
and maximised over $q$, is [[expected-information-gain]] — a selection
criterion, not the same object.

## Consequence of symmetry

$I(X;Y) = I(Y;X)$ says a question carries information only if **its answer
cannot be predicted**. If the answer is already determined, $H(Y)$ is small,
so $I$ is small. This is the formal version of the observation in
[[surprisal]].

## Transfer

| | |
|---|---|
| **Home field** | a joint distribution $p(x,y)$ over two random variables with known discrete alphabets, from which both entropies are computable |
| **Here** | $X$ is an implicit belief over $W$ with no written prior; $Y$ is one natural-language answer, drawn once, from an unbounded answer space |
| **What survives** | the entropy-drop *ranking* logic — a question is scored before it is answered, from the distribution of its answers — and the sign result $I \geq 0$ under the assumptions above |
| **What does not** | the number. A free-text answer has no fixed alphabet and $p(y\mid q)$ is a model estimate, so the score inherits the model's [[calibration]] error and the induced ranking carries no guarantee |

## Limits

- **Measures information, not value.** $I > 0$ with $\mathrm{VoI} = 0$ is
  common: a question can be maximally informative and change no decision
  ([[value-of-information]]). The sentence above is about informational
  value only.
- The counting reading and the identity as stated assume **discrete
  alphabets and finite entropies**; the continuous case replaces $H$ by
  differential entropy and loses the world count.
- $I \geq 0$ assumes the act of asking does not itself move the belief state.
  A question whose presupposition is accommodated updates $W$ before any
  answer exists ([[presupposition-accommodation]]).
- Symmetric: it cannot say which way information flows.
- It is an **expectation**. A question with high $I$ can still return a
  useless answer this time.
- Needs the joint distribution $p(x,y)$; in practice $p(y\mid q)$ is a model
  estimate and inherits its calibration error.

## Related

[[entropy]] · [[conditional-entropy]] · [[expected-information-gain]] · [[value-of-information]] · [[data-processing-inequality]]
- [[generalized-binary-search]]

[^s1]: shannon-1948
[^s2]: cover-2006
[^s3]: quinlan-1986
