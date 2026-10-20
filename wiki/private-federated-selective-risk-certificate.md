---
description: "A private federated certificate bounding accepted-output loss from noised score and loss histograms, valid over all thresholds and rounds; it abstains until the bound clears the target."
aliases: ["Fed-SRC", "private federated anytime selective-risk certificate", "private federated selective risk certification"]
sources: ["doi-10-48550-arxiv-2608-07913"]
---
# Private federated selective-risk certificate

A [[abstention|selective]] risk certificate promises that the outputs a system accepts meet a declared error target, and abstains where that cannot be shown.[^c1] Fed-SRC is one such certificate for a setting where calibration data cannot be pooled. Each client scores its own examples with a bounded score, bins them by threshold, and releases only Gaussian-perturbed histograms of score counts and loss-weighted counts; no prompt, output, or per-example label leaves the client.[^c2] The server sums the released vectors into noisy cumulative accepted and error counts for each threshold, and forms a gated target-risk contrast whose mean is nonpositive exactly when accepted risk is at or below the target, given positive acceptance (see [[gated-target-risk-contrast]]).[^c3] Two martingales, one indexed by the number of records and one by the accumulated noise variance, are combined so that a single event bounds the contrast and the accepted mass together, for every registered threshold and every monitored round.[^c4]

Three pieces carry the design, and each is a separate part of the claim:

- **Predictable recruitment.** The client identity, batch size and noise scale for the next release are fixed before that release is seen. Under that condition a transcript-measurable threshold and stopping time can be chosen after looking at past certificates, and the paper states that "No additional optional-stopping or postselection correction is needed."[^c5]
- **Acceptance floor.** A certificate also needs a predeclared floor on accepted mass. "Operational certification additionally requires a predeclared floor" a_min > 0, because a contrast of zero is also what a policy that accepts nothing produces.[^c6] When nothing is accepted the method makes no risk claim and returns always-abstain (see [[crc-confident-error-control]] for the same triviality in CRC).
- **Mixture transfer.** The bound is on the realized calibration mixture. A declared deployment mixture is reached by paying a term built from weight mismatch and per-client total-variation radii. Because the contrast has range one, "It therefore pays ηt , not (1 + r⋆ )ηt."[^c7]

What the paper measured: across 500 trials per core cell the simultaneous bounds showed no violation.[^c8] Power is a different matter. The primary target r⋆ = 0.10 certified nowhere; at r⋆ = 0.20 the certificate fired on HaluEval question answering, where in the nonprivate case "it certifies in all 200 nonprivate trials with held-out risk below target," and abstained on RAGTruth.[^c9] Naive privatization, which adds noise without the accounting here, "Naively privatized non-private certificates violate their bounds in 146 to 198 of 200 trials."[^c10] The point of the construction is that validity survives the noise. The paper is explicit that it does not claim useful private power: it contributes a private federated certificate "without claiming a superior hallucination score or strong private utility on the current data."[^c19]

## Limits

- **Marginal, not conditional.** The guarantee is "marginal selective risk under a declared mixture"; it says nothing about risk for a single input or a subgroup.[^c11] A subgroup version needs pre-registered subgroup histograms and a split budget, at extra sample and communication cost.
- **Relative to the declared loss.** "Validity is relative to the declared loss."[^c12] The certificate controls expected declared loss among accepted outputs, not the truth of any response. Human disagreement, weak judge labels, or a mismatch between correctness and faithfulness can make the loss a poor proxy.
- **Thin private power.** "Operational private utility is limited at the registered targets," and "The primary target r⋆ = 0.10 certifies nowhere."[^c13] Every positive private cell consumed "roughly 20× to 78× event reuse," with "times more stream events than unique calibration items" as the cost of certifying occurrences rather than items.[^c14]
- **Privacy scope.** The privacy statement is event-level, and "the guarantee is not privacy for the 839 public support responses, nor for their contributors."[^c15] User- or source-level protection needs bounded contribution and a recalibrated accountant (see [[event-level-zcdp-histogram-release]]).
- **Drift.** The transfer radii were declared by the authors, not justified by a shift audit; "so the drift route remains a sensitivity analysis."[^c16]
- **Comparator.** The private betting heuristic in the paper is unproved, and "the paper still contains no proved private competitor."[^c17] Nonprivate betting CRC is a separate object (see [[betting-based-conformal-risk-control]]).
- **Predictability is load-bearing.** A service that peeks at an unreleased batch, retains favorable records, or lets dropout depend on unreported losses falls outside the theorem; "service that peeks at an unreleased batch, retains favorable records" is named as a violation of the assumption.[^c18] The paper's own reasoning, that a visible schedule depending on earlier private messages is safe but a schedule using hidden data leaks, is a restriction the operator must enforce, not something the certificate checks.

## Related

- [[crc-confident-error-control]] — the single-stream conformal risk control threshold this extends to federated, anytime, private release
- [[betting-based-conformal-risk-control]] — a nonprivate anytime betting alternative; the paper's betting step is an unproved private analogue
- [[conformal-abstention-floor]] — the acceptance floor question, which Fed-SRC has to pay for separately
- [[atom-stratified-federated-conformal-calibration]] — federated calibration with group-conditional sketches, without the private anytime martingale
- [[dp-stability-full-data-conformal-coverage]] — differential privacy's effect on full-data conformal coverage, a different privacy object
- [[calibration]] — the calibration problem the certificate answers for a declared mixture

[^c1]: doi-10-48550-arxiv-2608-07913 — "Selective-risk certificates promise that accepted"
[^c2]: doi-10-48550-arxiv-2608-07913 — "Clients release only Gaussian-perturbed"
[^c3]: doi-10-48550-arxiv-2608-07913 — "the gated target-risk contrast"
[^c4]: doi-10-48550-arxiv-2608-07913 — "bound target-risk contrast and accepted mass"
[^c5]: doi-10-48550-arxiv-2608-07913 — "No additional optional-stopping or postselection correction is needed"
[^c6]: doi-10-48550-arxiv-2608-07913 — "Operational certification additionally requires a predeclared floor"
[^c7]: doi-10-48550-arxiv-2608-07913 — "It therefore pays ηt , not (1 + r⋆ )ηt"
[^c8]: doi-10-48550-arxiv-2608-07913 — "the simultaneous bounds show no violation"
[^c9]: doi-10-48550-arxiv-2608-07913 — "it certifies in all 200 nonprivate trials with held-out risk below target"
[^c10]: doi-10-48550-arxiv-2608-07913 — "Naively privatized non-private certificates violate their bounds in 146 to 198 of 200 trials."
[^c11]: doi-10-48550-arxiv-2608-07913 — "The guarantee is marginal selective risk under a declared mixture"
[^c12]: doi-10-48550-arxiv-2608-07913 — "Validity is relative to the declared loss"
[^c13]: doi-10-48550-arxiv-2608-07913 — "The primary target r⋆ = 0.10 certifies nowhere"
[^c14]: doi-10-48550-arxiv-2608-07913 — "times more stream events than unique calibration items"
[^c15]: doi-10-48550-arxiv-2608-07913 — "the guarantee is not privacy for the 839 public support responses, nor for their contributors"
[^c16]: doi-10-48550-arxiv-2608-07913 — "so the drift route remains a sensitivity analysis"
[^c17]: doi-10-48550-arxiv-2608-07913 — "the paper still contains no proved private competitor"
[^c18]: doi-10-48550-arxiv-2608-07913 — "service that peeks at an unreleased batch, retains favorable records"
[^c19]: doi-10-48550-arxiv-2608-07913 — "claiming a superior hallucination score or strong private utility on the current data"
