---
description: "Clustering physician rubric embeddings and refining the clusters by hand yields a 29-criterion shared pool that trains about as well as instance rubrics in-domain."
aliases: ["Health-SCORE rubric creation", "rubric abstraction by clustering", "reusable rubric criteria", "pooled rubric criteria"]
sources: ["doi-10-48550-arxiv-2601-18706"]
---
# Clustered criteria pool

Physician-written rubrics are precise but expensive, and they are written per conversation. A clustered criteria pool is an attempt to keep the precision of those rubrics while making the criteria reusable across conversations. The starting material is large: HealthBench, the source here, is "evaluated using more than 48,000 physicianauthored criteria."[^c1] The pool is built by collapsing that set into a small number of general criteria.

The procedure has three steps. First, each rubric is embedded: "producing high-dimensional semantic representations of the rubric."[^c2] Second, the embeddings are clustered, so that rubrics with the same evaluative aim group together despite different wording. The clustering is not uniform. "While some rubrics formed individual clusters due to their high specificity, others" are "naturally grouped together based on shared evaluative intent."[^c3] Third, the clusters are checked by hand, through "manual inspection and refinement" that is meant "to reduce noise and remove outliers."[^c4] The result is a pool of "29 HealthSCORE criteria."[^c5]

The grouping step is meant to merge rubrics that differ in surface form but share a failure mode. The paper's example is two rubrics, one checking patient details and one checking fabricated laboratory results, which "both target the same underlying failure mode: making unsupported assumptions or introducing information not stated in the prompt."[^c6] A single pooled criterion covers both.

## What was measured

The pool is used as a reward and as prompt content, and the paper evaluates it by how well models trained on it perform against the physician rubrics. In-domain, the authors report "attaining performance comparable to training directly with HealthBench instance-specific rubrics."[^c7] The framing is that the pool serves as "a scalable surrogate supervision signal," with the human rubrics kept as the gold standard for evaluation.[^c8] The authors also state that the gains "extend to outof-distribution evaluations," naming HealthBench-Hard and CSEDB.[^c9]

The cost argument is framed in the figure and introduction. The figure caption says the pool is "far less costly to develop" than instance-level rubrics,[^c10] and the paper says instance-level criteria carry "substantial development effort and domain knowledge, making them costly, hard to scale."[^c11] The text I read does not report development hours or money spent on either route, so the cost advantage is asserted and not measured here.

## Limits

- The pool is derived from the same HealthBench rubrics that the evaluation then uses as its gold standard. The authors write, "We use the set of rubrics from HealthBench to develop the initial set of criteria for Health-SCORE."[^c12] Their argument against circularity is that models are scored on human rubrics, not on the pool itself. That still leaves a dependence: the pool and the test criteria come from one source, so agreement is not independent evidence about the pool's coverage (my inference).
- The clustering involves choices. The paper says the process "involves heuristic choices as well as a manual" refinement step.[^c13] The distance measure, the number of clusters, and which outliers were removed are not varied in the parts I read.
- The abstraction assumes that expert criteria can be generalized. The authors' premise is that "rubrics encode reusable, higher-level evaluation" criteria.[^c14] Where that premise fails, a pool would keep general items and lose the case-specific ones that matter for a given conversation.
- The validation of the pool is downstream performance and an axis-level analysis: "validating the resulting Health-SCORE rubrics through downstream performance and axis-level analysis."[^c15] No independent check of whether each pooled criterion is a faithful summary of its cluster is reported in the text I read.
- The pool is built for health data tasks, and the authors say their findings "may not imply universal applicability" beyond them.[^c16]

## Related

- [[adaptive-rubric-selection]] — chooses a per-prompt subset from a pool like this one; the pool is the input and the selection is the second step
- [[rubric-formation-gap]] — shows that human rubrics beat model-written ones when judge and verification are fixed, and that deciding what to check is the bottleneck; a pool built once from human rubrics is one answer to that gap (my inference)
- [[question-specific-rubric]] — the opposite choice: writing criteria afresh for each question rather than abstracting from existing expert rubrics
- [[recursive-rubric-decomposition]] — also edits the rubric item set for redundancy, but by splitting items into finer ones rather than merging clusters into a shared item

[^c1]: doi-10-48550-arxiv-2601-18706 — "evaluated using more than 48,000 physicianauthored criteria"
[^c2]: doi-10-48550-arxiv-2601-18706 — "producing high-dimensional semantic representations of the rubric"
[^c3]: doi-10-48550-arxiv-2601-18706 — "naturally grouped together based on shared evaluative intent"
[^c4]: doi-10-48550-arxiv-2601-18706 — "of the clusters to reduce noise and remove outliers"
[^c5]: doi-10-48550-arxiv-2601-18706 — "we derived a final set of 29 HealthSCORE criteria"
[^c6]: doi-10-48550-arxiv-2601-18706 — "making unsupported assumptions or introducing information not stated in the prompt"
[^c7]: doi-10-48550-arxiv-2601-18706 — "attaining performance comparable to training directly with HealthBench instance-specific rubrics"
[^c8]: doi-10-48550-arxiv-2601-18706 — "functions as a scalable surrogate supervision signal"
[^c9]: doi-10-48550-arxiv-2601-18706 — "these performance gains extend to outof-distribution evaluations"
[^c10]: doi-10-48550-arxiv-2601-18706 — "but Health-SCORE is far less costly to develop"
[^c11]: doi-10-48550-arxiv-2601-18706 — "substantial development effort and domain knowledge, making them costly, hard to scale"
[^c12]: doi-10-48550-arxiv-2601-18706 — "We use the set of rubrics from HealthBench to develop the initial set of criteria for Health-SCORE."
[^c13]: doi-10-48550-arxiv-2601-18706 — "involves heuristic choices as well as a manual"
[^c14]: doi-10-48550-arxiv-2601-18706 — "rubrics encode reusable, higher-level evaluation"
[^c15]: doi-10-48550-arxiv-2601-18706 — "downstream performance and axis-level analysis"
[^c16]: doi-10-48550-arxiv-2601-18706 — "not imply universal applicability across all healthcare tasks or non-medical domains"
