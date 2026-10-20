---
description: "Irrelevant context that resembles the question lowers reasoning-model accuracy while raising reasoning tokens, so more thinking under noise does not help; similarity, not input length, drives it."
aliases: ["inverse scaling under distractors", "hard negative distractor interference", "contextual distractor degradation"]
sources: ["arxiv-2601-07226", "arxiv-2511-22176", "arxiv-2511-21397"]
---
# Distractor similarity and reasoning inflation

A reasoning model given a question plus irrelevant context does worse than on the clean question, and the damage grows with how much the context looks like the question. The benchmark (NoisyBench, 11 datasets over RAG, reasoning, alignment and tool use) uses three noise types: random documents (RD), random chat history (RC) and hard negatives (HN, relevant-looking but wrong passages).[^c1]

## What was measured

**Drops are large and not predicted by clean accuracy.** Declines range from about 9% to nearly 80% on average. Hard negatives hurt most for most models: one distilled 8B model lost 80.6% relative to its no-distractor score, and 64.2% even with random documents.[^c2] The strongest clean model (Gemini-2.5-Pro) still dropped 38.3%.[^c2]

**Noise reaches alignment behavior.** With no harmful intent in the added text, BBQ accuracy fell from 94.0% to 60.5% for Gemini-2.5-Pro and from 93.0% to 33.7% for DeepSeek-R1-0528.[^c3]

**Similarity inflates thinking.** Binning question-distractor pairs by embedding similarity, accuracy fell and average reasoning tokens rose as similarity rose. The authors read this as the model reviewing distractors to check relevance.[^c4] Output length did not grow with distractor length (weak negative correlation, R=-0.115), so the extra reasoning is attributed to similarity, not to longer input.[^c5] Their conclusion is that scaling reasoning tokens in the presence of distractors often degrades performance.[^c4]

**More distractors raise uncertainty.** With zero to ten hard negatives, output entropy rose and confidence fell.[^c6]

**Attention.** On a misleading-math set with Qwen3-4B-Thinking, incorrect answers allocated far more attention to distractor tokens than correct ones.[^c7]

**Agents amplify it.** Tool-using agents beat the bare reasoning model on clean input but lose to it under RD, RC and HN. The stated causes are trust in tool output, distractor-born hypotheses re-entering later planning steps, and contaminated tool routing.[^c8]

**Taking the irrelevant detail out before reasoning.** A different paper works on the input side: it extracts the facts a question needs into a block and has the model reason over that block alone. On arithmetic word problems the authors claim that by preventing "attention to irrelevant details, F-CoT naturally produces shorter reasoning paths."[^c9] That work measures token counts and accuracy on clean questions, not accuracy under distractors, so it does not test this note's finding; see [[focused-context-reasoning]].

## Limits

- The causal story (models "review" distractors; agents "overtrust") is the authors' interpretation of correlations; only the attention comparison is at token level, on one 4B model and one synthetic dataset.
- Similarity bins are embedding-based; whether human-judged relevance gives the same curve is untested.
- Prompting, context engineering and SFT were reported as insufficient; the one remedy that helped is in [[rationale-aware-reward]].
- For asking: my inference is that padding a question with loosely related background is not harmless to a reasoning answerer. The paper does not test question-writing practice.
- Modality. The inflation is shown for textual context. In a VQA study of reasoning VLMs, visual distractors inserted into the image "reduce accuracy without increasing reasoning length"[^c10], while textual distractors in the prompt "intensify the test-time inverse scaling"[^c11]. The two channels are read as different, not as one effect; the visual side is in [[distractor-attribute-ratio]].

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — retrieval noise damage depends on what the model already knows.
- [[refinement-drift-under-forced-deliberation]] — extra deliberation can also degrade answers.
- [[moderate-adaptive-reasoning-length]] — reasoning length has an optimum rather than rising monotonically.
- [[distractor-strength-reward-signal]] — distractor strength there is wrong-answer attraction in options; here it is context similarity.
- [[focused-context-reasoning]] — the input-side counterpart: extract the needed facts and drop the rest before reasoning, which shortens traces on clean arithmetic problems.
- [[distractor-attribute-ratio]] — the visual-channel counterpart: visual distractors lower accuracy with trace length flat, and the share of distractor attributes in the trace tracks accuracy.

[^c1]: arxiv-2601-07226 — "random documents, irrelevant chat histories, and hard negative distractors"
[^c2]: arxiv-2601-07226 — "Hard negative distractors cause the most severe degradation for most models."
[^c3]: arxiv-2601-07226 — "Gemini-2.5-Pro drops from 94.0% to 60.5% on the"
[^c4]: arxiv-2601-07226 — "Higher similarity between questions and distractors increases reasoning effort while degrading accuracy."
[^c5]: arxiv-2601-07226 — "the output length"
[^c6]: arxiv-2601-07226 — "More distractors lead to higher output entropy and lower confidence."
[^c7]: arxiv-2601-07226 — "Incorrect predictions assign disproportionately high attention to distractor tokens."
[^c8]: arxiv-2601-07226 — "Agentic workflow is more fragile to noise."
[^c9]: arxiv-2511-22176 — "attention to irrelevant details, F-CoT naturally produces shorter reasoning paths."
[^c10]: arxiv-2511-21397 — "visual distractors reduce accuracy without increasing reasoning length"
[^c11]: arxiv-2511-21397 — "textual distractors intensify the test-time inverse scaling"
