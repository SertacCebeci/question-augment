---
description: "Score the answerer's own rationale by the share of its statements an NLI critic finds entailed by retrieved text; if under 0.7, append the unsupported statements to the query and retrieve again."
aliases: ["self-reflective retrieval loop", "rationale support score", "Self-MedRAG"]
sources: ["doi-10-48550-arxiv-2601-04531"]
---
# Unsupported-rationale query refinement

Each iteration retrieves context for the current query, has the generator produce an answer plus a rationale citing that context, and then checks the rationale against the context. Each rationale statement is compared with every retrieved passage; an NLI model (RoBERTa-large-MNLI) or a prompted Llama 3.1-8B takes the passage as premise and the statement as hypothesis, and the best entailment confidence is kept per statement.[^c1] A statement counts as supported if that confidence exceeds tau = 0.5. The support score S is the proportion of supported statements. If S is at least theta = 0.7 the answer is returned.[^c2]

Otherwise the unsupported statements are collected and the next query is the old query plus those statements (Q(i+1) = Qi union Ui). The history of earlier queries, contexts and rationales goes back into the generator prompt.[^c3] The query is therefore rewritten by what the answerer claimed but could not ground, not by the question alone. The loop's stop signal is the rationale's grounding, not the model's stated confidence. Both thresholds were chosen on preliminary validation experiments.[^c4]

## Reported effect

On 1,000 questions sampled from MedQA and PubMedQA, with DeepSeek as generator, adding the loop to a hybrid-retrieval baseline raised PubMedQA accuracy from 69.10% to 79.82% and MedQA from 80.00% to 83.33% (NLI critic).[^c5] The LLM critic gave 78.76% and 82.90%; the authors conclude that gains come from the iteration, not the critic's identity, since both critics beat the non-iterative baseline.[^c6] Per-iteration curves show most of the gain at the second pass (MedQA 79.3% to 86.1%, PubMedQA 69.8% to 83.3%), with a plateau or slight MedQA decline at a third.[^c7]

The retrieval underneath is hybrid: BM25 and Contriever-MSMARCO rankings are fused by Reciprocal Rank Fusion (K = 60). On MedQA the fused retriever reached 80.00% against 41.74% (BM25) and 43.30% (Contriever) alone.[^c8] The authors attribute this to complementary lexical and semantic evidence; that is their explanation, not an isolated test.

## Limits

- The critic checks entailment against the retrieved passages only. A rationale supported by a wrong or irrelevant passage passes; support is not truth. (My inference.)
- No ablation separates "second retrieval with a different query" from "second generation with history", so "iteration itself" is not isolated from the query-update rule. (My inference.)
- The MedQA baseline jump from about 42% to 80% through fusion is very large and unexplained by a controlled test; the single-retriever numbers may reflect index or setup issues. (My inference.)
- Only medical benchmarks, a sample of 1,000, one generator, no variance reported; thresholds tuned on preliminary validation data of unstated size.
- Gains shrink or reverse after two iterations, so the loop needs a cap that the algorithm as written lacks (it is `while true`).

## Related

- [[verification-aware-stopping]] — also stops on evidence matching claims, with a trained per-hop verifier instead of a general NLI critic.
- [[reasoning-gap-driven-retrieval]] — turns unmet checklist items into follow-up sub-queries; here the unmet items are unsupported rationale statements.
- [[coverage-driven-retrieval-control]] — a retrieve, reformulate or stop policy driven by coverage signals.
- [[decoupled-support-contradiction-retrieval]] — NLI over retrieved text for support and contradiction.

[^c1]: doi-10-48550-arxiv-2601-04531 — "For every evidence context and rationale pair, the evidence passage serves as the premise and the rationale statement as the hypothesis."
[^c2]: doi-10-48550-arxiv-2601-04531 — "If Si ≥ θ = 0.7, the system returns (Ai, Rati) as the final"
[^c3]: doi-10-48550-arxiv-2601-04531 — "Update query: Qi+1 ← Qi ∪ Ui"
[^c4]: doi-10-48550-arxiv-2601-04531 — "were selected based on preliminary validation experiments to balance retrieval"
[^c5]: doi-10-48550-arxiv-2601-04531 — "increasing PubMedQA accuracy from 69.10% to 79.82% and MedQA accuracy"
[^c6]: doi-10-48550-arxiv-2601-04531 — "demonstrating that the improve in performance is due to the iteration"
[^c7]: doi-10-48550-arxiv-2601-04531 — "MedQA accuracy rising from 79.3% to 86.1% and PubMedQA from"
[^c8]: doi-10-48550-arxiv-2601-04531 — "performance from 41.74% (BM25 alone) and 43.30% (Contriever alone) to 80.00%"
