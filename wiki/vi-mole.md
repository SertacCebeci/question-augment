---
description: "A certified value-of-information allocator that spends budget on the largest certified marginal risk drop per cost, then answers or abstains by a risk certificate."
aliases: ["VI-MoLE", "Value-of-Information Mixture of LoRA Experts"]
sources: ["saliencro-2026"]
---
# VI-MoLE

> Two routing decisions can look identical by [[entropy]] alone — one has an
> unqueried expert with complementary evidence, the other has already-agreeing
> experts that will not move — and only pricing the *next acquisition's*
> certified risk drop, not the current uncertainty, tells them apart.

## Definition / Mechanism

Saliencro et al. (2026) target a mixture of LoRA experts where dynamic
routers had been activating more experts whenever the router or prediction is
uncertain: "This rule silently equates uncertainty with useful additional
computation: an uncertain example may contain complementary, unqueried expert
evidence, but it may instead remain ambiguous after every expert agrees."[^c1]

VI-MoLE replaces the uncertainty gate with counterfactual value: "VI-MoLE
learns the counterfactual risk remaining after each expert prefix, converts
these predictions into simultaneous upper-risk certificates on held-out
[[calibration]] data, and spends a global adapter budget on the token–layer
action with the largest certified marginal risk reduction per unit cost."[^c2]

Allocation is greedy under a shared budget, not per-site thresholds: "Routing
is then a global discrete resource-allocation problem: repeatedly acquire the
action with the largest certified risk reduction per profiled unit cost until
the budget is exhausted or every gain is nonpositive."[^c3]

A separate terminal step then commits to an output or refuses one: "A
terminal certificate then decides whether to answer or abstain... The
terminal certificate answers only when the remaining risk is acceptable;
otherwise it abstains."[^c4]

The paper proves three properties of this allocator: "simultaneous
certificate validity, optimal greedy allocation under diminishing certified
gains, and allocation regret under value-estimation error."[^c5]

## Why it matters

On stall 2, it gives a selection rule that is not "acquire where entropy is
highest" but "acquire where the *certified drop in a calibrated risk bound*
per unit cost is highest" — the same critique [[value-of-information]] makes
of raw [[mutual-information|entropy-based]] selection, instantiated with a
finite-sample guarantee instead of an [[expected-utility]] argument. On stall 7,
the stopping rule is not a fixed count or a single threshold crossing but
"budget exhausted or every gain is nonpositive" — a budget-and-diminishing-
gains analogue of [[sprt|sequential testing]]. On stall 10, the terminal
certificate is a calibrated answer/abstain decision at a declared risk level
$\alpha$, the same shape as the [[abstention|reject option]] but built from a certificate
that must already be simultaneously valid across every candidate action
considered during allocation, not just the one taken.

## Transfer

| | |
|---|---|
| **In its home field** | Parameter-efficient mixture-of-experts routing: a frozen [[backbone-of-a-formula|backbone]], a fixed pool of low-rank adapters, a profiled FLOP/latency cost per adapter, and offline calibration data with task labels |
| **Here** | Choosing which axis of $W$ to query next under a compute or interaction budget, and when to answer instead of asking again |
| **What survives** | Pricing the *next acquisition* by its certified marginal value per cost rather than by current uncertainty; stopping when the best remaining certified gain is zero; separating the acquisition decision from the answer/abstain decision |
| **What does not** | The mechanism needs a labelled calibration split, an exchangeable test distribution, and a risk function computable from ground truth — none of which exist for an open-ended natural-language question; the paper reports only internal MoE-routing benchmarks, not question-asking tasks |

[^c6]

## Limits

- The greedy allocation's optimality (their Proposition 1) needs equal
  acquisition costs, nonnegative chain-wise diminishing marginal gains, and
  exact certificates; the paper states this assumption is "testable rather
  than structural" and reports its violation rate rather than assuming it
  holds.[^c7]
- The terminal certificate's validity depends on the simultaneous prefix-risk
  certificate (a separate result, see
  [[simultaneous-prefix-risk-certificate]]) holding, which itself requires
  calibration and test examples to be exchangeable; the paper notes the
  certificate "can fail under shift."[^c8]
- Evaluated only on internal LoRA-expert acquisition inside one model (BoolQ,
  PIQA, and similar commonsense/transfer benchmarks), not on questions put to
  an external answerer; the transfer to interactive asking above is this
  wiki's reading, not the paper's claim.

## Related

[[value-of-information]] · [[abstention]] · [[adaptive-submodularity]] · [[simultaneous-prefix-risk-certificate]] · [[sprt]]

[^c1]: saliencro-2026 — "This rule silently equates uncertainty with useful additional computation: an uncertain example may contain complementary, unqueried expert evidence, but it may instead remain ambiguous after every expert agrees."
[^c2]: saliencro-2026 — "VI-MoLE learns the counterfactual risk remaining after each expert prefix, converts these predictions into simultaneous upper-risk certificates on held-out calibration data, and spends a global adapter budget on the token–layer action with the largest certified marginal risk reduction per unit cost."
[^c3]: saliencro-2026 — "Routing is then a global discrete resource-allocation problem: repeatedly acquire the action with the largest certified risk reduction per profiled unit cost until the budget is exhausted or every gain is nonpositive."
[^c4]: saliencro-2026 — "A terminal certificate then decides whether to answer or abstain."
[^c5]: saliencro-2026 — "We prove simultaneous certificate validity, optimal greedy allocation under diminishing certified gains, and allocation regret under value-estimation error."
[^c6]: saliencro-2026 — "The diminishing-gain assumption is testable rather than structural: complementary experts may make a later gain larger."
[^c7]: saliencro-2026 — "With equal acquisition costs, nonnegative chain-wise diminishing gains, and exact certificates, Algorithm 1 minimizes the certified residual risk over all nested-prefix allocations with the same integer budget."
[^c8]: saliencro-2026 — "Likewise, the certificate can fail under shift; coverage, certificate width, accepted calibration count, and shifted-domain violations are mandatory outputs rather than hidden caveats."
