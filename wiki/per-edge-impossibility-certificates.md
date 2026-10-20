---
description: "A causal-discovery protocol that certifies each edge as data-identified or names the exact oracle question needed, and proves 1+K queries suffice for any DAG (K = non-leaf vertices)."
aliases: ["impossibility certificate protocol", "tier-aware oracle queries", "1+K bound", "meta-hub query", "node-children query"]
sources: ["uehara-2026"]
---
# Per-edge impossibility certificates

> For each edge of a data-only causal skeleton, decide whether its direction
> is identified by the data or must be asked of a domain expert — and, in the
> latter case, name the exact question. Two oracle primitives then bound the
> total number of questions any DAG can require to $1+K$.

## Problem

Causal-discovery algorithms that force a fully oriented DAG (NOTEARS, DAGMA,
PC/GES with default orientation rules) give every edge a direction, but under
Markov and faithfulness the observational distribution identifies only a
Markov equivalence class — edges off a v-structure are not determined by the
joint distribution, and more samples cannot recover them; only a functional
restriction or an intervention can. Existing outputs do not say, per edge,
which case it is.

## Mechanism

**Stage 1–2 (data only).** Skeleton by FDR-controlled HSIC; each surviving
pair is passed through an eight-tier identifiability cascade (linear/nonlinear
ANM, location-scale noise, IGCI, Stein-score, MDL, HOC-LiNGAM, and a new
[[entropy]]-inversion test), each tier gated by its own precondition test. A tier
whose precondition fails abstains rather than forcing an orientation.

**The certificate.** Every edge that survives receives a discrete code: a
`resolved_*` code names the identifiability theorem that committed the
direction (or that the edge is mediated); an `impossible_*` code names the
failure mode *and the specific question a domain expert must answer* to
resolve it.[^c1]

**Stage 3 (oracle).** Only `impossible_*` edges are shown to the practitioner.
Two interaction types: a per-edge query (fwd/bwd/absent), or two primitives
that exploit hub structure — a **meta-hub query** (list the top-$K$ nodes by
out-degree, one interaction) and a **node-children query** (enumerate one
node's direct children, one interaction, committing every outgoing edge of
that node at once).

## The bound

**Theorem 1 (Uehara 2026).** Let $G$ be a DAG with vertex set
$V$ and $K$ the number of non-leaf vertices. With a perfect oracle answering
`node_children(v)` queries with $v$'s true direct children, the protocol
recovers $G$ exactly (precision = recall = 1) in $1+K$ oracle interactions:
one meta-hub query selects the $K$ targets, then one node-children query per
target enumerates its outgoing edges.[^c2]

Verified exactly on four benchmarks (asia $K$ small, sachs, child, alarm
$V=37$) under an ideal-oracle assumption, with query count growing far slower
than edge count (alarm: 46 edges committed by 27 interactions).[^c3]

## Limits

- The bound assumes a **perfect oracle**: the protocol does not assess
  confidence in answers, and an incorrect fwd/bwd/absent response produces an
  incorrect commit; the paper defers noisy or probabilistic elicitation to
  future work.[^c4]
- Restricted to continuous-variable observational data; the discrete-BN runs
  reported exercise only the oracle layer, not the cascade, as a robustness
  check.
- The skeleton phase upper-bounds recall: an edge dropped by FDR-controlled
  pruning is never seen by the cascade or the oracle stage.
- $1+K$ is a worst-case-structure ceiling reached only when the domain expert
  can enumerate a node's children on request; the paper's own Sachs Pareto
  frontier shows intermediate operating points (5 to 21 queries) when that
  assumption is relaxed.
- `uehara-2026` is a single-author 2026 arXiv preprint; no independent
  replication is recorded here.

## Related

[[generalized-binary-search]] · [[value-of-information]] · [[optimal-decision-tree]] · [[adaptive-submodularity]]

[^c1]: uehara-2026 — "a resolved_* code records the identifiability theorem under which the direction was committed, while an impossible_* code records the failure mode together with the specific question a domain expert must answer to resolve it."
[^c2]: uehara-2026 — "Theorem 1 (1+K upper bound). Let G be a DAG with vertex set V and let K be the number of non-leaf vertices. With a perfect oracle answering node_children(v) queries with v’s direct children in G, the protocol recovers G exactly (precision = 1, recall = 1) in 1 + K oracle interactions: one meta-hub query selects the K targets, then one node-children query per target enumerates its outgoing edges."
[^c3]: uehara-2026 — "Assuming a domain expert who answers each meta-hub and node-children query correctly, the protocol recovers each ground-truth DAG at precision = recall = F1 = 1.000 using exactly 1+K oracle interactions, where K is the count of non-leaf vertices."
[^c4]: uehara-2026 — "the protocol does not assess confidence in practitioner responses, so an incorrect fwd/bwd/absent answer produces an incorrect commit or drop at the affected edge."
