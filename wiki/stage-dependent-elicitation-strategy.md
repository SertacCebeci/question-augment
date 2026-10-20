---
description: "In conversational recommendation, attribute questions elicit preferences best in early dialogue stages while item comparisons work better once preferences are concrete."
aliases: ["stage-dependent preference elicitation", "attribute-based vs item-based elicitation shift", "context-aware preference elicitation"]
sources: ["xia-2026"]
---
# Stage-dependent elicitation strategy

> Which kind of question to ask next in a conversational recommender
> depends on how far the user's preferences have already narrowed: attribute
> questions early, item comparisons late.

## Definition / Mechanism

Xia, Zhang & Wang (2026) ran a user study (328 participants,
eight scripted dialogue scenarios spanning three stages — preference
exploration, refinement, post-recommendation readjustment) comparing
attribute-based elicitation (asking about genres, authors, features) against
item-based elicitation (presenting concrete items to compare or choose
among). Neither strategy alone was rated sufficient across stages: "Regarding
attribute-based elicitation, 54% of participants reported it was effective in
most situations, whereas only 21% found it sufficient across all
situations... Item-based elicitation yielded similar results, with
corresponding proportions of 59%, 25%, and 16%, respectively."[^c1]

Tracking which strategy users preferred as the eight scenarios progressed:
"In the early stages, attribute-based elicitation dominates user choices.
However, as the dialogue progresses and preferences become more concrete,
the use of item-based elicitation increases steadily and eventually
surpasses attribute-based strategies in the later stages."[^c2]

The paper states the general form of the finding: "attribute-based
inquiries are effective in early stages, while item-based strategies become
superior as preferences refine."[^c3]

## Why it matters

This is a direct answer to "which axis first, and in what form" for one
concrete asking system: not just which attribute to ask about, but whether
to ask about an attribute at all versus asking the user to compare concrete
options — and the right choice flips partway through the interaction. Most
prior conversational-recommendation systems fix one strategy for the whole
dialogue; this finding is the empirical case against that.

## Limits

Single domain (movie/INSPIRED-style dialogues) and a coarse three-stage
partition (exploration / refinement / readjustment) defined by the
experimenters, not detected automatically from the dialogue by any measured
procedure in this study — the note does not claim a method for knowing which
stage a live conversation is in. The 328 participants rated pre-written
scenario responses rather than living through an adaptive system, so the
finding is a preference judgment, not a downstream task-success result.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[adaptive-submodularity]]

[^c1]: xia-2026 — "Regarding attribute-based elicitation, 54% of participants reported it was effective in most situations, whereas only 21% found it sufficient across all situations, and 25% considered it effective in only a few cases. Item-based elicitation yielded similar results, with corresponding proportions of 59%, 25%, and 16%, respectively."
[^c2]: xia-2026
[^c3]: xia-2026 — "attribute-based inquiries are effective in early stages, while itembased strategies become superior as preferences refine."
