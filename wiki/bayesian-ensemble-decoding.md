---
description: "Compresses K document-conditioned generation branches into one answer by weighting each token with a document posterior updated via Bayes' rule."
aliases: ["BERAG", "Bayesian Ensemble Retrieval-Augmented Generation", "Bayesian Ensemble Fine-Tuning", "BEFT", "document posterior ensemble decoding"]
sources: ["arxiv-2604-22678"]
---
# Bayesian ensemble decoding

> Compresses K document-conditioned generation branches into one answer by weighting each token with a document posterior updated via Bayes' rule.

## Definition / Mechanism

Chen et al. (2026) give a query $x$ and $K$ retrieved
documents $Z=[z_1,\dots,z_K]$: the standard way to distil them into one
answer concatenates all of $Z$ into a single context and decodes once
([[compound-ai-systems|ConcatRAG]]). Bayesian ensemble decoding instead
runs $K$ parallel generation branches,
one per document singleton $z_k$, and marginalizes the next-token
probability over branches at every step:

$$P(y_j|y_{<j},x,Z) \approx \sum_{k=1}^{K} P_\Theta(y_j|y_{<j},x,z_k)\,P(z_k|y_{<j},x,Z)$$

The mixing weight is a **document posterior**, not a fixed or retriever-only
score: it is computed by [[bayesian-estimation|Bayes' rule]] from a document
**prior** — a learned two-layer MLP over the model's last-token embedding
for $(x, z_k)$ — and the running likelihood of the generated tokens so far
under $z_k$: document posterior probabilities are ensemble weights updated
token by token using Bayes' rule during generation.
[^c1]
The document posterior is computed via Baye's rule.
[^c2]

$$P(z_k|y_{<j},x,Z) = \frac{P_\Theta(y_{<j}|z_k,x)\,P_\Theta(z_k|x,Z)}{\sum_{k'} P_\Theta(y_{<j}|z_{k'},x)\,P_\Theta(z_{k'}|x,Z)}$$

Each generated token therefore *updates the weight of the evidence it came
from*: a branch whose document keeps explaining the tokens well gains
posterior mass; one that stops explaining them loses it. Compression is not
a single pooling step over static scores but a Bayes-filtered mixture that
is re-evaluated at every token of the output. The weights come from an
end-to-end trained system (Bayesian Ensemble Fine-Tuning, BEFT) rather than
being read off a fixed retriever score or a heuristic (entropy, contrastive
logits) applied post hoc to a frozen model.

Because each branch conditions on only one document, ordering in the
retrieval list cannot bias which tokens get attended to first: the work
reports the mechanism is unaffected by document ordering and therefore
immune to the "lost-in-the-middle" effect.[^c3]

A finite candidate set also lets one slot be reserved for a "no-evidence"
document $z_0$, so the same number that distils the answer also detects
when no retrieved document explains the query — deflection is issued when
$z_0$ holds the highest posterior, not decided by a separate prompted
judgment.[^c4]

## Why it matters

It separates two things a single concatenated context conflates: *how much
of the answer came from which piece of evidence* (the posterior, an
attribution) and *what the answer is* (the marginal, the distillate). The
posterior is not decoration — it is load-bearing for three downstream uses
in this note's source: ordering-invariance, abstention, and inference
pruning (documents whose cumulative posterior mass is negligible can be
dropped without changing the marginal, giving decode time that stays
constant in $K$).
[^c6]

## Limits

The posterior-weighted mixture is **not training-free**: applying it to a
model pretrained only for concatenative RAG gives weak performance, because
the model was never trained to have its per-branch token probabilities
combined this way — end-to-end fine-tuning (BEFT) is required.
[^c5]
Naive (unpruned) decoding is slower than concatenation, since the $K$
branches' KV caches together exceed one concatenated cache; the speed
advantage depends on the pruning heuristic. And the marginalization is
only over document *singletons* — it does not model the powerset of
document combinations, so an answer that genuinely requires synthesizing
two documents jointly is approximated by two independent single-document
branches, which the source itself flags as a place its synthesis ability
is limited.
[^c7]

## Related

[[bayesian-estimation]] · [[compound-ai-systems]] · [[data-processing-inequality]] · [[abstention]] · [[entropy]]

[^c1]: arxiv-2604-22678 — "BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes’ rule during generation."
[^c2]: arxiv-2604-22678 — "where the document posterior P (zk |y<j , x, Z) is computed via Baye’s rule"
[^c3]: arxiv-2604-22678
[^c4]: arxiv-2604-22678 — "For BEFT systems, deflection is issued when z0 has the highest posterior (Eq.3), not via prompting."
[^c5]: arxiv-2604-22678 — "We find that BEFT training is required to obtain strong performance with BERAG decoding."
[^c6]: arxiv-2604-22678 — "We find that BERAG with Top-P pruning is gives decoding time that is constant in K and is faster than that for RAG (44.4 ms/tok v.s. 203.0 ms/tok at K = 50)."
[^c7]: arxiv-2604-22678 — "it is likely that this ability can be improved by considering the ensemble over all document combinations (i.e., marginalize over the powerset of Z) compared to over document singletons."
