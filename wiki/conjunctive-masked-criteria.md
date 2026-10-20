---
description: "A query of several vague criteria can pick out one page even when each criterion alone fits many, because the target is the only page where all of them hold together."
aliases: ["fuzzy exploratory query", "masked-criteria query", "multi-constraint webpage retrieval", "intersection-unique query", "fuzzy exploratory search"]
sources: ["arxiv-2512-16553", "arxiv-2511-22843"]
---
# Conjunctive masked criteria

A vague query can still have one target if it is a conjunction. The query lists several impressions of a page, each with its specific handle removed: a name is replaced by "someone", a place by "somewhere". Taken alone, each impression fits a large set of documents. The paper's claim is that the set satisfying all of them together is "typically extremely small—even unique".[^c1] The arithmetic under this is plain, though the paper's own measurement of it is the claim above: the intersection of candidate sets cannot be larger than any one of them, so each added criterion can only shrink the candidates. The paper names this "the intersection property of constraints", and says it is what lets people "to efficiently and reliably locate target content in open-web environments" without precise keywords.[^c2][^c3]

Each criterion is an impression with a masked centre. The paper says "a central part is masked using a generic expression", so the query does not name the entity it is about, and no single search term retrieves it directly.[^c4] The masking is generic replacement of "names, locations, species, etc." with placeholders.[^c5] The agent is then asked "to find a specific webpage whose content mentions all of the information" in the query, and is not asked to recover the masked elements.[^c6]

A second design choice fixes where the conjunction is taken. The answer must be one page that contains every criterion, not a page assembled from several. The reason given is that the pieces "are not necessarily talking about the same thing", and that a single page is "typically internally consistent and free of logical contradictions".[^c7][^c8] So the intersection is over one document. The uniqueness claim is about that document, and it is what makes a whole page, rather than a short fact, the right answer.

The mechanism bears on how difficulty behaves. If the target is fixed by the conjunction, then the hard part is not the number of criteria but how many documents each criterion admits and how much those sets overlap. That second half is my inference; the paper measures difficulty by the claims chosen, not by the overlap (see [[claim-centrality-difficulty]]). What the paper does show is that accuracy "consistently declines as query difficulty increases" for every agent it tested.[^c9]

The same mechanism sets a demand on the answerer. A reader who runs one search, takes the first hits for one criterion, and stops has not done the intersection. The paper reports that agents "frequently commit to fractured snippets returned by the search tool" without checking each candidate.[^c10] The conjunction only helps a reader who tests each candidate against every criterion.

The same device appears in a question generator that starts from one relation. A question built from a single relation can fit several answers; the RETINA paper names this case "where multiple entities could validly satisfy the question."[^c16] Its remedy adds a second related entity, a qualifier, so that "contextual cues to uniquely specify the answer entity among multiple possible candidates" remain.[^c17] The stated aim is "ensuring that most generated questions yield a single, well-defined answer."[^c18] Here the conjunction is taken over two related entities, not over masked impressions of one page. That the two are one mechanism is my inference; the RETINA paper does not cite this work.

## Limits

- Uniqueness is asserted by design, then reported: "Our query design effectively excluded the possibility of multiple valid answers."[^c11] The check was an LLM judge asking whether an article mentions each criterion. So "unique" means unique among pages a model judges to satisfy the criteria, not unique across the web. The paper also counts a page as correct when it meets every criterion without being the target: such answers are "considered correct, though only the former corresponds" to the expected page.[^c12]
- The corpus is fixed: "the benchmark relies on a fixed corpus of queries and webpages".[^c13] The web changes, so a conjunction that is unique now may not be later.
- The sections I read do not vary the number of criteria while holding the rest fixed. So the claim that conjunction is what makes the target findable, rather than the difficulty of the chosen claims, is not isolated.
- The sample is 663 queries from seven sites, with 30 to 35 articles each.[^c14] Coverage is narrow, and the paper says it is "a limited slice of the" real web.[^c15]
- Each criterion's match count is asserted to be large ("a vast set of potential documents"), with no per-criterion count reported in the slices read.
- The two-entity version is checked for uniqueness only on the RETINA test set. That set is curated "to ensure factual accuracy, linguistic fluency, and answer unambiguity";[^c19] the 120k training samples rest on the generator's rules alone, so "most" questions is the claim, not "all".

## Related

- [[referent-match-set-ambiguity]] — counts the match set to type ambiguity; the same counting, over objects in a scene rather than masked claims across web pages.
- [[reverse-constructed-indirect-question]] — the same removal of search handles, built from the source backward and checked for a unique answer.
- [[agentic-keyword-search-retrieval]] — the retrieval interface a vague query meets; a lexical search returns one criterion's matches at a time.
- [[ambiguity-taxonomy]] — the general catalogue of ambiguity; a vague criterion is one source among others.
- [[claim-centrality-difficulty]] — how the claims that make up a query are chosen, and how that sets its difficulty.

[^c1]: arxiv-2512-16553 — "the number of documents satisfying all implicit constraints simultaneously is typically extremely small—even unique"
[^c2]: arxiv-2512-16553 — "It is precisely this intersection property of"
[^c3]: arxiv-2512-16553 — "to efficiently and reliably locate target content in open-web environments"
[^c4]: arxiv-2512-16553 — "a central part is masked using a"
[^c5]: arxiv-2512-16553 — "which replaces entity-specific content (names, locations, species, etc.) with generic placeholders such as"
[^c6]: arxiv-2512-16553 — "and require the agent to find a specific webpage whose content mentions all of the information"
[^c7]: arxiv-2512-16553 — "Since these pages are not necessarily talking about the same thing"
[^c8]: arxiv-2512-16553 — "information within a single webpage is typically internally consistent and free of logical contradictions"
[^c9]: arxiv-2512-16553 — "Across all agents, accuracy consistently declines as"
[^c10]: arxiv-2512-16553 — "without carefully checking each candidate to identify"
[^c11]: arxiv-2512-16553 — "Our query design effectively excluded the possibility of multiple valid answers."
[^c12]: arxiv-2512-16553 — "considered correct, though only the former corresponds"
[^c13]: arxiv-2512-16553 — "the benchmark relies on a fixed corpus of queries and webpages"
[^c14]: arxiv-2512-16553 — "From each website, we randomly sampled 30 to 35 articles as the foundational corpus."
[^c15]: arxiv-2512-16553 — "it only represents a limited slice of the"
[^c16]: arxiv-2511-22843 — "where multiple entities could validly satisfy the question"
[^c17]: arxiv-2511-22843 — "contextual cues to uniquely specify the answer entity among multiple possible candidates"
[^c18]: arxiv-2511-22843 — "ensuring that most generated questions yield a single, well-defined answer"
[^c19]: arxiv-2511-22843 — "to ensure factual accuracy, linguistic fluency, and answer unambiguity"
