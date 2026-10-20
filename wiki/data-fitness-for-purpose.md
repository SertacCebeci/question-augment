---
description: "Whether a data source is fit for a causal question is judged against that question, not by its size; the same records can suit one estimand and fail another."
aliases: ["fit for purpose", "data fitness", "fitness for purpose"]
sources: ["arxiv-2511-19735"]
---
# Data fitness for purpose

Data fitness asks whether a source holds the right information, at sufficient quality, for one stated causal question. The paper's position is that fitness is not a property of the data alone: "RWD is not automatically fit for causal use simply because it is large".[^d1] The roadmap gives it a step of its own, "Assess data provenance, alignment, and fitness for purpose",[^d2] and says this is "often the most consequential step" in integrative settings.[^d3]

The threats are listed concretely. Selection bias arises "when RWD populations differ systematically from those in RCTs".[^d4] Unmeasured confounding arises when key clinical variables are missing or inconsistently captured. Immortal time bias arises when treatment initiation and outcome follow-up are not anchored to a common baseline. Measurement error arises when routine-care outcomes do not match trial-defined endpoints. The roadmap's own list for Step 2 adds "coding drift, linkage error, treatment and outcome misclassification",[^d5] and the paper notes these can "silently bias and invalidate causal conclusions".[^d6]

The mechanism is a check made against the question rather than against the dataset. A registry that is large and well-kept may still record the wrong baseline for the estimand, so its size says nothing about whether it addresses the causal contrast. The fitness judgement therefore has to be repeated for each estimand that the same data are asked to serve. This is why the estimand comes first in the roadmap: fitness cannot be assessed until the question names what the data must contain.

Some threats can be dealt with. The paper says "Some can be partially mitigated through principled design, causal inference, calibration, validation studies, or sensitivity analysis".[^d7] Others cannot be fixed by method, and the text allows that they leave a causal estimand not credible for the intended decision. AI does not change this: the paper says the tools "do not eliminate the need for scientific judgment" in this step.[^d8]

What transfers, in my reading: an answer drawn from a source is only as good as the source's fit to the question asked. Whether a log, a benchmark or a sample contains the variable a question needs is a fitness question of this kind. The paper argues the point for health data only; the transfer is my inference.

## Limits

- The threat list is argued from regulatory guidance and the authors' experience. The text gives no sample of data sources judged for fitness, and no measure of how often a given threat changes a result.
- No threshold is given for when a source counts as fit. The roadmap separates "a maturity classification that distinguishes currently credible, partially reliable, and unproven" integrative applications,[^d9] but does not say how to score one source against one question.
- The text is about clinical and regulatory data. Outside that setting the threats are named by analogy, not tested.

## Related

- [[estimand]] — the question that fitness is judged against
- [[common-support-positivity]] — a fitness failure of a specific kind: the data hold no comparison in a stratum
- [[predicted-outcome-substitution]] — a predicted value standing in for a field the source never recorded
- [[evidentiary-role-of-analysis]] — how far the conclusion from a fit or partly fit source may be read

[^d1]: arxiv-2511-19735 — "RWD is not automatically fit for causal use simply because it is large"
[^d2]: arxiv-2511-19735 — "Assess data provenance, alignment, and fitness for purpose"
[^d3]: arxiv-2511-19735 — "this is often the most consequential step"
[^d4]: arxiv-2511-19735 — "tion bias, when RWD populations differ systematically from those in RCTs"
[^d5]: arxiv-2511-19735 — "coding drift, linkage error, treatment and outcome misclassification"
[^d6]: arxiv-2511-19735 — "silently bias and invalidate causal conclusions"
[^d7]: arxiv-2511-19735 — "Some can be partially mitigated through principled design, causal inference, calibration, validation studies, or sensitivity analysis"
[^d8]: arxiv-2511-19735 — "these tools do not eliminate the need for scientific judgment"
[^d9]: arxiv-2511-19735 — "a maturity classification that distinguishes currently credible, partially reliable, and unproven"
