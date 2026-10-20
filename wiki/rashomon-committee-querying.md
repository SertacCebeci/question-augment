---
description: "Query where all near-optimal models (the Rashomon set), weighted by a Gibbs posterior, disagree most; this grounds committee disagreement in model multiplicity and helps under moderate label noise."
aliases: ["REAL", "Rashomon Ensembled Active Learning", "epsilon-version space querying", "Rashomon-weighted vote entropy"]
sources: ["arxiv-2603-22750"]
---
# Rashomon committee querying

Query-by-committee picks the unlabeled instance on which a committee of hypotheses disagrees most. The usual committee is made by perturbation: bootstrapping or random feature subsets, as in random forests. Rashomon Ensembled Active Learning (REAL) replaces it with the set of all models whose training objective is within a factor (1+epsilon) of the optimum, enumerated exactly for sparse decision trees.[^c1] Any disagreement then separates two models that fit the same evidence about equally well, not two random subsamples.[^c2]

## Mechanism

The tree objective is misclassification plus lambda times leaf count. The epsilon-Rashomon set holds every tree within (1+epsilon) of the best objective.[^c3] At epsilon = 0 it is the classical [[version-space]]. A larger epsilon gives an "epsilon-version space" that keeps hypotheses a noisy or misspecified problem cannot rule out.[^c4]

Treating every member equally lets near-duplicate trees dominate the vote ("structural saturation"). Pruning to representatives discards how many near-optimal structures support a boundary. REAL instead gives each tree a Gibbs weight proportional to exp(-beta times its objective), so better-fitting trees count more.[^c5] The uniform-weight variant is called UNREAL and the Gibbs variant BREAL. The query is the instance with maximal weighted vote entropy over the weighted committee. An Effective Committee Size, the exponential of the weight entropy, tracks how broad the plausible space still is. A value near 1 means collapse onto one hypothesis.[^c6] Each new label shrinks the set.

Setup details: the selector's epsilon is raised in steps of 0.05 until the set has at least 2 members. Beta is chosen by grid search to maximize the AUPRC between vote entropy and actual errors.[^c7]

## What was measured

The test used synthetic data with 20 binary features, of which 2 are informative. The labels were a mixture of an XOR tree rule and a linear rule, with mixture weight alpha. Noise flipped 5 to 45 percent of labels. Runs used 25 replications, a 20-sample initial set, and comparison with random-forest QBC, uncertainty sampling and coreset.[^c8]

- At low misspecification (alpha = 0.25) REAL reached a higher accuracy ceiling, because random feature subsetting often misses the sparse signal by chance.[^c9]
- Under total misspecification the Rashomon set becomes "equally misspecified experts". REAL still found stable boundaries earlier, but the random forest's variance acted as a smoothing buffer that made the gap narrow.[^c10]
- Under label noise the Rashomon set grows, and REAL's advantage widened until extreme noise (0.45) equalized all strategies.[^c11]

## Limits

- Only sparse decision trees were tested, because exact enumeration exists only for them. How far the idea carries to model classes without enumeration is not shown. Sampling the set is my untested suggestion.
- The selector's depth, lambda, epsilon and beta were tuned on a 20-sample pilot. The paper does not test how fragile that tuning is.
- The abstract states a moderate-noise advantage. The paper's own text says the gap narrows under misspecification, and it ends at extreme noise. The "robust" label holds only for the synthetic regimes tried.
- The paper says it also ran 20 real-world benchmarks. I read the design and synthetic results but not those tables, so no real-data claim is made here.
- The paper's explanation, that REAL isolates robust structure from noise-induced hypotheses, is an interpretation and was not isolated by an ablation I read.

## Related

- [[version-space]] — REAL generalizes the version space from perfectly consistent hypotheses to the epsilon-radius set.
- [[generalized-binary-search]] — the half-split rule over surviving hypotheses; here the vote is weighted and the entropy is soft.
- [[active-probing]] — another query-the-split-of-surviving-hypotheses scheme, applied to an LLM informant.
- [[adaptive-submodularity]] — a theoretical frame for greedy information-gain querying.

[^c1]: arxiv-2603-22750 — "REAL) which constructs a committee by"
[^c2]: arxiv-2603-22750 — "we ensure that any observed disagreement represents a conflict between two plausible structural"
[^c3]: arxiv-2603-22750 — "We define the ϵ-Rashomon Set, R̂(ϵ, Dtr ), as the set of all"
[^c4]: arxiv-2603-22750 — "retaining diverse models that are indistinguishable based on training error alone."
[^c5]: arxiv-2603-22750 — "we assign each tree h ∈ R̂(ϵ)"
[^c6]: arxiv-2603-22750 — "signals a collapse of the ϵ-version space onto a single"
[^c7]: arxiv-2603-22750 — "to maximize the Area Under the Precision-Recall Curve"
[^c8]: arxiv-2603-22750 — "Experiments used N = 25 independent replications with"
[^c9]: arxiv-2603-22750 — "REAL (both versions) demonstrates superiority (see Figures"
[^c10]: arxiv-2603-22750 — "equally misspecified experts."
[^c11]: arxiv-2603-22750 — "with its advantage"
