---
description: "A 541-instance benchmark scoring agents on five dimensions of handling genuinely unresolvable personal-memory conflict, finding conflict recognition far outpaces calibrated action or clarification."
aliases: ["TANGLE", "Testing Agents' Navigation of Genuine", "Latent", "and Entangled Memory Conflicts"]
sources: ["yang-2026-when"]
---
# TANGLE benchmark

> A memory-conflict benchmark built so that no response is uniquely
> correct, so it can score whether an agent recognises that its memory
> underdetermines the answer and asks, rather than rewarding it for
> reconstructing one value from conflicting evidence.

## Definition / Mechanism

Yang, Xu & Li (2026) introduce TANGLE: "541 instances
that span 40 diverse personas and three conflict types: Context-Partitioned
Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction
Conflict (SCC)." Two tracks separate memory construction from reasoning — an
oracle track that hands the model curated memory directly, and a pipeline
track where a memory system (Letta, Mem0, A-mem, MemOS) extracts memory from
multi-session dialogue first — "to assess five cognitive dimensions required
for conflict handling: conflict perception, causal reasoning, confidence
[[calibration]], clarification seeking, and memory faithfulness."[^c1]

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-memory (Yang et al. 2026) | TANGLE | exact — the acronym |
| agent-memory (Yang et al. 2026) | Testing Agents' Navigation of Genuine, Latent, and Entangled Memory Conflicts | exact — the expansion |

## Why it matters

Across five response models scored on complete oracle memory, "conflict
perception, diagnosis, and memory faithfulness are stronger than confidence
calibration and clarification seeking, with D4 [clarification] the
lowest-scoring dimension for every response model" — the paper calls this
the recognition-to-action gap: describing a tension is not the same
capability as asking the question that would resolve it or picking a
calibrated, reversible action.[^c2]

The pipeline track locates a second, upstream bottleneck: memory extractors
differ sharply in how much conflict-bearing structure they preserve before
an agent ever gets to reason about it — "Letta preserves the complete
target conflict in 91.7% of cases, compared with 69.1% for Mem0, 47.0% for
A-mem, and 46.2% for MemOS. The resulting information loss ranges from 8.3%
to 53.8%." A non-full bank can still answer the surface query while
discarding exactly the context, temporal or source relation that made the
conflict genuine — so an agent can fail to ask not because it lacks the
disposition but because extraction already erased the evidence that would
have prompted it.[^c3]

## Limits

- One paper, five response models (Claude Sonnet 5, Gemini 3.1 Pro,
  DeepSeek-V3.2, GLM-4.7, GPT-4o) and four third-party memory systems; the
  recognition-to-action gap is not yet replicated outside this benchmark,
  so `replicated: null`.
- Dimension scores (D1–D5) come from two LLM judges (GPT-5.4, Claude Opus
  4.7) rather than from a ground-truth action label; the paper reports
  human-judge agreement on a 556-record subset (85.8% within one point) but
  the main results are LLM-judged.
- Conflicts are "genuinely unresolvable by design" — constructed so that no
  single value is correct — which isolates the clarification decision
  cleanly but does not show how the same models behave on the far more
  common case of conflicts that *are* resolvable from context already in
  memory.
- The pipeline-track comparison confounds two failure sources (extraction
  loss and reasoning failure) only in the sense that the paper's own D3–D5
  scoring is computed over whatever the extractor returned, not over a
  controlled degradation of a fixed oracle bank.

## Related

[[memory-clarification-boundary]] · [[clarification-benchmarks]] · [[conflict-aware-action-policy]] · [[query-clarification-rate]]

[^c1]: yang-2026-when — "541 instances that span 40 diverse personas and three conflict types: Context-Partitioned Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction Conflict (SCC)"
[^c2]: yang-2026-when — "conflict perception, diagnosis, and memory faithfulness are stronger than confidence calibration and clarification seeking, with D4 the lowest-scoring dimension for every response model"
[^c3]: yang-2026-when — "Letta preserves the complete target conflict in 91.7% of cases, compared with 69.1% for Mem0, 47.0% for A-mem, and 46.2% for MemOS"
