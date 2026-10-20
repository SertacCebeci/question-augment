---
description: "Cascades a surface-form early exit with NLI conflict detection over generated answers to classify query ambiguity, trained for distractor invariance (Lee et al. 2026)."
aliases: ["ARCHIVE", "Ambiguity Recognition via Cascaded Hypothesis Inspection and Conflict VErification"]
sources: ["lee-2026-diversity"]
---
# ARCHIVE (cascaded conflict-based ambiguity detection)

> Tests whether generated candidate answers logically conflict, and skips
> the LLM call entirely when [[efe-planning-as-variational-inference|ambiguity]] is already visible in the query's
> surface form.

## Definition / Mechanism

Lee et al. (2026) cascade two stages. Stage 1: "A lightweight encoder-based
module detects surface-detectable ambiguity from the query, bypassing LLM
inference when possible" — a frozen text encoder plus a linear classifier
head estimates P(surface-detectable-ambiguous | query); above a
validation-tuned threshold the pipeline returns that label without calling
an LLM.[^c4]

Stage 2, for the rest: "the conflict modeling module generates answers,
builds and refines an NLI relation grid, and combines the grid with the
query embedding to predict arg max ŷ" — ten candidate answers are sampled
from an LLM, a frozen NLI model scores every ordered pair for
entailment/neutral/contradiction, a query-conditioned gate reweights the
three channels, and a classifier reads the flattened grid plus the query
embedding to output knowledge-dependent-ambiguous, closed-unambiguous or
open-unambiguous.[^c5]

Robustness: the classifier is trained to be invariant to one candidate
answer being replaced by an LLM-generated distractor, because "such
distractors create pointwise rather than distributed contradictions" —
genuine ambiguity spreads contradiction across the grid; a lone
hallucination does not.[^c6]

## Why it matters

On their own 4,703-query benchmark (QUIREQA), against nine baselines
([[entropy]]-over-samples, self-ask, taxonomy-guided chain-of-thought among
them): "ARCHIVE outperforms competitors, improving F1-amb by up to 10.4%
and F1-unamb by up to 21.6%, while operating 16× faster than the best
competitor" — the speed gain comes from the early-exit stage removing most
queries from the LLM-dependent path entirely.[^c7]

## Limits

- Tested with two backbones only (LLaMA-2-7B, Qwen2.5-14B-Instruct) and one
  frozen NLI checkpoint (DeBERTa-v3, Laurer et al. 2022); conflict-detection
  accuracy is bounded by that NLI model's contradiction judgement, which is
  not evaluated independently of the pipeline's end-to-end F1.
- Evaluated mostly in-distribution on the authors' own QUIREQA; the one
  out-of-distribution test is AmbigTriviaQA.
- The early-exit stage is trained on surface-ambiguity labels produced by a
  heuristic pass over the ORCAS query log; its behaviour on surface forms
  the heuristic does not cover is untested.

## Related

[[logical-conflict-ambiguity]] · [[semantic-entropy]] · [[clarification-request]] · [[ambiguity-taxonomy]]

[^c4]: lee-2026-diversity — "A lightweight encoder-based module detects surface-detectable ambiguity from the query, bypassing LLM inference when possible."
[^c5]: lee-2026-diversity — "the conflict modeling module generates answers, builds and refines an NLI relation grid, and combines the grid with the query embedding to predict arg max ŷ."
[^c6]: lee-2026-diversity — "such distractors create pointwise rather than distributed contradictions"
[^c7]: lee-2026-diversity
