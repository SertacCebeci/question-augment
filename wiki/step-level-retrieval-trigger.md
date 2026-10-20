---
description: "Retrieval inside a reasoning chain fires at the step where that step's own uncertainty score is high, not once before generation; random triggering costs 8.5% F1 on multi-hop QA."
aliases: ["RSUS-triggered retrieval", "Reasoning Step Uncertainty Score", "mid-reasoning retrieval trigger", "step-granularity retrieval gate"]
sources: ["doi-10-1145-3805712-3809722"]
---
# Step-level retrieval trigger

Outside evidence can be fetched in the middle of a reasoning chain instead of once before it starts. The usual retrieve-then-generate pipeline runs a single search up front. For a large reasoning model that writes 12K to 25K tokens, the paper's argument is that this timing is wrong, since the gaps arise mid-inference and cannot be known at query time.[^c1][^c15] The step-level trigger keeps the chain, scores each reasoning step for how much it needs knowledge the model does not hold, and searches only at the steps whose score is high.

The score is the paper's Reasoning Step Uncertainty Score, RSUS: a weighted sum over each reasoning step of three terms, a verbalized uncertainty, an entropy term and a consistency term.[^c2] The three were chosen partly for cost: semantic entropy or self-consistency costs 5 to 20 times the reasoning inference, and the authors also argue the three signals are complementary.[^c3][^c16] The weights are fit on a validation set "to maximize the correlation between RSUS and downstream retrieval benefit".[^c4] A separate learned policy then decides whether to retrieve, what query to formulate and how to integrate the result, conditioned on the reasoning so far.[^c5] The score answers where to look; the policy answers whether to look now.

The reported headline is an average of 10.1% absolute F1 over standard RAG on MuSiQue, HotpotQA and 2WikiMultiHopQA, and "reducing retrieval calls by 47% compared to fixed-interval" approaches such as IRCoT.[^c6][^c17] Two comparisons bear on the trigger itself rather than on the search. Replacing the learned trigger with random triggering "degrades F1 by 8.5%", and the authors read this as "demonstrating that when to retrieve matters substantially".[^c7][^c18] A learned threshold also beats a fixed one, "outperforms fixed threshold", by 2.3% F1.[^c8] The gain over IRCoT grows with hop count, from +3.2% F1 on 2-hop to +8.4% on 4-hop questions. The authors tie this to step-level detection: it "identifies the specific reasoning step where" the gaps occur, so retrieval lands where the chain needs it.[^c9][^c19]

## Limits

- The evidence is three multi-hop QA sets over Wikipedia-style corpora. Nothing here tests open-ended reasoning, code, or any task where the missing knowledge is not a fact in a document. Whether a per-step uncertainty score transfers to those is my inference, not a result.
- The trigger over-fires. The paper reports that "RSUS occasionally triggers retrieval during exploratory reasoning phases", which it counts as about 31% of its failure cases, and that this disrupts productive chains.[^c10]
- Retrieval itself can mislead. "When relevant information is absent, retrieval" wastes time and "may introduce noise (14% of" out-of-domain retrievals return misleading information.[^c11][^c20]
- The overhead is not zero: "RSUS computation add 8% inference overhead, with no benefit for" queries that need no retrieval.[^c12]
- The learned parts are costly to build. "The policy requires 19,938 training examples," and the paper says 5K to 10K may suffice on other benchmarks.
- Repeated injection degrades the score: segmentation and RSUS are "robust against one prior retrieval but degrade after ≥ 3 injections;".[^c13]
- The method depends on token-level access. Completion-only models score "2–3% F1 lower" because "open-weight models where richer uncertainty signals are available" allow stronger signals.[^c14][^c21]
- The uncertainty is the model's own. A step can be confidently wrong and never reach the trigger; the paper does not measure this miss rate. The search query is also the model's own, formed from its reasoning, and no person is asked anything. Both points are my reading of the design, not a finding.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the same retrieve-or-not decision, but taken once before drafting on the whole query's likelihood; this note moves it inside the chain and per step
- [[chain-of-thought-interleaved-retrieval]] — IRCoT retrieves at every sentence on a fixed schedule; the trigger here asks which step, and the paper reports 1.8 calls against IRCoT's 3.4 on MuSiQue
- [[boundary-novelty-retrieve-or-think-gate]] — a mid-trace retrieve-or-think gate, but on embedding novelty against the evidence already held rather than on step uncertainty
- [[stop-continue-criteria-in-retrieval-loops]] — the stop side of the same loop, which this paper does not treat
- [[evidence-gap-state]] — tracks what evidence is still missing as an explicit state, a rival to a per-step uncertainty score

[^c1]: doi-10-1145-3805712-3809722 — "reasoning models encounter knowledge gaps during 12K–25K token chains"
[^c2]: doi-10-1145-3805712-3809722 — "We define the Reasoning Step Uncertainty Score (RSUS), a composite measure identifying when a reasoning step requires external"
[^c3]: doi-10-1145-3805712-3809722 — "whereas semantic entropy or selfconsistency cost 5–20× inference"
[^c4]: doi-10-1145-3805712-3809722 — "to maximize the correlation between RSUS and downstream retrieval benefit"
[^c5]: doi-10-1145-3805712-3809722 — "that decides whether to retrieve, what query to formulate, and how to integrate"
[^c6]: doi-10-1145-3805712-3809722 — "achieves on average 10.1% absolute improvement in answer F1"
[^c7]: doi-10-1145-3805712-3809722 — "Random triggering degrades F1 by 8.5%"
[^c8]: doi-10-1145-3805712-3809722 — "The learned threshold outperforms fixed threshold"
[^c9]: doi-10-1145-3805712-3809722 — "+3.2% F1 on 2-hop, +5.8% on 3-hop, and +8.4% on 4-hop questions"
[^c10]: doi-10-1145-3805712-3809722 — "RSUS occasionally triggers retrieval during exploratory reasoning phases"
[^c11]: doi-10-1145-3805712-3809722 — "When relevant information is absent, retrieval"
[^c12]: doi-10-1145-3805712-3809722 — "RSUS computation add 8% inference overhead, with no benefit for"
[^c13]: doi-10-1145-3805712-3809722 — "robust against one prior retrieval but degrade after ≥ 3 injections;"
[^c14]: doi-10-1145-3805712-3809722 — "Completion-only models: Performance is 2–3% F1 lower than"
[^c15]: doi-10-1145-3805712-3809722 — "gaps that cannot be anticipated at"
[^c16]: doi-10-1145-3805712-3809722 — "the three signals are complementary"
[^c17]: doi-10-1145-3805712-3809722 — "reducing retrieval calls by 47% compared to fixed-interval"
[^c18]: doi-10-1145-3805712-3809722 — "demonstrating that when to retrieve matters substantially"
[^c19]: doi-10-1145-3805712-3809722 — "uncertainty detection identifies the specific reasoning step where"
[^c20]: doi-10-1145-3805712-3809722 — "may introduce noise (14% of"
[^c21]: doi-10-1145-3805712-3809722 — "open-weight models where richer uncertainty signals are available"
