---
description: "Checking an LLM relevance judge's highlighted passages against human highlights shows it can be right about the document yet wrong about where the answer is, worst for small or scattered passages."
aliases: ["right for the right reasons relevance assessment", "LLM passage highlighting as assessor", "rationale-based assessor evaluation"]
sources: ["arxiv-2601-08919", "arxiv-2511-21401"]
---
# Rationale-level relevance judging

A document-level relevant/non-relevant label from an LLM assessor says nothing about whether the model found the part of the document that answers the query. The study uses the INEX 2009 and 2010 Wikipedia collections, where human assessors highlighted "all passages within a document that respond to the information need", and asks LLMs for the same highlights under few-shot prompting.[^c1] The highlighted spans are treated as rationales, and are scored against the human spans by character-level precision, recall and F1. This makes "right for the right reason" measurable: a judge is credited only if its evidence overlaps the human evidence.

## What was measured

**Document level.** On non-relevant documents, Llama-3.1-8B was worse than random, with accuracy 0.30 for the top-100 ranked non-relevant pages of INEX 2009, rising to 0.48 for ranks 700-800. GPT-4.1-mini and GPT-4o-mini scored 0.78 to 0.90.[^c2] More capable models were more conservative about calling a document relevant.[^c3] The small model's false positives correlated only weakly with BM25 overlap with the query (Spearman 0.26 and 0.28), so lexical cues do not explain them.[^c4]

**Rationale level.** The smaller model's recall exceeded its precision because it over-highlighted. It marked more than half the document in 80.7% of INEX 2009 cases, and a model that marks everything gets recall 1.0 trivially.[^c5] Moving to GPT-4.1-mini raised micro precision on INEX 2009 from 0.5226 to 0.6185.[^c6] Even the larger model produced longer spans than the human's for about 72% of documents on INEX 2010, with average recall 0.836.[^c7] Recall alone therefore flatters the judge; precision is the informative figure.

**Where it fails.**
- Small passage in a long document ("needle in a haystack"): precision drops when only a small fraction of the document is relevant, especially for longer documents.[^c8]
- Several separate relevant passages: on INEX 2009 with Exemplar2, GPT-4.1-mini reached macro precision 0.4951 on discontiguous cases against 0.6163 on contiguous ones.[^c9]
- Hard cases: on pairs where all six model/exemplar configurations scored at most 0.2 precision, the added GPT-4o-mini reached 0.19 to 0.25 on INEX 2009, so a stronger model helps only a little.[^c10]
- Exemplar choice matters differently by model. Exemplar2 (longer example documents) was best for the small model, but the larger model did as well or better with Exemplar1 or Exemplar3.[^c11]

The authors conclude that LLMs can cut human effort but "cannot replace humans as assessors".[^c12]

## Limits

- Two Wikipedia collections, three models (Llama-3.1-8B, GPT-4.1-mini, GPT-4o-mini), k=6 few-shot exemplars; no newer or larger judges.
- Document-level accuracy tables are single data points, so the authors say significance tests cannot be applied to them.
- Human highlights are the reference, but how consistent human assessors are with each other was not measured here, so low precision may partly reflect human-side disagreement (my inference).
- The effect of highlight length on scores is confounded with precision; over-highlighting inflates recall and the authors do not test a length-controlled score.
- No downstream test of how rationale errors change system rankings; the document-level ranking literature cited reports high Kendall tau, which this paper does not reproduce.
- The human-side question above is partly answered by a later span-level study on Czech and Slovak claims: two annotators labelling the same claim evidence reach a token-level F1 of 48 under one-to-one matching.[^c13] Read against that ceiling, a judge's F1 near 0.5 is close to human agreement, a different reading from the precision figures above. That study's task (fact-checking evidence, not relevance) and language differ, so the transfer is my inference. Its one-to-one matching also means a longer set of spans is not penalised for exhaustiveness, which the character-level precision used here does not do.[^c14]

## Related

- [[llm-judge-biases]] — document-level biases of LLM judges; this note asks about the evidence behind a verdict instead
- [[dispersed-evidence-retrieval-collapse]] — scattered evidence defeats retrieval; here scattered passages defeat the judge
- [[llm-filtered-pseudo-relevance-feedback]] — an LLM relevance filter in retrieval, where the same document-level errors would enter

[^c1]: arxiv-2601-08919 — "to highlight all passages within a document that respond to the"
[^c2]: arxiv-2601-08919 — "The results are worse than random for Llama-3.1-8B model, which"
[^c3]: arxiv-2601-08919 — "increasingly capable models are more conservative when predicting relevance."
[^c4]: arxiv-2601-08919 — "false-positive predictions by"
[^c5]: arxiv-2601-08919 — "This observation indicates a tendency of the model to overhighlight document content, thereby inflating recall scores."
[^c6]: arxiv-2601-08919 — "0.5226 to 0.6185 (an 18.3% increase)"
[^c7]: arxiv-2601-08919 — "the average recall in this setting"
[^c8]: arxiv-2601-08919 — "where the model struggles to identify the small relevant"
[^c9]: arxiv-2601-08919 — "We observe that LLMs tend to struggle"
[^c10]: arxiv-2601-08919 — "stronger reasoning capabilities can improve precision even on challenging cases."
[^c11]: arxiv-2601-08919 — "Exemplar1 and Exemplar3"
[^c12]: arxiv-2601-08919 — "they cannot replace humans as assessors"
[^c13]: arxiv-2511-21401 — "The average F1-score between two annotators is 48"
[^c14]: arxiv-2511-21401 — "degree of exhaustiveness, we use the Hungarian matching algorithm"
