---
description: "An AI mediator monitors group chat for a semantic or pragmatic boundary signal, pauses the discussion, privately elicits each affected member, then returns one anonymized synthesis."
aliases: ["boundary-triggered elicitation", "Spritz mediation mechanism"]
sources: ["cheng-2026-exploring"]
---
# Boundary-triggered elicitation

> Instead of scoring every candidate question by [[expected-information-gain|expected information gain]] at every turn, this mechanism asks nothing until it detects a specific signal — a semantic or pragmatic boundary between team members — and only then opens a private, individual round of questions before synthesizing the answers back.

## Definition / Mechanism

The protocol has three stages, run by an AI agent embedded in a group
text channel (implemented as `Spritz`, a Discord bot). **DG1 — detect**:
the agent monitors the shared channel for signals that collaborators
attach different meanings to the same concept (a semantic boundary) or
hold conflicting goals despite shared understanding of the issue (a
pragmatic boundary); on detection it pauses the group discussion with a
short public notice. **DG2 — elicit privately**: it opens one-to-one
direct-message channels with the relevant members; for a semantic
boundary it asks each to clarify how they interpreted the topic, for a
pragmatic boundary it asks each to explain the motivations behind their
position and which concerns they consider hard to compromise. **DG3 —
synthesize**: after the private exchanges close, the agent posts one
anonymized summary back to the group — multiple interpretations for a
semantic boundary, or stakeholder perspectives with a tentative,
explicitly-labelled compromise direction for a pragmatic one.[^c1]

"During team discussions, Spritz monitored recent messages to identify
signals of potential semantic or pragmatic boundaries (DG1). When such
situations were detected, Spritz temporarily paused the group discussion
by sending a short public message... The agent then initiated private
conversations with relevant participants (DG2)... After the private
conversations concluded, Spritz generated an anonymized summary and
shared it with the group (DG3)."[^c2]

## Why it matters

This is a trigger-based rule for *when* to open a question round and
*to whom*, decided not by a [[value-of-information]] score but by a
detected structural signal (divergent term use or divergent goals) —
an alternative selection criterion to [[entropy]]-drop or EIG-style scoring
elsewhere on this stall: ask only the members implicated by the
detected boundary, and ask them privately before any synthesis is
shared. In a technology-probe study with 12 participants across three
role-played interdisciplinary teams (technical/business/UX), members
reported that the private DM round helped them "surface implicit
reasoning and clarify their own positions before returning to group
discussion," and that the anonymized synthesis helped them "compare,
reinterpret, and take up positions across disciplinary boundaries."[^c3]

## Limits

The claim rests entirely on one qualitative technology-probe study: 12
participants, three-person role-played teams, a single scripted
resource-allocation task, one session per team, evaluated by
co-design-workshop self-report rather than by any outcome measure (task
quality, time, or a control condition without the mediator). The
detection step (DG1) is not specified as a mechanism in the extract read
here — the paper does not give the classifier or prompt that turns a
"signal" into a trigger, only that the agent "monitors" for one — so the
selection criterion itself is not yet reproducible from this claim.
Participants themselves contested *when* the agent intervened: the
study's own summary records "intervention timing remained contested" as
an open finding, meaning the trigger threshold this mechanism depends on
is not validated by the same study that reports the mechanism useful.[^c4]

## Related

[[value-of-information]] · [[expected-information-gain]] · [[five-whys]] · [[constraint-seeking]]

[^c1]: cheng-2026-exploring — "DG1. Detecting Potential Collaboration Tensions. Rather than waiting for conflicts to become explicit, Spritz monitors team conversations for signals of potential semantic and pragmatic boundaries."
[^c2]: cheng-2026-exploring — "During team discussions, Spritz monitored recent messages to identify signals of potential semantic or pragmatic boundaries (DG1). When such situations were detected, Spritz temporarily paused the group discussion by sending a short public message indicating that it wanted to talk with several members individually. The agent then initiated private conversations with relevant participants (DG2)."
[^c3]: cheng-2026-exploring — "Experienced as helping members surface implicit reasoning and clarify their own positions before returning to group discussion"
[^c4]: cheng-2026-exploring — "Experienced as useful for reorganizing fragmented threads, but intervention timing remained contested"
