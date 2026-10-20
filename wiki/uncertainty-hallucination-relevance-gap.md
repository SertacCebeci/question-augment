---
description: "Across 46 uncertainty estimators, 4 hallucination benchmarks and 3 LLMs, the association is weak and task-dependent; no estimator is a universally valid ask-trigger."
aliases: ["uncertainty relevance for hallucination", "estimator-hallucination association heterogeneity"]
sources: ["agnimo-2026"]
---
# Uncertainty-hallucination relevance gap

> Uncertainty estimators are widely treated as proxies for hallucination,
> but whether an estimate is high or low tracks a token/sample/self-report
> property, not a hallucination label directly — and this study measures
> how much that gap costs, dataset by dataset.

## Definition / Mechanism

Agnimo, Korba, Blangero, Chesneau & Alahari (2026) evaluate
46 white-box (information/logit-based, sample-based, internal-state,
training-based, reflexive) and black-box uncertainty estimators against
explicit hallucination targets on four datasets (RAGTruth for intrinsic,
context-faithfulness hallucination; PreciseWikiQA, LongWiki,
NonExistentRefusal for extrinsic, pretraining-groundedness hallucination)
across three LLMs, rather than assuming the association holds: "we evaluate
directly when and to what extent it holds... We find that the association
is highly variable and often weak, depending on the hallucination type and
the LLM under evaluation."[^c1]

Estimator rankings are far less stable across datasets than across models:
Kendall's τ agreement between estimator rankings is 0.10–0.15 when the
dataset changes at fixed model, versus 0.30 (RT) to 0.71 (LongWiki) when
the model changes at fixed dataset — "the dataset is the primary source of
heterogeneity in estimator rankings." Discrimination itself varies by task:
short-form QA yields strong AUROC for most estimators, long-form generation
gives uniformly moderate AUROC, and context-faithfulness/[[abstention]] give
moderate AUROC concentrated in few estimators.[^c2]

No estimator wins everywhere: "the estimators that perform best on one
dataset do not reliably remain best on another," and training-based density
estimators (Mahalanobis Distance, Relative MD, RDE) plus the
pointwise-[[mutual-information]] variants (PMI, CPMI) are "consistently among
the bottom five in nearly every panel." Among the top performers, however,
Spearman correlation analysis over the 12 dataset-model panels finds three
correlated clusters rather than 7 independent signals: a logit/sample-based
cluster (MSP, CCP, CocoaMSP, SAR; ρ ≥ 0.78 between MSP, CCP, CocoaMSP), a
black-box NLI-graph cluster (Eccentricity-contradiction,
Eccentricity-entailment; ρ = 0.36), and a singleton internal-state estimator
(AttentionScore, low correlation with both). The clusters also differ in
access requirements — logits, samples, or generated text alone — so
"selecting a few representatives from distinct groups of correlated
estimators may be preferable to relying on a single estimator or using all
available scores."[^c3]

## Why it matters

On stall 2, treating a single uncertainty score as the trigger for an
asking agent to stop and answer (or instead flag/abstain) inherits this
paper's warning at the level of the trigger's own validity: the estimator
that reliably flags hallucination on one task-model pair is not guaranteed
to flag it on the next, and the dataset — not the model — is the dominant
source of that instability. A deployed ask-trigger built on one estimator,
validated on one benchmark, is validated for that benchmark's hallucination
type and response format, not for hallucination in general. See
[[semantic-entropy]] for one of the sample-based estimators this study
places among the mid-ranked, not top-cluster, methods, and
[[ue-method-scale-dependence]] for the companion instability along model
scale rather than dataset.[^c4]

## Limits

The claim rests on four benchmarks and three 7B–13B open-weight models
(Mistral-7B-Instruct, Llama-2-7B/13B-Chat); whether the same
task-dominated heterogeneity holds for larger or closed models, or for
hallucination types outside context-faithfulness and pretraining-groundedness,
is not established here. AUROC, PRR and rank-[[calibration]] error are shown to
induce near-identical rankings in this study (median Spearman +0.97 /
−0.96), so the finding is reported on one effective discrimination metric,
not validated against calibration-style metrics independently.

## Related

[[semantic-entropy]] · [[ue-method-scale-dependence]] · [[reasoning-language-ue-bottleneck]] · [[abstention]] · [[calibration]]

[^c1]: agnimo-2026
[^c2]: agnimo-2026 — "the dataset is the primary source of heterogeneity in estimator rankings"
[^c3]: agnimo-2026 — "the estimators that perform best on one dataset do not reliably remain best on another"
[^c4]: agnimo-2026 — "the dataset is the primary source of heterogeneity in estimator rankings"
