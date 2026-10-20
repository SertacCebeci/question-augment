---
description: "Misleading ML evaluation reduces to three tricks, contamination, cherrypicking and misreporting, each a way a reported score stops answering the question it is read as answering."
aliases: ["QRPs in machine learning", "researcher degrees of freedom in ML evaluation", "over-hyping", "meta-contamination"]
sources: ["doi-10-48550-arxiv-2407-12220", "doi-10-1523-eneuro-0017-22-2022"]
---
# Evaluation questionable research practices

Imported from psychology, "questionable research practice" names behaviour short of fraud that inflates a reported result. The source taxonomy sorts most ways to mislead others, or delude yourself, in ML evaluation into three tricks: contamination, cherrypicking and misreporting, plus a weaker class of "amplifiers" that enable the others.[^c1]

## The three tricks

**Contamination (leakage)** is any influence of test-set information on model development, from reusing hyperparameters to training on the test set. It can invalidate a benchmark score if the score is read as evidence of general capability on the task.[^c2] With web-scale corpora the prior probability of contamination is very high, so countermeasures such as canary strings or exact label matches are needed before readers can trust a result.[^c3] New versions of existing benchmarks generally show substantial performance drops, which is the signature of earlier contamination.[^c4]

**Cherrypicking** is choosing among runs and configurations to make a system look good or relatively good: weak competitors, undertuned strong competitors, or more optimisation of one's own prompt or inference parameters.[^c5] The question being answered ("is method A better than B?") silently changes into "is A, tuned harder, better than B?". The source requires a shared experimental setting, including equal optimisation effort, to hold the comparison constant.[^c6]

**Misreporting** is any error or misleading presentation of the model's specification or results: point estimates only, understated model size, credit given to inert modules, or claims of general task performance without external validity.[^c7]

## Contamination is a gradient, not a binary

- *Over-hyping*: tuning on the test set, then re-testing with another metric. The test score becomes a training signal and unreported multiple comparisons accumulate; this biases results even when each iteration uses cross-validation correctly.[^c8]
- *Meta-contamination*: when a whole field reuses one test set, successors are designed from a summary statistic of it, so the multi-team process is effectively training on the test set. Recht et al. found error on fresh near-identical test sets 4-15% higher; Arora and Zhang bound the ImageNet meta-overfitting error below 7-10%.[^c9]

Because the same test set is touched by many hands, the question "was this benchmark leaked?" has no answer at the level of one model; it applies to lineages of work. This is my reading, not the source's claim.

The psychology origin has measurements that the ML catalogue does not carry. A survey of 2155 psychologists asked about ten practices, and self-admission rates ran from 0.6% to 63.4%, with prevalence estimates higher than self-admission for all but one practice.[^c10] Ellis reads the cause as incentive rather than individual character: academic research incentivizes these practices, because high-impact journals publish positive results and treat null findings as failures.[^c11] For neuroscience no such survey is cited: "While there are no published surveys of neuroscientists" on engagement, and the text argues only that "the same incentive structures described are arguably inherent to neuroscience."[^c12][^c13] An ML evaluation note can borrow the incentive account, but not a prevalence figure from psychology.

## Limits

The paper is a catalogue and argument, not a measurement of how common each practice is; it notes a dearth of concrete examples in the ML literature. The three-way split is a classification chosen by the authors, not a proven partition, and many practices belong to several classes. The psychology lens (researcher degrees of freedom) transfers the idea of undisclosed analytic choice; it does not transfer psychology's remedies one-for-one, since ML contamination is often accidental and invisible because the training data are unknown. Only a few of the numbered practices were read here (3.1.1, 3.1.8, 3.1.9); the cherrypicking and misreporting subsections were taken from the summary section.

## Related

- [[benchmark-contamination-convergent-audit]] — measures contamination with three probes; this note supplies the broader taxonomy of how it arises
- [[reasoning-contamination-of-verbalized-confidence]] — a different contamination, of confidence reports, not of test data
- [[contamination-robust-selective-calibration]] — designing evaluation to survive contamination
- [[registered-reports]] — the psychology remedy that changes the publication payoff for the practices, rather than detecting them after the fact

[^c1]: doi-10-48550-arxiv-2407-12220 — "Most ways to mislead others, or delude yourself, in ML evaluation fall into one of the"
[^c2]: doi-10-48550-arxiv-2407-12220 — "Contamination can totally invalidate a reported benchmark score"
[^c3]: doi-10-48550-arxiv-2407-12220 — "We thus need to account for the very high prior probability of contamination in web corpuses"
[^c4]: doi-10-48550-arxiv-2407-12220 — "new versions of existing benchmarks, which generally exhibit substantial"
[^c5]: doi-10-48550-arxiv-2407-12220 — "Choosing among runs and configurations to make your system look"
[^c6]: doi-10-48550-arxiv-2407-12220 — "shared experimental setting as an assignment of values to all variables that the evaluation"
[^c7]: doi-10-48550-arxiv-2407-12220 — "any error or misleading presentation of the model’s specification or"
[^c8]: doi-10-48550-arxiv-2407-12220 — "it biases results even if every iteration of the cycle uses cross-validation properly"
[^c9]: doi-10-48550-arxiv-2407-12220 — "this multi-team process is effectively training on the test set"
[^c10]: doi-10-1523-eneuro-0017-22-2022 — "rates ranging from 0.6% to 63.4%"
[^c11]: doi-10-1523-eneuro-0017-22-2022 — "academic research incentivizes them to"
[^c12]: doi-10-1523-eneuro-0017-22-2022 — "While there are no published surveys of neuroscientists"
[^c13]: doi-10-1523-eneuro-0017-22-2022 — "the same incentive structures described are arguably inherent to neuroscience"
