---
description: "Prompting a large LLM to write a pseudo-document is a strong query augmenter; on-policy RL wins only when tuned to one retriever and domain, and training pseudo-documents (OPQE) combines both."
aliases: ["SPQE vs DeepRetrieval", "OPQE", "on-policy pseudo-document query expansion", "prompting vs on-policy RL for query rewriting"]
sources: ["doi-10-48550-arxiv-2510-17139"]
---
# Prompted versus trained query augmentation

Rewriting a query before retrieval can be done two ways: ask an instruction-following LLM to write a hypothetical passage (SPQE, simple prompt-based pseudo-document expansion), or train a smaller policy with PPO against a retrieval reward to rewrite the query directly (DeepRetrieval, DR). Lin et al. (2026) compared them with extra inference compute deliberately given to prompting, so the budgets are closer.[^c1]

## What was measured

- Both beat no augmentation, but the benefit differs by task and retriever.[^c2]
- Trained policies can win: with a dense retriever, DR-7B averaged 57.5 against a base of 51.6, with FEVER rising from 75.8 to 85.5.[^c3]
- Prompting is competitive: for sparse retrieval SPQE gave the best averages on both evidence-based (78.2) and ad hoc (51.6) sets.[^c4]
- The hybrid, OPQE, trains the policy to generate pseudo-documents under a retrieval reward. OPQE-7B reached the best average, 58.1, in the setting reported.[^c5]

## Why each side wins (the authors' account)

Training adapts the policy to a specific retriever and domain, for instance learning financial terminology on FiQA. It costs more, needs labeled data for rewards, and may not improve: the tool-retrieval policy fell below no augmentation with dense retrievers.[^c6] Prompting is robust and cheap to set up, and the authors hypothesize three reasons: the LLM's internal knowledge bridges vocabulary mismatch for BM25; a passage specifies an underspecified short query better; and a pseudo-document sits closer to the passage-level text dense retrievers were trained on.[^c7] These are hypotheses, not isolated by ablation here.

Cost differs in shape: RL pays up front and amortizes over queries, prompting pays per query. RL may be cheaper at high throughput on a fixed corpus; prompting suits shifting domains or little compute.[^c8]

## Limits

- Only PPO was tested; group-based on-policy methods such as GRPO were left out.[^c9]
- The three reasons for prompting's strength are conjectures of the authors.
- Results are on the authors' chosen benchmarks and model sizes; the compute equalization is approximate.
- Outcomes depend on retriever type, so no universal ranking holds; the authors state they do not claim one.

## Related

- [[cross-retriever-reformulation-gain]] — gains from reformulation vary by retriever, as here
- [[corpus-grounded-one-shot-query]] — another way to make a single query strong without training
- [[hypothesis-conditioned-query-rewriting]] — rewriting conditioned on a generated hypothesis
- rewrite-retrieve-read — the same trained-rewriter choice, but rewarded mainly by a frozen reader's answer score, with a retrieval-hit term added

[^c1]: doi-10-48550-arxiv-2510-17139 — "we intentionally allocate more inference-time compute to prompting by using larger LLMs"
[^c2]: doi-10-48550-arxiv-2510-17139 — "but their benefits differ across tasks and retrievers."
[^c3]: doi-10-48550-arxiv-2510-17139 — "the DR-7B (DeepRetrieval) model achieves the highest average score of 57.5"
[^c4]: doi-10-48550-arxiv-2510-17139 — "SPQE consistently delivers the best performance"
[^c5]: doi-10-48550-arxiv-2510-17139 — "the OPQE-7B model achieves the best average score of 58.1"
[^c6]: doi-10-48550-arxiv-2510-17139 — "our ToolRetrieval policy underperforms no query augmentation setting with dense retrievers"
[^c7]: doi-10-48550-arxiv-2510-17139 — "We hypothesize that its effectiveness stems from three factors."
[^c8]: doi-10-48550-arxiv-2510-17139 — "Our paper does not claim one paradigm is universally"
[^c9]: doi-10-48550-arxiv-2510-17139 — "We did not include group-based on-policy RL algorithms"
