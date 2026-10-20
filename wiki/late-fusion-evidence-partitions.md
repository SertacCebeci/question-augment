---
description: "Reasoning over separate evidence partitions and aggregating their answers (late fusion) can beat pooling all retrieved evidence into one context, by under a point on one benchmark."
aliases: ["stratified ensemble", "late fusion of retrieved contexts", "early vs late fusion"]
sources: ["arxiv-2512-05576", "doi-10-48550-arxiv-2603-08329"]
---
# Late fusion of partitioned evidence

When a tool-using agent retrieves evidence, each run returns a sample of what the tools can reach, and a reader can be given some or all of those samples. Where the samples are combined is a design choice with two ends. Early fusion pools every sample into one context and reads it once. Late fusion keeps the samples in separate partitions, lets a reader reason over each partition, and aggregates the answers at the end. The CURE-Bench paper uses the second arrangement under the name Stratified Ensemble, and gives its purpose as "a Stratified Ensemble strategy (Figure 3(b)) that preserves information diversity."[^c2] The contrast case, global pooling, is built to "maximize the retrieval sample size by pooling all Executor instances" into one aggregation step.[^c1]

The mechanism the authors give concerns what one pool can lose. Pooling reduces noise, but "it risks filtering out rare but valid cues," because a single aggregation step decides which evidence reaches the reader.[^c3] Late fusion keeps such items alive in at least one partition. The authors write that "preserving diverse retrieval contexts prevents the premature filtering of critical evidence, effectively reducing collective hallucination."[^c4] This is their account of the result. The text read does not isolate which items a pool filtered out.

The measurement holds the total number of Executor runs fixed at 30. Early fusion with three Analysts "yields strong results (80.51%), it still faces an information bottleneck".[^c5] Splitting the same 30 runs into three parallel pipelines of ten each, with each pipeline read by its own Analyst and the final decision reached by a self-consistency vote, gave 81.367%, the paper's best figure, "performance of 81.367%".[^c6][^c8] The runs used Gemini 2.5 Flash without search; the leaderboard entry added search, and "Gemini 2.5 Flash achieves 83.803% accuracy" with it.[^c7] The difference between the two fusion arrangements is therefore 0.86 points on the same backbone and the same run budget.

What transfers is the choice of where to combine evidence samples. Whether the aggregation should be a vote, a vote over drafts, or a merge of partitions is not settled by this result, which compares one early arrangement with one late one (my inference, not a test the paper runs).

A second late-fusion design cuts the evidence by source document rather than by run. SPD-RAG gives each document its own sub-agent, and "We assign a dedicated sub-agent" to each one.[^c10] Its synthesis layer then merges the per-document findings. On LOONG the arrangement scored 58.1, and "SPD-RAG achieves an Avg Score of 58.1, substantially outperforming both Normal RAG (33.0)."[^c9] The baselines there pool all evidence under a single top-K retrieval, so the comparison changes the retrieval scope as well as the fusion point. The gain cannot be assigned to late fusion alone (my inference from the design; the paper does not run that split).

## Limits

- One benchmark, one backbone, and one partition split. The text read does not sweep the partition size, and it does not compare late fusion against a single pool with a larger reader.
- The gap is under one point. The text reports no repeated runs and no interval for it, so whether it exceeds sampling noise is open.
- The mechanism, that rare evidence is filtered out of a pool, is the authors' explanation. No experiment in the text read shows which evidence the pool lost.
- Late fusion runs one reader per partition. The text read gives no cost figures for that, so the accuracy comparison is not a cost comparison.

## Related

- [[retrieval-utilization-gap]] — the reader side: late fusion changes how many evidence contexts reach readers, not whether a reader uses the context it has.
- [[medium-context-sweet-spot-for-numeric-prediction]] — shorter contexts are one way to stay off the noisy side of a context-length curve; the two papers do not test each other.
- [[cross-layer-probe-ensemble]] — also an ensemble of readings, but it aggregates across model layers rather than across retrieved evidence; the choice of where to aggregate appears in both.
- [[per-source-exhaustive-coverage]] — the same late merge with the cut made by source document, where each document gets its own retrieval loop; there the coverage gain and the fusion point cannot be separated.

[^c1]: arxiv-2512-05576 — "maximize the retrieval sample size by pooling all Executor instances"
[^c2]: arxiv-2512-05576 — "a Stratified Ensemble strategy (Figure 3(b)) that preserves information diversity."
[^c3]: arxiv-2512-05576 — "it risks filtering out rare but valid cues"
[^c4]: arxiv-2512-05576 — "preserving diverse retrieval contexts prevents the premature filtering of critical evidence, effectively reducing collective hallucination."
[^c5]: arxiv-2512-05576 — "yields strong results (80.51%), it still faces an information bottleneck"
[^c6]: arxiv-2512-05576 — "performance of 81.367%"
[^c7]: arxiv-2512-05576 — "Gemini 2.5 Flash achieves 83.803% accuracy"
[^c8]: arxiv-2512-05576 — "The final decision is reached via self-consisteny mechanism"
[^c9]: doi-10-48550-arxiv-2603-08329 — "SPD-RAG achieves an Avg Score of 58.1, substantially outperforming both Normal RAG (33.0)"
[^c10]: doi-10-48550-arxiv-2603-08329 — "We assign a dedicated sub-agent"
