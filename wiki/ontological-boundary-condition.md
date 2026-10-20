---
description: "Where a text-trained model's learned patterns run sparse, it cannot register the gap as absence and keeps generating, so fabrication starts at the edge of its grounding."
aliases: ["ontological boundary conditions", "boundary conditions of a pseudo-ontology", "fictional completion boundary"]
sources: ["arxiv-2512-14801"]
---
# Ontological boundary condition

An ontological boundary condition is a place in a text-trained model's learned space where the patterns that would ground an answer run out. The paper defines the term for "regions in the embedding space where textual patterns fail to correspond to actual facts"[^c1], that is, where the training data gives too little support to a claim. The boundary is set by density. "Dense areas of the manifold correspond to highly regular patterns"[^c2] such as names, dates and known facts; sparse areas hold uncommon combinations and poorly represented entities.

Prompts reach the boundary in a few ways. One pulls the model into a region with insufficient density; one demands specificity where the learned space holds ambiguity; one requires a discrimination finer than its associations allow; and one references entities that are "underrepresented or absent in the corpus."[^c3]

What makes the boundary a concept rather than a data-quality problem is what the model does there. It does not detect a void. "grounding does not register as absence, it registers as faint statistical traction."[^c4] The model must bridge the gap, and it does so by interpolation. "At these boundaries, the model does not abstain or express uncertainty."[^c5] What it produces instead is what the paper calls fictional completion: a continuation that keeps the form of an answer while its content has no referent.

The paper predicts the forms this takes. Fabricated specificities (an invented attribute for an obscure figure), spurious causal links, category cross-contamination, and nonexistent references. For references, "The model may generate bibliographies, citations, or articles that fit the form of genuine references but"[^c6] lack any real counterpart.

For a question-asker the consequence is that the answerer's own signal is silent exactly where the boundary is. "Boundary conditions, therefore, are invisible to the model."[^c7] The paper's account of abstention follows from this: refusal is "a learned linguistic pattern, triggered by contexts that resemble prior abstention cues,"[^c8] not a report from inside about missing grounding. An answer given at the boundary therefore carries no mark of having been given there.

## Limits

- The boundary is defined and argued, not measured. No embedding density is observed in the work. The claim that fabrication sits where density is low is asserted, and the four forms are said to follow from it; none of the forms is counted against density. My inference.
- "Invisible to the model" is a universal claim that rests on the architecture argument. The wiki's [[abstention]] note records a learned policy that refuses on most questions when refusal is rewarded. That shows refusal moves with reward. It does not show whether refusal tracks a density boundary, and this paper does not test that either. My reading.
- The training-density gradient in [[training-density-citation-fabrication-gradient]] fits the boundary's prediction: recent and niche literature is fabricated more. That note says its density mechanism "was not tested by manipulating training data". The two agree in direction; neither tests the mechanism.
- The concept is written for a model whose knowledge sits in its weights. In a system with retrieval the sparse region may lie in the retrieved text, and the work does not discuss that case. My inference.

## Related

- [[abstention]] — refusal as a named third output; the boundary is where the answerer lacks the signal refusal would need
- [[training-density-citation-fabrication-gradient]] — a measured ordering of citation fabrication by literature density; its mechanism is inferred, as it is here
- [[structural-hallucination]] — the broader thesis that places fabrication at such boundaries as a consequence of the architecture
- [[externalized-abstention-gate]] — the paper's remedy for a failure the generator cannot see from inside

[^c1]: arxiv-2512-14801 — "where textual patterns fail to correspond to actual facts"
[^c2]: arxiv-2512-14801 — "Dense areas of the manifold correspond to highly regular patterns"
[^c3]: arxiv-2512-14801 — "references entities that are underrepresented or absent in the corpus"
[^c4]: arxiv-2512-14801 — "grounding does not register as absence, it registers as faint statistical traction"
[^c5]: arxiv-2512-14801 — "At these boundaries, the model does not abstain or express uncertainty."
[^c6]: arxiv-2512-14801 — "The model may generate bibliographies, citations, or articles that fit the form of genuine references but"
[^c7]: arxiv-2512-14801 — "Boundary conditions, therefore, are invisible to the model."
[^c8]: arxiv-2512-14801 — "epistemic act but a learned linguistic pattern, triggered by contexts that resemble prior abstention cues"
