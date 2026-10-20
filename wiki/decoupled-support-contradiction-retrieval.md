---
description: "Support and contradiction follow different retrieval dynamics; dense retrieval collapses negation, so contradictions come from a deep lexical pool, a negation filter and NLI."
aliases: ["semantic collapse of negation", "retrieval asymmetry", "decoupled lexical architecture", "entailment trap"]
sources: ["arxiv-2603-17580"]
---
# Decoupled support and contradiction retrieval

A question asked of a corpus has two evidential answers: passages that agree with a claim and passages that refute it. The work argues the two follow different retrieval dynamics and need separate pipelines. Most retrievers optimize topical similarity, so models "conflate 'about the same topic' with 'agrees with the claim.'"[^c1] Refutations are rarer and often expressed through negation, hedging or population-specific conditions, which makes them hard for generic dense retrieval to capture.[^c2]

## Mechanism

The authors name the failure "Semantic Collapse": a refutation and an agreeing passage on the same topic sit close together in vector space, so the negation signal is lost.[^c3] They tie this to earlier findings that models misclassify contradictions as agreements when word overlap is high.[^c4]

Their fix is a decoupled pipeline on the SciFact proxy. Support uses BM25 at depth 100 plus a biomedical cross-encoder reranker. Contradiction uses BM25 at depth 1000, then a NegEx negation filter, then sentence-level NLI.[^c5] Depth is the main decoupling lever: contradiction needs a large candidate pool because few candidates survive the filter.

Measured on SciFact (124 support and 64 contradiction claims), weighted MRR was 0.790 for the BM25 pipeline. Its support MRR was 0.810 and its contradiction MRR 0.750. The dense pipeline with the same filter got contradiction 0.766 but support 0.786, and weighted MRR 0.779.[^c6]

Two further observations:

- **Retrieval asymmetry.** Applying the strict negation filter to dense candidates helped contradictions but hurt support. The authors' reading is that dense retrievers rely on semantic smoothness, and keyword constraints disrupt their ranking of supporting evidence.[^c7] This reading is theirs and was not isolated experimentally.
- **Simplicity paradox.** An "adversarial" dense variant with a complex penalty formula scored 0.023 on contradiction MRR, worse than naive BM25 at 0.109, despite a pool of 1200. The authors conclude that binary filtering beats probabilistic complexity in zero-shot biomedical verification.[^c8]

For a questioner, the implication is that asking for the opposing evidence is a different retrieval task from asking for the confirming evidence, and a single ranked list tends to serve only the second.

## Limits

- One proxy dataset (SciFact, 188 claims) stands in for PubMed. Transfer to the 30-million-document target was not measured against labels. The official TREC result (second on contradiction F1) is reported but not decomposed by component.
- The dense-versus-lexical comparison mixes backbone and depth. The causal story for Semantic Collapse is inferred from related work and the score pattern, not probed in embedding space.
- Variant 4's failure is attributed to the penalty formula's calibration with the word "likely"; it was not ablated.
- The choice of BM25 was partly made for scalability, so the accuracy edge over dense was small (0.790 against 0.779).
- Only one negation detector (NegEx) and one NLI setup were tested.

## Related

- [[selection-abstention-asymmetry]] — another case where lexical retrieval handles one decision but not its complement
- [[solve-verify-detection-gap]] — contradictions go unnoticed unless a separate verification step looks for them
- [[contradiction-gate]] — a downstream gate acting on detected contradiction
- [[retrieval-order-sensitivity]] — which evidence ranks first shapes the answer

[^c1]: arxiv-2603-17580 — "leading models to conflate"
[^c2]: arxiv-2603-17580 — "often expressed"
[^c3]: arxiv-2603-17580 — "where negation signals get lost because the topics are very"
[^c4]: arxiv-2603-17580 — "agreements when there is high word overlap"
[^c5]: arxiv-2603-17580 — "uses BM25 (𝑘 = 1000) + NegEx filter + sentence-level NLI."
[^c6]: arxiv-2603-17580 — "Weighted MRR"
[^c7]: arxiv-2603-17580 — "disrupts their ranking logic for supporting evidence."
[^c8]: arxiv-2603-17580 — "This validates the principle that in zeroshot biomedical verification, heuristic simplicity (binary filtering)"
