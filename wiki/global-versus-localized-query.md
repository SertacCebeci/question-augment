---
description: "Whether a question needs the whole video or one segment decides the frame strategy: uniform sampling holds for whole-video questions, while segment questions need query-aware selection."
aliases: ["query typology", "global versus localized question", "holistic versus localized query", "query scope in frame selection"]
sources: ["arxiv-2512-04000"]
---
# Global versus localized query

A question about a long video can need the whole of it or only one part. The first kind, called global here, "requir[es] a comprehensive understanding of the entire video," with the example "What title best summarizes this video?"[^c1] The second, localized, "relate[s] directly to specific, localized segments of a video," as in a question about one object doing one thing.[^c2] The work's claim is that this difference in scope should decide which frames a model sees.

The mechanism starts from a budget. A large multimodal model cannot take every frame, so "only a sampled subset of frames is typically used as input."[^c3] The usual choice is uniform sampling, which spaces the frames evenly and is "query-agnostic, often selecting redundant frames while omitting crucial, query-relevant moments."[^c4] With a fixed count, a localized question has only a few frames that bear on it, and the rest enter the context as distractors. The authors measured the consequence on three video LMMs: as the number of sampled frames rises, "performance on localized queries degrades substantially, as irrelevant frames are injected into the context," while "performance on global queries remains stable."[^c5][^c6] They attribute the difference to "global queries benefiting from holistic information, whereas excess frames introduce noise for localized tasks."[^c7] This is the same non-monotone pattern the paper finds overall, where accuracy "initially improves with more input frames but declines beyond a certain point."[^c8]

The consequence for selection is a per-type comparison. For global questions, "standard uniform sampling consistently achieves performance comparable to, or occasionally even superior to, our complex pipeline."[^c9] For localized questions, "our pipeline consistently outperforms uniform sampling."[^c10] The design conclusion is that "identifying the query type is essential to determine whether to" use broad sampling or targeted extraction.[^c11] So the scope of a question works as a switch: the cheap strategy for whole-video questions, and a search for the relevant segment for localized ones. The search has a compute cost, and the paper's point is that it buys nothing on global questions.

The switch has to be read off the question. The paper does this with an LLM, asked to "classify a given query Q as either global or localized."[^c12] Against human labels, "nearly all evaluated LLMs achieve an overall classification accuracy exceeding 80%," and "almost all LLMs achieve an accuracy greater than 90%" on the localized class, which is the one that drives final performance.[^c13][^c14]

For someone asking or answering, the transferable part is the variable, not the video machinery: how much of the available material a question needs. A question that needs the whole record is served by spread-out evidence. A question that needs one segment is harmed by spread-out evidence, because the extra material is noise. This step from video to other questions is my inference; the paper tests only video QA. The closest parallel in the wiki is [[retrieval-gain-by-question-type]], where a question kind also predicts where an added step pays, but the axis there is where the missing fact lives, not how much of the input the question needs.

## Limits

- The trend evidence comes from three 7–8B open models, "pretrained LMMs: Qwen2.5-VL-7B [16], InternVL3-8B [68], and LLaVA-OneVision-7B [3]."[^c15] The benchmarks are "MLVU [54], VideoMME [56], and LongVideoBench [55]."[^c16] Other model sizes, other video tasks and non-video questions are not in the text I read.
- The labels for the trend analysis were assigned by hand: "we manually categorize queries from" MLVU and VideoMME.[^c17] The boundary between global and localized is a judgment about scope. The paper gives two examples and a definition, not a rule that a third party could apply mechanically, and the LLM classifier is itself only about 80 to 90 percent accurate by its own measure.
- The noise account is the authors' attribution ("We attribute this to"). The text I read does not isolate it by changing only the irrelevant frames, so "dilution" as the cause is plausible, not established.
- The global result is parity: uniform sampling is "comparable to, or occasionally even superior to" the pipeline. It shows that selection adds little on global questions, not that selection can never help them.
- Classification errors are argued to matter little for global questions: the lower global accuracy has "a negligible impact" on final performance.[^c18] That is an argument from the type-level gap; the text I read does not run the pipeline with misrouted questions and measure the result.
- Whether a cheaper selector, or a larger frame budget under uniform sampling, would close the localized gap is not tested in the text I read.

## Related

- [[retrieval-gain-by-question-type]] — also a split by question kind that predicts where an added step pays; there the axis is whether the missing fact lives in the parameters or the passages, here it is how much of the input a question needs
- [[contiguous-clip-evidence-unit]] — the same video setting seen from the evidence unit: keyframes versus contiguous clips, with uniform sampling weakest in its ablation
- [[query-type-variance-in-qpp]] — query type as a between-query factor in predicting retrieval performance; the same move of typing the query before choosing a method, in another field

[^c1]: arxiv-2512-04000 — "requiring a comprehensive understanding of the entire video"
[^c2]: arxiv-2512-04000 — "relate directly to specific, localized segments of a video"
[^c3]: arxiv-2512-04000 — "only a sampled subset of frames is typically used as input"
[^c4]: arxiv-2512-04000 — "it is query-agnostic, often selecting redundant frames"
[^c5]: arxiv-2512-04000 — "performance on localized queries degrades substantially, as irrelevant frames are injected into the context"
[^c6]: arxiv-2512-04000 — "performance on global queries remains stable"
[^c7]: arxiv-2512-04000 — "whereas excess frames introduce noise for localized tasks"
[^c8]: arxiv-2512-04000 — "more input frames but declines beyond a certain point"
[^c9]: arxiv-2512-04000 — "sampling consistently achieves performance comparable to, or occasionally even superior to, our complex pipeline"
[^c10]: arxiv-2512-04000 — "For LQs, our pipeline consistently outperforms uniform sampling"
[^c11]: arxiv-2512-04000 — "identifying the query type is essential to determine whether to"
[^c12]: arxiv-2512-04000 — "classify a given query Q as either global or localized"
[^c13]: arxiv-2512-04000 — "achieve an overall classification accuracy exceeding 80%"
[^c14]: arxiv-2512-04000 — "almost all LLMs achieve an accuracy greater than 90%"
[^c15]: arxiv-2512-04000 — "Qwen2.5-VL-7B [16], InternVL3-8B [68], and LLaVA-OneVision-7B [3]"
[^c16]: arxiv-2512-04000 — "MLVU [54], VideoMME [56], and LongVideoBench [55]"
[^c17]: arxiv-2512-04000 — "we manually categorize queries from"
[^c18]: arxiv-2512-04000 — "this has a negligible impact"
