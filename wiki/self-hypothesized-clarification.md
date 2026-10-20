---
description: "A runtime RE pipeline resolves a detected user-story defect by having the agent itself generate and rank candidate answers, never asking the user, and defers correctness to observed behaviour."
aliases: ["self-hypothesized clarification", "User Story Clarification", "autonomous clarification hypothesis generation"]
sources: ["fahim-2026"]
---
# Self-hypothesized clarification

> When a user story is flagged as underspecified, ReqEvolve's Clarification
> component does not ask the user which axis to fill in: it generates the
> question, guesses the answer, ranks its own guesses, and lets the user's
> later observation of the running feature stand in for the missing answer.

## Definition / Mechanism

In Fahim & Ferrari's (2026) ReqEvolve pipeline, a rule-based
AQUSA quality check first detects which fields of a user story ("As a
[role], I want [means], so that [ends]") are missing or vague — the
detected defect set $D$. Only the axes actually flagged in $D$ are passed
to the Clarification agent, so the axis selection is not scored by an
information-theoretic criterion but handed off wholesale to the upstream
defect detector.[^c1]

For each flagged axis, the agent — "rather than querying the user" —
autonomously generates clarification hypotheses: a question and one or more
candidate answers, using the user story, the defect set and retrieved
codebase context. Hypotheses fall into four categories tied to the story's
structure — Stakeholder (role), Scope (means), Outcome (ends/edge cases)
— plus a fourth, Example, that supplies a usage scenario with no
corresponding structural slot.[^c2]

Candidate answers are ranked by the same agent "according to contextual
plausibility"; only the top-ranked answer per axis is kept and used to
complete the story before it is handed to the rest of the pipeline. The
paper states explicitly that this ranking step is heuristic and, in its own
design, not load-bearing: "it is not critical, as users can refine the
functionality generated based on the hypotheses after observing its
behaviour."[^c3]

## Why it matters

This is a distinct answer to "where does the source come from" (stall 4):
neither the user nor an external corpus, but the asking agent itself,
immediately and without the round trip a clarification question normally
buys. Its own stated justification is that a runtime capability is a
cheaper artifact for a user to react to than a written question — "it is
easier for users to give feedback on a prototypical implementation, rather
than through questions." Whether that answer is correct is deferred
entirely to the observed behaviour of the generated feature, not checked at
generation time.[^c4]

## Transfer

| | |
|---|---|
| In its home field | a rule-based structural defect detector (AQUSA) fixes which slots of a user story need filling; an LLM agent fills each slot by guessing and self-ranking, with no user turn before code is generated |
| Here | the source-of-constraint choice on stall 4 (ask the user vs. search the world, per [[uncertainty-decomposition]] and [[clarification-action-generation]]) gains a third branch: answer the question yourself and let a later, cheaper signal (observed behaviour) stand in for verification |
| What survives | the idea that a syntactic completeness check, not an information-theoretic score, can select which axis needs a question at all |
| What does not | any guarantee that the self-generated answer is correct — the paper reports only that downstream Pass@1 is higher with the mechanism than without it (ablation), not that any individual hypothesis was right; nothing here bounds how wrong a confidently top-ranked wrong guess can be before the deferred-observation check catches it |

## Limits

- Single-system, single-paper report (fahim-2026, arXiv preprint, ASE '26);
  no independent replication of the mechanism itself is cited here.
- The claim that self-hypothesizing beats asking is not isolated from the
  rest of the RE pipeline: the ablation the paper reports (89.2% vs. 56.6%
  Pass@1) removes the whole automatic-RE stage — defect detection,
  clarification and decomposition together — not clarification alone, so
  this note's mechanism cannot be credited with a specific share of that
  number (see [[automatic-re-ablation-effect]]).
- The ranking heuristic is admitted by the authors themselves to be
  unvalidated; no accuracy figure for "was the top-ranked hypothesis the
  one the user actually meant" is reported.

## Related

[[uncertainty-decomposition]] · [[clarification-action-generation]] · [[clarification-request]] · [[automatic-re-ablation-effect]]

[^c1]: fahim-2026
[^c2]: fahim-2026 — "Rather than querying the user, the agent autonomously hypothesises plausible clarification answers, enabling generation without user interaction."
[^c3]: fahim-2026 — "Answers are ranked by the agent according to contextual plausibility. Although this ranking is heuristic, it is not critical, as users can refine the functionality generated based on the hypotheses after observing its behaviour."
[^c4]: fahim-2026 — "The assumption is that it is easier for users to give feedback on a prototypical implementation, rather than through questions."
