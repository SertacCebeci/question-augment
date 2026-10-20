---
description: "Keeping what the agent knows in a separate graph from the report outline lets graph topology (communities, structural holes) expose missing relations, and those become targeted queries."
aliases: ["dual-graph memory", "KG-driven gap discovery", "outline graph and knowledge graph separation"]
sources: ["arxiv-2602-13830"]
---
# Topology-driven knowledge-gap detection

Open-ended research agents usually keep one memory, the outline, and ask the
language model to guess from section headers what is still unknown. The
DualGraph design separates the two roles: an Outline Graph (OG) records how
the report is written, and a Knowledge Graph (KG) stores fine-grained
knowledge units, "core entities, concepts, and their relations."[^c1] The
motivation is that an outline used as a proxy for the agent's state gives
"weak supervision for identifying missing relations and triggering targeted
exploration."[^c2]

## Mechanism

The KG is analysed as a graph, not queried as a store. For relations not yet
in the graph but likely needed, the agent builds exploratory chains from
several graph-internal signals: semantic similarity between entity and
concept nodes, community-level gap statistics from a stochastic block model
(prior probability and uncertainty of cross-community links), and
structural-hole cues that mark connections between topic islands.[^c3] The
OG supplies structural context so that the gaps found are prioritised by
where they sit in the report. Together they form a joint exploration
controller whose output is a set of targeted search queries; new evidence then
reshapes both graphs on each round.[^c4]

Two kinds of chain are distinguished: enrich chains strengthen relations that
exist but are under-evidenced, and explore chains bridge gaps between topic
islands.

## What was measured

On DeepResearch Bench the paper ablates components with self-termination
disabled. Removing enrich or explore chains degrades results; tracking only
entity-relation gaps also underperforms, which the authors read as showing
that "topological signals beyond raw entity-relation gaps (community
structure, SBM," are needed; a retrieval-oriented KG (LightRAG) does worse,
which they attribute to overly fine-grained triplets.[^c5] The outline-only
variant terminates later (average 3.88 iterations against 3.23), with 41%
of its runs needing the fifth iteration.[^c6] In pairwise LLM-judge
comparisons the KG-enhanced outlines win more often as iterations go on,
from 53.3% at iteration 1 to 76.2% at iteration 5.[^c7]

## Limits

- Evidence is benchmark scores and LLM-as-judge win rates on report writing;
  there is no human study of whether the gaps found are the gaps that matter.
- The authors name extra computation and token cost for building and
  maintaining the KG (extra LLM calls for extraction, refinement,
  consolidation).
- Which topological signal carries the gain is only partly separated:
  the ablation drops whole signal families, not each one singly.
- The explanations (fine-grained triplets are unsuited to gap detection) are
  the authors' reading, not tested directly.
- Whether the idea transfers from report-writing to answering a single
  question is my inference; it was not tested.

## Related

- [[reasoning-gap-driven-retrieval]] — also turns unmet evidential needs into follow-up queries, but from a per-type checklist rather than graph topology
- [[unbudgetable-completeness]] — completeness of a report is what gap detection tries to approach
- [[value-of-information]] — a scored alternative for choosing what to look up next

[^c1]: arxiv-2602-13830 — "a Knowledge Graph (KG), a semantic memory"
[^c2]: arxiv-2602-13830 — "exploration. We present DualGraph memory, an"
[^c3]: arxiv-2602-13830 — "cross-community links; (3) cross-community bridging"
[^c4]: arxiv-2602-13830 — "jointly generating targeted queries to resolve these gaps."
[^c5]: arxiv-2602-13830 — "The LightRAG variant performs significantly worse, suggesting that retrieval-oriented"
[^c6]: arxiv-2602-13830 — "DualGraph w/o KG 2% 11% 25% 21% 41%"
[^c7]: arxiv-2602-13830 — "win 53.3% of cases at Iter 1, rising to 63.0% (Iter 2) and"
