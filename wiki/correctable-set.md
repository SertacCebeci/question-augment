---
description: "A decision-theoretic gate — query only if some admissible sequence of interactions could still reach an acceptable output; otherwise accept or defer without asking."
aliases: ["correctable set", "reachability gate", "reachability score"]
sources: ["zhu-2026"]
---
# Correctable set

> Before asking whether a question is worth its cost, ask whether any
> question can reach an acceptable answer at all.

## Definition / Mechanism

At an episode state $s_t$ — case, interaction history, remaining budget
$B_t$ — Zhu (2026) defines the one-step reachable set as every
output attainable by one admissible query action and its possible
response, closed under further admissible sequences whose cost still fits
$B_t$.[^c1]

Given a clinically elicited acceptability criterion $C$ with tolerance
$\eta$, the **correctable set** $M_C(s_t)$ is the reachable outputs that
would pass $C$; the case is correctable at $s_t$ iff $M_C(s_t)\neq\emptyset$.[^c2]

This yields a **reachability gate**: if $M_C(s_t)=\emptyset$, no admissible
query can reach an acceptable output, so any query with strictly positive
cost has non-positive net value — the correct action is to defer (or
accept, if already acceptable), never query.[^c3]

Because $C$ depends on an unobserved ground truth, $M_C$ is not computable
at run time; it is replaced by a learned **reachability score**
$\hat\rho(s_t)\approx \Pr[M_C(s_t)\neq\emptyset]$, trained on traces where
the reachable outcome is known post hoc.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| decision theory (Zhu 2026, Def. 2) | correctable set | exact — the set $M_C(s_t)$ itself |
| decision theory (Zhu 2026, Prop. 1) | reachability gate | exact — the decision rule "query only if $M_C(s_t)\neq\emptyset$", i.e. the set used as a test |
| decision theory (Zhu 2026, §3) | reachability score | close — the learned estimate $\hat\rho(s_t)$ of the set's nonemptiness, not the set |

## Why it matters

The construction names an asymmetry no other note on this stall states:
"a click carries a few bits, whereas domain shift induces a
high-dimensional mismatch in the representation. Low-bandwidth input
cannot inject high-dimensional information." A query can only collapse
[[efe-planning-as-variational-inference|ambiguity]] among hypotheses the system already entertains — it cannot
manufacture evidence the system lacks.[^c5]

That reframes selection. In Zhu's controller (Eq. 4) the query of maximum
net value is chosen *subject to* $\hat\rho(s_t)\ge\rho_{\min}$, and the
constraint is stated separately because a positive value under a
misspecified, optimistic response model does not imply the case is
reachable. So before any value computation, an asker checks whether the
space it can still reach contains an acceptable answer, and skips straight
to defer or accept when it does not.[^c10]

Zhu (2026) contrasts the gate with learning-to-defer, which
routes to a human on predicted model error: "Learning to defer typically
routes on predicted model error. The gate routes on predicted
irreparability, which is a different quantity: a case may be badly wrong
and trivially correctable, or nearly right and unreachable because the
residual disagreement is irreducible ambiguity rather than error."[^c6]

That the same contrast separates the gate from [[abstention]]'s selection
function — which also thresholds a predicted-error score — is this wiki's
reading, not the paper's; the paper uses selective prediction only as the
risk–coverage perspective on its accept decision.

## Transfer

| | |
|---|---|
| In its home field | Reachable-set / feasibility-gate reasoning from control and robust decision theory, applied to one clinician-in-the-loop image-segmentation episode with a bounded, reversible update operator |
| Here | Any asker deciding whether a further question can still change its output, before pricing that question |
| What survives | The precondition itself — a query is worth considering only if some admissible sequence of queries reaches an acceptable output — and the move of replacing the unobservable feasibility test with a learned score trained on traces where the outcome is known after the fact |
| What does not | The specific objects — a pixel-level acceptability criterion $C$, a segmentation-specific update operator $T$, a resource vector $B$ measured in interruptions and corrected area — need re-definition for a non-visual asking system, and no general-purpose $\hat\rho$ estimator exists outside this one domain |

[^c11.1][^c11]

## Limits

- $M_C$ itself is never computed; every claim above transfers only as far
  as the estimate $\hat\rho$. The paper's own falsification test for the
  whole framework is whether $\hat\rho$ clears chance and clears plain
  predicted-quality at an external site: "If ρ̂ does not exceed chance at
  external targets, or is not better than predicted mask quality alone,
  the base layer fails."[^c7]
- That test has not been run.
- The framework is stated as normative, not evaluated: "Equations (2)–(4)
  are normative until their risk, response, cost, and update models have
  been estimated for a defined clinical use case and separately
  safeguarded."[^c8]
- Single-author Perspective (arXiv, 2026), not peer-reviewed; the authors
  call the reachability gate itself "deliberately weak, and its usefulness
  lies in what it excludes rather than in what it proves."[^c9]
- The Transfer rows and the reading of the gate as an asker's
  pre-valuation check are this wiki's mapping from one segmentation
  setting to asking in general; the source makes no claim beyond its
  clinical use case.

## Related

[[value-of-information]] · [[abstention]] · [[reversibility]] · [[question-budgets]] · [[expected-utility]]

[^c1]: zhu-2026 — "The one-step reachable set at state st is"
[^c2]: zhu-2026 — "the correctable set at st is MC (st ) = {ŷ ∈ M(st ) : C(ŷ; η) = 1}."
[^c3]: zhu-2026 — "The correct action is therefore D (or A, if the current mask is already acceptable), not Q."
[^c4]: zhu-2026 — "trained on simulated and recorded interaction traces where the post-hoc reachable outcome is known."
[^c5]: zhu-2026 — "a click carries a few bits, whereas domain shift induces a high-dimensional mismatch in the representation. Low-bandwidth input cannot inject high-dimensional information."
[^c6]: zhu-2026 — "The gate routes on predicted irreparability, which is a different quantity: a case may be badly wrong and trivially correctable, or nearly right and unreachable because the residual disagreement is irreducible ambiguity rather than error."
[^c7]: zhu-2026 — "If ρ̂ does not exceed chance at external targets, or is not better than predicted mask quality alone, the base layer fails."
[^c8]: zhu-2026 — "Equations (2)–(4) are normative until their risk, response, cost, and update models have been estimated for a defined clinical use case and separately safeguarded."
[^c9]: zhu-2026 — "The proposition is deliberately weak, and its usefulness lies in what it excludes rather than in what it proves."
[^c10]: zhu-2026 — "a response model that is optimistic about what a click achieves can manufacture positive value for an unreachable case"
[^c11.1]: zhu-2026 — "Interaction therefore helps only when an acceptable solution lies within the range the system can reach."
[^c11]: zhu-2026
