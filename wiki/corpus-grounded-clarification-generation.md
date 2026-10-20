---
description: "Conditioning a clarifying-question generator on retrieved passages, then preferring it over noise-injected ungrounded negatives, makes questions answerable from the corpus; tested on four benchmarks."
aliases: ["RAC", "retrieval-augmented clarification", "corpus-faithful clarification"]
sources: ["arxiv-2601-11722"]
---
# Corpus-grounded clarification generation

A clarifying question can be fluent and on-topic yet ask about something the document collection cannot answer. Kebir et al. (2026) treat that as a distinct failure, separate from fluency or intent alignment, and propose RAC: generate the question from the user query plus the top-k retrieved passages, so that facet extraction happens implicitly inside the generator rather than as a separate stage.[^c1]

## Mechanism

1. **Passage-conditioned fine-tuning.** The model is trained with a negative log-likelihood on (query, passages, gold question) tuples. Qulac and ClariQ carry only document-level relevance labels, so the authors derive passage supervision: 250-token passages, an LLM rewrite of the query that folds in the gold clarification, then BM25 retrieval of pseudo-relevant passages.[^c2]
2. **Manufactured unfaithful negatives.** Two models are fine-tuned from one base: a grounded one (query and passages) and an ungrounded one (query only). Decoding samples each token from a mixture, taking the ungrounded model with Bernoulli probability alpha. The result is fluent text containing intrinsic errors (contradicting passages) and extrinsic ones (unsupported additions).[^c3]
3. **Preference tuning.** DPO prefers the grounded question over the noisy one for the same input; the final loss mixes DPO and SFT (weight 0.5 chosen by ablation).[^c4]

## What was measured

- Passage conditioning beats query-only fine-tuning on all four datasets (Qulac, ClariQ, PaQa, CAmbigNQ). A zero-shot passage-conditioned model scores below the query-only fine-tuned one, which the authors read as the form of a clarification having to be learned separately from its content.[^c5]
- Reference-overlap metrics (ROUGE, BLEU, METEOR, BERTScore) do not register the DPO gain; the reference-free faithfulness metrics (an NLI-based AlignScore and an adapted PARENT recall) do. GPT-4 judged DPO over SFT with ties dominating, e.g. 72.23% ties on CAmbigNQ.[^c6]
- More passages help but saturate at about four; random passages fall to roughly the query-only baseline; BM25 beat a dense retriever trained on MS MARCO, attributed to domain mismatch.[^c7]
- Negatives from the query-only fine-tuned model were better training signal than negatives from the raw base model, because the latter often do not resemble clarifications at all. Intermediate alpha gives negatives that are hard but informative.[^c8]
- Qualitatively, SFT sometimes asked about an entity the passages lacked (a season "17"); DPO stayed within the passages.[^c9]

## Limits

- Single-turn, one question, and every query is assumed ambiguous; whether to ask at all is not addressed.[^c10]
- Faithfulness is to the retrieved top-k, not to the whole corpus: a question grounded in retrieved passages may still miss a facet the retriever did not surface. This is my inference.
- Faithfulness metrics needed adapting: questions were converted to declarative statements for entailment scoring, and PARENT was applied through SpaCy entity extraction. Both are proxies; no human faithfulness study was reported.
- One 8B model; the training passages are pseudo-relevant from BM25, so "grounded" is partly defined by the same retriever used at test time.
- Only the DPO-over-SFT gap is shown to be faithfulness-specific; the gold-reference gains are confounded with learning question form.

## Related

- [[retrieval-conditioned-question-selection]] — also trains the generator on the retrieval state, but the target is rank improvement, not faithfulness
- [[preference-optimization-for-questions]] — preference tuning applied to question quality; here the negatives are synthetic and ungrounded
- [[dynamic-facet-suggestion]] — the explicit facet route that RAC replaces with implicit facets from passages
- [[clarification-benchmarks]] — Qulac, ClariQ and AmbigNQ-derived sets used here

[^c1]: arxiv-2601-11722 — "Facet extraction is performed implicitly by supplying the topk retrieved passages to the LLM, which then generates the clarifying question."
[^c2]: arxiv-2601-11722 — "This produces training tuples (Uq , D, Cq ) that support retrieval-conditioned clarification generation."
[^c3]: arxiv-2601-11722 — "The resulting questions remain fluent but contain ungrounded"
[^c4]: arxiv-2601-11722 — "In our joint loss, we set γ = 0.5, based on ablation results."
[^c5]: arxiv-2601-11722 — "The fact that QP-Zero performs significantly worse than Q-cond highlights"
[^c6]: arxiv-2601-11722 — "Moreover, results show that reference-based measures fail to capture the"
[^c7]: arxiv-2601-11722 — "but the effect saturates after approximately four passages"
[^c8]: arxiv-2601-11722 — "Table 3 shows that puncond provides more effective negative"
[^c9]: arxiv-2601-11722 — "RACDP O produces questions more tightly grounded in passages."
[^c10]: arxiv-2601-11722 — "we restrict to a single-turn"
