---
description: "A browser extension triggers a delayed follow-up preference prompt only when a downstream event is topic-matched and textually overlaps an earlier LLM interaction, not on a fixed schedule."
aliases: ["BITE", "outcome-aware follow-up reflection", "context-triggered follow-up preference elicitation", "event-triggered reflection prompt"]
sources: ["gebreegziabher-2026"]
---
# Outcome-aware follow-up elicitation

> Do not re-ask a preference question on a timer; re-ask it when a
> real-world event that textually overlaps the earlier interaction is
> detected.

## Definition / Mechanism

Gebreegziabher, Sproul, Yang, Chen, Gómez-Zará & Li (2026)
build BITE, a Chrome extension that decides *when* to issue a second,
delayed preference-elicitation prompt about an earlier LLM interaction.
The first prompt fires immediately: "When the user is interacting with the
LLM, BITE prompts a locally deployed Meta Llama model... to categorize the
conversation into one of nine tracked topics established in this version.
If a conversation is classified into one of these topics, the system
triggers a reflection prompt by showing a pop-up on the user's screen."[^c1]

The follow-up prompt is gated by a second, independent signal rather than
elapsed time. BITE watches Gmail content, classifies each email into the
same nine topics, and for topic-matching candidates "computes the Jaccard
similarity between the tokenized word sets of the email text and the
earlier LLM interaction content... If the similarity score exceeds 0.5,
BITE interprets the email as a likely follow-through action related to the
earlier interaction and triggers a delayed follow-up reflection prompt."[^c2]
Deployed in the wild for two weeks with 8 participants, this pipeline
captured "182 LLM conversations with corresponding ratings."[^c3]

## Why it matters

This is a concrete instantiation of *when to re-ask* rather than *which
axis to ask next*: the trigger for a follow-up preference question is an
external, non-conversational event (an email) whose content lexically
overlaps the original interaction, not a fixed re-survey interval or a
model-internal confidence signal. It answers stall 2 for the specific case
of a second elicitation round: score readiness to re-ask by evidence that
the user has acted, not by how much time has passed.

## Transfer

| | |
|---|---|
| **In its home field** | Experience-sampling / context-aware computing: prompts fire on situational triggers (location, time-of-day) chosen for ecological validity, not tied to a specific prior artifact's content. |
| **Here** | The trigger is tied to one specific prior LLM interaction via topic match plus lexical (Jaccard) overlap with a new, independently-arriving document (an email). |
| **What survives** | Event-driven rather than interval-driven prompting to reduce burden while catching consequential moments. |
| **What does not** | Jaccard token overlap is a shallow proxy for "this event follows from that interaction" — it has no semantic-similarity or causal check, and the 0.5 threshold is fixed by the authors, not tuned or ablated. |

## Limits

- Deployment is 8 participants over two weeks (182 conversations); the
  0.5 Jaccard threshold and the nine tracked topics are proof-of-concept
  choices the authors state are not exhaustive.
- The downstream-event channel is Gmail only: "We currently support Gmail
  because these DOM selectors were implemented and validated against
  Gmail's interface; extending to other providers would require
  provider-specific DOM mapping." Coverage of non-browser (e.g. mobile)
  LLM use is explicitly noted as missed by the sensor.
- Read from the archived arXiv preprint text extract only; unverified [?]
  as of this draft.

## Related

[[value-of-information]] · [[preference-optimization-for-questions]] · [[expected-information-gain]]

[^c1]: gebreegziabher-2026
[^c2]: gebreegziabher-2026
[^c3]: gebreegziabher-2026 — "Across the two-week deployment, we captured 182 LLM conversations with corresponding ratings from eight participants using BITE."
