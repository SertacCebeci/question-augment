---
description: "The Vendi score reads a set as an effective count of distinct members: exp of the Shannon entropy of a similarity matrix's eigenvalues, from 1 for identical items to set size for unrelated ones."
aliases: ["Vendi score", "Vendi diversity", "effective number of distinct items"]
sources: ["arxiv-2512-23601"]
---
# Vendi score

Counting distinct items in a generated set needs a rule for when two items are the same. The Vendi score replaces the yes-or-no rule with a graded one. Given a set of items and a pairwise similarity matrix over them, it returns a number that behaves like a count of distinct members. In the paper's words, "compute the Vendi Score as the exponential of the Shannon entropy of its eigenvalues."[^v1] The range is stated as: "it ranges from 1 (all tasks identical) to |S| (all tasks dissimilar)."[^v2] So a set of identical items scores 1, a set of mutually unrelated items scores its size, and a set in between scores somewhere between.

The mechanism is spectral. A similarity matrix that is close to all-ones (every item like every other) has one dominant eigenvalue, and its entropy is low, so the exponential is near 1. A matrix close to the identity (every item unlike every other) has a flat spectrum, and its entropy is near log of the set size, so the exponential is near the size. The score is the number of equally weighted directions the set spans, measured through the eigenvalues. In the paper the similarity is cosine similarity between embeddings: "each task P is represented by an embedding obtained from a model," here Qwen3-Embedding-0.6B, and "we construct a cosine similarity matrix."[^v3] The authors use the result as "the number of distinct tasks," and pair it with the utility filter in [[effective-diversity]].

## What survives the transfer

The part that carries over is the effective-number reading: exp of entropy turns a spread of weights into a count of equally weighted parts, so it can be compared across sets of different size. The paper does not write the normalization it uses; the standard form divides the similarity matrix by the set size so that its eigenvalues sum to one. That normalization is my inference from the usual definition, not something the paper states, and it is what makes the score comparable across K.

What does not carry over is the count's meaning. The score is a continuous number, not a tally of distinct things, and its value depends entirely on the similarity kernel. Two items that differ in the algorithm they require but share a theme and wording may look near-identical to an embedder, and the reverse can also happen. The score measures distinctness as the chosen embedder sees it, not as an expert or a learner would. The paper's own expert counts are higher than the automatic ones in the same setting.[^v5]

## Limits

- The paper uses the Vendi score as a proxy and says so: "This evaluation provides evidence that the automated metric we used can serve as a proxy for expert-perceived diversity."[^v4] The evidence is that the two curves have a "similar pattern" and that the expert count is "generally higher."[^v5] A higher level is not a fixed offset, and a proxy that tracks ordering is not a calibrated count.
- Only one embedder (Qwen3-Embedding-0.6B) is used. How the score changes with another embedding model, or with a different similarity kernel, is not tested in the paper.
- The score says nothing about whether items are valid or relevant. A set of distinct but broken items scores as diverse, which is why the paper restricts the count to high-utility items before applying it.
- The paper does not report a variance decomposition for the score, so the gap between methods is shown in figures with standard-error bands across contexts, not as a single measured effect size.

## Related

- [[effective-diversity]] — the utility-restricted count that this score is applied to
- [[questioning-diversity]] — average pairwise cosine distance, a simpler distinctness measure over the same kind of embedding
- [[divergent-convergent]] — a prompting split whose effect on the count is measured with this score in the paper

[^v1]: arxiv-2512-23601 — "compute the Vendi Score as the exponential of the Shannon entropy of its eigenvalues"
[^v2]: arxiv-2512-23601 — "it ranges from 1 (all tasks identical) to |S| (all tasks dissimilar)"
[^v3]: arxiv-2512-23601 — "each task P is represented by an embedding obtained from a model"
[^v4]: arxiv-2512-23601 — "This evaluation provides evidence that the automated metric we used can serve as a proxy for expert-perceived diversity"
[^v5]: arxiv-2512-23601 — "effective diversity perceived by experts has a similar pattern but is generally higher than the automated Vendi Score"
