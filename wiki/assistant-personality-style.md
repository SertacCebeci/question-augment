---
description: "An LLM assistant's prompted conversational style causally changes turn count, word share and response length, but no single style wins across tasks."
aliases: ["expressed assistant personality", "conversational style manipulation"]
sources: ["abukar-2026"]
---
# Assistant personality style

> Holding the base model fixed and varying only the system prompt's expressed
> personality changes how a user talks to it — but which style serves the
> interaction best depends on the task, not on the style alone.

## Definition / Mechanism

In a within-subject study (26 participants, 78 task-phase conversations),
three system prompts on the same base model (gpt-4.1) produced an
extraverted style ("Titan"), a conscientious style ("Europa"), and a neutral
baseline ("Neptune"). The three were behaviourally distinguishable without
any personality label shown to participants: Titan produced the longest
assistant responses (146.38 words) but the lowest user word share (0.155)
and fewest turns (4.19 per interaction); Europa produced the shortest
responses (90.22 words) but the highest user word share (0.210) and most
turns (4.85); Neptune fell between both on every measure (114.86 words,
0.188, 4.31).[^c1]

The strongest inferential effect in the study was not a main effect of
style but a Task × Assistant interaction on trust and delegation
(F(2,46)=3.55, p=.037, partial η²=.134): the top-rated assistant differed by
task — Titan in the exploratory travel task, Neptune in the comparative
shopping task, Europa in the verification-sensitive health task. No style
dominated across tasks.[^c2]

This is not explained by the participant's own personality: after Holm
correction, participants' Extraversion and Conscientiousness scores did not
reliably predict their own turn count, word share, question count or
follow-up rate (the one directional trend, message length, stayed at
p=.085). The behavioural shift traces to the assistant's expressed style
and its fit to the task, not to a stable trait-to-behaviour mapping on
either side.[^c3]

## Known as

| Field | Name | Match |
|---|---|---|
| HCI / conversational search | expressed assistant personality | exact |
| Prompt engineering | conversational style manipulation / persona prompting | close — same mechanism (system-prompt conditioning), not validated as a psychological trait |

## Why it matters

For a question-asking pipeline, this is evidence that the *interaction
style* the assistant adopts — not just which questions it asks — is itself
a variable that changes how much a user elaborates, how many turns a
dialogue takes, and how much the user is willing to rely on the answer, and
that the right setting is task-conditioned rather than fixed.

## Transfer

| | |
|---|---|
| Home field | Personality psychology — the Big Five / OCEAN taxonomy (Extraversion, Conscientiousness as stable individual-difference dimensions) |
| Here | Used only as prompt labels: two system prompts instructed to emphasise Extraversion- or Conscientiousness-linked behaviours; no claim that the model has the trait |
| What survives | The trait vocabulary as a way to name and reproducibly generate distinguishable interaction styles (validated by pre-study BFI-2-S profiling of the prompt outputs) |
| What does not | Trait stability and internal causation: the "trait" is a manipulated condition, not a measured property of the assistant, and the analogous participant-side trait did not predict behaviour (^c3) |

## Limits

The claim rests on one base model (gpt-4.1), two of five Big Five
dimensions, three tasks, and a young, male-skewed, computing-oriented
convenience sample of 26 — the task-dependent ranking (Titan/Neptune/Europa
by task) is a single-study finding, not yet replicated, and several
supporting effects (the overall post-interaction composite, F(2,46)=3.17,
p=.051) fall short of the study's own significance threshold and are
reported by the authors as directional only.

## Related

[[personality-compatibility]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: abukar-2026 — "Titan produced the longest assistant responses, with a mean of 146.38 words. Europa produced the shortest responses, with a mean of 90.22 words. Neptune was intermediate at 114.86 words."
[^c2]: abukar-2026 — "the Task × Assistant interaction was significant for trust and delegation (𝐹 (2, 46) = 3.55, 𝑝 = .037, partial 𝜂 2 = .134)."
[^c3]: abukar-2026 — "The corrected inferential analyses did not show robust direct effects after Holm correction [24]."
