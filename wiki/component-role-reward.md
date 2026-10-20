---
description: "Giving each field of a multi-part model output its own reward, judged by what the downstream search engine does with that field, beat one end-to-end reward on search quality."
aliases: ["component-specific reward", "role-specific component reward", "decomposed composite reward", "search-aware component reward"]
sources: ["doi-10-48550-arxiv-2609-30177"]
---
# Component-role reward

A model that emits one structured output with several fields can be trained with one reward on the final result, or with one reward per field. The second design is what this work tests. Its query-understanding model emits a JSON search plan with fields for intent, normalized query, fan-out queries, negative terms and attributes. Each field is scored against the role it plays in the search pipeline, and the scores depend on what the engine returns. "We therefore run the live production search and pass the returned results to an LLM judge alongside the QU output."[^c1] The intent reward asks whether the declared intent is right given the retrieval route it triggered and the items it returned.[^c2] The fan-out reward scores each expansion lane by its own search quality, minus a penalty for overlap with the other lanes and the normalized query.[^c12] Nothing in the scheme needs labels: "each is computed entirely from the input query, the QU output, and live interaction with the production search engine."[^c3]

The per-field scores are combined by a plain mean over the rewards that apply, so a field that is not triggered (no search, no fan-out) drops out instead of counting as zero. A formatting failure zeroes the whole output, because an invalid plan cannot be executed.[^c13] The mechanism claimed is credit assignment. A single outcome reward cannot say which field earned a good or bad result, so the signal it does pass back is concentrated on one field. The authors state that "a single end-to-end signal cannot disentangle which upstream component was responsible for a good or bad outcome, so what little credit survives concentrates on fan-out, leaving the other components with little to learn from."[^c4]

Measured on the same SFT starting point (Qwen 4B, GR-DPO), the composite reward reached NDCG@20 of 54.1, against 50.6 for the policy trained on the single search reward ("NDCG@20: 50.6% vs. 54.1%"). The composite also reached a higher aggregate per-field score, 0.861 against 0.820.[^c5] The abstract puts the gap at 3.5 NDCG points.[^c6] The single-reward policy was not worse on everything: it scored higher on the search reward it was trained on and on the fan-out reward.[^c11]

## Limits

- The comparison is one pair of runs on one model family, one offline algorithm and one production domain. The authors say "Both policies are trained from the same Qwen 3.5 4B sft checkpoint with GR-DPO."[^c7]- The single-reward arm uses the search reward and the format check, while the composite uses all seven rewards. The 3.5-point gain therefore is not isolated from the effect of adding more judges. Separating "more signal" from "per-field signal" is not done here (my inference).
- The comparison is reported for one starting checkpoint in the figure caption, so the text gives no run across other starting points or seeds.
- The search-utility reward is an LLM judge's relevance label, not ground truth. The text validates it only against target-game labels on a subset, and reports that "lists where it is missed tend to receive lower scores, though with substantial variance within each bucket."[^c8]
- The per-field criteria are not reproducible from the text. "we omit the full prompt text and the exact search mechanics underlying this coupling," so a reader cannot check which search behaviour each judge was told to look for.[^c9]
- The seven rewards carry equal weight, and no weighting is tuned. The gain is reported for offline GR-DPO. On-policy methods were tried and the authors report that "whereas on-policy training proves less stable under our" decomposed reward, so the benefit is not shown for every optimizer.
- The authors extend the idea "beyond this industry context" to "any production search with a comparable multi-task QU formulation."[^c10] That is a hope, not a result. Nothing here tests a second search system, or a structured output whose fields do not have separable downstream roles.

## Related

- [[dimension-aware-reward-decomposition]] — splits one given score across the actions that earned it, by action type. This note instead builds a judge per field from the start and combines them by a mean; the two share the credit-assignment motive, not the mechanism.
- [[multi-objective-advantage-aggregation]] — normalizes each objective's reward before combining, to stop one scale from dominating. It addresses scale, not which field earned the outcome.
- [[intermediate-query-quality-credit]] — scores each intermediate search query for usefulness, a per-query version of the same role-based judgment.
- [[competence-aware-credit-assignment]] — assigns credit along the time axis of a tool-use trajectory, where this note assigns it across the fields of one output.

[^c1]: doi-10-48550-arxiv-2609-30177 — "We therefore run the live production search and pass the returned results to an LLM judge alongside the QU output."
[^c2]: doi-10-48550-arxiv-2609-30177 — "an LLM judge evaluates whether the declared intent is correct."
[^c3]: doi-10-48550-arxiv-2609-30177 — "each is computed entirely from the input query, the QU output, and live interaction with the production search engine."
[^c4]: doi-10-48550-arxiv-2609-30177 — "a single end-to-end signal cannot disentangle which upstream component was responsible for a good or bad outcome"
[^c5]: doi-10-48550-arxiv-2609-30177 — "yields a higher aggregate score (0.861 vs. 0.820)"
[^c6]: doi-10-48550-arxiv-2609-30177 — "by 3.5 points over training with a single end-to-end reward."
[^c7]: doi-10-48550-arxiv-2609-30177 — "Both policies are trained from the same Qwen 3.5 4B sft checkpoint with GR-DPO."
[^c8]: doi-10-48550-arxiv-2609-30177 — "lists where it is missed tend to receive lower scores, though with substantial variance within each bucket"
[^c9]: doi-10-48550-arxiv-2609-30177 — "we omit the full prompt text and the exact search mechanics underlying this coupling"
[^c10]: doi-10-48550-arxiv-2609-30177 — "Beyond this industry context, the underlying idea applies to any production search with a comparable multi-task QU formulation."
[^c11]: doi-10-48550-arxiv-2609-30177 — "The single-reward policy exceeds the composite-reward policy on"
[^c12]: doi-10-48550-arxiv-2609-30177 — "Search overlap penalty: from the same search run, we measure the overlap (via Jaccard similarity) between the returned items"
[^c13]: doi-10-48550-arxiv-2609-30177 — "Invalid QU output cannot be executed."
