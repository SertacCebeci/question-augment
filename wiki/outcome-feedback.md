---
description: "Telling an answerer how it scored is the weakest feedback there is: a **Outcome feedback** returns only the result of the judgment — the true value, the hit/miss,"
aliases: ["outcome feedback", "OFB", "knowledge of results", "results-only feedback"]
sources: ["balzer-1989", "greenberg-2018", "lichtenstein-1980", "martin-2025"]
---
# Outcome feedback

> Telling an answerer how it scored is the weakest feedback there is: a
> scalable, unfacilitated loop built on a proper-family score left [[calibration]]
> unchanged in two experiments with 1,481 people.

## Definition / Mechanism

**Outcome feedback** returns only the result of the judgment — the true value,[^s1][^s2][^s3][^s4]
the hit/miss, or a score computed from both — and nothing about the task that
produced it. It is the loop any answering system can build for free: emit a
probability, wait for the outcome, return the number.

**The null.** Martin & Mandel (2025), *Futures & Foresight Science* 7(1) e199,
tested exactly that loop at scale. Two experiments ($N_1 = 610$, $N_2 = 871$)
compared a control group, an outcome-feedback group, and a group trained with
performance feedback scored by the **Practical scoring rule** — Greenberg's (2018) modification of the logarithmic rule, built to remove the log rule's
unintuitive features so that a trainee can learn from the number. Neither
training regime improved calibration. Calibration overall was predicted by
Actively Open-Minded Thinking, but change in calibration across blocks was
not. The paper's motive is the point: facilitated calibration workshops work
but do not scale, so the question was whether a score alone can carry the
training. The answer here is no.

**Why the score does not teach.** Balzer, Doherty & O'Connor (1989),
*Psychological Bulletin* 106, 410–433, reviewed *cognitive* feedback against
outcome feedback and split it into three components: information about the
task system, information about the judge's own cognitive system, and
information about the relation between them. In multiple-cue probability
learning it was the **task-system component** that appeared responsible for
the performance gains. Outcome feedback carries none of it: the outcome is a
sample from the task, not a description of it.

**Where outcome feedback did work.** Lichtenstein & Fischhoff (1980) got
substantial learning from own-score feedback — over 11 sessions of 200 items
each, with the learning arriving at the first feedback. The regime that
produces an effect is intensive and repeated on one item family; the regime
that does not is short, scalable and general.

## Known as

| Field | Name there | Match |
|---|---|---|
| JDM / lens-model research | outcome feedback (OFB) | exact |
| Forecasting training studies | results-only feedback | exact |
| Motor learning, education | knowledge of results | close — same information type, measured on skill acquisition rather than on probability judgment |

**Not this concept.** *Performance feedback* (also called *score feedback*) is
a separate object, not another name for this one: it is a distinct
experimental arm in Martin & Mandel, run alongside the outcome-feedback arm
and scored by the Practical rule, and it is separately measured in Stone &
Opel as reported by *[[calibration-training]]*, where returning own scores
reduced overconfidence — an effect, where outcome feedback shows none. This
note's null covers the performance-feedback arm only as Martin & Mandel report
it, and nothing said here transfers to score feedback in general. *Cognitive
feedback* (also *lens-model feedback*) is the contrast class in Balzer et al.:
it returns task structure and policy parameters and is measured to produce
different — larger — effects. *[[calibration-training]]* is the whole
intervention family, of which outcome feedback is one member.

## Why it matters

Stall 10 asks how far an answerer should commit, and the standing assumption
is that a scored loop will fix the commitment level. Martin & Mandel remove
that assumption for the cheap version of the loop:

1. **Propriety is not pedagogy.** The Practical rule is built for
   learnability and still taught nothing. A score that makes honest reporting
   optimal at report time says nothing about whether returning it changes the
   next report.
2. **What must be returned is the task, not the verdict.** Balzer et al.
   locate the effect in task information. A loop that can only say "wrong"
   is, on this evidence, the component with no demonstrated effect.
3. **The working regimes are the expensive ones.** Lichtenstein & Fischhoff's
   2,200 scored items and the facilitated workshops Martin & Mandel were
   trying to replace both cost far more than a scoring rule bolted onto an
   answering pipeline. Whichever of length, facilitation or task information
   is doing the work, it is not the score.

## Transfer

| | |
|---|---|
| **Home field** | humans in multiple-cue probability learning and calibration studies, receiving outcomes or scores on repeated resolvable items |
| **Here** | an answering system whose only available self-signal is a score on its past answers — the loop a designer reaches for first when commitment is miscalibrated |
| **What survives** | the taxonomy (outcome vs task-system information) and the ranking it implies; the demonstration that a rule designed for learnability does not by itself change calibration in a short, unfacilitated regime |
| **What does not** | the null's scope — it is measured on human participants over two blocks; nothing here tests a model, and the human null does not establish that gradient-level score feedback fails. Balzer's task-information result comes from multiple-cue learning tasks, not from confidence calibration, so its use as the explanation of the null is this note's inference and not a measured finding |

## Limits

- The load-bearing claim is a **null**. Martin & Mandel report no improvement
  from either regime; with $N = 1{,}481$ across two experiments that is
  informative, but this note has not read their power analysis or effect-size
  bounds, so "no effect" should be read as "no effect detected at their
  session length and item type".
- The Martin & Mandel design (N, arms, outcome) is taken from the publisher's
  listing and the paper's abstract, not the full text [?]; the AOMT result and
  the absence of a block-wise change effect are reported at that level of
  detail only.
- The Lichtenstein & Fischhoff (1980) full text was not obtained [?]: the
  11 sessions × 200 items figure and "learning arrives at the first feedback"
  are taken from secondary listings and the authors' later review, so the
  contrast between the intensive regime and the scalable one rests on an
  unverified description of the intensive one.
- The explanation offered in *Why it matters* — that task information is what
  outcome feedback lacks — joins two literatures that were never run against
  each other. Balzer et al. (1989) is a narrative review of multiple-cue
  probability learning, not of calibration of confidence.
- Lichtenstein & Fischhoff (1980) and Martin & Mandel (2025) differ on more
  than one dimension at once (session length, item family, facilitation,
  incentive), so this note cannot say which difference produces the
  disagreement.
- No source here involves a machine answerer.

## Related

[[calibration-training]] · [[calibration]] · [[verbal-probability-expressions]] · [[constraint-as-information]] · [[sycophantic-capitulation]]

[^s1]: balzer-1989
[^s2]: greenberg-2018
[^s3]: lichtenstein-1980
[^s4]: martin-2025
