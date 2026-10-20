---
description: "The disruption index scores a paper by whether later work cites only it or also its references, (Ni-Nj)/(Ni+Nj) from -1 consolidating to +1 disruptive; SciNet uses it as a retrieval target."
aliases: ["disruption index", "Funk-Owen-Smith disruption", "CD index", "disruptiveness index"]
sources: ["arxiv-2601-03260"]
---
# Disruption index

The disruption index is a citation-structure measure of whether a paper extends the work it builds on or replaces it. It looks at the papers that cite the focal paper. Some of them cite only the focal paper; others cite the focal paper together with its references. The index compares the two counts. The work's own formulation: "This metric evaluates whether subsequent publications continue"[^c1] "to cite both the focal paper and its predecessors, or instead"[^c2] "shift to citing only the focal paper. The index is calculated as"[^c3] (Ni − Nj)/(Ni + Nj), where Ni counts papers citing only the focal work and Nj counts papers citing both the focal work and its references.

The mechanism is simple once the two counts are in view. If later papers keep citing the older literature alongside the focal paper, the focal paper sits inside an existing trajectory and the index is low. If later papers cite the focal paper alone, the older literature is no longer needed to read the later work, and the index is high. The paper glosses this as "the work extends existing trajectories or fundamentally disrupts prior research."[^c4] The range is fixed: "the disruption index ranges from -1 (consolidating) to +1 (disruptive)."[^c5]

Within SciNet the index is a retrieval target. The authors justify it by the claim that "citation patterns, how it is cited by later work, can serve as a reliable indicator of its novelty, and disruptiveness."[^c6] Because raw values are hard to read, each score is converted "into a percentile rank against a global reference corpus of millions of papers."[^c7] For each subfield the top 50 papers by disruption form a ground-truth set, and retrieval is scored by Disruption-Recall@50. The best system reached 4.71%.[^c8]

The index is one of the two measures that make a question such as "most disruptive paper in [topic]" answerable only through citations. A content-based retriever has no direct access to it (my inference). For the broader category, see [[relation-aware-retrieval]]. The novelty counterpart, which works from co-citation pairs in a paper's references, is described in [[novelty-co-citation-score]].

## Limits

The index is computed from later citations, so it depends on the citing population and the time elapsed since publication. Neither dependence is tested in the work I read; both are my inference from the definition.

The SciNet ground truth is the top 50 papers ranked by the same metric the system is scored against: "papers based on their scientometric ranks, creating two distinct ground truth sets."[^c9] Recall@50 therefore measures agreement with the citation metric itself. Whether top-ranked disruption corresponds to what a scientist calls disruptive is not checked. In the sections I read, the disruption labels are not checked against the LLM-based novelty judgment (my reading).

The percentile conversion makes scores relative to a reference corpus. A paper's rank depends on what is in that corpus, and the work does not show how sensitive the ranks are to the choice of corpus.

The index measures structure, not value (my reading of the definition). A high score says that later work stopped needing the paper's references; it does not say the paper is correct or important. Predictive validity against impact is not established by the text I read.

## Related

- [[relation-aware-retrieval]] — the category of questions this measure is one example of
- [[novelty-co-citation-score]] — the other scientometric ego-centric measure used alongside it
- [[retrieval-dissimilarity-novelty-reward]] — novelty as embedding distance from retrieved papers, a content-based alternative that uses no citation structure

[^c1]: arxiv-2601-03260 — "This metric evaluates whether subsequent publications continue"
[^c2]: arxiv-2601-03260 — "to cite both the focal paper and its predecessors, or instead"
[^c3]: arxiv-2601-03260 — "shift to citing only the focal paper. The index is calculated as"
[^c4]: arxiv-2601-03260 — "the work extends existing trajectories or fundamentally disrupts prior research."
[^c5]: arxiv-2601-03260 — "the disruption index ranges from -1 (consolidating) to +1 (disruptive)."
[^c6]: arxiv-2601-03260 — "reliable indicator of its novelty, and disruptiveness."
[^c7]: arxiv-2601-03260 — "rank against a global reference corpus of millions of papers."
[^c8]: arxiv-2601-03260 — "disruption only 4.71%, indicating that over 95% of truly"
[^c9]: arxiv-2601-03260 — "papers based on their scientometric ranks, creating two distinct ground truth sets."
