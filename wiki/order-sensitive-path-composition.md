---
description: "A relation chain's code must change when its order or direction changes: a noncommutative binding keeps founded_by→CEO_of apart from its reverse, where commutative bindings merge them."
aliases: ["noncommutative relation binding", "order-aware path encoding", "block-diagonal GHRR binding", "order-sensitive path binding"]
sources: ["arxiv-2512-09369"]
---
# Order-sensitive path composition

A chain of relations is a sequence, and the sequence says something the bag of its relations does not. "Founded by X, then CEO of" and "CEO of X, then founded by" use the same two relations and point the reader in different directions. A system that matches a question against chains of relations therefore needs a code in which order and direction change the code. PathHD builds one by treating each relation as a block-diagonal unitary matrix and a path as the product of those matrices, block by block, with "binding applied left-to-right along the path."[^c1] Matrix multiplication does not commute, so the product for r1 then r2 is not the product for r2 then r1, and the encoding "preserves the order and directionality of relations, which are critical for multi-hop KG reasoning."[^c2] The query is encoded the same way: the authors "use the plan-based encoding in all main experiments," so the relation plan a question implies is bound into the same space, and candidates are ranked by cosine similarity to it.[^c3]

The contrast that gives the concept its content is with commutative bindings. The classical hyperdimensional bindings (XOR, element-wise products, circular convolution) do not distinguish order. The authors' reason is algebraic: these bindings "collapse r1 →r2 and r2 →r1 to similar codes and hurt directional reasoning."[^c4] A commutative code cannot tell a chain from its reverse, so a path that matches the query's words and entities but runs the wrong way scores as well as the right one.

The effect was measured by changing only the binding inside the same pipeline and reading Hits@1 on WebQSP and CWQ. GHRR, the noncommutative choice, scored highest. The commutative variants lagged, and the circular-convolution variant (HRR) gave modest gains over them.[^c5] The authors summarize the result as GHRR "reliably separating founded_by→CEO_of from its reverse."[^c6] The numbers in that table are about 86 Hits@1 on WebQSP for GHRR, about 85 for HRR and FHRR, and about 71 versus 70 on CWQ.[^c5]

A second property follows from the same algebra. Because the blocks are unitary, a composed path can be partly unbound, which "enables inspection of the contribution of individual relations in a composed path."[^c7] The paper uses this for its path-level rationales; the measurement of rationale quality is not in the slices read here.

What transfers from this work is a requirement, not the algebra. Any matcher that compares a question's relational structure with evidence has to keep the order and direction of the relations it compares, or it will treat a reversed relation as a match. The paper's own motivating case is of this kind: a system "selects a candidate path whose relation sequence does not match the query relation (“acquired_by”)," and returns a plausible but wrong answer.[^c8] For "which company acquired SolarCity?", the direction of the relation is part of what is asked. That the requirement holds beyond Freebase-style KG retrieval is my inference; the paper does not test it.

## Limits

The scope is narrow: "Our study is therefore scoped to Freebase-style KGQA,"[^c9] on three benchmarks that all draw on Freebase. Nothing here tests text, citation or other relational data.

The measured gap is small. GHRR beats HRR by about one point of Hits@1 on both datasets. The text I read reports no variance, interval or significance test for these figures, so the ranking is one run of one pipeline, not an established margin.[^c5] This is my reading of the slices, not a claim the paper makes or denies.

Order helps only if the candidate set contains the right chains. The query's relation plan comes from schema enumeration, "we use the plan-based encoding in all main experiments,"[^c10] so a wrong plan is encoded faithfully in its order. The paper's own failure case shows the limit: with K=2, "the vector-only choice can become brittle and select a high-scoring but" underconstrained path, and the LLM must recover the answer from what is left.[^c11] Preserving order does not guarantee that every needed constraint is among the retained paths.

The paper argues that commutative bindings collapse reversed chains. The slices I read show the outcome in accuracy, not the similarity of reversed-chain pairs under each binding. Whether the commutative codes are near-identical for reversed chains, or only less discriminative, is not established here.[^c6]

The latency and GPU-memory claims in the same paper concern a different property, the single LLM call and the absence of neural encoders. They do not support this note.

## Related

- [[relation-aware-retrieval]] — the path-wise level of relation questions, where the answer is a chain joining two papers and its order is part of the content
- [[relation-driven-hop-count-selection]] — the knowledge-graph case where the relations a traversal activates set the depth; this note is about what the chain's order encodes, not how long the chain is

[^c1]: arxiv-2512-09369 — "Binding is applied left-to-right along the path"
[^c2]: arxiv-2512-09369 — "the order and directionality of relations, which are critical for multi-hop KG reasoning"
[^c3]: arxiv-2512-09369 — "we use the plan-based encoding in all main experiments"
[^c4]: arxiv-2512-09369 — "which collapses r1 →r2 and r2 →r1 to similar codes and hurts directional reasoning."
[^c5]: arxiv-2512-09369
[^c6]: arxiv-2512-09369 — "GHRR yields the best Hits@1 on WebQSP and CWQ by reliably separating founded_by→CEO_of"
[^c7]: arxiv-2512-09369 — "This property enables inspection of the contribution of individual relations in a composed path"
[^c8]: arxiv-2512-09369 — "selects a candidate path whose relation sequence does not match the query relation"
[^c9]: arxiv-2512-09369 — "Our study is therefore scoped to Freebase-style KGQA"
[^c10]: arxiv-2512-09369 — "we use the plan-based encoding in all main experiments"
[^c11]: arxiv-2512-09369 — "the vector-only choice can become brittle and select a high-scoring but"
