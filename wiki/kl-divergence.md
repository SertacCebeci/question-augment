---
description: "The \"surprise gap\" between two distributions. How far the prior travelled to For two probability distributions $P$ and $Q$ on a **common discrete support** $\\mathcal{X}$: The assumptions the line c…"
aliases: ["relative entropy", "Kullback–Leibler divergence", "realised information gain"]
sources: ["kullback-1951", "cover-2006"]
---
# KL divergence (relative entropy)

> The "surprise gap" between two distributions. How far the prior travelled to
> become the posterior.

## Definition (Kullback and Leibler, 1951)

For two probability distributions $P$ and $Q$ on a **common discrete support**[^s1][^s2]
$\mathcal{X}$:

$$D_{KL}(P \| Q) = \sum_{x \in \mathcal{X}} p(x)\log_2\frac{p(x)}{q(x)}$$

The assumptions the line carries, and which the properties below inherit:

- **A common space.** Discrete $\mathcal{X}$, or — the general form Kullback and Leibler (1951) give — $P$ and $Q$ both absolutely continuous with respect to
  one dominating measure $\lambda$, with the sum replaced by
  $\int p\log(p/q)\,d\lambda$.
- **Conventions** $0\log\frac{0}{q}=0$ and $p\log\frac{p}{0}=\infty$ (Cover & Thomas, 2006). Hence the value is finite only when $P \ll Q$: $Q$ must put
  mass wherever $P$ does.
- **Direction.** Kullback and Leibler introduced it as a *directed* divergence
  — mean information per observation for discriminating one hypothesis from
  another. The symmetrised sum $D_{KL}(P\|Q)+D_{KL}(Q\|P)$ is a different
  quantity (the $J$-divergence) and is not what this note writes $D_{KL}$.

## Properties

Under exactly those assumptions, $P$ and $Q$ normalised on the same space:

- $D_{KL}(P\|Q) \geq 0$, with equality iff $P = Q$ — Gibbs' inequality, from
  Jensen's inequality applied to $-\log$; Kullback and Leibler (1951) prove it
  for the directed divergence, and Cover & Thomas (2006) state it as the
  [[cramer-rao-bound|information inequality]]. It fails if either argument is unnormalised.
- **Not symmetric**: $D_{KL}(P\|Q) \neq D_{KL}(Q\|P)$ in general.
- Not a metric (violates the triangle inequality).

## Interpretation

The average number of extra bits paid when you encode for $Q$ but the world is
$P$ (Cover & Thomas, 2006) — **the cost of the wrong model**. This reading
presupposes an actual code over $\mathcal{X}$.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | relative entropy | exact |
| Bayesian statistics | information gain (realised) | exact |
| Machine learning | KL loss / KL regulariser | exact |
| Statistical physics | free-energy difference | close |

## Why it matters

The *realised* information gain of an answer:

$$IG = D_{KL}(\text{posterior} \| \text{prior})$$

[[mutual-information]] is the expectation of this over answers — the estimate
before asking. KL is the realised value after the answer arrives.

```text
before asking  →  I(X;Y)            expected gain      (for question selection)
after the answer →  D_KL(post‖prior)  realised gain      (surprise measurement)
```

*This wiki's inference, not a result of the theorem above:* a realised
$D_{KL}$ far above what the pre-answer expectation predicted is a candidate
signal that the incoming answer disturbs decisions upstream of its own node,
not only that node. The upstream reading — "ancestor–descendant contradiction"
— is a house coinage set out in [[cusum]], where the accumulate-then-threshold
version of it lives; neither the coinage nor the threshold comes from the
literature cited here.

## Transfer

| | |
|---|---|
| In its home field | two explicitly specified distributions over one measurable space with a common dominating measure |
| Here | prior and posterior over the remaining worlds $W$ after one natural-language answer — neither distribution is written down |
| What survives | non-negativity and the equality case; the asymmetry; the ordering "larger value = larger revision", once a surrogate fixes both distributions |
| What does not | the bits-wasted coding reading (no code over $W$ exists); finiteness (a posterior with support the prior lacked gives $\infty$); any localisation of the disturbance — $D_{KL}$ is one scalar over the whole belief and names no node |

## Limits

- Asymmetric and not a metric; "distance" language is loose.
- Infinite when the posterior has support where the prior had none — which is
  precisely what a shocking answer does. The "surprise" reading breaks at the
  extreme it is meant to capture.
- Needs both distributions explicit; over free-text beliefs it is a metaphor
  until a surrogate is chosen.
- The upstream claim above rests on two things this note does not supply: the
  realised KL **localises nothing** — flagging a particular upstream decision
  needs a dependency structure over decisions on top of it — and
  "unexpectedly large" needs a declared threshold, which neither
  Kullback and Leibler (1951) nor Cover & Thomas (2006) provide.

## Related

[[mutual-information]] · [[surprisal]] · [[maximum-entropy-principle]] · [[fisher-information]] · [[cusum]]

[^s1]: kullback-1951
[^s2]: cover-2006
