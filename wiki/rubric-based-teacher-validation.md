---
description: "Before distillation, a rubric-conditioned teacher's rollouts are kept only if they cover every rubric aspect; the filter lifts self-distillation on four backbones over no filter."
aliases: ["RTV", "rubric-based teacher validation", "teacher coverage filtering", "rubric-coverage teacher filter"]
sources: ["doi-10-48550-arxiv-2609-35262"]
---
# Rubric-based teacher validation

A teacher that is handed the target rubric aspects is not thereby a reliable teacher. The authors state the gap plainly: "privileged information alone" "does not guarantee reliable supervision."[^c1] In rubric-aware self-distillation the teacher's next-token distributions are transferred to the student wholesale, so a teacher that overlooks or underplays some aspects passes that failure on as misleading supervision. Rubric-based teacher validation (RTV) is a filter placed in front of distillation. It asks, for each training instance, whether the rubric-informed teacher can actually use the aspects it was given, and drops the instance if not.

## The procedure

For each training instance, a response is first generated from the frozen rubric-informed teacher. That response is used only for validation, not for distillation. A rubric judge scores it against every aspect, and the score s_T is the mean of the per-aspect coverage: the fraction of aspects the response addresses, each graded on the benchmark's scale.[^c2] The authors describe the reading directly: "A higher sT therefore indicates more reliable teacher guidance."[^c3] The filter keeps instances with s_T at or above a threshold. The filter runs once, on the whole training set, before distillation begins, not per step.[^c4]

The main setting uses the strictest threshold, which requires "requiring the teacher response to fully address all target rubric aspects."[^c5] The stated reason is that the strict criterion "filters out unreliable instances, reducing the risk of transferring misleading rubric guidance" to the student.[^c6]

## What it changes

Against vanilla self-distillation (threshold 0, no filter), the full-coverage threshold "consistently improves performance across all four backbones."[^c11] The authors summarize the threshold sweep as "stricter validation generally leads to better performance."[^c12] On Gemma2-9B and Qwen2.5-7B, where the sweep was run, intermediate thresholds gave small and non-monotonic gains, and the authors read this as lenient validation letting through "unreliable teacher signals with incomplete rubric coverage."[^c7]

The size of the filter depends on the backbone. Gemma2-9B has a heavier tail of low-coverage teacher outputs: "Only 37% of its training instances attain sT = 1," against 57%, 62% and 81% for the other backbones.[^c8] That explains why Gemma2-9B benefits most from the strict threshold: at a permissive threshold it is training on many teacher responses that only partly cover the aspects. The authors also claim RTV improves "improving both supervision quality and training efficiency."[^c9] The efficiency side is supported only by the retained counts and wall-clock times they report, not by a comparison of cost against the unfiltered run that I saw in the sections read.

## Limits

- The coverage score is produced by the same kind of LLM judge used for evaluation, so the filter selects instances the judge rates as covered. A filter and an evaluation metric that share a judge can agree with each other for reasons the target does not share. The paper does not test this with a human-judged or differently-judged metric in the sections I read (my inference).
- The threshold sweep is complete only on two backbones; for Qwen2.5-14B and Qwen3-4B only the unfiltered and full-coverage settings are compared.[^c10]
- At the default threshold the filter discards most of the data for some backbones. The retained set is a biased subset: instances whose questions are hard for the rubric-conditioned teacher are the ones removed. The effect of that bias on what the student learns is not measured.
- The threshold is a single scalar on mean coverage. An instance that covers all but one aspect is dropped as firmly as one that covers none; the filter cannot say which aspects the teacher missed.
- The gains are small on the figure's scale: its axis runs from about -0.002 to +0.014 average (my reading of the figure, not a stated effect size).
- The validation step costs one extra teacher generation per training instance; the paper's training-cost table does not isolate that cost (my inference).

The general point, that a teacher's reliability limits what can be learned from it, is one the wiki already has in another setting: a proxy built on a teacher's labels needs the teacher to be "correct a clear majority of the time" ([[teacher-relative-uplift-proxy]]). RTV's contribution here is to check the teacher per instance rather than assume it.

## Related

- [[rubric-aware-on-policy-self-distillation]] — the distillation this filter sits in front of; RTV does not change the loss, only which instances enter it.
- [[teacher-relative-uplift-proxy]] — another setting where a teacher's reliability limits what a student can be measured against.
- [[qcp-guided-self-distillation]] — a privileged-teacher method that, as far as its note records, does not check teacher output before distilling.

[^c1]: doi-10-48550-arxiv-2609-35262 — "does not guarantee reliable supervision."
[^c2]: doi-10-48550-arxiv-2609-35262 — "we first generate a response from the frozen rubric-informed teacher"
[^c3]: doi-10-48550-arxiv-2609-35262 — "A higher sT therefore indicates more reliable teacher guidance."
[^c4]: doi-10-48550-arxiv-2609-35262 — "RTV is applied once to the original training set before distillation."
[^c5]: doi-10-48550-arxiv-2609-35262 — "requiring the teacher response to fully address all target rubric aspects."
[^c6]: doi-10-48550-arxiv-2609-35262 — "criterion filters out unreliable instances, reducing the risk of transferring misleading rubric guidance"
[^c7]: doi-10-48550-arxiv-2609-35262 — "retain unreliable teacher signals with incomplete rubric coverage, whereas requiring full coverage"
[^c8]: doi-10-48550-arxiv-2609-35262 — "Only 37% of its training instances attain sT = 1"
[^c9]: doi-10-48550-arxiv-2609-35262 — "improving both supervision quality and training efficiency."
[^c10]: doi-10-48550-arxiv-2609-35262 — "on Gemma2-9B and Qwen2.5-7B,"
[^c11]: doi-10-48550-arxiv-2609-35262 — "consistently improves performance across all four backbones."
[^c12]: doi-10-48550-arxiv-2609-35262 — "stricter validation generally leads to better performance."
