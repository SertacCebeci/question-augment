---
description: "Deciding and being told are the same operation: both remove worlds. A constraint narrows the set of live possibilities. Where it came from does not change what it does."
aliases: ["commitment as information", "decision as constraint"]
sources: ["alchourron-1985", "cover-2006", "lindley-1956", "shannon-1948", "zhou-2024"]
---
# Constraint = information

> Deciding and being told are the same operation: both remove worlds.

## The claim

A constraint narrows the set of live possibilities. Where it came from does not[^s1][^s2][^s3][^s4][^s5]
change what it does.

```text
"The character dies on page 100" — decided by the author
"The character dies on page 100" — read in the manuscript
```

After either, the character cannot speak on page 101. The commitment and the
observation impose the identical restriction.

## The counterpart in theory

Both narrow the support in the same way:

$$\mathcal{W}' = \{w \in \mathcal{W} : w \models \text{constraint}\}$$

Shannon's $H$ (Shannon 1948) is a function of the probabilities alone: it has
no argument for provenance. Two constraints that delete the same worlds leave
the same [[entropy]] whoever imposed them. The source-blindness of the
restriction is the whole content of this note — it is a property of the
definition of $H$, not an extra assumption.

## Observation and commitment are not symmetric — but the DPI is not what says so

**What the theorem says.** For a Markov chain $X \to Y \to Z$,
$I(X;Z) \le I(X;Y)$ (Cover & Thomas 2006, ch. 2). Processing $Y$ cannot
increase what is known about $X$.

**What this wiki adds.** An observation fits the chain: a state of the world
$X$, a channel, a report. A commitment has no $X$ — nothing outside the
decider determined which world would be picked — so this wiki *places* it
outside the chain and treats the DPI as not binding on it. That placement is a
modelling choice, not a result: the inequality is simply silent about a
variable that was never defined. [[data-processing-inequality]] records the
same caveat in its own Limits.

What the placement buys is a difference in **how each can fail**:

- a wrong observation locks the system onto the wrong world and will collide
  with reality;
- a commitment cannot be wrong — there was no right answer — it can only be
  **inconsistent** with a constraint already recorded.

The practical form of the distinction is **when the conflict shows up**. A
constraint that already exists in the world (an API signature, a physical
limit) punishes a wrong guess from outside, at an unpredictable moment. A
constraint you invent punishes you only when you contradict yourself later.

## The value of an answer

If an answer is a constraint, its value is the entropy it removes:

$$\text{value of an answer} = H(\theta) - H(\theta \mid \text{answer})$$

Lindley (1956) established this quantity as the measure of the information
provided by an experiment — but **in expectation over answers not yet
received**, which is [[expected-information-gain]]. The realised single-answer
form written above is not the same object and is not guaranteed non-negative:
one particular answer can raise $H(\theta)$; only the average over answers
equals $I(\theta; \text{answer}) \ge 0$ (Cover & Thomas 2006).

Three ways an answer can be bad:

```text
H unchanged      →  "it depends"               (imposes no constraint)
|W| = 0          →  conflicts with an existing constraint
wrong axis       →  narrowed a different variable
```

The first is the most insidious: an answer **appears** but entropy is flat. How
often models produce that shape is not measured here; the nearest measurement
runs the other way — Zhou et al. (2024) find RLHF-tuned models emit more
strengtheners than weakeners while base and SFT models do the reverse — and
hedging is an adjacent construct, not "it depends".

## Relation to MaxEnt

On an unasked axis there is no constraint → [[maximum-entropy-principle]]
applies → the axis must stay open. A model silently picking a value without
recording it (*silent fork*) is both a MaxEnt violation and an unrecorded
constraint: the most dangerous combination.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | conditioning on an event / restricting the support | close — the same set operation, but defined only over a measurable space |
| Belief revision (AGM) | expansion $K + p$ (Alchourrón, Gärdenfors & Makinson 1985) | close — restricts the models of $K$ identically and is likewise source-blind, but is defined on a deductively closed belief set and assumes $p$ is consistent with $K$ |
| Planning / decision practice | commitment | close — names only the self-imposed half of this note's object |

The frontmatter aliases *commitment as information* and *decision as
constraint* are this wiki's own restatements, each naming one direction of the
identity; neither is a term of art in a field.

## Transfer

| | |
|---|---|
| **In its home field** | Information theory: a distribution over a specified measurable space, a defined source variable $X$, a known likelihood; $H(\theta)$ and $I(X;Y)$ have computed values, and the DPI needs the chain $X \to Y \to Z$ to be specified. |
| **Here** | A set $\mathcal{W}$ of worlds described in natural language, an informally modelled $\theta$, a free-text answer or an author's commitment. No prior is written, no likelihood is estimated, and no numeric entropy is computed. |
| **What survives** | The set operation $\mathcal{W}' = \{w : w \models c\}$ and its source-independence — worlds removed is a well-defined count however the constraint arose — plus the ordinal reading of the value of an answer: an answer that removes no world is worth nothing. |
| **What does not** | The numbers. $H(\theta)$ is undefined without a modelled [[possible-worlds|hypothesis space]], so $H(\theta) - H(\theta\mid\text{answer})$ is a shape, not a measurement. A commitment supplies no source variable $X$, so the DPI does not apply to it — and therefore proves nothing about it either. MaxEnt needs a measure on the axis, which a free-text axis does not supply. |

## Limits

- Placing a commitment outside the Markov chain, because its $X$ is undefined,
  is **this wiki's modelling choice, not a theorem**. Everything in the
  asymmetry section rests on it. A reading that assigns $X$ (e.g. the decider's
  own prior dispositions) would bring commitment back under the DPI and dissolve
  the asymmetry.
- The identity holds for the *effect on the support*. It says nothing about the
  two risk profiles, which are what the asymmetry section is about.
- The good-answer measure needs $H(\theta)$ defined, i.e. a modelled hypothesis
  space; and in its single-answer form it can be negative, unlike Lindley's
  expectation.
- The three bad-answer types are this wiki's classification, not a result of
  anyone's.
- The frequency with which any answerer, human or model, produces the
  "$H$ unchanged" shape is **uncited here**: this wiki has no measurement of it.

## Related

[[possible-worlds]] · [[data-processing-inequality]] · [[maximum-entropy-principle]] · [[expected-information-gain]] · [[agm-belief-revision]] · [[sufficient-statistic]]

[^s1]: alchourron-1985
[^s2]: cover-2006
[^s3]: lindley-1956
[^s4]: shannon-1948
[^s5]: zhou-2024
