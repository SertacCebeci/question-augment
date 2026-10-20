---
description: "A reference set used to anchor an LLM-judge panel can share the judges' error; under a single-factor model its contamination correlation can be estimated, not assumed zero."
aliases: ["clean-anchor assumption", "anchor contamination correlation", "reference-set contamination", "anchor-judge error correlation"]
sources: ["doi-10-48550-arxiv-2609-08826"]
---
# Anchor contamination

An external reference set (an anchor) is often used to split a judge panel's error into two parts: a quality signal, and a shared error common to all judges. The standard decomposition treats the anchor as a yardstick free of that shared error. It assumes the anchor is uncontaminated, "its error uncorrelated with the judges’ shared error."[^c1] The paper's warning is that when the anchor's builders share the judges' biases, the decomposition is wrong and nothing in the usual analysis reports it: "the decomposition is silently wrong, with no check."[^c2]

The mechanism. Write each judge as Jj = t + c + ej, where t is quality and c is a common-mode factor, and each anchor as Ak = t + βk c + uk. The contamination correlation is ρk = βk/(σak σc), where σak is anchor k's total error standard deviation. ρk = 0 is the clean anchor. Under this single-common-factor model, the covariances among ≥ 2 judges and ≥ 2 anchors determine the quality variance, the common-mode variance, and each ρk in closed form. The paper states that "No clean-anchor and no anchor-difference assumption is required," and that with fewer than two judges "the quantity K is undefined and the parameters are not identified."[^c3] The paper says that "identification is supplied by the ≥ 2-judge panel."[^c12] (My inference, not stated in the paper: the anchor pair supplies the contrast that separates contamination from quality, and the judges supply the shared-error moment.)

The failure boundary is exact. The denominator of the closed form factors as (σc² − β1)(σc² − β2)/σc², so identification through an anchor pair fails exactly at βk = σc² (measure zero).[^c4] The practically relevant failure is the neighbourhood around it: "In a positive-measure neighbourhood the estimator is weakly identified and its variance grows." In the paper's Table 1, at ρ1 = 0.99 the standard deviation of the estimate grows fifteen-fold (0.955 ± 0.061) while point estimates stay near the truth at ρ1 = 0.90 to 0.98.[^c5]

A second, less obvious failure concerns the usual shortcut. A designated clean-anchor estimator, which trusts one anchor, "reports a contaminated companion anchor as fully clean once its trusted anchor is itself contaminated."[^c6] Choosing which anchor to trust is itself a claim about contamination. The pair-based closed form does not need that claim, which is the paper's stated advantage.

Identifiability is not the novelty. The paper places the model inside multitrait–multimethod common-method-factor models: "identifiability is not new; the closed form, the exact boundary, the violation taxonomy, and the calibrated battery for the LLM-judge setting are the contribution."[^c7] What a reader gets from this note is the form of the failure: a reference that shares the judges' common mode looks like a clean anchor unless the pair-based contrast is available and the boundary is checked.

## Limits

- The single-common-factor model carries the whole result, and the paper says it is itself untestable: the estimator "ships gated behind a calibrated diagnostic battery." The battery tests violations, and the paper says passing it is necessary, not sufficient. "Not established: that real LLM-judge and human-anchor errors follow Assumption 1" is the paper's own disclaimer.[^c8]
- No real panel has passed the adequacy pre-test so far. On the real human panel tested (three raters, N = 431) "the test fires,"[^c14] and the raw six-provider LLM panel "fails the pre-test."[^c15] The paper says "the estimator has not been validly applied to a real panel."[^c9] The estimator was checked in simulation and, on real LLM judges, only with synthetic anchors and oracle loading calibration. A robustness observation, not a clean-model validation.
- Small contamination is hard to see at realistic size. In the synthetic real-judge run at N = 499, "a moderately contaminated anchor is not statistically distinguishable from a clean one," because its interval covers zero.[^c10] The paper also reports that "Near ρ = 0 the mixed-scale estimator carries a finite-sample upward bias at small N."[^c13]
- Ordinal scores change what is identifiable at all: "with all variables ordinal, ρk is not identified at any number of anchors." With ordinal judges and ≥ 3 continuous anchors it is identified, with a working estimator.[^c11] This restriction is not a finite-sample issue; it does not go away with more anchors.
- A panel-wide shared cause, such as one prompt template behind every judge and the anchor's builders, is outside the closed form's reach. The note on [[common-mode-judge-error]] gives the detail.
- I have not checked the paper's numbers beyond the slices quoted here, and the paper's own real-data run is one panel.

## Related

- [[common-mode-judge-error]] — the judges' own shared residual, which the same closed form either credits as quality or misattributes; the judge-side half of this note.
- [[effective-independent-votes]] — also measures how much a judge panel's votes co-vary (an ICC), with no reference set; this note asks what the co-variation is made of when an anchor is present.
- [[rater-effects-latent-score-model]] — latent rater strictness and reliability parameters; the question here is whether the reference is itself one of the raters.
- [[llm-judge-validation-gap]] — many judges are never validated against humans; anchor contamination is one way a validating reference can carry the same error as the judges (my inference, not tested by the paper).

[^c1]: doi-10-48550-arxiv-2609-08826 — "standard practice assumes the anchor is uncontaminated: its error uncorrelated with the judges’ shared error."
[^c2]: doi-10-48550-arxiv-2609-08826 — "If the anchor’s builders share the judges’ biases, the decomposition is silently wrong, with no check."
[^c3]: doi-10-48550-arxiv-2609-08826 — "No clean-anchor and no anchor-difference assumption is required"
[^c4]: doi-10-48550-arxiv-2609-08826 — "identification through this anchor pair fails exactly at βk = σc2 (measure zero)"
[^c5]: doi-10-48550-arxiv-2609-08826 — "In a positive-measure neighbourhood the estimator is weakly identified and its variance grows"
[^c6]: doi-10-48550-arxiv-2609-08826 — "reports a contaminated companion anchor as fully clean once its trusted anchor is itself contaminated."
[^c7]: doi-10-48550-arxiv-2609-08826 — "identifiability is not new; the closed form, the exact boundary, the violation taxonomy, and the calibrated battery for the LLM-judge setting are the contribution."
[^c8]: doi-10-48550-arxiv-2609-08826 — "Not established: that real LLM-judge and human-anchor errors follow Assumption 1"
[^c9]: doi-10-48550-arxiv-2609-08826 — "the estimator has not been validly applied to a real panel"
[^c10]: doi-10-48550-arxiv-2609-08826 — "so at this N a moderately contaminated anchor is not statistically distinguishable from"
[^c11]: doi-10-48550-arxiv-2609-08826 — "with all variables ordinal, ρk is not identified at any number of anchors"
[^c12]: doi-10-48550-arxiv-2609-08826 — "identification is supplied by the ≥ 2-judge panel"
[^c13]: doi-10-48550-arxiv-2609-08826 — "Near ρ = 0 the mixed-scale estimator carries a finite-sample upward bias at small N"
[^c14]: doi-10-48550-arxiv-2609-08826 — "the test fires"
[^c15]: doi-10-48550-arxiv-2609-08826 — "fails the pre-test"
