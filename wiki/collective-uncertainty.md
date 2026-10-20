---
description: "Pools heterogeneous VLMs' semantic opinions and decomposes the pooled entropy exactly into mean per-model uncertainty plus a Jensen-Shannon conflict term."
aliases: ["CUSP", "Collective Uncertainty through Semantic Opinion Pooling", "collective entropy decomposition"]
sources: ["yu-2026"]
---
# Collective uncertainty

> When several heterogeneous models answer the same question, their pooled
> uncertainty splits exactly into "each model is unsure" and "the models
> disagree" — two different reasons to keep asking.

## Definition / Mechanism

Yu, Garcia, Jalaian & Bastian (2026) introduce CUSP: each of $K$
heterogeneous VLMs samples free-form responses to the same input; an
LLM-based semantic-equivalence judge clusters them into a shared set of
semantic response classes $\{s_1,\dots,s_J\}$, giving each model an empirical
opinion $\hat p_k$ over that shared support and a per-model semantic entropy
$H_k$. The opinions are pooled uniformly (linear opinion pooling, $w_k=1/K$)
into $\bar p_M$, whose [[entropy|Shannon entropy]] is the **collective entropy**
$H^{coll}_M$, which decomposes exactly as $H^{coll}_M = \bar H^{ind}_M +
D_{JS}(\hat p_1,\dots,\hat p_K)$ — the unnormalized collective entropy
decomposes exactly into the mean of the models' individual semantic
entropies and the JSD, separating total dispersion from model conflict.[^c1]

Both terms are reported as normalized scores in $[0,1]$: collective
uncertainty (dispersion of the pooled opinion) and JSD (conflict among the
model-level opinions). The method needs neither token logits nor [[calibration]]
labels, so it applies to closed commercial APIs.

## Why it matters

Two systems can have equal collective uncertainty for opposite reasons —
every model is uniformly hesitant, or the models confidently disagree — and
the decomposition tells them apart, which a single pooled-entropy number
cannot.

In static multi-VLM ensembles, collective uncertainty is the strongest
signal in the small-model regime (0.764 AUROC for prediction-error
detection, 0.889 AUARC for [[abstention]]), outperforming majority voting and
naive selection by 4.7 to 15.8 points and widening its margin as the
ensemble grows; JSD is strongest in the evaluated commercial regime (0.819
AUROC, 0.910 AUARC) and ranks hard-answer model conflict with AUROC up to
0.982.[^c2]

Over the full trajectory of a multi-step, multi-agent evidence-acquisition
system, subagent collective uncertainty ranks system failures above chance
(0.619 AUROC) and gives the best abstention ordering among the evaluated
signals (0.699 AUARC).[^c3]

## Transfer

| | |
|---|---|
| **Home field** | linear opinion pooling of expert probability distributions (Stone 1961, cited in Yu et al. 2026) and the generalized Jensen-Shannon divergence identity (Lin 1991) over a fixed, shared outcome space; [[semantic-entropy]]'s entailment-clustered entropy for a single model |
| **Here** | free-form answers from heterogeneous VLMs, mapped by an LLM judge (not an NLI entailment model) into a shared semantic response space, then pooled and decomposed |
| **What survives** | the algebraic identity itself — pooled entropy = mean individual entropy + JSD — holds exactly regardless of what produced the per-model opinions |
| **What does not** | the entailment-model clustering semantic entropy was validated with; here clustering is done by an LLM judge whose errors propagate directly into both terms; JSD's role as a *conflict* signal is not a proxy for prediction error |

[^c4]

Conflict-AUROC uses the standard AUROC calculation with a different binary
target; it must not be interpreted as prediction-error detection.[^c5]

## Limits

- CUSP's collective uncertainty depends on semantic-clustering granularity
  and judge errors. This limitation is more consequential in free-form
  multi-agent settings, which require an LLM-based judge, than in
  fixed-choice tasks with lightweight response parsing.[^c6]
- Each opinion is estimated from only 10 samples per model, limiting
  distributional resolution; the commercial-regime evaluation (20
  three-VLM systems from six models) is not a population estimate.
- The decomposition names two failure modes it does not cover: models
  sharing a misconception, or an orchestrator misintegrating consistent
  evidence — the signals are complementary, not certificates of
  correctness.
- Single preprint (arXiv, September 2026), not yet peer reviewed; no
  independent replication.
- This note rests on one paper's own benchmarks; it does not establish that
  the AUROC/AUARC gains generalise beyond the tested VLM regimes.

## Related

[[semantic-entropy]] · [[uncertainty-decomposition]] · [[abstention]] · [[expected-information-gain]]

[^c1]: yu-2026 — "the unnormalized collective entropy decomposes exactly into the mean of the models’ individual semantic entropies and the JSD, separating total dispersion from model conflict"
[^c2]: yu-2026 — "collective uncertainty is the strongest signal in the small-model regime (0.764 AUROC for prediction-error detection, 0.889 AUARC for abstention), outperforming uncertainty baselines majority voting and naive selection by 4.7 to 15.8 points and widening its margin as the ensemble grows; JSD is strongest in the evaluated commercial regime (0.819 AUROC, 0.910 AUARC) and ranks hard-answer model conflict with AUROC up to 0.982"
[^c3]: yu-2026 — "Over the full trajectory of a multi-step, multi-agent system, subagent collective uncertainty ranks system failures above chance (0.619 AUROC) and gives the best abstention ordering among the evaluated signals (0.699 AUARC)"
[^c4]: yu-2026 — "Because the positive class here is conflict rather than incorrect prediction, Conflict-AUROC is not interchangeable with the prediction-error detection AUROC reported in Section 4.1."
[^c5]: yu-2026 — "Conflict-AUROC uses the standard AUROC calculation with a different binary target; it must not be interpreted as prediction-error detection."
[^c6]: yu-2026
