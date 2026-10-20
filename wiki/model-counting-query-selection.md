---
description: "Counting the hypotheses left under each possible answer, with approximate model counting over a SAT encoding, picks the query that most halves the version space without enumerating it."
aliases: ["SAMCAL", "ApproxMC-guided query selection", "model-counting guided active learning"]
sources: ["arxiv-2512-03971"]
---
# Model-counting query selection

A learner that must recover an unknown Boolean function from membership queries can keep its hypotheses symbolic instead of listing them. The space of depth-$d$ decision trees over $n$ features is written as one propositional formula: the space "can be encoded compactly as a propositional formula in conjunctive normal form".[^c1] Each oracle answer adds a constraint, so the formula at any moment stands for the hypotheses still consistent with the answers so far. That is the [[version-space]], held as a CNF rather than as a list.

The next query is chosen by counting. For each unqueried input $x$, an approximate counter estimates how many surviving hypotheses would output 0 on $x$ and how many would output 1. The score of $x$ is the smaller of the two, and the input with the highest score is asked.[^c2] This is the halving rule of [[generalized-binary-search]], with counts in place of enumerated hypotheses: "our learner selects the input that approximately halves the number of consistent hypotheses".[^c3] The conclusion describes the same step as estimating the expected information gain of each query: the candidate query "is estimated using approximate model counting".[^c4] The operative score, though, is a minimum of two counts, not an entropy, so that label is loose. See [[expected-information-gain]] for what the entropy version measures.

The counter is ApproxMC, which estimates the number of "satisfying assignments of a CNF formula without exhaustively enumerating all" models.[^c5] The related-work section says that approximate counters such as ApproxMC "provide provable (ε, δ) guarantees using universal hashing".[^c6] The count is therefore an estimate with an error form stated by the counter, not an exact tally of trees. Counting is needed because enumeration fails at scale: "the number of candidate decision trees grows exponentially with the number of features and the tree depth".[^c7]

**What was measured.** On the worked example (depth 2, three features, 432 candidate trees before any query), the approximate remaining count goes 432, 216, 108, 72, 35, 17, 9, 1 over seven queries (Table 1). The text reads the run as "hypothesis steadily reduces from step one to step six, achieving near halving".[^c8] Across the experiments the authors report that the method "consistently reduced the hypothesis space at an exponential rate before query 10".[^c9] In the deepest settings the initial spaces were "ranging from hundreds of thousands to several billion",[^c10] and the reduction was "typically stabilizing or collapsing within 8–12 queries".[^c11]

**Stopping.** The count alone does not end the search, because distinct trees can compute one function. The learner watches the count: its stagnation test is "Check for ApproxMC stagnation", a change of less than 1 between successive counts.[^c12] When the count stalls, it makes two copies of the remaining formula and asks a SAT solver whether they can disagree on some input. The solver is "invoked to determine if this assumption is unsatisfiable".[^c13] If no disagreement exists, the remaining trees compute one function, and the paper says this lets the learner "collapse equivalent hypotheses into one and continue refining and terminate the learning process".[^c14] In the reported stagnation cases the check was fast: "the SAT check completes in less" than a second.[^c15]

**Scope of the evidence.** Each setting uses "one ground truth" tree, generated at random;[^c16] the grid is "depth = [2, 3," and on up to five features.[^c17]

**What transfers (my reading).** Two things survive a move to other question-asking settings: the question is picked by the balance of surviving counts, and the search ends on a semantic test rather than on a count of one. What does not survive is the encoding. ApproxMC counts CNF formulas over a finite Boolean domain with a fixed hypothesis language. A free-text answer has neither, and the [[version-space]] note already requires the language to be declared before the answers arrive.

## Limits

- **The halving is assumed, not shown for each query.** The derivation of $|V_{t+1}| \approx |V_t|/2$ holds "assuming the query is near-optimal".[^c18] The authors also say that "the fraction of eliminated trees varies per query and is rarely exactly 50%."[^c19]
- **No query-complexity bound.** The paper "also does not provide theoretical query complexity guarantees".[^c20] Its $\lesssim \log_2 |H|$ query count is conditional on the near-halving assumption, so it is not a bound the method is shown to meet. The greedy guarantees of [[adaptive-submodularity]] belong to a different setting and are not claimed here.
- **Counting error can misdirect the choice.** The authors concede that "may occasionally select suboptimal queries if estimation error skews comparison".[^c21]
- **Cost grows with the formula.** "The runtime of our algorithm scales with the cost of approximate model counting";[^c22] the stated reach is "10k CNF clauses with over 1k variables",[^c23] and non-binary nodes would make the formula grow further, since the internal nodes could "support more than binary decisions".[^c24]
- **Noise breaks the mechanism.** "Finally, our evaluation assumes a noise-free oracle."[^c25] A wrong answer adds a false clause, and "the current SAT-based mechanism offers no robustness guarantees."[^c26] This is the same fragility noted for [[version-space]].
- **The counts are over trees, not over functions.** The hypothesis class lets features repeat: "each internal node selects one feature from the n features (selection may".[^c27] Its size is "the number of distinct hypotheses" of that class.[^c28] My inference, not the paper's: distinct trees can compute one function, so a count over trees weights each function by how many trees represent it. The paper's own check exists because the survivors may be "functionally identical".[^c29]
- **Small evaluation.** The reported experiments are a single Python tool on randomly generated targets. The sections read report no comparison against a heuristic such as information gain, so no claim is made here that the counting rule beats one.

## Related

- [[version-space]] — the object being counted; this note adds a counting estimator and a semantic stopping test to it.
- [[generalized-binary-search]] — the same min-balance rule, here over tree counts rather than mass over effective hypotheses.
- [[expected-information-gain]] — the conclusion's name for this step; the operative score is a minimum of counts, a halving rule.
- [[adaptive-submodularity]] — supplies greedy guarantees for its own setting; this paper claims none for its.
- [[rashomon-committee-querying]] — also queries over decision trees, but enumerates the epsilon-Rashomon set where this note counts.

[^c1]: arxiv-2512-03971 — "can be encoded compactly as a propositional formula in conjunctive normal form"
[^c2]: arxiv-2512-03971 — "The ideal query maximizes the minimum reduction in the version space"
[^c3]: arxiv-2512-03971 — "our learner selects the input that approximately halves the number"
[^c4]: arxiv-2512-03971 — "candidate query is estimated using approximate model counting"
[^c5]: arxiv-2512-03971 — "satisfying assignments of a CNF formula without exhaustively enumerating all"
[^c6]: arxiv-2512-03971 — "provide provable (ε, δ) guarantees using universal hashing"
[^c7]: arxiv-2512-03971 — "the number of candidate decision trees grows exponentially with the number of features and the tree depth"
[^c8]: arxiv-2512-03971 — "hypothesis steadily reduces from step one to step six, achieving near halving"
[^c9]: arxiv-2512-03971 — "the hypothesis space at an exponential rate before query 10"
[^c10]: arxiv-2512-03971 — "ranging from hundreds of thousands to several billion"
[^c11]: arxiv-2512-03971 — "typically stabilizing or collapsing within 8–12 queries"
[^c12]: arxiv-2512-03971 — "Check for ApproxMC stagnation"
[^c13]: arxiv-2512-03971 — "invoked to determine if this assumption is unsatisfiable"
[^c14]: arxiv-2512-03971 — "collapse equivalent hypotheses into one and continue refining and terminate the"
[^c15]: arxiv-2512-03971 — "the SAT check completes in less"
[^c16]: arxiv-2512-03971 — "For each tree setting, we randomly generate one ground truth"
[^c17]: arxiv-2512-03971 — "We evaluate our tool under the decision trees setting with depth = [2, 3,"
[^c18]: arxiv-2512-03971 — "assuming the query is near-optimal"
[^c19]: arxiv-2512-03971 — "trees varies per query and is rarely exactly 50%."
[^c20]: arxiv-2512-03971 — "also does not provide theoretical query complexity guarantees"
[^c21]: arxiv-2512-03971 — "may occasionally select suboptimal queries if estimation error skews comparison"
[^c22]: arxiv-2512-03971 — "the runtime of our algorithm scales with the cost of approximate model counting"
[^c23]: arxiv-2512-03971 — "10k CNF clauses with over 1k variables"
[^c24]: arxiv-2512-03971 — "support more than binary decisions"
[^c25]: arxiv-2512-03971 — "Finally, our evaluation assumes a noise-free oracle."
[^c26]: arxiv-2512-03971 — "the current SAT-based mechanism offers no robustness guarantees"
[^c27]: arxiv-2512-03971 — "each internal node selects one feature from the n features (selection may"
[^c28]: arxiv-2512-03971 — "Then the number of distinct hypotheses in Hd,n is"
[^c29]: arxiv-2512-03971 — "to verify that all remaining hypotheses are functionally identical"
