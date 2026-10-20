---
description: "A sequence model writing an evidential path token by token can add edges the graph lacks: it completes sparse chains walkers cannot follow, but the path no longer records existing links."
aliases: ["walk-and-complete", "generative path completion", "path generation over missing edges"]
sources: ["doi-10-48550-arxiv-2201-06206"]
---
# Generated path completion

An evidential path is a chain of relations that justifies a predicted link. For a query (h, r, ?), the chain shows how the answer follows from the query: the paper's example infers "native language" for Albert from the relational path "born in" and "language".[^c1] Walk-based methods find such chains by training an agent to step along existing edges from h toward the answer. A chain with one absent edge is then unreachable, and the walker fails to return it. The paper names this the missing path problem: "the model fails to infer an evidential path" when edges are missing along it.[^c1]

The alternative in SQUIRE is to stop walking the graph. The query is the source sequence and the path is the target sequence of an encoder-decoder Transformer, which decodes the path token by token.[^c2] Each training triple "induces a supervised training sample" pairing the query with a path sampled from paths between h and t.[^c3] Because the decoder predicts the next token from learned embeddings rather than from a stored edge list, the output "does not explicitly rely on existing edges in the graph to generate the path sequence", and so it can "automatically infer missing edges along the path".[^c4] The gain on sparse graphs is attributed to this: it allows "the model to dynamically complete the graph while" writing the path.[^c5]

The completion has a cost that the mechanism itself creates. Where no path links h to t in training, the target is the edge itself, "to memorize the edge".[^c6] The training target is therefore sometimes a bare fact with no chain behind it. The paper says plainly that "there is no such supervision on the target path" in the first place, and it uses rules mined from the graph to pick better targets.[^c7] A generated path is thus a chain the model found plausible given its training, which may include links the graph never contained. Whether a given path is evidence is a separate question from whether the model produced it.

## Limits

- The paper's own plausibility measure is weak. Its authors write that "and reasonable rate are still low for practical concerns".[^c8] They report that on FB15K237 "there is no reasonable path in the graph for more than 70% of the triple queries in" their sample.[^c9] So for most queries no grounded chain exists to be recovered, and a completed one is a claim about a graph that does not contain it.
- The evaluation is "link prediction over six benchmark KGs", scored by ranking metrics.[^c10] No human or downstream use of the paths is tested beyond the paper's own readability checks.
- The head-to-head comparison caps paths at three hops, chosen "with baselines that all set maximum path length to 3".[^c11] Whether completion helps on longer chains is not shown.
- Whether a generated edge is correct cannot be read off the output. The paper reports the score of paths, not the rate at which a completed edge is false (my inference from the design).

## Related

- [[exposure-bias-in-self-rationalization]] — the same gap between training conditioning and inference-time generation, here in rationales; the path model trains on its own predicted paths for the same reason
- [[spreading-activation-retrieval]] — a multi-hop route that propagates over existing graph edges; a missing link cuts it, which is the failure generation avoids (my inference)

[^c1]: doi-10-48550-arxiv-2201-06206 — "the model fails to infer an evidential path"
[^c2]: doi-10-48550-arxiv-2201-06206 — "we use a Transformer encoder-decoder"
[^c3]: doi-10-48550-arxiv-2201-06206 — "each triple induces a supervised training sample"
[^c4]: doi-10-48550-arxiv-2201-06206 — "not explicitly rely on existing edges in the graph to"
[^c5]: doi-10-48550-arxiv-2201-06206 — "allowing the model to dynamically complete the graph while"
[^c6]: doi-10-48550-arxiv-2201-06206 — "to memorize the edge"
[^c7]: doi-10-48550-arxiv-2201-06206 — "is no such supervision on the target path"
[^c8]: doi-10-48550-arxiv-2201-06206 — "and reasonable rate are still low for practical concerns"
[^c9]: doi-10-48550-arxiv-2201-06206 — "for more than 70% of the triple queries in"
[^c10]: doi-10-48550-arxiv-2201-06206 — "link prediction over six benchmark KGs"
[^c11]: doi-10-48550-arxiv-2201-06206 — "with baselines that all set maximum path length to 3"
