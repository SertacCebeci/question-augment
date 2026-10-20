---
description: "A two-level attack that fabricates locally-reasoned adversarial documents and chains them across a document set to hijack a deep-research agent's subtask and follow-up-question generation."
aliases: ["FORGE", "Fabricated Orchestrated Reasoning chain for aGent Exploitation", "research-trajectory hijacking"]
sources: ["pan-2026"]
---
# FORGE (research-trajectory hijacking)

> A deep-research agent decomposes a query into subtasks, retrieves evidence
> per subtask, and plans the next subtask from what it just retrieved — so a
> document that ranks highly in an early retrieval pass can steer which
> question the agent asks next, not just what it writes.

## Definition / Mechanism

FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation) is a
two-level poisoning construction against the plan–retrieve–synthesize loop
of deep-research agents: "a two-level attack that combines intra-document
reasoning fabrication with inter-document chain coordination to hijack
subtask planning." At the document level, each adversarial document embeds
an internal reasoning chain that presents the target claim as a derived
conclusion rather than a bare assertion; at the set level, the documents are
organized as a distributed argument chain so the poisoned set "reads as
convergent multi-source evidence," bypassing the [[planner-dynamic-stopping|planner]]'s implicit
consensus filter.[^c1]

The escalation to report-level contamination runs through subtask
hijacking: when the planner performs its initial retrieval pass over the
document pool, "if FORGE documents rank highly in [that pass], the planner
absorbs their framing into the subtask structure," so a hijacked subtask
$\hat t$ semantically aligned with the target narrative disproportionately
retrieves more FORGE documents in the next round, and "a single hijacked
subtask can inject V-aligned content into R even when all remaining
subtasks are benign."[^c2]

Measured on 25 queries across five topic categories, the network variant
(adversarial documents competing against real retrieved content) "reaches
26.4% PRISM with five injected documents and exhibits depth migration, in
which recursive synthesis shifts poisoned content from overt framing into
factual premises," and on the ten-query defense subset it reaches 38.5%
PRISM with no defense in place.[^c3]

## Why it matters

This is a direct, measured attack on stall 2 (which axis first): the
follow-up question an agent selects is not chosen from a neutral candidate
set — it can be steered by which documents an earlier, uncontrolled
retrieval step happened to surface. Selection criteria on this stall
(greedy [[entropy]] drop, [[adaptive-submodularity|adaptive submodularity]]) assume the value estimate of
a candidate question is computed over genuine evidence; FORGE shows that
assumption is an attack surface, not a given, once the evidence used to
score candidate subtasks is itself adversarial.

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-security | FORGE | exact |
| agent-security | Fabricated Orchestrated Reasoning chain for aGent Exploitation | exact — the acronym's expansion |
| agent-security | research-trajectory hijacking | exact — the paper's own name for the failure class FORGE instantiates |
[^c4]

## Limits

- Construction is human-supervised: "an operator specifies V and chain C,
  an LLM drafts each pk..., and a human reviews drafts for plausibility and
  retrieval relevance" — this is not a fully automated attack pipeline, and
  the released materials withhold the automation components.[^c5]
- Main results are on one platform (gpt-researcher); Appendix E replicates
  trends on two more, but PRISM values "are not directly portable across
  retrieval architectures."
- The network setting simulates retrieval competition without modelling
  live-web factors such as domain authority, freshness, or anti-spam
  filtering, so PRISM there is described as an upper bound.

## Related

[[root-query-anchoring]] · [[prism-poisoning-severity-metric]] · [[adaptive-submodularity]]

[^c1]: pan-2026 — "We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with inter-document chain coordination to hijack subtask planning."
[^c2]: pan-2026 — "When Ls generates the research plan, it performs an initial retrieval pass D(0) over the document pool. If FORGE documents rank highly in D(0) , the planner absorbs their framing into the subtask structure"
[^c3]: pan-2026 — "Across 25 queries, Network FORGE reaches 26.4% PRISM with five injected documents and exhibits depth migration, in which recursive synthesis shifts poisoned content from overt framing into factual premises."
[^c4]: pan-2026 — "FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation)"
[^c5]: pan-2026 — "The two construction levels are instantiated through a human-supervised LLM pipeline: an operator specifies V and chain C, an LLM drafts each pk (Appendix B), and a human reviews drafts for plausibility and retrieval relevance."
