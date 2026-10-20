---
description: "A rubric built from two tracks, atomic facts from retrieved evidence and interaction-level constraints read from the query; removing the interaction track cost the most measured coverage."
aliases: ["dual-track constraint construction", "interaction-level constraints", "interaction-intent module", "dynamic atomic dual-track scheme"]
sources: ["doi-10-48550-arxiv-2601-15161"]
---
# Dual-track rubric constraints

A rubric for one query can draw its criteria from two sources that are decomposed separately and merged afterwards. The first is the evidence. Retrieved medical text is split into atomic facts, "atomic medical facts F (the Reference Board) including declarative assertions, contraindications," and safety-critical red flags.[^c1] The second is the query's interaction level: the constraints a patient's message carries beyond the information it asks for, "interaction-level constraints such as uncertainty, urgency, incomplete" history and the wanted style of communication.[^c2] The design "independently decomposes the synthesized evidence" and the query into these two kinds of constraint, "subjective interaction constraints, ensuring the" rubric captures conversational quality as well as factual accuracy.[^c3]

The two tracks meet in a rubric synthesis step, which drafts criteria from the facts, the interaction constraints and the query. An audit step then runs a gap analysis against the atomic facts. It "first identifies and supplements missing details" and afterwards filters out "unsupported hallucinations or irrelevant constraints."[^c4][^c5] Read this way, the atomic track is the audit's reference and the interaction track is what lets the criteria be about this patient's situation rather than about the disease alone. That reading is mine, not the paper's.

## What was measured

The paper scores a generated rubric by recall against physician-written gold criteria. Each gold criterion is an atomic constraint, and an LLM judge decides whether the generated rubric entails it: "Treating the entire generated rubric R as" the premise and each gold constraint as the hypothesis.[^c6] On HealthBench the framework reaches 50.20% and on LLMEval-Med 31.90%, which the abstract reports as "significantly outperforming the GPT-4o baseline."[^c7] The gain over the one-step GPT-4o rubric is +9.36% on HealthBench and +3.15% on LLMEval-Med; the text calls the absolute gain moderate.[^c8]

The component ablation is the part that bears on the track split. Removing the interaction agent gave the largest drop in coverage on both datasets, −14.60 on HealthBench and −23.90 on LLMEval-Med. Removing the medical fact agent gave the smallest, −0.40 and −5.18.[^c9] The authors read the second result as meaning that "atomic decomposition is not the primary driver of coverage improvement." Its value is that it makes the evidence-to-criterion mapping explicit and auditable.[^c10] They conclude that "interaction-intent modeling provides the most consistent contribution" to coverage, while the component contributions differ across datasets.[^c11]

## Limits

- One backbone. "Our framework currently relies exclusively on a single backbone model" (Llama-3.3-70B-Instruct); smaller or other models were not tested.[^c12]
- The tracks are separated by role, not by input. The interaction agent reads "from the user query Q and evidence E,"[^c13] so the interaction track is conditioned on the retrieved evidence. The ablation isolates an agent, not a clean split of information.
- Coverage is a recall measure. "Since CIA is recall-oriented," precision is reported separately.[^c14] High recall against gold criteria does not show that the extra interaction criteria are correct. Whether the physician criteria weight communication constraints the way this rubric does is not checked here; that is my inference.
- Single-turn evaluation. The experiments use "fixed queryresponse pairs,"[^c15] so the interaction track was not tested on follow-up questions or longitudinal context.
- The weights are "clinically motivated but heuristic,"[^c16] and the paper runs no sensitivity analysis on them.
- Cost. "processing a single query requires 6 LLM calls," with "end-to-end latency of roughly 43.26 seconds."[^c17][^c18] Two tracks plus an audit are several calls per query before any reading of the rubric.

## Related

- [[question-specific-rubric]] — a per-question rubric as an RL reward; this note says where such criteria can come from and what the interaction track adds in measured coverage.
- [[expert-report-derived-atomic-rubrics]] — also atomic, content-bearing criteria, but taken from one expert article and graded as binary checklist items, not retrieved and merged with query constraints.
- [[criteria-transfer-locked-rubric-scoring]] — evidence grounding at scoring time for a fixed rubric; here the grounding happens at construction time.

[^c1]: doi-10-48550-arxiv-2601-15161 — "atomic medical facts F (the Reference Board) including declarative assertions, contraindications,"
[^c2]: doi-10-48550-arxiv-2601-15161 — "interaction-level constraints such as uncertainty, urgency, incomplete"
[^c3]: doi-10-48550-arxiv-2601-15161 — "subjective interaction constraints, ensuring the"
[^c4]: doi-10-48550-arxiv-2601-15161 — "first identifies and supplements missing details"
[^c5]: doi-10-48550-arxiv-2601-15161 — "filters out unsupported hallucinations or irrelevant constraints"
[^c6]: doi-10-48550-arxiv-2601-15161 — "Treating the entire generated rubric R as"
[^c7]: doi-10-48550-arxiv-2601-15161 — "scores of 50.20% and 31.90%, significantly outperforming the GPT-4o baseline"
[^c8]: doi-10-48550-arxiv-2601-15161 — "rubrics yield a consistent improvement of +9.36%"
[^c9]: doi-10-48550-arxiv-2601-15161 — "Intent Agent causes the largest CIA degradation"
[^c10]: doi-10-48550-arxiv-2601-15161 — "atomic decomposition is not the primary driver of coverage improvement"
[^c11]: doi-10-48550-arxiv-2601-15161 — "interaction-intent modeling provides the most consistent contribution"
[^c12]: doi-10-48550-arxiv-2601-15161 — "our framework currently relies exclusively on a single backbone model"
[^c13]: doi-10-48550-arxiv-2601-15161 — "from the user query Q and evidence E"
[^c14]: doi-10-48550-arxiv-2601-15161 — "Since CIA is recall-oriented"
[^c15]: doi-10-48550-arxiv-2601-15161 — "our experiments primarily evaluate fixed queryresponse pairs"
[^c16]: doi-10-48550-arxiv-2601-15161 — "clinically motivated but heuristic"
[^c17]: doi-10-48550-arxiv-2601-15161 — "processing a single query requires 6 LLM calls"
[^c18]: doi-10-48550-arxiv-2601-15161 — "end-to-end latency of roughly 43.26 seconds"
