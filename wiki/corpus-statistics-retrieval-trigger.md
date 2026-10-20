---
description: "Gate retrieval by pre-training corpus counts, not model logits: rare question entities and zero entity co-occurrence in the corpus trigger retrieval; reported gains are on OLMo-2."
aliases: ["corpus-grounded uncertainty", "QuCo-RAG trigger", "pre-training co-occurrence check"]
sources: ["arxiv-2512-19134"]
---
# Corpus-statistics retrieval trigger

A dynamic RAG system must decide during generation whether to retrieve. The common gate reads the model's own signals, such as logits or entropy, and the paper's premise is that these are unreliable: "existing methods rely on model-internal signals (e.g., logits, entropy), which are fundamentally unreliable because LLMs are typically ill-calibrated".[^c1] The alternative takes the uncertainty from the pre-training corpus itself. The model's factual knowledge is treated as a function of that corpus, so counts in the corpus stand in for how well the model knows something.[^c2]

The trigger has two checks, both answered by lookup in a suffix-array index of the corpus (Infini-gram). "Both stages leverage Infini-gram (Liu et al., 2024) for millisecond-latency queries over trillion-token corpora."[^c3]

**Stage 1, before generation.** Entities are pulled from the question. Retrieval fires when their average corpus frequency falls below a threshold, with a default of 10^3.[^c19] The rationale is that low-frequency entities mark "long-tail knowledge that models struggle to memorize reliably".[^c4]

**Stage 2, during generation.** Each generated sentence is turned into knowledge triplets (head, relation, tail), and the head and tail entities are counted together within a 1,000-token window, "roughly matching passage-level context length".[^c5] If the minimum count over the triplets is below 1,[^c20] retrieval runs and the sentence is regenerated with a query built from head and relation. A zero count is read as "evidential support" being absent, "and likely constitutes a hallucination".[^c6] Zero co-occurrence is treated as a sign of risk, not as a verdict on truth.

**What was measured.** On 2WikiMultihopQA and HotpotQA with OLMo-2 models (7B to 32B), the paper reports that QuCo-RAG "achieves EM gains of 5–12 points over" state-of-the-art baselines.[^c7] In the ablation (2Wiki, OLMo-2-7B), removing the runtime check causes "a larger drop of 5.1 EM points", and removing the initial check reduces EM by 2.5.[^c8] The paper reads this as co-occurrence verification being the more important stage.

The gain depends on entity frequency. In the rarest bin (0–10 occurrences), the method is "outperforming Wo-RAG by 10–17 EM", while internal-signal methods come out "nearly identical" to no retrieval despite triggering retrieval, "suggesting that models lack sufficient signal to recognize uncertainty on rare entities."[^c9] In the highest-frequency bin, internal-signal baselines degrade while the corpus trigger keeps improving; the paper's explanation is overconfidence on the baseline side and "richer knowledge coverage" on the corpus side.[^c10]

Transfer to models with undisclosed training data is the paper's second claim. Corpus statistics from OLMo-2's corpus are used as a proxy, justified by "the substantial overlap of web-scale pre-training corpora"[^c11], and the paper reports EM improvements "by up to 14" on Llama-3, Qwen2.5 and GPT-4.1/5-chat.[^c12]

A theoretical note in the paper supports the premise: for rarely seen facts, "even perfectly calibrated models must hallucinate".[^c13]

## Limits

- The matched-corpus results are for one family (OLMo-2) with a full index. The transfer to closed models rests on the corpus-overlap assumption, which is argued, not measured per model.
- The ablation is one configuration (2Wiki, OLMo-2-7B). The paper does not show per-component effects across all datasets.
- Co-occurrence is asymmetric. Nonzero co-occurrence "does not guarantee correctness": "entities may co-occur with different relations or in unrelated contexts."[^c14] On a post-hoc sample, Stage 2 "detects roughly half of the hallucinated" sentences, and "59–68% involve wrong-relation hallucinations" among the misses.[^c15]
- Matching is lexical. Aliases such as "NYC" and "New York City" can produce "false positive retrieval triggers when two genuinely" related entities co-occur under other names.[^c16]
- The index is static. A corpus snapshot "cannot provide meaningful" statistics for entities or events that emerged after it was built.[^c17]
- Stage 2 depends on a triplet extractor; the paper "distill[s] a specialized 0.5B model from GPT-4omini" for it, and the end-to-end results carry that dependency.[^c18]
- My inference, not tested in the paper: a count threshold is not a calibrated probability, so the trigger says where retrieval is cheap insurance, not how likely an answer is wrong.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the internal-likelihood gate this trigger is set against; the two disagree on which signal to trust
- [[sequence-likelihood-confidence]] — the token-probability confidence that the paper calls unreliable
- [[parametric-knowledge-gates-retrieval-noise-damage]] — where retrieval adds noise; a corpus gate that fires on rare entities would have to be checked against that regime

[^c1]: arxiv-2512-19134 — "existing methods rely on model-internal signals (e.g., logits, entropy), which are fundamentally unreliable because LLMs are typically ill-calibrated"
[^c2]: arxiv-2512-19134 — "fundamentally shaped by its pre-training corpus"
[^c3]: arxiv-2512-19134 — "Both stages leverage Infini-gram (Liu et al., 2024) for millisecond-latency queries over trillion-token corpora."
[^c4]: arxiv-2512-19134 — "long-tail knowledge that models struggle to memorize reliably"
[^c5]: arxiv-2512-19134 — "to 1,000 tokens, roughly matching passage-level"
[^c6]: arxiv-2512-19134 — "evidential support and likely constitutes a hallucination"
[^c7]: arxiv-2512-19134 — "achieves EM gains of 5–12 points over"
[^c8]: arxiv-2512-19134 — "causes a larger drop of 5.1 EM points"
[^c9]: arxiv-2512-19134 — "suggesting that models lack sufficient signal to recognize uncertainty on rare entities"
[^c10]: arxiv-2512-19134 — "degradation while QuCo-RAG continues to improve"
[^c11]: arxiv-2512-19134 — "Leveraging the substantial overlap of web-scale pre-training corpora"
[^c12]: arxiv-2512-19134 — "improving EM by up to 14"
[^c13]: arxiv-2512-19134 — "even perfectly calibrated models must hallucinate"
[^c14]: arxiv-2512-19134 — "entities may co-occur with different relations or in unrelated contexts"
[^c15]: arxiv-2512-19134 — "59–68% involve wrong-relation hallucinations"
[^c16]: arxiv-2512-19134 — "false positive retrieval triggers when two genuinely"
[^c17]: arxiv-2512-19134 — "A corpus indexed at a particular point in time cannot provide meaningful"
[^c18]: arxiv-2512-19134 — "distill a specialized 0.5B model from GPT-4omini"
[^c19]: arxiv-2512-19134 — "as the default threshold"
[^c20]: arxiv-2512-19134 — "if the co-occurrence count falls below a threshold"
