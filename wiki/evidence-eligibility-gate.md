---
description: "A verifier can abstain before diagnosis when the deployed agent never generated matched evidence about a component, so an unsupported unit gets no score rather than a wrong one."
aliases: ["diagnosability gate", "support gate", "evidence eligibility gate", "abstain-before-diagnosis", "two-stage diagnosability gate"]
sources: ["openalex-org-w7219155344"]
---
# Evidence eligibility gate

A diagnostic verifier can fail in a way a score cannot show. If the agent never visited a component often enough, its aggregate traces carry no information about that component, and any diagnosis built on them is a guess dressed as a result. The gate is a test on the evidence, applied before a prediction is constructed, that decides whether a diagnosis is allowed at all. Zhu and Chang state the principle: "A verifier must establish that its evidence is eligible and non-revealing before its score can support an optimizer comparison."[^c1]

The mechanism is two checks in sequence. The first is a reference-map gate on clean traffic. A component has support in a clean partition when its support count is at least 12, and a regime-component unit enters the reference map when at least 14 of 15 clean partitions have support.[^c2] The second is a runtime gate on the deployed traffic. A partition counts only when the reference stream and the current stream each have support of at least 12 in that same partition, and a unit is admitted when 14 of 15 partitions are jointly supported.[^c3] The intersection is the point: "Matched support ensures that the aggregate difference is grounded in comparable evidence."[^c4] Two totals that are each adequate can still refer to different partitions. A unit that fails either gate returns an abstention label (REFERENCE_ABSTAIN or RUNTIME_ABSTAIN) and receives no diagnostic score: "Unsupported units abstain instead of receiving a diagnostic score."[^c5]

The gate is a different object from a confidence threshold. "This is not a confidence threshold on a completed prediction" — it "is an eligibility test on the evidence from which a prediction would be constructed."[^c6] It also does not look at the planted fault: the reference gate "does not use planted fault identity and does not infer a diagnosis."[^c7] Abstention then becomes a reported outcome rather than missing data: the paper argues that reporting failure in such a case confounds "lack of capability with lack of evidence", and that a support gate makes the denominator visible and turns "not testable here" into a first-class outcome.[^c8]

The measured result in the preregistered heldout: the reference gate admitted 55 of 72 regime-component units, 54 of those 55 passed the runtime gate, and among the 20 physical components that were represented, stable false admission was zero. Zero is not a bound, and the paper's own one-sided exact 95% upper bound on the false-admission rate is 0.1391.[^c9]

## Limits

- The thresholds (support of 12 per partition, 14 of 15 partitions, a signal cutoff of z at least 1.50) were fixed by the authors. The signal cutoff was fixed before the formal run, chosen from a small grid,[^c10] but the paper does not show how sensitive coverage is to these numbers. A different threshold admits a different set of units.
- The gate is a coverage trade-off. It admits 55 of 72 units, so a quarter of the units produce no diagnosis, and the paper does not report what the uncovered units would have scored on a fully known target. The abstention is honest about what it leaves out; whether those units are the hard ones is not shown.
- The false-admission figure is an upper bound, not a rate. The paper says plainly that the zero count "does not establish that the true rate is zero," and the bound 0.1391 is wide for 20 components.
- One simulator, one policy family, three demand regimes, and one fault type. The eligibility criterion for a real deployment (what counts as "support" for a real agent's trace) is not established here.
- The gate checks whether evidence exists and is matched, not whether it is non-revealing. The non-revelation side is a separate check and is handled in [[verifier-leakage]].
- The gate is a construction I have not seen tested against a confidence-based abstention baseline on the same units. Whether an eligibility test beats a calibrated confidence threshold on the same diagnosis is my inference, untested here.

## Related

- [[pre-generation-evidence-sufficiency]] — judging whether passages contain what an answer needs, before a generator runs. The same move, deciding before producing, in a retrieval setting.
- [[abstention]] — "I don't know" as a third output. The gate here is a verifier-side abstention that fires on evidence, not on the model's own confidence.
- [[conformal-abstention]] — a post-hoc threshold on a completed prediction. The gate in this note is upstream of the prediction, which is the distinction the paper draws.
- [[eligibility-gated-grounding-score]] — an eligibility judge that disqualifies evasive responses. There the eligibility is of a response to a request; here it is of evidence to a diagnosis.
- [[verifier-leakage]] — the other half of the paper's contract: a verifier must also be non-revealing before its score counts.

[^c1]: openalex-org-w7219155344 — "A verifier must establish that its evidence is eligible and non-revealing before its score can support"
[^c2]: openalex-org-w7219155344 — "A regime-component unit enters the reference map when at least 14 of 15 clean"
[^c3]: openalex-org-w7219155344 — "14 jointly supported partitions out of 15"
[^c4]: openalex-org-w7219155344 — "Matched support ensures that the aggregate difference is"
[^c5]: openalex-org-w7219155344 — "Unsupported units abstain instead of receiving a diagnostic score."
[^c6]: openalex-org-w7219155344 — "This is not a confidence threshold on a completed prediction"
[^c7]: openalex-org-w7219155344 — "does not use planted fault identity and does not infer a diagnosis"
[^c8]: openalex-org-w7219155344 — "lack of capability with lack of evidence"
[^c10]: openalex-org-w7219155344 — "was selected before formal execution from"
[^c9]: openalex-org-w7219155344 — "produces no stable false admissions among 20 represented components"
