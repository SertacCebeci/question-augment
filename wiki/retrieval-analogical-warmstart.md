---
description: "Retrieve the nearest past-solved elicitation instance and replay its start-to-accepted edit path, found by bipartite matching, to warm-start a new elicitation before any question is asked."
aliases: ["retrieval-analogical preference reasoning", "path-aware operation extraction", "PAOE"]
sources: ["arxiv-2604-21380"]
---
# Retrieval-analogical warm-start

> Do not start every elicitation from the same naive draft — start it where
> the nearest past case ended up, and only ask about what is left over.

## Definition / Mechanism

Given a new instance to elicit preferences on, Wang & Chen (2026)
retrieve the most semantically-similar past instance that has already been
taken through elicitation to its accepted state, and reuse the **edit
operations** that carried that past instance from its initial draft to its
accepted state as an analogy, applying them to the new instance's draft
before any question is put to the person. The initial draft is "still far
away from one's true preference," so the aim is "creating a better starting
point of interaction for the newly given requirement statement... that can
reach [the preferred state] quicker."[^c1]

The two states being compared (initial draft, accepted state) are each sets
of points; extracting the edit path between two such sets — which points
correspond to which, and how the corresponding ones differ — is formalized
as a **bipartite maximum-weight matching**: one state's points form vertex
set $U$, the other's form $V$, and each edge weight is the negative
Euclidean distance between the two points, solved by the Kuhn-Munkres
algorithm. The matching gives, first, which points in the two states
correspond (Points alignment) and, second, among the corresponding pairs,
which ones actually changed value (Changes identification); unmatched
points become ADD or REMOVE operations, matched-but-different points become
CHANGE operations, and ADD/REMOVE are sequenced before CHANGE so the
extracted sequence is always a valid one to replay — "we cannot change a
value before it is added." Matching by minimum total distance rather
than an arbitrary pairing matters: two point-pairings can both be valid
correspondences, but the one with smaller total edit distance is "wiser,"
i.e. it is the more parsimonious analogy.[^c4]

Because the edit path is extracted once from an already-matched pair of
past states rather than searched for per new instance, it is cheap: "for
processing requirement under 40+ past examples, it takes < 0.2 seconds on a
2.8GHz and 8GB RAM machine."[^c5]

An ablation isolating this mechanism from the interactive tuning that
follows it shows both contribute independently, and removing both is worse
than removing either alone: "while both retrieval-analogical preference
reasoning and interactive preference tuning make non-trivial contributions
... individually, their combination is the key to its success."[^c6]

## Why it matters

This is a warm-start for interactive elicitation, not a stopping rule or a
question-scoring function: it changes what the *first* question is about by
shrinking the gap between the draft and the target before interaction
starts, so a fixed downstream question policy (here a bounded tree, see
[[optimal-decision-tree]]) needs fewer rounds to close the remainder. The
mechanism generalizes past this one paper's numeric-threshold setting: any
elicitation whose intermediate and target states are representable as
comparable structured objects (point sets, slot-fillers, feature vectors)
can reuse a past accepted instance's edit path as a prior, provided a
distance over the object's parts and a way to enumerate matched-in-turn
edit operations (add/remove/change) both exist.

## Limits

Requires the new and analogous instances to be embeddable and comparable
in a shared distance space, and requires the two states to have the same
kind of parts (same-typed points here) for the bipartite matching to be
well-defined; the paper handles unequal counts only through ADD/REMOVE, not
through richer structural mismatches. The analogy is only as good as
retrieval: a poorly-matched past instance transfers a *wrong* prior, and
the paper reports no lower bound on similarity below which the analogy is
withheld — an unverified gap. The claimed efficiency (<0.2s) is reported
for a small library (40+ examples); scaling of the retrieval step itself is
not evaluated.

## Related

- [[optimal-decision-tree]] — the downstream question policy this mechanism
  warm-starts; it fixes an expected-query-minimizing order, not a starting
  point.
- [[cold-start-value-of-information]] — also addresses the "before you know
  the response distribution" problem, but by pricing queries pessimistically
  rather than by importing a resolved prior case.
- [[value-of-information]] — the per-question quantity a warm-started
  elicitation still needs once the analogy runs out.
- [[bayesian-experimental-design]] — the broader family of "choose the next
  observation" frameworks this mechanism supplies a prior for, instead of
  competing with.

[^c1]: arxiv-2604-21380 — "creating a better starting point of interaction for the newly given requirement statement"
[^c4]: arxiv-2604-21380 — "Clearly, the former is wiser with smaller magnitudes of changes on the quantification function."
[^c5]: arxiv-2604-21380 — "for processing requirement under 40+ past examples, it takes < 0.2 seconds on a 2.8GHz and 8GB RAM machine"
[^c6]: arxiv-2604-21380
