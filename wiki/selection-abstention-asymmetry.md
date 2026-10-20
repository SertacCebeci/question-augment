---
description: "In on-device tool routing, lexical retrieval solves which tool to call but not whether any tool applies; the two decisions need different components."
aliases: ["selection-abstention asymmetry"]
sources: ["lee-2026-selection"]
---
# Selection–abstention asymmetry

> Ranking the catalog and deciding the catalog contains nothing valid are not
> the same problem, and a component that is excellent at the first can be
> near-chance at the second.

## Definition / Mechanism

Lee (2026) separates two decisions a tool-calling
router makes on every request: **selection** — which local action is nearest
to the request — and **abstention** — whether the catalog contains a valid
action at all. "A retriever answers the first by construction and cannot
answer the second, because it returns a nearest item even when every item is
wrong."[^c1]

Over 600 Korean/English requests against a 70-action catalog, a
character-3-gram BM25 retriever reaches 0.988 top-1 accuracy on
vocabulary-matched selection, but on the in-catalog-versus-out abstention
question "the six BM25 score features range from 0.480 to 0.610 AUC
individually," and a seven-feature logistic combination over those scores
("G3") reaches only "0.697 on mismatch-in versus out" — while a frozen
sentence encoder (multilingual-e5-base) reaches 0.806 AUC on the same
abstention split.[^c2]

Architecturally separating an in-catalog gate from nearest-item selection —
rather than letting the retriever's top score double as a confidence
signal — "reduces delegate-to-skill errors from 134 to 12 of 150" and
mutating false positives from 269 to 43 of 600 requests. The paper's summary
of the asymmetry: "Abstention, not selection, is where a neural component is
required."[^c3]

The gap survives resampling: on a cluster bootstrap (2000 resamples) the
encoder exceeds the BM25-feature gate by 0.109 AUC (95% CI [0.059, 0.159]).[^c4]

## Why it matters

On stall 2 this names a precondition every selection criterion on the map
assumes without stating: that the candidate set contains a valid answer to
select. [[entropy|Entropy]]-drop, GBS, EIG and [[adaptive-submodularity]] criteria all
presuppose $W$ is non-empty of the right kind; this result shows that
whether that presupposition holds is a *separate*, harder-to-solve decision
from choosing among the candidates once it does, and that a method proven to
solve the second (lexical or embedding retrieval) is not thereby shown to
solve the first.

## Limits

- The claim rests on one deployed catalog (70 actions, Korean/English,
  on-device tool routing); the paper itself frames the utterances as
  "authored... not a sample of production traffic," so the absolute AUC
  numbers are this catalog's, not a general constant.
- "Abstention" here is a binary in/out-of-catalog gate, not the general
  reject-option framework of [[abstention]] (which prices a coverage/risk
  tradeoff over a fixed label set with ground truth); no risk–coverage curve
  is computed in this paper, so the relation to that framework is an analogy
  of shape (a decision split into "what" and "whether"), not a shared metric.
- Query length alone accounts for most of the BM25-feature gate's AUC
  (0.741 out-of-fold), a possible artifact of how mismatch/out-of-catalog
  items were authored rather than a routing signal; the paper flags this
  itself and reports the conclusion survives either reading.

## Related

[[abstention]] · [[recognition-refusal-dissociation]] · [[generalized-binary-search]] · Selection

[^c1]: lee-2026-selection — "A retriever answers the first by construction and cannot answer the second, because it returns a nearest item even when every item is wrong."
[^c2]: lee-2026-selection — "the six BM25 score features range from 0.480 to 0.610 AUC individually"
[^c3]: lee-2026-selection — "reduces delegate-to-skill errors from 134 of 150 to 12 of 150"
[^c4]: lee-2026-selection — "e5 exceeds G3 by 0.109 AUC with a 95% interval of [0.059, 0.159]"
