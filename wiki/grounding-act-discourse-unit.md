---
description: "Conversational content is grounded per discourse unit: utterances are typed as initiate, continue, ack, repair, request-repair, request-ack or cancel, and the unit's state says what is still owed."
aliases: ["discourse unit grounding", "grounding acts", "conversational grounding protocol"]
sources: ["traum-1994"]
---
# Grounding acts and the discourse unit

Traum replaces Clark and Schaefer's contribution (presentation plus acceptance) with the discourse unit (DU), the level at which content is grounded, built from single-utterance grounding acts. The reason is processing: from an utterance alone one cannot tell whether a presentation is finished. "I: Move the boxcar to Corning / I: and load it with oranges / R: ok" is one contribution, while the same opening followed by "R: ok" and then "and load it with oranges" is two, so the state of the unit is only known once the next act arrives.[^c1]

## The acts

The opening utterance is an initiate; further material is a continue; any claim of understanding is an ack, whatever else the utterance does. An ack may repeat or paraphrase, signal comprehension ("ok", "uh huh"), or be implicit, as when an answer to a question proceeds with the next unit.[^c2] A repair changes the content of the current unit, a request-repair (like a next-turn repair initiator, often distinguishable only by intonation) hands the other party a discourse obligation to repair, refuse or postpone, and a request-ack does the same for acknowledgement. A cancel abandons the unit as ungrounded; the underlying intention, if still held, must be expressed in a new unit.[^c3]

## What the structure gives

The unit is tracked by a small finite-state machine built from common sequences in the TRAINS corpus. A repair by the responder must itself be acknowledged by the initiator, which first suggested a recursive network, then simplified to finite-state.[^c4] A unit is grounded when it reaches the final state, so a sender knows what is still needed (an ack, an answer to a repair request) and a listener knows which next acts are probable. Several units can be open at once, each with its own state. Repairs here concern only the grounding of content; modifying already grounded content is a separate, domain-level act.[^c5] The preference ordering of Schegloff et al. that the work reviews (self-initiated self-repair first, other-repair last) frames when repair is expected.

## Limits

- The model is descriptive: "It is still mainly a descriptive model; it says nothing" about when a repair should be uttered, except after a request-repair.[^c6]
- It was fitted to task-oriented TRAINS dialogue; coverage of other settings is not established here.
- Some sequences (repairs inside repairs, multiple acknowledgements) are problem cases handled by proposed fixes, not settled; whether the repair sub-unit or the whole unit is grounded was left open.
- My inference, not the work's: for a questioner, an unanswered clarification request is an open obligation on the other party, and an answer is itself implicit evidence of understanding. This is unmeasured here.

## Related

- [[grounding-entropy-clarification-gate]] — decides when to ask a clarification; this note describes what a clarification request creates in the exchange
- [[execution-grounded-gap-clarification]] — clarification triggered by detected gaps, which in this vocabulary is a request-repair
- [[self-supervised-clarification-question-generation]] — generating clarifying questions, the request-repair act
- [[proactive-voice-agent-over-triggering]] — unsolicited initiation by an agent opens units the user must acknowledge

[^c1]: traum-1994 — "Unfortunately, there is no way to recognize whether a presentation is complete, just by"
[^c2]: traum-1994 — "or an implicit signaling of understanding, such as by proceeding with the initiation of a new DU"
[^c3]: traum-1994 — "Closes o the current DU as ungrounded."
[^c4]: traum-1994 — "must be acknowledged by the initiator in order to be grounded"
[^c5]: traum-1994 — "Repairs are concerned merely"
[^c6]: traum-1994 — "It is still mainly a descriptive model; it says nothing"
