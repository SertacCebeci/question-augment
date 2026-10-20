---
description: "An LLM can encode the relation linking two entities in mid-upper layers yet fail to apply it to a new entity; the failure sits in transfer through the link, not only in encoding."
aliases: ["relation application bottleneck", "relational transfer bottleneck", "encoding-application gap in analogy", "link transfer failure"]
sources: ["arxiv-2511-20344"]
---
# Relation-application bottleneck

In a proportional analogy such as "Persuasion is to Jane Austen as 1984 is to", the answer needs two steps: extract the relation from the first pair, then apply it to the third entity. The work finds that the two steps fail separately in a language model. The relation is present in the representations of the entities in correct cases, and its absence is the mark of failure: "a significant gap is observed between these cases in terms of relational information."[^a1] Attributive information about the entity is present in both correct and incorrect cases, so the gap is specific to the relation.

Knocking out attention from the answer position to the second and third entities shows where this information is used. Blocking those positions in the mid-upper layers "leads to noticeable drops in performance."[^a2] The application step is tested by intervention. Replacing the first pair of an incorrect analogy with a correct pair of the same relation changes the answer in some cases, which the authors read as extraction failure inside the first pair; in the rest, they conclude that models still struggle to transfer relational structure.[^a3] For those remaining cases, the authors patch the representation of the second entity into the link position, the word "as". This "leads to noticeable performance gains up to 38.1%."[^a4] The reading is that the link carries the relation forward, and a failure there leaves a relation that was encoded but not passed on.

The bottleneck is therefore two-stage. A model can hold the relation and still produce the wrong entity because the relation did not reach the position that generates the answer. The conclusion states the claim in its own terms: "applying them remains a major bottleneck."[^a5] My reading is that this is a relation-level version of the timing problem [[late-entity-resolution-two-hop]] describes for a different kind of input; the work does not make that link.

## Limits

- The "relational information" measure is a containment test. A Patchscopes description counts as encoding the relation when it contains the correct relation string. Detecting the relation in a decoded description is not the same as showing the model uses it to answer.
- The percentages are "up to" figures over the incorrect cases, and the patch uses the best layer pair found by search. The gains are optimistic for an unseen case and were not cross-validated.
- The experiments use three open models (Llama-2-13B, Gemma-7B, Qwen2.5-14B) and proportional analogies only, with 500 items per condition after filtering for knowledge and shortcuts. Larger or instruction-tuned models, and other relation types, were not tested here.
- The split between "encoding" and "application" is the authors' decomposition. Replacing the first pair changes the input as well as the relation, so the two stages are not fully separated by that experiment.
- Knockout and patching locate positions and paths; they do not give the full circuit. The paper's own wording for the link is that it "may contribute to reasoning failures."[^a6]

## Related

- [[dependence-versus-utility-dissociation]] — the same shape in a trained policy: information is encoded everywhere, yet is needed for performance only in part of the cases, so detecting use is not detecting necessity.
- [[late-entity-resolution-two-hop]] — another stage-timing failure: a hidden first hop must be resolved early enough for later layers to read it.
- [[structural-alignment-in-analogy]] — the paper's second question: whether the model maps the right parallel between situations, not only whether it encodes a relation.

[^a1]: arxiv-2511-20344 — "a significant gap is observed between these cases in terms of relational information"
[^a2]: arxiv-2511-20344 — "leads to noticeable drops in performance"
[^a3]: arxiv-2511-20344 — "suggesting that models still struggle to transfer relational structure"
[^a4]: arxiv-2511-20344 — "leads to noticeable performance gains up to 38.1%"
[^a5]: arxiv-2511-20344 — "applying them remains a major bottleneck"
[^a6]: arxiv-2511-20344 — "may contribute to reasoning failures"
