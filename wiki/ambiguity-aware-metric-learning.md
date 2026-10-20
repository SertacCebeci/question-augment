---
description: "A metric-learning loss pushes ambiguous queries toward the origin of a compressed feature space, so a vector-norm threshold decides when a robot must ask before retrieving."
aliases: ["ambiguity-aware feature space", "SaaF", "scene-specific ambiguity-aware feature space"]
sources: ["yano-2026"]
---
# Ambiguity-aware metric learning

> A 3D object-retrieval robot needs one number, not a classifier, to decide
> whether to ask: how far the query's compressed feature sits from the
> origin of a space it was trained to shape that way.

## Definition / Mechanism

Yano, Kanaoka, Tamukoh & Kawanishi (2026) train an autoencoder
on CLIP image/text features with a combined loss — a cosine-similarity
metric-learning term plus a reconstruction term — that pulls features of the
*same* tracked object instance together and pushes different instances
apart, while a set of VLM-generated text labels spanning "varying levels of
[[efe-planning-as-variational-inference|ambiguity]]" per object is folded into the same training signal. The
consequence is geometric: "Ambiguous features that overlap multiple
objects, such as a round bottle and a shaped bottle, are located near the
origin as a result of simultaneously satisfying both [the metric-learning
loss] and [the reconstruction loss]... From the above process, the feature
space that determines ambiguity via vector norm is obtained."[^c1]

At query time the decision is a single thresholded norm, not a learned
classifier: a user query's compressed feature $q_{comp}$ is classified
ambiguous "if $\|q_{comp}\|_2 < \mu$... unambiguous query otherwise," and
only an unambiguous query proceeds to similarity-based pixel retrieval
against the 3D language field.[^c2]

Evaluated on the LERF Figurines and 3D-OVS scenes, more specific queries
score higher norms than the general queries they disambiguate: "the query
food corresponds to both tart and green grape, and receives a score of
0.10 (below the threshold), indicating ambiguity... the query fruit scores
0.53, since only green grape is applicable... the more specific the query
is, the higher the score becomes, 0.74 and 1.59, respectively."[^c3]

## Why it matters

This gives an embodied agent a triggering rule for a clarifying question
that is a *byproduct of the retrieval representation itself* — no separate
ambiguity classifier, no LLM self-report of uncertainty, no explicit
enumeration of candidate referents. The training objective that makes
retrieval accurate (separate instances, compress robustly) is the same
objective that makes the norm carry an ambiguity signal, because ambiguous
labels are deliberately included as training targets that the two loss
terms cannot simultaneously separate and reconstruct except by shrinking
toward the origin.

## Transfer

| | |
|---|---|
| Home field | Metric learning / representation learning (contrastive and margin-based losses, e.g. triplet loss, large-margin cosine loss) |
| Here | The margin loss that normally only spaces instances apart is reused to make an *unspaced* region (features close to the origin) carry a semantic meaning: "this query does not separate cleanly into one instance" |
| What survives | The core mechanism — training two losses to [[competitive-llm-probing|compete]] (separate instances vs. reconstruct faithfully) forces genuinely ambiguous inputs into a geometrically distinct, low-norm region that a threshold can read off cheaply at inference time |
| What does not | The norm-as-ambiguity reading depends on this specific training recipe (ambiguous labels included, reconstruction loss present, cosine-based margin loss); a generic embedding trained only for discrimination has no reason for its ambiguous points to concentrate near the origin, so the transfer is to *this construction*, not to metric-learned embeddings generally |

## Limits

The claim that vector norm tracks ambiguity rests on the specific loss
combination (Eq. 1: $L_{lmc} + \lambda L_{reconst}$) and on training data
that explicitly supplies ambiguous text labels per object; the paper gives
no evidence the norm-threshold rule transfers to a feature space trained
without deliberately ambiguous labels, or to object vocabularies unlike the
service-robot household objects tested (3D-OVS, LERF Figurines). The
threshold $\mu$ itself is fixed per experiment rather than derived from a
[[calibration]] procedure, so this is a demonstrated mechanism, not a general
theorem about when embeddings encode ambiguity as norm. [?] — arXiv preprint,
2607.16309v1, not confirmed as peer-reviewed.

## Related

- [[embodied-ambiguity-sources]] — the two-way split (observation vs.
  semantic ambiguity) this mechanism sits inside; SaaF's ambiguity is
  semantic/referential, detected after observation, not a substitute for
  the observe/ask/select routing
- [[semantic-entropy]] — an LLM-side proxy for the same triggering
  decision, computed over generated meanings rather than a trained
  embedding norm
- [[knowno]] — the interactive task-planning system this paper explicitly
  positions itself against for assuming object locations and names are
  already known
- [[clarification-benchmarks]] — the broader empirical record that
  recognizing ambiguity and acting on it (asking) are different skills

[^c1]: yano-2026
[^c2]: yano-2026
[^c3]: yano-2026 — "the query food corresponds to both tart and green grape, and receives a score of 0.10 (below the threshold), indicating ambiguity. Meanwhile, the query fruit scores 0.53, since only green grape is applicable in this scene. We also confirmed that the more specific the query is, the higher the score becomes, 0.74 and 1.59, respectively."
