---
description: "Best-of-K recall of a correct SQL query can sit far above the accuracy a selector reaches from the same candidates: 77.8% recall against 62.78% execution accuracy at K=30 on BIRD dev."
aliases: ["selection gap", "recall-accuracy gap", "candidate recall versus selected accuracy", "best-of-K ceiling gap", "Pass@K versus Pass@1 gap", "path selection bias"]
sources: ["arxiv-2512-18622", "arxiv-2512-06258"]
---
# Candidate selection gap

When a generator returns several candidate answers and a separate selector picks one, two numbers can be measured apart. The first is the recall of the candidate set: the share of questions for which at least one candidate is correct. The second is the accuracy of the pick. The recall is an upper bound on the accuracy, and the difference between them is the part of the error that belongs to the selector rather than to the generator.

The paper's case is MATS, a Text2SQL system built from small language models. In its framework "the Planner produces" several SQL queries per question, and a Selection Agent chooses among them.[^c9] The Selection Agent "is an SLM that chooses the best SQL query," and it does so "from multiple candidates based on the responses obtained when evaluating them over the database."[^c1][^c2]

The recall is defined as an upper bound: "The upper bound represents the recall, indicating the maximum possible" accuracy, reached if the correct query is always in the candidate set.[^c3] The measured numbers on BIRD dev are "While recall reaches 77.8% at" K = 30, and the pick reaches only 62.78%, "highlighting a gap between potential and actual execution" accuracy.[^c4][^c5]

Raising the number of candidates lifts the ceiling but not the pick at the same rate. The paper reports that "accuracy of MATS does not consistently follow the" same trend as recall.[^c6] The authors' explanation is that "The reason is likely that more incorrect SQL queries" enter the pool, so the selector has more wrong options to choose from.[^c7] That is their hypothesis. The text does not test it.

My reading, which is an inference and not a result of the paper, is that two mechanisms could produce the gap and the text cannot separate them. Either the pool grows more wrong options as K rises, which dilutes a selector that is working, or the selector cannot tell a correct query from a plausible wrong one even when the correct one is present. Those two readings predict different things: the first says a better selector recovers most of the gap, the second says the gap is a ranking limit that more candidates cannot close.

What survives the transfer to other generate-and-select pipelines is the arithmetic. The accuracy of such a pipeline is bounded by the recall of its pool, and the distance below that bound is set by the selector against the pool, not by K alone. What does not survive is any size for the gap: it is one pair of numbers from one system on one dev set.

The same gap appears when the candidates are not produced by a planner but are one policy's own samples, and the pick is the answer that policy commits to. arxiv-2512-06258 names it path selection bias: a large-K Pass@K set against a Pass@1 is read as "failures primarily stem from misreasoning rather than ignorance".[^c10] Here the selector is not a second model but the policy's own distribution over reasoning chains. The paper's remedy works on that distribution rather than adding a selector: a thinking reward in which the base model is "a self-rewarding mechanism that leverages the base" judge of chain quality, and a memory of low-reward chains that are "repeatedly sampled as hard negatives in subsequent training".[^c11][^c12] The authors report that the gap between the trained model and the baseline grows as the sampling budget rises, "with increasing sampling budget, evidenced by superior" Pass@128 scores, "Pass@128 scores on both MMBench and MMStar".[^c13][^c14] They read the widening as a change in the pool, not only in the pick: "PSO not only elevates the top-ranked reasoning path but systematically restructures the underlying" trajectory distribution.[^c15] The MATS numbers cannot test that claim, since they fix one pool and move only K. What transfers is the decomposition: the gap belongs to the candidate pool and to the pick together, and training on the pool can move the ceiling itself. Whether pool or pick carries more of the gap is not separated in the parts of the paper read (my reading).

## Limits

- One system (MATS), one benchmark split (BIRD dev), and one range of K (up to 30). The 77.8% and 62.78% are single figures in the text, not a curve with error bars.
- The paper says that even at temperature 0.0 "the results remain slightly non-deterministic due" to sampling,[^c8] so the gap is measured with some run-to-run noise that the text does not quantify.
- Correctness of a candidate is the execution match with the gold query. Execution match can accept a query that returns the right rows for the wrong reason, and it can reject a correct query that returns the rows in another form. The gap is measured against that label.
- The authors give a reason for the gap but do not test it. No experiment varies the selector while holding the pool fixed, or varies the pool's wrong-answer share while holding the selector fixed.
- The text does not report how the selector's accuracy changes with K beyond the two endpoints shown here, so the shape of the gap is not established.
- The path-selection reading comes from a second paper, and its evidence is thinner than the MATS pair. Its disparity is asserted across "numerous models" in the abstract, and the parts read give no Pass@1 and Pass@K table to check its size.[^c18] Its Pass@k comparison is one model on two benchmarks.[^c17] A large K can hit a correct answer by chance, especially on multiple-choice items, so a Pass@K gap alone does not show that the model knows the answer (my inference).
- The thinking reward that reshapes the pool is scored by the base model itself, and the authors name this as a limit: "the current thinking reward relies on self-evaluation from the base model".[^c16] A chain can look stable under its own model's judgment and still be wrong; the parts read give no stability measure the model does not supply (my reading).

## Related

- [[generate-then-verify-candidate-pipeline]] — the same generate-then-filter shape; there a verifier only filters what the generator produced, so recall is capped by the generator.
- [[black-box-correctness-ceiling]] — correctness rankers for text-to-SQL that stay in a narrow band; a weak ranking signal is one plausible source of a selector shortfall (my inference, not tested in this paper).
- [[rewriting-repairability-ceiling]] — another best-of-K upper bound, here on rewrites rather than on SQL candidates.
- [[execution-verified-preference-pairs]] — the same paper's use of execution results, here to train the generator rather than to pick among its outputs.
- [[population-search-under-noisy-verifier]] — the same best@K-versus-pass@1 gap closed by a verifier-scored search over candidate proofs, not by training the sampler.

[^c1]: arxiv-2512-18622 — "The Selection Agent is an SLM that chooses the best SQL query"
[^c2]: arxiv-2512-18622 — "from multiple candidates based on the responses obtained when"
[^c3]: arxiv-2512-18622 — "The upper bound represents the recall, indicating the maximum possible"
[^c4]: arxiv-2512-18622 — "While recall reaches 77.8% at"
[^c5]: arxiv-2512-18622 — "62.78%, highlighting a gap between potential and actual execution"
[^c6]: arxiv-2512-18622 — "accuracy of MATS does not consistently follow the"
[^c7]: arxiv-2512-18622 — "The reason is likely that more incorrect SQL queries"
[^c8]: arxiv-2512-18622 — "temperature 0.0, the results remain slightly non-deterministic due"
[^c9]: arxiv-2512-18622 — "the Planner produces"
[^c10]: arxiv-2512-06258 — "failures primarily stem from misreasoning rather than ignorance"
[^c11]: arxiv-2512-06258 — "a self-rewarding mechanism that leverages the base"
[^c12]: arxiv-2512-06258 — "repeatedly sampled as hard negatives in subsequent training"
[^c13]: arxiv-2512-06258 — "with increasing sampling budget, evidenced by superior"
[^c14]: arxiv-2512-06258 — "Pass@128 scores on both MMBench and MMStar"
[^c15]: arxiv-2512-06258 — "PSO not only elevates the top-ranked reasoning path but systematically restructures the underlying"
[^c16]: arxiv-2512-06258 — "the current thinking reward relies on self-evaluation from the base model"
[^c17]: arxiv-2512-06258 — "Comparison of Pass@k performance on MMBench and MMBench-Star for Qwen2.5VL-7B-Instruct before and after PSO"
[^c18]: arxiv-2512-06258 — "The substantial disparity between Pass@K (with large K) and Pass@1 across"
