---
description: "The rule for updating belief with evidence, plus the loss function that The inversion was proved by Thomas Bayes in the essay Richard Price communicated posthumously to the Royal Society (Bayes 1763,"
aliases: ["Bayesian updating", "posterior inference", "sequential Bayes"]
sources: ["bayes-1763", "laplace-1774", "wald-1950", "berger-1985", "lehmann-1998"]
---
# Bayesian estimation

> The rule for updating belief with evidence, plus the loss function that
> turns a belief into one answer. The loop step of any question-and-answer
> process — if a likelihood exists.

## Bayes

The inversion was proved by Thomas Bayes in the essay Richard Price[^s1][^s2][^s3][^s4][^s5]
communicated posthumously to the Royal Society (Bayes 1763, *Phil. Trans.*
53) and stated as a general "probability of causes" by Laplace (1774):

$$p(\theta\mid x) = \frac{p(x\mid\theta)\,p(\theta)}{p(x)}$$

## Sequential updating

The critical property: **yesterday's posterior is today's prior.**

$$p(\theta\mid x_1,x_2) \propto p(x_2\mid\theta)\,\underbrace{p(\theta\mid x_1)}_{\text{new prior}}$$

This is algebra from Bayes' rule, not a further result — but it holds in this
form only when $x_2 \perp x_1 \mid \theta$. Under that condition you need not
retain the whole history; the current belief suffices. This is the sequential
form of a [[sufficient-statistic]].

## Estimators

Turning a posterior into a single answer is a decision problem in the sense
of Wald (1950): choose the action minimising expected loss. The Bayes
estimator minimises **posterior** expected loss, and the standard
correspondence is stated in this form by Berger (1985) and by Lehmann & Casella (1998):

| Loss function | Bayes estimate |
|---|---|
| Squared error | Posterior mean (MMSE) |
| Absolute error | Posterior median |
| 0–1 (discrete $\Theta$) | Posterior mode (MAP) |

The third row is exact when $\Theta$ is a discrete, enumerated set. For
continuous $\theta$ the 0–1 loss has to be taken as the limit of a shrinking
tolerance window, and MAP is the limiting Bayes rule (Berger 1985).

**This wiki's inference, not a result:** a design decision is read as 0–1
loss — either the right choice is made or it is not — so its counterpart is
MAP: pick the most likely world, not the average, because the average of two
designs is usually a design that does not work. This reading assumes what
the third row above assumes: a **discrete, enumerated set of candidate
designs**. Before the candidates are enumerated there is no mode to take and
the reading has no content.

## Why it matters — this wiki's conjecture

*The identification of one-question-at-a-time asking with sequential Bayes is
this wiki's inference, not a result: no likelihood over natural-language
answers has been specified, so nothing below is proved.*

Under that identification, answering one question at a time without
second-order thinking is the recursion above, and the recursion loses nothing
provided the belief is carried exactly. In practice the agent carries not a
belief but **text**:

```text
In theory:   belief(t) = f(belief(t-1), answer_t)     — lossless
In practice: context(t) = context(t-1) + answer text  — lossy
```

Recording each settled point durably before asking the next question is what
the recursion would require if the identification held — the conjecture's
one operational consequence.

## Known as

| Field | Name there | Relation |
|---|---|---|
| statistics | Bayesian updating | exact |
| statistics, machine learning | posterior inference | close — names computing $p(\theta\mid x)$ in general, including one-shot inference with no update sequence |
| signal processing, filtering | sequential Bayes | close — names the recursion alone, not the loss-to-estimator half of this note |

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation $x$ | an i.i.d. draw from a known family | one natural-language answer |
| $p(x\mid\theta)$ | a known parametric likelihood | undefined; needs a surrogate |
| Belief state | a posterior distribution over $\theta$ | accumulated text |
| What survives | the recursion — carry the current belief, not the history — and mode-over-mean once the candidates are discrete and enumerated | |
| What does not | losslessness; the optimality of MAP/MMSE; any quantitative posterior | |

## Limits

- Requires a likelihood $p(x \mid \theta)$. For natural-language answers no
  such function exists; "sequential updating" is a metaphor until a model is
  fitted — this is why *Why it matters* is marked as conjecture.
- The recursion's "carry only the belief" claim rests on conditional
  independence of successive answers given $\theta$. Answers that refer back
  to earlier answers break it, and then the history is not discardable.
- Lossless propagation assumes the posterior is representable. Text is not a
  posterior — the note's own point.
- MAP is the right estimator under 0–1 loss **only if** the hypothesis set is
  the right one *and* enumerated.
- The three book sources are cited at work level for the loss-to-estimator
  correspondence, not by section or theorem number.

## Related

[[likelihood-ratio]] · [[sufficient-statistic]] · [[maximum-entropy-principle]] · [[value-of-information]]

[^s1]: bayes-1763
[^s2]: laplace-1774
[^s3]: wald-1950
[^s4]: berger-1985
[^s5]: lehmann-1998
