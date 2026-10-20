---
description: "Whether an answerer's confidence should be read as typically too high or Juslin & Olsson (1997, *Psychological Review* 104(2),"
aliases: ["Thurstonian–Brunswikian distinction", "origins of uncertainty in judgment"]
sources: ["baranski-1994", "bjorkman-1993", "juslin-1997", "vickers-2001"]
---
# Origins of uncertainty in judgment

> Whether an answerer's confidence should be read as typically too high or
> typically too low is fixed by *where the question's uncertainty comes from*
> — and that is a property of the question, not of the answerer.

## Definition / Mechanism

Juslin & Olsson (1997, *Psychological Review* 104(2), 344–366) "propose a[^s1][^s2][^s3][^s4]
distinction between 2 different origins of uncertainty named after 2 of the
great probabilists in the history of psychology, L. L. Thurstone and Egon
Brunswik." They "review data that suggest that there are empirical as well as
conceptual differences between the 2 modes of uncertainty and thus that
separate models of confidence are needed in tasks dominated by Thurstonian and
Brunswikian uncertainty."

The two values of the variable, in the classical content of the two names:

| Origin | Where the uncertainty sits | Paradigm task |
|---|---|---|
| **Thurstonian** | in the internal representation of a stimulus that is fully present — Thurstone's *discriminal dispersion*: a fixed stimulus produces a fluctuating internal value | sensory discrimination with pair comparisons: which of these two lines is longer |
| **Brunswikian** | in probabilistic cue–criterion relations in an environment that has to be sampled — Brunswik's lens model: the cues are present but their validity is not | two-alternative general-knowledge items; any judgment from imperfect cues to a criterion |

Juslin & Olsson supply a computational model for one class only: the **sensory
sampling model**, "for 1 class of tasks dominated by Thurstonian uncertainty:
sensory discrimination with pair comparisons," which "predicts decisions,
confidence assessments, and the complex pattern of response times in simple
psychophysical discrimination tasks (J. V. Baranski and W. M. Petrusic, 1994)"
and "accounts for the disposition towards underconfidence often observed in
sensory discrimination with pair comparisons."

So the taxonomy is load-bearing in one specific way: it makes the *sign* of
the expected miscalibration an index on the task class — underconfidence in
the Thurstonian class ([[sensory-underconfidence]]), the difficulty-dependent
crossover in the Brunswikian class ([[hard-easy-effect]]) — rather than a
property of the judge.

**Contested.** Vickers & Pietsch (2001, *Psychological Review* 108(4),
789–804) examine the distinction and dissect the sampling model, concluding
that "the window-sampling model is a maladapted combination of inappropriate
elements, which is implausible as a model of decision making, memory, or
confidence, in sensory discrimination." Their stated conclusion is about the
model; it is not a demonstration that the distinction is empty.

## Known as

| Field | Name there | Match |
|---|---|---|
| JDM / psychophysics | the Thurstonian–Brunswikian distinction | exact |
| Juslin & Olsson's own title | origins of uncertainty in judgment | exact |
| Calibration research generally | sensory versus cognitive tasks / sensory versus cognitive uncertainty | close — that split is by stimulus domain; this one is by where the uncertainty originates, and the whole point of the distinction is that a task can be visual and still Brunswikian. Not carried as an alias of this note: it names a different partition, and [[uncertainty-origin-as-calibration-prior]] argues it puts one task on the wrong side |

Not this concept:

- **Thurstonian uncertainty** and **Brunswikian uncertainty** are the two
  *values* of this variable, and the literature measures them as different
  things — opposite typical signs of miscalibration, and separate confidence
  models by Juslin & Olsson's own conclusion. Neither name is an alias of the
  distinction; a note on either is a note on one cell.
- **[[uncertainty-decomposition]]** (aleatoric / epistemic / specification) is
  the wiki's other origin-of-uncertainty taxonomy and is a different cut: it
  indexes *which action resolves* the uncertainty — accept, search, ask —
  while this one indexes *which confidence model and which miscalibration
  sign* applies to a judgment already made. A question can be epistemic in
  that taxonomy and Thurstonian or Brunswikian in this one; they are run for
  different decisions, not alternatives to each other.

## Why it matters

Stall 10 asks how far an answerer should commit.

1. **It turns "how confident should this answer be?" into a question about the
   question.** Before any measured calibration regularity may be applied to an
   answer, the class of the question has to be settled, because the two
   classes carry opposite corrections.
2. **It is the only principle here for deciding whether a calibration result
   transfers *across question classes*.** [[hard-easy-effect]]'s corpus is
   general-knowledge items only; the transfer condition this framework names is
   sameness of *origin*, not sameness of modality. Transfer across *response
   formats* is a separate condition this framework says nothing about and does
   not license: [[hard-easy-effect]] holds it, and reports that on a .5–1.0
   scale the scale-end effects are confounded with over/underconfidence, so
   matching the origin does not carry a result across formats.
3. **It says a single confidence model is not available.** Juslin & Olsson's
   conclusion is that separate models are *needed*, so an answering system with
   one uncertainty head fitted on one class is making an assumption the
   framework denies, not a simplification it licenses ([[calibration]],
   [[abstention]]).

## Transfer

| | |
|---|---|
| **Home field** | models of confidence in psychophysical pair comparison and in probabilistic-cue judgment, where the class of the task is fixed by the experimenter's design |
| **Here** | an asker deciding which miscalibration prior may be applied to an answerer's stated confidence on a question nobody designed |
| **What survives** | the claim that the confidence model is indexed by the origin of the uncertainty, and that one model covering both classes was not available to its proposers |
| **What does not** | the sensory sampling model itself, which is specific to pair comparison and was argued implausible by Vickers & Pietsch (2001); and any *procedure* for assigning a naturally occurring question to a class — in the sources the class comes from the experimental design, so applying the taxonomy outside the laboratory is an inference and not a transfer ([[uncertainty-origin-as-calibration-prior]]) |

## Limits

- **The full text of Juslin & Olsson (1997) was not obtained** [?]; every claim
  above is from the published abstract, with Vickers & Pietsch (2001) read from
  theirs. In particular the empirical test by which they separate the two modes
  was **not read**, so "empirical as well as conceptual differences" is carried
  here as their reported claim and not as a criterion this wiki can run. The
  note's own claim rests on that gap: it says the class *indexes* the
  correction, and it cannot say how to read the class off a question.
- **The content of the two names in the table is supplied by this note** from
  Thurstone's and Brunswik's own models, not quoted from Juslin & Olsson.
- **"Dominated by" is not quantified.** The sources give no measure of how much
  of a task's uncertainty is of which origin and no treatment of mixed tasks,
  so the taxonomy is two labelled extremes, not a partition with a decision
  rule.
- **The empirical anchor on the Thurstonian side is itself disputed.** The
  underconfidence the model accounts for is the quantity two laboratories
  failed to agree on ([[sensory-underconfidence]]), so "the sign is fixed by
  the class" is at best fixed by the class *and* the setting.
- **Nothing read here bears on response format, elicitation scale, or scoring
  rule**, so the origin condition is necessary at best and never sufficient for
  a calibration result to transfer.
- No source here classifies a machine answerer, and a token-sampling process
  is not evidently of either origin.

## Related

[[sensory-underconfidence]] · [[hard-easy-effect]] · [[uncertainty-origin-as-calibration-prior]] · [[uncertainty-decomposition]] · [[calibration]] · [[abstention]]

[^s1]: baranski-1994
[^s2]: bjorkman-1993
[^s3]: juslin-1997
[^s4]: vickers-2001
