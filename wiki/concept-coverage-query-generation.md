---
description: "Synthetic training queries are generated one at a time, each conditioned on the document's concepts that earlier queries left under-covered, so the set complements rather than repeats."
aliases: ["CCQGen", "concept coverage-based query set generation", "coverage-conditioned synthetic query generation"]
sources: ["arxiv-2601-00567"]
---
# Concept-coverage query generation

Synthetic query generation builds training data for a retriever by prompting an LLM to write queries for each document. Its known weakness is redundancy. The authors put the mechanism this way: "LLMs often focus on only a narrow subset" of a document's concepts, so the queries repeat a few ideas and leave the rest of the paper without a training signal.[^c1]

Concept-coverage query-set generation (CCQGen) makes the generator aware of what the set has already covered, using the document's concept index. The procedure runs per document. The first query has no conditions, "For the first query of each document, we impose no conditions,", so it is the same as in the baseline.[^c4] Before each further query, the concept extractor is applied to the text of the queries so far, "we apply the concept extractor to the concatenated text", which gives a coverage weight to every topic and phrase in the index.[^c2] A concept is under-covered when its importance in the index is high and its coverage by the queries is low. The paper's Eq. 1 turns the difference into a distribution: the positive part of the gap, floored at a small constant and normalised. The under-covered concepts are then written into the prompt as conditions, so the next query has to articulate concepts the set has not yet reached.[^c3] A final filter checks quality and conceptual correctness before a query is kept.[^c5] The loop "is repeated until a predefined number" of queries exists; the experiments use five per document.[^c6][^c12]

The effect is measured by fine-tuning. Queries from each generator are used to train the retriever, and CCQGen is added to three LLM-based generators: Promptgator, pair-wise generation, and a Promptgator variant told to reduce redundancy. Specialised T5 generation (GenQ) is the other baseline. The paper reports that "CCQGen consistently outperforms all baselines" with both backbones, Contriever-MS and SPECTER-v2.[^c7] Two results carry the mechanism. The first is that the baselines "often fail to improve the backbone model", while CCQGen does.[^c8] The second is data scaling. Pair-wise generation "shows limited performance under restricted data conditions", whereas CCQGen "delivers relatively consistent and considerable improvements, even" when only a few queries are available.[^c9][^c11]

The redundancy control is the informative part. The Promptgator variant, with an explicit instruction to reduce redundancy and use varied terms, "often generates redundant queries covering similar aspects, despite increased" diversity of wording.[^c10] My reading, not the paper's wording: what the set lacks is coverage of concepts, and an instruction to vary phrasing does not supply the missing concepts. Conditioning on uncovered concepts does.

## Limits

- The gains are reported for fine-tuned retrievers. CCQGen is a data-side method; a training-free setting is handled by a different component of the same paper, not by this procedure.
- The test sets are small or partly synthetic. CSFCube has 50 test queries, and DORIS-MAE's queries are "annotated by human experts and LLMs, respectively", so one benchmark's relevance labels come from an LLM.[^c13]
- The main results use one generator, gpt-3.5-turbo-0125, which the paper itself describes as a legacy model. The paper also runs a smaller model in a separate table, which I did not read. Transfer to other LLMs is not shown in what I read.
- Coverage is estimated by the same concept extractor that built the index (my inference from the procedure). An extractor error shifts both the target distribution and the coverage estimate; I did not find a test of how such errors propagate.
- The procedure is sequential within a document, since each query waits for the coverage of the queries before it. The cost is one extractor pass per query (my inference).
- In domains where the taxonomy is sparse, the under-coverage signal can point at generic words. The authors' example is a game-theory paper, where the generated queries drift toward general aspects of the document.[^c14]

## Related

- [[academic-concept-index]] — supplies the concepts and importance weights that the coverage check reads
- [[question-generation-as-policy]] — the same redundancy in self-study QA: the generator revisits already covered evidence, and varied prompt seeds do not fix it

[^c1]: arxiv-2601-00567 — "LLMs often focus on only a narrow subset"
[^c2]: arxiv-2601-00567 — "we apply the concept extractor to the concatenated text"
[^c3]: arxiv-2601-00567 — "identify concepts that remain insufficiently covered"
[^c4]: arxiv-2601-00567 — "For the first query of each document, we impose no conditions,"
[^c5]: arxiv-2601-00567 — "A final filtering stage ensures the quality and conceptual correctness"
[^c6]: arxiv-2601-00567 — "This process is repeated until a predefined number"
[^c7]: arxiv-2601-00567 — "CCQGen consistently outperforms all baselines"
[^c8]: arxiv-2601-00567 — "existing methods often fail to improve the backbone model"
[^c9]: arxiv-2601-00567 — "shows limited performance under restricted data"
[^c10]: arxiv-2601-00567 — "It often generates redundant queries covering similar aspects, despite increased"
[^c11]: arxiv-2601-00567 — "CCQGen delivers relatively consistent and considerable improvements, even"
[^c12]: arxiv-2601-00567 — "we generate five queries for each document"
[^c13]: arxiv-2601-00567 — "annotated by human experts and LLMs, respectively"
[^c14]: arxiv-2601-00567 — "When the academic taxonomy provides limited coverage for certain domains (e.g., game theory,"
