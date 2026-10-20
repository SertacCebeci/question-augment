---
description: "A post-hoc calibrator that fits a separate logistic-regression scaler per embedding cluster instead of one global scaler, cutting calibration error where errors are heterogeneous."
aliases: ["local Platt-scaling"]
sources: ["arxiv-2604-06723"]
---
# Local Platt-scaling

> A single calibration curve assumes one kind of miscalibration; splitting
> the training set into clusters first lets each region be wrong in its
> own way.

## Definition / Mechanism

Global [[calibration|Platt-scaling]] fits one logistic regression
$P(y=1\mid X)=\sigma(w\hat p+\beta)$ mapping an uncalibrated confidence
score $\hat p$ to a correctness probability, shared across every sample of
a task. Lin, Liu, Gao, Thongtanunam & Treude (2026) argue this
is miscalibrated by construction whenever error is sample-dependent: a
single $(w,\beta)$ cannot separately correct a region of the input space
where the score under-states correctness from a region where it
over-states it.[^c1]

**Local Platt-scaling** replaces the one calibrator with an ensemble: a
feature vector $\phi(x)$ concatenates a UMAP projection of input/output
text embeddings (Qwen3-Embedding-8B, 20 dimensions) with the sample's
uncalibrated confidence score, HDBSCAN partitions the training set on
$\phi(x)$, and a separate Platt calibrator is fit per cluster.
[^c2]

At inference, a new instance is routed to its nearest-neighbour cluster
and scored by that cluster's calibrator; an instance HDBSCAN marks an
outlier falls back through a backoff function $\psi(\hat p)$ — itself a
hyperparameter, either the global calibrator or the raw uncalibrated
score.
[^c3]

## Why it matters

The method is only worth its extra machinery where errors are in fact
heterogeneous, and the paper's own results show that condition is not
guaranteed: across three automated-code-revision tasks (program repair,
vulnerability repair, code refinement), global Platt-scaling already
reaches ECE ≤ 0.08 on two of the three tasks, and only the third shows
the ≥ 0.14 ECE gap that gives local scaling something to close.
[^c4]

Local Platt-scaling improved calibration on every model, confidence score
and correctness metric tested, but on the two tasks where the global
baseline was already adequate the gains were marginal (ECE improved by
0.01–0.07).
[^c5]
[^c6]

The one confidence score it paired best with — **minimum token
probability**, the lowest single-token probability in the generated
sequence — was also the strongest fine-grained score on its own, ahead of
lowest-K token probability, attention-weighted uncertainty, and both
sequence-level scores (normalised sequence likelihood, average token
probability), across all 14 models and three tasks.
[^c7]

That is the opposite ranking from [[sequence-likelihood-confidence]],
where minimum token probability was one of three intrinsic signals
found to fall in the same *weak* band as sequence likelihood on
retrieval-dominated extractive QA — a different task and correctness
notion, not a direct contradiction, but a sign that which token-level
statistic is informative is task-dependent, not a property of the
statistic alone.

## Limits

- A **white-box** method: it needs token-level softmax probabilities and,
  for the attention-weighted variant, attention weights, so it does not
  apply to closed-source models reachable only through an API.[^c8]
- Gains are task-dependent and were marginal on two of the three tasks
  studied; the paper frames the local/global choice on those two as a
  latency-versus-accuracy tradeoff, not a strict improvement.
- Evaluated on 14 open-source models (≤8B–≤72B) and three code-revision
  tasks only; not evaluated on non-code domains or on models larger than
  72B.
- Correctness metrics (exact match, edit progress, checks passed) are
  the paper's own stated imperfect proxies for true correctness.

## Related

[[calibration]] · [[sequence-likelihood-confidence]] · [[abstention]] ·
[[confidence-report-repair]]

[^c1]: arxiv-2604-06723 — "Conventional Platt-scaling assumes calibration errors are uniform across a task by learning only a single global calibrator. However, the variability in code and specifications within ACR tasks can induce heterogeneous errors"
[^c2]: arxiv-2604-06723 — "local Platt-scaling trains distinct calibrators for specific clusters of samples. These clusters are partitioned according to a multidimensional space comprised of input/output embeddings, alongside their corresponding uncalibrated confidence scores."
[^c3]: arxiv-2604-06723 — "If an instance is assigned to cluster k, the corresponding local calibrator is applied; otherwise, it is classified as an outlier, triggering our novel ψ(·) backoff function."
[^c4]: arxiv-2604-06723 — "we find that global Platt-scaling is generally sufficient for achieving low calibration error in DCF-Bug and DCF-Vul (best calibration results ≤ 0.08 ECE), yet falls short for CR-Trans (best calibration results generally ≥ 0.14 ECE)"
[^c5]: arxiv-2604-06723 — "the consistent improvements from local Platt-scaling across all models, correctness metrics, and ACR tasks demonstrate that our rationale holds in practice"
[^c6]: arxiv-2604-06723 — "we note that all calibration improvements are still marginal (ECE: ∆0.01-0.07, B: ∆0.01-0.02, BC: ∆1-2)"
[^c7]: arxiv-2604-06723 — "minimum token probability is the best-performing confidence score across all tasks, correctness metrics, and models considered"
[^c8]: arxiv-2604-06723 — "Because our methods rely on token-level softmax probabilities with some requiring access to the attention mechanism, they are generally not applicable to most closed-source models that are only available through an API."
