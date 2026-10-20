---
description: "An ensemble of simulated-user agents with varying profile access decides per design dimension whether a real question is needed, spending a fixed clarification budget only where they disagree."
aliases: ["Buddy"]
sources: ["wang-2026-turning"]
---
# Simulated-user consensus filtering

## The mechanism

Buddy (Wang, Han & Xu 2026) first drafts a spec sheet
from the user's stated intent and builds a morphological chart: independent
preference dimensions (e.g. privacy level, feature scope), each restricted
to choices already grounded in the user's own proposal. "It then uses these
elements to construct a morphological chart: a structured breakdown of
preference dimensions along which different users may make different
choices," and each dimension "presents exactly four alternatives describing
meaningfully different approaches to scope, behavior, or user experience."[^c1]

Rather than asking about every dimension, Buddy runs three simulated-user
sub-agents that share a conversation-history summary but differ in how much
of the inferred user profile they see — one gets the full profile, one has
20% of its attributes randomly removed, one gets none — plus different
system-prompt instructions to diversify their reasoning. "A design choice is
finalized only if all three simulators select the same option with high
confidence over the alternatives."[^c2]

The gate is explicitly modeled on ensembling for uncertainty: "This approach
is inspired by classical MC dropout [GG16] and serves as a conservative
filter to identify decisions that can be reliably inferred from user
preferences."[^c3]

For the dimensions the simulators do not agree on, "the user interaction
module generates candidate clarification questions, selects the question
expected to most effectively reduce uncertainty, and poses it to the user."[^c4]
Only that residual set consumes the round budget.

Measured against three CLI coding-agent baselines on SpecBench (see
[[clarification-benchmarks]]), Buddy needs fewer queries yet scores higher
on both of the benchmark's tasks: "Buddy queries the user significantly
fewer times than other agents, while still achieving the highest evaluation
scores and outperforming all baselines in head-to-head comparisons."[^c5]

## Transfer

| | |
|---|---|
| Home field | Design methodology — Zwicky's morphological analysis: decompose a problem into independent dimensions, enumerate discrete alternatives per dimension, treat the resulting cross-product as the design space. |
| Here | Only the decomposition step: intent is broken into user-facing preference dimensions with four alternatives each, bounding which axes a clarifying question could ever be about. |
| Survives | The independence assumption across dimensions and the discreteness of alternatives — both are what let the ensemble score "agreement" per dimension at all. |
| Does not | Classical morphological analysis has no consensus filter, no [[question-budgets|question budget]] and no notion of consulting an external party; the ensemble-agreement gate and the question-selection step are this paper's own addition, not part of the imported formalism. |

## Limits

- "Reliable" inference rests on three simulated users built from one
  inferred profile and one conversation summary, all produced by the same
  underlying LLM (Opus-4.6 in the reported experiments); agreement among
  them is not independent evidence the way three differently-sourced raters
  would be.
- Reported gains (fewer queries, higher accuracy) are against three specific
  CLI baselines (Claude Code, Cursor CLI, Gemini CLI) on one benchmark,
  SpecBench, with LLM-simulated users answering on the other side of the
  dialogue too; there is no test against a human user or a non-CLI
  clarification method.
- The numeric "high confidence" threshold that finalizes a decision without
  asking is not given in the extract read here.

## Related

[[clarification-benchmarks]] · [[mutual-information]] · [[value-of-information]]

[^c1]: wang-2026-turning — "It then uses these elements to construct a morphological chart: a structured breakdown of preference dimensions along which different users may make different choices."
[^c2]: wang-2026-turning — "A design choice is finalized only if all three simulators select the same option with high confidence over the alternatives."
[^c3]: wang-2026-turning — "This approach is inspired by classical MC dropout [GG16] and serves as a conservative filter to identify decisions that can be reliably inferred from user preferences."
[^c4]: wang-2026-turning — "the user interaction module generates candidate clarification questions, selects the question expected to most effectively reduce uncertainty, and poses it to the user."
[^c5]: wang-2026-turning — "Buddy queries the user significantly fewer times than other agents, while still achieving the highest evaluation scores and outperforming all baselines in head-to-head comparisons."
