---
description: "Build the answer key as a relational database first and render documents from it, so every question's answer is known by construction and scoring needs no judge or annotator."
aliases: ["paradigm inversion", "ground-truth-first generation", "generating documents from known ground truth", "regenerable corpus"]
sources: ["arxiv-2601-08847"]
---
# Ground-truth-first corpus generation

The usual order of building an evaluation runs from the documents outward. Texts are collected or written first, facts are extracted from them, and questions are asked about those facts, so each answer is whatever an annotator or a judge reads off the text. Ground-truth-first generation reverses the order. In RIKER the answer key exists before any text does: the knowledge base is "populated in a relational database before any document is generated", and "Documents are then rendered as human-readable views of this" store.[^c1] The paper names the move paradigm inversion: generating documents FROM known ground truth rather than extracting ground truth FROM documents.[^c2]

The mechanism is what the order buys. Because the facts are stored, "every question has a verifiable answer by construction, enabling deterministic scoring".[^c3] The database "serves as the authoritative answer key for all generated questions",[^c4] and questions that need computation, such as counts, sums or time relations, "can be derived from this ground truth through SQL".[^c5] Scoring then compares a response with the stored key instead of with a judge's reading: "RIKER employs answer-key-based scoring, eliminating the variability inherent in LLM-as-judge approaches".[^c6]

Two further properties follow from the same order. A corpus can be regenerated under a new seed, "different random seeds while maintaining structural equivalence", so a fresh test set costs little and a fixed one is not needed; the paper's motive is that "their fixed nature means they inevitably leak into training corpora".[^c7] Across four corpora generated from one configuration, "top-performing models showed less than 2% accuracy variance across corpora (CV < 1%)".[^c8] The documents are also rendered from templates rather than written by a language model. "RIKER avoids this through template-based generation": the stated reason is that "Smaller LLMs exhibit biases towards" their own generated data, a bias the paper says undermines validity for LLM-generated benchmarks.[^c9]

The paper claims the move is domain-agnostic: it "can be applied wherever synthetic documents can be generated from structured facts".[^c10] Its own validity claim is narrower. "RIKER makes bounded validity claims",[^c11] and what it establishes is the converse direction only: "if a system cannot extract known facts from synthetic documents, it will fail on real documents".[^c12]

## Limits

The synthetic text lacks what real corpora have. The paper says that "synthetic documents may lack certain characteristics of real-world data", and that such characteristics, including OCR errors and contradictions across sources, "are not included" in the work. Behaviour on messier corpora is untested.[^c13]

The domain is narrow. The corpora are commercial leases, field reports and HR records, and "performance on these document types may not transfer to other domains".[^c14] The language is English only; "Multilingual performance remains untested".[^c15] The stability result rests on four models and four corpora from one configuration. The paper's extension to a benchmark of any domain, that it "should exhibit similar stability properties, regardless of domain", is a conjecture here, not a measurement.[^c16]

The method fixes the answer key before the text, so it covers questions whose answers can be stored as facts. Whether open-ended answers can be keyed this way is not addressed in the passages read; that is my inference, not the paper's claim.

## Related

- [[shared-entity-pool-coherence]] — the generation step that makes cross-document questions possible at all.
- [[ground-truth-admission-test]] — another way a synthetic benchmark earns its ground truth, by passing checks against held-out behaviour.
- [[shared-completion-batching-distortion]] — why generating several records in one LLM completion distorts synthetic data; the reason for template rendering here.
- [[dormant-contamination-resurfacing]] — the leak that fixed benchmarks invite and that regenerable corpora are meant to avoid.

[^c1]: arxiv-2601-08847 — "populated in a relational database before any document is generated"
[^c2]: arxiv-2601-08847 — "generating documents FROM known ground truth rather than extracting ground truth FROM documents"
[^c3]: arxiv-2601-08847 — "every question has a verifiable answer by construction, enabling deterministic scoring"
[^c4]: arxiv-2601-08847 — "This database serves as the authoritative answer key for all generated questions"
[^c5]: arxiv-2601-08847 — "can be derived from this ground truth through SQL"
[^c6]: arxiv-2601-08847 — "RIKER employs answer-key-based scoring, eliminating the variability inherent in LLM-as-judge approaches"
[^c7]: arxiv-2601-08847 — "their fixed nature means they inevitably leak into training corpora"
[^c8]: arxiv-2601-08847 — "top-performing models showed less than 2% accuracy variance across corpora"
[^c9]: arxiv-2601-08847 — "Smaller LLMs exhibit biases towards"
[^c10]: arxiv-2601-08847 — "can be applied wherever synthetic documents can be generated from"
[^c11]: arxiv-2601-08847 — "RIKER makes bounded validity claims"
[^c12]: arxiv-2601-08847 — "if a system cannot extract known facts from synthetic documents, it will fail on real documents"
[^c13]: arxiv-2601-08847 — "synthetic documents may lack certain characteristics of real-world data"
[^c14]: arxiv-2601-08847 — "performance on these document types may not transfer to other domains"
[^c15]: arxiv-2601-08847 — "Multilingual performance remains untested"
[^c16]: arxiv-2601-08847 — "should exhibit similar stability properties, regardless of domain"
