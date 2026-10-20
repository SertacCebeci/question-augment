---
description: "A 3-arm EEG study finds an unrestricted answer-giving chatbot produced higher immediate learning gains than a Socratic hint-only or EEG-adaptive tutor, despite lower engagement."
aliases: []
sources: ["deffarges-2026"]
---
# Answer-withholding learning tradeoff

> Withholding the final answer and asking guiding questions instead does not,
> by itself, beat just giving the answer — on an immediate post-test, giving
> it won.

## Definition / Mechanism

Clin Deffarges, Kosmyna & Maes (2026) randomise 50
participants with no prior knowledge of nuclear safety protocols to one of
three AI study-assistant designs, holding the instructional video, question
set and grading model fixed: an unrestricted chatbot that gives the final
answer on request, a [[staged-socratic-hint-policy|Socratic]]-constrained chatbot that never gives the final
answer and instead asks one guiding question at a time with a hint, and a
non-conversational system that redirects to simpler sub-questions and
reformulates them in real time when a participant's EEG-derived engagement
drops. Mode 1 gives the answer on request; the Socratic mode never gives the
final answer and instead asks guiding questions and provides hints to nudge
the student in the right direction.[^c1]

On an immediate post-test taken right after the assisted session, the
unrestricted chatbot produced higher learning gains than both constrained
modes ($p<.03$, $d>0.80$), while the adaptive condition generated
significantly higher EEG engagement ($p=.018$) without matching the
unrestricted mode's test gain.[^c2]

A behavioural cluster analysis of chatbot transcripts separated *why*:
participants in the unrestricted mode adopted a direct answer-retrieval
strategy, while participants in the Socratic mode initially attempted to
reason through the hints before progressively disengaging.[^c3]

The authors' own reading is that this also suggests that the success of the
unrestricted AI is not an evidence of deeper learning, but rather a result of
the immediate post-test evaluation after the training phase.[^c4]

## Why it matters

This is a controlled point estimate against a claim this wiki otherwise
treats as near-default: that an answerer who withholds the answer and
asks instead — [[socratic-method|Socratic]], [[non-advisory-dialogue]],
[[gated-socratic-scaffolding]] — improves the asker's outcome. Here,
withholding cost the measured outcome (an immediate factual test) even
though it raised engagement; the paper's own account is that withholding
only pays off if the respondent keeps reasoning through it, and the Socratic
arm mostly stopped doing so partway through.

## Limits

- 17/17/16 participants per arm; the paper itself calls the design
  exploratory, powered only for moderate-to-large effects ($d \geq 0.70$).[^c5]
- One outcome window (a post-test immediately after the session); no
  delayed-retention measure exists to check the authors' own "not deeper
  learning" reading against actual retention.
- Answers on the pre/post tests were graded by the same model family
  (GPT-5.2) that also role-played the two chatbot conditions; the paper
  itself flags but does not rule out favourable grading of GPT-phrased
  answers.
- `deffarges-2026` is an unreviewed arXiv preprint (harvested 2026-09-17,
  not yet verifier-confirmed) — `[?]` pending verification.

## Related

[[socratic-method]] · [[non-advisory-dialogue]] · [[gated-socratic-scaffolding]] · [[value-of-information]]

[[metacognitive-laziness]] · [[process-outcome-dissociation]] — a vocational deployment where answer-retrieval chat patterns and flat exam scores appeared together; it had no controlled arm, so it cannot be set against this study's immediate post-test result.

[^c1]: deffarges-2026 — "If the student asks for the final answer, the AI gives it directly."
[^c2]: deffarges-2026 — "The unrestricted chatbot produced higher learning gains (delta) than both constrained modes (𝑝 < .03, 𝑑 > 0.80), while the adaptive condition generated significantly higher EEG engagement (𝑝 = .018)."
[^c3]: deffarges-2026 — "most participants in the unrestricted-mode adopted a direct answer-retrieval strategy, while participants in the Socratic-mode initially attempted to reason through the hints before progressively disengaging."
[^c4]: deffarges-2026 — "this also suggests that the success of the unrestricted AI is not an evidence of deeper learning, but rather a result of the immediate post-test evaluation after the training phase."
[^c5]: deffarges-2026 — "With 50 participants across three conditions, the study is exploratory in nature and detected moderate-to-large effects (Cohen’s 𝑑 ≥ 0.70)."
