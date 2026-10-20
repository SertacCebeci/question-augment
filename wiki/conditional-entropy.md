---
description: "The uncertainty about $X$ that remains once $Y$ is known. Shannon (1948, §6) defines this quantity — \"the average of the entropy of $y$ for each value of $x$,"
aliases: ["equivocation", "remaining uncertainty", "H(X|Y)"]
sources: ["shannon-1948", "cover-2006"]
---
# Conditional entropy

> The uncertainty about $X$ that remains once $Y$ is known.

## Definition

$$H(X\mid Y) = -\sum_{x,y} p(x,y)\log_2 p(x\mid y)$$[^s1][^s2]

Shannon (1948, §6) defines this quantity — "the average of the [[entropy]] of $y$
for each value of $x$, weighted according to the probability of getting that
particular $x$" — and in the same section places it in the decomposition
$H(X,Y) = H(X) + H(X\mid Y)$ that [[chain-rule]] generalises to $n$ variables.

## Conditioning reduces entropy

$$H(X \mid Y) \leq H(X)$$

Equality iff $X \perp Y$. **Acquiring information never increases
uncertainty.** Shannon (1948, §6) states the inequality in this form — the
uncertainty of $y$ "is never increased by knowledge of $x$. It will be
decreased unless $x$ and $y$ are independent events, in which case it is not
changed" — and Cover & Thomas (2006) give it as *Conditioning reduces
entropy* (Theorem 2.6.5, "information can't hurt"), with the same equality
condition.

The subtlety: this holds **on average**, over the distribution of $Y$. A
single answer $Y=y$ can raise $H(X\mid Y=y)$ above $H(X)$ — a surprising
answer shakes the model and more worlds become visible at that moment. The
theorem constrains only the $p(y)$-weighted average of those per-answer
values.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Information theory (channel coding) | equivocation | close — Shannon (1948, §12) names $H_Y(X)$, the conditional entropy of the transmitted message given the received signal, the equivocation; that is this quantity at one particular pair of variables, not the general object |
| Information theory | $H(X\mid Y)$ | exact — the standard notation, not a second concept |
| Informal usage | remaining uncertainty | close — the same direction, without the joint distribution that makes the number defined |

## Why it matters

This is the theorem behind the claim that a question narrows the possible
solution space: on stall 5, an answer that is not independent of $X$ lowers
expected uncertainty, and one that is independent of $X$ lowers it by exactly
zero — which is the test for whether what came back was a constraint at all.

What the theorem gives about a sequence is only that expected uncertainty is
**non-increasing at every step**. It says nothing about whether the greedy
one-question-at-a-time sequence is *good*: per-step non-increase is
compatible with an arbitrarily bad ordering. Near-optimality of the greedy
sequence is a separate claim with separate conditions — see
[[adaptive-submodularity]] — and [[chain-rule]] puts the emphasis the other
way: under any stopping rule only the order-dependent per-step gains matter.

**This wiki's inference, not in shannon-1948 or cover-2006.** A *growing*
list of open questions during asking is consistent with $H$ falling: a longer
list is not rising entropy, it is a widening measured area. $H$ can fall
while the number of variables one is tracking rises. This reading is an
interpretation, and it holds only when the added variables were always part
of $X$ and merely unattended — if they extend $X$ itself, the two $H$ values
are not on the same axis and are not comparable.

## Transfer

| | In its home field | Here |
|---|---|---|
| The unknown $X$ | a random variable with a defined alphabet | whatever the asker has not pinned down, with no enumerated outcome set |
| The observation $Y$ | a draw from a known joint $p(x,y)$ over a defined alphabet | one natural-language answer; $p(x,y)$ is a model's estimate, and the alphabet is open |
| What survives | the direction and its quantifier: expected uncertainty never rises, and rises by zero exactly when the answer is independent of the unknown; and the per-answer exception, which stays a real possibility | |
| What does not | any numeric value of $H(X\mid Y)$; the guarantee at all on an axis with no defined outcome set (second bullet under Limits); and any claim about the quality of the asking *sequence*, which this theorem does not address | |

## Limits

- The reduction holds **in expectation**. A single answer can raise
  uncertainty; the theorem does not forbid it.
- Requires a joint distribution over $X$ and $Y$ — for an unmodelled axis
  there is no $Y$ to condition on, and the inequality has no referent rather
  than being true-but-loose.
- The theorem is per-step. Any statement here about how good a *sequence* of
  questions is rests on [[adaptive-submodularity]]'s assumptions, not on this
  one.
- The distinction between "more visible variables" and "more entropy" is this
  wiki's interpretation (marked above), not a theorem, and assumes a fixed
  $X$.

## Related

[[entropy]] · [[mutual-information]] · [[chain-rule]] · [[adaptive-submodularity]] · [[surprisal]]

[^s1]: shannon-1948
[^s2]: cover-2006
