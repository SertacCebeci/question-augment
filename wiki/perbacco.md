---
description: "A greedy heuristic that queries a bounded record-matching oracle batch by batch, prioritising dense record communities and deciding each step whether to enlarge a found cluster or open a new one."
aliases: ["pERbacco"]
sources: ["balzotti-2026"]
---
# pERbacco

> The practical answer to [[batched-oracle-entity-resolution]]'s hard
> selection problem: build a similarity graph, carve it into dense
> "communities" sized near the oracle's batch limit, and at each oracle call
> decide — by a running estimate of expected gain — whether to keep growing
> the cluster already found or open a fresh one.

## Definition / Mechanism

pERbacco has three steps: (1) compute a similarity graph over the record set
from any off-the-shelf similarity method; (2) partition it by recursively
running a community-detection algorithm into "heavy communities" — dense
subgraphs sized comparably to the batch limit $b$, chosen so that most match
edges fall inside one community rather than between two; (3) at each query,
adaptively decide whether to enlarge an already-visited entity or visit new
records of the current community, driven by an evolving parameter the paper
calls **temperature**, itself linked to an expected-gain measure called
**benefit**.[^c1]

The rule of thumb behind step 3: visiting brand-new records is expected to
discover fewer match edges than continuing to probe an entity already
partly found, so a low observed benefit from enlarging pushes the algorithm
to switch to new records instead.[^c2]

## Why it matters

pERbacco is the heuristic the paper runs where the exact
[[batched-oracle-entity-resolution|batch-selection]] optimum is NP-hard and
its provably-optimal special case does not apply: it substitutes a
cheap graph-partition-plus-adaptive-switch rule for solving the Heaviest
Subgraph Problem at every step. With GPT-5 mini as the oracle, batches of up
to 10 records return an F-score at or near 1 on the tested datasets, with
quality degrading at larger batch sizes on some datasets — evidence that the
"bounded, consistent oracle" assumption the theorem needs is approximately
met by an LLM oracle only up to a batch-size limit, not unconditionally.[^c3]

## Limits

- The batch-size range where an LLM oracle stays near-perfect (up to about
  10 records in the paper's test) is empirical and dataset-dependent; it is
  not derived from the paper's theory, which assumes a perfectly consistent
  oracle regardless of $b$.[^c4]
- The community-detection and temperature/benefit heuristics are not shown
  to inherit [[batched-oracle-entity-resolution]]'s $b$-optimality guarantee
  — that guarantee is proved only for the Heaviest-Subgraph-Problem greedy
  rule on $\mathrm{Gain}^b_Q$, not for pERbacco's community-based
  approximation of it.
- `balzotti-2026` is an arXiv preprint (2026-06-23), read here for its
  method description and Figure 1 only; the full experimental comparison
  against baselines (Section IV) was not read for this note.

## Related

[[batched-oracle-entity-resolution]] · [[adaptive-submodularity]] · [[generalized-binary-search]]

[^c1]: balzotti-2026 — "It consists of three steps: computing a similarity graph G on R, partitioning G by recursively calling a Community Detection Algorithm (CDA), and adaptively deciding whether to enlarge already visited entities or visit new records belonging to the same community."
[^c2]: balzotti-2026 — "The main idea is that visiting new records should discover fewer match edges (see Table I and Subsection III-C3). So, if by trying to enlarge already visited entities we discover a few edges, then in the next query we visit new records of the current community."
[^c3]: balzotti-2026 — "We observe that the F-score is equal or very close to 1 for batch sizes up to 10, while in some datasets it degrades for larger batch sizes."
[^c4]: balzotti-2026 — "We observe that the F-score is equal or very close to 1 for batch sizes up to 10, while in some datasets it degrades for larger batch sizes."
