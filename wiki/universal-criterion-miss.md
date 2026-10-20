---
description: "Counting the criteria every model fails, not each model's own rate, exposes shared blind spots: 55 of 108 critical rubric criteria were missed by all three frontier models in the pilot."
aliases: ["universal miss", "shared blind spot", "criterion no model satisfies", "universal weight-5 miss"]
sources: ["doi-10-48550-arxiv-2607-02175"]
---
# Universal criterion miss

Given the same expert-labelled criteria for several models, one can ask two different questions. The per-model rate asks how often each model fails. The universal count asks whether the models fail the same criteria. The paper defines the second as "a critical criterion that all three models failed."[^c1] Across five clinical tasks, "55 of 108 (51%) critical criteria that no frontier model satisfied" is the count it reports.[^c2]

The mechanism is an intersection over models rather than an average. Two models can each pass 40% of a set and fail entirely different items, or fail the same items. The per-model rate cannot tell these apart; the universal count does. When the failures coincide, the gap is less likely to belong to one model's habits and more likely to sit in the item: in the question's framing, in the knowledge the models share, or in an inference none of them draws. The authors present their qualitative examples under the heading "Examples of Universal misses (shared blind spots)."[^c3]

The examples show what kind of inference is shared. In one, the models were given a falling biomarker: "All three models anchored on the admission heart-failure diagnosis and missed the contradicting biomarker trend."[^c4] In another, the criterion needed a two-step chain from medication to kidney injury to impaired drug clearance, and "No model connected the medication list to the AKI"[^c5] — the chain was not drawn at all. The authors read both as failures to override a salient earlier frame with later evidence, and as failures of mechanism rather than of recall. The universal count is what makes these visible as recurring failures instead of one model's slip.

The counts are uneven. Per task the universal misses were "Task 1, 11/30; Task 2, 5/15; Task 3, 2/12; Task 4, 4/13; Task 5, 33/38."[^c6] So one scenario supplies most of the total: "Task 5 dominates: 33 of its 38 critical criteria were universally missed."[^c7] A per-task reading is needed before a universal count is taken as a property of the models at large.

## Limits

- Only three models were tested, from three vendors. The paper's phrase "no frontier model satisfied" generalises from these three. "Universal" here means "none of these three." (my inference)
- Most of the total comes from one task. Without Task 5 the universal count is 22 of 70 other critical criteria, about 31%, by my arithmetic from the per-task counts. The headline 51% is largely a single-scenario result. (my inference)
- The count depends on one expert label per criterion, and "independent double-expert grading on every criterion" was not done.[^c8] A criterion marked missed by the expert is missed in the count; an expert error becomes a shared blind spot by construction.
- The harness is deliberately conservative: "models equipped with reasoning scaffolds, tools, or retrieval might perform differently on specific criteria."[^c9] A universal miss under single-turn prompting may not survive a different harness, and the paper does not test one.
- A shared failure is not shown to be a shared cause. Three models trained on overlapping data could miss the same item for different reasons; the text gives no mechanism test beyond the examples.
- Universal misses do not say which criteria a clinician would rate as more important. The weight-5 restriction is a choice made before the count, and the paper reports weights as clinical judgement.[^c10]

## Related

- [[weight-stratified-criterion-pass-rate]] — the same labels read by weight class within each model; this note reads them across models
- [[expert-report-derived-atomic-rubrics]] — the content-bearing rubric form whose criteria are tallied here
- [[verifier-exploitation-rate]] — another per-criterion measure that requires agreement across a reference panel before counting a failure
- [[judge-coverage-overestimation]] — the judge-side version of the same blind spot: surface coherence credited as completeness

[^c1]: doi-10-48550-arxiv-2607-02175 — "We define a universal weight-5 miss as a critical criterion that all three models failed."
[^c2]: doi-10-48550-arxiv-2607-02175 — "55 of 108 (51%) critical criteria that no frontier model satisfied"
[^c3]: doi-10-48550-arxiv-2607-02175 — "Examples of Universal misses (shared blind spots)."
[^c4]: doi-10-48550-arxiv-2607-02175 — "All three models anchored on the admission heart-failure diagnosis and missed the contradicting biomarker trend."
[^c5]: doi-10-48550-arxiv-2607-02175 — "No model connected the medication list to the AKI"
[^c6]: doi-10-48550-arxiv-2607-02175 — "Task 1, 11/30; Task 2, 5/15; Task 3, 2/12; Task 4, 4/13; Task 5, 33/38"
[^c7]: doi-10-48550-arxiv-2607-02175 — "Task 5 dominates: 33 of its 38 critical criteria were universally missed"
[^c8]: doi-10-48550-arxiv-2607-02175 — "independent double-expert grading on every criterion"
[^c9]: doi-10-48550-arxiv-2607-02175 — "models equipped with reasoning scaffolds, tools, or retrieval might perform"
[^c10]: doi-10-48550-arxiv-2607-02175 — "a weight from 1 (trivial) to 5 (critical"
