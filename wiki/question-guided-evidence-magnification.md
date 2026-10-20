---
description: "Scoring candidate image regions against the question, keeping the best one per frame and enlarging it before answering raised video-text QA accuracy, without any training."
aliases: ["scan-focus-amplify", "query-conditioned region zoom", "relevance-gated magnification", "question-conditioned crop"]
sources: ["arxiv-2511-20190"]
---
# Question-guided evidence magnification

When an answerer is given a whole input, the part that matters can be too small to read or buried among other content. One way to change what the answerer can read is to put a question-conditioned filter in front of it. The filter does three things in order: it locates candidate regions, scores each against the question and discards the weak ones, and then enlarges the survivor back to the input's full size. The answerer sees fewer pixels, at higher resolution, and the selection of those pixels depends on the question.

The paper that measures this is SFA (Scan, Focus, Amplify) for Video TextVQA. It is training-free and runs on top of a Video-LLM. A text-spotting model first finds text lines in each frame, and "Frames without any detected text are discarded."[^m1] Each remaining frame is split into up to four corner subregions, and the windows are adjusted so that no text line is cut.[^m2] Next, "a multimodal large language model (MLLM) θs is employed as the scoring model to evaluate the relevance" of each window to the question.[^m3] Windows below a threshold are dropped, and "only the most relevant window in each frame is retained."[^m4] The retained windows are resized to the frame size and passed to the Video-LLM together with the question.[^m5]

The reason the paper gives for the filter is that a general answerer's attention lands elsewhere: general Video-LLMs "easily overlook key" text regions because the text is often "not the primary subject."[^m6] The mechanism is that the question chooses the crop and the crop is enlarged. The answerer then never receives the rest of the frame.

The measured effects are small pieces of the pipeline. Using an adaptive window instead of a fixed one in the Scan stage "yields a 3.95% improvement in accuracy."[^m7] Using an MLLM rather than a text-only LLM as the scorer gives "a 3.4% performance gain."[^m8] The window scale was tuned: beyond 0.6, "larger window sizes result in a smaller magnification factor," so small text loses clarity.[^m9] The relevance threshold, set at 0.7, trades noise against lost evidence: "an excessively high threshold raises the risk of mistakenly" discarding a needed region, while a low one admits irrelevant content.[^m10]

What survives the transfer beyond video text is the structure, not the numbers. An external selection conditioned on the question changes the input the answerer receives, and a crop that is enlarged trades context for resolution. Both are general. What does not transfer is the reliance on a detector that proposes the candidate regions. The answerer can only be guided to regions the detector found, so the candidate generator bounds the whole method.

This is a different lever from [[salience-control]], which moves which evidence a fixed model foregrounds through prompt wording. Here the foregrounding is done by a separate filter outside the answerer, and it changes the input rather than the instruction. My reading is that both act on the same asker-side question, what the answerer is made to attend to, at different points. The paper does not compare the two, and I did not test one against the other.

## Limits

- The evaluation is on Video TextVQA benchmarks, where the answer is text in the scene. The text I read does not test questions whose evidence is not text, or inputs that are not video.
- The paper states its own bound: "its overall capability remains bounded by the inherent limitations of the current VTS models" and the base Video-LLMs.[^m11]
- The design keeps one region per frame. The text I read does not isolate that choice against keeping several regions per frame, so I cannot say from it whether the one-per-frame rule or the threshold carries the gain.
- The paper reports accuracy, not which region the answer rests on. Whether the kept crop is the evidence the answer depends on is not measured. That is my inference from the design.
- Fixed windows can cut text in half. The paper's example is a line read as "MAN" instead of "MANCHESTER", and it argues "text lines may be fragmented, potentially altering their semantic meaning."[^m12] The paper gives this as a motivating example; it does not count how often such cuts happen.
- The gains are modest and come from one validation split with one scorer family. The paper's own generality result is that SFA "improves accuracy by 0.97" with one configuration.[^m13]

## Related

- [[salience-control]] — the prompt-side version of foregrounding evidence; here the foregrounding acts on the input before the answerer.
- [[instruction-steered-cue-reliance]] — wording moves which cue a multimodal answerer relies on; this filter moves what the answerer is shown.
- [[text-prior-over-visual-evidence]] — when the picture is needed, language priors can displace it; magnification works on the perception side of the same visual evidence.
- [[retrieval-utilization-gap]] — the same split between evidence surfaced and evidence used, here for visual input: the filter surfaces the region, and the answerer must still use it.

[^m1]: arxiv-2511-20190 — "Frames without any detected text are discarded"
[^m2]: arxiv-2511-20190 — "each frame is partitioned into up to four subregions"
[^m3]: arxiv-2511-20190 — "is employed as the scoring model to evaluate the relevance"
[^m4]: arxiv-2511-20190 — "only the most relevant window in each frame is retained"
[^m5]: arxiv-2511-20190 — "the selected windows are amplified to their original frame size"
[^m6]: arxiv-2511-20190 — "not the primary subject (which is typically humans, animals, vehicles"
[^m7]: arxiv-2511-20190 — "employing an adaptive window during the Scan stage yields a 3.95% improvement in accuracy"
[^m8]: arxiv-2511-20190 — "leads to a 3.4% performance gain over using a"
[^m9]: arxiv-2511-20190 — "larger window sizes result in a smaller magnification factor during the"
[^m10]: arxiv-2511-20190 — "an excessively high threshold raises the risk of mistakenly"
[^m11]: arxiv-2511-20190 — "its overall capability remains bounded by the inherent limitations of the current VTS models"
[^m12]: arxiv-2511-20190 — "text lines may be fragmented, potentially altering their semantic meaning"
[^m13]: arxiv-2511-20190 — "SFA improves accuracy by 0.97 when using Qwen2.5-VL-7B as scoring models"
