---
description: "Persistent homology (H0) over each layer's token point cloud gives three per-layer statistics that, concatenated, classify ill-posed questions better than prompt or neuron-probe baselines."
aliases: ["H0 topology features", "finite H0 descriptors", "topology vector", "finite zero-dimensional persistent homology"]
sources: ["jiang-2026"]
---
# Persistent-homology ill-posedness detection

> Before a model generates anything, the shape of how it has contextualized a
> question's tokens already tells you whether the question is ambiguous,
> underspecified, or contradictory — and which kind.

## Definition / Mechanism

Jiang, Tang, Imani & Lan (2026) treat the contextual hidden
states of a prompt's tokens at each transformer layer as a point cloud and
characterize its geometry with finite zero-dimensional persistent homology
$H_0$, which tracks how initially disconnected token components merge as a
distance threshold increases. "We model the contextual hidden states of
prompt tokens at each transformer layer as a point cloud and characterize
its geometry using finite zerodimensional persistent homology." Each
layer's $H_0$ diagram is compressed to three scalars — mean finite lifetime
$\mu$, normalized lifetime [[entropy]] $E$, and a largest-lifetime concentration
ratio $R$ over the five largest lifetimes — concatenated across all layers
into one standardized topology vector per question, which a logistic-
regression classifier is trained on. "Each layer is summarized by three
compact descriptors: mean finite lifetime, normalized lifetime entropy, and
largest-lifetime concentration. Concatenating these descriptors across
layers yields a topology representation of the question."[^c1]

Averaged over three open-weight 7–8B models, this topology vector
outperforms a sparse-neuron [[efe-planning-as-variational-inference|ambiguity]] probe and several prompt-based
baselines on both binary ill-posedness detection and 9-way CLAMBER subtype
classification: "topology features consistently outperform prompt-based and
pooled-hidden-state baselines for ill-posedness classification, improving
average accuracy from 67.4% to 78.9% on AmbigQA, from 79.9% to 88.5% on
SituatedQA, and from 57.6% to 69.6% on CLAMBER 9-way classification."[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (interpretability / TDA) | H0 topology features | exact |
| This paper (interpretability / TDA) | finite H0 descriptors | exact |
| This paper (interpretability / TDA) | topology vector | exact |

[^c3]

## Why it matters

The CLAMBER subtypes the classifier distinguishes are themselves named by
*which* piece is missing — unfamiliar entity, contradiction, lexical
polysemy, co-reference, or an unspecified personal/temporal/spatial/task
constraint — so a working classifier is a detector for which axis is
unconstrained, read off the internal state before any answer is generated,
rather than from output behaviour.

## Transfer

| | |
|---|---|
| In its home field | topological data analysis: persistence diagrams/barcodes of a point cloud, vectorized for machine learning (persistence images, compact statistics) |
| Here | a fixed-dimensional, per-layer feature of a question's token cloud, used to detect and subtype ill-posedness before generation |
| What survives | the compact three-statistic summary (mean lifetime, lifetime entropy, concentration) as a cheap, fixed-size representation regardless of prompt length |
| What does not | any claim that the topology vector identifies *which follow-up question* to ask — it classifies the subtype label a supervised classifier was trained on, not a next-question policy |

## Limits

- Reported for three specific 7–8B open-weight models (Gemma-7B-it,
  Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3); generalization to other
  scales or closed models is untested here.
- The classifier is trained supervised on labelled ill-posedness datasets
  (AmbigQA, SituatedQA, CLAMBER); it is not a zero-shot detector.
- Requires white-box access to every layer's per-token hidden states during
  prefill, unavailable for API-only models.

## Related

[[topology-conditioned-activation-steering]] · [[semantic-entropy]] · [[gated-activation-steering-for-abstention]] · [[abstention]]

[^c1]: jiang-2026 — "We model the contextual hidden states of prompt tokens at each transformer layer as a point cloud and characterize its geometry using finite zerodimensional persistent homology."
[^c2]: jiang-2026 — "topology features consistently outperform prompt-based and pooled-hidden-state baselines for ill-posedness classification, improving average accuracy from 67.4% to 78.9% on AmbigQA, from 79.9% to 88.5% on SituatedQA, and from 57.6% to 69.6% on CLAMBER 9-way classification."
[^c3]: jiang-2026 — "finite H0 topology features consistently outperform prompt-based baselines"
