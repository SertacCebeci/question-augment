---
description: "Federated group-conditional conformal calibration: clients sketch scores per group-membership atom into mergeable digests; coverage loses at most sin(pi/delta) against the centralized guarantee."
aliases: ["GC-FCP", "group-conditional federated conformal prediction", "atom-stratified coreset calibration"]
sources: ["arxiv-2603-14198"]
---
# Atom-stratified federated conformal calibration

Marginal conformal prediction is valid on average over the whole population, so it can fail on a subgroup. [[mondrian-conformal-prediction]] repairs this for disjoint groups; CondCP extends it to overlapping groups, "allows for overlapping groups by reframing conditional coverage as simultaneous coverage over a class of covariate shifts".[^c1] Both need the pooled calibration scores. When the calibration data sit on separate clients, pooling costs communication, computation and privacy. GC-FCP (Wen, Xing and Simeone) is a federated version of CondCP for a target mixture over prespecified, possibly overlapping groups.[^c2]

## Mechanism

1. **Atoms.** The input space is cut into the smallest disjoint partition from which every group can be recovered by unions. Each atom is the set of points with one group-membership pattern, meaning inside exactly the groups in S and outside all the others. Points in an atom share the same membership vector.[^c3]
2. **Local sketches.** Each client splits its nonconformity scores by atom and compresses each non-empty atom's scores into a T-Digest. Raw examples stay on the client.[^c4]
3. **Merge.** The server merges the digests atom by atom. The union of the merged digests is the coreset.[^c5]
4. **Solve.** The server solves the CondCP quantile-regression problem (a regression of the score on the membership vector, with the pinball loss) on the coreset instead of on all n scores. The prediction set contains every label whose score is below the fitted group-dependent threshold.[^c6]

## What was shown

- **Coverage.** For each group G the sketched method satisfies P(Y in C(X) | X in G) ≥ 1 − α − sin(π/δ), where δ is the digest compression parameter.[^c7] The proof rests on a uniform bound on the digest's CDF error: "produced by T-Digest satisfies the uniform accuracy bound". The authors call the finite-sample analysis technically challenging, because coreset samples are not exchangeable and the sketch adds approximation error.[^c8] The coverage loss is therefore set by the compression level. An upper bound is also given, so the method cannot be arbitrarily conservative (Appendix C).
- **Cost.** Communication is O(δ·Σ|active atoms per client|), against O(n) "for score-based communication of CondCP".[^c9] The server solve scales with the coreset size, not with n.
- **Atom count.** In the worst case overlaps can yield up to 2^|G| atoms. The gain relies on the active atoms being few; for one-dimensional interval groups the count grows linearly with |G|.[^c10]
- **Experiments.** Synthetic regression, CIFAR-10 and PathMNIST were compared with centralized CP, FedCP and centralized CondCP. CondCP and the centralized variant were run only on the small synthetic data and CIFAR-10 because of their cost. I read the setup, not the result tables, so I cannot quote effect sizes.[^c11]

## Why it matters for asking and answering

A stated confidence is only as trustworthy as the slice it is checked on. Making the guarantee group-conditional means a consumer of the answer can rely on it for the slice that matters. This note shows the guarantee can be kept when evidence is distributed and cannot be pooled, at a price quantified by the compression parameter. This reading of the relevance is mine, not the paper's.

## Limits

- The privacy claim is weak: the method "does not provide any formal privacy guarantee". Atom membership patterns, counts and centroid weights are exposed, and the analysis assumes a trustworthy server.[^c12]
- Groups must be prespecified. Groups discovered after calibration are not covered.
- Efficiency depends on the number of active atoms being moderate; with many overlapping groups it degrades toward the centralized cost (my inference from the 2^|G| worst case).
- The guarantee is a lower bound with a sketch-error term. It is not exact finite-sample validity, and the bound assumes the server's optimization is solved exactly.
- Exchangeability within the target mixture is assumed. Personalized coverage for each client's own distribution is a different target, handled by other work.

## Related

- [[mondrian-conformal-prediction]] — disjoint-group special case that needs pooled scores
- [[hierarchical-group-conditional-conformal-risk-control]] — another group-conditional conformal guarantee
- [[sequence-level-conformal-prediction]] — conformal sets in another setting
- [[exceedance-design-effect]] — coverage error from finite data

[^c1]: arxiv-2603-14198 — "allows for overlapping groups by reframing conditional coverage as simultaneous coverage over a class of covariate shifts"
[^c2]: arxiv-2603-14198 — "constructs mergeable, atom-stratified coresets from"
[^c3]: arxiv-2603-14198 — "Although arbitrary overlaps can induce up to"
[^c4]: arxiv-2603-14198 — "GC-FCP first stratifies the data at the clients into disjoint atoms"
[^c5]: arxiv-2603-14198
[^c6]: arxiv-2603-14198
[^c7]: arxiv-2603-14198 — "Theorem 5.1 (Group-conditional coverage guarantees for"
[^c8]: arxiv-2603-14198 — "Deriving finite-sample group-conditional guarantees for GCFCP is technically challenging"
[^c9]: arxiv-2603-14198 — "compared to order O(n) for score-based communication of CondCP"
[^c10]: arxiv-2603-14198
[^c11]: arxiv-2603-14198 — "CondCP and centralized GC-FCP are only evaluated on the small-scale synthetic"
[^c12]: arxiv-2603-14198 — "does not provide any formal privacy guarantee"
