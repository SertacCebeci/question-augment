---
description: "An example in a few-shot prompt is credited by its average marginal accuracy gain over random subsets of the others; the least-credited example is the candidate to replace or drop."
aliases: ["Shapley demonstration valuation", "Monte Carlo Shapley example utility", "in-context example Shapley value"]
sources: ["arxiv-2512-11013"]
---
# Shapley example utility

Few-shot examples interact. One example may only help when another is present, and two near-duplicates may each look useless while the pair is redundant. Scoring each example alone misses both cases. A Shapley value handles this by giving each example a share of the prompt's accuracy that is averaged over the ways the set could have been built. For an example i in a set of n, its value is the average, over orderings of the set, of the accuracy gained by adding i to the examples that come before it.[^c15]

Summing over all n! orderings is infeasible, so the value is estimated by sampling permutations: "approximate it by sampling K i.i.d. permutations".[^c7] Averaging the marginal contributions over those K permutations "gives an unbiased estimator" of the value.[^c1] The utility v(S) is the accuracy of the prompt built from subset S, measured on a small sampled split. The empty subset is the instruction alone, so v of the empty set is the accuracy without any examples.

In the PIAST loop the least-valued example becomes the candidate for one of three moves. Replace it with the best of several newly proposed examples, drop it, or keep it. The rule computes three scores, one per move, and "whichever score is largest" decides.[^c2] Ties go to replace, then drop. The effect is that a change is adopted only when it does not do worse than the best alternative: "This policy ensures we only adopt a modification when it".[^c3]

The estimator treats coalitions as sets and evaluates them in the fixed order the prompt will be deployed with. The authors justify this by the method's design: "algorithm never searches over orderings, only replaces or drops examples", so the attribution is wanted under the deployed order.[^c4] The instruction is held fixed; "Our final prompt consists of the hand-crafted instruction proposed by (Zhang et al., 2022)" and the examples are what the loop changes.[^c13]

What the paper measures against this is a leave-one-out rule, which removes each example once and picks the one whose removal does best. Across several classification benchmarks, leave-one-out "attains results comparable to our full method, but" on SUBJ the gap is clear.[^c5] The authors read the difference as a matter of starting point: where the initial pool is already mostly good, leave-one-out makes small useful adjustments; where the outcome depends on which examples happen to be present, Shapley credit is "sensitive to initialization" and more robust.[^c6] The numbers are averages over three runs: "All reported numbers (main results and ablations) are averaged over".[^c10]

The Shapley step is not used for the replace-drop-keep decision itself. The authors note that the decision "could also be formulated directly using Shapley" values, but that doing so "would significantly increase" the cost of each iteration, and speed was the design goal.[^c8]

Because each round scores examples on a small subsample of the training data, the scores can flatter examples that happen to suit that subsample. The paper's remedy is a replay buffer: "newly crafted examples can overfit the" current subset, so a small part of earlier data is kept and merged into later rounds.[^c9] The training set enters only through accuracy: "The only information it gets from the" training set "is its accuracy with the given prompt."[^c14]

## Limits

- The gap between Shapley credit and leave-one-out is shown clearly on one classification task (SUBJ) in the text read. On the others the two rules are reported as comparable. The advantage of Shapley credit as such is therefore not established across tasks.
- The estimator is unbiased for v as defined. v is itself an accuracy on a small split, so the credits carry that split's noise. The replay buffer is the stated answer; its effect is not separated by an ablation in the text read. (My reading.)
- The Shapley axioms, such as credits summing to the full-set accuracy, hold for an exact v. Under a noisy, subsampled v they hold at best in expectation. The transfer keeps the idea of crediting an example by its average marginal contribution and loses any exact accounting of the total. (My inference.)
- Credit is conditional on one fixed order. Whether a different order would change which example is least useful was not tested. (My inference from the design choice.)
- Longer optimisation can overfit the evaluator. In cross-model transfer the extended run showed "accuracy drop, which we attribute to overfitting to" the source model, so more iterations of a Shapley-driven loop do not guarantee better transfer.
- The method "relies on the LLM having" some task-specific competence to propose useful examples. Where it does not, the authors expect a more involved synthesis would be needed.[^c12]
- The source is an arXiv preprint (v2, April 2026) and the figures are the authors' own.

## Related

- [[similarity-selected-exemplars]] — chooses demonstrations per test item by similarity; this note's method fixes one set per task, which is why the paper does not compare against retrieval.
- [[error-selected-exemplars]] — picks demonstrations by the model's baseline errors, a different signal for the same question of which examples to show.
- [[active-in-context-learning]] — chooses labeled items for the context by acquisition rule under a frozen predictor; the same question of which examples enter the prompt, asked of a tabular setting.
- [[shapley-uncertainty-localization]] — applies Shapley attribution to ambiguous input spans rather than to prompt examples.
- [[evolutionary-prompt-search]] — searches over prompt wording; the method here searches over examples with the wording held fixed.

[^c1]: arxiv-2512-11013 — "averaging over K permutations gives an unbiased estimator"
[^c2]: arxiv-2512-11013 — "whichever score is largest"
[^c3]: arxiv-2512-11013 — "This policy ensures we only adopt a modification when it"
[^c4]: arxiv-2512-11013 — "algorithm never searches over orderings, only replaces or drops examples"
[^c5]: arxiv-2512-11013 — "attains results comparable to our full method, but"
[^c6]: arxiv-2512-11013 — "sensitive to initialization (see PIAST (I)), and the"
[^c7]: arxiv-2512-11013 — "approximate it by sampling K i.i.d. permutations"
[^c8]: arxiv-2512-11013 — "However, this would significantly increase"
[^c9]: arxiv-2512-11013 — "newly crafted examples can overfit the"
[^c10]: arxiv-2512-11013 — "All reported numbers (main results and ablations) are averaged over"
[^c12]: arxiv-2512-11013 — "PIAST relies on the LLM having"
[^c13]: arxiv-2512-11013 — "Our final prompt consists of the hand-crafted instruction proposed by (Zhang et al., 2022)"
[^c14]: arxiv-2512-11013 — "The only information it gets from the"
[^c15]: arxiv-2512-11013 — "Monte Carlo Shapley estimation of example utility"
