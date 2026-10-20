---
description: "One LLM call emits a relation sequence and a deterministic breadth-first traversal supplies the answers, so every answer is a graph path; smaller planners lose accuracy at depth three."
aliases: ["LLM-planned traversal", "relation-sequence planning", "plan-then-execute KG traversal", "LLM-guided relation planning"]
sources: ["arxiv-2511-19648"]
---
# Relation-plan-then-traverse

A model can answer a multi-hop question by writing a program instead of an answer. The program is a short list of relation names, one list per hop. A breadth-first search then walks the knowledge graph from the question's start entity, following only the predicted relations at each hop. The paper describes the model as "translating natural language into a relational program"[^r1]: it maps the phrasing of the question onto relation types, and the traversal produces the answer set. The answers are the nodes the walk reaches, so "the BFS engine ensures that the resulting answers are grounded"[^r2] in the graph. Every answer is the end of a path of existing edges. That is a stronger property than the answer merely being plausible.

The cost argument is about calls. Earlier graph-planning methods were criticised because "each traversal step requires a separate LLM call"[^r3]. Here the model is called once per question and emits the whole relation sequence, and the graph does the hops.

On MetaQA the contrast is measured along one axis, the same model with and without the traversal. Asked for answers directly, GPT-5-mini reaches "(micro-F1 = 0.28, hit rate = 0.56)" on 1-hop questions, and none of the correct answers appear among its top-50 candidates "for a large portion of the test questions."[^r4][^r4b] Under planning, the same model "achieves nearly perfect performance on 1- and 2-hop" questions, with micro-F1 between 0.91 and 0.98, and it "still sustains strong 3hop performance (0.92)."[^r5a][^r5]

Depth is where the smaller planners fail. Qwen3-30B scores 0.98 at 2 hops but "its accuracy collapses at 3-hop (0.60)."[^r6] The paper's explanation is that this "may stem from compounding errors in relation sequencing."[^r7] My reading of that: a wrong relation at hop one sends the walk into the wrong neighbourhood, and the later hops then return well-formed answers that are wrong. The paper gives the phrase, not the mechanism; the mechanism is my inference.

The planning skill can be moved to a small model. A Qwen3-4B fine-tuned with LoRA on the large model's traces, using "only about 10% of the training data," "recovers most of GPT5-mini"[^r8][^r9] accuracy, with micro-F1 of 0.91, 0.99 and 0.91 at 1, 2 and 3 hops. The paper's account of why this works is that "Predicting relations instead of answers isolates the reasoning" pattern from the particular entities named.[^r10] What survives outside this setting is the division of labour: the model supplies the shape of the path and the graph supplies the instances. What does not carry over by itself is the closed relation vocabulary that makes a plan checkable in the first place.

## Limits

- Entity linking was supplied. The start entity is read from the question's brackets: "starting from the entity identified via bracketed mention."[^r12] The planner never has to find the entity, and "evaluation is conducted on a single domain (movies) with"[^r13] exact entity linking. Noisy or incomplete resolution is not tested.
- The relation vocabulary is small. "nine relation types are relatively few compared to large-scale" knowledge graphs such as Freebase or Wikidata.[^r11] The discussion claims that other graphs "also exhibit limited relation diversity relative to node count,"[^r14] but that is asserted, not measured.
- Depth is fixed in advance. The planner receives the question, the relation set and the hop count, "LLM M, hops k."[^r15] A plan whose length is wrong answers at the wrong depth, and the paper does not test that failure. My reading of the algorithm is that the planner never sees the neighbourhood the question touches, only the vocabulary.
- Grounded means present in the graph, not correct. The paper's definition is that "every answer exists in the KB."[^r16] An answer can satisfy that and still be wrong, if the graph lacks the right edge or the plan names a wrong relation. Coverage of a graph with missing facts was not measured here.
- The distillation result is one teacher, one student and one domain, on a benchmark with synthetic questions.

## Related

- [[text-free-triplet-answering]] — the hop-by-hop alternative: an LLM walks a triple store one sub-question at a time, where the plan here is written once before the walk.
- [[relation-driven-hop-count-selection]] — also fixes the depth before a walk; there the depth is read from the relations a traversal activates, whereas a plan of fixed length takes its depth from the question alone.

[^r1]: arxiv-2511-19648 — "translating natural language into a relational program"
[^r2]: arxiv-2511-19648 — "the BFS engine ensures that the resulting answers are grounded"
[^r3]: arxiv-2511-19648 — "each traversal step requires a separate LLM call"
[^r4]: arxiv-2511-19648 — "(micro-F1 = 0.28, hit rate = 0.56)"
[^r4b]: arxiv-2511-19648 — "for a large portion of the test questions"
[^r5a]: arxiv-2511-19648 — "achieves nearly perfect performance on 1- and 2-hop"
[^r5]: arxiv-2511-19648 — "still sustains strong 3hop performance (0.92)"
[^r6]: arxiv-2511-19648 — "but its accuracy collapses at 3-hop (0.60)"
[^r7]: arxiv-2511-19648 — "may stem from compounding errors in relation sequencing"
[^r8]: arxiv-2511-19648 — "only about 10% of the training data"
[^r9]: arxiv-2511-19648 — "it recovers most of GPT5-mini"
[^r10]: arxiv-2511-19648 — "Predicting relations instead of answers isolates the reasoning"
[^r11]: arxiv-2511-19648 — "nine relation types are relatively few compared to large-scale"
[^r12]: arxiv-2511-19648 — "starting from the entity identified via bracketed mention"
[^r13]: arxiv-2511-19648 — "evaluation is conducted on a single domain (movies) with"
[^r14]: arxiv-2511-19648 — "also exhibit limited relation diversity relative to node count"
[^r15]: arxiv-2511-19648 — "LLM M, hops k"
[^r16]: arxiv-2511-19648 — "every answer exists in the KB"
