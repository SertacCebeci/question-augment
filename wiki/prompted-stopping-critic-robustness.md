---
description: "A prompted self-critique stopping gate holds up when the retrieved evidence's order shifts; a fine-tuned lightweight stopping critic degrades, at far lower compute cost."
aliases: []
sources: ["arxiv-2604-19899"]
---
# Prompted stopping-critic robustness

> Two ways to decide "have I retrieved enough, or do I keep going" trade
> robustness for compute in opposite directions.

## Definition / Mechanism

The same job — deciding whether a multi-hop retrieval loop has gathered
enough evidence to stop and answer — is implemented two ways in
Iturra Bocaz & Galuščáková (2026)'s comparison: a small
classifier fine-tuned once on a fixed retrieval distribution to signal
sufficiency (SIM-RAG's critic), against a frozen LLM prompted at each turn
to critique its own candidate answer's coherence and completeness (MetaRAG's
Critic Module). The comparison holds the retriever and dataset fixed and
varies only the *ordering* of retrieved documents, by adding PointWise and
ListWise rerankers on top of the same retrieval-only pipeline.

Under that shift, the fine-tuned critic's accuracy drops while the prompted
critic's does not: "In contrast, MetaRAG conducts self-critique through
prompting rather than fine-tuning, making it more flexible and less
sensitive to such distributional changes, and thus better able to adapt to
varying retrieval conditions." Paired t-tests confirm the gap is not
uniform but is real in several settings: "Several settings show
statistically significant improvements in favor of MetaRAG (𝑝 < 0.05), as
indicated by the asterisks in Table 5, while other configurations are favor
SIM-RAG."[^c2]

The robustness is not free. Under identical retrieval-only conditions —
before rerankers are even introduced — the prompted critic already costs
far more per decision: "MetaRAG incurs substantially higher overhead across
both LLMs. It requires more model calls per question and exhibits
significantly higher token usage and latency than SIM-RAG, resulting in a
markedly higher overall cost in the GPT-3.5 setting."[^c3]

## Why it matters

Choosing how a stopping decision is implemented is itself a design choice
with a measured tradeoff axis, not just an accuracy number: a critic fit to
one input distribution (the fine-tuned classifier) is cheap per call but its
sufficiency judgment degrades when that distribution moves, e.g. when
upstream components like a reranker change what "the retrieved evidence"
looks like; a critic that reasons from the model's general competence (the
prompted judge) tolerates that shift but pays for it on every stopping
decision, not only on the ones where the distribution actually moved.

## Limits

- The distribution shift tested is exactly one kind — reranker-induced
  document reordering — not a new domain, retriever, or dataset; whether the
  same robustness gap holds under other shifts is unverified.
- SIM-RAG is evaluated as a released checkpoint, not reproduced from
  scratch here, so part of its measured brittleness could reflect that
  specific checkpoint rather than fine-tuned stopping critics in general
  (unverified).
- The comparison is symmetric in accuracy only in aggregate: some
  LLM × reranker configurations still favor SIM-RAG, so "prompted is more
  robust" is a tendency across settings, not a per-setting guarantee.

## Related

[[verification-aware-stopping]] · [[threshold-staleness]] · [[stopping-rules]] · [[self-answer-driven-search-depth]]

[^c2]: arxiv-2604-19899 — "Several settings show statistically significant improvements in favor of MetaRAG (𝑝 < 0.05), as indicated by the asterisks in Table 5, while other configurations are favor SIM-RAG."
[^c3]: arxiv-2604-19899 — "MetaRAG incurs substantially higher overhead across both LLMs. It requires more model calls per question and exhibits significantly higher token usage and latency than SIM-RAG, resulting in a markedly higher overall cost in the GPT-3.5 setting."
