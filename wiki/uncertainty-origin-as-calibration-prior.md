---
description: "**This wiki's inference, not a result.** A question nobody designed can be Two measured facts and one taxonomy are in the wiki: nearly linear in difficulty with the crossover near proportion correc…"
aliases: ["uncertainty origin as calibration prior"]
sources: ["baranski-1994", "bjorkman-1993", "fischhoff-1980", "juslin-1997", "juslin-2000"]
---
# Uncertainty origin as calibration prior

> **This wiki's inference, not a result.** A question nobody designed can be
> assigned an origin class by inspecting its description — and on that reading
> the children's-drawings task is Brunswikian, so the general-knowledge line is
> its reference and the sensory-underconfidence dispute does not bear on it.

## Definition / Mechanism

Two measured facts and one taxonomy are in the wiki:[^s1][^s2][^s3][^s4][^s5]

- on two-alternative **general-knowledge** items, over/underconfidence is very
  nearly linear in difficulty with the crossover near proportion correct .75
  (Juslin, Winman & Olsson 2000 — [[hard-easy-effect]]);
- on **sensory pair comparisons**, the modal error is *under*confidence
  (Björkman, Juslin & Winman 1993 — [[sensory-underconfidence]]), contested by
  Baranski & Petrusic (1994);
- Juslin & Olsson (1997) index the confidence model on the *origin* of the
  uncertainty rather than on the domain of the stimulus, so that a task can be
  visual and still Brunswikian — that step is theirs, reported in
  [[origins-of-uncertainty-in-judgment]], not conjectured here.

**The conjecture.** What this note adds is that the index can be *read off a
task description from the outside*, for a question no experimenter built to
isolate an origin — and that doing so changes which measured regularity an
asker may carry over.

**The case this resolves.** Fischhoff & Slovic's children's-drawings task
(1978/1980 — [[warning-as-debiasing]]) asks whether a drawing is by a European
or an Asian child. Nothing about the drawing is described as hard to *see*;
what is unknown is which visual features predict the child's origin and how
strongly. Classified on that description it is a Brunswikian multicue
categorisation wearing a visual stimulus, so:

1. the general-knowledge line of [[hard-easy-effect]] is the right reference
   for it, and point 3 of that note — placing the near-chance drawings task at
   the hard end — is licensed by *task class* rather than left hanging on the
   absence of perceptual tasks from the Juslin corpus;
2. [[sensory-underconfidence]] does **not** apply to it, so the Ottawa–Uppsala
   disagreement, whichever way it resolves, does not bear on the drawings
   result at all;
3. the discriminator is not "is the task perceptual?" but "is the uncertainty
   Thurstonian?" — so a search of the perceptual literature is the wrong
   search for a task of this class, however visual its material.

**A second inference, weaker and unsourced.** On the classical content of
Thurstone's model, discriminal dispersion makes a repeated presentation of the
same stimulus a *fresh draw* of the internal value, while a Brunswikian
judgment from fixed cues has no such draw. If that carries, then re-asking the
same answerer the same question is informative in the first class and
near-worthless in the second, and only in the second must the constraint come
from a different source (Source). No source read here measures this;
see Limits.

## Why it matters

Stall 10 asks how far an answerer should commit. Every correction the wiki
holds for commitment level was fitted on one question class. This note says
what has to be true before one of them may be applied to a new question — and
that the test is not the one an implementer would reach for. A router that
sorts questions into "perceptual" and "factual" to pick an uncertainty
correction would put the drawings task in the wrong bin and apply a correction
of the wrong sign.

## Transfer

| | |
|---|---|
| **Home field** | psychophysics and JDM, where the origin of a task's uncertainty is decided by the experimenter who built the task |
| **Here** | an asker classifying a question that nobody designed, in order to choose which measured [[calibration]] regularity to apply to the answer |
| **What survives** | the *form* of the selector — origin of uncertainty, not stimulus modality — and the worked classification of one task (the drawings task) that the modality test gets wrong |
| **What does not** | any procedure: no source read here classifies a task from the outside, so the classification above is made by inspection of a task description and could be made differently by another reader; and the two-class exhaustiveness, since a real question may mix origins in a proportion nothing here measures |

## Limits

- **This is a conjecture and its load-bearing step is a classification made by
  this note.** No source classifies the children's-drawings task; Fischhoff &
  Slovic call it multicue discrimination and do not use Juslin & Olsson's
  taxonomy, which postdates them by two decades. Worse, the *input* to the
  classification is itself unconfirmed: the task description used here comes
  from the unpublished DTIC technical report (PTR-1060-78-6, 1978) via
  [[warning-as-debiasing]], which marks every experiment-level detail of that
  report as not independently confirmed against the published chapter [?]. The
  classification rests on the task's description alone; the presentation
  conditions of the drawings — size, reproduction quality, viewing time — are
  not reported in anything read here, and if they made the stimulus itself
  hard to resolve then the task is partly Thurstonian and the argument weakens
  in proportion.
- **The second inference has no source at all.** Nothing cited here measures
  whether repeated elicitation from one answerer is informative in either
  class; the discriminal-dispersion premise is taken from the classical
  content of Thurstone's model and not from any work read in this cell [?],
  and juslin-1997 was read from its abstract only. It reaches into
  Source and would change what a practitioner does with repeated
  elicitation, so it is held here as a flagged consequence awaiting its own
  cell, not as a claim this note supports.
- **It inherits an unread criterion.** [[origins-of-uncertainty-in-judgment]]
  records that Juslin & Olsson's empirical test separating the two modes was
  not read; without it this note has no way to *check* its classification
  against the sources' own method, only to argue for it.
- **The prior it licenses is directional only.** [[hard-easy-effect]] shows the
  general-knowledge slope's magnitude is not usable, so the most this note can
  hand a practitioner is a sign and a crossover location, not a number.
- **It says nothing about machine answerers.** Neither class has been
  established for a model that samples tokens, so for an LLM the selector
  identifies no prior at all — which is the honest reading: on the conjecture,
  the wiki currently has *no* applicable miscalibration prior for a model
  answering an arbitrary question.

## Related

[[hard-easy-effect]] · [[sensory-underconfidence]] · [[origins-of-uncertainty-in-judgment]] · [[warning-as-debiasing]] · [[calibration]]

[^s1]: baranski-1994
[^s2]: bjorkman-1993
[^s3]: fischhoff-1980
[^s4]: juslin-1997
[^s5]: juslin-2000
