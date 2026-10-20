---
description: "Replicability, reproducibility and robustness are three different tests of a finding: a new sample, the same data re-analysed the same way, and the same data under a different analysis."
aliases: ["replication", "same question, new data", "replication success"]
sources: ["doi-10-1523-eneuro-0017-22-2022"]
---
# Replicability

Replicability is "the degree to which a previous scientific finding can be repeated in a distinct set of data."[^p1] The commentary separates it from two neighbouring words, using definitions it borrows from a review by Nosek et al. (2021).[^p2] Replicability is "the ability to answer the same question with new data and obtain similar results compatible with prior studies." Reproducibility is "the ability to answer the same question with the same data" using the same analysis strategy and getting the same result.[^p3] Robustness is the same data with "a different analysis strategy" that still gives "the same result."[^p4]

The three words name three different ways a finding can be fragile. My inference: a failed reproduction points at the code, the reporting or the data handling, since nothing about the question has changed. A failed robustness check points at the analysis: the same data support the claim only under one set of choices. A failed replicability check can mean the original result was a sampling accident, or that the new study differs in a way that matters. The commentary's own neuroimaging example is a robustness case: 70 teams tested nine hypotheses on one fMRI dataset, and "no two teams used the same workflow to analyze the data," which gave "highly varied results."[^p5] The text reads this as evidence that "analytical flexibility could strongly impair replication success" in neuroimaging.[^p6]

Keeping the three apart changes what a failure means. A reader who sees "not replicated" needs to know which of the three was tested before deciding whether the original analysis was wrong, the original sample was unlucky, or the new study was different. The commentary uses replicability in its own sense throughout: "this commentary primarily deals with 'replicability,' as opposed to 'reproducibility' or 'robustness.'"[^p7]

The measured rates in the text are for replicability in this sense, across fields. In the cancer-biology replications it cites (Errington et al., 2021), "43% of replication effects were both statistically significant and in the same direction as the original" for original positive effects, and "replications of positive effects had effect sizes smaller than the originals."[^p8][^p9] The text's summary across the projects is that replication effects are roughly half the originals, and about half of them show "statistical significance in the same direction as original studies."[^p11]

## Limits

- The three-part split is a convention, borrowed from one review. Other fields use "replication" for what this text calls reproduction, and the text does not settle the terminology across them.
- The split says where a failure lies; it does not say how often each kind occurs. The text gives replication rates but no rates for reproducibility or robustness failures in neuroscience.
- Success criteria are not fixed. The text reports "same direction and significant," "smaller effect," and "similar results," which are different thresholds. My inference: what counts as a replication success depends on which threshold is chosen, and the rates above depend on it too.
- The rates are from psychology, cancer biology and social science. The text says: "Since there are no completed large-scale replication projects focused on neuroscience, one can only guess what the results would be."[^p10]

## Related

- [[evaluation-questionable-research-practices]] — the analytic flexibility that makes robustness fail, catalogued for ML evaluation
- [[registered-reports]] — the format argued to raise replicability by fixing the analysis before results are known
- [[minimum-detectable-effect]] — whether a new sample is large enough to detect the original effect at all
- [[distributional-reproducibility-vs-bitwise-determinism]] — a different sense of "reproducible": whether a rerun gives the same output

[^p1]: doi-10-1523-eneuro-0017-22-2022 — "the degree to which a previous scientific finding can be repeated in a distinct set of data"
[^p2]: doi-10-1523-eneuro-0017-22-2022 — "the definitions of which are"
[^p3]: doi-10-1523-eneuro-0017-22-2022 — "ability to answer the same question with the same data"
[^p4]: doi-10-1523-eneuro-0017-22-2022 — "analysis strategy and achieve the same result"
[^p5]: doi-10-1523-eneuro-0017-22-2022 — "no two teams used the same workflow to analyze the data"
[^p6]: doi-10-1523-eneuro-0017-22-2022 — "could strongly impair replication success"
[^p7]: doi-10-1523-eneuro-0017-22-2022 — "this commentary primarily deals with"
[^p8]: doi-10-1523-eneuro-0017-22-2022 — "43% of replication effects were both statistically significant and in the same direction as the original"
[^p9]: doi-10-1523-eneuro-0017-22-2022 — "replications of positive effects had effect sizes smaller than the originals"
[^p10]: doi-10-1523-eneuro-0017-22-2022 — "Since there are no completed large-scale replication projects focused on neuroscience"
[^p11]: doi-10-1523-eneuro-0017-22-2022 — "statistical significance in the same direction as original studies"
