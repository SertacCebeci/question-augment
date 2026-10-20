---
description: "Generating QA from text and checking it against the figure is argued to cut correlated hallucinations; in one ablation the vision check supplied most of the gain."
aliases: ["cross-modal verification", "cross-modal verification framework", "modality-separated verification", "decoupled generation and verification"]
sources: ["arxiv-2511-19899"]
---
# Decoupled-modality verification

A generated question-answer pair about a figure can be checked in two ways. One is to ask a second vision model to review the answer against the same figure. The other is to generate the pair from a different source, here the text that cites the figure, and to check it against the figure only afterwards. The Cross-Modal Verification framework takes the second route. Its generator is a text-only LLM working from figure-citing paragraphs, and a vision model enters later, to build distractors and to test whether the answer is visually supported.[^d1] The argument is that the two stages fail differently: "from text-based generation and vision-based verification are less likely to coincide."[^d2]

The reason given is that same-figure checks share a failure mode. In LiveXiv a second LVLM reviews each generated answer against the same figure, discarding pairs where it disagrees.[^d3] The authors' objection is that both models "operating on the same visual input, can share correlated hallucinations."[^d4] A verifier that reads what the generator read cannot be relied on to catch what the generator hallucinated, because both may be wrong in the same place. The text read does not measure this correlation; the claim is the authors' premise, and the design follows from it.

The vision stage is concrete. A candidate keeps its answer only if the vision model, asked the question from the figure, reaches the generated answer by majority vote over several runs; the paper credits "the final vision-based step strengthened by self-consistency" for this.[^d5] Text-only checks run first. A source-consistency check asks whether the paper's text picks out the answer uniquely, and a visual-dependence check asks whether the question can be answered without the figure at all.

The measured effect is on downstream training. In the ablation, fine-tuning on 20K pairs taken at three stages of the pipeline gave the following average gains: unfiltered generation hurt the model, text-based filtering helped a little, and the full verification helped most. The paper reports "the average gain from +0.24% to +2.05% (8.5×), confirming that" the vision check is essential.[^d6] The price is volume: the vision check keeps "about 36% of the QA pairs that pass text-based filtering."[^d7]

## Limits

- The independence is asserted, not measured. The ablation compares filter stages by their training gain. It does not measure how correlated the generator's and the verifier's errors are, and the text read contains no run of a same-figure verifier on the same pairs. "Less likely to coincide" is the premise of the design, not a result.
- The effect is shown for one fine-tuned model, "when fine-tuning Qwen2.5-VL-7B-Instruct",[^d8] on one pipeline over arXiv papers. The authors "hope this work can extend beyond SVQA to other domains" such as medical imaging; that extension is not tested here.
- The vision filter over-rejects. In a small human check of rejected items the paper reports that "The vision-based filtering demonstrates strong precision (82.0%)",[^d9] so about one rejection in five was not a real problem in that sample. The text-based checks are weaker: "The text-based filtering achieves 72.0% and 66.0% precision" for the two checks.[^d10]
- Yield is low. "The retention rate is low (3.0%)" from the candidate pool.[^d11] The paper attributes this to vague claims in the figure-citing text, which is a cost of grounding the generator in text that states its claims loosely.

## Related

- [[cross-modal-aggregation-gap]] — the opposite move: there figure and caption are combined into one verdict and do no better than either channel; here the channels are kept apart on purpose.
- [[generate-then-verify-candidate-pipeline]] — the same generator-then-filter shape, where the verifier can only remove candidates; here the difference is which modality each stage reads.
- [[same-model-self-verification-conditional-confidence]] — self-verification is the same-input case in which shared errors are expected.
- [[generation-context-asymmetry]] — the paper's other root cause; the text-only generator answers that asymmetry, and this note is about the separate question of whether the checks share errors.

[^d1]: arxiv-2511-19899 — "generate QA from figure-citing paragraphs to mitigate information asymmetry, and verify against figures to enforce visual grounding"
[^d2]: arxiv-2511-19899 — "from text-based generation and vision-based verification are less likely to coincide"
[^d3]: arxiv-2511-19899 — "uses a second LVLM as a verifier to review each"
[^d4]: arxiv-2511-19899 — "operating on the same visual input, can share correlated hallucinations"
[^d5]: arxiv-2511-19899 — "the final vision-based step strengthened by self-consistency"
[^d6]: arxiv-2511-19899 — "the average gain from +0.24% to +2.05% (8.5×), confirming that"
[^d7]: arxiv-2511-19899 — "about 36% of the QA pairs that pass text-based filtering"
[^d8]: arxiv-2511-19899 — "when fine-tuning Qwen2.5-VL-7B-Instruct"
[^d9]: arxiv-2511-19899 — "The vision-based filtering demonstrates strong precision (82.0%)"
[^d10]: arxiv-2511-19899 — "The text-based filtering achieves 72.0% and 66.0% precision"
[^d11]: arxiv-2511-19899 — "The retention rate is low (3.0%)"
