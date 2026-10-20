---
description: "A production system that ranks which of a curated set of query-narrowing facets to surface next for an underspecified search query, conditioned on the live query and user context."
aliases: ["DFS", "dynamic facet suggestion"]
sources: ["xu-2026-policy"]
---
# Dynamic facet suggestion

Dynamic facet suggestion (DFS) is a policy-grounded retrieval-and-ranking
mechanism deployed at LinkedIn that decides, for a short underspecified job
search query, which of a bounded set of facet values (workplace type,
industry, function, domain knowledge) to surface next as a clickable
refinement. Selecting a suggestion appends it to the query, so the
mechanism answers stall 2 — which axis of $W$ to constrain next — inside a
live retrieval interface rather than through a chat turn. "We introduce
dynamic facet suggestion (DFS), which surfaces a set of contextualized,
query-aware attributes (e.g., workplace type, industry, function, domain
knowledge) directly beneath the search bar... these facet 'pills' are
dynamically generated and personalized based on joint member–query
context."[^c1]

The action space is restricted to **narrowing** refinements: a suggested
facet must keep the intent expressed by the refined query a strict subset
of the intent expressed by the original query, ruling out broadening or
rewriting moves. "We focus exclusively on narrowing refinements which
increase query specificity without altering its core intent. Formally, we
require refinements to satisfy a monotonic precision property: the intent
expressed by q′ must constitute a strict subset of the intent expressed by
q."[^c2]

## Mechanism

1. **Offline taxonomy curation.** GPT-4o proposes facet-keyword candidates
   from seed queries; candidates pass an LLM-as-a-judge policy check
   (query faithfulness, member plausibility, refinement utility — axioms
   C1–C3), a job-liquidity check (does the keyword yield enough postings),
   and a search-popularity filter, then a human-in-the-loop review.
2. **Candidate retrieval.** A fine-tuned embedding model (Siamese,
   InfoNCE-trained) retrieves the top ~27 candidates from a pool of ~400
   taxonomy entries, conditioned on the joint query + member-context
   embedding.
3. **Candidate scoring.** A distilled small language model scores each
   candidate with a single-token "Yes"/"No" generation; $p_{\text{Yes}}$ is
   the ranking score. Point-wise single-token scoring with batching and
   prefix caching gives a 3–4× lower P95 latency than list-wise
   multi-token ranking at comparable (~90%) top-5 precision. "the
   point-wise formulation enables efficient batching and predictable
   latency, achieving a 3×∼4× reduction in P95 latency without increasing
   GPU cost."[^c3]
4. The top-5 "Yes"-scored facets are served.

The end-to-end ranking model reaches F1 = 0.84 and 91.1% precision on the
served top-5 facets after a four-stage training pipeline (base SLM →
reasoning SFT → on-policy distillation from a 14B teacher → prompt-compressed
class-only SFT). "The end-to-end models achieve an F1 score of 0.84, and
91.1% precision for the top-5 served facets."[^c4]

## Measured effect

In online A/B testing at production scale, DFS increased Facet
click-through rate by +34.8% (p < 0.0001), Job Apply-to-Impression ratio by
+2.6% (p = 0.0031), and Successful Job Search Sessions by +1.6%
(p < 0.0001), against a baseline of existing static facet filters. "Overall
Facet CTR ... +34.8% ... < 0.0001; Job Apply-to-Impression Ratio ... +2.6%
... 0.0031; Successful Job Search Sessions ... +1.6% ... <0.0001"[^c5]

The authors also report that DFS shifts the query distribution toward
multi-attribute queries, which can transiently degrade downstream
relevance models until they are co-trained on the new distribution. "DFS
also alters how members express intent by increasing the prevalence of
multi-attribute queries... it may introduce out-of-distribution query
patterns for downstream models, occasionally leading to transient
relevance regressions until those models adapt."[^c6]

## Limits

The measured lift rests on one deployment (LinkedIn job search) with a
single restricted action space (append-only narrowing over a curated,
policy-filtered taxonomy); the paper gives no evidence the same policy
formulation or the size of the lift transfers to open-ended clarification
(free-text questions) or to domains without a comparably curated facet
taxonomy. The offline precision figures are judged against an LLM-as-a-judge
proxy for the product policy, not independent human ground truth for every
reported number.

## Related

- [[intent-elicitation-graph]] — another ordering of which refinement to elicit next

[^c1]: xu-2026-policy
[^c2]: xu-2026-policy
[^c3]: xu-2026-policy — "the point-wise formulation enables efficient batching and predictable latency, achieving a 3×∼4× reduction in P95 latency without increasing GPU cost."
[^c4]: xu-2026-policy — "The end-to-end models achieve an F1 score of 0.84, and 91.1% precision for the top-5 served facets."
[^c5]: xu-2026-policy
[^c6]: xu-2026-policy
