---
description: "A two-gate execution rule for an edge diagnostic agent that acts only when both its causal-hypothesis posterior and its predicted-effect free energy pass independent thresholds, else escalates."
aliases: ["AURORA", "dual-gated execution mechanism", "dual-gated active inference", "Posterior Certainty Gate", "VFE Safety Gate"]
sources: ["silva-2026"]
---
# AURORA dual-gated execution mechanism

> An edge agent diagnosing a fault does not act on "the posterior favours
> cause C" alone: it also checks whether its own generative model's
> predicted effect of intervening on C is consistent with what it just
> observed, and only acts when both checks pass — otherwise it abstains
> and hands the case up a tier.

## Definition / Mechanism

De Silva et al. (2026) present AURORA, a micro-agent for
grey-failure diagnosis in the computing continuum that ranks candidate
root causes by a causal interventional-contrast score and, before acting
on the top-ranked cause, runs it through two independent safety gates
rather than one. "Gate 1 verifies that the diagnosis is sufficiently
confident, while Gate 2 verifies that the predicted intervention remains
consistent with the current observations... Either failure mode alone is
sufficient to trigger a destructive intervention: a concentrated but
incorrect posterior may bypass Gate 1, while an inconsistent generative
model may bypass Gate 2. Therefore, both gates must pass for execution to
proceed."[^c1]

Gate 1, the Posterior Certainty Gate, enforces $P_{max} \geq \tau$ on the
top candidate cause's posterior probability: "When the maximum posterior
falls below this threshold, the posterior mass is spread across multiple
root-cause hypotheses, indicating that the agent cannot reliably
distinguish which fault class it is observing... Gate 1 treats diagnostic
[[efe-planning-as-variational-inference|ambiguity]] as a sufficient reason for [[abstention]]." Gate 2, the VFE Safety
Gate, addresses "a confident diagnosis whose predicted effects under
action are inconsistent with the observed telemetry" by thresholding
variational free energy.[^c2]

If either gate fails, "the micro-agent abstains from local remediation and
forwards the case for deeper analysis" to a fog-tier node, rather than
guessing or always calling up the tier.[^c3]

Across a 10,002-trial Monte Carlo evaluation, AURORA "eliminated all
destructive actions... validating the efficacy of the dual-gated execution
mechanism," with a 65.9% abstention rate and 62.0% repair accuracy; of the
abstentions, "the Posterior Certainty Gate fires on 4,433 trials (44.3%)
and the VFE Safety Gate fires on 2,158 trials (21.6%)... Both gates are
operationally active under the studied fault distribution. The dual-gated
mechanism is therefore not redundant."[^c4]

## Why it matters

Most escalation mechanisms this wiki carries key the decide-or-defer call
to one scalar — a confidence score, a posterior threshold, a learned
competence estimate. AURORA's contribution is that it measures **two
independent failure modes of "should I act"** — is the diagnosis
unambiguous, and does the generative model's own prediction of the
intervention's effect still match reality — and shows empirically that
both fire on disjoint trial subsets, so collapsing them into one gate
would miss cases the other catches.

## Limits

The claim rests on a single 2026 arXiv preprint, not yet peer-reviewed
`[?]`; the causal graph is "pre-specified from domain knowledge and held
fixed across trials," not learned, so the gates are validated on a
diagnostic model whose structure is assumed correct, not discovered.
Evaluation is synthetic Monte Carlo fault injection (three fault classes:
network drop, CPU spike, memory leak) on one simulated edge/fog/cloud
testbed, not a physical deployment; the abstention rate (65.9%) trades
resolution rate for the zero-destructive-action guarantee, a
precision/coverage tradeoff whose generality outside these three fault
classes is untested.

## Related

[[bayesian-self-escalation]] · [[informed-abstention-framework]] · [[detect-verify-escalate-pipeline]] · [[clinician-veto]] · [[value-of-information]]

[^c1]: silva-2026
[^c2]: silva-2026
[^c3]: silva-2026 — "the micro-agent abstains from local remediation and forwards the case for deeper analysis"
[^c4]: silva-2026 — "AURORA successfully eliminated all destructive actions across the entire 10,002-trial subset, validating the efficacy of the dual-gated execution mechanism."
