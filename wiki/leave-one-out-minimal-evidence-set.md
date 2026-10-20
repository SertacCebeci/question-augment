---
description: "Greedy leave-one-out pruning keeps a passage only if removing it flips a judge's answer to wrong, giving a set minimal for that judge rather than for the whole pool."
aliases: ["greedy leave-one-out pruning", "minimal sufficient evidence set", "judge-minimal evidence subset", "golden evidence set"]
sources: ["arxiv-2512-14465"]
---
# Leave-one-out minimal sufficient evidence set

Given a question and a pool of retrieved passages, one can ask which passages the answer actually needs. The mechanism the paper uses to answer this is a greedy leave-one-out (LOO) search. Start from the full candidate pool. Take one passage out, have a generator answer from what is left, and have a judge score that answer against the gold answer. If the judge still marks the answer correct, the passage was redundant and is dropped for good. If the answer now fails, the passage stays. The loop repeats until no passage can be removed.[^c1] The result is a set that is minimal in a local sense: "a greedily minimal sufficient evidence set with respect to the judge", in which "would cause the model to fail the judge" is the condition that each remaining passage meets.[^c2]

The pipeline gates the search. Pairs whose full pool already fails the judge are discarded before any pruning, because "evidence does not support a correct answer even before pruning."[^c3] So a minimal set is only defined where the pool was sufficient to begin with.

The paper uses the output as supervision, not as a runtime procedure. The mined set becomes the target against which a learned selector is rewarded, and the stated purpose is to address sparsity: the introduction says the reinforcement learning methods it reviews rely on sparse rewards, "making it difficult to credit assignment to individual passages" and to suppress redundant content.[^c4] Dense supervision on the mined set is the paper's answer, "To alleviate reward sparsity and stabilize training".[^c5]

Two details matter for transfer. First, retrieval for mining uses "using BM25 on the concatenation of the query and answer",[^c6] so the gold answer shapes which passages enter the pool. At test time the picker's input is a query and a candidate pool, not the answer.[^c7] The mined set is therefore a target that was chosen with knowledge the selector does not have. Second, the judge is "an LLM-based judge J decides whether" the answer matches the reference,[^c8] so minimality is relative to that judge.

What survives the move out of this paper is the procedure's logic, which is independent of the reinforcement learning around it: a passage is evidence if and only if taking it away changes the answer's verdict. A reader of a cited source can apply the same test to the passages an answer relies on. That application is my inference; the paper does not test it on human readers.

The paper reports the downstream effect of the whole method, not of this step alone. Context-Picker "improves accuracy over strong RAG baselines on four out of five datasets."[^c9]

## Limits

- Minimality is relative to one generator and one judge. A judge error becomes a false "necessary" passage or a wrongly dropped one, and the text read reports no error rate for the judge.
- The search is greedy and, as I read the algorithm, order-dependent: the loop removes the first passage it can and then tests the rest against the reduced set. Passages that can substitute for each other are therefore resolved by iteration order, not by content. The paper does not test a different order. This is my inference from the algorithm.
- The result is not the smallest sufficient set in the pool. The paper says "greedily minimal", and no bound or comparison to an exhaustive search appears in the part read.
- The paper's ablations are on LoCoMo and cover the rationale, the redundancy term and the first stage.[^c10] None removes the LOO mining step, so its own contribution to the reported accuracy is not isolated.
- Pairs the pool cannot answer are dropped from training. The supervision therefore covers only questions the retrieval already handled, which the paper does not measure against the questions it drops.

## Related

- [[set-level-selection-over-relevance]] — the same complaint about per-item relevance ranking; there the missing property is coverage or non-redundancy scored by a rubric, here it is an answer's verdict under removal.
- [[dependency-closed-selection]] — also closes a selected set, but over a declared dependency graph rather than over a judge's answer.
- [[retrieval-depth-relative-to-relevant-count]] — the depth question that a minimal set answers per query instead of by a fixed K.
- [[minimal-sufficient-level-reward]] — a similar minimality penalty, applied to reasoning tiers rather than passages.
- [[loose-to-tight-redundancy-schedule]] — the training schedule that uses these mined sets as targets, relaxing the size margin first and tightening it second.

[^c1]: arxiv-2512-14465 — "If J still marks the answer as correct, we treat"
[^c2]: arxiv-2512-14465 — "a greedily minimal sufficient evidence set with respect to the judge"
[^c3]: arxiv-2512-14465 — "evidence does not support a correct answer even before pruning"
[^c4]: arxiv-2512-14465 — "making it difficult to credit assignment to individual passages"
[^c5]: arxiv-2512-14465 — "To alleviate reward sparsity and stabilize training"
[^c6]: arxiv-2512-14465 — "using BM25 on the concatenation of the query and answer"
[^c7]: arxiv-2512-14465 — "the retriever provides a candidate pool"
[^c8]: arxiv-2512-14465 — "an LLM-based judge J decides whether"
[^c9]: arxiv-2512-14465 — "improves accuracy over strong RAG baselines on four out of five datasets"
[^c10]: arxiv-2512-14465 — "we conduct ablations on the LoCoMo dataset"
