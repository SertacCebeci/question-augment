---
description: "A costly pairwise LLM judgement is rewritten as a CNF of cheap feature-distance predicates that prune pairs before the LLM; thresholds are set for a recall guarantee."
aliases: ["FDJ", "Featurized-Decomposition Join", "feature-based pruning before LLM judgement"]
sources: ["arxiv-2512-05399"]
---
# Featurized decomposition

A semantic join asks an LLM, for every pair of records, whether a natural-language
condition holds. The naive cost is quadratic in the number of records. Earlier
work reduced it with a model cascade: embed each record, score each pair by
cosine similarity, and set cascade thresholds so that "low similarity are
discarded as non-matches, those with high similarity are accepted as matches, and
pairs with inconclusive scores" go to the LLM.[^f1] The weak point is the
embedding. Zeighami, Shankar and Parameswaran argue that a single vector cannot
carry the join criterion for long, mixed records: "Embedding this information
into a single vector fails to capture the relevant details with sufficient
fidelity." In their police-records example the cascade defers "to the LLM on
around 80% of all record pairs, thus costing close to" the naive cost.[^f2][^f3]

The alternative rewrites the join condition itself. A *featurized decomposition*
is "a logical expression in conjunctive normal form that we call a featurized
decomposition to effectively prune out non-matching pairs."[^f4] Its parts are:
functions that extract features from each record; predicates that compare the
features of a left and a right record with a feature-specific distance (lexical,
arithmetic, or embedding-based) and a threshold; and a CNF that combines the
predicates. In the paper's police example one predicate checks whether officer
names "are within threshold 0.3", and others check dates and locations.[^f5]

The cost structure is what makes the rewrite pay. Feature extraction is one
pass over each table, while the predicates are cheap comparisons evaluated on
every pair. The paper says extraction "requires only a linear pass over the
records with an LLM, relative to performing a quadratic number of pairwise
comparisons with an LLM."[^f6] Pairs the decomposition rejects never reach the
LLM. Pairs it accepts are refined by an LLM call, and the paper's cost is
driven by the false positives the decomposition lets through: "false positive
pairs introduced incur additional cost of LLM calls."[^f7]

The thresholds carry the guarantee. "we first sample a set, S, uniformly at
random" from the product and label it with the LLM; each threshold is then chosen
so that recall on the whole product meets the target with high probability.[^f8]
The paper's Theorem 6.1 adjusts the target for the number of clauses r and the
number of positive sample pairs k+. The authors describe it as "generalizing
existing bounds in the model cascade literature that set" one-dimensional
thresholds, extended to high dimensions.[^f9] Its conditions, a bound on r and a
lower bound on k+, are "an artifact of our proof technique."[^f10] Reported
results are that FDJ "has about half the cost on" average against BARGAIN, and
"reduces the cost up to 10 times on some datasets," across the paper's
experiments.[^f11][^f12][^f13]

What transfers to asking is the separation of a costly judgement into a cheap
screen and a residual that is still put to the expensive source. The screen is
built from features chosen to be sufficient for the judgement, and its
threshold is set from labelled samples rather than from intuition. My inference,
not the paper's claim: a question could be run through a cheap decomposition
before the expensive answerer is consulted, and the decomposition's recall could
be bounded in the same way. The paper does not study questions, answers or
human asking, so this bridge is mine.

## Limits

- The guarantee is over a uniform sample of record pairs. It bounds recall on
  the product, not on the particular pairs an asker cares about, and it holds
  only when the labelled sample is representative.
- The theorem's conditions are, per the authors, an artifact of the proof: they
  "saw no practical need for them" in experiments, but the paper does not show
  the bound without them.[^f14]
- Choosing a lowest-cost decomposition is NP-hard ("MCFD is NP-hard."),[^f15] so
  the construction is a search. The paper says the procedure "uses labeled
  samples to iteratively refine them",[^f16] and it does not claim optimality.
- Feature extraction is itself an LLM task, and the paper motivates the whole
  method with the fact that "LLMs often miss" important features.[^f17] Errors in
  extraction enter the cost only through the false-positive rate.
- The cost model counts "the cost of using LLMs and embedding" models.[^f18]
  Latency, human effort and answer quality beyond the stated precision and recall
  targets are outside it.
- The empirical claims come from six real datasets.[^f13] I read only the
  introduction's summary of them, not the experiments, so the spread of gains
  across datasets is not mine to state. Whether the gains hold for open-ended
  questions with no pairwise structure is not tested here.

## Related

- [[value-of-information]] — weighs what an answer teaches against what asking costs; the featurized decomposition is a cost device that acts before any answer is bought
- [[expected-information-gain]] — ranks candidate questions by their answer distribution before asking; the decomposition instead prunes which pairs are asked at all, and carries a recall bound rather than an information score

[^f1]: arxiv-2512-05399 — "low similarity are discarded as non-matches, those with high similarity are accepted as matches, and pairs with inconclusive scores"
[^f2]: arxiv-2512-05399 — "Embedding this information into a single vector fails to capture the"
[^f3]: arxiv-2512-05399 — "to the LLM on around 80% of all record pairs, thus costing close to"
[^f4]: arxiv-2512-05399 — "logical expression in conjunctive normal form that we call a featurized decomposition to effectively prune out non-matching pairs."
[^f5]: arxiv-2512-05399 — "are within threshold 0.3"
[^f6]: arxiv-2512-05399 — "relative to performing a quadratic number of pairwise"
[^f7]: arxiv-2512-05399 — "false positive pairs introduced incur additional cost of LLM calls"
[^f8]: arxiv-2512-05399 — "we first sample a set, S, uniformly at random"
[^f9]: arxiv-2512-05399 — "generalizing existing bounds in the model cascade literature that set"
[^f10]: arxiv-2512-05399 — "an artifact of our proof technique"
[^f11]: arxiv-2512-05399 — "FDJ has about half the cost on"
[^f12]: arxiv-2512-05399 — "reduces the cost up to 10 times on some datasets"
[^f13]: arxiv-2512-05399 — "Our experimental evaluation across 6 different real-world"
[^f14]: arxiv-2512-05399 — "saw no practical need for them. For example, for the common case"
[^f15]: arxiv-2512-05399 — "MCFD is NP-hard."
[^f16]: arxiv-2512-05399 — "uses labeled samples to iteratively refine them"
[^f17]: arxiv-2512-05399 — "LLMs often miss"
[^f18]: arxiv-2512-05399 — "We focus on the cost of using LLMs and embedding"
