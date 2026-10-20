---
description: "A prompt-level uncertainty score that inflates semantic entropy by cluster-brittleness features and conformally calibrates an accept/abstain threshold with a finite-sample guarantee."
aliases: ["ACSE", "Adaptive Conformal Semantic Entropy"]
sources: ["karimi-2026"]
---
# Adaptive Conformal Semantic Entropy (ACSE)

> Semantic entropy tells you the answers disagree; ACSE adds *how much to
> trust that number* and a calibrated cutoff for acting on it.

## Problem

Base [[semantic-entropy]] (normalized [[entropy]] over meaning clusters,
$u(x)\in[0,1]$) can be overconfident: a "wrong consensus" — nine of ten
resamples land on the same incorrect meaning cluster — produces low
entropy despite being wrong, and a raw threshold on $u(x)$ has no
statistical guarantee. Karimi, Meyappan & Samavi (2026) target exactly the
gap the semantic-entropy note leaves open: whether an entropy-based
threshold can be trusted to trigger [[abstention]] rather than just rank
axes.

## Definition / Mechanism

1. Sample $n$ responses per prompt with nucleus sampling; embed each with
   a sentence encoder; soft-cluster the embeddings (hierarchical
   agglomerative clustering under cosine dissimilarity) into $K$ meaning
   clusters, giving soft memberships $s_{ik}$ and a prompt-level
   distribution $P(C_k)$ over clusters.
2. Base score: normalized semantic entropy
   $u(x) = H_{sem}(x)/\log K$ for $K\ge 2$, else $0$.
3. Adjustment: five label-free, prompt-level "brittleness" features
   (dominant-cluster centroid distance, dominant-cluster internal
   dispersion, dominant-cluster sparsity relative to a [[calibration]]-set
   median, a margin-to-threshold overconfidence-suppression term, and
   $u(x)$ itself) are combined by a fixed weighted average into a
   brittleness score $B(x)\in[0,1]$, which maps through
   $\lambda(x)=2/(2-B(x))\in[1,2]$ to inflate the odds of $u(x)$ into an
   adjusted score $\hat u(x)\in[u(x),1]$; inflation is monotone and
   strictly increasing in every feature.[^c1]
4. Conformal calibration ([[conformal-prediction]]): on a held-out
   calibration set restricted to prompts whose returned (dominant-cluster)
   response was correct, set $\hat\tau$ to the $(1-\alpha)$-quantile of
   $\hat u$; at inference, accept the prompt (return the dominant-cluster
   response) iff $\hat u(x)\le\hat\tau$, else abstain. Theorem 1 of the
   paper gives $P(\hat u(x_{new})\le\hat\tau \mid E(x_{new})=0)\ge 1-\alpha$
   under exchangeability; a parallel response-level non-conformity score
   yields a prediction *set* over the sampled responses with the same
   coverage form (Theorem 2).[^c2]
5. Reported result: on TriviaQA, ACSE reaches AUROC 0.88 for
   discriminating correct from incorrect responses, against 0.65 for raw
   token entropy.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | LLM hallucination/uncertainty detection: open-domain QA with a checkable reference answer |
| **Here** | A calibrated stop signal for whether a returned answer is trustworthy enough to treat as a constraint, versus needing further asking |
| **What survives** | The two-stage structure — a cheap, label-free dispersion score, then a conformal threshold with a stated finite-sample error bound — and the specific finding that brittleness features catch "wrong consensus" cases plain entropy misses |
| **What does not** | The correctness label $E(x)$ that calibration needs: most axis or design questions this wiki treats have no single ground-truth answer to compare resamples against, so the accept/abstain rule as specified cannot be calibrated in that setting without inventing a substitute for $E(x)$ |

## Limits

- Rests on one paper (karimi-2026) not yet cross-verified elsewhere;
  benchmarked on factual QA (TriviaQA and similar), not on open-ended
  axis-selection or specification questions.
- The five feature weights in $\lambda(x)$ are a declared design choice
  ("not learned parameters"), not validated by ablation against alternative
  weightings in the slices read here.
- The coverage guarantee is conditional on $E(x)=0$ (a correct calibration
  response) and marginal over the calibration/test exchange, not a
  guarantee for any individual accept/abstain decision.
- Whether $\hat u(x)$'s ranking of *axis* questions (this wiki's stall 2)
  agrees with EIG-based ranking is untested here, exactly as for base
  semantic entropy — see [[semantic-entropy]]'s own Limits.

## Related

[[semantic-entropy]] · [[conformal-prediction]] · [[calibration]] · [[expected-information-gain]]

[^c1]: karimi-2026 — "This bounded, monotone, and order-preserving transform ensures û(x) ≥ u(x) with equality iff λ(x) = 1 or u(x) ∈ {0, 1}."
[^c2]: karimi-2026
[^c3]: karimi-2026 — "As a highlight, for TriviaQA dataset, AUROC of our approach is 0.88 compared to 0.65 produced by the token entropy approach."
