---
description: "Adaptive ranking of models stops each adjacent pair once its ordering is confident, spends items on close pairs, favours cheap models, and reports unresolved pairs as ties."
aliases: ["adaptive multi-model ranking", "continuous computerized adaptive testing", "uncertainty-aware ranker"]
sources: ["arxiv-2601-13885"]
---
# Pairwise-confidence adaptive ranking

When the goal of an evaluation is an ordering, not a score, the question budget should follow the uncertainty of the ordering. Standard computerized adaptive testing (CAT) runs each model until its own standard error falls under a fixed threshold. That gives a model far above the next-best the same budget as two models within half a standard error of each other.[^c1]

## Mechanism

Each model gets its own CAT estimator of ability. The next item is the one with maximal Fisher information at the current ability estimate. After every answer the posterior is updated and the standard error shrinks.[^c2]

Pairwise confidence is the probability that model i beats model j, from a normal approximation on the two ability estimates and their standard errors. Testing stops when every adjacent pair in the current ranking is confidently ordered at a user level gamma, or when the item budget is spent. Pairs still unresolved at the budget can be reported as tied, not forced into an order.[^c3]

For an uncertain pair, testing either model reduces the uncertainty of the comparison. The next model is therefore chosen by uncertainty reduction per unit cost, which sends more items to cheaper models.[^c4]

The method extends CAT from binary to continuous bounded scores (ROUGE, BLEU, LLM-as-judge). It replaces the Bernoulli response with a normal distribution that keeps the logistic mean and a Bernoulli-shaped variance k·mu·(1−mu). Variance is therefore highest when the expected score is most uncertain and shrinks at the bounds.[^c5] The noise parameter k is the inverse squared discrimination, so one parameter of measurement precision covers both binary and continuous cases.[^c6] Item difficulties and k are estimated once from the scores of calibration models.

## Measured

On five generation benchmarks and 21 models, with four hold-out models per fold, the ranker reached 0.75 Kendall's tau against full-evaluation rankings. It used about 2% of the items and beat random sampling by 0.13 tau. Adaptive stopping saved a further 32% of items and 39% of cost over fixed-length CAT.[^c7] The one-time calibration cost is excluded from these figures and breaks even after roughly 70 model evaluations on a dataset.[^c8] The main comparison fixed the budget at 20 items per model, below where the stopping rule would fire naturally (about 30–100 items), so the headline gain is a budget-constrained result.[^c9]

## Limits

- Calibration needs exhaustive scores from existing models, so a new benchmark has a cold-start cost. Item parameters must be re-fit for each metric.[^c10]
- Each adjacent pair is tested separately. This controls the per-comparison error, not the family-wise error. The authors put the chance of at least one misordered pair at about 18% for five models at alpha 0.05. Corrections would need more items.[^c11]
- The method targets the ranking a full evaluation would give, not latent ability. Whether the benchmark reflects true capability is outside its claim.[^c12]
- The adaptive ranker beat random sampling on 7 of 9 dataset-metric pairs, not all.[^c13]
- One shared discrimination for all items is assumed; item-specific discrimination is left to future work. The normal response has unbounded support, and the bound is only mitigated by the shrinking variance.
- My inference: the cost-aware rule assumes that item cost is constant per model. Variable item costs are listed as future work and were not tested.

## Related

- [[stopping-rules]] — this is a pairwise, confidence-threshold stopping rule over a ranking
- [[active-testing]] — also selects the items to label or score adaptively, with its own stopping rule
- [[cost-priced-joint-selection-and-stopping]] — pricing items in the selection and the stop together
- [[pairwise-advantage-validity-stopping]] — stopping on pairwise comparisons
- [[interval-overlap-three-region-ranking-decomposition]] — ranking by overlap of uncertainty intervals

[^c1]: arxiv-2601-13885 — "a model whose ability lies several standard errors above the"
[^c2]: arxiv-2601-13885 — "At each iteration, it selects the item that maximizes"
[^c3]: arxiv-2601-13885 — "they can be reported as tied rather than forced into an"
[^c4]: arxiv-2601-13885 — "we select the"
[^c5]: arxiv-2601-13885 — "the natural property that variance is highest when"
[^c6]: arxiv-2601-13885 — "high"
[^c7]: arxiv-2601-13885 — "stopping provides an additional 32% item reduction"
[^c8]: arxiv-2601-13885 — "breaks even after"
[^c9]: arxiv-2601-13885 — "We set B to the cost equivalent of 20"
[^c10]: arxiv-2601-13885 — "creating a cold-start problem for new benchmarks."
[^c11]: arxiv-2601-13885 — "which controls the per-comparison error rate but not the"
[^c12]: arxiv-2601-13885 — "not models’ latent ability in the psychometric sense."
[^c13]: arxiv-2601-13885 — "On 7 of 9 dataset-metric pairs, the"
