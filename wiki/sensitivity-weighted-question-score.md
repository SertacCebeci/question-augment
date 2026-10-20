---
description: "Rank candidate questions by expected [[entropy]] reduction, but weight each Sadeghi, Smith & Del Rey Fernández (2026,"
aliases: []
sources: ["sadeghi-2026"]
---
# Sensitivity-weighted question score

> Rank candidate questions by expected [[entropy]] reduction, but weight each
> one by how much the optimization's own objective moves when the
> underlying parameter is perturbed — a decision-relevance proxy computed
> from the solver, not from a separately elicited utility.

## Definition / Mechanism

Sadeghi, Smith & Del Rey Fernández (2026, §4.4–4.6) score each candidate[^s1]
clarification question $q$ about an uncertain numeric parameter $\theta_i$
(a cost, capacity, demand, bound or penalty an LLM guessed while
translating a natural-language optimization problem into solver code) as

$$\mathrm{score}(q) = \Delta H(q)\cdot g(s_i), \qquad g(s_i)=\alpha+(1-\alpha)s_i,\ \alpha=0.5$$

(Eq. 5), where $\Delta H(q)$ is the expected reduction in the parameter's
own differential entropy $H_i=\tfrac12\log(2\pi e\sigma_i^2)$ (Eq. 3) under a
truncated-Gaussian belief $\theta_i\sim\mathcal N(\mu_i,\sigma_i^2)$, and
$s_i$ (Eq. 4) is the importance-score component that weights it — built
entirely from the solver, with no elicited utility function:

$$s_i = w_{\mathrm{sw}}\phi_{\mathrm{sw}}(\theta_i) + w_{\mathrm{gr}}\phi_{\mathrm{gr}}(\theta_i) + w_{\mathrm{sh}}\phi_{\mathrm{sh}}(\theta_i) + w_{\mathrm{bd}}\phi_{\mathrm{bd}}(\theta_i)$$

with weights $(0.40,0.30,0.15,0.15)$ on four re-solve signals obtained by
perturbing $\theta_i$ by $\{0.5,0.8,1.2,2.0\}\times$ its current value and
re-solving: the normalized swing in the optimal objective, a local
finite-difference sensitivity, the magnitude of the associated shadow
price, and the fraction of constraints whose binding status flips. The
note's object is the composite $\mathrm{score}(q)$, not $s_i$ alone: a
parameter with low entropy but high $s_i$ does not necessarily outrank one
with high entropy and low $s_i$, since $\Delta H(q)$ still multiplies the
result. Three answer types (a direct value, a binary threshold split, a
value confirmation) are each mapped to a different $\Delta H(q)$
computation, and the highest-scoring open parameter is asked about next,
one at a time, after every re-solve.

## Why it matters

This is a concrete answer to stall 2's "which axis first?" for a domain
where [[value-of-information]] is usually blocked by the absence of a
written utility ([[expected-utility]]): here the optimization's own
objective supplies one, and the score approximates decision-relevance
without computing $\mathrm{VoI}$ or exact regret. Evaluated on 1,723
instances across seven masked optimization-translation benchmarks, ordering
questions by this score raised exact objective-value agreement over a
no-interaction baseline by 21.3–71.3 percentage points (final agreement
27.0%–87.6%, most datasets above 77%), at a cost of 1.4–5.7 questions per
instance on average (Sadeghi et al. 2026, §6, Table 2).

## Transfer

| | |
|---|---|
| **In its home field** | post-optimal sensitivity analysis in linear/mixed-integer programming: shadow prices (dual values), objective-coefficient ranging and binding-constraint status, each with a defined validity region around a computed optimum |
| **Here** | a cheap, repeated local re-solve after multiplicative perturbation of one uncertain parameter at a time, used only to rank which of several open axes is worth a question |
| **What survives** | the core move — that decision-relevance can be read off the local shape of an optimization landscape at negligible extra solver cost, with no separate utility elicitation, whenever the object being asked about is itself an input to an optimization problem |
| **What does not** | the guarantees duality theory attaches to a shadow price (validity only within the current LP basis, under non-degeneracy); the benchmark set includes mixed-integer and nonlinear problems where no such guarantee holds, and the four perturbation multipliers are an ad hoc discretization rather than a certified sensitivity interval |

## Limits

- The score is evaluated only against an idealized simulator that answers
  every question with the exact masked ground-truth value; the authors
  name this as a threat to validity — real users answer approximately or
  inconsistently (§7, threats to validity, point 1).
- The benchmarks were built by masking parameters selected by objective
  sensitivity, solution sensitivity and feasibility impact — signals that
  overlap with the [[recovery-postulate|recovery]]-time importance scorer itself, which the
  authors flag as a circularity that may favor the method the masking was
  designed to test for (§7, point 4).
- Reported agreement depends heavily on the translator model that first
  turns text into code (GPT-5.3-Codex in the main results); the paper
  reports sharply worse behaviour with a weaker translator (GPT-4o-mini),
  and interactive repair of numeric values cannot fix a structural
  translation error (§7, point 6).
- The weights $(0.40,0.30,0.15,0.15)$, $\alpha=0.5$ and the perturbation
  multipliers are fitted choices for this system, not derived quantities;
  no ablation isolating their individual contribution is reported here.
- IndustryOR (42 instances) and ComplexOR (18 instances) are small enough
  that the per-dataset agreement figures carry wide uncertainty.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[current-solution-strategy]] · [[optimistic-pessimistic-strategy]] · [[expected-utility]] · [[sensitivity-as-value-of-information]]

[^s1]: sadeghi-2026
