---
description: "A multi-hop question's difficulty is estimated before retrieval as the expected cost of reaching each supporting document along its retrieval path, from query-term specificity."
aliases: ["multHP", "retrieval path difficulty", "pre-retrieval difficulty for multi-hop questions", "multi-hop query performance prediction"]
sources: ["doi-10-48550-arxiv-2308-06431"]
---
# Multi-hop retrieval-path difficulty

A multi-hop question needs evidence from more than one document. The paper's starting point is that "one must collect evidence from two or" more relevant documents before the question can be answered.[^c1] Its claim is that such a question's difficulty can be estimated before any retrieval runs, by modelling the walk the retriever would have to make from the question to each supporting document. The difficulty is a cost: "the difficulty of the question can be measured by the cost" of retrieving its context documents along that path, and the cost "refers to the number of additional documents retrieved."[^c2]

This is a case of [[query-performance-prediction]] for a question type where the usual single-hop predictors have no grip. The paper says it was "in the absence of prior research on QPP in multi-hop QA settings" that it compared against standard pre-retrieval baselines.[^c3]

## The mechanism

A question is assigned one of three retrieval-path shapes. In a bridge path, "the second document cannot be easily retrieved without retrieving the first document," so the first hop must be reached before the second is even reachable.[^c4] In a comparison path, "both supporting documents can be retrieved with" the question, and the reasoning needs both.[^c5] When the question does not show which shape it has, the path is mixed: "This is called mixed retrieval path meaning that the retriever may consider it as bridge or comparison."[^c6]

Given a path, the probability of reaching all supporting documents is a product of hop probabilities. For a two-hop bridge path it is the probability of reaching the first document times the probability of reaching the second given the first. For a comparison path the two hops are independent and the probabilities multiply. For a mixed path the paper takes the best of the three orderings, because "the retriever will take the path with the highest probability."[^c7] The expected number of documents to be retrieved is the inverse of this probability.[^c8] A question that fits no path, with probability near zero, is counted as difficult.[^c9]

The probabilities have to be estimated without retrieving anything. "Under a pre-retrieval setting, our probabilities can be estimated" from the question and perhaps corpus statistics.[^c10] Each hop is scored by the document frequency of a query n-gram: P(c given n) is one over N(n), where N(n) "denotes the number of documents that" mention the n-gram.[^c11] Candidate n-grams come from named entities, as unigrams to trigrams, and from frozen phrases. The paper hypothesises that comparison questions mention two or more entities, each tied to one hop, so the two most specific n-grams stand for the two hops; that is a hypothesis it does not test directly. For a bridge question only the first hop is reachable from the question, and the paper scores it with an "optimistic estimation that assumes the most specific ngram" appears in the first supporting document.[^c12] The second-hop probability is then a constant, set by hand "to calibrate the score difference between bridge and comparison".[^c13]

Path type is not given in the data for every question, so a classifier is trained to detect it from the question: "a classifier may be trained to detect the retrieval path type of a question."[^c14] On the HotpotQA development set this detector reached "99.63%, 94.64%, and 97.07% in terms of precision, recall, and" F1.[^c15]

Across HotpotQA's training set, about 20% of questions show a bridge path and 63% a mixed one.[^c16] The authors add: "Clearly, these are some rough estimates," since the numbers depend on the overlap threshold.[^c17]

## What was measured

Difficulty was checked against the actual average precision of two retrievers on HotpotQA, a sparse one (GoldEn) and a dense one (MDR).[^c18] On pairwise accuracy, the predictor "outperforms all of the baselines with over" a 4.87% improvement on bridge questions.[^c19] On mixed questions it beat every baseline by 1.93% and 2.05% for the two retrievers.[^c20] On bridge questions the Pearson correlation with GoldEn's average precision is 0.2858 in the paper's table, against a best baseline that my reading of the table puts near 0.15.[^c21] The paper also reports that the difficulty classes built from this score show a drop in retriever performance from easy to extra-hard questions,[^c32] and that an adaptive retriever giving more documents to hard questions gets "a higher performance, in terms of F1-score" than a constant one at the same budget.[^c22]

For asking and answering, the transferable idea (my inference, not tested here) is that a question's difficulty can sit in its hop structure rather than in its wording. A question that names one entity and leaves the other to be reached through a document is harder in a measurable way, and the number of hops is where the cost comes from.

## Limits

- Comparison questions do not come out well. For MDR the Pearson correlation on comparison questions was lower, because "MDR performs quite well in comparison questions."[^c23] Even for the proposed model, "for comparison questions, our approach did" not beat the baselines on the sparse retriever either.[^c24]
- Error cases exist in both directions. "the GoldEn retriever could not find the supporting documents" for some questions the model rated easy, and it found documents for some it rated difficult.[^c25]
- The estimate sees only syntax and document frequency: "the relatedness is defined syntactically."[^c26]
- The paper's own single evaluation dataset is HotpotQA: "the largest multi-hop QA dataset using several modern QA systems."[^c27] The thresholds and the constant second-hop probability were set on it.
- Difficulty is defined by retriever performance, not by answer quality: "query difficulty may be quantified in terms of the performance of the retrievers."[^c28] The authors caution that their score "is merely based on the retrieval paths, and some questions that" look hard may not be hard for the QA system.[^c29]
- The paths are defined for two hops. Generalising to n hops "may be generalized to" n-hop questions, and the paper does not test it.[^c30]
- The single-hop test on WikiQA and WikiPassageQA gave correlations that the paper itself calls "not very strong."[^c31]
- The 0.125 second-hop constant is a calibration choice; the paper does not show the result is stable across settings.

## Related

- [[query-performance-prediction]] — the wider family; this note is a pre-retrieval predictor scored against retriever average precision, not against human relevance judgements.
- [[syntactic-complexity-routing-between-retrieval-paths]] — also reads question structure before retrieval; there the output is a routing label, here a cost estimate and a path type.
- [[hop-depth-difficulty-with-entropy-check]] — difficulty by hop depth on knowledge graphs, a different readout of multi-hop difficulty.
- [[generation-retrieval-difficulty-divergence]] — difficulty depends on which task it is measured for; this note is about retrieval difficulty only.

[^c1]: doi-10-48550-arxiv-2308-06431 — "one must collect evidence from two or"
[^c2]: doi-10-48550-arxiv-2308-06431 — "the difficulty of the question can be measured by the cost"
[^c3]: doi-10-48550-arxiv-2308-06431 — "In the absence of prior research on QPP in multi-hop QA settings"
[^c4]: doi-10-48550-arxiv-2308-06431 — "easily retrieved without retrieving the first document"
[^c5]: doi-10-48550-arxiv-2308-06431 — "a scenario where both supporting documents can be retrieved with"
[^c6]: doi-10-48550-arxiv-2308-06431 — "This is called mixed retrieval path meaning that the"
[^c7]: doi-10-48550-arxiv-2308-06431 — "that the retriever will take the path with the highest probability"
[^c8]: doi-10-48550-arxiv-2308-06431 — "or the cost, may be denoted by"
[^c9]: doi-10-48550-arxiv-2308-06431 — "We consider these questions difficult"
[^c10]: doi-10-48550-arxiv-2308-06431 — "Under a pre-retrieval setting, our probabilities can be estimated"
[^c11]: doi-10-48550-arxiv-2308-06431 — "denotes the number of documents that"
[^c12]: doi-10-48550-arxiv-2308-06431 — "This is an optimistic estimation that assumes the most specific ngram"
[^c13]: doi-10-48550-arxiv-2308-06431 — "to calibrate the score difference between bridge and comparison"
[^c14]: doi-10-48550-arxiv-2308-06431 — "a classifier may be trained to detect the retrieval path type of a"
[^c15]: doi-10-48550-arxiv-2308-06431 — "99.63%, 94.64%, and 97.07% in terms of precision, recall, and"
[^c16]: doi-10-48550-arxiv-2308-06431 — "about 20% of the questions demonstrate a bridge retrieval path"
[^c17]: doi-10-48550-arxiv-2308-06431 — "Clearly, these are some rough estimates,"
[^c18]: doi-10-48550-arxiv-2308-06431 — "is evaluated in the context of both sparse and dense retrievers."
[^c19]: doi-10-48550-arxiv-2308-06431 — "our metric outperforms all of the baselines with over"
[^c20]: doi-10-48550-arxiv-2308-06431 — "In the Mixed type, our multHP outperformed all"
[^c21]: doi-10-48550-arxiv-2308-06431 — "multHP (ours) 0.2342 0.2480 0.1849 0.2858 0.3088 0.2369"
[^c22]: doi-10-48550-arxiv-2308-06431 — "a higher performance, in terms of F1-score, is achieved using the"
[^c23]: doi-10-48550-arxiv-2308-06431 — "MDR performs quite well in comparison questions"
[^c24]: doi-10-48550-arxiv-2308-06431 — "for comparison questions, our approach did"
[^c25]: doi-10-48550-arxiv-2308-06431 — "the GoldEn retriever could not find the supporting documents"
[^c26]: doi-10-48550-arxiv-2308-06431 — "the relatedness is defined syntactically."
[^c27]: doi-10-48550-arxiv-2308-06431 — "the largest multi-hop QA dataset using several modern QA systems"
[^c28]: doi-10-48550-arxiv-2308-06431 — "query difficulty may be quantified in terms of the performance of the retrievers"
[^c29]: doi-10-48550-arxiv-2308-06431 — "is merely based on the retrieval paths, and some questions that"
[^c30]: doi-10-48550-arxiv-2308-06431 — "may be generalized to"
[^c31]: doi-10-48550-arxiv-2308-06431 — "while the correlations are not very strong"
[^c32]: doi-10-48550-arxiv-2308-06431 — "performance drop between easy and extra hard classes of DrQA,"
