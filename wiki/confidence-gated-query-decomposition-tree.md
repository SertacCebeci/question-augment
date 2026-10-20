---
description: "A three-way node rule (answer if token-probability confidence passes a threshold, else split into two sub-queries, else extract entities) prunes drift in multi-hop retrieval and cuts retrievals."
aliases: ["PruneRAG", "confidence-guided query decomposition tree", "answer-or-decompose-or-retrieve node rule"]
sources: ["arxiv-2601-11024"]
---
# Confidence-gated query decomposition tree

Multi-hop questions are usually answered by decomposing them. Sequential decomposition lets a wrong intermediate answer propagate into the final one, and unconditional decomposition produces redundant sub-queries. Shuguang et al. (PruneRAG) make each node of a decomposition tree choose among three outcomes, with the model's own answer confidence deciding whether decomposition is needed at all.

## Mechanism

Each node holds a query, retrieved context and the parent query. A first layer asks whether the retrieved context supports a direct answer; if so the node is an "answer" leaf. If not, a second layer asks whether the query can be split into two sub-queries, giving a "query" node whose children are processed recursively. If it can be neither answered nor split, key entities are extracted and used for retrieval, giving an "entity" leaf.[^c1]

The gate on the first layer is the geometric mean of the answer's token probabilities, exp of the mean token log-probability given the query and context. An answer above the threshold tau_A is accepted and expansion stops. Below it the answer is rejected and the node decomposes or falls back to entity retrieval.[^c2] The reported setting is maximum depth 3 and tau_A = 0.95, and the authors report that tau_A in [0.9, 0.95] performs consistently well on HotpotQA and 2WikiQA.[^c3] The statistic is the same one as in [[sequence-likelihood-confidence]], used here as a per-node stop rule rather than a final abstention gate.

After construction, a bottom-up pass returns the stored answer for answer nodes, aggregates children for query nodes, and summarizes retrieved documents for entity nodes.[^c4]

## What was measured

Ablations remove one part at a time: confidence pruning, the answer branch, the entity branch, and adaptive expansion (decompose unconditionally). Each removal degraded performance. Removing adaptive control hurt most on most datasets, because uncontrolled decomposition generates redundant sub-queries. Removing the answer branch raised retrieval calls. Removing confidence pruning raised the [[evidence-forgetting-rate]].[^c5] The authors also claim an average 5.45% F1 gain over the strongest baseline and a 4.9x speedup against mainstream multi-retrieval baselines.[^c6]

## Limits

- The ablation variants overlap: w/o Answer and w/o Adaptive also remove the pruning mechanism, so the effect of confidence alone is not cleanly isolated; the paper itself notes this.[^c5]
- Whether a question is answerable or splittable is itself an LLM judgment, so the first two layers are not independently validated. That is my observation.
- Token-probability confidence is weak at ranking correct answers in other settings (see [[sequence-likelihood-confidence]]); the 0.95 threshold was tuned on the benchmarks reported, and transfer to other models or tasks is untested here.
- Requires access to token log-probabilities, so API-only models are excluded.
- Evaluated on multi-hop Wikipedia-style QA only; the speed and F1 figures are the authors' own comparison.

## Related

- [[sequence-likelihood-confidence]] — the same confidence statistic and its weakness as an abstention gate
- [[evidence-forgetting-rate]] — the diagnostic metric this method targets
- [[dual-threshold-risk-controlled-early-exit]] — another threshold rule that stops computation early
- [[recoverability-aware-selective-escalation]] — decides when to escalate rather than answer

[^c1]: arxiv-2601-11024 — "the system executes a semantic abstraction strategy by extracting"
[^c2]: arxiv-2601-11024 — "If Confidence(𝐴) is greater than the threshold 𝜏𝐴 , the decision mechanism accepts the answer"
[^c3]: arxiv-2601-11024 — "The results demonstrate that the threshold range 𝜏𝐴 ∈ [0.9, 0.95] consistently"
[^c4]: arxiv-2601-11024 — "This backtracing mechanism aggregates evidence, helping to"
[^c5]: arxiv-2601-11024 — "Eliminating adaptive control produces the"
[^c6]: arxiv-2601-11024 — "achieving a 4.9×"
