---
description: "A memory that distills turns into artifacts fixes what is relevant at write time, before any question exists; keeping raw text defers that choice to query time, where the question can guide it."
aliases: ["write-time relevance decision", "deferred relevance selection", "query-independent storage selection"]
sources: ["arxiv-2601-00821", "arxiv-2511-23304", "arxiv-2511-21726"]
---
# Write-time relevance commitment

A memory that must answer later questions has to decide what to keep, and the point at which it decides is a variable in its own right. An extractor that turns each conversation turn into typed artifacts makes the decision when the turn is stored: "Extraction commits to relevance before the question exists."[^c1] "An extractor decides at write time what survives; whatever it discards is unrecoverable at read time."[^c2] A store that keeps verbatim chunks makes no such decision at write time. "Verbatim chunks defer the decision to query time, when the question can guide"[^c3] the selection.

The mechanism follows from this timing. An extractor works without the question that will later be asked, so it keeps what it judges worth keeping, and a detail it did not judge worth keeping is absent from the store at every later point. The paper measures where this bites. Among questions that the chunk store answers and the artifact store fails, "69.0% of diagnosable chunkpass/artifact-fail questions involve facts surviving" in no deliberately extracted artifact.[^c5] The worked example is a temporal question whose answer sits in a dated source turn. The chunk store keeps that turn; the artifact store answers only if the extractor happened to log the date. The author calls such errors "avoidable by not extracting."[^c6]

The same timing explains where extraction does not lose. The paper's synthetic multi-hop probe authors each planted fact as exactly one artifact and asks questions that recombine two or three of them. There artifacts win, and the author says so: "when facts are pre-shaped to the schema, artifacts" win.[^c4] When the relevant units are known before the questions arrive, deciding at write time costs nothing. What separates the two regimes is whether the questions are known at write time, not whether the store holds structure.

For someone formulating questions against a memory, the consequence is about recoverability. A question can only draw on what the store kept. A better-phrased question does not recover a detail that the extractor discarded, while a raw store leaves the detail available for a question that asks for it. This is my inference from the write-time argument; the paper does not test reformulation against a fixed extracted store.

A model's internal structure shows the same split. In audio-visual question answering the scene graph is built without the question: "is not used when constructing a scene graph, so the same annotation can support multiple questions."[^c8] The authors give a reason for leaving the question out, that "Incorporating textual information may introduce bias or unintended priors that could interfere with accurate scene graph prediction."[^c9] The question is admitted only at a later step, where the selection module "only filters the query-relevant triplets within each individual segment."[^c10] So the structure is committed before any question, and the choice among its parts is made at query time, as in a verbatim store. The graph is a structure, not raw text, so this is not a return to the raw-chunk case. My inference is that the two papers together suggest a general pattern: commit the structure at write time, defer the selection to read time. The audio-visual paper does not test that pattern against an extractor that sees the question.

The same timing argument reappears in a search setting. SUMER treats goal-agnostic compression as the weak point because it is applied "for a downstream query unknown at compression time", and so it keeps the raw conversation and searches it when a question arrives.[^c11] On LoCoMo the trained search agent beats the compression baselines, which the authors describe as "nearly doubling judge accuracy relative to the strongest compression-based baseline."[^c12] This is evidence about where the decision sits, not about when it is made: the paper compares a raw store with compressed ones and does not vary when an extractor commits to what it keeps. The search measurements and their limits are in [[compressed-memory-versus-raw-retrieval]].

## Limits

- The timing is the author's argument for a result measured on another variable. The paper swaps the stored representation and holds everything else fixed; it does not vary when the relevance decision is made. A question-aware extractor, which would see the question before deciding what to keep, is not among the pipelines in the text read, so whether it closes the gap is open here.
- The 69.0% figure is a diagnostic over the questions on which the two stores disagree, not an intervention on the extractor. It says where the artifact store's failures sit in these two benchmarks, not how often such failures occur in natural conversation generally.
- The regime is narrow: the paper confines its claim "to the stateless," training-free setting.[^c7] A store that revisits and rewrites its contents over time is a different case, and this note does not cover it.

## Related

- [[compressed-memory-versus-raw-retrieval]] — the same raw-versus-compressed contrast, measured on behavior logs; this note names the timing of the relevance decision as one account of why compression loses.
- [[multi-modal-scene-graph]] — a question-blind audio-visual graph whose triplets a question then selects among, the same commit-then-select split inside a model.
- [[pre-retrieval-fidelity-selection]] — chooses the input fidelity for each question before retrieval, which is the query-time side of a choice this note places at write time (my inference: the two are not studied together in either source).

[^c1]: arxiv-2601-00821 — "Extraction commits to relevance before the question exists."
[^c2]: arxiv-2601-00821 — "whatever it discards is unrecoverable at read time"
[^c3]: arxiv-2601-00821 — "Verbatim chunks defer the decision to query time, when the question can guide"
[^c4]: arxiv-2601-00821 — "when facts are pre-shaped to the schema, artifacts"
[^c5]: arxiv-2601-00821 — "69.0% of diagnosable chunkpass/artifact-fail questions involve facts surviving"
[^c6]: arxiv-2601-00821 — "errors avoidable by not extracting"
[^c7]: arxiv-2601-00821 — "confined to the stateless,"
[^c8]: arxiv-2511-23304 — "is not used when constructing a scene graph, so the same annotation can support multiple questions"
[^c9]: arxiv-2511-23304 — "Incorporating textual information may introduce bias or unintended priors that could interfere with accurate scene graph prediction."
[^c10]: arxiv-2511-23304 — "only filters the query-relevant triplets within each individual segment"
[^c11]: arxiv-2511-21726 — "for a downstream query unknown at compression time"
[^c12]: arxiv-2511-21726 — "nearly doubling judge accuracy relative to the strongest compression-based baseline"
