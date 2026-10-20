---
description: "A temporal hop is one temporal expression a question must resolve, so a question with several timestamps or intervals is multi-hop; this is not the graph hop of knowledge-graph QA."
aliases: ["temporal hops", "multi-hop temporal question", "temporal expression count", "time-expression hops"]
sources: ["doi-10-48550-arxiv-2311-09821"]
---
# Temporal hop count

In temporal question answering, "multi-hop" has a meaning of its own. The Complex-TR paper defines a multi-hop temporal question as one that contains multiple temporal expressions, and a temporal expression is either a timestamp or a time interval.[^t1] The count is of time expressions in the question, not of edges in a graph. The authors separate it from the graph hops of knowledge-graph QA, where the number of hops is "the number of triples required to answer the question," and they claim to be "the first to differentiate temporal hops from KG hops."[^t2]

The distinction is about what a question has to resolve. A question with one anchor is one hop. "What team did Kobe Bryant play for in June 2010?" carries a single timestamp. "What awards did Kobe Bryant win when he was playing for the LA Lakers?" needs both the start and the end of a roughly twenty-year career, so it has two temporal expressions and is multi-hop.[^t3] A time can also be reached by composition rather than stated outright. The paper's example is a year that "can be explicitly expressed as a numerical value (1-hop expression)" or "implicitly as t1 + ∆t1 + ∆t2", a birth date plus two offsets.[^t4] The same target can therefore be asked with one expression or with a chain of them, and the chain is the harder formulation.

The paper treats the count as a formulation choice. Its multi-hop L2 questions come in two variants: an interval, and a reference time plus "the temporal difference between the reference time and the query time." In the second variant the answerer must infer the query time from the offset, which is one more step than reading a timestamp off the question.[^t5]

The measured effect is in the paper's ReasonQA experiments, where the context is structured facts from a knowledge base. There "multi-hop temporal reasoning is much more challenging compared to single-hop reasoning, and most tested models have lower performance on multi-hop temporal reasoning."[^t6] The authors call it "a common weakness for current LLMs."[^t7]

## Limits

- The hop count is set by how the dataset was built. Complex-TR's single- and multi-hop questions were generated from templates over the same kinds of facts, so the comparison is not a controlled change of hop count alone. The paper made only "a small number of 1-hop questions with the same temporal quintuples and contexts" for a fair comparison.[^t8]
- The measured gap is between single-hop and multi-hop items as a group. Whether the difficulty comes from the number of expressions, from how they compose, or from the answer count (the dataset also has multi-answer items) is not separated in the text I read.
- The result is on structured KB context. Open-domain retrieval changes the picture, and this note does not claim the same gap there.
- That a question with the same count of expressions in natural language would be as hard or as easy is my inference, not a measurement.

## Related

- [[tkgqg-constraint-count-degradation]] — the same temporal axis seen from question generation: adding temporal constraints or graph hops both lower faithfulness, at a comparable size
- [[temporal-constraint-taxonomy]] — a finer vocabulary for how one timestamp can constrain another; a question that uses more such relations carries more temporal expressions to resolve (my inference)
- [[relation-driven-hop-count-selection]] — the knowledge-graph counterpart: the depth a KG answer needs is read from the relations a traversal activates, while a temporal hop count is read from the time expressions the question contains
- [[max-over-references-scoring]] — the same dataset also has multi-answer questions, and the scoring rule for those is a separate question from how many hops a question has

[^t1]: doi-10-48550-arxiv-2311-09821 — "we define multi-hop temporal questions as questions that contain multiple temporal expressions"
[^t2]: doi-10-48550-arxiv-2311-09821 — "we are the first to differentiate temporal hops from KG hops for temporal question answering"
[^t3]: doi-10-48550-arxiv-2311-09821 — "Since Kobe Bryant had a 20-year career with the Lakers, it is a multi-hop question"
[^t4]: doi-10-48550-arxiv-2311-09821 — "explicitly expressed as a numerical value (1-hop expression)"
[^t5]: doi-10-48550-arxiv-2311-09821 — "the temporal difference between the reference time and the query time"
[^t6]: doi-10-48550-arxiv-2311-09821 — "multi-hop temporal reasoning is much more challenging compared to single-hop reasoning"
[^t7]: doi-10-48550-arxiv-2311-09821 — "multi-hop temporal reasoning is a common weakness for current LLMs"
[^t8]: doi-10-48550-arxiv-2311-09821 — "we also created a small number of 1-hop questions with the same temporal quintuples and contexts"
