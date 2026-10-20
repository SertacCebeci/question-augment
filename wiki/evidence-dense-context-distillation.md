---
description: "Long-document QA reduces retrieved pages to per-page clue records and screened page images, a fixed-length evidence context, so accuracy rises with retrieval top-K."
aliases: ["context engineering for long documents", "evidence-dense context", "coarse-to-fine evidence distillation", "clue distillation over retrieved pages"]
sources: ["arxiv-2511-22850"]
---
# Evidence-dense context distillation

When the answer to a question is spread thinly over a long document, the trouble is often less the reasoning than what the model is shown. The paper's diagnosis is that vision-language models "have difficulty identifying the few key pieces of evidence scattered across multiple pages."[^c1] Its response is to treat the step before answering as a construction problem. The method, SLEUTH, "builds concise and evidence-dense contexts from" noisy retrieval results, and it does this without changing the model.[^c2]

The construction runs in stages over the top-K pages a visual retriever returns. Each page is handled alone. A clue agent "treats each page as the minimal processing unit" and "records structured textual and visual cues."[^c3][^c4] Each record keeps the page, a region, the extracted content, a key insight and the reasoning behind it, so a clue can be traced back to its source. A screening agent keeps only page images with "task-relevant tables, charts, or diagrams" and drops the rest.[^c5] A difficulty agent reads the query and sets the reasoning mode: it "guides Core Decision Agent to adopt the optimal reasoning mode."[^c6] The answering model then reasons over the distilled record, not over the raw pages.

What the design buys is a property of length. Because pages are reduced one at a time, the input to the answering model does not grow with K: "SLEUTH keeps the effective context length fixed, enabling accuracy to scale with larger retrieval top-K."[^c7] The reason the authors give is that extra raw context is itself harmful: "Redundant context brings excessive noise, confusing VLMs."[^c8] In their top-K ablation, "as the K increases, the recall rate rises, and" accuracy improves, and they argue hallucination does not grow with it, because "so the severity of hallucinations will not increase" when the input length is fixed by the construction agent.[^c9][^c10][^c11]

The gains are reported as stage contributions on Qwen3-VL-8B, the example backbone in the ablation.[^c12] The clue agent alone, with no page images, gave "an average gain of +1.85%."[^c13][^c14] Adding page screening raised the gain: "the improvement increases to +4.53%."[^c15] With difficulty assessment the Top-5 setting reached "overall gain of +6.01% over the Base method."[^c16] The authors also report that removing any single agent lowers performance: "is removed, the performance decreases, and the drop."[^c17]

## Limits

The chain starts with a retriever, and the construction can only work on what the retriever returns. The authors state that "agents cannot compensate." for missed pages, and they name feedback-based or hierarchical retrieval as a remedy they do not test.[^c18]

The difficulty signal is binary, and the authors call it "but coarse, which may not capture intermediate reasoning cases."[^c19] Its effect on accuracy is shown only as part of the stacked ablation, not as a standalone comparison against a graded alternative.

The experiments are on "English administrative and academic documents," and the authors name multilingual, handwritten, legal and medical material as untested.[^c20] The method is "entirely prompt-driven and training-free, which benefits interpretability but limits self-evolution."[^c21] Its numbers come from four benchmarks, "Extensive experiments on four benchmarks,"[^c22] run with the authors' own prompts and agent setup. The SOTA claim is theirs and is not checked here.

Not measured in the text: whether reducing pages one at a time loses evidence that only makes sense across pages. A rule split over two pages reaches the answering model as two separate records, and the text reports no case of this kind. That is my inference from the per-page design, not a result.

## Related

- [[page-image-evidence-unit]] — the page as the unit of evidence; SLEUTH's visual-only versus visual-plus-text comparison is recorded there.
- [[complexity-tiered-strategy-routing]] — the difficulty agent is a two-level version of a per-query reasoning-mode router, set after the evidence is built.
- [[distractor-similarity-reasoning-inflation]] — irrelevant context that resembles the question hurts reasoning; the screening stage removes that kind of input before the answer is formed.
- [[context-register]] — keeps a fixed-size working state instead of a growing raw trace, the same aim in search agents.
- [[retrieval-utilization-gap]] — separates evidence that never surfaced from evidence that surfaced and was misused; the clue stage addresses the second, while the retriever-coverage limit above is the first.
- [[medium-context-sweet-spot-for-numeric-prediction]] — compact, decision-relevant context helping while bulk context hurts is a related shape, measured on another task.

[^c1]: arxiv-2511-22850 — "have difficulty identifying the few key pieces of evidence scattered across multiple pages."
[^c2]: arxiv-2511-22850 — "builds concise and evidence-dense contexts from"
[^c3]: arxiv-2511-22850 — "Clue Discovery Agent treats each page as the minimal processing unit."
[^c4]: arxiv-2511-22850 — "records structured textual and visual cues."
[^c5]: arxiv-2511-22850 — "task-relevant tables, charts, or diagrams and filters out"
[^c6]: arxiv-2511-22850 — "guides Core Decision Agent to adopt the optimal reasoning mode."
[^c7]: arxiv-2511-22850 — "SLEUTH keeps the effective context length fixed, enabling accuracy to scale with larger retrieval top-K"
[^c8]: arxiv-2511-22850 — "Redundant context brings excessive noise, confusing VLMs."
[^c9]: arxiv-2511-22850 — "so the severity of hallucinations will not increase"
[^c10]: arxiv-2511-22850 — "length input by our context construction agent is fixed,"
[^c11]: arxiv-2511-22850 — "as the K increases, the recall rate rises, and"
[^c12]: arxiv-2511-22850 — "Taking Qwen3-VL-8B as an"
[^c13]: arxiv-2511-22850 — "evidence recording without any visual input yields"
[^c14]: arxiv-2511-22850 — "an average gain of +1.85%."
[^c15]: arxiv-2511-22850 — "the improvement increases to +4.53%."
[^c16]: arxiv-2511-22850 — "overall gain of +6.01% over the Base method."
[^c17]: arxiv-2511-22850 — "is removed, the performance decreases, and the drop"
[^c18]: arxiv-2511-22850 — "agents cannot compensate."
[^c19]: arxiv-2511-22850 — "but coarse, which may not capture intermediate reasoning cases."
[^c20]: arxiv-2511-22850 — "English administrative and academic documents"
[^c21]: arxiv-2511-22850 — "entirely prompt-driven and training-free, which benefits interpretability but limits self-evolution."
[^c22]: arxiv-2511-22850 — "Extensive experiments on four benchmarks,"
