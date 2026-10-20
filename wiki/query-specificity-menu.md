---
description: "Fixing one retrieval query fails at both ends of specificity; a per-turn menu of triple-component query forms lets the agent choose how broad each search is, though the menu itself is not ablated."
aliases: ["component-combination query guide", "query granularity menu", "triple-component query forms"]
sources: ["doi-10-48550-arxiv-2607-09092", "arxiv-2512-00772"]
---
# Query specificity menu

A question sent to a document index can be too broad or too narrow, and the two failures look different. The knowledge-graph verification paper states both ends for a triple (subject, predicate, object) turned into a search query. "an overly broad query returns documents that mention the entity but do not" contain the fact, and "an overly specific query may match no document when the corpus expresses the same fact with different wording."[^c1] A single fixed query therefore has no setting that avoids both failures, because the right specificity depends on how the corpus happens to phrase the fact.

The mechanism the paper proposes is a menu. A set of component combinations is shown to the agent as selectable options in the prompt, and "one combination is chosen per each turn to set the specificity and surface form of its query."[^c2] The menu draws on the triple's parts: the subject alone, the subject with the predicate, the subject with the predicate and object, and the same with a paraphrased predicate. In the paper's example the subject is "Hamlet", and the paraphrased predicate is "author" where the plain one is "written by". The choice is per turn, not fixed for a triple, so the agent can move from a broad query to a narrow one, or change the predicate wording, depending on what the previous search returned.

The revision rule follows the same logic. The agent does not write each query fresh after the first. It "reformulates the query toward a more suitable component combination or surface form."[^c3] When a query returns nothing useful, "the agent changes the formulation rather than repeats the same search."[^c4] The point is not that the menu finds more documents in any single turn. It is that a repeated search with the same form is ruled out by the rule, so each turn spends a retrieval on a different specificity or wording.

What survives the move from question answering to triple verification is the trade itself: a term that is too general pulls in documents that mention the entity without the fact, and a term that is too precise misses the document that states it in other words. What does not carry over unchanged is the menu. It exists because a triple has named parts. A free-form question has no such parts, so the menu would have to be built from some other decomposition.

A ladder of specificity can also be built from a ranked keyword list rather than from a triple. The SHRAG pipeline starts from the full list of keywords and drops the least important one at each step, so each rung is a broader query than the one above it, and all rungs are run and their results pooled.[^c7] The paper's stated reason is that this "progressive reduction method ensures diversity in the search queries while maintaining the thematic" focus of the original question.[^c7] The ladder is a fixed rule with no per-turn choice, so it trades the menu's selection for coverage of the whole ladder. Whether that beats a single well-chosen rung was not tested in the paper (my inference).

## Limits

The menu is argued, not measured in the parts of the text read. The ablation section varies the training stages only, comparing the untrained framework, the supervised stage and the supervised stage with GRPO. No run compares the menu with a fixed query, and no run removes the paraphrased-predicate forms. The benefit of the menu is therefore the authors' reasoning from the design, not a result (my reading).

The paraphrased predicate is a fixed lexical variant, and the text presents the menu as a way to "cover lexical variation of" the predicate.[^c6] Whether a menu built from one paraphrase per predicate reaches the wordings a corpus uses is not shown. The evaluation reports outcomes, not which forms the agent picked.

The retriever shapes the trade. The English benchmark uses a dense BGE retriever and the Korean enterprise benchmark an in-house lexical one.[^c5] A lexical retriever rewards the exact predicate wording more than a dense one, so the broad-versus-narrow balance would be expected to differ between them. The paper does not vary the retriever to test this (my inference).

The agent's choice is learned from a teacher. The supervised stage trains the small model on the last turn of correct teacher trajectories, which include the teacher's choice of form. The text does not report which combinations the trained agent actually chooses, so whether it uses the menu for specificity or mostly for one default form is open.

## Related

- [[failed-retrieval-reformulation]] — rewrites a sub-question after an empty result, with no fixed menu of forms; the menu here constrains the rewrite to a set of forms
- [[evidence-guided-query-reformulation]] — revises a multi-hop query from passages already read, where the change is driven by content and not by a set of forms
- [[query-adaptive-evidence-granularity]] — chooses the grain of evidence per question by chunk size; the menu here chooses the grain of the query's terms
- [[extra-search-penalty]] — the same agent's training charge for extra searches; the menu decides what each search asks, the penalty how many searches are spent
- [[conjunctive-keyword-recall-loss]] — the breadth question at the level of keyword operators: an AND-joined query narrows the set, and the ladder above widens it by dropping terms

[^c1]: doi-10-48550-arxiv-2607-09092 — "an overly broad query returns documents that mention the entity but do not"
[^c2]: doi-10-48550-arxiv-2607-09092 — "one combination is chosen per each turn to set the specificity and surface form of its query"
[^c3]: doi-10-48550-arxiv-2607-09092 — "more suitable component combination or surface form"
[^c4]: doi-10-48550-arxiv-2607-09092 — "the agent changes the formulation rather than repeats the same search"
[^c5]: doi-10-48550-arxiv-2607-09092 — "benchmark uses an in-house lexical retriever"
[^c6]: doi-10-48550-arxiv-2607-09092 — "cover lexical variation of"
[^c7]: arxiv-2512-00772 — "progressive reduction method ensures diversity in the search queries while maintaining the thematic"
