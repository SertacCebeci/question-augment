---
description: "Questions about how papers relate (novelty, citing stance, lineage) need the citation network, not topical similarity; retrievers often score under 20% on them (SciNet)."
aliases: ["relation-aware literature retrieval", "relational retrieval", "scientific network retrieval", "relation-aware scientific retrieval"]
sources: ["arxiv-2601-03260"]
---
# Relation-aware retrieval

A literature question can ask for a relation between papers instead of for papers that match its words. SciNet, built on a meta-database of 269 million papers, separates three levels of such relations: "We systematically define three levels of scientific relations: ego-centric, pair-wise, and path-wise, to characterize how scholarly papers relate to each other."[^c1] At the ego-centric level the question asks for a property of one paper within the citation structure, such as how novel it is: "Ego-centric: Retrieving papers based on intrinsic scientific properties, such as identifying the most novel".[^c2] The two measures used there are [[novelty-co-citation-score]] and [[disruption-index]]. At the pair-wise level it asks for the relation between two papers, such as whether one cites the other positively: "Pair-wise: Identifying the specific relational context".[^c3] At the path-wise level it asks for a chain of citations joining two papers: "Path-wise: Retrieving citation paths that reflect the".[^c4]

The mechanism the authors propose is that the answer to such a question is carried by the citation network and by the citing text, not by the topical neighbourhood of the query. Embedding retrievers "rely solely on static representations of the literature, limiting retrieval to shallow semantic" matching.[^c5] When the answer is a relation, the relevant paper may share few words with the query, so a retriever that ranks by similarity is aimed at the wrong quantity. That consequence is my inference from the design of the three levels; the paper does not state it in those words.

The measured result is low accuracy. Across eight methods in three categories (embedding, agentic, deep research), accuracy on relation-aware tasks "below 20%, highlighting a fundamental shortcoming of current retrieval paradigms."[^c6] Ego-centric recall is lowest: "disruption only 4.71%, indicating that over 95% of truly"[^c7] groundbreaking papers were missed by every system. Pair-wise recall is uneven: "CoMention-Acc can be as high as 76%."[^c8] yet the sentiment and paragraph-level tasks stay low: "Cite-Sentiment and CoMention-Paragraph continue to show"[^c9] low performance across all approaches. On the path-wise task, embedding models "essentially fail, achieving near-zero Consistency and Connectivity, alongside very low scores in both LLM-judged"[^c10] and human rationality ratings. The authors also run a downstream check: in a literature review application, agents given SciNet show "a 25.3% improvement in review quality".[^c11]

## Limits

The ground truth is built from the same citation data the tasks ask about. For the ego-centric tasks the labels are "papers based on their scientometric ranks, creating two distinct ground truth sets."[^c12] Recall against these labels measures agreement with a citation metric, not with what a scientist would call novel; the paper does not test the second.

Only eight systems are evaluated, on one OpenAlex release (RELEASE 2025-07-07).[^c13] The authors themselves say the failures call for "relation-aware retrieval models capable of understanding" the network;[^c14] no such model is built or tested here, so the work establishes that current retrievers fail on these tasks, not that a particular repair works.

The path-wise ground truth is chosen by a rule: "highest total citation count was selected as the candidate trajectory."[^c15] Summing citations along a path favours highly cited papers, so the path-wise benchmark may reward popularity as much as relation (my inference; not tested in the paper).

## Related

- [[novelty-co-citation-score]] — the ego-centric novelty measure: how atypical a paper's reference pairs are
- [[disruption-index]] — the ego-centric disruption measure: whether later work still needs the paper's references
- citation-context-relation — the pair-wise level: stance and co-mention read from the citing text
- [[semantic-proximity-bias]] — retrievers reward similarity to the query; relation questions are built where similarity is not enough
- [[situational-relevance]] — relevance beyond semantic closeness, the same gap seen from the user's side
- [[relation-driven-hop-count-selection]] — the knowledge-graph analogue, where the relations a traversal activates set the depth needed
- [[literal-match-dependence]] — evidence found by word overlap; relation questions are where overlap is least informative (my inference)
- [[citation-back-tracking]] — the reverse movement: inheriting the citations of earlier sentences to check a claim

[^c1]: arxiv-2601-03260 — "We systematically define three levels of scientific relations: ego-centric, pair-wise, and path-wise, to characterize how scholarly papers relate to each other."
[^c2]: arxiv-2601-03260 — "Ego-centric: Retrieving papers based on intrinsic scientific properties, such as identifying the most novel"
[^c3]: arxiv-2601-03260 — "Pair-wise: Identifying the specific relational context"
[^c4]: arxiv-2601-03260 — "Path-wise: Retrieving citation paths that reflect the"
[^c5]: arxiv-2601-03260 — "rely solely on static representations of the literature, limiting retrieval to shallow semantic"
[^c6]: arxiv-2601-03260 — "below 20%, highlighting a fundamental shortcoming of current retrieval paradigms."
[^c7]: arxiv-2601-03260 — "disruption only 4.71%, indicating that over 95% of truly"
[^c8]: arxiv-2601-03260 — "CoMention-Acc can be as high as 76%."
[^c9]: arxiv-2601-03260 — "Cite-Sentiment and CoMention-Paragraph continue to show"
[^c10]: arxiv-2601-03260 — "essentially fail, achieving near-zero Consistency and Connectivity, alongside very low scores in both LLM-judged"
[^c11]: arxiv-2601-03260 — "a 25.3% improvement in review quality"
[^c12]: arxiv-2601-03260 — "papers based on their scientometric ranks, creating two distinct ground truth sets."
[^c13]: arxiv-2601-03260 — "we first leverage OpenAlex (RELEASE 2025-07-07),"
[^c14]: arxiv-2601-03260 — "relation-aware retrieval models capable of understanding"
[^c15]: arxiv-2601-03260 — "highest total citation count was selected as the candidate trajectory."
