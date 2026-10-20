---
description: "A multimodal LLM that fails to name an entity freely identifies it far more often when choosing from a short candidate list; separating that step from evidence ranking improves KB-VQA without training"
aliases: ["identify-before-answer", "IBA", "open-ended naming versus candidate selection", "tip-of-the-tongue effect in MLLMs"]
sources: ["openalex-org-w7165972910", "arxiv-2512-15748"]
---
# Candidate-constrained entity identification

Ma et al. (2026) report that a multimodal LLM asked to name the entity in an image often fails, but given a small list of candidate names it picks the right one much more often. Their reading is that open-ended naming imposes a high uncertainty burden, while selecting from a set is a more tractable discriminative problem.[^c1] The model seems to hold incomplete but usable entity knowledge that free generation cannot reach.[^c2]

## Mechanism

In knowledge-based VQA, a retriever returns the top 20 candidate articles by image similarity. The model is shown the image, the candidate names and their retrieval similarity, and selects the top-j candidates; this yields an identification confidence per entry.[^c3] Only then does an off-the-shelf textual re-ranker score sections of the surviving articles against the question. The final score is a weighted sum of identification confidence, visual similarity and textual relevance.[^c4] The design decouples entity-level from section-level grounding, which most earlier pipelines fold into one re-ranking step.[^c5]

## What was measured

- E-VQA grounded questions: the correct entity was identified for 934 of 2,322 (40.2%) with candidates versus 593 of 2,322 (25.5%) with open-ended naming. On InfoSeek, 578 of 790 (73.2%) versus 362 of 790 (45.8%).[^c6]
- A proprietary model (GPT-5.2) went from 23.4% to 58.0% on the E-VQA grounded subset when given textual options.[^c7]
- Setting all fusion weights to 1 cost 0.6 points of Recall@1 on E-VQA and 2.1 on InfoSeek, so the gain is attributed to the workflow rather than weight tuning.[^c8]
- The authors say the gains come not only from better entity identification but also from more informative evidence once the entity is fixed.[^c9]

The authors compare the effect to the human tip-of-the-tongue state, but say they use it only as an intuitive analogy.[^c10]

## Limits

- The comparison is confounded in one respect (my inference): the candidate list comes from a retriever that already contains the correct entity most of the time, so the choice task is easier by construction. The paper shows the list helps, not that the model's knowledge is equal across entities.
- Candidates are drawn from a Wikipedia-style knowledge base and tested on two benchmarks (EncyclopedicVQA, InfoSeek). Other domains and noisier candidate sets are untested here.
- The identification ratios are measured on the subset of questions answerable from the ground-truth page; ungrounded questions are not covered.
- The weights were set per dataset (higher identification weight on InfoSeek), so some tuning exists despite the sensitivity check.
- The tip-of-the-tongue link is an analogy; no human data is offered.
- A candidate list can also hurt when it is handed over bare. In a visual species study, a generalist asked to pick one name from an expert's top-5 lowered mean accuracy from 59.2% to 49.7%; the gain appeared only once exemplars, confidence scores and re-ranking were added (see [[expert-shortlist-correction]]).[^c11]

## Related

- [[lost-in-generation-entity-grounding]] — another case where losing the grounding entity, not the evidence, is the failure
- [[implicit-subject-resolution-injection]] — supplying the subject entity explicitly to downstream steps
- [[dispersed-evidence-retrieval-collapse]] — retrieval failures that a staged workflow may separate
- [[expert-shortlist-correction]] — the same candidate-list move in visual species recognition, where the list alone degraded a generalist's accuracy

[^c1]: openalex-org-w7165972910 — "open-ended entity naming imposes a high uncertainty burden, whereas"
[^c2]: openalex-org-w7165972910 — "MLLMs often possess"
[^c3]: openalex-org-w7165972910 — "The MLLM is asked to assess entity relevance"
[^c4]: openalex-org-w7165972910 — "score(Si,j ) = α·ID(Pi )+β ·V(I, Ii )+γ ·T(Si,j ),"
[^c5]: openalex-org-w7165972910 — "implicitly couple these two"
[^c6]: openalex-org-w7165972910 — "(40.2%), compared to 593/2,322 (25.5%) under"
[^c7]: openalex-org-w7165972910 — "providing textual options."
[^c8]: openalex-org-w7165972910 — "The drops are"
[^c9]: openalex-org-w7165972910 — "not only from better entity identification, but also"
[^c10]: openalex-org-w7165972910 — "which we"
[^c11]: arxiv-2512-15748 — "the mean accuracy drops from 59.2% to 49.7%"
