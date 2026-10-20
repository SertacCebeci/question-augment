---
description: "Uzzi-style novelty scores a paper by how atypical the co-citation pairs among its references are, as a z-score against the field norm, read at the 10th percentile; lower means more novel."
aliases: ["Uzzi novelty score", "co-citation novelty", "atypical combination novelty", "novelty-SoS"]
sources: ["arxiv-2601-03260"]
---
# Co-citation novelty score

A paper can be called novel when it puts together references that the field seldom puts together. The co-citation novelty score makes that precise without reading the paper's content. It takes the pairs of references a paper cites and asks how often each pair has been co-cited elsewhere. The work states the source: the score follows Uzzi et al., "al. (Uzzi et al., 2013) for measuring novelty: by analyzing"[^c1] pairs of co-cited references, which "quantify the extent to which the work combines rare or atypical knowledge components."[^c2] Each pair's frequency is turned into a z-score against the disciplinary norm, and the paper's score is the 10th percentile of those z-scores: "being the 10th percentile (p10,z ) of these scores. A lower"[^c3]

The direction is fixed by the construction. Because the statistic is taken from the low tail, a paper whose references include a few very unusual pairs gets a strongly negative value. In the authors' words, "score thus signifies a more novel combination of knowledge."[^c4] A low score is therefore a high novelty, and the reading inverts a naive expectation.

In SciNet the score is one of two novelty signals. It is converted to a percentile rank like the disruption index, and averaged across candidates to give Novelty-SoS.[^c7] A second signal is produced by a language model: "Second, we incorporate LLMs (GPT-5) to provide complementary semantic judgments, yielding the Novelty-LLM"[^c5] metric, which scores each concept from the title and abstract. Recall at 50 against the top-50 most novel papers was low for every system, with the best at 1.47%.[^c6]

The measure is about recombination, not about content. A question such as "the most novel paper in [topic]" that is answered by this score is answered by the citation structure, not by what the paper says. The complementary structural measure is [[disruption-index]]. The category of such questions is [[relation-aware-retrieval]].

## Limits

The score depends on a "disciplinary norm" for co-citation frequency. Where that norm is estimated from a small or uneven field, the z-scores move. The work does not report how the norm was estimated for each subfield; I did not find that detail in the sections read (my inference that this matters).

Taking the 10th percentile is a convention. The text does not show that the 10th percentile tracks novelty better than other tail cut-offs, and it was not varied here.

The score rewards unusual combinations of references. An unusual combination can also be an error, a weak citation, or a field-boundary artefact. The work does not check which of these the score is picking up (my inference from the definition).

In the sections I read, the score is checked only through the retrieval benchmark, whose ground truth is the same ranking (my reading). The LLM-based Novelty-LLM is a separate judgment, and the two are not shown to agree in the text I read.

## Related

- [[disruption-index]] — the companion citation-structure measure, which looks at what later papers cite
- [[relation-aware-retrieval]] — the category of questions these measures answer
- [[novelty-feasibility-decoupling]] — expert ratings of novelty in research plans, a different sense of novelty that is not citation-based

[^c1]: arxiv-2601-03260 — "al. (Uzzi et al., 2013) for measuring novelty: by analyzing"
[^c2]: arxiv-2601-03260 — "the extent to which the work combines rare or"
[^c3]: arxiv-2601-03260 — "being the 10th percentile (p10,z ) of these scores. A lower"
[^c4]: arxiv-2601-03260 — "score thus signifies a more novel combination of knowledge."
[^c5]: arxiv-2601-03260 — "Second, we incorporate LLMs (GPT-5) to provide complementary semantic judgments, yielding the Novelty-LLM"
[^c6]: arxiv-2601-03260 — "the best recall@50 for novelty was only 1.47%, and for"
[^c7]: arxiv-2601-03260 — "The average of these percentile ranks for the candidates constitutes our final Novelty-SoS and Disruption-SoS metrics."
