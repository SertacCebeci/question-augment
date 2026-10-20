---
description: "Structuring raw search results into source-tagged evidence bound to outline nodes, then critic-ranking them before drafting, targets context rot; the gains are reported only in ablations."
aliases: ["evidence audit", "Evidence Audit Module (EAM)", "audited memory", "evidence units bound to outline nodes", "context audit before drafting"]
sources: ["arxiv-2511-18743"]
---
# Evidence audit for context structuring

Retrieval fills an agent's context with raw results, and most of them are noise. The paper's claim is that this noise is what breaks drafting: "the noisy content dilutes factuality and consistency, causing the context rot phenomenon and poor traceability during drafting."[^e1] The remedy it proposes is to audit the retrieved material before the report is written from it, so that drafting draws only on structured, traceable sources.

The audit runs in two stages. In the first, each search's raw results are normalized and "structured into evidence units with" source, timestamp and confidence fields, and persisted to a memory store.[^e2] After each search the outline is updated, so that new evidence is aligned with specific nodes. The structuring step organizes the searched material into a hierarchy that removes duplicates and allows node-level retrieval. A summarization model then condenses each evidence cluster into "concise, source-cited abstracts that preserve signal and improve factual precision."[^e3]

In the second stage, drafting produces node-level text first. A critic then ranks the candidate evidence in the audited memory "by relevance, quality, timeliness, and consistency" and selects the high-salience items, so that each claim is bound to a specific audited item: "ensuring every claim and visualization is traceably linked to audited evidence."[^e4][^e5] The module's stated effect on context is that it "reduces contamination, and ensures each claim and visualization is verifiable."[^e6]

The part that transfers is the separation of two things an agent does with search output: it can keep the raw trace in the drafting context, or it can reduce the trace to units keyed by the outline node they serve. The first grows with every search. The second is bounded by the outline. My inference is that a drafter working from node-keyed units sees less of the rest of the search than one reading the whole trace, which is the property the authors call a guard against context rot.

The paper measures the audit only as an ablation. On DeepConsult, the average score I read from Table 3 is 3.65 with neither module and 5.45 with the audit alone, against 6.82 with both modules.[^e7] On GAIA text-only, accuracy goes from 58.3% (60 of 103) to 64.1% (66 of 103) with the audit alone, and to 68.9% (71 of 103) with both. On GAIA the authors read the audit's standalone gain as the larger of the two, "with EAM delivering a slightly larger standalone improvement than VCM."[^e8][^e9]

## Limits

- The audit is one module with four parts (normalization, structuring, summarization, critic ranking). No ablation separates them, so the gain cannot be assigned to the summarizer, the ranker or the outline binding (my inference).
- Summarization sits between the source and the drafter. The drafter reads abstracts, and the passages read do not measure what the abstracts drop. A claim traced to an abstract is traced one step removed from its source.
- "Context rot" is asserted by the authors as the failure the audit prevents. The paper does not measure rot directly; it measures end scores with and without the module.
- No variance across runs is reported. On GAIA the audit-only gain is five cases of 103, and the passages read do not say whether it exceeds run-to-run spread.
- The confidence and timeliness fields are described but their assignment is not explained in the passages read, and no experiment varies them.
- The benchmarks are the authors' own tasks with one backbone, Gemini-2.5-Pro, per the paper's setup. A search that returns few or no relevant items gives the audit little to structure; the passages read do not test that case.

## Related

- verifiable-checklist-before-search — the paper's other module: the checklist fixes the outline nodes that the audit then files evidence under
- [[context-register]] — a slot register of plan state that keeps a step-to-step loop from filling the window; the audit does the same for evidence, keyed by outline node instead of by plan slot
- [[traceable-evidence-chain]] — the claim-to-source trail that an audit makes checkable; the audit adds structuring and summarization before drafting, which the trail itself does not cover
- [[context-pollution-naive-tool-addition]] — unpruned tool output lowering performance; the audit is a pruning step applied to exactly that kind of input
- [[hierarchical-context-isolation]] — bounds a planner's context with step-response summaries from workers; a different split of the same context-growth problem

[^e1]: arxiv-2511-18743 — "the noisy content dilutes factuality and consistency, causing the context rot phenomenon"
[^e2]: arxiv-2511-18743 — "structured into evidence units with"
[^e3]: arxiv-2511-18743 — "concise, source-cited abstracts that preserve signal and improve factual precision"
[^e4]: arxiv-2511-18743 — "audited memory by relevance, quality, timeliness, and consistency"
[^e5]: arxiv-2511-18743 — "ensuring every claim and visualization is traceably linked to audited evidence"
[^e6]: arxiv-2511-18743 — "reduces contamination, and ensures each claim and visualization is verifiable"
[^e7]: arxiv-2511-18743 — "Table 3: Ablation of the VCM and EAM on DeepConsult."
[^e8]: arxiv-2511-18743 — "with EAM delivering a slightly larger standalone improvement than VCM"
[^e9]: arxiv-2511-18743 — "Table 4: Effect of the VCM and EAM on GAIA (text-only)."
