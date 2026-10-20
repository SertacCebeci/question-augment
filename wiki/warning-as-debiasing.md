---
description: "A warned-and-reframed instruction — \"this task may be impossible, answer .5 A **warning** is the cheapest debiasing intervention: the judge is told, before answering, that the task is hard,"
aliases: ["warning instruction", "debiasing by warning", "task-impossibility warning", "caution instruction"]
sources: ["fischhoff-1980", "fischhoff-1982", "schall-2017"]
---
# Warning as debiasing

> A warned-and-reframed instruction — "this task may be impossible, answer .5
> if you like" — moved judges' confidence *level* by about .05 and left the
> overconfidence intact, and 92% of them declined the offered .5.

## Definition / Mechanism

A **warning** is the cheapest debiasing intervention: the judge is told,[^s1][^s2][^s3]
before answering, that the task is hard, that the cues may be invalid, or
that people are typically overconfident. Nothing about the judge's own past
performance is returned; nothing about the task's structure is supplied. In
Fischhoff's (1982) classification of debiasing strategies for "faulty
judges", warning is the first and weakest of an escalating four — warn,
describe the bias, give personalised feedback, train extensively.

**The primary result.** Fischhoff & Slovic (1978/1980) ran eight experiments
on confidence in multicue discrimination. Experiment 5 asked 92 subjects to
say whether each children's drawing was by a European or an Asian child;
accuracy was 54.1% (with labelled study examples) and 52.3% (without),
against mean confidence of .667 and .677 — near-chance discrimination held
at two-thirds confidence. Experiment 6 repeated the task with 76 new
subjects under discouraging instructions. Two things changed together: the
framing paragraph became "many people have claimed that the art of small
children is the same in all cultural settings; others disagree", and the
response instructions appended

> "Remember, it may well be impossible to make this sort of discrimination.
> Try to do the best you can. But if, in the extreme, you feel totally
> uncertain about the origin of all of these drawings, do not hesitate to
> respond with .5 for every one of them."

The authors report that "the change in instructions had some effect in the
appropriate direction, reducing the mean confidence of both groups by
approximately .05" — to .631 and .627 — while accuracy was 57.7% and 45.6%.
"Only 6 of 76 subjects (4 in the labels group, 2 in the no-labels group)
accepted the option of responding with .5 to all items." Both groups
remained overconfident.

**Two separable effects, both small.** The warned-and-reframed instruction
shifted the *level* of commitment; it did not restore the correspondence
between commitment and accuracy, and in the no-labels group accuracy fell
while confidence fell by the same order. The explicitly offered abstention
was refused by 92% of judges who had been told in the same paragraph that
using it was legitimate — a refusal that, unlike the .05, is a
within-experiment count and does not depend on the between-experiment
contrast.

**The boundary condition.** Schall, Doll & Mohnen (2017) argue the null is a
result about *warning design* rather than about warnings: across two
experiments on interval estimates they report that repeated, dynamic
warnings — as opposed to a single static one — do reduce overestimation.
The Fischhoff & Slovic warning was static and delivered once.

## Known as

| Field | Name there | Match |
|---|---|---|
| JDM / debiasing literature | warning (step 1 of the faulty-judges escalation) | exact |
| Fischhoff & Slovic's own text | discouraging instructions | exact |
| Human factors / ergonomics, via Schall et al. | static vs dynamic warning design | close — the same intervention, parameterised by repetition and salience rather than treated as one thing |
| LLM prompting | "be careful, you may be wrong" / calibration prompt | close — same content and same one-shot delivery, but no source here measures it on a model |

Not this concept: **"a little learning"**, the title finding of the same
paper, is the *other* result — that studying labelled examples raises
confidence whether or not it raises accuracy — and is measured differently
(a labels-vs-no-labels contrast across eight tasks, not a warned-vs-unwarned
contrast). **[[calibration-training]]** is scored feedback on the judge's own
probabilities, an intervention Fischhoff ranks two steps above a warning and
which does move calibration.

## Why it matters

Stall 10 asks how far an answerer should commit.

1. **A prompt is a warning.** "You may be wrong, express uncertainty" is
   close to the intervention measured here, and its measured effect is a
   small downward shift of the stated number with the miscalibration
   surviving. A hedge bought this way removes fewer worlds
   ([[constraint-as-information]]) and buys no [[calibration|reliability]].
2. **Offering the exit is not enough to make it used.** [[abstention]]
   treats "I don't know" as a second function with its own threshold; this
   experiment shows what happens when the option is merely *offered* to a
   judge who sets their own threshold — 7.9% uptake at chance-level
   accuracy. An abstention channel that is not priced is an abstention
   channel that is not used.
3. **Warning and feedback are not interchangeable, and neither is a
   substitute for the other.** Fischhoff's escalation orders them; the wiki's
   commitment mechanisms should name which rung they are on before claiming
   an effect.

## Transfer

| | |
|---|---|
| **Home field** | undergraduates making forced binary discriminations on multicue stimuli, one session, no stake, confidence reported on a .5–1.0 half-scale |
| **Here** | an answering agent instructed, in-context and once, to be cautious about a question whose answerability it cannot check |
| **What survives** | the dissociation of a *level* shift from a *calibration* repair, and the size of the level shift relative to the size of the miscalibration; the refusal of an offered abstention when nothing prices it |
| **What does not** | the magnitude — .05 is a number for these stimuli, this scale and a package that also reframed the task, and no source here delivers this warning to a model; and the mechanism, since a human's reluctance to answer .5 may be a demand characteristic of the experiment ("any task set before them in an experiment must be possible", as the authors put it), which has no obvious counterpart in a model |

## Limits

- **The warning comparison is between experiments, not within one, and the
  manipulation was not the warning alone.** Experiment 6's 76 subjects are
  not Experiment 5's 92; the .05 is a difference of group means across two
  runs, and the report gives no significance test for it that this note
  verified. Experiment 6 also changed the framing paragraph (the
  "same in all cultural settings" cover story) alongside the response
  instruction, so the .05 is the effect of a warning-plus-reframing package
  and cannot be attributed to the warning by itself. The claim this note
  rests on — that such an instruction moves the level and not the
  calibration — is therefore an effect-size claim on an unrandomised,
  co-manipulated contrast, not a tested null.
- Accuracy in both experiments sits at or near 50%, so calibration cannot be
  decomposed into level and discrimination here in the way
  [[calibration-training]] does for feedback; "overconfidence persists" is
  the only calibration statement the data support.
- The text read is the DTIC technical report (PTR-1060-78-6, June 1978); the
  published chapter is Fischhoff & Slovic (1980) in Nickerson (ed.),
  *Attention and Performance VIII*, 779–800, which was not obtained. Every
  experiment-level figure above — the 92 and 76 subject counts, the
  .667/.677 and .631/.627 means, the accuracies, the 6-of-76 count and the
  quoted .5 instruction — is quoted from that report and was **not
  independently confirmed** against the published chapter or by a second
  reader [?]. The verifier could confirm the paper, its authorship and the
  children's-drawings task, but not these numbers.
- Schall et al. (2017) is read from its abstract and secondary description
  only; the full text is paywalled and was not obtained [?]. Its task is
  interval estimation, not binary discrimination, so "dynamic warnings work"
  is not a direct rebuttal of Experiment 6.
- No source here warns a machine answerer. The transfer to prompts is this
  wiki's inference, not a measured result.

## Related

[[calibration-training]] · [[abstention]] · [[calibration]] · [[outcome-feedback]] · [[constraint-as-information]] · [[verbal-probability-expressions]]

[^s1]: fischhoff-1980
[^s2]: fischhoff-1982
[^s3]: schall-2017
