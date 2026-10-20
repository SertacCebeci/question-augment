---
description: "A concept's information is its parser's per-token uncertainty, kept when a one-sample t-test against the other concepts of its own document is significant at a loose α = 0.3."
aliases: ["conceptual entropy", "AMR node entropy", "node-level entropy screening", "concept-level entropy"]
sources: ["arxiv-2511-18832"]
---
# Conceptual entropy screen

A concept is scored by how uncertain a generative model is about it, and it is kept only if its score stands out from the other concepts of the same document. The mechanism has three steps. First, each document is parsed into a sentence-level Abstract Meaning Representation graph, one node per concept; a node "corresponds to a semantic concept (e.g., entities, predicates, or modifiers)" and keeps its textual realization in the source.[^c1] Second, each node is scored with the parser's own generative model: "we calculate its information entropy by leveraging the AMR generation model" on the tokens that spell the concept. A concept can span several subword tokens, so the per-token terms are combined into one number, "accumulate entropy scores for all" the pieces that belong to the same concept. The stated purpose is that a multi-token concept is not penalised against a single-token one.[^c2]

Third, the scores are screened inside each document. The concept scores of a document form one sample; each concept gets a one-sample t-statistic against that sample's mean and standard deviation, a p-value is read from the t-distribution with n−1 degrees of freedom (n the number of concepts), and "We then screen out concepts whose p-values satisfy" the threshold α.[^c3] The threshold is deliberately loose: "we adopt a relaxed threshold" of α = 0.3. The ablation reports that low α values "overly restrict the retained information, pruning out useful concepts".[^c4]

The rationale offered is that a node-level score is sharper than a token-level one: "computing entropy over AMR concept nodes leverages semantic structure to more precisely estimate informational content".[^c5] The surviving concepts are then mapped back to their source wording, and the edges between them are dropped: "we keep the concept nodes Vi and discard the explicit Ei in each Gi".[^c6] The output is a bag of surface spans rather than a graph. The justification for dropping relations is a cognitive hypothesis that readers rebuild scenes from concepts alone; the paper cites that hypothesis and does not test it in this work.

What was measured: on PopQA and EntityQuestions, using only documents that contain the answer, the method "reduces the length to about 50% of the vanilla on average, while keeping the Acc stable in both datasets".[^c7] Keyword and summary baselines reach lower token counts, "but they often remove meaningful factual cues".[^c8] The abstract's headline is "achieving higher accuracy while substantially reducing context length".[^c9]

What survives the move out of AMR: the operation of scoring each unit by the generator's uncertainty about it, then judging the unit against its own document's distribution instead of against a cut fixed in advance. The relative test does not require graphs. What does not survive is the parser-based score, which is the specific contribution here.

## Limits

- **Query-free as I read it.** The task is stated with a query ("Given a query Q and a set of retrieved documents"),[^c10] but the entropy and the test in the equations use only the graph and the document's own concepts. My reading is that the same concepts survive whatever is asked. That differs from [[structure-then-select-compression]], which selects against the question. The experiments test the screen only in "a controlled testing environment" where every document carries an answer,[^c11] so handling of irrelevant documents is untested.
- **Parser-bound.** The authors say the approach "relies on the stability of AMR parsers",[^c12] and sentence-level graphs mean that "complex document-level structures are easily ignored".[^c13]
- **The printed per-token term is ambiguous.** It appears as exp(−log P), which equals P itself, not the −log P that "entropy" usually denotes. The text extraction may have garbled the formula, and I did not check the typeset page, so I cannot say which quantity was computed.
- **Two-sided test, my reading.** The printed p-value uses the absolute t-statistic, so a concept whose uncertainty is significantly low relative to its document would pass the same screen. The paper says the aim is concepts with higher entropy,[^c14] and does not discuss the low tail.
- **The threshold is weak evidence.** At α = 0.3, a document whose scores carry no signal would still pass about a third of its concepts by chance. That is my inference from the threshold, not a claim of the paper. The screen selects what is unusual within a document, not what is informative about the question.
- **Preprocessing cost.** "computing AMR graphs and entropy scores introduces extra cost during preprocessing".[^c15]
- **Accuracy wording.** The abstract says "higher accuracy"; the compression section describes accuracy as held "stable". I read the second as the narrower claim.

## Related

- [[structure-then-select-compression]] — both keep units that point back into the source; there selection is query-relative under a token budget, here it is a document-level significance test with no budget.
- [[information-bottleneck]] — the general frame of compression as keeping what bears on a target; this screen has no target, only the document's own distribution, so it is a weaker form of that frame.
- [[entropy]] — the score borrows the word. It is a per-token uncertainty of a parser over the spelling of one concept, not an entropy over a defined outcome set.
- [[calibrated-surprisal]] — that note removes a word-frequency prior from an answer's surprisal; the conceptual score is raw per-token uncertainty and keeps whatever frequency prior the parser has, which the paper does not correct.

[^c1]: arxiv-2511-18832 — "corresponds to a semantic concept (e.g., entities, predicates, or modifiers)"
[^c2]: arxiv-2511-18832 — "we calculate its information entropy by leveraging the AMR generation model"
[^c3]: arxiv-2511-18832 — "We then screen out concepts whose p-values satisfy"
[^c4]: arxiv-2511-18832 — "pruning out useful concepts"
[^c5]: arxiv-2511-18832 — "computing entropy over AMR concept nodes leverages semantic structure to more precisely estimate informational content"
[^c6]: arxiv-2511-18832 — "we keep the concept nodes Vi and discard the explicit Ei in each Gi"
[^c7]: arxiv-2511-18832 — "reduces the length to about 50% of the vanilla on average, while keeping the Acc stable in both datasets"
[^c8]: arxiv-2511-18832 — "but they often remove meaningful factual cues"
[^c9]: arxiv-2511-18832 — "achieving higher accuracy while substantially reducing context length"
[^c10]: arxiv-2511-18832 — "Given a query Q and a set of retrieved documents"
[^c11]: arxiv-2511-18832 — "evaluates compression under a controlled testing environment"
[^c12]: arxiv-2511-18832 — "relies on the stability of AMR parsers"
[^c13]: arxiv-2511-18832 — "so complex document-level structures are easily ignored"
[^c14]: arxiv-2511-18832 — "Concepts exhibiting higher entropy relative to the general nodes carry more discriminative information"
[^c15]: arxiv-2511-18832 — "computing AMR graphs and entropy scores introduces extra cost during preprocessing"
