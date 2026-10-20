---
description: "Ask next about the unspecified attribute whose values are most evenly spread over the still-feasible candidates, stop below an entropy threshold, and reuse the same entropy to diversify results."
aliases: ["entropy-guided question selection", "data-grounded elicitation", "entropy-based grid diversification"]
sources: ["arxiv-2603-11399"]
---
# Candidate-set entropy question selection

A recommender that faces an ambiguous query keeps a filtered candidate set C. For every attribute dimension not yet fixed by a filter and not yet asked about, it computes the Shannon [[entropy]] of the attribute's value distribution over C and asks about the dimension with the highest value. High entropy means the candidates are spread across many values, so an answer would partition the set well; low entropy (for example 95% of candidates share one transmission type) means the question discriminates little.[^c1] Continuous attributes are first cut into three equal-frequency bins, and entropy is normalised by log2 of the number of values so dimensions of different cardinality are comparable.[^c2]

The selection is data-grounded rather than scripted: the filtered database, not a fixed questionnaire, decides what to ask. The language model only phrases the question, given the chosen dimension and its distribution statistics (such as "40% gasoline, 35% hybrid, 25% electric"). Choosing the dimension and wording the question are separate steps.[^c3]

## Stopping

A minimum entropy threshold of 0.3 ends the interview: if no available dimension exceeds it, the system goes straight to recommending. Questioning also ends after k questions or when the parser flags the user as impatient.[^c4] This ties the stop rule to what is left to learn in the data, a close cousin of the [[entropy-threshold-clarification-trigger]], but computed over candidate items rather than over a model's predictive distribution.

## The same signal reused for presentation

Residual uncertainty is not discarded when questioning stops. After ranking, the system picks the unspecified dimension with highest normalised entropy over the ranked set and builds a grid: candidates are grouped by value on that dimension, and the top-ranked items from each group form a labelled row. The stated purpose is to let users discover preferences by comparison along dimensions they have not committed to.[^c5] Ranking is paired with maximal marginal relevance (lambda 0.85) to avoid near-duplicates.

## What was measured

On 150 review-grounded simulated personas in a car domain, with three runs per cell, removing the entropy-guided questions lowered precision@9 in both query regimes. With long queries and embedding-similarity ranking, precision fell from 0.744 to 0.719, and with coverage-risk ranking from 0.801 to 0.753.[^c6] The authors read this as evidence that entropy-guided follow-ups clarify even when users state detailed preferences. Removing MMR cut intra-list diversity sharply (0.779 to 0.279 for short queries with similarity ranking) while often raising precision, a relevance-diversity trade-off.[^c7]

## Limits

- Entropy over attribute values measures spread in the catalogue, not what the user cares about. A highly spread attribute the user finds irrelevant is still asked first; the rule is not [[expected-information-gain]] about the user's preference, and the abstract's claim of "expected information gain" is looser than the algorithm, which is plain maximum entropy (my reading of Algorithm 1).
- The effect sizes are small, standard deviations are comparable to some of the gaps (for example 0.744 +-0.036 versus 0.719 +-0.062), and only three runs were made, so the precision gain is weakly supported (my inference from Table 1).
- Evidence comes from LLM-simulated users and an LLM judge in one domain; electronics was only noted qualitatively. No human users were tested, and no comparison against a decision-theoretic cost-aware stopping rule appears.
- The threshold 0.3 and the grid-size choices are set by hand.

## Related

- [[entropy]] — the quantity computed here over item attributes
- [[expected-information-gain]] — the principled criterion this heuristic approximates
- [[entropy-threshold-clarification-trigger]] — threshold-based asking over a model's predictive entropy
- [[elicitation-burden-tradeoff]] — the question-fatigue versus premature-commitment tension this targets
- [[task-ambiguity]] — the underspecified-query setting

[^c1]: arxiv-2603-11399 — "High entropy indicates that candidates are spread across many values for that dimension, suggesting that user input would effectively partition the candidate space."
[^c2]: arxiv-2603-11399 — "we apply quantile-based discretization into k = 3 equal-frequency"
[^c3]: arxiv-2603-11399 — "This hybrid approach separates datadriven dimension selection from language generation."
[^c4]: arxiv-2603-11399 — "we apply a minimum entropy threshold τH = 0.3. If no available dimension exceeds"
[^c5]: arxiv-2603-11399 — "enabling preference discovery through comparison."
[^c6]: arxiv-2603-11399 — "For ES under Long queries, Prec@9"
[^c7]: arxiv-2603-11399 — "disabling MMR"
