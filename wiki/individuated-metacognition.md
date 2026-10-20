---
description: "Across 20 frontier LLMs and six benchmarks, binary confidence judgements collapse to a shared item-difficulty axis rather than tracking each model's own per-item capability."
aliases: ["individuated metacognition", "functional metacognition", "metacognitive monitoring"]
sources: ["moran-2026", "arxiv-2512-18880"]
---
# Individuated metacognition

> Confidence-gated routing, [[abstention]] and ensemble weighting all assume a
> model's stated confidence tracks *its own* per-item capability. Across 20
> frontier LLMs and six benchmarks, it mostly does not: confidence collapses
> to a factor shared across models, and models differ chiefly in where they
> set their threshold on it.

## Definition / Mechanism

Moran & Whiting (2026) define the object directly: "A model's
capacity to assess its own capabilities at the item level in a way specific
to that model, without exercising those capabilities, beyond what is
explained by a shared signal."[^c1]

They decompose binary yes/no confidence judgements from 20 frontier LLMs
across six benchmarks (SQuAD, MMLU-Pro, LegalBench, MathBench, Omni-MATH,
SciCode) using tetrachoric factor analysis paired with pairwise [[calibration]]
(Kendall-τ between model pairs). On factual, retrieval and legal tasks the
cross-model confidence matrix is approximately rank-one: "Models retrieving
facts share an item-level difficulty axis and differ mainly in their
decision thresholds along it," and "We find no evidence for significant
verbalised individuated metacognition in any tested domain."[^c2]

Pairwise calibration between models is statistically significant but tiny,
and disappears once each model's own accuracy base rate is controlled for:
"The statistically significant but minor effect size vanishes when
controlling for differences in performance base rate... one model being
more confident than another has near-zero correlation with performance
beyond what is explained by performance base-rate differences."[^c3]

Mathematical reasoning looked like an exception — pairwise calibration
survived at matched accuracy — but this resolves to a confound: "The
apparent MathBench exception to the pairwise-calibration result collapses
on closer inspection. The signal is concentrated entirely in
Reasoning–Non-Reasoning pairs, where reasoning-trained models attempt the
problem inline when asked about confidence," a symbolic work-around rather
than the sub-symbolic self-knowledge the measure targets.[^c4]

The same shape appears when the question is item difficulty rather than confidence. In a study of over 20 LLMs on educational items, models agree with each other more than they agree with human field-test difficulty: "where models exhibit relatively stronger alignment with each other".[^c7] Their explicit difficulty estimates are also weak at predicting their own errors. The AUROC of predicted difficulty against the model's own incorrect answers is near chance, and "Most models hover near 0.55," so the explicit estimate is effectively decoupled from the model's own correctness.[^c8][^c9] The two studies measure different objects, a yes/no confidence judgement here and a graded difficulty estimate there, so their agreement is a parallel, not a replication (my inference).

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| LLM evaluation (this paper) | individuated metacognition | exact — Definition 1.1, the object measured |
| LLM evaluation (this paper) | functional metacognition | exact — same capacity, used before the formal definition is given |
| Cognitive science (Nelson & Narens 1990, cited by the source) | metacognitive monitoring | close — the human-cognition antecedent this paper narrows its attention to; no test in this source establishes equivalence to the human construct |

## Why it matters

A question-selection or abstention rule that gates on a model's own stated
confidence — "ask again / escalate / abstain when this model is unsure" —
is gating on a signal this source finds carries little model-specific
information beyond a difficulty axis every model in the population already
agrees on. Where models disagree on an item (the case a selection or
abstention rule is meant to catch) the confidence signal and the
performance signal are shown to be largely independent, so the premise
behind confidence-triggered abstention on stall 2 does not hold in the
population and benchmarks this source tested.

## Transfer

| | |
|---|---|
| **Home field** | Psychometrics: tetrachoric correlation on binary item responses, then factor analysis, to recover a latent ability/difficulty structure from test-takers' item scores |
| **Here** | Applied to binary confidence judgements from 20 LLMs across six benchmarks, treating each model as a respondent to a "confidence test" rather than a correctness test |
| **What survives** | the latent-variable decomposition itself, and the diagnosis that a single dominant factor (rank-one structure) accounts for most cross-model variance |
| **What does not** | the bivariate-normal latent-trait assumption the tetrachoric method rests on, which the paper says "is presumed rather than tested" and "almost certainly wrong" on the Gaussian assumption |

[^c5]

## Limits

This note's claim rests on binary, single-shot, temperature-zero confidence
elicitation. The source states: "we elicit one binary yes/no judgement per
(model, item) trial at temperature 0. On uncertain items this masks the
variance in the model's responses at higher temperature."

A graded or
sampled confidence protocol, or a different elicitation prompt, could
recover more individuated structure than binary elicitation does; the
source's own related work notes reasoning-trace text carries information a
model's binary judgement does not use (its §3.4/§A.1), so absence of signal
in the binary channel is not evidence the model lacks the underlying
information. Six benchmarks and 20 models, none of them audited for
benchmark contamination by this note.[^c6]

## Related

[[semantic-entropy]] · [[confidence-calibrated-cascade-judgment]] · [[calibration]] · [[expected-information-gain]]

[^c1]: moran-2026 — "A model’s capacity to assess its own capabilities at the item level in a way specific to that model, without exercising those capabilities, beyond what is explained by a shared signal."
[^c2]: moran-2026 — "Models retrieving facts share an item-level difficulty axis and differ mainly in their decision thresholds along it."
[^c3]: moran-2026
[^c4]: moran-2026 — "The apparent MathBench exception to the pairwise-calibration result collapses on closer inspection. The signal is concentrated entirely in Reasoning–Non-Reasoning pairs, where reasoning-trained models attempt the problem inline when asked about confidence."
[^c5]: moran-2026 — "The tetrachoric latent-normality assumption is presumed rather than tested. The bivariate-normal latent model is almost certainly wrong on the Gaussian assumption, and base-rate noise in the marginals isn’t modeled so inflates dimensionality for extreme base rates."
[^c6]: moran-2026 — "We elicit one binary yes/no judgement per (model, item) trial at temperature 0. On uncertain items this masks the variance in the model’s responses at higher temperature."
[^c7]: arxiv-2512-18880 — "where models exhibit relatively stronger alignment with each other"
[^c8]: arxiv-2512-18880 — "Most models hover near 0.55,"
[^c9]: arxiv-2512-18880 — "find that explicit difficulty estimates are effectively decoupled from the model"
