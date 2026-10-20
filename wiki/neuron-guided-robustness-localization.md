---
description: "Attribution finds the small FFN neuron set that separately processes relevant vs. irrelevant context; those neurons anchor separate training for abstention and extraction."
aliases: ["NeuRIT", "Neuron-guided Robust Instruction-Tuning", "context-aware neuron mining"]
sources: ["arxiv-2604-02194"]
---
# Neuron-guided robustness localization

> Abstention and evidence extraction are not one skill trained at once —
> they live in different, mostly non-overlapping neurons, and can be
> taught to each separately.

## Definition / Mechanism

A retrieval-augmented answerer facing noisy context needs two distinct
behaviors: abstain when the retrieved context is uninformative, and
selectively extract the answer when it is buried in irrelevant material.
Prior instruction-tuning methods train one objective for both and adapt
whole layers or modules, "overlooking that only a small subset of
neurons is strongly activated for a given input."[^c1]

Lee, Kim, Ahn & Park (2026) locate that subset
directly. For each query they build a (query, relevant-document,
irrelevant-document) triplet and score every FFN neuron's contribution
to the prediction with Integrated Gradients, comparing the neuron's
activation with and without the document. Per query they keep the top
20 highest-scoring neurons, then take the neurons most frequent across
all queries, separately for relevant and irrelevant documents: "Initial
mining yields 7,380 relevant and 7,036 irrelevant candidate neurons"
with "6,240 overlapping neurons".[^c2]

Overlap neurons respond to both context types and so carry no
discriminative signal, so they are pulled into a third, shared set and
removed from the other two: the final sets are 100 relevant-aware, 100
irrelevant-aware, and 30 shared neurons.[^c2]

These three neuron groups then anchor a two-stage instruction-tuning
regime rather than a single combined one. First, a denoising stage
updates only the irrelevant-context-aware neurons, training them to
"emit an End-of-Text (EOT) token" — abstain — whenever the retrieved
context is uninformative, under "a hard constraint that decouples these
irrelevant context-aware neurons from generation" so they cannot also
participate in extracting an answer.[^c3]

Second, a noise-filtering stage adapts all three neuron groups together
with the top-3 transformer layers where those neurons are most densely
concentrated, teaching the model to extract the answer when it is mixed
with distracting context. Two ablations show both the separation and
the localization are load-bearing. Removing either stage hurts: average
accuracy across five QA benchmarks drops from 68.46 to 66.38 without
denoising, and to 61.18 without noise-filtering — below the untrained
baseline's 62.08, i.e. abstention training alone, applied without a
paired extraction stage, over-suppresses useful evidence. Replacing
the mined neurons and their densest layers with randomly sampled
neurons of matched group sizes, then tuning the layers those land in,
reaches only 63.73 average accuracy against 68.46 for the mined
selection — the localization signal, not merely tuning a few layers, is
what drives the gain.[^c5]

The mined neurons also transfer across retrievers: neurons mined with
one retriever (SPLADE-v3) and reused unchanged at inference with a
different one (Contriever) still outperform baselines evaluated under
that same retriever, without re-mining.[^c6]

## Why it matters

This gives commitment a mechanistic, not just behavioral, account: the
decision to abstain versus to commit and extract is not one scalar
threshold on a hidden confidence signal but sits on a structurally
separable subset of parameters, small enough (100–130 neurons plus
three layers, in an LLM with far more) to be trained in isolation from
the rest of the network's competence.

## Limits

- Evaluated up to 14B-parameter open-source backbones only; whether the
  same neuron sparsity and localization hold at 30B–70B scale is
  unexplored — the paper names this as its own limitation.
- The mining triplet needs a top-ranked relevant document and a
  zero-relevance-score irrelevant document per query; the method has not
  been shown to work from noisier, real retrieval output alone.
- Neuron sets are mined once per generator backbone on one training
  distribution (HotpotQA); generalization of the *mined neurons
  themselves* (as opposed to the trained behavior) to other domains is
  not measured here — only the resulting model's accuracy is.
- The two group sizes (100/100/30) and the "top 20 per query" cutoff are
  hyperparameters set by inspection; a budget sweep found accuracy
  stable within 0.31 points across a 2x range, but the underlying
  selection frequencies were not validated against a held-out cutoff.

## Related

[[abstention]] · [[gated-activation-steering-for-abstention]] ·
[[compression-aware-abstention]]

[^c1]: arxiv-2604-02194 — "model at a coarse layer- or module-level granularity, overlooking that only a small subset"
[^c2]: arxiv-2604-02194 — "Initial mining yields 7,380 relevant and 7,036 irrelevant"
[^c3]: arxiv-2604-02194 — "emit an End-of-Text (EOT) token under irrelevantcontext inputs. Since Pirrel are identified as primarily responsible for processing irrelevant or misleading contexts, allowing them to participate in"
[^c5]: arxiv-2604-02194 — "this Random layer selection (Random layer sel.)"
[^c6]: arxiv-2604-02194 — "Table 5, the SPLADE-v3-mined neurons remain"
