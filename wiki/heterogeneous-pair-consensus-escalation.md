---
description: "A three-stage escalating stopping cascade for multi-agent debate — pairwise heterogeneous consensus, then an oscillation-counter debate cutoff, then collective voting."
aliases: ["HCP-MAD", "Heterogeneous Consensus Verification", "Heterogeneous Pair-Agent Debate", "Adaptive Stopping Criterion", "Escalated Collective Voting"]
sources: ["arxiv-2604-09679"]
---
# Heterogeneous pair-consensus escalation

> Spend tokens only on the tasks that still disagree, and stop each stage the moment it stops disagreeing.

## Definition / Mechanism

HCP-MAD (2026) routes every query through three stages, escalating only when the previous stage fails to settle.

**Stage 1 — Heterogeneous Consensus Verification (HCV).** Two agents with different backbones independently answer once, with no shared history. If their answers agree, the system stops immediately and returns the agreed answer: "The consensus between two heterogeneous agents can provide an efficient indicator of answer reliability." Formally, an indicator Φinit = 𝟙[ŷ1,0 = ŷ2,0]; "If Φinit = 1, HCP-MAD stops early and returns the agreed answer." Heterogeneity (different backbones) is load-bearing, not incidental: replacing the pair with homogeneous agents dropped accuracy from 86.30% to 82.77% on MMLU, because a same-model pair colludes into false agreement rather than genuinely cross-checking.

**Stage 2 — Heterogeneous Pair-Agent Debate (HPAD).** On disagreement, the same two agents debate over further rounds, but the debate is cut off — not by a fixed round count — by two oscillation detectors. An *answer-exchange* counter tracks consecutive rounds where the two agents swap each other's prior answers (`AB → BA → AB`): "If two agents repeatedly exchange answers with each other across consecutive rounds … more debate rounds are unnecessary." A *deadlock* counter tracks consecutive rounds where both agents hold their own prior answer while still disagreeing (`AB → AB → AB`): "If both agents keep their own answers unchanged while still disagreeing … the debate has reached a deadlock." Each counter resets to zero the moment its pattern breaks, and increments only while the pattern holds. Debate stops — to consensus or to escalation — once either counter reaches a threshold η (both set to 2 in the implementation) or a maximum round T is hit: "where ηe and ηd are the exchange and deadlock thresholds, respectively. In our implementation, both are set to 2."[^c5]

**Stage 3 — Escalated Collective Voting (ECV).** Tasks still unresolved after HPAD recruit additional agents, split into an independent subgroup reasoning from scratch and a reviewer subgroup evaluating the debate history, to aggregate a final vote: "For tasks that have not yet reached a consensus, ECV recruits additional agents to introduce broader collective intelligence and aggregate their judgments."[^c6]

**Measured effect of the cascade.** On MMLU, 80.12% of queries resolve at Stage 1 (92.16% accuracy at 980 tokens), 14.31% at Stage 2, and 5.57% escalate to Stage 3 (62.20% accuracy at 6,736 tokens) — cost is spent roughly in proportion to how unresolved a query is. Removing Stage 1's early stop raised token cost from 1,977 to 3,951 on MMLU without an accuracy gain. Removing the oscillation-counter cutoff (replacing it with running debate to the round cap) raised token cost from 1,997 to 2,753 while lowering accuracy from 86.30% to 86.02%, i.e., the cutoff is not just cheaper but more accurate than exhausting the round budget.[^c9]

## Why it matters

This is a stopping rule assembled from a chain of cheap, local sufficiency tests rather than one global one: agreement between two agents is the test at the top, one of two label-repetition patterns is the test in the middle, and only what survives both goes to the expensive test (many-agent voting) at the bottom. The oscillation counters are notable in their own right as a stopping signal that needs no confidence score, probability or external threshold on the *answer* — only on the *pattern of the answer sequence itself*.

## Limits

Both oscillation thresholds are fixed at 2 by the paper's implementation choice, not derived or swept; how they'd scale to a debate topology with more than two agents, or to answers with partial or graded (not just exact) agreement, is untested. The three stage cutoffs (80/14/6% resolution) are dataset-specific (MMLU) and the paper does not claim they transfer to other domains. Heterogeneity is treated only as different backbones; whether the same effect holds for agents heterogeneous in role, prompt, or training rather than model identity is not examined.

## Related

- [[stopping-rules]]
- [[collective-uncertainty]]
- [[double-confidence-filtering]]
- [[trajectory-equivalence-rate]]
- [[cusum]]

[^c5]: arxiv-2604-09679 — "where ηe and ηd are the exchange and deadlock thresholds, respectively. In our implementation, both are set to 2."
[^c6]: arxiv-2604-09679 — "For tasks that have not yet reached a consensus, ECV recruits additional agents to introduce broader collective intelligence and aggregate their judgments."
[^c9]: arxiv-2604-09679 — "ASC effectively decreases token usage from 2,753 to 1,997 on MMLU, while also increasing accuracy from 86.02% to 86.30%."
