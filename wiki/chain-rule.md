---
description: "Why the information from 10,000 questions can be accumulated sequentially — Entropy and its additive decomposition over a joint distribution are Shannon's (1948);"
aliases: ["chain rule for entropy", "chain rule for mutual information"]
sources: ["shannon-1948", "cover-2006"]
---
# Chain rule

> Why the information from 10,000 questions can be accumulated sequentially —
> and why that licence says nothing about what any one of them is worth.

## For entropy

$$H(X_1,\dots,X_n) = \sum_{i=1}^{n} H(X_i \mid X_1,\dots,X_{i-1})$$[^s1][^s2]

[[entropy|Entropy]] and its additive decomposition over a joint distribution are
Shannon's (1948); the standard modern statement of both identities on this
page is Cover & Thomas (2006), ch. 2.

## For mutual information

$$I(X_1,\dots,X_n; Y) = \sum_{i=1}^{n} I(X_i; Y \mid X_1,\dots,X_{i-1})$$

The second identity follows from the first through
$I(\cdot\,;Y) = H(\cdot) - H(\cdot \mid Y)$ (Cover & Thomas 2006, ch. 2).

## The theoretical licence

Answering one question at a time, without second-order thinking, loses no
information — **provided all $n$ questions are eventually asked and the set of
questions does not depend on the answers** — thanks to the chain rule:

```text
total information = information of Q1
                  + information of Q2 (GIVEN Q1)
                  + information of Q3 (given Q1, Q2)
                  + ...
```

Under those two conditions the total is **independent of ordering**. Ask in
any order; once all are asked, the information collected is the same.

## But order still matters

The chain rule fixes the total, **not the per-step gain**. Two consequences,
one of them weaker than it looks:

1. **If you stop early, order decides everything.** Stopping after the first
   50 of 10,000 questions makes the choice of those 50 decisive. This is the
   source of **path dependence**: the order of questions decides the outcome.
2. **The average per-step gain falls; a monotone decline does not follow.**
   The whole sum is bounded by $H(Y)$, so the *average* of the $n$ terms is at
   most $H(Y)/n$ and shrinks as $n$ grows — that much is the chain rule plus
   $I \le H$. It does **not** follow that $I(X_i;Y \mid X_{<i})$ is
   non-increasing in $i$: conditioning can *raise* conditional [[mutual-information|mutual information]]. Cover & Thomas (2006, ch. 2) give the standard counterexample
   — $X$ and $Y$ independent, $Z$ their sum, so $I(X;Y)=0$ while
   $I(X;Y \mid Z) > 0$; information that exists only jointly is called
   **synergy**. A monotone decline of the per-step gain is the
   **adaptive-submodularity assumption on the objective, restated**
   ([[adaptive-submodularity]]), not a consequence of this identity. *This
   wiki's reading:* the 10,000th question is worth less than the 10th **on
   average over the run**, not necessarily in sequence.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Information theory | chain rule for entropy | close — the identity for $H$; the same decomposition, applied to one functional |
| Information theory | chain rule for mutual information | close — the identity for $I$, obtained from the entropy form by $I = H - H(\cdot\mid Y)$ |

Not this concept: the **chain rule of calculus** (composition of derivatives),
and the probability **chain rule / product rule**
$p(x_1..x_n)=\prod_i p(x_i \mid x_{<i})$ — a factorisation of a *distribution*,
whose expected log is this identity but which is a different object with a
different measure. *Conditional entropy* names a term of the sum, not the sum
([[conditional-entropy]]).

## Transfer

| | In its home field | Here |
|---|---|---|
| Objects | $X_1,\dots,X_n,Y$ jointly distributed, with a **known** joint law | one question = one variable; one natural-language answer = its realisation |
| The sum | bits of an information measure defined by that law | "what the answers told you", accumulated question by question |
| What survives | the additive decomposition, and the order-independence of the **total** once the variable set is fixed | |
| What does not | the shape of the per-step sequence, and any claim about a particular question's position in it; and the identification of an answer's content with $H$ when no joint law over answers exists — free-text answers have none, so the sum is a model of the accumulation, not a measurement of it | |

## Limits

- Exact for random variables with a joint distribution.
- "The total is order-independent" needs **all** questions eventually asked.
  Under any stopping rule only the per-step gains matter, and those are
  order-dependent — the note's own second half.
- **The per-step decline is not implied by the chain rule.** It needs an
  adaptive-submodularity assumption on the objective, and conditional mutual
  information can rise with conditioning (synergy). Only the average over the
  run is forced.
- Treats the questions as fixed variables. In practice later questions are
  chosen in response to earlier answers; the chain rule still holds, but the
  variables are no longer the same set across runs.
- Sourcing: `shannon-1948` and `cover-2006` are `verified: prior`; no
  unverified `[?]` source is load-bearing here. The formal decomposition of
  synergy (Williams & Beer 2010) is *not* cited as a source of this note — the
  counterexample above rests on Cover & Thomas alone.

## Related

[[entropy]] · [[mutual-information]] · [[conditional-entropy]] · [[adaptive-submodularity]] · [[value-of-information]]

[^s1]: shannon-1948
[^s2]: cover-2006
