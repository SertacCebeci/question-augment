---
description: "In a sample of real chatbot questions only about 13% carried a false presupposition, far below the 21-100% rates that false-presupposition benchmarks use."
aliases: ["FPQ base rate", "false-presupposition prevalence"]
sources: ["wang-2026-well"]
---
# False-presupposition prevalence

> Benchmarks for detecting a false presupposition are built almost entirely from questions that have one. Real questions mostly do not. Sizing a presupposition-check step against benchmark accuracy overstates what it is worth in deployment.

## Definition / Mechanism

Wang, Shwartz & Gonen (2026) manually annotated 100 questions sampled from WildChat (real chatbot logs) as false-presupposition (FPQ) or true-presupposition (TPQ) and found only about 13% were FPQs — against up to 100% in synthetic FPQA benchmarks (Syn-QA2), 21% reported for natural questions in Kim et al. (2021), and 25% in CREPE.[^c1]

Weighting the FPQ and TPQ accuracy scores of each tested method by this 13%/87% split (rather than the benchmark's own, much higher, FPQ share) flips which method looks best: Direct QA — which does no presupposition check at all — becomes the best-scoring method under the realistic weighting, and FP Identification, the strongest method under a benchmark's FPQ-heavy weighting, becomes the worst.[^c2]

## Why it matters

This is the base-rate term in the expected value of running a presupposition-check step at all: a check step's benefit is realized only on the ~13% of questions that need it, while its cost (see [[presupposition-verification-tradeoff]]) is paid on all of them, including the 87% that do not. A selection decision — whether to spend a turn or a module call verifying a question's presuppositions before answering — scored on FPQ-heavy benchmark accuracy is scored against the wrong prior.

## Limits

- The 13% estimate comes from 100 hand-annotated WildChat questions, one dataset, one annotation pass; it is a point estimate with no reported confidence interval or inter-annotator agreement.
- WildChat is a general chatbot log; the base rate for a domain-specific deployment (medical, legal) is not measured here and could differ substantially.
- The reweighting argument assumes the 1-5 judge scores are commensurable across the FPQ and TPQ scoring rubrics (they are designed to be symmetric but scored by an LLM judge, not verified as truly comparable).

## Related

[[presupposition-verification-tradeoff]] · [[presupposition-accommodation]] · [[value-of-information]]

[^c1]: wang-2026-well — "We found only ~13% of questions are FPQs, in contrast to much higher percents in synthetic benchmarks (up to 100%) and even the percentage reported in prior benchmarks for natural questions: 21% in Kim et al. (2021) and 25% in CREPE."
[^c2]: wang-2026-well — "Under such a weighted score, direct QA is the best method. FP identification is the worst-performing method across all datasets."
