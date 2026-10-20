---
description: "Arrow's impossibility for multi-metric benchmarks hinges on Universal Domain; where metric rankings are single-peaked or group-separable, pairwise majority is coherent, but only on some suites."
aliases: ["Arrow escape via domain restriction in benchmarking", "single-peaked metric profiles", "benchmark as social choice"]
sources: ["arxiv-2602-07593"]
---
# Restricted-domain pairwise majority for multi-metric benchmarking

Asking "which model is best?" across several metrics is a preference-aggregation question: each metric on each dataset is a voter ranking the models. Gordienko et al. cast it this way and argue the impossibility is not fixed. Arrow's theorem needs Universal Domain, meaning every logically possible combination of metric rankings must be admissible. In benchmarking this is unreasonable: the paper says that "trade-offs across families of metrics are" systematic, so profiles are structured.[^c1] The theorem also cannot be applied to the benchmark operator directly, because the suite "does not induce the full domain of preference profiles".[^c2]

## Mechanism

Pairwise majority (model A beats B if more metrics rank A at least as high) is the natural local rule, but it can produce a Condorcet cycle, so the aggregate ranking is not transitive. The paper's escape route is to restrict the domain of profiles rather than the rule. It proves that, for a given dataset, if the metric-induced profile is single-peaked (models can be placed on one axis so each metric has a peak and declines away from it) or group-separable (with an odd number of metrics), then pairwise majority is complete, transitive, non-dictatorial, satisfies Weak Pareto and IIA. Of single-peaked profiles the paper says: "On such domain of single-peaked preferences, Condorcet cycles are impossible."[^c3] A third, distance-restricted domain is treated the same way. Intuition (the paper's): single-peakedness fits metrics that measure one latent construct or a clean trade-off such as accuracy against inference time; group separability fits metrics that agree some models are entirely above the rest.[^c4]

Rank-combining rules such as Borda are the usual alternative, but they "are unstable to changes in model set" and violate IIA, so the pairwise rule is preferred when its domain condition holds.[^c5]

Because the operator yields one ranking per dataset, a suite-level ranking requires choosing a representative among them (the paper points to depth functions over relations); this is a further step, not the domain result.

## What was measured

On HELM MMLU (57 subjects) the check is empirical and depends on which models and metrics are included. With three accuracy metrics the profiles were "single-peaked on all 57" subjects; adding more high-performing models erased this, leaving "single-peakedness holds only for three out of 57 datasets."[^c6] On another suite, none of 80 datasets was single-peaked.[^c7] Under perturbation of metric values, a Condorcet cycle appeared in at least 51 of 57 subjects in one test.[^c8] My reading: the model set and metric set decide whether the guarantee applies, so the domain check is a precondition to run, not a property of benchmarking.

## Limits

- The paper itself says "Our study is descriptive: we verify domain restrictions on" particular benchmarks; there are no inferential guarantees.[^c9]
- Guarantees are per dataset and conditional; many metric/model combinations fail, and cycles are common under perturbation.
- Group separability needs an odd number of metrics.
- Strategic behavior (optimizing against the benchmark) is untested.
- Whether the ranking helps a questioner choose what to ask is my inference, not shown.

## Related

- [[value-incommensurability]] — rank-only combination of incommensurable criteria reproduces Arrow's problem; here a structural condition licenses it
- [[rank-lexicographic-source-aggregation]] — another rank-based aggregation rule over multiple criteria
- [[median-procedure-for-n-trees]] — choosing a representative structure among many, akin to picking a central ranking

[^c1]: arxiv-2602-07593 — "trade-offs across families of metrics are"
[^c2]: arxiv-2602-07593 — "does not induce the full domain of preference profiles"
[^c3]: arxiv-2602-07593 — "preferences, Condorcet cycles are impossible."
[^c4]: arxiv-2602-07593 — "This is very plausible in cases where"
[^c5]: arxiv-2602-07593 — "problems, since they are unstable to changes in model set (e.g., see"
[^c6]: arxiv-2602-07593 — "single-peakedness holds only for three out of 57 datasets."
[^c7]: arxiv-2602-07593 — "We find that none of 80 datasets is single-peaked"
[^c8]: arxiv-2602-07593 — "persist under small perturbations of the metric values. Under this procedure, we find at least one Condorcet cycle in 51 of 57"
[^c9]: arxiv-2602-07593 — "Our study is descriptive: we verify domain restrictions on"
