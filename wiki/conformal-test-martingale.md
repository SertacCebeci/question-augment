---
description: "The cheapest surrogate for a [[likelihood-ratio|likelihood ratio]] over answers: **any** function"
aliases: ["conformal martingale", "CTM"]
sources: ["vovk-2021", "vovk-2021-randomness"]
---
# Conformal test martingale

> The cheapest surrogate for a [[likelihood-ratio|likelihood ratio]] over answers: **any** function
> that scores how strange a new answer looks beside the previous ones. The
> price is the null it buys — the answers must be **exchangeable** while
> nothing has changed, and an adaptively questioning agent violates that by
> construction.

## Definition / Mechanism

Two ingredients, neither of them a model of answers (Vovk 2021):[^s1][^s2]

1. A **nonconformity measure** — any real-valued function scoring a new
   example against the bag of earlier ones. It can wrap any prediction
   algorithm; its quality affects power only, never validity.
2. A **betting function** turning the resulting sequence of conformal
   $p$-values into a nonnegative process starting at 1.

Under exchangeability the conformal $p$-values are i.i.d. uniform, so the
betting process is a martingale: a **conformal test martingale**. Vovk et al. (2021) note that these are martingales under *any* exchangeable law for the
data, and that this is what makes their validity automatic. A large value is
evidence against exchangeability by Ville's inequality — the chance of ever
reaching $c$ is at most $1/c$ — and the same object is turned into a change
detector: Vovk's review of online randomness testing (2021) gives **conformal
versions of the CUSUM and Shiryaev–Roberts procedures**, valid when the data
are i.i.d. from a completely unknown distribution.

The application Vovk et al. build it for is operational: **decide when to
retrain** a deployed predictor, i.e. when the stream stopped looking like the
stream the model was fitted on.

## Known as

| Name | Field | Relation |
|---|---|---|
| conformal martingale, CTM | conformal prediction | exact — this note |
| exchangeability martingale | game-theoretic probability | close — the wider class (any martingale under every exchangeable law); Vovk describes conformal martingales as the only known non-trivial members, so the names are not interchangeable |
| nonconformity measure | conformal prediction | **not** this concept — the scoring input, measured as a number per example, not as accumulated evidence |
| conformal prediction | machine learning | **not** this concept — the parent framework, whose output is a prediction set with a coverage guarantee |

## Why it matters

For stall 6 this is the surrogate with the **lowest declaration cost** in the
wiki. [[e-detector]] asks the practitioner to write down a class of pre-change
laws for a chosen score; a conformal test martingale asks for no class and no
threshold model — only a scoring function and a betting rule, and it will
still control the false alarm.

What it charges instead is a **null about the sequence**: the answers must be
exchangeable while nothing has changed. Alarms are therefore evidence against
*exchangeability*, not against coherence, and every mechanism that reorders
or re-targets the stream is a source of them.

## Transfer

| | In its home field | Here |
|---|---|---|
| The stream | i.i.d. labelled examples arriving at a deployed model | answers arriving in a questioning session |
| The increment | a betting function on a conformal $p$-value from a nonconformity score | the same, with the nonconformity score computed over answers (an entailment or embedding score, say) |
| What survives | validity without any model: a scoring function suffices, the guarantee is by Ville's inequality, and the CUSUM/Shiryaev–Roberts shells have conformal analogues |
| What does not | the null itself. Answers in a session respond to **different, adaptively chosen** questions, so they are not exchangeable before any contradiction occurs — the detector then fires on the asker's own change of policy. Efficiency also does not transfer: Vovk et al. state validity as guaranteed and describe their efficiency work as first steps |

## Limits

- **Exchangeability is the assumption this note's usefulness rests on, and
  a questioning agent breaks it deliberately.** The remedy — scoring with a
  question-independent functional — is not in the cited work; it is the
  conjecture in answer-stream-null.
- **The alarm is against a compound null.** Any departure from exchangeability
  triggers it: topic drift, a change of answerer, a reordering. Nothing
  separates "the answers now contradict what was said" from "the questions
  moved on".
- **No localisation and no culprit.** As with [[cusum]], the process names no
  answer; [[truth-maintenance-system]] would be needed for that.
- **Power depends entirely on the nonconformity measure**, which the theory
  leaves free; a badly chosen score is valid and blind.
- **The PMLR/COPA text and the Statistical Science review were read through
  their abstracts and metadata this pass**, not in full; no theorem number is
  cited here.

## Related

[[e-detector]] · [[cusum]] · [[semantic-entropy]] · [[scan-b-statistic]] · [[metamorphic-probes]]

[^s1]: vovk-2021
[^s2]: vovk-2021-randomness
