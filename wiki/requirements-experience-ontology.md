---
description: "A three-level aspect/dimension/slot tree, induced automatically from domain requirement texts under a merge-over-add policy, fixes in advance what an elicitation interview may ask."
aliases: ["experience ontology"]
sources: ["jin-2026-chat"]
---
# Requirements experience ontology

> A pre-declared, automatically-induced tree of what an elicitation
> interview is allowed to ask about, built before the dialogue starts so
> the axis set is fixed rather than invented turn by turn.

## Definition / Mechanism

The ontology is a three-level tree T = (A, D, S, π_D, π_S): the **aspect**
layer is the top-level partition of the requirement space (e.g. for web
applications: interaction, content, style) and is fixed by domain experts
to keep the top level stable; the **dimension** layer (e.g. login, search,
display) and **slot** layer (e.g. filtering options, sorting rules) are
induced automatically from a corpus of domain-specific requirement texts
by prompting an LLM per text to either merge a new item into an existing
node, expand an existing node, or add a genuinely new one — in that
preference order ("merge > expand > add"), so the tree grows conservatively
instead of fragmenting into near-duplicate nodes. Each slot is a pair
⟨k, q⟩ of a normalized requirement key and a candidate clarification
question, phrased as a binary confirmation ("Do you need …?") when the
source text only mentions the topic, or as an open refinement ("What …?")
when it already gives partial detail.[^c1]

## Why it matters

This is a concrete, automated answer to stall 1 (the dimensions of $W$):
rather than an analyst hand-listing axes, or a model inferring them ad hoc
from the live dialogue, the axis set is mined once, offline, from a corpus
of past requirement texts in the same domain, and then held fixed as the
menu a downstream selection policy (see
[[ontology-guided-elicitation-agent]]) scores and traverses. The
merge-over-add rule is a concrete anti-fragmentation policy for automated
axis discovery: an axis is added only when the corpus offers no existing
node it can be folded into.

## Limits

The top aspect layer is not induced — it is supplied by domain experts —
so the method only automates axis discovery below a human-fixed top
partition; it does not establish where that partition itself should come
from. The merge/expand/add decision is made by a single LLM call per text
with a "carefully designed prompt," and the paper reports no measurement
of how often merge decisions are wrong (false-merging two genuinely
distinct requirement dimensions) versus how often expansion fragments one
dimension into near-duplicates; only a downstream sensitivity check on the
size of the induction corpus is reported, not a directly audited
merge/split error rate. [?] no independent replication found.[^c2]

## Related

[[ontology-guided-elicitation-agent]] · Axes

[^c1]: jin-2026-chat
[^c2]: jin-2026-chat
