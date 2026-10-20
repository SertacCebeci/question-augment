---
description: "A benchmark metric scoring, with partial credit, whether an LLM halts and asks or refuses instead of continuing along an executable but evidence-unsupported analysis path."
aliases: ["MRS", "Mean Reliability Score"]
sources: ["shi-2026"]
---
# Mean Reliability Score (MRS)

> Before an agent can pick which axis of a structured-data task to act on
> next, it must first recognise that no axis is answerable at all — MRS
> scores exactly that recognition, with partial credit for a model that
> notices trouble but answers anyway.

## Definition / Mechanism

Shi et al. (2026) build TrustDABench from 2,340
human-verified perturbed instances over 19 controlled operators, "covering
missing evidence, evidence conflicts, representation changes, and
redundant information."[^c1]

On the [[calibration|reliability]] split — tasks made unanswerable by construction — an
LLM judge assigns each response one of three scores against a gold
reason: full refusal (1), partial refusal (0.5, the model notices
insufficiency, [[efe-planning-as-variational-inference|ambiguity]] or conflict but still answers), or no refusal
(0). A full-refusal response, in the paper's own wording, "requests
necessary clarification, gives a reason consistent with the gold reason,
and does not provide a concrete" answer.[^c2]

MRS is the mean of these per-instance scores across the unanswerable set.
The paper states that it "measures evidence-grounded [[abstention]] on
unanswerable tasks while allowing partial credit for responses that
detect" the issue without properly stopping.[^c3]

## Why it matters

MRS is a stall-2 gate measurement: before an agentic LLM chooses which
data-evidence axis to act on next, it must first decide whether any valid
evidence-supported axis exists to select at all. Across eight evaluated
models the ceiling is low: "the best reliability result is only 24.21%
average MRS," achieved by GPT-5.5.[^c4]

The metric also separates *why* recognition fails. Conflicting evidence is
far harder to flag than an explicitly missing input — conflict-based
operators achieve "0.46% MRS, compared with 16.49% for
information-deletion operators, indicating that models more readily
notice" an absence than an inconsistency.[^c5]

This asymmetry is itself a finding about what triggers a clarification
decision: an *absent* axis is detectable, a *contradictory* one is not.

## Limits

The judge that assigns full/partial/no-refusal labels is itself an LLM
graded against a gold reason, not a human rater on every instance, so MRS
inherits that judge's own error rate on borderline refusals. The
unanswerable instances are constructed by the paper's own 19 perturbation
operators over two existing QA datasets (AIDABench-QA, DABench), so the
24.21% ceiling and the conflict/missing-input gap describe this
construction's difficulty distribution, not a general rate of
evidence-grounded refusal across all structured-data tasks.

## Related

[[missing-input-clarification-gate]] · [[clarification-benchmarks]] · [[clarification-request]]

[^c1]: shi-2026 — "covering missing evidence, evidence conflicts, representation changes, and redundant information."
[^c2]: shi-2026 — "to answer or requests necessary clarification, gives a reason consistent with the gold reason, and does not provide a concrete"
[^c3]: shi-2026 — "measures evidence-grounded abstention on unanswerable tasks while allowing partial credit for responses that detect"
[^c4]: shi-2026 — "the best reliability result is only 24.21% average MRS,"
[^c5]: shi-2026 — "0.46% MRS, compared with 16.49% for informationdeletion operators, indicating that models more readily notice"
