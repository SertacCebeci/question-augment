---
description: "Evidence forgetting rate: among cases where all golden documents were retrieved, the share still answered wrongly; it separates evidence use from retrieval recall in multi-hop RAG."
aliases: ["EFR", "key-evidence forgetting"]
sources: ["arxiv-2601-11024"]
---
# Evidence forgetting rate

End-task accuracy in retrieval-augmented QA mixes two failures: the retriever never fetched the needed evidence, or it did and the generator failed to use it. The evidence forgetting rate (EFR) isolates the second. Shuguang et al. define it as the proportion of cases where golden evidence has been retrieved but the answer is still incorrect.[^c1]

## Mechanism

The denominator is the set of questions for which every golden document was retrieved; the numerator is those among them answered incorrectly. This conditions away retrieval recall, so a method can be compared on how well it uses what it has. The paper marks EFR as not applicable for a no-retrieval baseline, and for single-shot methods where the denominator (all golden documents retrieved) is zero; comparisons are among multi-turn retrieval methods.[^c2]

In their method, a [[confidence-gated-query-decomposition-tree]], removing the confidence-based pruning raised EFR: accepting unreliable intermediate answers disrupts transmission of critical evidence. The authors report an average EFR reduction of 20.8% against mainstream multi-retrieval baselines.[^c3]

## Limits

- It is defined and used by one paper, with no external validation of the metric.
- Conditioning on full golden recall makes the denominator small and method-dependent; comparisons between methods use different question subsets. That is my observation.
- "Forgetting" is a label for any wrong answer given the evidence; it does not distinguish distraction, reasoning error or answer-format mismatch.
- Requires annotated golden documents.

## Related

- [[confidence-gated-query-decomposition-tree]] — the method it was introduced to evaluate
- [[lost-in-generation-entity-grounding]] — another account of failures after the right input is present
- [[sequence-likelihood-confidence]] — the confidence signal used to reduce EFR

[^c1]: arxiv-2601-11024 — "Evidence Forgetting Rate (EFR), which measures the proportion"
[^c2]: arxiv-2601-11024 — "denominator case where all"
[^c3]: arxiv-2601-11024 — "with an average reduction of"
