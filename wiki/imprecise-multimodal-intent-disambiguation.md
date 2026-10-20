---
description: "An LLM fuses casual, imprecise voice, gaze and pointing cues into ranked candidate instructions and asks the user to pick one, instead of asking a clarifying question."
aliases: ["IntenBot"]
sources: ["liu-2026-intenbot"]
---
# Imprecise multimodal intent disambiguation

> Instead of asking the user a follow-up question when a command is
> incomplete, the system lets an LLM read voice together with whatever
> non-verbal cues happened to accompany it, generate several candidate
> readings, and hand the choice back to the user as a selection, not a
> question.

## Definition / Mechanism

Liu et al. (2026)'s IntenBot takes voice, gaze and
finger-pointing as parallel, optional input channels, any subset of which
can be missing, noisy, or contradictory: "The disambiguation capability of
large language models (LLMs) is used to filter out irrelevant input
modalities and imprecise input data, generating potential instructions for
user confirmation."[^c1]

Rather than emitting one best guess or asking a clarifying question, the
system generates a ranked list and defers the final constraint to a
selection: "the LLM interprets the user's command and infers their
intention by generating 9 potential instructions, ranked from most to
least likely. 3 of them are shown on the headset at the same time... The
user selects the correct instruction to confirm... If none are correct,
the user can revise or retry."[^c2]

To resolve conflicts between channels when fusing them, a fixed rule
breaks ties: "a modality priority policy is included: voice commands have
the highest priority, while gaze and finger-pointing are treated equally."[^c3]

## Why it matters

This replaces stall 2's question — which axis to constrain next — with a
selection over several already-generated hypotheses for the same axis
(the target object/action), collapsing the axis-selection and
answer-collection steps the wiki's other selection criteria treat as
separate ([[mutual-information]]-style scoring, threshold gates). It is
also an answer to stall 4 (where the constraint comes from): non-verbal,
imprecise, and possibly redundant or empty channels are treated as
candidate evidence to be filtered, not as inputs requiring a predefined
protocol.

In a 12-participant behavior study comparing voice-only, explicit
multimodal, and implicit multimodal conditions, the implicit condition cut
command length without adding time: "a significant main effect (F2,22 =
9.31, p < 0.01) was observed for the number of words per command. The
post-hoc pairwise tests revealed that the number of words in (I) was
significantly lower than in (V) and (E)," with "no significant main effect
(F1.36,14.96 = 0.31, p = 0.65)... across the methods for time." Overall
selection accuracy across all three methods was "95.42% after correction
(originally 73.62%)."[^c4]

## Limits

The 95.42% figure is corrected for participants' pronunciation
transcription errors after the fact, not raw system accuracy; the paper
reports the uncorrected rate (73.62%) separately, and the LLM's own
disambiguation failure rate is not zero: "LLM interpretation errors
(5.4%), caused by failure to disambiguate the target(s) and generate the
correct instruction in the 9 potential instructions."[^c5]

The study is a 12-participant, simulated-VR home scene with a GPT-4o
backend and a fixed ranked-list size (9 candidates, 3 shown); the
modality-priority policy (voice over gaze/pointing) is an unablated design
choice, not a result the paper isolates.

## Related

[[target-confirmation-workflow]] · [[clarification-request]] · [[value-of-information]] · [[robot-response-mode-taxonomy]]

[^c1]: liu-2026-intenbot — "The disambiguation capability of large language models (LLMs) is used to filter out irrelevant input modalities and imprecise input data, generating potential instructions for user confirmation."
[^c2]: liu-2026-intenbot
[^c3]: liu-2026-intenbot — "a modality priority policy is included: voice commands have the highest priority, while gaze and finger-pointing are treated equally."
[^c4]: liu-2026-intenbot — "a significant main effect (F2,22 = 9.31, p < 0.01) was observed for the number of words per command. The post-hoc pairwise tests revealed that the number of words in (I) was significantly lower than in (V) and (E)"
[^c5]: liu-2026-intenbot
