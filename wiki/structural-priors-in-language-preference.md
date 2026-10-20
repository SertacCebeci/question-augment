---
description: "Benchmark evidence distribution (exposure, gold availability, topic locality) inflates measured language preference in multilingual RAG, so English dominance may not be model bias."
aliases: ["gold availability prior", "exposure bias in multilingual retrieval", "topic locality prior", "cultural prior", "evidence-distribution confound in language preference"]
sources: ["arxiv-2601-02956", "arxiv-2512-05959"]
---
# Structural priors in language preference

A multilingual retrieval-augmented system can look as if it prefers English. The question is whether that preference lives in the model or in the data the benchmark puts in front of it. The paper's claim is that, in measured mRAG preference, much of it is the data. Its experiments use MKQA queries aligned to KILT, BGE-m3 as retriever and re-ranker, and Wikipedia editions in English and the query's local language as the corpus.[^c1] Under that setup the authors read the English lead as a product of three structural priors, not of the encoder's linguistic intent.[^c2]

## The three priors

**Exposure.** The retrieval system surfaces documents from the larger corpus whatever the query language. The paper defines exposure bias as the retriever's "tendency to surface documents from more prevalent languages regardless of the query" language.[^c3] English Wikipedia is much denser, so the top-50 pool is dominated by English documents. The exposure prior is estimated as the average share of each document language among the top-50 candidates for queries in a given language.

**Gold availability.** For most benchmark queries the answer-bearing passage exists only in English. The authors state the consequence directly: "English pivoting appears effective not because models prefer" English.[^c4] The table of gold coverage shows the imbalance. In my reading of its ratio column, English has a gold-present ratio of 73.29 %, while the other six languages sit between about 0.5 % and 1.4 %. (That reading is mine; the paper's text is the claim.)

**Topic locality (cultural prior).** Some queries name a place, title, or script that is native to one language. Those surface forms act as retrieval anchors. In the paper's words, "locale-tied queries contain native surface forms that act as structural anchors, naturally pulling retrieval toward the corresponding" local-language evidence.[^c5] For queries whose predicted locale is not English, about 20 % have gold pages only in the local Wikipedia, which is why the paper treats locale-tied queries as a separate confound.[^c6]

## What the confound does

Taken together, the authors say the measured English preference is inflated. The abstract puts it as the measurements being "significantly distorted by structural priors" in evaluation benchmarks.[^c7] The conclusion restates it: gains from English pivoting "stem from retrieval-side evidence imbalance, which biases preference measurements."[^c8] Their Table 4 reports that the raw preference score (MLRS) correlates strongly with all three priors, which is the basis for calling the raw score prior-driven.

The consequence for asking and answering is that a benchmark which concentrates gold evidence in one language will reward routing every query through that language, and will show this as a model preference. The cheap diagnostic is to check where the gold passages live before reading a language gap as the model's.

## Limits

- The paper measures retriever-level preference. Generator-level preference is not removed: "our debiasing targets retriever-level preference, while generator-level preference can still remain."[^c9]
- The priors are estimated on one benchmark subset: "we use a 2.7K-example subset that overlaps with" KILT NQ.[^c10] Whether the same decomposition holds on other corpora is not shown; the authors say "Evaluating DeLP and DELTA on broader," domain-specific corpora is needed.[^c11]
- The cultural prior depends on an LLM classifier that assigns each query a single locale language. Its error rate is not evaluated in the text I read.
- The list of priors is a modelling choice. Nothing here shows the three named priors are the complete set of confounds.
- The priors explain the retriever's side only. With the evidence's content held fixed by translation, a multimodal VQA benchmark still shows the answerer failing on non-English evidence: "cross-lingual evidence integration is a deeper bottleneck than instruction following."[^c12] That is a generator-side effect the priors do not reach; see [[evidence-language-integration-gap]].

## Related

- [[debiased-language-preference]] — the regression that removes these priors from the raw score
- [[monolingual-query-document-alignment]] — the residual preference that remains once they are removed
- [[embedding-retriever-position-bias]] — another retriever measurement where a nuisance variable (document length) must be held fixed before the effect is read
- [[embedding-retrieval-literal-token-anchoring]] — retrievers ranking by literal surface tokens; a plausible route by which native-script anchors pull retrieval (my inference, not tested here)

[^c1]: arxiv-2601-02956 — "BGE-m3 (Chen et al., 2024) as the multilingual retriever and re-ranker."
[^c2]: arxiv-2601-02956 — "retrieval-side structural biases rather than any inherent linguistic preference of the model."
[^c3]: arxiv-2601-02956 — "tendency to surface documents from more prevalent languages regardless of the query"
[^c4]: arxiv-2601-02956 — "English pivoting appears effective not because models prefer"
[^c5]: arxiv-2601-02956 — "locale-tied queries contain native surface forms that act as structural anchors, naturally pulling retrieval toward the corresponding"
[^c6]: arxiv-2601-02956 — "about 20% of these queries have gold pages"
[^c7]: arxiv-2601-02956 — "are significantly distorted by structural priors"
[^c8]: arxiv-2601-02956 — "in mRAG stem from retrieval-side evidence imbalance, which biases preference measurements."
[^c9]: arxiv-2601-02956 — "our debiasing targets retriever-level preference, while generator-level preference can still remain."
[^c10]: arxiv-2601-02956 — "we use a 2.7K-example subset that overlaps with"
[^c11]: arxiv-2601-02956 — "Evaluating DeLP and DELTA on broader,"
[^c12]: arxiv-2512-05959 — "cross-lingual evidence integration is a deeper bottleneck than instruction following"
</content>
