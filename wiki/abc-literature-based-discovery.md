---
description: "Literature-based discovery infers a hidden A–C link from A–B and B–C links in disjoint literatures; open discovery starts from one concept, closed discovery tests a given pair."
aliases: ["ABC principle", "Swanson linking", "literature-based discovery", "LBD", "open and closed discovery"]
sources: ["doi-10-47852-bonviewmedin52025348"]
---
# ABC literature-based discovery

Literature-based discovery (LBD) generates hypotheses by joining facts that no single paper states together. The ABC principle: if concept A and concept B are directly associated in one body of literature, while B and C are linked in a separate, disjoint body, then merging the two sets allows a new possible inference of a connection between A and C via B.[^c1] The concepts can be any entity: gene, protein, drug, disease, miRNA, or a MeSH term.[^c2]

## Two ways to pose the question

The approaches differ in how much of the question is fixed in advance.

**Open discovery** starts from one concept only. The start can be a scientific problem or research question, and the end of the discovery is not defined.[^c3] Swanson's initial study took Raynaud's disease as C, looked for clues B (drugs, pathways, physiological processes), then for A-terms acting on those Bs, and ended with a hypothesis such as "substance A can be used for the treatment of disease C".[^c4] Its main difficulty is containing the vast number of possibilities found in the first search; knowledge of the domain is needed because the search space grows at each level.[^c5]

**Closed discovery** starts with both A and C known and looks for B terms that support the claim that the A–C association is relevant. The more pathways or processes lie between A and C, the more likely the hypothesis is valid.[^c6] Because both ends are known, it is simpler, and most LBD work focuses on it.[^c7]

In my reading, the split is a split in how well-specified the question is: open discovery asks "what might relate to C?", closed discovery asks "is A related to C, and why?" The second is a verification question and the first a generation question. This is my inference, not the paper's claim.

## Concept profiles

A concept's profile is the set of terms related to it by curated association or by co-occurrence in a biologically relevant context; it is written as weighted MeSH terms, with a weight for each term's association to the concept.[^c8] LBD then links concepts whose profiles overlap.

## What it produced

Swanson's disjoint-literature approach proposed magnesium and migraine, fish oil and Raynaud's syndrome, and somatomedin C and arginine; none had been predicted or reported before, and they were later confirmed.[^c9] Later systems (Arrowsmith, BITOLA, FACTA+, CoPub) apply the ABC principle with co-occurrence at the title, MeSH or abstract level.[^c10]

## Limits

- This is a review; it reports no benchmark that compares open with closed discovery, or co-occurrence with context-based variants, on hit rate.
- The figure legend itself says that many B-paths found are "spurious" or not relevant; precision of the linking step is not quantified here.
- Co-occurrence is treated as implying semantic association "in the majority of the cases", which is asserted, not measured here.[^c11]
- The setting is biomedical; whether disjoint-literature bridging helps in asking questions elsewhere is untested.

## Related

None of the existing notes covers this idea closely; the nearest are about hypotheses and their use in retrieval.

- [[llm-hypothesis-proposer]] — a language model proposes hypotheses; LBD does so by bridging literatures
- [[hypothesis-testing]] — closed discovery is a check of a stated A–C hypothesis
- [[contrastive-hypothesis-retrieval]] — retrieval organised around hypotheses

[^c1]: doi-10-47852-bonviewmedin52025348 — "then merging these two sets enables a new possible inference of a connection between concepts A and C"
[^c2]: doi-10-47852-bonviewmedin52025348 — "The concepts can be any relevant biological entity such as gene,"
[^c3]: doi-10-47852-bonviewmedin52025348 — "the end of the discovery is not defined"
[^c4]: doi-10-47852-bonviewmedin52025348 — "Swanson’s [48, 49] initial study was to find"
[^c5]: doi-10-47852-bonviewmedin52025348 — "The major challenge of open discovery"
[^c6]: doi-10-47852-bonviewmedin52025348 — "The more pathways or physiological"
[^c7]: doi-10-47852-bonviewmedin52025348 — "most of the LBD approaches are focused"
[^c8]: doi-10-47852-bonviewmedin52025348 — "The concept profile of a biological entity represents a set of terms"
[^c9]: doi-10-47852-bonviewmedin52025348 — "None of these"
[^c10]: doi-10-47852-bonviewmedin52025348 — "Hristovski et al. [64] released BITOLA"
[^c11]: doi-10-47852-bonviewmedin52025348 — "In the majority of the cases biologically"
