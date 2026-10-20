---
description: "A query is split into semantic, spatial and temporal retrieval keys, each run against its own index of a 4D object memory; single keys give modest gains, the combination more."
aliases: ["4D retrieval keys", "semantic-spatial-temporal keys", "multi-axis retrieval keys", "typed retrieval keys"]
sources: ["arxiv-2512-15940"]
---
# Semantic, spatial and temporal retrieval keys

A question put to an embodied memory can be cut into three retrieval keys, one for each axis the memory is indexed on. In R4, each object-level entry has three parts: a natural-language description, a position, and a time span. The description is "a concise, full-text natural language description of the masked single object".[^c1] The position is the object's centroid, "Each centroid ctj is inserted as a" point in a shared SLAM map.[^c2] The time part is stored "with timestamps for appearance and disappearance".[^c3]

The retrieval side reads the query through the same three axes. The pipeline "decomposes natural language queries into semantic, spatial, and temporal keys".[^c4] The authors frame the derivation as an option for the VLM: "three types of retrieval keys from the query" are derived when the model judges its own answer unreliable.[^c5] Each key then runs against its own store. The semantic key is compared with stored descriptions "using cosine similarity in an embedding space".[^c6] The spatial key is applied to the map: "Spatial search operates on the SLAM map M in metric".[^c7] The temporal key filters the intervals: "Temporal search filters objects by matching their temporal intervals (TEM) against the temporal key".[^c8] A key, whether used alone or with others, returns complete records: it will "retrieve a complete set of 4D information from the corresponding search results".[^c9]

What distinguishes the keys is what they are matched against. A semantic key is "textual descriptors referring to object classes, attributes, states, or roles".[^c10] A spatial key relates the target to the agent's frame or to the world: "ego coordinate frame or in absolute world coordinates".[^c11] A temporal key is "absolute or relative temporal references and intervals".[^c12]

On a subset of the OpenEQA episodic-memory questions, the authors switch keys on and off. The result they draw from it is that "isolated cues are insufficient for robust episodic reasoning".[^c13] Adding the full combination "further increases performance (+3.9%)".[^c14] The authors read the gain as coming from the interplay: the three axes have to be combined before the method reaches its full potential, since the combination is what "of semantic, spatial, and temporal dimensions enables R4" to do.[^c15] The reading of the ablation is that the semantic axis is the anchor. Spatial and temporal cues without it "provide limited benefit", because "world knowledge semantics in the VLM act as the essential anchor".[^c16][^c17]

The keys also sit inside an answer-first gate. The model first tries the question from live perception and "it outputs the result immediately" when it judges the answer reliable; retrieval starts only otherwise.[^c18] Once retrieval has begun, the scope can widen, "allowing exploration of less certain but potentially relevant information".[^c19]

For the asker, the transferable point is that a question is better answered when its wording is turned into typed constraints (what kind of thing, where relative to what frame, when) and each constraint is matched against the store that holds that kind of fact. The text does not measure the decomposition itself: how often the VLM produces correct keys is not reported, only end accuracy. That gap is my reading, not the paper's claim.

## Limits

The ablation is small and single-backbone: it runs "on a subset of 184 EM-EQA questions", and "Gemma3-4B-IT [15] serves as the backbone VLM".[^c20][^c21] Its numbers are the authors' own, and the text gives no variance or repeated runs.

The authors name cost as a limit: "storage and retrieval latency remains a limiting factor".[^c22] The keys are only meaningful where there is an ego frame, a metric map and timestamps. A text-only corpus has none of the spatial or temporal axes, so the scheme does not carry over as it stands. That is my inference from the method, not a tested claim.

The multi-agent part is not separately tested by a benchmark, since "existing benchmarks do not enable dedicated evaluation of" collaboration through shared maps.[^c23] The keys are also not compared with other ways of splitting a query, such as sub-question decomposition, so the claim that typed keys beat them is not established here.

## Related

- [[retrieval-reasoning-procedure]] — axis B of its schema is the index structure; typed keys are one multi-index design inside that axis.
- [[self-ask-decomposition]] — splits a question into textual follow-up questions; typed keys split it along retrieval axes instead.
- [[uncertainty-guided-retrieval-triggering]] — the same answer-first gate: retrieve only when the draft answer is not trusted.
- [[spatial-semantic-eig-decomposition]] — also splits a search into spatial and semantic parts, but to score the next action, not to retrieve.
- [[epistemic-state-memory]] — another structured memory queried by retrieval; there the structured form scored below full context on a consulting corpus.

[^c1]: arxiv-2512-15940 — "SEM contains a concise, full-text natural language description of the masked single object"
[^c2]: arxiv-2512-15940 — "Each centroid ctj is inserted as a"
[^c3]: arxiv-2512-15940 — "with timestamps for appearance and disappearance"
[^c4]: arxiv-2512-15940 — "decomposes natural language queries into semantic, spatial, and temporal keys"
[^c5]: arxiv-2512-15940 — "three types of retrieval keys from the query"
[^c6]: arxiv-2512-15940 — "using cosine similarity in an embedding space"
[^c7]: arxiv-2512-15940 — "Spatial search operates on the SLAM map M in metric"
[^c8]: arxiv-2512-15940 — "Temporal search filters objects by matching their temporal intervals (TEM) against the temporal key"
[^c9]: arxiv-2512-15940 — "retrieve a complete set of 4D information from the corresponding search results"
[^c10]: arxiv-2512-15940 — "textual descriptors referring to object classes, attributes, states, or roles"
[^c11]: arxiv-2512-15940 — "ego coordinate frame or in absolute world coordinates"
[^c12]: arxiv-2512-15940 — "absolute or relative temporal references and intervals"
[^c13]: arxiv-2512-15940 — "isolated cues are insufficient for robust episodic reasoning"
[^c14]: arxiv-2512-15940 — "further increases performance (+3.9%)"
[^c15]: arxiv-2512-15940 — "of semantic, spatial, and temporal dimensions enables R4"
[^c16]: arxiv-2512-15940 — "temporal and spatial cues without semantic grounding (A7) provide limited benefit"
[^c17]: arxiv-2512-15940 — "world knowledge semantics in the VLM act as the essential anchor"
[^c18]: arxiv-2512-15940 — "it outputs the result immediately"
[^c19]: arxiv-2512-15940 — "allowing exploration of less certain but potentially relevant information"
[^c20]: arxiv-2512-15940 — "on a subset of 184 EM-EQA questions"
[^c21]: arxiv-2512-15940 — "Gemma3-4B-IT [15] serves as the backbone VLM"
[^c22]: arxiv-2512-15940 — "storage and retrieval latency remains a limiting factor"
[^c23]: arxiv-2512-15940 — "existing benchmarks do not enable dedicated evaluation of"
