---
description: "Separating a query's relational core from its surface syntax, modalities and conventions lets queries be compared by the relational pattern they express, not by their text."
aliases: ["abstract relational query language", "ARQL", "semantics-first query representation", "core, modality and convention split"]
sources: ["arxiv-2512-12957"]
---
# Relational core, modality and convention

A query in a relational language can be split into three layers. The first is a relational core, "the compositional structure that determines intent": the way a query composes its base relations to define what is asked.[^c1] The second is a set of modalities, which are alternative representations of that same core tailored to different readers. The paper's examples are a comprehension-style text, a tree for machine reasoning, and a diagram for humans.[^c2] The third is a set of conventions, orthogonal environment-level parameters under which the core is interpreted, such as set or bag semantics and the treatment of nulls.[^c3]

The point of the split is comparison. Surface syntax is a weak proxy for what a query asks: "semantically equivalent queries can differ substantially in syntactic structure, while" syntactically similar queries may encode different semantics.[^c4] Benchmarks that score generated queries by "exact string match or execution match" miss those relations.[^c5] If the core is separated, two queries written in different languages can be compared by which relational patterns they share, and "comparing languages" becomes a question of which patterns each supports and which conventions it chooses.[^c6] A convention is a design decision that changes behaviour without changing the core. The paper's example is that an aggregate initialises with null in SQL but with 0 in another language. "It is a convention that does not affect" the way the query composes its parts.[^c7]

The same split reassigns where usability lives. Usability depends less on which language is chosen than on which modality is presented: the authors write that it depends "more on choosing an appropriate modality."[^c8] The reason given is a change of reader. "Fewer people will write queries directly in the future; more people will read them and try to make sense of them."[^c9] For humans, the paper cites "initial evidence" that a diagrammatic modality "can be read faster and more accurately than SQL".[^c10] For machines, the tree form exposes binding, scoping and grouping, so that "models generate a structurally constrained representation, which can be validated" before it is rendered back to SQL.[^c11] The same move gives an evaluation: scoring generated queries "at the semantic-structure level rather than at the surface-syntax level" is what the authors propose for intent-based evaluation.[^c12]

## Limits

The paper proposes the split and one formal instance, Abstract Relational Calculus. It does not measure the human side itself. The "initial evidence" for diagrams rests on earlier user studies that the paper cites, and the authors state that "questions about relative usability need to be solved with" "reproducible, task-oriented user studies".[^c13]

The coverage claim is planned, not proved. The authors "plan to prove coverage results" for a fragment of SQL that includes correlated queries, and they list ordering and nested relations as open extensions.[^c14] The calculus also "assumes flat relational inputs and outputs", which leaves out some of what production queries do.[^c15]

The orthogonality of conventions is asserted, and the paper's own notation shows a limit. The diagram draws existential scopes that were previously omitted, because scope only needed fixing under negation, and the authors note that "this changes under bag semantics and aggregation."[^c16] So a convention can leak into the notation even when it does not change the core.

Whether a relational intermediate form helps language models generate queries is left open: "an open question is whether ARC/ALT can indeed serve" as an intermediate target for NL2SQL.[^c17]

The paper concerns formal query languages. Carrying the split over to natural-language questions, where a question's core is what it asks and its modalities are how it is phrased for a reader, is my extrapolation. The paper does not make it.

## Related

- [[intention-abstraction]] — a written intermediate that separates task comprehension from solution design, the same kind of split applied to code generation (my parallel, not the paper's).
- [[confidence-discounted-composite-score]] — a reference-free SQL score built from separate semantic components, an instance of judging generated SQL by what it means rather than its text.

[^c1]: arxiv-2512-12957 — "the compositional structure that determines intent"
[^c2]: arxiv-2512-12957 — "modalities (alternative representations of that core tailored to different audiences)"
[^c3]: arxiv-2512-12957 — "orthogonal environment-level semantic parameters under which the core is interpreted, e.g., set vs."
[^c4]: arxiv-2512-12957 — "semantically equivalent queries can differ substantially in syntactic structure, while"
[^c5]: arxiv-2512-12957 — "criteria such as exact string match or execution match."
[^c6]: arxiv-2512-12957 — "Comparing languages"
[^c7]: arxiv-2512-12957 — "It is a convention that does not affect"
[^c8]: arxiv-2512-12957 — "more on choosing an appropriate modality."
[^c9]: arxiv-2512-12957 — "fewer people will write queries directly in the future; more people will read them and try to make sense of them."
[^c10]: arxiv-2512-12957 — "can be read faster and more accurately than SQL"
[^c11]: arxiv-2512-12957 — "models generate a structurally constrained representation, which can be validated"
[^c12]: arxiv-2512-12957 — "intent-based evaluation and comparison of generated queries at the"
[^c13]: arxiv-2512-12957 — "reproducible, task-oriented user studies"
[^c14]: arxiv-2512-12957 — "we plan to prove coverage results"
[^c15]: arxiv-2512-12957 — "assumes flat relational inputs and outputs"
[^c16]: arxiv-2512-12957 — "this changes under bag semantics and aggregation"
[^c17]: arxiv-2512-12957 — "an open question is whether ARC/ALT can indeed serve"
