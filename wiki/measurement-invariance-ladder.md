---
description: "Invariance across two samples is a nested ladder (configural, metric, scalar, residual), each rung licensing a different comparison; simulated and human data pass some rungs, fail others."
aliases: ["multigroup CFA invariance", "dimensional invariance", "factorial invariance", "measurement equivalence across groups"]
sources: ["arxiv-2512-02910"]
---
# Measurement invariance ladder

Measurement invariance asks whether one instrument measures the same thing in two groups. The test is a sequence of multigroup confirmatory factor models, each adding equality constraints on the model's parameters. Each step is nested in the one before, so a failure at one rung stops the rungs above it.

Cipriani and colleagues use the ladder to compare simulated respondents with human respondents on the same scale, treating the two as the two groups. They state what each rung allows. If configural invariance holds, "the pattern of factor loadings is equal across the group."[^i1] If metric invariance holds, "it is also possible to perform a comparison of variances between latent variables."[^i2] If scalar invariance holds, "it is also possible to compare latent scale means."[^i3] Residual invariance allows "further comparisons of manifest means and analyses"[^i4] on the observed scores.

The rungs therefore gate comparisons. The lower two say whether the items relate to the factors in the same way across groups. The upper two say whether the group levels can be compared. For a simulator this split matters. A simulated sample can pass the lower rungs, meaning its loadings look like the human ones, and still fail the scalar rung, meaning its means are not on the human scale. In that case the simulated and human means cannot be compared directly, whatever the loadings say.

The rule for accepting a rung is a change-in-fit rule, not a test with a p-value. A higher rung is accepted only when the change in fit is small: "dimensional invariance is accepted only if the degree of change in CFI"[^i5] is at most .010, and "less than .010, and the ∆RMSEA is equal to or less than .015"[^i6] for the RMSEA change. The cut-offs come from Chen (2007) and were set for comparing models fitted to real samples.

The results differ by scale. In Study 1, "The configural invariance model showed a marginal but unacceptable fit"[^i7], and the "residual invariance model was outright inadmissible, as Heywood cases"[^i8], so the ladder stopped early. In Study 2 the result was "configural invariance (H2.1) and partial support for metric invariance."[^i9] In Study 3, "and scalar invariance (H2.3) were supported across real and simulated data."[^i10] The authors describe the Study 3 and 4 pattern as "Remarkably" high: "Studies 3 and 4 achieve high levels of measurement invariance between datasets."[^i11]

The authors offer an interpretation of that difference, not a finding. "One possible interpretation is that, when responding, LLMs tend to interpret scale items using a more standardized" reading, "less influenced by randomness and biases due to study conditions and population characteristics."[^i12] On this reading the simulator's item interpretation is more uniform, and so the structure transfers better. The paper does not test the reading.

The same ladder was applied inside the simulated data, across gender. There the verdict was weaker: "these results support configural and metric invariance, with limited evidence for scalar"[^i13] invariance. So the simulator is not clearly invariant across its own demographic subgroups at the scalar rung either.

## What survives the transfer

The nested logic and the comparisons each rung licenses survive the move from human groups to simulated groups. What does not survive unchanged is the premise that the two groups are draws from one population. The human samples are sampled people. The simulated group is a set of draws from one fixed model, with temperature as its only source of variation. Invariance then tests whether the instrument behaves the same in two data-generating processes, not two populations. The fit-change cut-offs do not say whether that is the same question (my inference).

## Limits

- The cut-offs are a convention from Chen (2007), applied to a comparison the convention was not built for. The paper reports fit indices but does not check that a ΔCFI of .010 means the same across real-versus-simulated groups.
- The Study 3 and 4 structures were chosen by factor analysis on simulated data, then checked on new human data. The human check is a fresh sample, but the structure was selected to fit the simulator. Whether that favours invariance is not tested here (my inference).
- The interpretation of the Study 3 and 4 results rests on a mechanism the paper does not measure.
- Only Likert-type scales and survey data were examined, so the ladder's behaviour for other response formats is not known.
- The paper reports which rungs held in each study. It does not say why the scalar rung failed in Studies 1 and 2, so it cannot say whether the failure lies in the means, the intercepts or the spread.

## Related

- [[network-measurement-invariance]] — the alternative test; [[simulated-respondent-variance-deficit]] reports that the compressed spread of simulated respondents makes the SEM scalar and strict tests hard to satisfy, which is the reason that note gives for preferring the network test
- [[simulated-respondent-structure-fidelity]] — the structure step that comes before this ladder; the same paper finds structure replicating while distributions do not
- [[nomothetic-span]] — another check on simulated respondents that asks about relations to other variables rather than about the instrument's internal structure

[^i1]: arxiv-2512-02910 — "the pattern of factor loadings is equal across the group"
[^i2]: arxiv-2512-02910 — "it is also possible to perform a comparison of variances between latent variables"
[^i3]: arxiv-2512-02910 — "it is also possible to compare latent scale means"
[^i4]: arxiv-2512-02910 — "further comparisons of manifest means and analyses"
[^i5]: arxiv-2512-02910 — "dimensional invariance is accepted only if the degree of change in CFI"
[^i6]: arxiv-2512-02910 — "less than .010, and the ∆RMSEA is equal to or less than .015"
[^i7]: arxiv-2512-02910 — "The configural invariance model showed a marginal but unacceptable fit"
[^i8]: arxiv-2512-02910 — "residual invariance model was outright inadmissible, as Heywood cases"
[^i9]: arxiv-2512-02910 — "configural invariance (H2.1) and partial support for metric invariance"
[^i10]: arxiv-2512-02910 — "and scalar invariance (H2.3) were supported across real and simulated data"
[^i11]: arxiv-2512-02910 — "Studies 3 and 4 achieve high levels of measurement invariance between datasets"
[^i12]: arxiv-2512-02910 — "One possible interpretation is that, when responding, LLMs tend to interpret scale items using a more standardized"
[^i13]: arxiv-2512-02910 — "these results support configural and metric invariance, with limited evidence for scalar"
