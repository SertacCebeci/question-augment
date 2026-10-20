---
description: "Citation checks retrieve candidate works from external indexes and have an LLM compare the citation to them, not recall; on a 982-citation physics set this beat direct LLM judgment."
aliases: ["retrieval-grounded citation verification", "candidate retrieval plus comparison", "retrieval-grounded reference verification", "citation existence check"]
sources: ["doi-10-48550-arxiv-2605-27700"]
---
# Retrieval-grounded comparison

A claimed reference can be checked in two ways. One asks the model whether it recognises the work. The other first looks the work up in an external index and then has the model compare the citation with what came back. The second is the mechanism here. The paper states the choice directly: the LLM "is not asked to decide citation validity from memory; it is used as a comparator over externally retrieved evidence."[^r1]

The pipeline has three stages. Retrieval is treated as candidate generation, not as the answer: "We therefore treat retrieval as candidate generation rather than final verification."[^r2] A cleaned title query goes to a cascade of scholarly metadata services, and a returned candidate is kept only if it clears a minimum title similarity. That gate is a plain string measure (normalized Levenshtein on cleaned titles), so a non-model filter runs before any model is involved.[^r3] The second stage is a verifier model that receives the original citation and the matched record, and "assigns a numeric score" from 0 to 10 together with the main discrepancies.[^r4] The score is then mapped to one of three labels (exact, minor, major) by two thresholds. The third stage is a reviewer pass for one specific case: an identifier such as a URL or arXiv ID resolves to a real paper, but the title similarity is low. The paper applies it to "suspicious cases where the retrieved candidate comes from an identifier-based" source.[^r5]

What was measured. On a held-out test set of 792 citations drawn from a 982-citation physics benchmark with controlled corruptions,[^r6] the pipeline reached "88.7 macro-F1, and 88.9% accuracy."[^r7] The authors compare it with direct LLM baselines, with and without web search and with and without few-shot examples. The strongest baseline, Claude Sonnet 4.6 with web search and few-shot examples, "reaches 82.9 macro-F1 and 83.2% accuracy."[^r8] The authors read the gap as evidence that "grounded retrieval and structured comparison are more reliable than prompting LLMs to judge citation validity directly."[^r9] The ablations split the gain between the two non-model parts. "Removing it reduces macro-F1 by 7.0 points" for the web-search fallback,[^r10] and without the reviewer, "macro-F1 drops from 88.7 to 84.7."[^r11]

The label boundaries are not fixed by the prompt. The verifier emits a graded score, and the cut points are tuned afterwards: "The selected threshold pair is the one that maximizes support-weighted F1 across the three classes."[^r12] Because the score is stored separately from the label, the paper says re-calibration needs no new retrieval or model calls: "This separation makes re-calibration inexpensive."[^r13]

What survives the transfer (my inference, not the paper's claim). The step that carries the gain is the separation of lookup from judgment. The model is asked whether two records agree, which it can do from the text in front of it, rather than whether a work exists, which it can only answer from what it happens to remember. The lookup needs an index that holds the thing being checked. Where a reference has no record anywhere, a missing match is the signal, and the comparison has nothing to compare against.

## Limits

- The benchmark is synthetic. "our benchmark is synthetic and focused" on one field, and the corruptions were produced by a single model under controlled prompts.[^r14]
- Only physics was tested: "is limited to physics, however, and future work" is needed before the claim transfers to other fields.[^r15] The paper expects transfer because the metadata is domain-independent, but that expectation is not tested here.
- The retrieval and the verifier are not separated cleanly. The authors state that their experiments "do not isolate" "database retrieval against web-search-only retrieval" under an identical verifier, so the advantage over direct web-search baselines cannot be credited only to the database cascade.[^r16]
- A valid identifier does not guarantee a faithful reference. "high title similarity can still hide metadata" drift, and the reviewer exists for the reverse case as well.[^r17] This is the case the third stage addresses, not one the design removes.
- Cost. The paper notes the pipeline "adds latency" relative to one model call, and it is a multi-stage pipeline.[^r18]
- The cut points (1.25 and 7.25) were tuned on a validation split with the same verifier that was then evaluated. I did not read the verifier-model sensitivity section (5.3), so whether these thresholds hold for another model is not established here.
- The headline numbers come from the authors' own benchmark and have not been replicated.

## Related

- [[schema-vocabulary-retrieval]] — the same move: retrieve the valid vocabulary so the generator chooses among real entries instead of recalling them
- [[data-grounded-reference-disambiguation]] — resolves a referent by lookup over a source the answerer can read, without asking; here the source is a scholarly index
- [[scaled-verification-labeling]] — another use of verifier output as a label, with a meta-filter in place of a retrieved record as the check

[^r1]: doi-10-48550-arxiv-2605-27700 — "validity from memory; it is used as a comparator"
[^r2]: doi-10-48550-arxiv-2605-27700 — "We therefore treat retrieval as candidate generation"
[^r3]: doi-10-48550-arxiv-2605-27700 — "accepts a candidate only if it passes a minimum title-similarity"
[^r4]: doi-10-48550-arxiv-2605-27700 — "assigns a numeric score"
[^r5]: doi-10-48550-arxiv-2605-27700 — "reviewer pass for suspicious cases where the retrieved candidate comes from an identifier-based"
[^r6]: doi-10-48550-arxiv-2605-27700 — "We construct our benchmark from a pool of 982"
[^r7]: doi-10-48550-arxiv-2605-27700 — "88.7 macro-F1, and 88.9% accuracy"
[^r8]: doi-10-48550-arxiv-2605-27700 — "which reaches 82.9 macro-F1 and 83.2% accuracy"
[^r9]: doi-10-48550-arxiv-2605-27700 — "more reliable than prompting LLMs to judge citation validity directly"
[^r10]: doi-10-48550-arxiv-2605-27700 — "Removing it reduces macro-F1 by 7.0 points"
[^r11]: doi-10-48550-arxiv-2605-27700 — "Without the reviewer, macro-F1 drops from 88.7 to 84.7"
[^r12]: doi-10-48550-arxiv-2605-27700 — "The selected threshold pair is the one that maximizes support-weighted F1 across the three classes."
[^r13]: doi-10-48550-arxiv-2605-27700 — "separation makes re-calibration inexpensive"
[^r14]: doi-10-48550-arxiv-2605-27700 — "our benchmark is synthetic and focused"
[^r15]: doi-10-48550-arxiv-2605-27700 — "is limited to physics, however, and future work"
[^r16]: doi-10-48550-arxiv-2605-27700 — "database retrieval against web-search-only retrieval"
[^r17]: doi-10-48550-arxiv-2605-27700 — "high title similarity can still hide metadata"
[^r18]: doi-10-48550-arxiv-2605-27700 — "compared to a single LLM call and may be less"
