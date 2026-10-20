---
description: "A three-step protocol that pauses an adaptive dialog agent before it silently picks the next topic, surfaces the observation, and hands the axis-selection decision to the user."
aliases: ["collaborative reflection moment", "three-step protocol"]
sources: ["tarvirdians-2026"]
---
# Collaborative reflection pause

> Where an adaptive dialog policy would otherwise pick the next axis
> silently, stop, show the observation that would have driven the pick,
> and ask the user to interpret it and choose instead — without ever
> revealing the system's own default.

## Definition / Mechanism

Tarvirdians, Hung & Oertel (2026) modify a reflection
support agent (ReflectiMate) that otherwise redirects a conversation
toward the topic category with the lowest coverage score whenever a
"Simple Asymmetry: one category has substantially higher coverage than the
others" or a "Cross-category Mismatch: despite prompting reflection within
one category, the user's" responses keep landing elsewhere is detected.
At each such point the agent pauses instead of acting and runs a
three-step exchange with the user.[^c1]

Step 1, Recognition, asks whether the user recognizes the pattern the
agent observed. Step 2, Interpretation — "Step 2 — Interpretation. 'Do you
have a feeling for why that could be?' Participants provided" an open-text
explanation. Step 3, Decision, asks what the user wants to explore next,
offered as descriptive options (not the system's category labels) in
randomized order.[^c2]

"Importantly, the agent never revealed its own default" interpretation or
preferred direction at any step, so the user's choice could not be
anchored on the system's own read of the pattern.[^c3]

Applied across 232 such moments, the pause changed the conversational
direction away from the agent's silent default in more than half of cases
("Users selected the same action as the agent's default in 105 of 232
moments (45.3%)"), and disagreement was mostly exploratory rather than
avoidant: "did not mean users stayed with what they had already explored.
Among the 127 misaligned moments, 45.7% moved toward an underexplored
dimension (albeit not the one selected by the agent),".[^c4]

## Why it matters

This is a concrete template for converting a stall-2 selection step a
system would otherwise take unilaterally — pick the next axis from a
coverage heuristic — into an explicit question directed at the party who
holds the missing information (why the pattern exists), while withholding
the system's own candidate answer so it cannot bias the response.

## Limits

Tested as a layer on one agent and one heuristic (coverage
Bk + Dk over topic categories in a reflection-support setting); the
three-question wording was refined by pilot cognitive interviewing with
five participants but not compared against shorter or differently phrased
alternatives, and the paper reports no measurement of the added
interaction cost (turns, time) against the silent baseline it replaces.

## Related
[[interpretive-gap]] · [[clarification-request]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: tarvirdians-2026 — "Simple Asymmetry: one category has substantially higher coverage than the others."
[^c2]: tarvirdians-2026 — "Step 2 — Interpretation. “Do you have a feeling for why that could be?” Participants provided"
[^c3]: tarvirdians-2026 — "Importantly, the agent never revealed its own default"
[^c4]: tarvirdians-2026
