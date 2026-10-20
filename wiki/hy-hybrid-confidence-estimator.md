---
description: "Averaging a model's self-reported verbal confidence with the spectral diversity of its sampled answer embeddings beats either signal alone at equal or lower sampling cost."
aliases: ["HY@p", "hybrid confidence estimator"]
sources: ["sharma-2026"]
---
# HY@p — hybrid confidence estimator

> Two cheap, independently weak confidence signals — what the model says
> about itself and how much its sampled answers disagree — are not
> redundant; averaged, they beat either alone.

## Definition / Mechanism

HY@p combines two black-box, per-query confidence signals for a query
answered $p$ times: **verbal confidence** (the model self-reports a
numeric confidence alongside its answer) and **spectral answer diversity**
(the negative von Neumann [[entropy]] of a Gram matrix built from the $p$
sampled answers' embeddings, following Nikitin et al. 2024's kernel
language entropy). Sharma, Sai & Pal (2026) introduce HY@p as "a simple
hybrid of the two" and report it is, to their knowledge, the first
empirical study of this combination.[^c1]

Across six domains from three datasets (MMLU-Pro, MATH500, TriviaQA) and
five black-box LLMs (GPT-4.1-nano, GPT-5-nano, GPT-5-mini, Claude-Haiku-4.5,
Llama-3.3-70B-Instruct), the per-query ranking is stable: verbal confidence
alone averages 0.689 AUROC, spectral diversity at 10 samples (VN@10)
averages 0.737, and HY@5 averages 0.752 — matching or beating VN@10 in 19
of 30 cells while using half as many samples (mean +0.014 AUROC, one-sided
$p=0.07$).[^c2]

## Why it matters

For stall 10 (how much to commit, and how to say the rest), this is a
concrete, cheaper alternative to sampling-only uncertainty scores such as
[[semantic-entropy]] when the base decision only needs a ranking (which
answers to trust) rather than a calibrated probability: it needs one
generation for the verbal component plus $p$ (as low as 5) for the
spectral component, rather than the larger sample counts semantic-entropy
style methods typically use, and it does not require white-box access —
only sampled generations and an embedding model.[^c3]

## Limits

- The comparison is a ranking metric (AUROC); the paper studies "confidence
  estimation as a ranking problem... not to produce calibrated
  probabilities," so HY@p's advantage says nothing about its calibration
  against [[calibration]]-style targets.[^c4]
- The margin over VN@10 is small and only one-sided significant
  ($p=0.07$) — a comparison, not an established superiority.
- Verbal confidence is known from prior work to saturate near 80–100%
  confidence even when accuracy is lower; HY@p inherits that component's
  weakness whenever the spectral term does not disagree with it.
- Evaluated only on short-answer/MCQ and math benchmarks under
  correctness labels taken from a single sampled answer, not on
  open-ended, unscoreable design questions.

## Related

[[pool-uncertainty-propagation]] · [[semantic-entropy]] · [[abstention]] · [[sequence-likelihood-confidence]]

[^c1]: sharma-2026 — "a hybrid estimator that combines verbal confidence with spectral answer diversity computed from the negative von Neumann entropy of sampled answer embeddings"
[^c2]: sharma-2026 — "V C is weakest (0.689 avg AUROC), V N @10 a clear step above (0.737), and H Y @5 the strongest (0.752)."
[^c3]: sharma-2026 — "This is cheap, requiring only one generation per query but often suffers from overconfidence and score saturation."
[^c4]: sharma-2026 — "We study confidence estimation as a ranking problem, that is, the goal is to assign scores that separate likely-correct from likely-incorrect outputs, not to produce calibrated probabilities."
