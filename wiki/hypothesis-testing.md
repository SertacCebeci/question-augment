---
description: "The decision-theoretic form of resolving uncertainty: which world are we in — Neyman & Pearson (1933) fixed the two error types and the level-$\\alpha$ framing: for a test is chosen among those whos…"
aliases: ["Neyman–Pearson framework"]
sources: ["neyman-1933", "neyman-1928", "lehmann-1959"]
---
# Hypothesis testing

> The decision-theoretic form of resolving uncertainty: which world are we in —
> and at what error rates you agree in advance to be wrong.

## Setup

Neyman & Pearson (1933) fixed the two error types and the level-$\alpha$[^s1][^s2][^s3]
framing: for

$$H_0: X \sim p_0 \qquad H_1: X \sim p_1$$

a test is chosen among those whose false-alarm rate is at most $\alpha$, and
judged by its miss rate $\beta$.

| | Truly $H_0$ | Truly $H_1$ |
|---|---|---|
| Said $H_0$ | correct | **miss** ($\beta$) |
| Said $H_1$ | **false alarm** ($\alpha$) | correct |

At a fixed sample size the trade-off is forced: lowering $\alpha$ raises
$\beta$. Both fall together only with **more data** — more observations drawn
from the same specified model.

## Known as

| Field | Name there | Relation |
|---|---|---|
| statistics | Neyman–Pearson framework | exact |
| statistics | Type I and Type II errors | *not this concept* — it names the error pair this framework tabulates, a part of the object rather than another name for it. The framework is the level-$\alpha$ decision rule; the error pair is what that rule books. |

## Why it matters

The tempting reading of a design question is as a small hypothesis test:

```text
H0: the design goes this way
H1: the design goes that way
answer = observation
```

*This wiki's reading, not a result:* **if** each answer could be treated as an
observation with a likelihood under two specified densities, the
$\alpha/\beta$ trade-off would say decision risk cannot be driven to zero,
only shrunk with the number of observations — which would be a mathematical
argument for large [[question-budgets|question budgets]]. The observation model does not hold (see
Transfer), so this is a conjecture here, and the arithmetic over a question
count is not licensed by the theorem.

What survives without that assumption is the **bookkeeping**: two error types
that cannot both be minimised at fixed evidence, and the third option — as in
[[sprt]], **"do not decide yet, ask one more"**.

## Composite hypotheses

Design hypotheses are not simple but **composite**: "this way" contains
infinite variation. A uniformly most powerful test — one best critical region
against every alternative at once — then generally fails to exist; Lehmann (1959) sets out both the restricted settings where it does (monotone
[[likelihood-ratio|likelihood ratio]], one-sided alternatives) and the two-sided cases where it
does not. This is the limit of [[neyman-pearson-lemma]]. What is used instead
is the generalised likelihood-ratio criterion $\lambda$ of Neyman & Pearson (1928): maximise the likelihood within each hypothesis and compare the maxima.
It is a rule that always exists, not an optimal one.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | i.i.d. sample from a known family | one natural-language answer to a design question |
| $p_0, p_1$ and $\Lambda(x)$ | two fully specified densities, ratio computable | undefined — no density over answers; needs a surrogate (a judge, a scored rubric) |
| What survives | the two-error-type bookkeeping, the forced $\alpha/\beta$ trade-off at fixed evidence, and the third option "do not decide yet, ask one more" | |
| What does not | the identification of "more data" with "more questions" (answers are neither independent nor identically distributed), any error-rate arithmetic over a question budget, and the optimality results | |

## Limits

- The count argument assumes each answer is an independent observation with a
  likelihood under both hypotheses; a free-text design answer supplies
  neither, so the $\alpha/\beta$ arithmetic does not transfer to a question
  budget.
- Binary and simple: composite hypotheses lose the optimality results, as
  above.
- $\alpha/\beta$ presuppose hypotheses fixed before the data. Design questions
  define their hypotheses as they go.
- Error rates are long-run frequencies, not the probability that *this*
  decision is wrong.
- `neyman-1933` [?] was carried over from before the verifier existed;
  `neyman-1928` and `lehmann-1959` are added here and are unverified until the
  verifier confirms them.

## Related

[[neyman-pearson-lemma]] · [[likelihood-ratio]] · [[sprt]] · [[roc-curve]]

[^s1]: neyman-1933
[^s2]: neyman-1928
[^s3]: lehmann-1959
