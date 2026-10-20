---
description: "Proves which of four nested controller classes (fixed, partition-router, instance-level, prior-gated) is supported for an LLM's answer/retrieve/defer/abstain decision, via a Bernstein-tight bound."
aliases: ["regime theory of controller class selection", "controller class selection theory", "nested policy lattice"]
sources: ["jiang-2026-regime"]
---
# Controller class regime theory

> Which action-decision rule to deploy — a constant policy, a coarse
> partition, a per-input learned rule, or a side-information gate — is
> itself a data-estimable choice, not a default toward "more expressive."

## Definition / Mechanism

Jiang et al. (2026) organize the controllers that
decide, per input, whether an LLM/VLM system should answer directly,
retrieve, defer to a stronger model, or abstain, into "a nested lattice of
four classes: fixed actions, partition routers, instance-level controllers,
and prior-gated controllers, ordered by complexity" — $\Pi_0 \subset \Pi_1
\subset \Pi_2 \subset \Pi_3$, where $\Pi_3$ pairs a deterministic
label-free prediction-time gate with a fallback controller from any lower
class.[^c1]

Population-optimal risk is monotone in the lattice, but finite-sample risk
is not: "the winning controller class changes with the statistical regime
of the benchmark," so that on some benchmarks "a coarser class can be the
statistically justified choice even when a finer per-input rule is
available."[^c2]

Three theorems turn this into a selection rule. Theorem 1 bounds how much
any adaptive controller can beat the best fixed action by the residual
mass of inputs where some other action helps, times the largest per-input
gain there. Theorem 2 gives the sample size an instance-level ($\Pi_2$)
controller needs before its empirical gain's *sign* is certifiable rather
than variance-bounded: "The resulting Bernstein-tight threshold has a
matching information-theoretic lower bound" (Proposition 1, via
Bretagnolle–Huber), so the threshold's order is tight, not just sufficient.
Theorem 3 gives the sample size a partition router ($\Pi_1$) needs, scaling
with cluster mass and gap rather than the per-sample margin that governs
$\Pi_2$ — which is why a coarser router can win exactly where the
instance-level controller is data-starved. Theorem 4 bounds the excess
risk of choosing the class by strict nested cross-validation: "Strict
nested cross-validation then turns the diagnostics into a selection rule,
choosing a near-best class up to an explicit stability term."[^c3]

Across four benchmarks under identical strict nested cross-validation, "the
predicted class matches the empirical winner": $\Pi_0$ on SMS-Spam
(residual-bounded), $\Pi_2$ on HallusionBench and A-OKVQA (Bernstein-viable),
$\Pi_1$ on FOLIO (n=203 far below the Bernstein threshold of 1898, so
$\Pi_2$'s sign is uncertified and its best controller slightly *increases*
loss over $\Pi_0$). On TextVQA, where OCR tokens supply a label-free
prediction-time prior, "the prior-gated controller wins... when OCR tokens
supply a label-free prediction-time prior," reaching 15.4% soft accuracy
against 8.4% for the fixed OCR action and beating $\Pi_2$ on non-OCR
features, which the paper attributes to an information-design gap (the
scalar feature block cannot recover what OCR gives directly) rather than a
Bernstein-threshold failure.[^c4]

## Why it matters

On stall 2 the wiki's existing entries score *which axis* or *whether to
ask at all* with a fixed-complexity criterion (mutual information, GBS,
VoI). This source adds a layer above those: which *class* of decision rule
— constant, partitioned, per-instance, gated — the data can support before
any of those criteria are estimated reliably. A per-instance uncertainty
score ([[mutual-information]]-style or otherwise) is one rung of this
lattice ($\Pi_2$); the theory says when that rung is not yet earned by the
sample size, and what to fall back to instead.

## Transfer

| | |
|---|---|
| In its home field | [[abstention|selective classification]] / learning-to-defer: a fixed action set, an i.i.d. sample, Bernstein concentration on a bounded loss, nested cross-validation for model selection |
| Here | choosing the class of an asking/deferral controller (answer, retrieve, defer, abstain) for a deployed LLM/VLM system |
| What survives | the nested-lattice decomposition of controller complexity; the residual bound as a ceiling on any adaptive gain; the finite-sample viability threshold as a reason a more expressive rule can be the wrong choice; nested CV as the nominated selector |
| What does not | the exact Bernstein constants (Theorem 2 is derived for a binary selective subproblem and used only as a *proxy* for richer multi-action controllers, per the paper's own limitation); the four benchmarks' specific regime tags, which depend on the chosen loss weights, feature block and judge model |

## Limits

- Theorem 2's derivation is for a binary reject/accept subproblem; its use
  as a viability proxy for the multi-action $\Pi_2$ families evaluated in
  Section 3 is stated by the authors as an approximation, not a proof for
  the general case.[^c5]
- The regime tags depend on the chosen action set, loss weights
  $(w_c,w_h,w_k)$, feature block, and (for semantic risk) a single judge
  model; the authors note "alternative judges or ensembles could shift the
  loss matrix and therefore the regime tags."[^c6]
- $\Pi_3$ requires a label-free, prediction-time side channel; none of the
  four core benchmarks has one, and the paper's own deployable-$\Pi_3$
  result (TextVQA) is a single case.
- This note's map to "which axis first" is this wiki's own framing: the
  paper never discusses axis selection — its controller classes choose an
  *action* (answer/retrieve/defer/abstain), not a *question axis*.

## Related

[[abstention]] · [[learned-deferral]] · [[value-of-information]] · [[mutual-information]]

[^c1]: jiang-2026-regime — "We organize controllers into a nested lattice of four classes: fixed actions, partition routers, instance-level controllers, and prior-gated controllers, ordered by complexity."
[^c2]: jiang-2026-regime — "the winning controller class changes with the statistical regime of the benchmark"
[^c3]: jiang-2026-regime — "The resulting Bernstein-tight threshold has a matching information-theoretic lower bound, and strict nested cross-validation provably selects a near-best class."
[^c4]: jiang-2026-regime — "the predicted class matches the empirical winner"
[^c5]: jiang-2026-regime — "The Bernstein analysis is derived for a selective subproblem and used as a class-level viability proxy for richer multi-action controllers."
[^c6]: jiang-2026-regime — "alternative judges or ensembles could shift the loss matrix and therefore the regime tags"
