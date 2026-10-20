---
description: "Analogies that succeed show more token-level mutual alignment between source and target stories than between source and a lexically similar distractor; failures are drawn to the distractor."
aliases: ["mutual alignment score", "MAS", "structural alignment", "structure mapping alignment", "relational parallel alignment"]
sources: ["arxiv-2511-20344"]
---
# Structural alignment in analogy

Structural alignment is the mapping of one situation's elements onto another's so that relations correspond, not surface features. The work measures it inside a model with a Mutual Alignment Score (MAS): the score is "the proportion of mutual best matches between contextualized token representations" of a source span and a candidate span.[^b1] A pair of tokens counts as a mutual best match when each is the other's most similar token by cosine similarity, computed layer by layer. The question the score answers is which parallel the model's own geometry prefers: the structural one, or the lexical one.

Two findings come out of it. First, the analogical structure of a pair of stories becomes separable from mere lexical similarity as depth grows: "analogical structure becomes increasingly linearly separable in the middle layers."[^b2] A linear probe reaches an average accuracy of 82.9% over layers 20 to 30.[^b3]

Second, the score separates success from failure. For correct cases, "the MAS between source and target stories consistently exceeds that between source and distractor stories."[^b4] The gap peaks in the middle layers. For incorrect cases the gap is much smaller, "with distractors often receiving greater alignment."[^b5] The abstract states the same contrast: successful analogical reasoning shows strong alignment "between analogous situations, whereas failures often reflect degraded or misplaced alignment."[^b6]

The design makes this a test of more than shared words. The target story has minimal entity overlap with the source, and the distractor is chosen for high noun similarity. A model that aligns the distractor is therefore following surface resemblance, while one that aligns the target is following the relation. This is the internal counterpart of [[literal-match-dependence]], where evidence is found by shared words rather than by content, and it fits the distractor classes in [[anchored-distractor-taxonomy-math-problems]], which are built from the problem's own entities and attributes.

## Limits

- The result is correlational. MAS and probe accuracy are associated with correct answers. The paper does not intervene on alignment and show that raising it repairs a failure; its patching experiments act on the relation path, not on the alignment score.
- One dataset: StoryAnalogy, 360 multiple-choice items, reduced to two options by dropping the random distractors. A two-option forced choice may not carry over to open generation.
- Three instruction-tuned models of 9B to 14B parameters, with the main analysis on Qwen2.5-14B-Instruct. Other families and scales are in the appendix, not in the text read here.
- MAS is a token-level cosine proxy. A high mutual-match count shows that tokens are geometrically matched, not that they correspond in the relational sense the authors intend. The correspondence is read off by the authors' examples, such as the heatmap of "Water-air, house-lungs" pairs.
- "Structure" here is what the dataset's construction defines (source, analogous target, noun-similar distractor). The measure says nothing about structural alignment in cases built differently.

## Related

- [[relation-application-bottleneck]] — the encoding and application side of the same models: a relation can be encoded in mid-upper layers and still fail to reach the answer position.
- [[literal-match-dependence]] — lexical overlap as the route to evidence; the retrieval-side analogue of the distractor effect here.
- [[anchored-distractor-taxonomy-math-problems]] — distractors tied to a problem's own entities, a related way that surface-anchored candidates compete with the intended structure.

[^b1]: arxiv-2511-20344 — "the proportion of mutual best matches between contextualized token representations"
[^b2]: arxiv-2511-20344 — "analogical structure becomes increasingly linearly separable in the middle layers"
[^b3]: arxiv-2511-20344 — "layers 20 through 30 showing an average accuracy of 82.9%"
[^b4]: arxiv-2511-20344 — "the MAS between source and target stories consistently exceeds that between source and distractor stories"
[^b5]: arxiv-2511-20344 — "with distractors often receiving greater alignment"
[^b6]: arxiv-2511-20344 — "between analogous situations, whereas failures often reflect degraded or misplaced alignment"
