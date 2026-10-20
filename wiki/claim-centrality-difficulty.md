---
description: "Query difficulty can be dialled by how central the chosen facts are to their source: the least central claims make the hardest query, and accuracy falls as the dial turns."
aliases: ["claim centrality difficulty", "thematic-relevance difficulty", "tangential-claim difficulty", "difficulty by claim relevance"]
sources: ["arxiv-2512-16553"]
---
# Claim-centrality difficulty

A query's difficulty can be set by which facts it asks for, relative to the source they came from, rather than by how many steps a search takes. The paper extracts short factual claims from each source article, embeds the full article and each claim, and ranks the claims by similarity to the article. "The most central claims appear at the top of the list, while increasingly tangential claims appear later."[^d1] A query is then built from a slice of that ranking. The mechanism is a dial with three settings: the three most central claims for an easy query, three mid-ranked claims for a medium one, and the three least related claims for a hard one.[^d2]

The paper states the assumption behind the dial: "We assume that a query becomes harder" when it is built from claims that are less tied to the article's theme.[^d3] The thing that changes between tiers is the claims chosen. The rest of the pipeline is the same for each tier: the paper says "their only difference is in the difficulty of final query."[^d4] So the tiers differ in one respect, the centrality of the claims.

This is a different axis from the usual ones. The paper contrasts its dial with existing criteria: "the length of reasoning chain, i.e. the number of hops in multi-hop queries," and the amount of missing information a search must recover.[^d5] A tangential claim is not necessarily more hops away from the answer. It is a fact the source mentions in passing, and a query built from such facts has less of the article's main theme to anchor a search.

The dial's effect is reported. "Across all agents, accuracy consistently declines as query difficulty increases."[^d6] The paper reads this as the fuzzy-search paradigm being harder for agents that do well on multi-hop benchmarks. The test set is split across tiers: 222 easy, 229 medium and 212 hard queries.[^d7]

What survives the move to other settings is the structure: a difficulty that is a property of the chosen content, fixed before any answerer is run, and measured by an embedding score that needs no human labels. My inference, not the paper's: the same structure could be applied to any source that can be split into claims with a relevance order. What does not transfer is the embedding model, which the paper takes as given, and the specific three-tier cut.

## Limits

- Centrality is an embedding similarity between each claim and the whole article. It is a proxy. The sections I read do not check it against human judgment of which claims are central, and do not show that a tangential claim is harder for a person as well as for the agents tested.
- Tangential claims may differ from central ones in more than relevance: they may be more specific, rarer, or less often repeated. The slices read do not separate centrality from these other properties, so a drop in accuracy cannot be credited to centrality alone.
- The ranking is per article. A claim that is central in one article may be peripheral in another, and no cross-article comparison of tiers is reported.
- Each tier is three claims from one source. The reported structure has three settings, not a curve. The slices read give no per-tier significance test, so the size of the gap between tiers is not established.
- The agents tested are six systems, three closed and three open. The paper does not show the decline for other retrieval setups.
- The dial sets difficulty for a query that is built to have one answer (see [[conjunctive-masked-criteria]]). Whether the same dial works for queries with several acceptable answers is not tested.

## Related

- [[conjunctive-masked-criteria]] — the query these claims form, whose target is the one page containing all of them.
- [[max-distractor-similarity-difficulty]] — another similarity-derived difficulty dial, but computed between a keyed answer and distractors in a closed-choice item, before any model is trained. Here the dial is the relevance of a claim to its own source.
- [[reverse-constructed-indirect-question]] — difficulty built into a question from its source, by adding conditions and removing handles.

[^d1]: arxiv-2512-16553 — "The most central claims appear at the top of the list, while increasingly tangential claims appear later."
[^d2]: arxiv-2512-16553 — "Hard queries use the three least relevant claims."
[^d3]: arxiv-2512-16553 — "We assume that a query becomes harder"
[^d4]: arxiv-2512-16553 — "processing, their only difference is in the difficulty of final query."
[^d5]: arxiv-2512-16553 — "include the length of reasoning chain, i.e. the number of hops in multi-hop queries"
[^d6]: arxiv-2512-16553 — "Across all agents, accuracy consistently declines as"
[^d7]: arxiv-2512-16553 — "222 easy, 229 medium, and"
