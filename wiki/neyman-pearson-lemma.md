---
description: "At fixed false-alarm rate, the most powerful test is the likelihood ratio Neyman & Pearson (1933) proved it."
aliases: ["NP lemma", "fundamental lemma of Neyman and Pearson"]
sources: ["neyman-1933"]
---
# Neyman–Pearson lemma

> At fixed false-alarm rate, the most powerful test is the likelihood ratio
> test.

## Theorem

Neyman & Pearson (1933) proved it. For **two simple hypotheses** $H_0: X \sim p_0$[^s1]
and $H_1: X \sim p_1$ — both fully specified, no free parameters — and a
**fixed level** $\alpha$, among all tests of size $\leq \alpha$ the
likelihood-ratio test

$$\Lambda(x) = \frac{p_1(x)}{p_0(x)} \gtrless \tau$$

maximises power $1-\beta$. The threshold $\tau$ is set by $\alpha$, and the
test **randomises on the boundary** $\Lambda(x) = \tau$ to attain exact size
$\alpha$ when the distribution of $\Lambda$ has an atom there.

Do not look at the raw data; look at the **likelihood ratio**.

## Known as

| Field | Name there | Relation |
|---|---|---|
| statistics | NP lemma | exact |
| statistics | fundamental lemma of Neyman and Pearson | exact |
| statistics | likelihood ratio test | close — the *test procedure*, not the theorem; it exists (as the generalised LRT) in composite settings where this lemma says nothing about optimality. See [[likelihood-ratio]], [[hypothesis-testing]] |
| statistics | most powerful test | close — a *property a test can have* at a given $\alpha$; the lemma is the claim that one particular test has it |

## Why it matters

It gives the **shape** of the optimal decision rule: whatever the data, what
you do is compare the probabilities under the two hypotheses. The rest of the
data is irrelevant — which leads to [[sufficient-statistic]].

## Why it matters when asking

*The mapping below is this wiki's inference from the lemma, not part of it.*

When judging which design direction an answer supports, the useful question is
plausibly not "is this answer consistent with X":

```text
Weaker:  "Is this answer compatible with design A?"
Better:  "Is this answer more likely under A or under B?"
```

An answer can be compatible with A yet *more* compatible with B — in which
case it is evidence for B. The heuristic *prefer the question that could prove
you wrong* is a loose echo, not a corollary: a non-discriminating question
would leave $\Lambda \approx 1$ and teach nothing. What licenses the analogy
and what it drops is the Transfer table; nothing here is proved.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | i.i.d. draw from a known $p_0$ or $p_1$ | one natural-language answer |
| $\Lambda(x)$ | computable ratio of two known densities | undefined — needs a surrogate (a judge, a scored rubric) |
| What survives | judge an answer by its relative likelihood under two rival designs, not by compatibility with one; a question whose $\Lambda$ stays near 1 buys nothing | |
| What does not | the optimality proof, exact level-$\alpha$ control, and the existence of the threshold $\tau$ | |

## Limits

- The lemma holds only for **two simple hypotheses** at a fixed $\alpha$, with
  randomisation at the boundary. Design spaces are composite and
  multi-hypothesis, so the optimality claim does not reach them — for
  composite alternatives one has the generalised LRT, which the lemma does not
  cover.
- The transfer above rests on the assumption that a surrogate for $\Lambda$
  exists and is monotone in the evidence a rival design gets. With a judge or
  a rubric standing in for the ratio, no [[calibration]] is claimed, so "more
  likely under A" is an ordering, not a level.
- Attribution rests on `neyman-1933` [?] — verified prior to the verifier, not
  re-confirmed.

## Related

[[hypothesis-testing]] · [[likelihood-ratio]] · [[sufficient-statistic]] · [[sprt]]

[^s1]: neyman-1933
