---
description: "K-12 learner feedback alone, with no Socratic specification set in advance, drove a GPT tutor prompt toward staged hints, pauses and checkpoints in four weeks."
aliases: ["SocratiCode"]
sources: ["lucas-2026"]
---
# Feedback-driven Socratic convergence

> A tutor prompt that started as a flexible explanation generator, revised
> only against weekly non-expert learner feedback with no theory-driven
> specification, ended up at the same structural constraints — staged
> hints, mandatory pauses, checkpoints — that theory-driven Socratic tutors
> are built with from the start.

## Definition / Mechanism

Lucas et al. (2026) run a four-week participatory design
study of SocratiCode, a GPT-based Python tutor for two K-12 novices. The
initial prompt was a general adaptive tutorial generator; it was revised
weekly using only the two students' daily and weekly feedback, not a
Socratic-tutoring specification chosen in advance: "Across W1–W4, the
system evolved from adaptive explanatory tutorialing toward a more
dialogic tutoring flow with increasingly Socratic characteristics."[^c1]

The endpoint the feedback loop converged on names the same constraints
found elsewhere in this wiki under controlled or engineered designs: "By
W4, the prompt had stabilized into a structured interactive flow
characterized by pauses, reflection, learner response requirements, and
hard stopping points. At this stage, the system no longer suggested
unsolicited next steps and instead ended lessons explicitly."[^c2]

The paper also records a failure the convergence did not remove:
"Midway through the study, both participants also noted that SocratiCode
sometimes acted as a 'yes-man,' prioritizing its own answers over learner
reasoning," which the authors report as a reason human intervention
remained necessary for correcting misconceptions and challenging weak
reasoning.[^c3]

## Why it matters

The other Socratic-tutor notes on this stall build their [[answer-withholding-supervisor-architecture|hint ladder]] or
gating rule from a stated design principle first
([[staged-socratic-hint-policy]]'s three fixed stages,
[[gated-socratic-scaffolding]]'s evaluator-triggered gate) and then measure
its effect. This source inverts the order: the structure is not chosen,
it is what remained after four weeks of unguided revision against only
two learners' complaints. That the search landed on the same shape —
graduated hints before a full solution, a pause point that requires
learner input before continuing — is weak evidence that this shape is not
an artifact of one lab's specification but something the feedback itself
selects for, at least for this population and this task.

## Limits

- n = 2 K-12 participants, one GPT-5 deployment, Python only; the authors
  themselves call the study preliminary and the generalizability claim
  explicitly limited.[^c4]
- Qualitative, self-reported thematic analysis by two coders with no
  stated inter-rater [[calibration|reliability]] figure and no control condition (no
  parallel run of a non-Socratic tutorial generator against the same
  learners); the "improved engagement" and "improved clarity" claims are
  the study's own inductive codes, not a measured pre/post or
  between-arms comparison.
- The convergence claim rests on one lineage (one prompt, one team, one
  four-week window); it is not established that a different starting
  prompt or different learners would converge on the same structure.
- The "yes-man" observation is a single retrospective remark from two
  participants, not characterized further (frequency, trigger, or
  whether later prompt revisions reduced it); this wiki does not extend
  it to the sycophancy notes elsewhere ([[sycophantic-capitulation]] etc.)
  because the source gives no mechanism, only the label.
- `lucas-2026` is queued/unverified `[?]` in this wiki pending the
  verifier.

## Related

[[staged-socratic-hint-policy]] · [[gated-socratic-scaffolding]] · [[socratic-method]] · [[non-advisory-dialogue]]

[^c1]: lucas-2026 — "Across W1–W4, the system evolved from adaptive explanatory tutorialing toward a more dialogic tutoring flow with increasingly Socratic characteristics."
[^c2]: lucas-2026
[^c3]: lucas-2026
[^c4]: lucas-2026 — "we worked with only two K–12 participants, which limits the generalizability of our findings."
