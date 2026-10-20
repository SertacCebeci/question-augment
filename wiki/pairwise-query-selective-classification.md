---
description: "Ranks which points to send to a human by an extra pairwise self-query instead of raw confidence, because a classifier's confidence and its true labeling function can be uncorrelated."
aliases: ["PairSel", "pairwise-query selective classification", "pairwise self-querying"]
sources: ["vardhan-2026"]
---
# Pairwise-query selective classification

> When a classifier's own confidence cannot be trusted to rank its errors, ask
> it a second, cheaper question — which of two points is closer to the
> positive label — and sort by the answers instead.

## Definition / Mechanism

Vardhan, Choudhary, Modani & Mazumdar (2026) find that for
in-context binary classification with LLMs (verifying NL2SQL outputs), a
classifier's next-token confidence $p_{clf,c}$ can be nearly uncorrelated
with its own labeling function $p_{clf,l}$ — the softmax peak and the
function actually driving predictions diverge, so thresholding on confidence
(**ConfSel**) rejects the wrong points. They propose **PairSel**: a *pairwise
query oracle* returns, for two unlabeled points $x,x'$, which one is closer
to label 1; comparison-sort (e.g. Mergesort, $O(n\log n)$ queries) over this
oracle produces a ranking by $p_{clf,l}$ without ever estimating it directly.
Five rejection rules read off this ranking — Middle, Max-[[entropy|Entropy]],
Max-Presence, Max-Displacement, kNN — the simplest, **PairSel-Middle**,
rejects the $\alpha$-fraction of points landing in the middle of the sorted
order, on the assumption that a balanced classifier is least confident there.[^c1]

Under a classifier assumption (a feature map $\varphi$ with unit-norm linear
weights and a monotone link $g$ — satisfied by linear, generalized-linear,
and wide neural-tangent-kernel models) and a feature distribution (spherical
or Gaussian), Theorem 4 and Theorem 5 give a sufficient condition on the
inner products between the true, human, confidence and labeling weight
vectors under which PairSel-Middle's population selective risk is lower than
ConfSel's.[^c2]

Across a synthetic dataset and four in-context LLM tasks (NL2SQL
verification on Spider and Bird, binary QA on BoolQ and VisOnlyQA, LLM
classifiers under 10B parameters), the best pairwise method reaches total
accuracy at least 8% higher than raw next-token-logit thresholding at some
rejection fraction, with the gain ranging from about 3% (Spider, where the
raw baseline is already near 90%) to about 16% (the harder Bird dataset).[^c3]

## Why it matters

This is a self-querying policy for stall 2: instead of trusting a single
self-reported confidence to decide which point needs an external answer
first, the asker puts a second, structurally different question to itself
(a comparison, not a magnitude) and ranks by that — a concrete case of
using an extra self-query as a better error detector than the model's own
stated uncertainty.

## Transfer

| | |
|---|---|
| Home field | [[abstention|selective classification]] for in-context LLM binary classifiers — one classifier, one fixed pairwise-query oracle, a human annotator as the only other source of ground truth |
| Here | ranking which uncertain point (axis) to raise for an external answer first, when the asker's own confidence signal cannot be trusted |
| What survives | the core move — trade a magnitude self-query (confidence) for a comparison self-query (pairwise), because comparisons can be more reliable than direct estimates from the same source |
| What does not | the risk guarantee (Theorem 4/5), which needs a linear/GLM/NTK classifier structure and a named feature distribution; PairSel-Middle's balanced-class assumption; the pairwise-query oracle's assumed perfect consistency (Definition 1), which real self-queries do not have |

## Limits

- The theoretical guarantee (Theorem 4/5) rests on Assumption 3: predictions
  are $g(\langle w,\varphi(x)\rangle)$ for some feature map and unit-norm
  weight vector, and features are spherical or Gaussian — it says nothing
  about when a classifier or self-querying oracle does not fit this
  structure.[^c4]
- The pairwise query oracle (Definition 1) is assumed to always answer
  correctly; the paper motivates this only by citing that LLMs are more
  accurate on pairwise comparisons than on direct labels on some tasks, not
  by bounding the oracle's own error rate.[^c5]
- All empirical gains are measured on binary classification/verification
  tasks with classifiers under 10B parameters; the paper does not test
  open-ended answers or larger models.[^c6]

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]] · [[value-of-information]]

[^c1]: vardhan-2026 — "To remedy this, we propose making additional pairwise queries to the same model. These pairwise queries can detect high-error samples and be incorporated into selective classification techniques to reduce the error on nonrejected samples."
[^c2]: vardhan-2026 — "we derive the necessary theoretical conditions under which the simplest of our pairwise algorithms, Pair-Middle, outperforms vanilla confidence thresholding for spherical (Theorem 4) and Gaussian features (Theorem 5)."
[^c3]: vardhan-2026 — "the best pairwise methods have total accuracy atleast 8% higher than the raw baseline, which corresponds to next-token logits (Synthetic, Bird and BoolQ)"
[^c4]: vardhan-2026
[^c5]: vardhan-2026
[^c6]: vardhan-2026
