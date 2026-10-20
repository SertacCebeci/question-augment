---
description: "Writing an ordered sub-question plan before any retrieval anchors each search to a fixed sub-question, so queries stop drifting under partially relevant documents retrieved earlier."
aliases: ["plan-first search", "PL-Search", "global plan before retrieval", "cross-hop query drift", "plan-based retrieval", "outline-conditioned query generation"]
sources: ["doi-10-48550-arxiv-2605-28354", "doi-10-48550-arxiv-2408-10490", "arxiv-2602-00007"]
---
# Plan-before-search anchoring

A reactive search agent forms each query from the documents it has just retrieved. Noisy or partially relevant documents pile up along the trajectory, and the queries slide away from the original question.[^c1] The plan-before-search behavior (PL-Search) changes the order. The agent first writes an ordered list of sub-questions as a global plan, with no retrieval yet. Each later think-search-refine step then names the plan step it serves and issues a short query for that step only.[^c2]

The anchor is the fixed sub-question. Under it, a query is checked against a stable target and not against whatever the last retrieval happened to surface. The paper's worked failure case shows the unplanned alternative. Two hops are fused into one query, the query matches neither sub-question cleanly, and retrieval lands on adjacent award years.[^c3]

The same order appears in long-form writing, where the plan is an outline of paragraphs. Godbole et al. first "write a list describing what paragraphs should be produced", conditioned on an initial search, and then "generate search queries from the paragraph descriptions".[^c6] Their ablation drops the outline and writes queries from the initial results alone. The ablated run is less attributable, and the authors read this as the outline's effect on the queries: "blueprint generation improves the utility of subsequently generated queries."[^c7] The same paper finds that the final prompt matters less than the evidence it brings in: "the outline-based retrieved information procured by Plan-Based Retrieval that leads to improvements in attribution."[^c8] The gain is measured as attribution to sources in biographies and event summaries, not as answer accuracy.

The paper trains this behavior with a reward that scores two things. One is the structural validity of the plan. The other is the alignment between each reasoning step and its planned sub-question.[^c4]

A plan only helps if later steps can revise it against evidence. Pre-written sub-questions must stay consistent with what is retrieved, which requires an earlier "refine" skill (summarizing evidence for the current step). Models that lacked this skill collapsed when plan was trained first.[^c5] This makes plan-before-search a behavior that depends on other skills, not a free prompt trick.

## Limits

- The evidence is multi-hop QA over a Wikipedia-style retriever with open models of 3B to 14B parameters. Nothing here tests open-ended or ambiguous questions, or a plan that must change when early evidence contradicts it. The paper only says refine lets the model keep sub-questions consistent.
- The drift mechanism is stated by the authors and shown in case studies. I did not read a measurement isolating drift as the cause of the accuracy gain, so "anchoring causes the gain" is the authors' account, not a tested result.
- The plan is fixed up front. How much a wrong initial decomposition costs was not established in the slices I read.
- The result is entangled with the training recipe (RL plus SFT). It does not show that prompting alone gives the same effect.
- The outline-based result is a different task and metric: zero-shot prompting of instruction-tuned LLMs, long-form biographies and event summaries, scored by attribution (AIS) rather than answer accuracy. The two results agree in direction only; the outline's effect is not measured as a cause of any QA gain (my inference).

## Related

- [[self-ask-decomposition]] — emits sub-questions one at a time, mid-trajectory, instead of a whole plan before search
- [[decomposer-planner-centric-rl]] — RL that trains the decomposing role
- [[dependency-aware-subquestion-scheduling]] — ordering sub-questions by dependency, which the plan's "ordered" list presupposes
- [[premature-closure]] — another way an agent's trajectory settles on the wrong path
- plan-level-self-correction — a proposed answer to the untested case above: after repeated step failures the plan is discarded and rewritten, with the gathered facts kept. The gain is measured only for the whole system, not for the replan alone

[^c1]: doi-10-48550-arxiv-2605-28354 — "accumulates noise and causes trajectories to drift."
[^c2]: doi-10-48550-arxiv-2605-28354 — "anchoring each retrieval step to a pre-designed subquestion"
[^c3]: doi-10-48550-arxiv-2605-28354 — "prevents cross-hop query drift."
[^c4]: doi-10-48550-arxiv-2605-28354 — "plan-aware"
[^c5]: doi-10-48550-arxiv-2605-28354 — "Models that lack the refine sub-skill also fail"
[^c6]: doi-10-48550-arxiv-2408-10490 — "We first prompt the model to write a list describing what paragraphs should be produced"
[^c7]: doi-10-48550-arxiv-2408-10490 — "blueprint generation improves the utility of subsequently generated queries"
[^c8]: doi-10-48550-arxiv-2408-10490 — "the outline-based retrieved information procured by Plan-Based Retrieval that leads to improvements in attribution"
