---
description: "Retrieval widened from top-ranked seeds along a structure graph, admitting near-misses that similarity misses, under a fixed budget, each with its reason for inclusion."
aliases: ["SpIDER", "spatially informed dense embedding retrieval", "graph-aware dense retrieval", "seed-centred neighbourhood expansion", "structural candidate expansion"]
sources: ["arxiv-2512-16956", "arxiv-2602-22219", "arxiv-2512-12117"]
---
# Structural neighborhood expansion

A similarity ranking orders items by how close each one is to the query, and it can leave out items that are close to a top-ranked item in the structure the items belong to but not close to the query. For code localization the paper states the premise directly: "buggy code modules are often spatially proximate within the codebase".[^c1] The failure it targets is the "near-miss", "where the correct function lies close structurally" to a highly ranked candidate without scoring well on its own.[^c2]

The mechanism has four steps. First, a dense ranking is computed as usual, and its top-C items become seeds. Second, from each seed a breadth-first search runs to depth d along containment edges in a code graph: "we perform breadth-first search up to depth d along" the containment structure.[^c3] Third, a neighbour is kept only if it also appears in a wider top-N pool of the dense ranking, so the walk stays "within semantically relevant regions of the graph".[^c4] Fourth, an LLM judges each surviving neighbour against the query and admits the ones it deems relevant; the seeds are always kept. The admitted items are placed into the output list by replacing the lowest-ranked non-seed items, so the list keeps its size K: "newly selected neighbors replace the lowest-ranked non-center nodes."[^c5]

Two properties follow from this design. The budget is fixed, so expansion trades an item that similarity ranked low for one that the structure places near a seed. And every admitted item carries a reason for being there, namely its relation to a seed: the method "attaches a structural reason for inclusion to each surfaced function", which the authors say makes "the candidate set auditable while keeping the retrieval budget fixed."[^c6] The distance that counts as structural is the number of graph hops; in their schema "two functions within the same class are 2 hops apart", and functions in different files are farther.[^c7]

The gain is reported as Recall@20 on three benchmarks spanning Python, Java, JavaScript and TypeScript. The abstract gives "by at least 13% relative (+0.05 to +0.12 absolute) along containment edges", with a larger gain once call edges are explored.[^c8]

A product catalogue gives a looser instance of the same move. In the STaRK product knowledge base, BM25 retrieval over product text was widened by one hop of edges, appending the neighbours linked by "also buy" and "also view" relations, and the paper reports a "significant improvement of the BM25 retrieval with the appending of" one-hop edge nodes.[^c13] The appended nodes sit "at end of top-k", so they are added to the list rather than swapped in for its lowest-ranked items.[^c14] The graph here is co-purchase and co-view, not containment, and the text read reports no seed filter or LLM judge on the added nodes. My inference: a neighbourhood of seeds helps in a graph that is not a syntax tree, but the text does not show that the fixed-budget swap, which is this note's mechanism, is the part that matters.

A third variant comes from a code-comprehension retriever for question answering rather than issue localization. It takes the top four files of a hybrid BM25-plus-dense ranking as seeds, and its one-hop step follows import edges: it "performs 1-hop BFS in Neo4j discovering IMPORTS neighbors", and "then boosts neighbor" scores instead of swapping items into a fixed list.[^c16] The paper reports that this expansion discovered "11.8 additional cross-file chunks per query" and "improv[ed] citation completeness by 24 percentage points" on its 180 questions.[^c17] My reading of the text is that the admission step differs from the containment method above: there is no LLM judge on the neighbours and the list is reordered by score, not held to a fixed-budget swap. The structural reason for inclusion is still the import edge, but the text does not measure what the boost displaces. The 24-point figure is the authors' own system on their own question set, and the reference to a 62% share of architectural queries is their classification, not an external one.

What survives the move out of code is the shape of the procedure: a seed set taken from a similarity ranking, a neighbourhood taken from a declared structure, a second filter on the neighbourhood, and a swap into a fixed budget. What does not survive is the graph itself. Containment in a syntax tree is formal and exact; the analogue of a containment edge between passages, claims or sources is not given by the paper and is my inference, not tested here.

## Limits

- The ceiling is the initial ranker. Some ground-truth functions are ranked far down by the dense model, and the paper says these "cannot be recovered regardless of graph structure". It reports 38% of SWEBench-Verified instances with such a target beyond the top 500.[^c9]
- The LLM filter is a second bottleneck. The paper reports that SpIDER "reaches 79–89% of the unfiltered neighborhood" recall, so part of the reachable recall is lost to filtering, and the cost is bounded by one LLM call per seed.[^c10]
- The main results use containment edges only. The stronger edge type, call edges, was "run on SWE-PolyBench only", so the other benchmarks do not show it.[^c11]
- The graph is built from the repository's primary language. "files in other languages are ignored, leaving cross-language edits out of reach."[^c12]
- Every test is software issue localization, with an issue text as the query and source functions as the answer units. Nothing here shows the mechanism for prose, dialogue or argument corpora, and the claim that it transfers there is mine.
- The product result is an append, not a fixed-budget swap, and it is one benchmark. The paper's gain on BM25 with one-hop edges does not measure the cost the swap imposes on items it displaces, which is the trade this note describes for code. Whether the two behave alike on product graphs is not tested in the text read.[^c15]

## Related

- [[dependency-closed-selection]] — the same complaint about per-item relevance; there a Steiner closure over declared dependencies adds connector items, here a bounded search from seeds adds near-misses and swaps out the lowest-ranked items.
- [[set-level-selection-over-relevance]] — both say that choosing items one by one by relevance misses properties of the set; here the property is structural nearness to a seed.
- [[two-stage-reranking]] — the LLM filter over the expanded pool is a second, costlier stage applied to a short list, as in reranking.
- [[semantic-proximity-bias]] — the pull toward similarity that leaves the structural near-misses out of a similarity-first ranking.

[^c1]: arxiv-2512-16956 — "buggy code modules are often spatially proximate within the codebase"
[^c2]: arxiv-2512-16956 — "where the correct function lies close structurally"
[^c3]: arxiv-2512-16956 — "we perform breadth-first search up to depth d along"
[^c4]: arxiv-2512-16956 — "This ensures exploration remains within semantically relevant regions of the graph"
[^c5]: arxiv-2512-16956 — "newly selected neighbors replace the lowest-ranked non-center nodes"
[^c6]: arxiv-2512-16956 — "candidate set auditable while keeping the retrieval budget fixed"
[^c7]: arxiv-2512-16956 — "Two functions within the same class are 2 hops apart"
[^c8]: arxiv-2512-16956 — "by at least 13% relative (+0.05 to +0.12 absolute) along containment edges"
[^c9]: arxiv-2512-16956 — "cannot be recovered regardless of graph structure"
[^c10]: arxiv-2512-16956 — "SpIDER reaches 79–89% of the unfiltered neighborhood"
[^c11]: arxiv-2512-16956 — "was run on SWE-PolyBench only"
[^c12]: arxiv-2512-16956 — "files in other languages are ignored, leaving cross-language edits out of reach"
[^c13]: arxiv-2602-22219 — "significant improvement of the BM25 retrieval with the appending of"
[^c14]: arxiv-2602-22219 — "Node augmentation appended at end of top-k and evaluated with reranker only"
[^c15]: arxiv-2602-22219 — "node relations enable better retrieval"
[^c16]: arxiv-2512-12117 — "performs 1-hop BFS in Neo4j discovering IMPORTS neighbors"
[^c17]: arxiv-2512-12117 — "improving citation completeness by 24 percentage points"
