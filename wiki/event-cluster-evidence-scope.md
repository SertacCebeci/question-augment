---
description: "Grouping posts and trusted articles into events first, then checking each claim only against its event cluster, beat a fixed top-N search on one Vietnamese news set."
aliases: ["event-level evidence clustering", "cluster-scoped evidence retrieval", "clustering before retrieval", "event clustering for fact-checking"]
sources: ["doi-10-11591-ijai-v15-i4-pp3144-3153"]
---
# Event-cluster evidence scope

Before any claim is checked, the pipeline sorts its articles into events. Social posts and mainstream reports are clustered by DBSCAN over PhoBERT document embeddings, and publication date is added so that similar stories on different days are not merged: "Temporal metadata (publication date) is also incorporated to prevent unrelated stories with similar content from being conflated."[^e1] Each cluster then holds the social and mainstream articles about one event. At verification time a claim sees only the trusted articles of its own cluster: "By clustering first, evidence retrieval is restricted to the cluster of interest."[^e2]

The scope is set by the event, not by a count. The authors contrast this with a fixed top-N search, where N is chosen in advance and may drop context: "clustering adaptively collects all pertinent references."[^e3] The same restriction is meant to keep sources on-topic and of known credibility, which "mitigates the issue of conflicting or spurious retrieval results."[^e4] The mechanism is a pre-filter on the evidence set, so the verifier never sees articles from outside the event, however relevant they might look to a search engine.

The measured effect is an ablation on one dataset. With the same GPT-4 claim verifier, the top-N variant reached 86.7% F1 on claims and 89.6% on news labels, and the cluster variant "achieved ~88.9%" on claims and 92.1% on news.[^e5] The paper also reports that clustering "improved precision by several points over top-N retrieval for the same number of sources."[^e6] Cluster quality was checked separately on 300 manually labelled articles, with purity 91.4% and NMI 86.7%, and the authors read the purity as a sign that "evidence clusters are semantically coherent".[^e7]

What transfers is the design choice: the evidence unit is a group defined by the event, and the group, not the retriever's rank, decides what the verifier may use. The shape of the gain does not transfer by itself. The paper compares sets of different construction, and the gain is a few points.

## Limits

- One dataset, built by the authors. "A custom dataset is constructed for evaluation." It has 723 social-media items and 1,042 trusted articles, all Vietnamese, from November and December 2024.[^e8] The Table 4 ablation is reported as single scores. The confidence intervals the paper gives are for the Table 5 benchmarks, not for the cluster comparison (my reading).
- The top-N baseline is described two ways. In the setup it is "an online search application programming interface (API)" that returns "the top-3" news.[^e9] In the results the top-N row uses "the top 3 relevant cluster" articles.[^e10] If the second is right, the comparison isolates ranking within a cluster, not cluster scope against search. The paper does not say which was run.
- Cluster errors are not traced to verdicts. Purity and NMI describe the clusters; how merged or split events change a verdict is not reported. The DBSCAN parameters were "tuned" but the values are not given in the text read.
- Scope size has a cost the paper does not separate. Verifying full articles against all cluster text gave 69.8% news F1, and the authors suspect "verbosity and confusion in long inputs."[^e11] Whether a wider cluster helps or hurts is therefore not isolated here.
- The "suspicious" label, given only "if there is conflicting evidence between the post and its cluster,"[^e12] is described but no result for it is reported.
- My inference, not the paper's: a claim whose event has no trusted article in the corpus gets no evidence at all under this scope, and the paper does not test that case. The reported dataset was built so that each claim had about three supporting articles, which avoids it by construction.

## Related

- [[claim-decomposed-retrieval-check]] — the open alternative: each claim is turned into a web query, so the evidence scope is the search result rather than a prior event grouping.
- [[set-level-selection-over-relevance]] — choosing evidence as a set can score coverage and consistency, which per-item ranking misses; an event cluster is one such set-level rule.
- [[demonstration-label-consistency]] — top-K similarity retrieval does not guarantee a property of the chosen set; the same complaint is made of top-N evidence here.
- [[query-adaptive-evidence-granularity]] — the grain of evidence set per query rather than a fixed size, a related argument against fixed-size retrieval.
- atomic-claim-extraction — the claim side of the same pipeline, which produces the units checked against each cluster.

[^e1]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "Temporal metadata (publication date) is also incorporated to prevent unrelated stories with similar content from being conflated"
[^e2]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "By clustering first, evidence retrieval is restricted to the cluster of interest."
[^e3]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "clustering adaptively collects all pertinent references"
[^e4]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "which also mitigates the issue of conflicting or spurious retrieval results"
[^e5]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "the full pipeline (claims + LLM + cluster evidence) achieved ~88.9%"
[^e6]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "improved precision by several points over top-N retrieval for the same number of sources"
[^e7]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "High purity confirms that evidence clusters are semantically"
[^e8]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "A custom dataset is constructed for evaluation."
[^e9]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "use an online search application programming interface (API) to retrieve the top-3"
[^e10]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "the top 3 relevant cluster"
[^e11]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "may be suffered from verbosity and confusion in long inputs"
[^e12]: doi-10-11591-ijai-v15-i4-pp3144-3153 — "only if there is conflicting evidence between the post and its cluster"
