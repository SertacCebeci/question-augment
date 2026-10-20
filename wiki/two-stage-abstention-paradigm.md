---
description: "A two-phase design that separates a model's answer-and-confidence report from a later commit-or-abstain decision, borrowed from post-decision confidence paradigms in animals."
aliases: ["post-decision confidence paradigm", "opt-out paradigm", "wait-or-leave paradigm", "two-phase abstention paradigm"]
sources: ["kumaran-2026"]
---
# Two-stage abstention paradigm

> Ask for the answer and the confidence first, without telling the model
> that a commit-or-abstain decision is coming; only then ask it to commit
> or abstain. Whatever the confidence signal was tracking has to show up
> before the second question is even asked.

## Definition / Mechanism

Kumaran (2026) runs every model through two separated
phases. Phase 1: the model selects from multiple-choice options or
generates a free-form response; a verbal-confidence rating and a
calibrated log-probability confidence are collected in the same phase.
Phase 2, on the same trial and shown its own Phase 1 answer, the model
"makes a binary commit-or-abstain decision. Commit returns the chosen
answer to a fictitious user;" abstain returns "I don't know" instead.[^c1]

Phase 1 is run without informing the model that Phase 2 is coming, so the
confidence signals it produces there are not shaped by anticipation of the
commit decision; this lets the same Phase-1 signal be scored twice — once
against Phase-1 correctness, once against the Phase-2 decision — on the
same trial.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Perceptual decision neuroscience (rodent/primate opt-out tasks, e.g. Kepecs & Mainen; Lak et al.) | post-decision confidence / opt-out ("wait-or-leave") paradigm | close |
| LLM uncertainty evaluation (Kumaran 2026) | two-stage abstention paradigm | exact |

[^c3]

## Why it matters

Gives the wiki a design for testing whether an answerer's stated
confidence and its behaviour under a commit/abstain choice are driven by
the same evidence, instead of assuming a confidence report already *is*
the commitment decision.

## Transfer

| | |
|---|---|
| In its home field | a rat or primate performs a two-alternative choice, then chooses to wait for a delayed, uncertain reward or to leave and start a new trial — opting out *is* the confidence readout, with a real time cost. |
| Here | an LLM answers and separately reports a confidence signal, then is later shown its own answer and explicitly asked to commit or abstain. |
| What survives | the two-stage separation of evidence-driven choice from a subsequent, distinct commit/withhold decision; scoring one confidence signal against two different outcomes (correctness vs. later decision) on the same trial. |
| What does not | the animal's opting-out is spontaneous, graded by waiting time and priced by a real delay cost; the model's is elicited by an explicit second prompt with no cost structure, so it reports on a decision rather than being the decision's own graded trace. |

Kumaran (2026) marks this directly: "Unlike in animal paradigms, where
opting out is itself the confidence readout, we" measure Phase 1
confidence independently and ask whether it tracks later [[abstention]] or
correctness.[^c4]

## Limits

- Tested only on multiple-choice and free-form QA with a fictitious
  downstream user standing in for real stakes; whether the dissociation
  changes when abstention has a real, named cost (as in the animal task) is
  untested here.
- The elicited, not spontaneous, Phase-2 prompt means the paradigm cannot
  by itself rule out that a differently-worded elicitation would change
  which signal looks decision-aligned.

## Related

[[abstention]] · [[sequence-likelihood-confidence]] · [[sensory-underconfidence]] · [[calibration]]

[^c1]: kumaran-2026 — "model) and makes a binary commit-or-abstain decision. Commit returns the chosen answer to a fictitious user;"
[^c2]: kumaran-2026 — "studies of post-decision confidence in rodents and primates 7,8,17,18 (Figure 1). In Phase 1, the model"
[^c3]: kumaran-2026 — "studies of post-decision confidence in rodents and primates 7,8,17,18 (Figure 1). In Phase 1, the model"
[^c4]: kumaran-2026 — "Unlike in animal paradigms, where opting out is itself the confidence readout, we"
