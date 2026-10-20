---
description: "A multi-hop question can be grown one hop at a time: a question about an answer entity is merged in, and a link is kept only if removing that entity leaves it unanswerable."
aliases: ["bridging questions", "bridge-entity question chaining", "iterative multi-hop question expansion", "forward multi-hop question construction"]
sources: ["arxiv-2512-13573"]
---
# Bridging question chaining

A multi-hop question can be built forward, starting from a question that is already single-hop and extending it through the answer to that question. The MMhops benchmark builds its bridging questions this way. The paper says it generates them "iteratively by starting with" single-hop questions, and then "progressively increas[es] the reasoning depth" by adding hops.[^c1] Bridging questions "begin with the visual information from a single image and progressively link relevant entities and knowledge through multi-step chain reasoning."[^c2]

The loop has four moves. First, an answer is kept as the bridging entity only if it is a Wikipedia entity; the paper excludes "vague entity types such as numbers or years".[^c3] Second, a language model writes a new knowledge question from that entity's Wikipedia page, and the entity must be named in it: "the entity Ani is explicitly mentioned in the question".[^c4] Third, the new question is checked as an independent single-hop question: it "meets the criteria of an independent single-hop" question, which the paper tests by removal.[^c5] Fourth, the two questions are merged, with the current question placed where the entity was named: "replacing the reference to the" bridging entity.[^c6] The merged question is one hop longer, so depth is set by how many passes are run.

The removal check is the part that makes the result a chain and not a longer sentence. The paper's stated test is that "removing the entity Ani from" the sub-question "should render the question unanswerable."[^c7] My reading: if the sub-question could be answered without the bridge, the merged question would not really need the earlier hop, and its depth would be overstated. The check is a logical test on the link, not a search test on the finished question.

The result is a large, typed set. MMhops has 31,117 samples, of which 26,437 are bridging, and "70.8% of samples require three reasoning steps" with the rest needing four.[^c8] The answers are sorted into numerical, time and string types, and "standardized answer sets for each category" are built so that scoring can be automatic.[^c9] The generation and filtering are done by GPT-4o in "an automated data annotation and quality filtering process."[^c10]

The reverse order is treated in [[reverse-constructed-indirect-question]]: there a question is written from a source and then made harder. Both aim at questions a search cannot shortcut, but they check the result differently. Chaining checks each link logically, by whether the bridge is needed. The reverse construction checks by search and by a model filter. Neither source compares the two at equal depth; that comparison is my inference, not a finding.

## Limits

- The removal check is described, not measured. The sections read report no count of sub-questions the check rejected and no human check of whether accepted links really need the bridge. Whether the check blocks shortcuts is not shown.
- Only entity answers can be chained. Numbers and years are excluded as bridges, so a chain cannot pass through a quantity, and the paper does not say how much of the pool that removes.
- Depth comes from the number of passes, and difficulty is judged by model accuracy. The paper does not separate a deeper chain from a harder one for a human reader, so "depth 3 to 4 is challenging" rests on model results alone.
- Generation used GPT-4o from Wikipedia pages. The paper does not assess whether the merged wording reads as a natural question.
- Answers are reduced to short strings, numbers or times so that scoring is automatic. That is the same trade-off that limits the reverse construction, and it removes open-ended answers from the chain.

## Related

- [[reverse-constructed-indirect-question]] — the same goal of questions a search cannot shortcut, reached from the other end: source first, then indirection.
- [[bridge-conditioned-retrieval]] — the retrieval-side use of a bridge: the second hop is scored with the passage the first hop found.
- [[self-ask-decomposition]] — the answer-time counterpart: a model decomposes a question into sub-questions while answering, where chaining composes them at construction time.
- [[multi-hop-retrieval-path-difficulty]] — how hard the retrieval path that such a chained question forces is to follow.

[^c1]: arxiv-2512-13573 — "single-hop questions and progressively increasing the reasoning depth"
[^c2]: arxiv-2512-13573 — "progressively link relevant entities and knowledge through multi-step chain"
[^c3]: arxiv-2512-13573 — "excluding vague entity types such as numbers or years"
[^c4]: arxiv-2512-13573 — "the entity Ani is explicitly mentioned in the question"
[^c5]: arxiv-2512-13573 — "meets the criteria of an independent single-hop"
[^c6]: arxiv-2512-13573 — "replacing the reference to the"
[^c7]: arxiv-2512-13573 — "meaning that removing the entity Ani from"
[^c8]: arxiv-2512-13573 — "70.8% of samples require three reasoning steps"
[^c9]: arxiv-2512-13573 — "Construct standardized answer sets for each category"
[^c10]: arxiv-2512-13573 — "an automated data annotation and quality filtering process"
