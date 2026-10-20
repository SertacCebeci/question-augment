---
description: "Instruction-tuned models often fix their answer before the chain of thought: a linear probe reads it pre-CoT (AUC >0.9) and steering that direction flips answers, with confabulated reasoning."
aliases: ["post-hoc reasoning in chain of thought", "pre-CoT answer commitment", "representational pre-commitment"]
sources: ["arxiv-2603-01437", "arxiv-2512-09555"]
---
# Pre-committed answer before chain of thought

Post-hoc reasoning is the case where the model's answer is settled before the CoT is written; that answer is the pre-committed answer.[^c1] The paper tests this with three hypotheses.

## Mechanism and measurements

**Decodable (H1).** Linear probes trained on residual-stream activations at the last token before CoT predict the model's final answer with above 0.9 AUC on most tasks.[^c2] The probes are difference-of-means directions built on the semantic answer label.

**Causal (H2).** Adding the probe direction to activations during generation often flips the answer. Flip rates substantially exceed those of norm-matched orthogonal baselines across most model-dataset pairs.[^c2] The orthogonal baseline is not near zero. The authors explain this as general degradation toward random guessing, which on a balanced binary task gives a 50% flip rate, and orthogonal steering saturates around 0.5.[^c3]

**Pathologies (H3).** When steering induces a wrong answer, two failure modes appear: confabulation, where the CoT fabricates false premises, and non-entailment, where it states correct premises but draws an unsupported conclusion.[^c2] The authors use both to argue against two rival readings. Confabulated chains are coherent and aligned with the wrong conclusion, which suggests intact reasoning, so the flips are not mere collapse.[^c4] In non-entailment the CoT stays largely correct while the conclusion shifts, which suggests the answer is set by a pathway that bypasses the verbalized reasoning, so the CoT is not mediating the effect.[^c5]

The paper's reading is that post-hoc reasoning may be harmless when the pre-CoT belief is correct, but can produce undesirable behaviour when the model reasons from a false belief.[^c2]

For asking and answering, an answer's accompanying rationale cannot be taken as the cause of the answer. The rationale may be a justification written for an answer that was already decided.

## Limits

- Steering was applied at every decoding position after the prompt, including the final-answer tokens, so part of the flip may be direct answer-token biasing rather than an edit to a pre-CoT belief. The authors leave a CoT-region-only intervention to future work.[^c6]
- Probe AUC was considerably lower for GPT-OSS 20B, a reasoning model, and its flip rate was negligible against the orthogonal baseline. The authors only speculate that the answers of reasoning models depend less on the pre-committed answer.[^c7]
- Evidence is from tasks with binary or short answers and from a limited set of models. Whether it holds for open-ended questions is not shown.
- The "bypasses the reasoning" reading is an interpretation of non-entailment cases, not a direct test.
- The chain-first case has a counterpart that the work does not frame as pre-commitment. In a blind image quality model the descriptions are generated before the quality token, yet the verdict's attention falls on a few image-embedding tokens rather than on those descriptions, and the descriptions sometimes contradict the verdict.[^c8][^c9][^c10] So a rationale written before the answer is not thereby the answer's basis. This is one model family and an attention analysis averaged over 720 samples; attention is a correlational readout, not a causal test of the chain.

## Related

- [[cot-reasoning-faithfulness-by-truncation]] — a behavioural test of the same question, without an internal probe or intervention
- [[implicit-answer-conditioning]] — a trace that converges on its answer inflates confidence in it
- [[stance-consistency-plus-causal-influence-faithfulness]] — faithfulness tested by causal influence
- [[cot-monitorability-information-bound]] — how far a CoT can be monitored for what drives the output

[^c1]: arxiv-2603-01437 — "We use post-hoc reasoning to refer to these instances where"
[^c2]: arxiv-2603-01437 — "we can predict the model’s final answer with >0.9 AUC on most tasks."
[^c3]: arxiv-2603-01437 — "Random guessing on a binary task with a balanced distribution will, on"
[^c4]: arxiv-2603-01437 — "which is evidence of intact reasoning ability"
[^c5]: arxiv-2603-01437 — "suggesting the answer is determined"
[^c6]: arxiv-2603-01437 — "Part of the steering effect may therefore reflect"
[^c7]: arxiv-2603-01437 — "despite its high AUC. We speculate that the final answer for LRMs is less causally dependent on the pre-committed answer"
[^c8]: arxiv-2512-09555 — "The VLM-based models will first generate the context tokens"
[^c9]: arxiv-2512-09555 — "prediction tends to ignore the context tokens but straightly fit to some unexplainable visual embeddings"
[^c10]: arxiv-2512-09555 — "such models sometimes produce textual descriptions of visual attributes that contradict the final quality predictions"
