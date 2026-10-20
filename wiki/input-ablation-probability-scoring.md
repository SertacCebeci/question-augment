---
description: "A learned scorer reads answer-token probabilities from the same VLM re-run with image and/or retrieved context removed, so the score reflects retrieval and visual uncertainty, not only generation."
aliases: ["LeMUQ", "Learnable Multimodal Uncertainty Quantification", "multimodal RAG uncertainty quantification", "input-configuration probability tokens"]
sources: ["openalex-org-w7162894282"]
---
# Input-ablation probability scoring

In multimodal retrieval-augmented generation the answer can be wrong for different reasons: the image is ambiguous, the retrieved text is noisy, the modalities are merged badly, or generation itself fails. The paper's claim is that a single token-probability trace from the full input cannot separate these, so it re-reads the answer under several input configurations.[^c1]

## Mechanism

A VLM receives query, image and retrieved context and produces a response with per-token probabilities. The same response is then re-scored with the image removed, with the retrieved context removed, and with both removed. Each probability sequence is discretised into quantile bins and mapped to special "probability tokens". Query, context, response tokens and all four probability sequences are concatenated and passed to a fine-tuned RoBERTa-based scorer, which emits one scalar confidence for the response.[^c2] This extends LARS, a learnable scorer that sees only one probability sequence.

The method is white-box and uses a single generation per answer, unlike sampling-based methods that use diversity among several outputs.[^c3]

## What was measured

- In-distribution (same retriever, dataset, VLM in training and test), the method beat baseline and fine-tuned UQ methods, with average AUROC 0.88, about 3.8% above the comparison on average.[^c4]
- Standard UQ methods lose performance as the supplied context gets more reliable, and a VLM-specific method based on removing visual evidence fails to give meaningful results once context is added.[^c5]
- Ablating one probability component at a time: dropping the without-image probability or the plain-response probability hurt most; the best variant differed by retriever and VLM, so no single component dominated.[^c6]
- Transfer is uneven: gains largely hold across retrievers, usually hold across datasets, and are mixed across VLMs.[^c7] Training on LLaVA transferred to Qwen3, but not the reverse; the authors suggest the extra parameters and signals need more training data than LARS.[^c8]

## Limits

- It needs token-level probabilities, so it is unavailable for API-only models.[^c9]
- Only a single retrieved context and relatively simple retrievers were tested; retriever effects on uncertainty are left open.[^c10]
- Robust generalisation under distribution shift is not shown; the paper says so itself.
- The reason for the VLM-transfer asymmetry (model complexity versus data) is the authors' conjecture, not tested. The per-source attribution of uncertainty to retriever, visual input or generator is not reported as a decomposition; only the aggregate score is evaluated (my reading).

## Related

- [[uncertainty-source-attribution]] — asks which pipeline stage the uncertainty comes from; this method folds the sources into one score
- [[uncertainty-decomposition]] — separates uncertainty kinds, which this scorer does not
- [[internal-prober]] — also contrasts model behaviour with and without retrieved context, via hidden states
- [[uncertainty-hallucination-relevance-gap]] — related finding that uncertainty signals depend on context relevance

[^c1]: openalex-org-w7162894282 — "A UQ model for multimodal RAG needs to"
[^c2]: openalex-org-w7162894282 — "the response is re-evaluated under multiple"
[^c3]: openalex-org-w7162894282 — "we focus on white-box probability-based methods and use a single generation"
[^c4]: openalex-org-w7162894282 — "LeMUQ consistently outperforms both baseline and finetuned"
[^c5]: openalex-org-w7162894282 — "fail to produce meaningful results"
[^c6]: openalex-org-w7162894282 — "Across most configurations, variants of LeMUQ consistently outperform LARS𝑅𝑒𝑡 ,"
[^c7]: openalex-org-w7162894282 — "yields mixed results when transferring"
[^c8]: openalex-org-w7162894282 — "which does not transfer effectively to LLaVA."
[^c9]: openalex-org-w7162894282 — "LeMUQ requires access to tokenlevel probability information, or logits, from the underlying VLM."
[^c10]: openalex-org-w7162894282 — "Second, we consider only a single retrieved context."
