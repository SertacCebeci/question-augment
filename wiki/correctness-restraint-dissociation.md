---
description: "In a retrieval-grounded LLM math tutor, task success hit 94% while the tutor disclosed the answer in 46% of dialogues, mostly on turn one: correctness and pedagogical restraint come apart."
aliases: ["success-telling dissociation", "answer-disclosure front-loading", "Success@K versus Telling@K"]
sources: ["doi-10-58445-rars-4229"]
---
# Correctness-restraint dissociation

A guided tutor has two separable jobs: get the student to the right answer, and refrain from stating it. Dialogue-tutoring benchmarks score them separately, as Success@K (the student reaches the correct answer within K turns) and Telling@K (the tutor discloses it within K turns).[^c1] The two are not redundant, because the trivial strategy of stating the answer immediately maximizes both.[^c2] A tutor with high Success@K therefore shows nothing about restraint until Telling@K is read beside it.

## What was measured

Umair and Munir (BR-Tutor) ran an open-weight 20B model, with a similarity-gated retriever that injects one real tutor turn (annotated with its talk move) into the prompt. They tested it on 50 MathDial problems with the same model playing tutor and student. The reported profile was Success@5 = 94% with Telling@5 = 46%.[^c3]

The curves were flat from the second turn on. Forty-five of fifty dialogues resolved correctly on the first turn and only two more later.[^c4] Of the 23 dialogues with disclosure, 21 had it at turn one.[^c5] The authors read this as an opening-move disposition, not a fallback after the student stalls: a tutor that conceded after the student failed would show a Telling curve that rises across turns, and this one does not.[^c6] Their explanation, stated as plausible and not tested, is that instruction-tuned helpfulness overrides the Socratic prompt on the first response, before any sign of student difficulty exists to scaffold against.[^c7]

Against reported baselines the system's Telling@5 of 46% was far above the ChatGPT baseline's 16%.[^c8] Its Success@5 of 94% exceeded every baseline's at K = 5, including the human ground truth (59% at K = 5).[^c9] This is the difference the authors call a dissociation: capability is competitive, discourse style is not.

## What follows for asking and answering

Success cannot stand in for restraint. A responder that answers early can score well on correctness-based measures, so a single outcome metric hides the failure. The authors' own suggested remedy is explicit first-turn constraints on what the tutor may reveal, or direct optimization for pedagogical behavior, with retrieval supplying the form of the move, not suppressing disclosure by itself.[^c10] This is their recommendation, not something tested in the paper.

## Limits

- Only the extended system was run, with no ablation. The paper itself says no claim about retrieval's effect on either metric is supported.[^c11] The dissociation describes the system as built. It does not show that retrieval fails to reduce disclosure.
- n = 50 gives wide intervals (Telling roughly 27 points wide), so small differences are not resolvable.
- The baseline comparison is indicative, not controlled: base model, sample, turn cap and simulated student differ.[^c12] Baseline values for some rows were read off printed figures.
- Self-play: the same model is tutor and student, which may inflate Success@K. No human learners took part, so simulated success is not evidence of learning.
- The mechanism (instruction-tuned helpfulness winning on turn one) is the authors' conjecture. The data show front-loading but do not identify its cause.
- Disclosure was scored as "supplied or confirmed" the answer, so some Telling may be confirmation, not a reveal.

## Related

- [[gated-socratic-scaffolding]] — a tutor design that withholds the answer by rule and was tested in a randomized trial
- [[premature-closure]] — answering before the evidence supports it, the failure disclosure on turn one resembles
- [[over-reliance-discrimination-failure]] — the student-side harm that answer disclosure is meant to avoid

[^c1]: doi-10-58445-rars-4229 — "Telling@K, is the proportion"
[^c2]: doi-10-58445-rars-4229 — "The metrics are not redundant, since the trivial strategy of"
[^c3]: doi-10-58445-rars-4229 — "46% answer disclosure rate (Telling@5), with both metrics rapidly saturating by the second"
[^c4]: doi-10-58445-rars-4229 — "forty-five of the fifty dialogues resolve correctly on the first turn and only two more resolve"
[^c5]: doi-10-58445-rars-4229 — "disclosure is predominantly an opening-turn phenomenon rather"
[^c6]: doi-10-58445-rars-4229 — "that rose across turns; this system's curve does not rise, so disclosure is an opening-move"
[^c7]: doi-10-58445-rars-4229 — "This is consistent with instruction-tuned helpfulness overriding the prompt's Socratic"
[^c8]: doi-10-58445-rars-4229 — "Second, BR-Tutor's Telling@5 of 46% is far above the ChatGPT baseline's Telling@5 of 16%"
[^c9]: doi-10-58445-rars-4229 — "is within range of the ground truth's own Success@10 of 82%, reached five turns earlier."
[^c10]: doi-10-58445-rars-4229 — "explicit first-turn constraints on what the tutor may reveal, or by optimizing the tutor directly for"
[^c11]: doi-10-58445-rars-4229 — "Only the extended system was evaluated."
[^c12]: doi-10-58445-rars-4229 — "this comparison is indicative rather than controlled"
