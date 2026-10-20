---
description: "The one quantity that turns two fully specified hypotheses and one Let $H_0$ and $H_1$ be **simple** hypotheses (each fixes one distribution of $x$), with densities $p(\\cdot \\mid H_0),"
aliases: ["Bayes factor", "LR", "weight of evidence"]
sources: ["good-1950", "good-1979", "kass-1995"]
---
# Likelihood ratio

> The one quantity that turns two fully specified hypotheses and one
> observation into a multiplicative update of the odds — and, in logs, into a
> running sum.

## Definition

Let $H_0$ and $H_1$ be **simple** hypotheses (each fixes one distribution of[^s1][^s2][^s3]
$x$), with densities $p(\cdot \mid H_0), p(\cdot \mid H_1)$ with respect to a
common dominating measure, and $p(x \mid H_0) > 0$:

$$\Lambda(x) = \frac{p(x\mid H_1)}{p(x\mid H_0)}$$

**Odds form of Bayes' rule.** Under those assumptions, for any prior with
$p(H_0) > 0$:

$$\underbrace{\frac{p(H_1\mid x)}{p(H_0\mid x)}}_{\text{posterior odds}} = \underbrace{\frac{p(H_1)}{p(H_0)}}_{\text{prior odds}} \times \underbrace{\Lambda(x)}_{\text{evidence}}$$

**Additivity in logs.** Good (1950) named $\log\Lambda$ the *weight of
evidence* and made its additivity the point of the quantity: if
$x_1,\dots,x_n$ are conditionally independent given each hypothesis, then

$$\log\Lambda(x_1,\dots,x_n) = \sum_i \log\Lambda(x_i)$$

so the posterior log-odds is the prior log-odds plus a sum of per-observation
terms. Conditional independence is an assumption of *this identity*, not a
caveat about applying it: without it only the joint ratio is defined and the
sum has no referent. Good's own account (Good 1979) traces the log form and
its units — the ban and the deciban — to Turing's wartime cryptanalytic work
at Bletchley Park, where the evidence for a wheel setting was accumulated
decibanwise.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Statistics / detection theory | likelihood ratio, LR | exact |
| Bayesian statistics | Bayes factor | **close** — Kass & Raftery (1995) define it as the ratio of *marginal* likelihoods, integrating each hypothesis over its parameter prior. It equals $\Lambda$ only when both hypotheses are simple, which is the sole case defined here; with composite hypotheses it depends on the parameter priors and $\Lambda$ does not exist |
| Cryptanalysis (Turing–Good) | weight of evidence, measured in bans / decibans | **close** — the quantity is $\log_{10}\Lambda$ in decibans, not $\Lambda$; a scale change, so it is the same object only up to the log and the base |
| Machine learning | log-odds update | **close** — the additive term in the recursion, again $\log\Lambda$ rather than $\Lambda$ |

The maximised likelihood ratio of a composite test (the statistic in
[[hypothesis-testing]]) is **not** this concept: its numerator is a supremum
over a parameter set, and neither the odds identity nor the additivity above
holds for it.

## Why it matters — accumulating evidence

*The reading in this section is this wiki's inference, not part of the
identity above.* It holds only if a per-answer surrogate for $\log\Lambda$
exists; see Transfer.

*If* each answer could be scored by some $\log\hat\Lambda$, then the record of
asking would have the shape

```text
log-odds(final) = log-odds(initial) + Σ log Λ̂(answer_i)
```

Two consequences follow **from the arithmetic of the sum**, given that
surrogate:

- Many weak but conditionally independent terms can outweigh one large term —
  a reason to expect that a long series of cheap questions is not dominated a
  priori by one decisive question. Whether this settles the "many weak
  questions" debate depends entirely on whether the surrogate and the
  independence hold, which is exactly what the debate is about.
- If independence fails, the sum inflates: the same evidence entered 100 times
  multiplies the accumulated log-odds by 100 while the true joint
  $\log\Lambda$ counts it once. This is where the concern about redundant
  questions belongs — the bookkeeping cannot detect its own double-counting.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | one i.i.d. draw from a family fixed by the hypothesis | one natural-language answer |
| $\Lambda(x)$ | ratio of two fully specified densities | undefined — needs a surrogate: a judge's score, a semantic-entropy proxy ([[semantic-entropy]]), a model's token log-probability ratio |
| What survives | the bookkeeping: odds multiply, logs add, order does not matter; and its consequence that many weak independent constraints can outweigh one strong one | |
| What does not | the numeric value of $\Lambda$; any [[calibration]] of the accumulated log-odds (it is not a posterior odds of anything); and additivity itself once answers are elicited adaptively from one respondent, where each answer is conditioned on the previous questions | |

## Limits

- Everything above is stated for **two simple hypotheses**. The wiki's own
  use — "does this answer favour world set A over world set B?" — is
  composite on both sides, so the object actually needed is a Bayes factor
  with priors over each set (Kass & Raftery 1995), not $\Lambda$.
- Additivity needs conditional independence given the hypothesis. Adaptive
  questioning breaks it by construction: the $i$-th question is chosen from
  the first $i-1$ answers.
- Requires $p(x\mid H)$ under both hypotheses. For a free-text answer no such
  density exists without a model; without the surrogate named in Transfer the
  sum in *Why it matters* is a metaphor, and this note claims nothing from it.
- Correlated evidence can drive the accumulated log-odds arbitrarily far while
  the real information arrived once — the failure mode
  Consistency cites this note for.

## Related

[[neyman-pearson-lemma]] · [[sprt]] · [[cusum]] · [[bayesian-estimation]] · [[hypothesis-testing]]

[^s1]: good-1950
[^s2]: good-1979
[^s3]: kass-1995
