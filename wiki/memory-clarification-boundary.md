---
description: "A four-way taxonomy (persist / ephemeral / verify / clarify) for agent memory writes, and cross-family results showing agents verify far more than they ask."
aliases: ["MCB", "Memory Commitment Benchmark", "memory commitment boundary"]
sources: ["li-2026"]
---
# Memory-clarification boundary

> When an LLM agent meets interaction-derived information, it has to
> decide not just *whether to ask* but **what kind of commitment** a
> non-question response would make — durable storage, one-session use, a
> re-check, or referral to the user — and cross-family measurement shows
> agents default to the re-check over the referral.

## Definition / Mechanism

Li, Yao & Zheng (2026) name the point where an agent decides
"whether interaction-derived information should be persisted, used only in
the current context, re-verified, or clarified with the user" the
memory-clarification boundary, because an "incorrect durable update can
silently distort future behavior."[^c1]

They score every item against four decisions: **persist** — "explicitly
durable preferences, authorized policies, or stable facts"; **ephemeral** —
"information scoped to one artifact, session, or time window"; **verify** —
"changing world state or a single noisy signal that must be rechecked"; and
**clarify** — "unresolved referent, durability, scope, conflict, or
second-hand preference for which the user is authoritative."[^c2]

The Memory Commitment Benchmark (MCB) operationalises this taxonomy: 140
primary scenarios (70 development, 70 held-out) plus a 70-item contrast
set, each labelled by two non-author annotators (97.1% agreement, Cohen's
κ = 0.962), scored on both the stated action label and the structured
tool-call the model actually issues.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-memory (Li et al. 2026) | memory-clarification boundary | exact |
| agent-memory (Li et al. 2026) | Memory Commitment Benchmark / MCB | exact — the benchmark that operationalises the boundary |

## Why it matters

Across Claude and Qwen, models "verify changing facts more reliably than
they ask users to resolve [[efe-planning-as-variational-inference|ambiguity]]" — an under-asking pattern specific to
the memory decision, not just to query disambiguation. Claude's
verification recall ran 0.889–1.000 against a weaker clarification recall
of 0.500–0.750; bare Qwen reached 0/12 clarification recall while still
verifying 12/18 freshness-sensitive items.[^c4]

Two interventions move the numbers without closing the gap: few-shot
prompting raised accuracy from 0.557 to 0.771 (p = 0.002) but left
clarification recall at 0.333, and an explicit policy prompt cut erroneous
persistence from 0.243 to 0.100. Stated label and issued tool-call also
diverge by model family — 57% agreement for Claude, 23% for Qwen.[^c5]

This gives the "should I ask before I remember this" decision a measured
baseline distinct from query-ambiguity clarification: the same
family-level under-asking bias that [[clarification-benchmarks]] reports
for short-form QA reappears here, but the object being withheld is a
durable memory write rather than an answer.

## Limits

- One paper, three models tested (Claude and Qwen families); the
  cross-family claim rests on that set and is not yet replicated
  elsewhere, so `replicated: null`.
- The taxonomy's four categories are the authors' construction, checked by
  inter-annotator agreement on their own 210 items, not validated against
  an independent theory of what counts as durable versus ephemeral.
- "Verify" and "clarify" are scored as mutually exclusive action labels;
  the benchmark does not measure a policy that does both (verify, then ask
  only if verification fails).
- Numbers above are as reported in the paper's abstract and body; this
  note has not re-derived them from the raw benchmark data.

## Related

[[clarification-benchmarks]] · [[query-clarification-rate]] · [[clarification-request]] · [[preference-signal-against-asking]]

[^c1]: li-2026 — "whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user"
[^c2]: li-2026 — "explicitly durable preferences, authorized policies, or stable facts"
[^c3]: li-2026 — "140 primary scenarios, split into 70 development and 70 held-out items, plus a separate 70-item contrast set"
[^c4]: li-2026 — "verify changing facts more reliably than they ask users to resolve ambiguity"
[^c5]: li-2026
