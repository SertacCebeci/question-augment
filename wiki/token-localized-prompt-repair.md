---
description: "Repair an input token by token: score each span against harmful and benign reference lists, substitute only the flagged spans, and leave the rest of the request intact."
aliases: ["token-wise purification", "risk-localized prompt sanitization", "selective embedding replacement"]
sources: ["arxiv-2512-23546"]
---
# Token-localized prompt repair

Some requests are unsafe in only a few words. A filter that acts on the whole input has two options: pass it through, or replace all of it. PurifyGen's argument is for a third option: find the risky part and repair only that part, so the rest of the request survives. The paper states the premise directly: "the objectionable meaning is concentrated in a handful of words".[^c1] A blanket change, "whether by masking every token or applying a uniform" replacement, damages the fluency of the rest.[^c2]

**Mechanism.** The method works in a text-to-image model's prompt embedding space and needs two reference lists, one toxic and one clean, each turned into a matrix of concept embeddings. For each token embedding, the paper computes a "complementary semantic distance" to each list, the residual left outside that concept subspace.[^c14] A token is labelled risky when it is nearer the toxic list than the clean one.[^c3] The authors argue for residuals over direct similarity: "Merely checking the cosine similarity between a token and the" toxic anchors is unreliable, and what is needed is "a score that reflects the residual information that survives" outside each concept subspace.[^c4]

Only the risky tokens are then transformed. The toxic component is removed by projecting into the null space of the toxic matrix, which "suppresses any components that align with toxic semantics", and a clean component is added by projecting into the range of the clean matrix, which "reinforces" alignment "with safe, desirable semantics".[^c5] Risky embeddings are swapped for their sanitized counterparts, and "ones remain untouched to preserve fidelity".[^c6] The paper contrasts this with methods that "indiscriminately suppress or remove toxic cues".[^c7]

**What transfers.** The reusable idea is the shape, not the linear algebra. A repair can be confined to the flagged span; the span can be scored against a harmful reference and a benign reference together, not against a harmful list alone; and the unflagged remainder is left byte-for-byte as it was. A refusal-or-pass decision on the whole request is then one special case of a larger space of edits (my inference). The same locality appears on the attacker's side: [[script-level-obfuscation]] rewrites a sensitive span while keeping its intent, and a defence that localizes the span is the mirror of that move. The idea of a minimal set of changed tokens as the unit of repair is also close to [[minimal-patch-edit-label]].

**Measured results.** On Stable Diffusion v1.4, against adversarial prompts, the full method posts the lowest attack success rate among training-free baselines, "ASR across every attack variant, eclipsing all other training-free" methods.[^c8] The ablation reports that "all variants substantially reduce the performance from adversarial prompts", so each module contributes something on the attack side.[^c9] These are attack-success numbers; they say the repaired prompt generates fewer unsafe images, not that it means the same thing.

## Limits

- The evaluation is one model (SD v1.4), tested "with adversarial prompts sourced from five red-teaming pipelines".[^c10] Nothing shows the localization carries to other generators, to language models answering questions, or to prompts the red teams did not write.
- Intent preservation is measured by FID, CLIP and TIFA on about a thousand COCO captions, which are mostly benign.[^c11] No measure checks that a repaired risky span still asks the same thing when the risky prompt is the input. That the rest of the request is kept is inferred from the image metrics, not shown.
- The risk score depends on user-defined lists: each concept is "the embedding of the relevant text associated with the user-defined" concept.[^c12] A span is only as well localized as the lists are complete; my inference is that a missing harmful concept gives a silent false negative, and this is not tested.
- The output is a sanitized embedding, not a sentence. A human asker cannot reproduce the repair by rewording, and the paper gives no natural-language rewrite of its own examples. Transfer to asking is therefore a claim about the principle (localize, then substitute), not about the procedure.
- The formal setup is loose. The paper defines the null space of a concept matrix as a subset of a different space from the one the matrix lives in, and it computes "the null space of the covariance matrix of the prompt" in one sentence and takes an SVD of the concept matrix in the next.[^c13] My reading is that the definitions and the procedure do not match exactly, so the geometry should be taken as motivation rather than as a verified derivation.
- The abstract claims "theoretical grounding", but the paper offers no bound on how often the residual score misclassifies a token.[^c15]

## Related

- [[script-level-obfuscation]] — the attacker's version of a local, intent-keeping rewrite of a sensitive span
- [[minimal-patch-edit-label]] — the minimal set of changed tokens as a label for where a repair belongs
- [[reward-model-bias-linear-tractability]] — the same null-space projection used to remove one linear direction, with the same limit that a single direction does not always carry the concept

[^c1]: arxiv-2512-23546 — "the objectionable meaning is concentrated in a handful of words"
[^c2]: arxiv-2512-23546 — "whether by masking every token or applying a uniform"
[^c3]: arxiv-2512-23546 — "concepts are flagged as risky"
[^c4]: arxiv-2512-23546 — "Merely checking the cosine similarity between a token and the"
[^c5]: arxiv-2512-23546 — "suppresses any components that align with toxic semantics"
[^c6]: arxiv-2512-23546 — "ones remain untouched to preserve fidelity"
[^c7]: arxiv-2512-23546 — "remove toxic cues, our approach offers a more fine-grained and"
[^c8]: arxiv-2512-23546 — "ASR across every attack variant, eclipsing all other training-free"
[^c9]: arxiv-2512-23546 — "substantially reduce the performance from adversarial prompts"
[^c10]: arxiv-2512-23546 — "with adversarial prompts sourced from five red-teaming pipelines"
[^c11]: arxiv-2512-23546 — "the CLIP similarity score for semantic alignment"
[^c12]: arxiv-2512-23546 — "embedding of the relevant text associated with the user-defined"
[^c13]: arxiv-2512-23546 — "compute the null space of the covariance matrix of the prompt, and"
[^c14]: arxiv-2512-23546 — "We employ the complementary semantic distance to gauge"
[^c15]: arxiv-2512-23546 — "with theoretical grounding"
