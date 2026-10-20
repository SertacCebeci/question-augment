---
description: "[[cusum]] needs a [[likelihood-ratio|likelihood ratio]] per observation and free-text answers"
aliases: ["e-detector", "e-process change detector"]
sources: ["shin-2024"]
---
# E-detector

> [[cusum]] needs a [[likelihood-ratio|likelihood ratio]] per observation and free-text answers
> supply none. An e-detector needs only a nonnegative statistic whose
> expectation stays at or below 1 under **every** law the pre-change state
> allows — a condition a hand-built score over answers can be made to meet,
> provided the declared class stays true of the stream the asker is driving.

## Definition / Mechanism

Shin, Ramdas & Rinaldo (2024) build sequential change detection for the case[^s1]
where the pre- and post-change distributions are **nonparametrically
specified, and therefore composite**.

- An **e-value** is a nonnegative statistic with expectation at most 1 under
  every distribution in the null. An **e-process** is its sequential form: a
  nonnegative process dominated by a nonnegative supermartingale for each law
  in the composite null. Ville's inequality then bounds the chance it ever
  exceeds a level, which is what makes an anytime threshold legal.
- An **e-detector** is a sum of e-processes **started at consecutive times** —
  one per candidate change point — with an alarm when it crosses a threshold
  fixed by the target false-alarm rate. That is the CUSUM shell (accumulate,
  restart, threshold) with the log-likelihood increment removed.
- When the two densities *are* known, the e-process is the likelihood ratio and
  the construction **recovers the classical likelihood-based procedures**
  (CUSUM, Shiryaev–Roberts).

The guarantees split, and the split is the whole point for an importer:

| Guarantee | Holds |
|---|---|
| average [[run-length|run length]] (false-alarm frequency) | nonasymptotically, for the composite nonparametric null |
| detection delay, near-optimal | only in specific nonparametric classes named by the paper (sub-Gaussian, sub-exponential) |

## Known as

| Name | Field | Relation |
|---|---|---|
| e-process change detector | sequential analysis | exact — this note |
| e-value, e-process | game-theoretic statistics | **not** this concept — the per-observation evidence statistic the detector is assembled from; measured as a single number with a mean bound, not as an alarm with a run length |
| test martingale, safe anytime-valid inference | game-theoretic statistics | close — the programme that supplies e-processes; it tests a fixed null rather than detecting a change point |
| [[conformal-test-martingale]] | machine learning | close — a different construction whose null is exchangeability rather than a declared bound |

## Why it matters

[[cusum]]'s transfer contract records $\Lambda$ as *undefined* here, which
leaves the whole import unearned. This note names the **weakest condition that
buys it back**: choose any per-answer score, then declare a class of laws that
the answer stream is assumed to obey while nothing has changed, such that the
score's e-value form has mean at most 1 under all of them. Nothing about
language, densities or i.i.d.-ness is needed for the false-alarm side.

Three consequences for a questioning procedure:

1. **The false-alarm rate is purchasable without a model of answers** — but the
   price is a true declaration, not a cheap one. The number of answers you will
   burn on spurious "the model has shifted" alarms is controllable by
   declaration alone, *for as long as the declared class remains true of the
   stream*.
2. **The speed is not.** The delay results need tail control on the score. A
   free-text score with unknown tails inherits the alarm-rate guarantee and no
   promise about *when* it fires — so a slow detector is the default outcome,
   not an implementation defect.
3. **The class has to survive the next question.** In a questioning session the
   asker chooses each question after seeing the previous answers, so the class
   is a class over the stream *as the asker drives it*. Only a score whose
   pre-change behaviour does not move when the asker moves — which pushes
   towards question-independent scores (answer-stream-null) — can be
   declared once and left standing.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | a draw whose law lies in a declared nonparametric class | one answer, plus a scalar score computed from it |
| The increment | an e-process for that class | an e-process for a declared class of "nothing has changed" answer behaviour — the practitioner must write that class down |
| What survives | the accumulate-restart-threshold shell; the nonasymptotic false-alarm bound with no parametric assumption; the fact that CUSUM is the special case where a likelihood exists |
| What does not | the near-optimal delay bounds (they need sub-Gaussian/sub-exponential control on the score, which no free-text scorer comes with); any localisation — the alarm still names no answer; and any warrant for the declared class itself, which the asker's own choice of questions can falsify |

## Limits

- **The guarantee is only as strong as the declared pre-change class is
  tight.** Widening the class until it is safely true (e.g. "the score's mean
  is at most anything") keeps validity and destroys power; this note's claim
  that the condition is *meetable* for answers rests on the practitioner
  naming a class narrow enough to be informative, which is an assumption, not
  a result.
- **A false class voids the bound; it does not weaken it.** The tight/loose
  tradeoff above is the benign case. When the declared class does not contain
  the law actually generating the stream, the e-value condition fails and the
  nonasymptotic average-run-length bound holds not at all — the detector then
  alarms at an unknown rate. In a questioning session this is the live risk,
  because the class must hold under **every continuation of the question
  sequence the asker may choose**: a question-dependent score ([[surprisal]],
  distance to the previous answer, a judge's rating) can be pushed outside its
  declared class by a change of topic alone, before any incoherence exists. The
  headline claim of this note therefore assumes a score whose declared class is
  stable across the questions that may be asked next.
- **That adaptivity reading is this note's own inference, not the paper's.**
  Shin, Ramdas & Rinaldo state the framework for pre- and post-change laws that
  are nonparametrically specified and composite; they say nothing about data
  collected under an adaptively chosen input, and no source read this pass
  licenses a conditional-on-the-question form of the class. Whether stating the
  class conditionally on the question asked repairs the problem is open here —
  see answer-stream-null for what this wiki does with it.
- **The mapping to answers is this note's own.** Shin, Ramdas & Rinaldo
  discuss no questioner and no text; nothing in the paper licenses the choice
  of score.
- **No theorem numbers are cited here.** The published article's full text was
  not read this pass; the claims above are those stated in the paper's own
  abstract and framework description. The detection-delay classes are named
  there, and their precise constants are not carried into this note.
- **Detects that, not which.** Like [[cusum]], the alarm has no sentence
  attached; [[truth-maintenance-system]] is what would supply one.

## Related

[[cusum]] · [[sprt]] · [[likelihood-ratio]] · [[conformal-test-martingale]] · [[truth-maintenance-system]]

[^s1]: shin-2024
