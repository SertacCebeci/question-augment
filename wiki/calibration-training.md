---
description: "Calibration is trainable cheaply and fast by *scored feedback*, but each calibration is a property of a set of answers."
aliases: ["probability training", "training for calibration", "calibration feedback training", "debiasing training for forecasters"]
sources: ["chang-2016", "hauenstein-2025", "lichtenstein-1980", "lichtenstein-1981", "lichtenstein-1982", "mellers-2014", "murphy-1977", "stone-2000"]
---
# Calibration training

> Calibration is trainable cheaply and fast by *scored feedback*, but each
> feedback type moves only its own component, almost all the gain arrives at the
> first feedback, transfer to a different task is modest at best — and *telling*
> an answerer it is overconfident is not one of the things that works.

## Definition / Mechanism

[[calibration]] is a property of a set of answers. **Calibration training** is[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8]
the intervention that changes it: the answerer emits probabilities, the
outcomes are scored, and the score is returned. Three findings carry this note.

**Scored feedback on one's own probabilities works, once.** Lichtenstein & Fischhoff (1980) ran 11 sessions of 200 two-alternative assessments with
personalised feedback — calibration graphs, probability score, overconfidence
measure, discussed for 5–10 minutes. Their own later review (Lichtenstein, Fischhoff & Phillips 1982) states the improvement was appreciable and "all of
which occurred between the first and the second session". Calibration training
is a one-shot correction, not a curve. Their Experiment 2 cut the training to
three sessions and reproduced the same pattern of learning and limited
generalisation.

**What it does not carry.** The same review records modest generalisation to
tasks differing in difficulty, content and response mode (four alternatives
rather than two), but *no* improvement on a fractile assessment task and none on
discriminating European from American handwriting. Calibration is not a trait
the answerer acquires; it is fitted to the task it was scored on. Stone & Opel (2000), reviewing this study alongside Benson & Önkal (1992), add that the
calibration feedback improved calibration "primarily by decreasing the level of
overconfidence" and had **no impact on discrimination**.

**Being told is not being trained.** Lichtenstein & Fischhoff (1981) gave one
group three single-spaced pages explaining calibration outright — "we want you
to be well calibrated in the same sense that a thermometer is well calibrated" —
against a group with brief standard instructions, over 200 general-knowledge
items. "The instructions had no statistically significant effect on any
measure"; most subjects were overconfident either way. The nearest thing to a
level effect comes from Fischhoff & Slovic (1980), as reported in the same 1982
review: instructions warning that a discrimination task (Asian versus European
children's drawings) might be impossible lowered the mean response by about
.05, and "substantial overconfidence was still found". Instruction moves the
level slightly at most and does not repair the calibration.

**Environmental feedback on the task.** Stone & Opel (2000) separated the two
components in one domain. Performance feedback (own scores) reduced
overconfidence; environmental feedback (information about the task's cue
structure) improved **discrimination** — and *increased* overconfidence.
Neither improved the other's component.

**Content training.** In the IARPA geopolitical tournaments, Chang, Chen, Mellers & Tetlock (2016) gave a module (comparison classes and base rates, time
series, averaging independent estimates, post-mortems, selecting effort)
designed never to exceed one hour; trained forecasters beat controls on
standardised Brier score in all four years. Mellers et al. (2014) report
probability training improved both calibration and resolution.

**The contested part.** Hauenstein, Thomas, Illingworth & Dougherty (2025)
re-analysed the same tournament under an item-response model of latent
forecasting ability; once extraneous method variance was controlled, the best
models across the first two years substantially reduced, eliminated, or in
places reversed the training and teaming effects.

**The environment that trains without training.** Murphy & Winkler (1977)
showed operational weather forecasters produce reliable probability forecasts.
The conditions are the ones no conversational answerer has: one repeated
question, prompt outcome, scored every day.

## Known as

| Field | Name there | Match |
|---|---|---|
| JDM / psychology of judgment | training for calibration | exact |
| Forecasting tournaments (Tetlock, GJP) | probability training | close — a content module, not outcome feedback |
| Metacognition / education | calibration feedback training | close — measured on exam-score prediction, not on events |
| Applied forecasting | debiasing training for forecasters | close — targets a bias list, of which overconfidence is one |

Not this concept: **CHAMPS KNOW** is the name of one training module, an
instance and not a synonym; **[[calibration]]** is the property being trained,
measured over answers, not the intervention.

## Why it matters

Stall 10 asks how far an answerer should commit.

1. **"You are overconfident, hedge" is not a fix.** That instruction is exactly
   what a prompt-level "be calibrated" implements, and it is the one
   intervention with a null result (Lichtenstein & Fischhoff 1981) or a level
   effect without a calibration gain (Fischhoff & Slovic 1980). A hedge produced
   this way removes fewer worlds ([[constraint-as-information]]) and buys no
   reliability.
2. **Which failure is being corrected must be named first.** Badly ordered
   scores need the task's cue structure, not own-score feedback; a wrong level
   with good ordering needs the reverse (Stone & Opel). A single "be calibrated"
   step targets neither.
3. **Calibration is per-domain.** Zero transfer to the fractile and handwriting
   tasks means an answerer calibrated on one question family carries no
   guarantee to another — a stopping threshold tuned against measured
   calibration ([[stopping-rules]], [[sprt]]) must be re-fitted per domain.

## Transfer

| | |
|---|---|
| **Home field** | humans emitting probabilities on repeated, resolvable questions with ground truth, scored in batches of hundreds |
| **Here** | an answering agent deciding how far to commit on one question inside a task, usually without ground truth arriving at all |
| **What survives** | the dissociation of calibration from discrimination and the two feedback types that address them; the one-shot shape of the learning curve; the null result for instruction as against scored feedback |
| **What does not** | the outcome loop itself — the answerer here rarely learns whether it was right, so nothing plays the role of the scored batch; and the generalisation results, measured between laboratory almanac tasks, say nothing about the distance between two substantive domains |

## Limits

- **A claim previously carried here has been withdrawn.** This note earlier
  reported that Lichtenstein & Fischhoff (1980) Experiment 2 showed
  overconfidence feedback lowering confidence without improving calibration or
  resolution. The paper's abstract describes Experiment 2 as a three-session
  reduction of the same feedback training, not an instruction study, and the
  authors' 1982 review describes no such experiment. The full text of the 1980
  paper is still paywalled and was not obtained [?]; every claim above about
  the 1980 study is taken from the authors' own 1982 review and from Stone &
  Opel (2000), not from the paper itself.
- The replacement evidence for "instruction does not calibrate" is one null
  result on 200 almanac items (Lichtenstein & Fischhoff 1981, a Decision
  Research technical report, not peer-reviewed) plus one [[warning-as-debiasing|warning-instruction]]
  result read in the 1982 review rather than in Fischhoff & Slovic (1980) [?].
  A null on a technical report is weak evidence; it bounds how strong point 1 of
  *Why it matters* may be stated.
- The per-domain claim rests on transfer tasks that were variations of the same
  laboratory assessment; how far the failure extends across substantively
  different domains is measured by no source here.
- Chang et al. (2016) and Mellers et al. (2014) are directly contested by
  Hauenstein et al. (2025) on method variance. This note reports both and does
  not adjudicate; the GJP effect sizes are not a design target. Brier score
  mixes calibration and resolution, so a Brier gain is not a calibration gain.
- No source here trains or tests an LLM answerer, and whether a model's stated
  confidence tracks its internal probability at all is open
  ([[verbal-probability-expressions]]).

## Related

[[calibration]] · [[verbal-probability-expressions]] · [[constraint-as-information]] · [[stopping-rules]] · [[semantic-entropy]] · [[sprt]]

[^s1]: chang-2016
[^s2]: hauenstein-2025
[^s3]: lichtenstein-1980
[^s4]: lichtenstein-1981
[^s5]: lichtenstein-1982
[^s6]: mellers-2014
[^s7]: murphy-1977
[^s8]: stone-2000
