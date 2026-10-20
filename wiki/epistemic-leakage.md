---
description: "Variation from the answering model, not the input's ambiguity, absorbed into answer-based aleatoric estimates — measured as correlation with epistemic uncertainty."
aliases: ["epistemic leakage"]
sources: ["nahum-2026"]
---
# Epistemic leakage

> When an estimator of *[[efe-planning-as-variational-inference|ambiguity]]* is built by generating model answers and
> comparing them, the answers carry the model's own knowledge gaps along with
> the input's ambiguity. That contamination is epistemic leakage — and it is
> exactly the failure mode stall 2 needs to rule out before trusting an
> aleatoric-uncertainty score as the reason to ask.

## Definition / Mechanism

Nahum et al. (2026) decompose an answer-based aleatoric
estimate $A_{Y|C}(x)$ into the part explained by the latent interpretation
space $I$ (the disambiguated meanings a clarification can express) and a
residual. Two formal results show the residual is not noise but a specific,
model-dependent distortion: **Proposition 2 (suppression)** — if two distinct
interpretations $i,j$ (with $H(I\mid x)>0$) induce the same response
distribution, $p(y\mid x,i)=p(y\mid x,j)$, the answer-based estimate collapses
to zero even though genuine ambiguity remains ($A_{Y|I}(x)=0$ while
$H(I\mid x)>0$); **Proposition 3 (inflation)** — if a single interpretation
($H(I\mid x)=0$) is expressed by two equivalent clarifications $c,c'$ that the
target model answers differently, $p(y\mid x,c)\neq p(y\mid x,c')$, the
answer-based estimate is pushed above zero ($A_{Y|C}(x)>0$) with no ambiguity
in the input at all.[^c1]

Empirically, the paper measures Pearson correlation $\rho(\mathrm{AU},
\mathrm{EU})$ between the answer-based aleatoric (AU) and epistemic (EU)
components of two existing decomposition methods (Clarification Ensembling,
Spectral Decomposition) across three benchmarks (AmbigQA, AmbigVQA,
AMBROSIA) and up to six model backbones. "Across datasets and models, these
correlations are consistently non-zero, and in some cases substantial (e.g.,
up to ρ ≈ 0.5 for spectral on AmbigQA), indicating a leakage between the two
components."[^c2]

When the answer-based AU term is replaced by a clarification-only estimate
computed over the *same* clarification set (see
[[clarification-only-aleatoric-uncertainty]]), leaving EU unchanged: "Across
the 32 available dataset-model-method settings, replacing the baseline AU
with our estimate yields a favorable outcome in 78% of cases. In 62% of
settings, our estimate significantly lowers |ρ(AU, EU)| (p < 0.05 …), and in
another 16%, the resulting correlation is not statistically different from
zero … Importantly, our estimate is never significantly worse."[^c3]

## Why it matters

Stall 2 asks which axis to open next; a common trigger is "the model is
uncertain about the input's meaning, so ask." If the estimator used to detect
that uncertainty is itself contaminated by what the model does or does not
know, an agent can be pushed to ask about axes that are not actually
underspecified (inflation) or fail to ask about axes that are (suppression) —
in both cases for reasons that have nothing to do with the input. Leakage is
therefore a *validity* problem for any answer-based ambiguity trigger, not
just a cost one.

## Limits

- Propositions 2 and 3 are exact only under the stated idealised conditions
  (perfect response determinism or perfect clarification equivalence); the
  paper itself notes real clustering and generation are imperfect, so leakage
  in practice is a matter of degree, not the all-or-nothing collapse the
  propositions state.
- The correlation evidence is confined to two answer-based decomposition
  methods (Clarification Ensembling, Spectral Decomposition), three
  benchmarks, and open/closed LLMs up to 120B-class; whether the same
  coupling holds for other answer-based uncertainty estimators is untested
  here.
- Correlation is a symptom, not a proof of causal contamination; the paper's
  causal story rests on the propositions, which are idealised.

## Related

[[clarification-only-aleatoric-uncertainty]] · [[uncertainty-decomposition]] · [[semantic-entropy]] · [[mutual-information]]

[^c1]: nahum-2026 — "Proposition 2 (Suppressed answer-based uncertainty). Fix an input x, and suppose H(I | x) > 0, but p(y | x, i) = p(y | x, j) for any two i, j with p(i | x), p(j | x) > 0. Then AY |I (x) = 0."
[^c2]: nahum-2026 — "Across datasets and models, these correlations are consistently non-zero, and in some cases substantial (e.g., up to ρ ≈ 0.5 for spectral on AmbigQA), indicating a leakage between the two components."
[^c3]: nahum-2026 — "Across the 32 available dataset-model-method settings, replacing the baseline AU with our estimate yields a favorable outcome in 78% of cases. In 62% of settings, our estimate significantly lowers |ρ(AU, EU)| (p < 0.05; paired bootstrap details in Appendix B.4), and in another 16%, the resulting correlation is not statistically different from zero, which is also desirable because aleatoric and epistemic uncertainty should be independent. Importantly, our estimate is never significantly worse."
