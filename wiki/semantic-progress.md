---
description: "Formalizes a dialogue's progress toward answering a question as conditional mutual information between the task-relevant state and accumulated answer evidence, given the question."
aliases: ["semantic progress", "question-conditioned uncertainty reduction", "agent-induced information gain"]
sources: ["he-2026"]
---
# Semantic progress

> Whether a multi-turn dialogue's accumulated answers reduced uncertainty about
> what the user needed to know — not whether any one turn was fluent, safe or
> well-styled.

## Definition / Mechanism

He, Kasiviswanathan & Janzing (2026) define a semantic progress
measure as a function $P_q: 2^E \to \mathbb{R}_{\geq0}$ over accumulated
evidence $A$, with marginal gain $\Delta_q(e\mid A) = P_q(A\cup\{e\}) -
P_q(A)$, required to satisfy three axioms: irrelevance ($\rho_q(e)=0
\Rightarrow \Delta_q(e\mid A)=0$), monotonicity ($\Delta_q(e\mid A)\geq0$)
and diminishing returns ($A\subseteq B \Rightarrow \Delta_q(e\mid A)\geq
\Delta_q(e\mid B)$).[^c1]

Treating dialogue as $D_{1:T}=(q_1,a_1),\dots,(q_T,a_T)$ and $W$ as the
latent task-relevant state, the [[chain-rule|chain rule for mutual information]] splits
$I(W;D_{1:T})$ into a user-induced term (task specification, from the
questions) and an agent-induced term $\sum_t I(W;a_t\mid C_t^U)$ (progress
from the answers, conditioned on context up to and including each
question). The paper adopts the user's perspective and studies only the
agent-induced term.[^c2]

The realized ideal semantic progress of an observed evidence trace $a_T$ is
$P_q^\star(a_T) \triangleq H(W\mid q) - H(W\mid q, A_T=a_T)$, whose
expectation over the random evidence is the conditional mutual information
$I(W;A_T\mid q)$ — the same functional as [[mutual-information]],
conditioned on the question and applied to accumulated multi-turn evidence
rather than a single answer. Because $P_q^\star$ is not computable in
open-ended dialogue, the paper tests the definition only indirectly: it
builds a tractable estimator ([[gaussian-information-gain]]) and checks
whether the dialogue it scores higher is the one human raters preferred.[^c3]

## Why it matters

This gives "has an exchange gotten closer to $|W|=1$" a form that works
across a whole multi-turn trace, not just per question: the same
conditional-mutual-information object this wiki uses at the single-question
level ([[mutual-information]], [[expected-information-gain]]) is
decomposed into user-induced and agent-induced parts and axiomatized by
irrelevance, monotonicity and diminishing returns instead of being read off
a fixed likelihood model.

## Transfer

| | |
|---|---|
| **Home field** | Bayesian/information-theoretic inference: a latent variable $W$, a known or assumed joint distribution over $W$ and observations, [[conditional-entropy|conditional entropy]] computed exactly |
| **Here** | open-ended natural-language dialogue with no explicit [[possible-worlds|hypothesis space]], no written prior over $W$, and no tractable posterior — evidence is free text |
| **What survives** | the definition itself (marginal-gain function with irrelevance/monotonicity/diminishing-returns axioms) and the chain-rule decomposition into user- vs. agent-induced information |
| **What does not** | direct computability of $P_q^\star$ — it is never evaluated in closed form here, only indirectly validated through the [[gaussian-information-gain]] estimator's agreement with human preference labels |

## Limits

- $P_q^\star$ itself is never computed in the paper's experiments; every
  empirical claim is about the [[gaussian-information-gain]] estimator's
  agreement with human preference, which is evidence for the estimator, not
  a direct test of the definition.[^c4]
- The decomposition treats the user's questions as exogenous task
  specification and studies only agent-induced progress; it explicitly does
  not model the user's private, unstated knowledge.
- Defined for information-seeking dialogue; the paper does not claim the
  measure captures fluency, style, safety or factual correctness.

## Related

[[gaussian-information-gain]] · [[mutual-information]] · [[expected-information-gain]] · [[semantic-entropy]]

[^c1]: he-2026 — "A useful measure of semantic progress in informationseeking dialogue should satisfy irrelevance (if ρq (e) = 0, then ∆q (e | A) = 0), monotonicity"
[^c2]: he-2026 — "The first term is user-induced task specification; the second is agent-induced semantic progress. The"
[^c3]: he-2026 — "Pq⋆ (aT ) ≜ H(W | q) − H(W | q, AT = aT )"
[^c4]: he-2026 — "conservative with respect to our stated scope: G AUSSIAN IG measures semantic progress rather than"
