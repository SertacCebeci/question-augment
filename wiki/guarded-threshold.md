---
description: "**This wiki's inference, not a result.** Of the stopping and commitment Three steps, of which only the second is someone else's. 1."
aliases: ["guarded threshold"]
sources: ["jcgm-2012-conformity"]
---
# Guarded threshold

> **This wiki's inference, not a result.** Of the stopping and commitment
> rules examined below, only [[sprt]]'s boundaries are derived from the error
> probabilities they control; the others compare an *estimated* quantity with
> a cut and offset it by nothing — so each is least reliable exactly where it
> fires. Metrology's repair is available and structural: move the cut, do not
> sharpen the estimate.

## The claim

Three steps, of which only the second is someone else's.[^s1]

1. **The thresholds inspected here are applied to estimates.** Five rules were
   read for this note. **No exhaustive count of the wiki's rules was made**,
   so what follows is a survey, not a census.

| Rule | What it compares with a cut | Offset for that statistic's own uncertainty |
|---|---|---|
| [[sprt]] (stall 7) | accumulated log-[[likelihood-ratio|likelihood ratio]], against two boundaries | **yes, implicitly** — the boundaries are derived from the two declared error probabilities |
| [[value-of-information]] (stall 7) | expected gain net of cost, against zero | none |
| [[qualitative-saturation]] (stall 7) | new themes per run, against $T \le 5\%$ or $0\%$ | none — $B$, $R$, $T$ are declared and the cut is fixed by fiat |
| [[abstention]] (stall 10) | a separately learned uncertainty score, against a cut set by a named price, risk or coverage | none on the score itself; Geifman & El-Yaniv's SGR bounds the *risk estimated on the [[calibration]] sample*, not the error of the score at its own cut |
| [[discordant-recommendation]] (stall 10) | nothing — certainty and strength are graded separately, and a consequence asymmetry may override certainty outright | not applicable: no cut to offset |

   Stopping records the second half of this already — "every field
   takes the threshold as given" — but not the first. ([[semantic-entropy]] is
   deliberately *not* in the table: it is a statistic the wiki holds with no
   threshold fixed for it, reported by AUROC rather than by a cut, so the
   conjecture would bear on it only once someone sets one.)

2. **A binary rule on an uncertain estimate is worst at its own cut.** JCGM 106:2012 (8.3.1.2) states for conformity assessment that with a symmetric
   unimodal PDF for the measurand and an acceptance limit equal to the
   tolerance limit, the probability of a wrong decision can be as large as
   50 % when the measured value lies very close to the limit.
3. **Therefore (this wiki):** a threshold rule of the kind tabulated above is
   invoked precisely in the region where its error rate is maximal — a rule
   *fires* when the estimate is near the cut — and the lever metrology reaches
   for is not precision but an offset: displace the cut by a declared multiple
   of the estimate's own uncertainty, in the direction of the costlier error
   ([[guard-band]]), which presupposes that this uncertainty has been composed
   and stated ([[uncertainty-budget]]).

What it would change in a derived procedure: such a rule stops being a number
and becomes a **pair** — threshold and offset — where the offset is a function
of the asker's uncertainty about its *own stopping statistic*, not about the
subject matter, and where the sign of the offset records whether stopping
early or asking too long is the worse failure. Two askers with the same
threshold and different evidence quality would then stop at different times
without either changing its threshold.

## Known as

Not a term of art. "Guarded threshold" is this wiki's name for the composition
of a metrological guard band with the wiki's own stopping rules; no field
known to this note carries the composition, and the name should not be
searched for in the literature. The metrological half is [[guard-band]]; the
statistical practice of adjusting a decision boundary for estimation error
under a named loss exists in decision theory and is not read here.

## Transfer

| | |
|---|---|
| In its home field | conformity assessment: a measured value against a tolerance limit specified from outside, with a post-measurement PDF for the measurand supplied by a GUM budget |
| Here | a stopping or commitment statistic against its threshold, where the statistic is estimated from the answers received so far |
| What survives | the structural point — the error rate of a thresholded decision peaks at the threshold, and the available lever is the offset rather than the precision; and the discipline that the offset be declared before the decision rather than chosen when the estimate arrives |
| What does not | the risk arithmetic. JCGM 106 computes consumer's and producer's risk from a stated PDF for the measurand; a stopping statistic over answers has no such PDF here, so the offset can be declared but not tuned to a named risk level. Nor does the transfer supply the tolerance limit — in metrology it is given by a specification, in an inquiry nobody hands it over |

## Limits

- **This is a conjecture and is typed as one.** No source states it; JCGM
  106's authors are not writing about inquiry, and none of the stall-7 sources
  considers measurement uncertainty in its own statistic.
- **The survey in step 1 is five rules, chosen because they are the wiki's
  explicit threshold rules; it is not a count.** How many of the wiki's rules
  omit the offset is therefore unknown, and the conjecture's reach is whatever
  that unmade count would show. Two of the five are already outside it —
  [[sprt]] has paid the correction inside the rule, and
  [[discordant-recommendation]] has no cut to move, because it lets the
  consequence asymmetry act on the commitment level directly instead of
  through an offset proportional to uncertainty.
- Step 2 is imported outside its conditions. The 50 % figure holds for a
  symmetric unimodal PDF of a scalar measurand. Several of the quantities in
  the table are not of that shape at all — the novelty rate in
  [[qualitative-saturation]] is a run over a discrete stream — so the argument
  reaches those rules only by analogy, if at all.
- The direction of the offset requires knowing which error costs more. The
  wiki does not have that cost — [[abstention]]'s limit (the price of an empty
  answer is exogenous and nothing in the literature supplies it) applies here
  unchanged, and so the conjecture relocates the missing number rather than
  producing it.
- Nothing here is measured. No experiment in this wiki or its sources compares
  an offset stopping rule with an unoffset one.

## Related

[[guard-band]] · [[uncertainty-budget]] · [[stopping-rules]] · [[abstention]] · [[sprt]] · [[discordant-recommendation]]

[^s1]: jcgm-2012-conformity
