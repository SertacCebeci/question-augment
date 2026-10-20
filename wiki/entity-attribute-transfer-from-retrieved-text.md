---
description: "Retrieved text about a look-alike entity can make a video or image answerer borrow that entity's attributes, or answer wholly about it, even when the visual entity is correctly identified."
aliases: ["entity substitution", "cross-entity transfer", "entity confusion in retrieval-augmented VQA", "deceptive grounding"]
sources: ["arxiv-2601-01513", "doi-10-48550-arxiv-2607-09349"]
---
# Entity-attribute transfer from retrieved text

A vision-language model asked a knowledge-intensive question about a video, with retrieved text added to the prompt, can fail in a specific way: the retrieved document describes an entity that is visually or semantically close to the one in the input, but not the same. The paper distinguishes two error types, which it defines by analysis and illustrates with worked examples rather than by counting.[^c1]

In the first, **cross-entity transfer**, the model identifies the entity actually shown and then applies attributes from the retrieved entity to it, "apply attributes or contextual information from the erroneous entity to the" correct one.[^c2] The paper's example is a video of a bar-backed partridge with retrieved text about the greater prairie-chicken: the draft "correctly identifies bar-backed partridg, incorrectly applies the knowledge of prairie-chicken to partridg."[^c3] The answer carries traces of the wrong entity and is inconsistent at the entity level.

In the second, **entity substitution**, "the VLM is fully influenced by the erroneous document," and the answer is grounded on the wrong entity. The paper notes that such an answer can be fluent and internally coherent while "replaces the authentic entity information with spurious attributes."[^c4]

The root cause the paper identifies is the retrieval step itself. Its ablation summary names "incorrect entity recognition in retrieved knowledge" as a major source of error.[^c5]

## What was measured

The paper adds a check on the entity. The drafter extracts the entity from the video, and each candidate answer's entity is scored by CLIP similarity against the video frames, with "the maximum similarity over all frames" taken as the alignment score.[^c6] Removing this score from the full pipeline "decreases accuracy" by 5.82% on VideoSimpleQA and 9.62% on Encyclopedic VQA, and removing both the alignment and reliability scores leaves accuracy at roughly half its full value.[^c7][^c11]

The check is not a sure separator. In the penguin case the wrong draft had the higher entity score (0.2731 against 0.2658), and the paper says that draft was caught by the earlier reliability stage instead.[^c8]

## Text-only case: deceptive grounding

The same structure appears with no image, in clinical retrieval-augmented generation. The paper calls it deceptive grounding (DG): "We term this deceptive grounding (DG)".[^c12] A DG response is one where every claim "is sourced from a real document, about the wrong entity".[^c13] In the paper's example, a query about rituximab returns documents about garetosmab; the reply cites a real trial of garetosmab, reports its outcome accurately, and says it applies to rituximab.[^c14]

Standard RAG evaluation frameworks pass such responses "by design".[^c15] NLI entailment passes them too, because the garetosmab claim is entailed by its own document.[^c16] This is a different blind spot from [[semantic-illusion]]: there the fabricated claim keeps the meaning of its evidence; here the claims are true of their source and the wrong element is the subject entity.

The mechanism is a two-stage account: "A two-stage mechanism explains cross-model variation."[^c30] Stage 1 is triggered by disease context: "Stage 1 opens when disease-context overlap activates a" parametric attribution prior.[^c17] Stage 2 sets the failure type: "when completing information is absent, Stage 2 defaults to confabulation."[^c18] Completing information is trial-level detail in the retrieved document, and it produces the jump: "R1 — Completing information creates a discontinuous jump."[^c19] An ablation that removes it reports "Entity-attribution failure dropped from 67.0% to 0.0%", while the incorrect rate rose to 98.1%, now all confabulation.[^c20] So one trigger yields misattribution when retrieval carries the detail and invention when it does not. The paper's per-claim check asks which entity each claim's source is about;[^c21] it does not cover substitution, which named-entity recognition finds.[^c22] "EAV is necessary but not sufficient."[^c23] Mapping the text-only case onto the VQA cross-entity transfer above is my inference, not the paper's.

## Limits

- The two error types come from error analysis and two case studies (Figures 2 to 4). The paper does not report how often either occurs in its benchmarks, so the prevalence of entity transfer is not measured.
- The VideoSimpleQA subset was curated to keep videos "that are clear and contain unambiguous entities."[^c9] The look-alike condition is thus under-represented by construction, and the reported accuracies do not show how often it arises in unfiltered video.
- The entity score is CLIP similarity between an extracted entity name and frames. Its agreement with human judgments of entity identity is not tested, and the penguin case shows it can rank the wrong entity higher.
- The pipeline was run with Qwen2.5-VL drafters and verifiers, retrieving k = 3 documents per query; the other VLMs appear only as baselines.[^c10]
- My inference: this is the entity-level, visually grounded case of the harm that [[distractor-similarity-reasoning-inflation]] measures at the level of reasoning tokens. The paper does not connect the two, and the similarity bins there are text-only.

- The clinical benchmark is built to be hard: "The controlled benchmark is maximally adversarial by design".[^c24] Its one production figure, "finds 7.8% overall DG", comes from a single deployed system.[^c25]
- The judge's agreement with human gold labels is reported with wide intervals: "CI is wide and should be read alongside the" precision interval, and the recall figure rests on 18 cases.[^c26] The 0% ablation result is for one model, "Completing-information ablation (n=264, L1-16B-A3B)".[^c29]
- Mitigation is partial. An entity-anchoring instruction "reduces entity-attribution failure from 36.4% to 5.7% in parametric-prior profiles"[^c27] and is near-null in other profiles; noticing the mismatch does not suffice, since "the entity mismatch still produce deceptive grounding at equivalent rates."[^c28]
- My inference: the VQA and clinical cases share the transfer step, but the completing-information gate was measured only on text. Whether it holds for retrieved visual descriptions is untested.

## Related

- [[distractor-similarity-reasoning-inflation]] — similarity-driven distractor harm measured on reasoning models; this note is the entity-level case of the same worry, with the image as the check.
- [[lost-in-generation-entity-grounding]] — evidence that loses its entity degrades answers; here the retrieved text carries a different entity instead.
- [[candidate-constrained-entity-identification]] — naming the entity from a short list in multimodal QA; a neighboring step in the same kind of pipeline.
- [[per-document-speculative-drafting]] — the paper's pipeline, which drafts one answer per retrieved document and then checks the entity against the frames.
- [[absent-entity-substitution]] — the answer-side case when the queried entity is missing; deceptive grounding is the case where the other entity's evidence is present and carried over intact.
- [[semantic-illusion]] — another check that passes a wrong answer because its meaning sits close to the context.

[^c1]: arxiv-2601-01513 — "we identify a major source of error"
[^c2]: arxiv-2601-01513 — "apply attributes or contextual information from the erroneous entity to the"
[^c3]: arxiv-2601-01513 — "incorrectly applies the knowledge of prairie-chicken to partridg"
[^c4]: arxiv-2601-01513 — "replaces the authentic entity information with spurious attributes"
[^c5]: arxiv-2601-01513 — "incorrect entity recognition in retrieved knowledge"
[^c6]: arxiv-2601-01513 — "The maximum similarity over all frames is taken"
[^c7]: arxiv-2601-01513 — "Removing the alignment score decreases accuracy"
[^c8]: arxiv-2601-01513 — "Entity score: 0.2731"
[^c9]: arxiv-2601-01513 — "contain unambiguous entities"
[^c10]: arxiv-2601-01513
[^c11]: arxiv-2601-01513 — "collapses to roughly half of the original"
[^c12]: doi-10-48550-arxiv-2607-09349 — "We term this deceptive grounding (DG)"
[^c13]: doi-10-48550-arxiv-2607-09349 — "is sourced from a real document, about the wrong entity"
[^c14]: doi-10-48550-arxiv-2607-09349 — "Attributed to rituximab."
[^c15]: doi-10-48550-arxiv-2607-09349 — "responses by design because every claim is sourced from a real document."
[^c16]: doi-10-48550-arxiv-2607-09349 — "NLI-based entailment checks also pass DG responses"
[^c17]: doi-10-48550-arxiv-2607-09349 — "Stage 1 opens when disease-context overlap activates a"
[^c18]: doi-10-48550-arxiv-2607-09349 — "when completing information is absent, Stage 2 defaults to"
[^c19]: doi-10-48550-arxiv-2607-09349 — "R1 — Completing information creates a discontinuous jump."
[^c20]: doi-10-48550-arxiv-2607-09349 — "Entity-attribution failure dropped from 67.0% to 0.0%"
[^c21]: doi-10-48550-arxiv-2607-09349 — "EAV implements this as a per-claim post-hoc check"
[^c22]: doi-10-48550-arxiv-2607-09349 — "Substitution (ES) is NER-detectable"
[^c23]: doi-10-48550-arxiv-2607-09349 — "EAV is necessary but not sufficient."
[^c24]: doi-10-48550-arxiv-2607-09349 — "The controlled benchmark is maximally adversarial by design"
[^c25]: doi-10-48550-arxiv-2607-09349 — "finds 7.8% overall DG"
[^c26]: doi-10-48550-arxiv-2607-09349 — "CI is wide and should be read alongside the"
[^c27]: doi-10-48550-arxiv-2607-09349 — "reduces entity-attribution failure from 36.4% to 5.7% in parametric-prior profiles"
[^c28]: doi-10-48550-arxiv-2607-09349 — "the entity mismatch still produce deceptive grounding at equivalent rates"
[^c29]: doi-10-48550-arxiv-2607-09349 — "Completing-information ablation (n=264, L1-16B-A3B)"
[^c30]: doi-10-48550-arxiv-2607-09349 — "A two-stage mechanism explains cross-model variation"
