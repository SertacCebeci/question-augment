---
description: "ChatGPT users begin information-seeking with narrow, pre-specified queries far more often than Google users, a field-experiment finding tied to worse critical-learning outcomes."
aliases: ["reduced querying scope"]
sources: ["mittal-2026"]
---
# Conversational query narrowing

In an 8-day, between-subjects field experiment (informal learning about
nutrition; 14 ChatGPT / 21 Google completers), participants using ChatGPT
began their information-seeking with a narrow, pre-specified query — one
tailored to personal detail rather than a general overview — in 32.65% of
diary entries (32/98), versus 3.57% (5/140) for participants using Google
Search.[^c1]

The mechanism the authors give is not that users choose narrowly by
preference but that the conversational interface constrains the choice:
the chat UI's ease of resuming a prior thread and its context retention led
participants to continue an old query instead of opening a new axis of
inquiry, and even a broad opening query returned a personalized,
already-narrowed answer.[^c2]

The behavioural gap co-occurs with a measured outcome gap: on two
knowledge-test items requiring application or evaluation (the study's
proxy for higher-order, critical learning), the Google group answered
correctly far more often than the ChatGPT group (95% vs 57%, and 57% vs
21%), while an equivalent pre-test gap was absent — the groups started
from comparable baseline knowledge (Welch's t-test, p=0.261).[^c3]

## Mechanism

The study's coding contrasts the two technologies at the point selection
(stall 2) happens on the asker's side: which query — which axis of the
information space — gets asked first, and how broadly it is framed. Under
Google, "Starting (broad)" dominates (96.43% of entries); under ChatGPT the
"Starting (narrow)" code rises sharply, and this narrowing is attributed to
the conversational and personalization affordances of the interface rather
than to the topic, since both groups pursued the same daily learning
prompts.

## Limits

Single field site (Prolific participants, one topic — nutrition and meal
planning), small completer samples (14 ChatGPT, 21 Google), and the
behavioural counts are diary-entry frequencies from one coder's thematic
analysis of a subset of entries, not an experimentally manipulated
query-scope variable — the paper itself cautions the counts "should not be
interpreted as quantitative measurements" but only to "guide our attention."[^c4]
The headline learning-outcome difference (11.62 vs 12.86) did not reach
significance (p=0.069); only two of the question-level Fisher tests did.
This wiki's claim rests on taking query breadth at the first turn as a
proxy for axis exploration in the $|W|\to1$ sense, an equation the source
itself does not make explicit.

## Related

- [[expected-information-gain]]
- [[clarification-benchmarks]]
- [[value-of-information]]

[^c1]: mittal-2026 — "participants in the ChatGPT condition were more likely to begin their information-seeking with a narrow or specified query, a behavior observed in 32.65% of their entries (nC =32/98) compared to only 3.57% of entries from Google participants (nG =5/140)."
[^c2]: mittal-2026 — "certain affordances of ChatGPT, including conversational interactions and easy access to and personalization based on past interactions, can constrain what people choose to query (Shah and Bender 2022), reducing knowledge exploration."
[^c3]: mittal-2026
[^c4]: mittal-2026 — "These numbers should not be interpreted as quantitative measurements, but serve to guide our attention towards how information-seeking behaviors differed in the two conditions."
