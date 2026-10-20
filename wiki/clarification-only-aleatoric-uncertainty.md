---
description: "Estimates ambiguity-induced aleatoric uncertainty by clustering generated clarifications into interpretations and scoring entropy there, without generating any model answers."
aliases: ["clarification-only aleatoric uncertainty estimation", "CO-SemEnt", "CO-SemEnt+Like"]
sources: ["nahum-2026"]
---
# Clarification-only aleatoric uncertainty estimation

> A way to score "how ambiguous is this input" without ever asking the model
> to answer it — cluster the clarifications the model would ask, not the
> answers it would give.

## Definition / Mechanism

Nahum et al. (2026) propose a pipeline that never samples a
model response. Given an input $x$: (1) prompt an LLM to generate a
clarification set $C(x)=\{c_1,\dots,c_N\}$, each resolving a possible
[[efe-planning-as-variational-inference|ambiguity]] differently — an unambiguous input yields none; (2) cluster the
clarifications by the interpretation they express, via a semantic-identity
map $\hat g: C(x)\to \hat I(x)$, giving $K\le N$ interpretation clusters
with empirical frequencies $\hat p_k = n_k/N$ ("This follows the idea of
semantic entropy (Kuhn et al., 2023), but applies semantic clustering to
clarifications rather than answers"); (3) optionally re-weight clusters by an
LLM-estimated plausibility $\tilde p_k$ instead of raw frequency; (4)
aggregate into a scalar via [[entropy|Shannon entropy]] over the interpretation
distribution — $H(\hat p)$ for **CO-SemEnt**, $H(\tilde p)$ for
**CO-SemEnt+Like**.[^c1]

Evaluated as ambiguity detection (AUROC) on three benchmarks (AmbigQA,
AmbigVQA, AMBROSIA) against answer-based baselines (Clarification Ensembling,
Spectral Decomposition, Verbalized, #Clars) under the *same* generated
clarification set: "this direct approach improves AUROC (63.34 vs. 60.85),
reduces computational cost by 4–26× in output tokens and 2.2–3.5× in API
calls, and yields estimates with substantially lower correlation with
epistemic uncertainty" ([[epistemic-leakage]]). CO-SemEnt+Like was the
strongest variant overall in Table 1.[^c2]

## Transfer

| | |
|---|---|
| **Home field** | [[semantic-entropy]]'s home use: cluster *sampled answers* to one fixed question by bidirectional entailment, score entropy over the partition, as a confabulation detector |
| **Here** | cluster *generated clarifications of the input itself*, before any answer is produced, as an ambiguity-of-the-input detector |
| **What survives** | the cluster-then-entropy computation, and the certainty/dispersion reading of the resulting score |
| **What does not** | the object being clustered (answers → clarifications) and the target event (confabulation risk → input ambiguity); the entailment-model clustering step of semantic entropy is replaced here by an LLM interpretation-identity call, with its own error profile |

## Limits

- Depends on the clarification-generation step being representative of the
  true ambiguity in $x$; an LLM that fails to surface a real reading never
  gets a chance to cluster it.
- The optional likelihood re-weighting (CO-SemEnt+Like) adds one more LLM
  call whose own [[calibration]] is unvalidated against ground-truth
  interpretation frequencies.
- Validated only as a binary ambiguity-detection signal (AUROC/AUPRC) on
  three QA/SQL benchmarks with ground-truth ambiguity labels; not evaluated
  as a trigger inside a live asking loop.
- Gains over the strongest answer-based baseline are modest on two of three
  benchmarks (AmbigQA, AmbigVQA); the larger gain is on AMBROSIA, where the
  paper attributes it to that dataset's many-valid-SQL-forms structure
  inflating the answer-based baselines specifically.

## Related

[[epistemic-leakage]] · [[semantic-entropy]] · [[uncertainty-decomposition]] · [[entropy]]

[^c1]: nahum-2026 — "This follows the idea of semantic entropy (Kuhn et al., 2023), but applies semantic clustering to clarifications rather than answers."
[^c2]: nahum-2026 — "this direct approach improves AUROC (63.34 vs. 60.85), reduces computational cost by 4–26× in output tokens and 2.2–3.5× in API calls, and yields estimates with substantially lower correlation with epistemic uncertainty"
