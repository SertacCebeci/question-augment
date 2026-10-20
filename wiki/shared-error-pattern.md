---
description: "Judge banks with the same average error correlation can fail in two shapes: errors shared by most judges, or errors packed into a subgroup. The shapes call for different consensus rules."
aliases: ["global co-failure", "vulnerable-subgroup failure", "shape of shared judge errors", "error-pattern structure"]
sources: ["doi-10-48550-arxiv-2609-22512"]
---
# Shared error pattern

A panel's votes are worth fewer independent judgments the more its errors move together, and the average pairwise error correlation is the usual scalar for that loss (see [[effective-independent-votes]]). The work this note draws on argues that the scalar hides the shape of the shared part, and that the shape decides which consensus rule is safe. "Measuring the overall amount of correlation alone is therefore insufficient."[^c1]

Two shapes are named. In *global co-failure*, many judges err on the same items, and the measured correlation rises.[^c2] In *vulnerable-subgroup failure*, errors are concentrated among a smaller group of judges. "In this case, measured correlation can decrease even as majority decisions" become less reliable.[^c3] The second shape is the one where a single average misleads in the direction that matters: the number looks calmer while the majority is failing. "Thus, the pattern of shared errors matters, not only their overall correlation."[^c4]

The mechanism is the attribution of agreement. An agreement counts as evidence only in the part that is not shared, so a correction has to know which judges share the error. Under global co-failure the redundancy is spread across the agreeing majority. Under subgroup failure the majority's apparent strength is partly one bloc that is wrong together, and the usable signal is the support from judges outside that bloc. The two corrections point in different directions, which is why the paper reports that "No single fixed rule we test works best in both cases."[^c5] The direction of each correction is my inference from that result; the paper states only that the two differ.

How the shape is read: the work estimates the correlation from a trusted calibration set, forming an error indicator for each judge (its vote against a trusted label) and correlating those indicators across items.[^c6] A label-free statistic over the votes can then assign a batch to a regime. The regime router "identifies the correct error pattern with 85% accuracy when each test batch contains a single pattern." Recognizing the pattern is not choosing the rule, though: "Recognizing the error pattern does not identify the best rule."[^c7] So the shape is a diagnostic input, and the step from shape to rule is a separate and weaker one. The paper names that step "The main limitation is the mapping from regime to filter."[^c8]

## Limits

- The two shapes were produced by controlled perturbations. "The global co-failure and vulnerable-subgroup experiments use controlled perturbations." The design "does not establish how frequently either" shape occurs in natural deployments, and "Real errors may combine several sources of dependence."[^c9]
- Only one subgroup vulnerability was tested in depth: "position bias is the only shared vulnerability" evaluated.[^c10]
- Choosing a rule needs labels: the adaptive filters and the selector "require about 100 trusted labels," so the diagnostic is not free of ground truth.[^c11]
- The judge banks are small (ten open-weight judges, or three to six frontier judges) and the datasets are a few preference and factuality sets. The shape result has not been measured on a panel of a different kind.[^c12]

## Related

- [[effective-independent-votes]] — the same effective-sample arithmetic applied to vote agreement; this note is about what that single number hides.
- [[common-mode-judge-error]] — the anchored-estimator version of the same split: a residual shared uniformly looks like quality, one shared by model family can be blocked out.
- [[coincident-failure]] — independently built sources that fail together, the older form of the shared-error problem.
- [[accuracy-error-correlation-coupling]] — in frontier banks the level of correlation rises with accuracy; this note asks what shape that correlation takes.

[^c1]: doi-10-48550-arxiv-2609-22512 — "Measuring the overall amount of correlation alone is therefore"
[^c2]: doi-10-48550-arxiv-2609-22512 — "make the same mistake on the same examples, which we call global co-failure, measured correlation"
[^c3]: doi-10-48550-arxiv-2609-22512 — "In this case, measured correlation can decrease even as majority decisions"
[^c4]: doi-10-48550-arxiv-2609-22512 — "Thus, the pattern of shared errors matters, not only their overall correlation."
[^c5]: doi-10-48550-arxiv-2609-22512 — "No single fixed rule we test works best in both cases"
[^c6]: doi-10-48550-arxiv-2609-22512
[^c7]: doi-10-48550-arxiv-2609-22512 — "Recognizing the error pattern does not identify the best rule."
[^c8]: doi-10-48550-arxiv-2609-22512 — "The main limitation is the mapping from regime to filter."
[^c9]: doi-10-48550-arxiv-2609-22512 — "it does not establish how frequently either"
[^c10]: doi-10-48550-arxiv-2609-22512 — "position bias is the only shared vulnerability"
[^c11]: doi-10-48550-arxiv-2609-22512 — "adaptive filters and the selector require about 100 trusted labels"
[^c12]: doi-10-48550-arxiv-2609-22512
