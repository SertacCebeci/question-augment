---
description: "Word-count compliance under prompt compression is U-shaped in one benchmark: 70 of 72 model-concept runs trough at medium context, near 27 words, and recover at both ends."
aliases: ["instruction ambiguity zone", "compression U-curve", "length-dependent constraint compliance", "medium-context compliance trough"]
sources: ["arxiv-2512-17920"]
---
# Constraint-compliance U-curve under compression

A stated constraint is not followed at a fixed rate. In the one benchmark read here, the constraint is held constant while the text around it is varied, and compliance is not monotone in the amount of context. The Compression-Decay Comprehension Test (CDCT) asks models to explain a scientific concept in a fixed number of words while the rest of the prompt is compressed. The compressed prompts are produced by a model "using GPT-5.1 with the following instructions," and the word count "remains fixed at 35 words across all compression levels, but the available context varies."[^c1] Compliance is scored on the count alone. A response of "exactly 35 words" gets the top rubric score, and the score falls as the count moves away from the target.[^c2]

The result is a U. "We observe a universal U-curve pattern in constraint compliance across compression levels,"[^c3] and "70 (97.2%) exhibit this pattern" of the 72 model-concept combinations.[^c4] Compliance is highest "where CC is highest at extreme compression (c=0.0) and no compression (c=1.0)," and lowest in the middle, at about 27 words (c=0.5).[^c5] The abstract states the same peak in one line: "Constraint compliance failures peak at medium prompt lengths."[^c6] The conclusion names this band an instruction ambiguity zone, and the worst case for deployment, in its own words, "at medium prompt lengths represents the worst-case scenario."[^c7]

What is measured is a relation between an instruction and the context it sits in. The same words are followed at both ends and missed in the middle. My reading: the object of the measurement is the pair (instruction, surrounding text), not the instruction taken alone. The paper's account of why the middle fails is a separate hypothesis about salience, set out in [[constraint-salience-against-helpfulness-prior]]. The semantic axis that the same runs also score, which does not show the U, is the subject of [[constraint-semantic-dissociation]].

## Limits

- The U is measured on one constraint (a word count), one task (a short explanation of a concept), eight concepts and nine models. The paper states the coverage limit itself: "First, we evaluate 9 models across 8 concepts."[^c8] It also says that "Third, we focus on factual concepts; creative domains may exhibit different" patterns.[^c9]
- Length is confounded with content. Each shorter prompt is a rewrite, so it also drops different words, examples and emphasis. The paper says "compression was achieved through model-generated rewriting" and does not separate the effect of length from the effect of which content survives.[^c10] My inference: the U is a property of these rewrites, and it does not show that length, as such, produces it.
- Compliance is judged by an LLM jury, not by a program counting words. The paper concedes that "our jury uses LLMs rather than human annotators."[^c11] The text read does not say whether the counts were checked mechanically.
- The headline percentage differs across sections. The introduction gives "97.5% of experiments exhibit a characteristic U-shaped" pattern,[^c12] while the results give 70 of 72, which is 97.2%.
- Generality beyond word counts is asserted, not tested. The discussion says "our framework generalizes to any constrained" task,[^c13] but no format, safety or style constraint is run in the parts read.
- Each condition appears to be one generation at temperature zero: "All models were accessed via API with temperature=0 for deterministic outputs."[^c14] The parts read report no repeated samples, so the spread of compliance across runs is unknown.

## Related

- [[constraint-salience-against-helpfulness-prior]] — the paper's mechanism for the trough, and its ablation
- [[constraint-semantic-dissociation]] — the same runs scored on the semantic axis, which does not show the U
- [[medium-context-sweet-spot-for-numeric-prediction]] — a different measure, interval accuracy, where added context helps only up to a point and then lowers accuracy
- [[super-additive-prompt-constraint-interaction]] — prompt constraints whose combined effect is missed by single-factor tests; a parallel case where one factor's curve can mislead

[^c1]: arxiv-2512-17920 — "remains fixed at 35 words across all compression levels, but the available context"
[^c2]: arxiv-2512-17920 — "Response is exactly 35 words"
[^c3]: arxiv-2512-17920 — "We observe a universal U-curve pattern in constraint compliance across compression levels"
[^c4]: arxiv-2512-17920 — "70 (97.2%) exhibit this pattern"
[^c5]: arxiv-2512-17920 — "where CC is highest at extreme compression (c=0.0) and no compression (c=1.0)"
[^c6]: arxiv-2512-17920 — "Constraint compliance failures peak at medium prompt lengths"
[^c7]: arxiv-2512-17920 — "at medium prompt lengths represents the worst-case scenario"
[^c8]: arxiv-2512-17920 — "First, we evaluate 9 models across 8 concepts"
[^c9]: arxiv-2512-17920 — "Third, we focus on factual concepts; creative domains may exhibit different"
[^c10]: arxiv-2512-17920 — "compression was achieved through model-generated rewriting"
[^c11]: arxiv-2512-17920 — "Second, our jury uses LLMs rather than human annotators"
[^c12]: arxiv-2512-17920 — "97.5% of experiments exhibit a characteristic U-shaped"
[^c13]: arxiv-2512-17920 — "our framework generalizes to any constrained"
[^c14]: arxiv-2512-17920 — "All models were accessed via API with temperature=0 for"
