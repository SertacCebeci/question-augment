---
description: "Stated confidence sits near .73 whether the task is answerable or not, so **The regularity.** Juslin,"
aliases: ["hard-easy effect", "difficulty effect", "discriminability effect"]
sources: ["juslin-2000", "klayman-1999", "lichtenstein-1977", "lichtenstein-1982"]
---
# Hard–easy effect

> Stated confidence sits near .73 whether the task is answerable or not, so
> over/underconfidence is very nearly a linear function of the task's
> difficulty — and two of the three things that produce that line are
> statistical artefacts of how it is measured.

## Definition / Mechanism

**The regularity.** Juslin, Winman & Olsson (2000) state it: "The hard–easy[^s1][^s2][^s3][^s4]
effect refers to a covariation between over/underconfidence and task
difficulty; overconfidence is more common for hard item samples, whereas
underconfidence is more common for easy item samples." They date the finding
to Lichtenstein & Fischhoff (1977), "who reported overconfidence for general
knowledge items with a proportion of correctly answered items … below
approximately .75 and underconfidence for items with a proportion correct …
above .75."

**Its shape is a slope, not a bias term.** In Juslin et al.'s quantitative
review — 95 independent data points using *selected* item samples and 35
using *representative* ones, all two-alternative general-knowledge items on
the .5–1.0 half scale — regressing over/underconfidence on proportion correct
gives $b = -.72 \pm .10$ ($r^2 = .70$) for selected samples and
$b = -.53 \pm .15$ ($r^2 = .58$) for representative ones (their Table 4).
Difficulty explains most of the variance in miscalibration.

**The mechanism, as the field's own review puts it.** Lichtenstein, Fischhoff & Phillips (1982) summarise: "Overconfidence is most extreme with tasks of
great difficulty"; "The hard/easy effect seems to arise from assessors'
inability to appreciate how difficult or easy a task is"; and, in the
decision-variable reading, "the hard/easy effect is seen as an inability to
change the cutoffs involved in the transformation from feelings of certainty
to probabilistic responses."

**What holds the level fixed.** Juslin et al.'s Table 3 makes the insensitivity
numerical. Mean subjective probability was **.73** for both selected and
representative item samples ($\pm$.01 and $\pm$.02), while proportion correct
was .64 against .72 — the same reported confidence over an 8-point difference
in accuracy, giving mean over/underconfidence of .09 ($\pm$.02) and .01
($\pm$.02). The number the answerer emits moved by essentially nothing; the
thing it was supposed to track moved a lot.

**The artefact case.** Juslin et al. name three problems, each "sufficient —
alone or in combination — to produce an apparent hard–easy effect in the
data": *scale-end effects* (with a .5–1.0 scale, response error alone forces a
negative slope with a crossover near .75), *linear dependency* (the observed
proportion correct enters both the independent variable and, with the opposite
sign, the dependent one), and *regression effects*. On their own 17 data sets
the slope fell from $-.63 \pm .31$ to $-.41$ after correcting for scale-end
effects, to $-.42$ after correcting for linear dependency, and to
$-.20 \pm .27$, non-significant, $r^2 = .06$, after both (Table 4). What
remains is a predicted overconfidence of .03 at proportion correct .5 and an
underconfidence of .06 at 1.0. They report that Klayman, Soll, González-Vallejo & Barlas (1999) corrected linear dependency across eight
topics and found no significant hard–easy effect either. Their verdict on the
survivor: "The hard–easy effect might be a robust phenomenon but perhaps for
the wrong reasons."

## Known as

| Field | Name there | Match |
|---|---|---|
| JDM / calibration research | hard–easy effect | exact |
| Griffin & Tversky's support-theory line, per Juslin et al. (2000) | difficulty effect | exact — named as the same effect in that paper's own list of its names |
| Signal-detection accounts of confidence (Ferrell & McGoey 1980), per Juslin et al. (2000) | discriminability effect | exact — same, from the decision-variable-partition model |

Not this concept: **overconfidence** is the level of the miscalibration (mean
confidence minus proportion correct at one difficulty), measured as a single
number; the hard–easy effect is its *slope* against difficulty, measured across
item samples, and Juslin et al. treat the two as separate phenomena with
separate evidence. **[[calibration]]** is the property; this note is a
regularity in how that property varies. **Overplacement** (believing one ranks
above others) is a third quantity and no source here measures it.

## Why it matters

Stall 10 asks how far an answerer should commit.

1. **A stated confidence is not a difficulty detector.** The .73-against-.64/.72
   contrast means the answerer's own number carries far less information about
   whether the question is answerable than its magnitude suggests. Anything that
   reads commitment level as evidence of answerability — a router that only asks
   for clarification when the answerer reports low confidence — is reading a
   nearly constant signal.
2. **Difficulty has to be supplied from outside the answerer.** If the level is
   held near-fixed by the response mapping, the correction has to act on the
   mapping or on the task description, not on the judge's self-report — which is
   why in [[calibration-training]] it is *environmental* feedback about the
   task's cue structure, not own-score feedback, that moves discrimination.
3. **It says which item sample is the worst case — within the measured format.**
   The crossover sits near proportion correct .75, so measured miscalibration is
   largest exactly where accuracy is near chance, for two-alternative
   general-knowledge items answered on a .5–1.0 scale. *The following is this
   note's inference and not a measured extension:* if the near-chance
   children's-drawings task of [[warning-as-debiasing]] is read as a point at the
   hard end of this line, then a warning that shifts the reported level by .05
   cannot close a gap of that size there. Juslin et al.'s 130 data points contain
   no multicue perceptual-discrimination task, so nothing measured places that
   task on this regression; and by the same argument the drawings-task gap would
   itself be partly scale-end and dependency, which cuts the other way.
4. **The magnitude is not usable as a prior.** After two of the three
   corrections the slope is not distinguishable from zero. This wiki may use the
   *direction* and the crossover location as a design assumption; it may not use
   "overconfidence scales with difficulty" as a quantity.

## Transfer

| | |
|---|---|
| **Home field** | undergraduates answering two-alternative general-knowledge items, confidence on a .5–1.0 half scale, difficulty operationalised as the observed proportion correct of an item sample |
| **Here** | an answering agent emitting a confidence with an answer, on a question whose answerability it cannot check |
| **What survives** | the dissociation between a near-invariant reported level and a varying accuracy; the location of the crossover as the point separating over- from underconfidence; and the demand that any measured difficulty-confidence relation be corrected for linear dependency before it is believed |
| **What does not** | the slope's magnitude, which is mostly attributable to the .5–1.0 scale and to shared measurement error and shrinks to non-significance when both are corrected; the format, since Juslin et al. note that on a full-range 0–1 interval-estimate format "the scale-end effects are perfectly confounded with over/underconfidence", so neither the corrections nor the crossover carries to an answerer giving intervals or free text; and the task type — the corpus is general-knowledge items throughout, so placing a perceptual-discrimination task such as [[warning-as-debiasing]]'s on this line is this note's inference (point 3), not a transfer the data support |

## Limits

- **The independent variable is measured with the error that generates the
  dependent one.** Difficulty here *is* the observed proportion correct, and
  over/underconfidence is mean confidence *minus* that same proportion.
  Lichtenstein, Fischhoff & Phillips (1982) already note "difficulty was defined
  on the basis of subjects' performance"; Juslin et al. formalise it as linear
  dependency. Every claim above about how confidence relates to difficulty
  inherits this, including the .73 invariance.
- **The .73 invariance is a between-study contrast.** It compares selected
  against representative item samples pooled across 130 data points from
  different laboratories, not a within-subject difficulty manipulation, and the
  selected/representative split is a claim about item *sampling* which Juslin
  et al. argue is not reducible to difficulty. It is evidence that reported
  confidence is stable where accuracy is not; it is not a controlled test of
  insensitivity to difficulty.
- **The corrections are stacked.** Juslin et al. say so themselves — each
  correction "involves assumptions, the appropriateness of which may be
  difficult to ascertain, and the mishaps and errors might accumulate" — so
  the residual $-.20$ is their estimate, not a measurement, and point 4 of *Why
  it matters* is only as strong as that.
- **The numbers above rest on one reading.** The Table 3 figures (.73; .64/.72;
  .09/.01), the Table 4 slopes (−.72, −.53, −.63 → −.41 / −.42 / −.20,
  $r^2 = .06$) and the quoted sentences are taken from a single reading of the
  Juslin et al. (2000) PDF and were **not** independently re-confirmed, because
  the available copy is image-encoded. The paper, its identifiers, the
  n = 95 / n = 35 split, the three artefacts and the conclusion were confirmed;
  the exact figures and verbatim quotations stand as `[?]`.
- Lichtenstein & Fischhoff (1977) was not obtained; the .75 crossover and the
  original finding are read in Juslin et al. (2000) and in Lichtenstein,
  Fischhoff & Phillips (1982) [?]. Klayman et al. (1999) is likewise read only
  as reported by Juslin et al. [?].
- No source here measures a language model, and whether a model's stated
  confidence is produced by anything like a response-scale mapping is untested
  ([[verbal-probability-expressions]]).

## Related

[[calibration]] · [[calibration-training]] · [[warning-as-debiasing]] · [[abstention]] · [[verbal-probability-expressions]] · [[outcome-feedback]]

[^s1]: juslin-2000
[^s2]: klayman-1999
[^s3]: lichtenstein-1977
[^s4]: lichtenstein-1982
