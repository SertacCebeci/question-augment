---
description: "Item difficulty can be set by the length of the knowledge-graph path behind a question and checked by a probe model's entropy over the options; retrieval or validation alone left entropy near zero."
aliases: ["KG path-length difficulty control", "predictive-entropy distractor pull", "KNIGHT hardness calibration", "causal depth"]
sources: ["arxiv-2602-20135", "arxiv-2511-19923"]
---
# Hop-depth difficulty control checked by distractor entropy

KNIGHT builds a topic knowledge graph once and writes each multiple-choice question from a path of d hops through it. The stem, key and three "semantically proximate" distractors come from a template that concatenates the node glosses and relation labels along the path.[^c1] Difficulty is a dial on graph depth: the authors say a user-defined difficulty parameter controls graph depth to elicit multi-hop or higher-order items.[^c2] Two levels were generated (Level 1, Level 3) in History, Biology and Mathematics.

## The check: distractor pull as entropy

Path length is only an intended difficulty. To test whether it is realised, a small fixed probe model (LLaMA 3.2-3B-Instruct) gives logits over A-D. Entropy H of the softmax over the four options measures how much probability mass the distractors take; higher H should coincide with lower probe accuracy when items are genuinely harder.[^c3]

## What was measured

- Entropy rises from Level 1 to Level 3, probe accuracy falls, and the standard deviation of H rises, which the authors read as a broader hardness spread rather than tightly clustered difficulty.[^c4]
- Across models from GPT-4o to 2B-scale, Level 3 accuracy is consistently lower than Level 1 within each domain, and a 200-item human study mirrors this.[^c5]
- Ablation: Plain is degenerate, with near-zero entropy and 100% probe accuracy. RAG and RAG+Val stay near zero entropy; so retrieval or validator-only filtering does not induce close distractors.[^c6] Adding KG-conditioned prompting is "the main driver" of stronger distractor competition.[^c7]
- Without a validator, KG prompting can raise topical drift and validity errors; with the five-criterion validator, Level 3 does not substantially increase violations.[^c8]
- The model ranking on KNIGHT's averaged items closely matches the ranking on external benchmarks (GPT-4o first, then Mistral Large and Llama3-70B-Instruct).[^c9]

## Why it bears on asking

The set of wrong options, not only the stem, carries difficulty, and the work separates three things that are easy to conflate: intended hardness (hops), realised hardness (probe entropy and accuracy) and validity (single key, answerable from evidence). Hardness raised by structure stayed answerable only because a validator enforced it; that reading of the ablation is mine.

The same dial appears in a causal graph of events, under the name causal depth. CounterVQA takes the maximum length of a simple path in each video's causal graph and keeps videos with depth 3 or more for its long-chain level.[^c10] Here the depth is applied to the material before any model answers: it selects which videos may carry a multi-hop question, rather than setting the difficulty of an item after it is written. My reading, not stated in the work: one long path sets the depth even when most of the graph is shallow, so the depth says little about how many events a typical question must pass through. The text read reports no entropy-style probe of this filter.

## Limits

- Entropy is from one 3B probe; whether it tracks hardness for other answerers is supported only by accuracy drops on the benchmarked models and a 200-item human study.
- Hop count and abstraction are confounded with domain; Mathematics at Level 3 had the highest entropy, so the depth effect is not isolated from content.
- Only Wikipedia/Wikidata and GPT-4o-mini generation were tested; the claim of ontology-agnosticism is untested here.
- Answerability from supplied evidence is used as a hallucination proxy, not a measure of truth.
- High entropy may also reflect ambiguous options; the paper handles this with audits, not a separate test.

## Related

- [[distractor-strength-reward-signal]] — measures distractor strength by a model's wrong-answer share; here by entropy of a probe.
- [[evidence-chain-question-generation]] — another way of forcing genuine multi-hop structure in generated questions.
- [[item-writing-guidelines]] — the human item-writing criteria the validator adapts.
- [[calibrated-question-generation]] — generation aimed at a target property.
- [[question-evaluation-method]] — appraising finished questions.

[^c1]: arxiv-2602-20135 — "and three semantically proximate distractors DP"
[^c2]: arxiv-2602-20135 — "parameter controls graph depth to elicit multi-hop or higher-order items"
[^c3]: arxiv-2602-20135 — "Higher H"
[^c4]: arxiv-2602-20135 — "entropy increases from Level 1 to Level 3 while probe accuracy decreases"
[^c5]: arxiv-2602-20135 — "accuracy is consistently lower than Level 1 within each domain"
[^c6]: arxiv-2602-20135 — "Plain is degenerate, with near-zero entropy and 100% probe accuracy"
[^c7]: arxiv-2602-20135 — "is the main driver of stronger distractor competition"
[^c8]: arxiv-2602-20135 — "moving to Level 3 does not substantially increase violations"
[^c9]: arxiv-2602-20135 — "closely matches the benchmark average"
[^c10]: arxiv-2511-19923 — "We select videos with Causal-Depth ≥ 3 to ensure adequate complexity for Level 2 questions."
