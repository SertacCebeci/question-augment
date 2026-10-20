---
description: "The information carried by a single event. The more unexpected, the more Unit: bits. informative. Three properties are demanded of a single-event information measure: 1."
aliases: ["self-information", "information content", "-log p"]
sources: ["shannon-1948", "csiszar-2008"]
---
# Surprisal (self-information)

> The information carried by a single event. The more unexpected, the more
> information.

## Definition

$$I(x) = -\log_2 p(x)$$[^s1][^s2]

Unit: bits.

- $p(x) = 1$ → $I = 0$. A certain event carries no information.
- $p(x) = 1/2$ → $I = 1$ bit.
- $p(x) \to 0$ → $I \to \infty$. The near-impossible happening is highly
  informative.

## Why this form — and under what assumptions

Three properties are demanded of a single-event information measure:

1. Less likely = more information (monotone decreasing in $p$)
2. Certain event = zero information: $I(1) = 0$
3. **Independent events add**: $I(xy) = I(x) + I(y)$ whenever $p(xy) = p(x)p(y)$

Property 3 is a Cauchy functional equation in disguise, and the uniqueness it
buys is narrower than the usual slogan. **Given a regularity condition —
continuity of $I$ in $p$ (measurability on a set of positive measure already
suffices; Csiszár 2008 surveys the weakest known hypotheses) — the functions
satisfying all three are exactly the family $I(p) = -\log_b p$, $b > 1$.** Two
qualifications are load-bearing:

- The base $b$ is *not* determined. It fixes only the unit — bits for $b = 2$,
  nats for $b = e$. So the three properties pin down a family, not a function.
- Without the regularity condition the equation admits pathological
  non-measurable solutions. "The only function satisfying all three" is false
  as stated.

Shannon (1948, §6 and Appendix 2) proved the corresponding uniqueness for the
**average** rather than the single event: continuity in the $p_i$, monotone
increase in $n$ for the uniform distribution, and a composition law force
$H = -K\sum_i p_i \log p_i$. That theorem is about $H$ ([[entropy]]), not
about $I$; the single-event statement above is the functional-equation result,
not Shannon's Theorem 2.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | self-information | exact — the same quantity $-\log p(x)$ |
| Information theory | information content (of an outcome) | exact — same quantity, textbook label |
| Information theory / ML practice | "$-\log p$" | exact — the notational label, not a separate object |

Not this concept: [[entropy]] is $\mathbb{E}[I]$ over a distribution, a
different number with a different uniqueness theorem, and is a separate note.

## Why it matters

**This wiki's reading, not Shannon's result:** if an answer is treated as an
event drawn from the asker's predictive distribution, then $I$ is the natural
scale for what one answer moved — an answer the asker already predicted scores
near zero bits. Two working rules follow, and they are inferences of this wiki,
not theorems: a question whose answer the model already predicts is nearly
worthless, and *prefer the question that could prove you wrong.*

The literature's value claim is the *expected* version, not this realised one:
[[expected-information-gain]] (Lindley 1956) scores a question by
$\mathbb{E}[I]$ over its possible answers before asking, and
[[value-of-information]] scores it by the decision it changes. Realised
surprisal is neither — a single high-$I$ answer can be a lie, and can change no
decision.

## Transfer

| | |
|---|---|
| **Home field** | information theory: an event $x$ in a defined, exhaustive outcome set with a known probability measure $p$ |
| **Here** | one natural-language answer, scored under the asker's or model's predictive distribution over replies — an outcome set that is unbounded free text and a $p$ that is an estimate |
| **What survives** | the monotone unexpectedness-to-bits scale (rank answers by $-\log p$) and additivity over answers that are genuinely independent |
| **What does not** | (i) a defined outcome set — an unmodelled axis has none, so its answers get no $p$ at all ([[unknown-unknowns]]); (ii) calibrated $p$ — the model's own estimate may be wrong ([[calibration]]); (iii) the identification of bits with usable value — a reply naming an entity absent from the asker's model is maximally surprising and still unusable ([[conclusive-answer]], and the contrast recorded in map-answer) |

## Limits

- The uniqueness claim in *Why this form* holds only under the regularity
  condition named there, and only up to the base of the logarithm.
- Requires $p(x)$. A model's probability for an answer is its own estimate, so
  surprisal measures surprise **to the model** — which may be miscalibrated
  ([[calibration]]).
- High surprisal from a *wrong* answer is not information about the world.
- Additivity needs independence; correlated answers double-count.
- Source status: `csiszar-2008` is newly cited here and has not yet been
  confirmed by this wiki's verifier — treat it as `[?]` until it is.

## Related

[[entropy]] · [[kl-divergence]] · [[expected-information-gain]] · [[value-of-information]] · [[calibration]] · [[conclusive-answer]]

[^s1]: shannon-1948
[^s2]: csiszar-2008
