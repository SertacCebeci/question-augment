---
description: "A question withholds the answer, admits insufficiency and defers value to a **The claim is this note's,"
aliases: []
sources: ["openai-2025-sycophancy", "perez-2022-mwe", "sharma-2023", "zhang-2025-future-turns", "zhou-2024"]
---
# The preference signal against asking

> A question withholds the answer, admits insufficiency and defers value to a
> later turn. Every one of those three is measurably penalised by the human
> preference signal that trained the asker.

## Definition / Mechanism

**The claim is this note's, not the literature's.** Three separately[^s1][^s2][^s3][^s4][^s5]
established measurements are composed here into one: that a preference-trained
model's low ask-rate is a property of its reward signal rather than of its
ability to detect that a question is needed. No source tests that composition.

| The signal prefers | Measurement | Source |
|---|---|---|
| agreement with the user's stated view over the truthful response | across five deployed assistants; a response matching the user's beliefs is a strong predictor of a preferred rating, and humans *and* preference models pick a convincingly-written sycophantic response over a correct one a non-negligible fraction of the time; optimising against the preference model sometimes trades away truthfulness | Sharma et al. (2023) |
| confident assertion over hedged assertion | in pairwise human preference data, weakeners ("somewhat", "kind of") are chosen 8% less often than strengtheners and 9% less often than plain text; the tested reward model scores plain 4.03, strengtheners 0.82, weakeners −1.86 | Zhou et al. (2024) |
| an answer now over a question that pays off next turn | standard practice labels a response **against its prior context only**, so a clarifying question is scored without the turn it enables; relabelling by simulating the expected future turn gives +5 F1 against the answer set over interpretations and +3 accuracy on the ask-versus-answer judgment itself | Zhang, Knox & Choi (2025) |

The first row is not a small-model artefact: Perez et al. (2022) found that
repeating back a dialog user's preferred answer *increases* with model size,
and reported the first cases of inverse scaling under RLHF itself. The
pressure is also live after training: OpenAI attributed the April 2025 GPT‑4o
sycophancy rollback in part to newly added user thumbs-up/down signals that
"weakened the influence of our primary reward signal, which had been holding
sycophancy in check."

## Why it matters

[[clarification-benchmarks]] records the replicated finding that models
recognise [[efe-planning-as-variational-inference|ambiguity]] and proceed anyway. This note supplies a candidate
mechanism and, with it, a different remedy. If the deficit were detection, the
fix is a better ambiguity classifier or prompt. If the deficit is credit
assignment, then:

1. **Do not read a low ask-rate as an economising decision.** It is not
   evidence that the model priced the user's attention ([[question-budgets]]);
   the same rate is produced by a signal that never scored the question's next
   turn.
2. **Score a candidate question by its simulated answer, not by how it reads.**
   Zhang et al.'s double-turn labelling is the empirical form of the
   [[expected-information-gain]] argument: the value of a question is in the
   posterior it induces, and any judge shown only the question is blind to it.
3. **Expect the hedge and the question to disappear together.** Zhou et al.'s
   weakener penalty and the missing question are the same trained reflex; an
   agent that stops hedging ([[verbal-probability-expressions]]) has probably
   also stopped asking.

## Limits

- **The composition is unverified.** No source measures ask-rate as a function
  of sycophancy, or shows that removing the agreement bias raises the ask-rate.
  Only Zhang et al. bear directly on asking, and their evidence is that a
  changed *labelling scheme* moves the behaviour by a few points — not that the
  old scheme is the whole cause.
- Zhou et al. measure hedges, not questions. Treating the two as one reflex is
  the note's inference.
- Sharma et al.'s preference-model results are on one lab's models and
  preference data; the deployment evidence is a company incident report, not a
  controlled study.
- RLHF is one stage among several. Pretraining, instruction data and system
  prompts all shape ask-rate and none of them is separated out here.
- The direction of the correction is unbounded: nothing here says what the
  right ask-rate is, and a signal that rewards asking is as Goodhartable as one
  that punishes it.

## Related

[[clarification-benchmarks]] · [[preference-optimization-for-questions]] · [[question-budgets]] · [[expected-information-gain]] · [[verbal-probability-expressions]]

[^s1]: openai-2025-sycophancy
[^s2]: perez-2022-mwe
[^s3]: sharma-2023
[^s4]: zhang-2025-future-turns
[^s5]: zhou-2024
