---
description: "Papers name a task beside the datasets used for it, so their text holds task-dataset pairs a catalogue lacks; the paper takes this co-location as a premise, not a measurement."
aliases: ["task-dataset co-mention", "task-to-dataset mapping gap", "co-location premise"]
sources: ["arxiv-2512-15363"]
---
# Task-dataset co-location in papers

A dataset catalogue describes a dataset by what its owner publishes about it. The paper's comparison point is Google Dataset Search, which "relies on data owners to publish structured metadata in" its index.[^t1] Such metadata says what a dataset is. It does not say what it was used for. A scientific paper says both: it names the task and the datasets it applied them to, in the same passage. That co-occurrence is the mechanism the KATS pipeline exploits.

The authors state the gap they target: "there exists no explicit mapping between scientific tasks and their associated" datasets.[^t4] Their premise is that the source documents "co-locate the mention of a dataset with a rich description of the specific task."[^t5] If that holds, a task-level query can be matched to datasets through the passages where they were applied, not only through the datasets' own descriptions. The names under which those datasets appear are a separate problem, handled in [[referent-name-fragmentation]].

The same co-occurrence supplies the benchmark. The authors write that scientific papers are "a natural source for this purpose, as they routinely describe both" the task and the datasets.[^t2] They add that "This implicit alignment enables us to" curate task-dataset pairs at scale.[^t3] A benchmark built this way inherits the premise it was built from.

The paper frames the whole problem as one of query formulation. KATS "interprets complex task descriptions and map them to relevant datasets," so the user no longer has to write a keyword query that already names the data.[^t6] The authors name the underlying difficulty as "there is a semantic gap between user intent and system."[^t7] The other way to close the same gap is to make the system's reading of a request an inspectable object, not a mapping it applies silently; that is the route in [[information-need-reification]].

## Limits

- The premise is stated, not tested. The paper does not measure how often a dataset in a paper is described together with its task, nor what share of datasets a catalogue would miss for lack of that description. The claim that papers supply the mapping rests on the premise alone.
- The premise is conceded to be conditional. The authors write that the extraction "might vary when applied to other types of documents" and the sentence continues "where this premise does not hold."[^t8] The concession is in the paper; it is not reported as a result.
- Dataset repositories, which list datasets without tasks, were handled by an extension the authors say still "requires a significant re-evaluation for other types of documents."[^t9]
- A dataset used in a paper but described without its task is not recovered by this route. My inference: co-location gives pairs the text states, not the full set of uses. The paper does not quantify this gap.
- The benchmark measures recovery of pairs that papers mention. It cannot show that the same retrieval serves a researcher whose task is not in the literature yet.

## Related

- [[referent-name-fragmentation]] — a co-located dataset is still named in several ways; the pairs are only as complete as the name resolution behind them.
- [[information-need-reification]] — the other route to the task-to-data gap: an inspectable interpretation of the request, instead of a learned mapping from the literature.

[^t1]: arxiv-2512-15363 — "relies on data owners to publish structured metadata in"
[^t2]: arxiv-2512-15363 — "a natural source for this purpose, as they routinely describe both"
[^t3]: arxiv-2512-15363 — "This implicit alignment enables us to"
[^t4]: arxiv-2512-15363 — "there exists no explicit mapping between scientific tasks and their associated"
[^t5]: arxiv-2512-15363 — "mention of a dataset with a rich description of the specific task"
[^t6]: arxiv-2512-15363 — "interprets complex task descriptions and map them"
[^t7]: arxiv-2512-15363 — "there is a semantic gap between user intent and system"
[^t8]: arxiv-2512-15363 — "where this premise does not hold"
[^t9]: arxiv-2512-15363 — "significant re-evaluation for other types of documents"
