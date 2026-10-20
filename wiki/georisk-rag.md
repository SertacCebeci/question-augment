---
description: "A DAG-based hierarchical-distance gate that classifies retrieved context against a query's geography as exact, broader, narrower, or a different place, and answers, warns, or abstains accordingly."
aliases: ["GeoRisk-RAG", "hierarchy-aware selective answering", "geographic-validity gating"]
sources: ["ravi-2026"]
---
# GeoRisk-RAG — hierarchy-aware selective answering

> A retrieved passage that is topically on-target can still be geographically
> wrong; GeoRisk-RAG measures how far wrong using the passage's position in
> an explicit place hierarchy, and turns that distance into a three-way
> commitment decision instead of a binary answer/abstain choice.

## Definition / Mechanism

Ravi, Sarkar, AlKulaib, Tessema & Lu (2026) build a directed
acyclic graph of administrative and landscape entities from Wikidata and
place both the query's target location and each retrieved passage's
geographic scope on it. The relationship between the two is classified into
one of four cases — exact match, passage broader than the query, passage
more specific (narrower) than the query, or a different place sharing only
a distant common ancestor — and that classification, not a confidence
score, drives the answering decision: "The extracted relationship is
classified as an exact match, broader context, more-specific context, or
different place-context. This classification guides selective answering in
which GeoRisk-RAG directly answers when context exactly matches the query
geography, warns when context is geographically related but broader or more
specific than the requested scope, and abstains when retrieved context
concerns a different place that only shares a broad ancestor with the
query's intended location."[^c1]

The evaluation keeps the middle case (warn) analytically separate from both
ends: *Appropriate Warning Rate* is the share of cases where a warning was
the correct call, *Over-Abstention Rate* is declining to answer despite
sufficient context, and *False Confidence Rate* is answering confidently
despite geographically invalid context — three distinct failure modes
rather than one abstention-vs-answer split.[^c2]

On a held-out 449-pair wildfire QA benchmark, this reduced the false
confidence rate on location-dependent queries to 0.009 against a 0.090
baseline: "GeoRisk-RAG reduces the false confidence rate from 0.090 to
0.009 compared to standard semantic similarity and reranking baselines."
Two blinded human annotators preferred GeoRisk-RAG's responses over the
strongest baseline in 70.0% and 68.75% of cases respectively (Cohen's
κ = 0.76).[^c3]

## Why it matters

This is a structural instance of the reject-option decomposition in
[[abstention]], but the selection function $g$ is not a scalar threshold on
a score — it is a lookup on graph distance in an externally supplied
applicability hierarchy, and its range is three-valued (answer / warn /
abstain) rather than two-valued. On stall 10 it gives a concrete mechanism
for "how much to commit, and how to say the rest": the warn tier is a
partial commitment that names the mismatch (e.g. answering at the state
level while flagging that the query asked at the county level) instead of
collapsing every non-exact match into refusal.[^c4]

## Transfer

| | |
|---|---|
| In its home field | geospatial disaster-QA over a Wikidata-derived administrative/landscape DAG, one hierarchy type (place containment), a fixed four-way relation taxonomy |
| Here | any answerer whose retrieved evidence carries a structural applicability scope narrower or broader than the question's (jurisdictions, software-version ranges, org-chart authority, time-bounded regulations) |
| What survives | classifying context by structural distance in an applicability hierarchy, not by a learned confidence score; keeping the middle case (partial commitment with a named mismatch) as a distinct output instead of forcing a binary decision |
| What does not | the specific DAG (Wikidata place containment) and its four-way relation taxonomy; the toponym-disambiguation heuristics; the claim is validated only for exactly this one hierarchy type and domain |

## Limits

- The claim rests on one domain (wildfire/natural-hazard QA), one external
  hierarchy source (Wikidata), and human validation on only 50 sampled
  location-dependent questions by two annotators; generalization to other
  applicability hierarchies (legal, temporal, organizational) is not
  tested.[^c5]
- The four-way relation taxonomy assumes the hierarchy is a clean DAG with
  resolvable toponyms; the paper's own disambiguation scheme (explicit
  identifiers, then context, then population, then sitelink counts) is a
  heuristic fallback the note does not carry as a general result.
- Good Decision Quality and false-confidence numbers are produced by an
  LLM-as-judge (Nemotron-3-Super) rather than by ground-truth labels
  applied automatically, so the metric partially depends on judge
  [[calibration|reliability]], which the paper does not separately validate against human
  labels beyond the 50-question spot check.[^c6]

## Related

[[abstention]] · [[compression-aware-abstention]] · [[calibration]] · Commitment

[^c1]: ravi-2026
[^c2]: ravi-2026 — "Appropriate Warning Rate: The proportion of cases in which the system appropriately provides a warning when the retrieved context is insufficient, irrelevant, or geographically mismatched."
[^c3]: ravi-2026 — "GeoRisk-RAG reduces the false confidence rate from 0.090 to 0.009 compared to standard semantic similarity and reranking baselines."
[^c4]: ravi-2026 — "GeoRisk-RAG gracefully escalates to the state level (New Mexico) and explicitly warns the user that the retrieved information applies at the state level, before providing a contextually relevant answer that aligns with the ground truth"
[^c5]: ravi-2026 — "For each of 50 randomly selected location-dependent questions, annotators were presented the original question and the unique responses generated by the 5 evaluation configurations"
[^c6]: ravi-2026 — "The Nemotron-3-Super is used as the LLM judge due to its reported effectiveness in long-context reasoning"
