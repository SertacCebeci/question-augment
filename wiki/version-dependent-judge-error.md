---
description: "A fixed judge's error rates can depend on which agent version produced the output, so the judged difference between two versions is biased beyond mere shrinkage."
aliases: ["differential misclassification", "agent-dependent judge error", "version-dependent judge error"]
sources: ["doi-10-48550-arxiv-2609-34198"]
---
# Version-dependent judge error

When an agent is upgraded, the judge that scores its outputs is usually held fixed, on the assumption that a difference in judged success then reflects a difference in actual success.[^c1] That assumption fails when the judge's error rates depend on which agent produced the trajectory. Write TPR and FPR for the judge's true- and false-positive rates on each version, and J = TPR − FPR for its Youden index. The judged difference between a new and an old version then differs from the true difference by one identity: the comparison error is a differential term δ, built from the change in TPR and FPR, minus an attenuation term (1 − J_o) times the true difference.[^c2] When the error is marginally non-differential (equal TPR and FPR on both versions), δ is zero and the judged difference keeps the true sign while being shrunk by J.[^c3] The differential term is the part that can reverse a comparison, or make a difference appear where none exists.

Two notions of non-differential error need to be kept apart.[^c4] A judge is conditionally non-differential when, for each task and reference label, its verdict probability is the same whichever version produced the output. It is marginally non-differential when the two versions have equal TPR and FPR. Neither implies the other: a judge can be conditionally non-differential and still have a marginal TPR that drops when the new version solves tasks that are harder to recognise (my reading of the paper's definitions in its Section 3.1).

**Measured.** On 35 public mini-SWE-agent submissions graded on 250 SWE-bench Verified issues, every available judge rejects the within-(task, reference label) exchangeability null, that is, the verdicts carry information about the agent beyond the task and the reference outcome.[^c5] The differential comparison component is detectable in 32 of the 60 judge-by-version-pair units after false-discovery adjustment.[^c6] Rank agreement is not the same thing: all three judges have a positive Kendall correlation with the reference ordering of the 35 agents.[^c7] The discrepancy is tied to capability. "Successful-patch acceptance also rises with capability, but false acceptance rises faster" [^c8]: the within-task false-positive contrast tracks the reference resolve rate, while the Youden contrast falls. A shuffle of verdicts within each judge, task and reference-label stratum drives the mean correlations to about zero, so the pattern is not a mechanical product of task mix.[^c9]

The transfer from epidemiology is worth stating. The algebra is the classical misclassification decomposition, which the paper restates for version pairs. What is not identified is the agent-specific remainder: the paper computes it as a leave-pair-out prediction, "rather than an identified causal decomposition".[^c10] Read this way, the differential term is a quantity the data can estimate and test, not a causal effect of the agent on the judge.

## Limits

- The pairs are observational. "Version pairs are observational: a released upgrade can change several things at once" [^c11], so a difference between versions is not a difference in one cause.
- The reference is not ground truth. "Execution-based labels are not ground truth." [^c12] Part of what the note calls differential judge error may be differential reference error, "part of what we call differential judge error is" [^c13] a reference that errs more for some agents.
- The capability pattern is an association, not a law. "This is an association among public configurations of one scaffold, not evidence that" [^c14] raising capability changes what the judge does. "The SWE-bench agents share one scaffold family" [^c15], so other scaffolds are untested.
- The judge set was reduced by an outage. Claude became unavailable before completing SWE-bench, so the primary analysis uses three judges, and the fourth is descriptive only.
- Power is low for close pairs. With 250 tasks, "of close versions have low power" [^c16], and the paper leans on interval estimates rather than counts of significant pairs.
- The measured quantity is a verdict on a patch, not on the full trajectory. The judge saw the repository, the issue and the patch; judges that can execute code may err differently.

## Related

- [[calibrated-judge-estimator-efficiency-ordering]] — the single-rate case, where measurement-error correction is one estimator among several; the differential term has no place in that setting
- [[llm-judge-biases]] — average-case judge biases such as position and verbosity; differential error is agent-specific, and can be present even when the average bias is small
- [[model-dependent-benchmark-difficulty]] — the same dependence on the subject, located in the benchmark's difficulty rather than in the judge's errors
- [[youden-index-threshold-for-noisy-reward-learning]] — the Youden index J = TPR − FPR, the judge's discriminability, which sets how much of a difference survives
- [[transported-judge-calibration]] — correcting the new version with the old version's error rates, which divides this differential term by the old Youden index
- [[paired-difference-judge-efficiency]] — how many labels a judge saves for a paired comparison, under the non-differential benchmark this note departs from

[^c1]: doi-10-48550-arxiv-2609-34198 — "is held fixed, a difference in judged success between two versions reflects a difference in their actual"
[^c2]: doi-10-48550-arxiv-2609-34198 — "This is the classical decomposition of misclassification bias"
[^c3]: doi-10-48550-arxiv-2609-34198 — "true sign and is shrunk by J ≤ 1."
[^c4]: doi-10-48550-arxiv-2609-34198 — "Two notions of non-differential error must be kept apart."
[^c5]: doi-10-48550-arxiv-2609-34198 — "Every available judge rejects the within-(task, reference label) exchangeability null"
[^c6]: doi-10-48550-arxiv-2609-34198 — "32 of the 60 judge-by-version-pair units (53.3%)"
[^c7]: doi-10-48550-arxiv-2609-34198 — "All three judges have a positive Kendall correlation with the reference ordering of 35 agents"
[^c8]: doi-10-48550-arxiv-2609-34198 — "Successful-patch acceptance also rises with capability, but false acceptance rises faster"
[^c9]: doi-10-48550-arxiv-2609-34198 — "the mean correlations are −0.001 for FPR and +0.004 for Youden"
[^c10]: doi-10-48550-arxiv-2609-34198 — "rather than an identified causal decomposition"
[^c11]: doi-10-48550-arxiv-2609-34198 — "Version pairs are observational: a released upgrade can change several things at once"
[^c12]: doi-10-48550-arxiv-2609-34198 — "Execution-based labels are not ground truth."
[^c13]: doi-10-48550-arxiv-2609-34198 — "part of what we call differential judge error is"
[^c14]: doi-10-48550-arxiv-2609-34198 — "This is an association among public configurations of one scaffold, not evidence that"
[^c15]: doi-10-48550-arxiv-2609-34198 — "The SWE-bench agents share one scaffold family"
[^c16]: doi-10-48550-arxiv-2609-34198 — "of close versions have low power"
