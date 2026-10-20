---
description: "Annotators disagree on one item for three separable reasons: the sentence's meaning is uncertain, the guideline is underspecified, or annotators behave systematically; one item can carry several."
aliases: ["Triangle of Reference", "sources of annotation disagreement", "disagreement taxonomy", "triangle of reference taxonomy"]
sources: ["doi-10-48550-arxiv-2209-03392"]
---
# Annotation disagreement sources

When several annotators label the same item and their labels spread, the spread has causes, and the causes can be sorted. Aroyo and Welty's "Triangle of Reference" puts the annotation process into three components, and Jiang and de Marneffe place each disagreement in one of them: "Disagreement can arise from (1) uncertainty in the sentence meaning, (2) underspecification of the guidelines, (3) annotator behavior."[^d1] On this reading (my reading), the three components are separate places where a label can be underdetermined: the sentence can mean more than one thing, the guideline can leave a choice open that the annotator must fill, and the annotator can apply a default that a reader would not share.

The paper turns this into a taxonomy for natural language inference (NLI). "Our taxonomy of potential disagreement sources consists of 10 categories, shown in Table 1."[^d2] The categories sit under the three classes. Under sentence meaning are lexical looseness, implicature, presupposition, probabilistic enrichment and imperfection. Under guidelines are coreference, temporal reference and interrogative hypotheses. Under annotator behaviour are accommodating minimally added content and high lexical overlap. Each class names a place where a single label can fail to be shared (my reading). The coreference example makes the point: "the hypothesis is a contradiction if we assume that Mughal" the same person is meant in both sentences, and neutral if not.[^d14]

Two properties matter for use. First, the categories are not exclusive: "More than one reason for disagreement may apply."[^d3] The items were coded with a set of categories, not one. Second, a category does not fix how much disagreement follows. Table 3 reports, per category, the share of items with convergence, defined as "at least 80/100 annotators agreed on the same NLI label,"[^d9] and the categories differ. The paper states that "Accommodating minimally added content" "has the largest amount of convergence (25.5%)," so this class most often reaches a shared label (my reading: a shared label is not thereby the correct one).[^d4]

The same item can also converge. "Even when an item lends itself to uncertainty or multiple interpretations, a high proportion of annotators may converge to the same interpretation."[^d5] So a source of disagreement in the taxonomy is a possibility, not a sign that the labels will spread. High agreement on an ambiguous item is consistent with the taxonomy.

The measured payoff is in modelling. Items with presupposition, probabilistic enrichment and imperfection are "often predicted in both setups to exhibit disagreement."[^d10] The paper also says that presupposition, implicature, imperfection and high overlap are "associated with surface patterns, potentially making it easier for the models to learn that they often exhibit disagreement."[^d11] So some categories may be learned as surface cues, and a model that predicts disagreement on them may not be reading the source the category names (my inference).

## Limits

- The taxonomy was built by one annotator from 400 items: "The taxonomy was developed by a single annotator." A second annotator was trained, and the reported check is on 110 further items.[^d6]
- The paper reports a Krippendorff's alpha of 0.69 with MASI distance, which is not high agreement (my reading), and states that "only expert annotation is possible." It also says "Some categories were merged because the distinction between them seem murky."[^d7][^d12]
- The taxonomy is an NLI taxonomy over MNLI items. It is not shown to cover disagreement in other tasks, and the authors say the source of disagreement may be the artificial task setup: "The premise and hypothesis are interpreted in isolation with no surrounding discourse." Whether adding context removes some disagreement was left for future work.[^d8]
- The category shares come from the items the authors chose to annotate. "In Round 1, one annotator annotated 400 items from" ChaosNLI, with a smaller second round, so they are not estimates of how common each source is in NLI data at large.[^d13]

## Related

- [[ambiguity-taxonomy]] — a lens for naming what a request leaves open; the NLI taxonomy names what a labeller leaves open, so the two share the idea of underspecification but not the object.
- [[presupposition-accommodation]] — the presupposition category here is one of the ten sources, where a question's presupposition is what a hypothesis can target.
- [[uncertainty-dependent-label-noise]] — label noise there rises with ambiguity even for accurate labelers; the sources here are one account of where that ambiguity comes from.
- [[label-distribution-readings]] — the same spread can be read as one probabilistic belief or as several categorical readings, which is a question about what the sources add up to.
- [[set-valued-disagreement-label]] — a way to output the sources' interpretations as a set rather than as one label.
- [[annotator-distribution-target]] — trains on the spread that these sources produce, instead of on a majority label.

[^d1]: doi-10-48550-arxiv-2209-03392 — "Disagreement can arise from (1) uncertainty in the sentence meaning, (2) underspecification of the guidelines, (3) annotator behavior."
[^d2]: doi-10-48550-arxiv-2209-03392 — "Our taxonomy of potential disagreement sources consists of 10 categories, shown in Table 1."
[^d3]: doi-10-48550-arxiv-2209-03392 — "More than one reason for disagreement may apply."
[^d4]: doi-10-48550-arxiv-2209-03392 — "has the largest amount of convergence (25.5%)"
[^d5]: doi-10-48550-arxiv-2209-03392 — "Even when an item lends itself to uncertainty or multiple interpretations, a high proportion of annotators may converge to the same interpretation."
[^d6]: doi-10-48550-arxiv-2209-03392 — "The taxonomy was developed by a single annotator,"
[^d7]: doi-10-48550-arxiv-2209-03392 — "Since the annotation requires the understanding of various linguistic phenomena, only expert annotation is possible."
[^d8]: doi-10-48550-arxiv-2209-03392 — "The premise and hypothesis are interpreted in isolation with no surrounding discourse."
[^d9]: doi-10-48550-arxiv-2209-03392 — "at least 80/100 annotators agreed on the same NLI label"
[^d10]: doi-10-48550-arxiv-2209-03392 — "are often predicted in both setups to exhibit disagreement"
[^d11]: doi-10-48550-arxiv-2209-03392 — "associated with surface patterns, potentially making it easier for the models to learn that they often exhibit disagreement"
[^d12]: doi-10-48550-arxiv-2209-03392 — "Some categories were merged because the distinction between them seem"
[^d13]: doi-10-48550-arxiv-2209-03392 — "In Round 1, one annotator annotated 400 items from"
[^d14]: doi-10-48550-arxiv-2209-03392 — "the hypothesis is a contradiction if we assume that Mughal"
