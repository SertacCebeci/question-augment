---
description: "A closed-form, training-free Gaussian log-determinant estimator of semantic progress in embedding space, provably monotone and telescoping across turns, submodular in redundant evidence."
aliases: ["GaussianIG", "Gaussian information gain"]
sources: ["he-2026"]
---
# Gaussian information gain (GaussianIG)

> The estimator [[semantic-progress]] cannot compute directly: turn answers
> are embedded, folded into a running Gaussian precision matrix, and the
> log-determinant drop is the turn's information gain.

## Definition / Mechanism

Each answer $a_t$ is split into evidence strings, embedded, and each
embedding contributes a question-relevance-weighted rank-one update to a
running precision matrix $J_t$. Modelling the latent semantic state as
Gaussian with covariance $\Sigma_t = J_t^{-1}$, the turn-level gain is
$\widehat{IG}_t = \tfrac12\log(\det\Sigma_{t-1}/\det\Sigma_t)$, and the
dialogue-level score is $\hat P_q(D_{1:T}) = \sum_{t=1}^T \widehat{IG}_t$.
He, Kasiviswanathan & Janzing (2026) motivate the
log-determinant specifically as the maximum-[[entropy]] choice once only
second-order (covariance) structure of the evidence embeddings is
retained, their closed-form updates running entirely in embedding space
without autoregressive inference.[^c1]

Because each update is a nonnegative-definite rank-one addition to
precision, posterior covariance can only shrink: the authors prove
$\Sigma_t \preceq \Sigma_{t-1}$, hence $\widehat{IG}_t\geq0$ for every turn,
and the per-turn gains telescope into $\sum_t \widehat{IG}_t =
\tfrac12\log(\det\Sigma_0/\det\Sigma_T)$ — the total score depends only on
the first and last covariance, not the path between them.[^c2]

Treating the accumulated weighted outer products as a set function
$F(S)=\log\det J(S)$, the authors prove $F$ is monotone submodular, so
adding evidence similar to what is already accumulated yields a strictly
smaller marginal gain than adding it earlier — the formal mechanism by
which the score discounts redundant or repeated evidence rather than
rewarding verbosity.[^c3]

## Why it matters

On MT-Bench, Chatbot Arena and UltraFeedback dialogue-pair preference data,
GaussianIG (a 0.6B embedding model, CPU-only) reached 84.03%, 65.80% and
71.64% agreement with the human-preferred dialogue respectively —
comparable to or above six evaluated LLM-as-judge baselines (Mistral Large
3, DeepSeek R1, GPT-OSS-120b, three Claude Sonnet variants) — while running
3-10x faster (e.g. 86s vs. 132-633s on MT-Bench for 100 pairs over 5 runs).

## Transfer

| | |
|---|---|
| **Home field** | Gaussian/max-entropy information theory: log-determinant of a covariance matrix as differential entropy, precision updates from conjugate Gaussian observation models |
| **Here** | sentence-level dialogue evidence embedded by a fixed text encoder, folded into a running precision matrix with question-relevance weights standing in for a likelihood |
| **What survives** | the monotonicity, telescoping and submodularity guarantees — proved directly for this embedding-space construction, not inherited by analogy |
| **What does not** | any claim that the log-determinant score equals or bounds the true semantic information $I(W;A_T\mid q)$ for actual natural-language evidence; the paper's own information-theoretic bound (their Theorem 1) holds only under an assumed common empirical covariance and an unverified entropy floor |

## Limits

- Agreement numbers are correlational: the metric is validated by how well
  its ranking matches a majority human preference vote, not by recovering
  $P_q^\star$ or any ground-truth uncertainty about $W$.
- The relevance weights and question-conditioning are themselves
  embedding-similarity heuristics, not a modelled likelihood; errors in the
  embedding model propagate directly into the score.
- Evaluated as agreement with *holistic* preference votes (fluency, safety,
  style included) even though the metric targets only semantic progress —
  the paper itself flags this as a conservative, not a clean, test.[^c4]

## Related

[[semantic-progress]] · [[mutual-information]] · [[expected-information-gain]] · [[semantic-entropy]]

[^c1]: he-2026 — "approximation in embedding space with closed-form updates and guarantees of monotonicity,"
[^c2]: he-2026 — "posterior uncertainty can only decrease. This gives monotonicity and a telescoping dialogue-level"
[^c3]: he-2026 — "Theorem 3 (Diminishing Returns). Assume J0 ≻ 0. The set function F is monotone submodular."
[^c4]: he-2026 — "• Empirical validation at scale. On MT-Bench, Chatbot Arena, and UltraFeedback, G AUS SIAN IG reaches 84.03%, 65.80%, and 71.64% agreement, respectively, while reducing"
