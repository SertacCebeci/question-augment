---
description: "Answers to reworded copies of one question are scored, and their standard deviation within the group is read as consistency; a model whose correctness moves with wording shows high spread."
aliases: ["PHCS", "Paraphrased Hallucination Consistency Score", "paraphrase consistency score", "within-group hallucination spread"]
sources: ["arxiv-2512-22396"]
---
# Paraphrase-group hallucination dispersion

Ask one question in several wordings, score each answer against a reference, and look at how far the scores spread within the group. Vangala et al. define this as the Paraphrased Hallucination Consistency Score (PHCS), "as the standard deviation of hallucination scores within a paraphrased" query group.[^c1] The group is built by rewording each query "to introduce syntactic and semantic variations while preserving its original meaning," so that every member asks the same underlying question.[^c2]

The score being spread is a similarity, not a verdict. The hallucination score is "A similarity score between the generated response and the factual answer," computed with BERT embeddings.[^c3] A group whose answers all sit close to the reference has low dispersion. A group whose answers scatter in similarity has high dispersion. The quantity is the spread, not the level. A model that is consistently wrong under every wording scores low on this measure, and a model that is right under some wordings and wrong under others scores high. The note's concept is this separation: consistency across rewordings of a question is one property, and accuracy on any single wording is another.

The authors use the measure to rank paraphrase groups. Their Table 2 lists the ten most inconsistent groups, "showing the groups where hallucination levels" fluctuate the most, with PHCS values from about 0.55 to 1.10.[^c4] They read a high value as a place where the model "struggles to maintain consistency" across rewordings, which leads to "fluctuating hallucination levels."[^c5] The paper then points to paraphrase-aware detection as the remedy, without testing one.

For an asker, the same arithmetic gives a check that a single answer cannot give: the question is posed in several equivalent forms, and an answer that holds in only some of them is flagged by its spread. This is my inference from the definition; the paper does not run it as a procedure for askers.

## Limits

- The scale is unclear. The text calls the hallucination score a similarity, and its reliability thresholds (Table 3) lie between 0 and 1. A standard deviation of values in [0, 1] cannot exceed 0.5, yet the reported PHCS values reach 1.095. Either the scale or the computation differs from what the text states, and the text does not say which (my inference).
- The measure is reported, not validated. The sections read contain no comparison of PHCS with human judgments or with another consistency measure. The paper's accuracy figures (82.2%) belong to the classifier, not to PHCS.
- The embedder sets the scale of the spread. "Currently, PHCS relies on BERT-based embeddings to" measure consistency, and the authors list stronger embedders only as future work.[^c6]
- Paraphrase equivalence is assumed. The text says the queries were paraphrased while preserving meaning, but it does not describe checking that the rewordings are equivalent. A spread caused by a changed meaning would be read as inconsistency (my inference).
- Level is discarded. Two groups with the same spread but different means look identical. A model that is uniformly poor is not flagged, though the paper's own classification depends on level.
- Group sizes are not reported next to the Table 2 values, and a standard deviation over a few members is unstable (my inference).
- The responses come from one generator: the dataset "generates responses at scale with LLaMA-2 models."[^c7] Whether the dispersion pattern holds for other generators is not tested here.

## Related

- [[prompt-variant-augmentation]] — the training-side response to wording sensitivity; PHCS measures the sensitivity and does not change the model.
- [[semantic-entropy]] — spread across sampled answers to one prompt, where this note's spread runs across prompts; the two can disagree.
- [[minimal-edit-prompt-attack]] — small rewordings searched adversarially for answer flips, the same wording effect pushed to its worst case.
- [[prompt-content-over-surface-form]] — a result that surface wording matters little for some models, which bounds how much a dispersion score should be expected to reveal.

[^c1]: arxiv-2512-22396 — "as the standard deviation of hallucination scores within a paraphrased"
[^c2]: arxiv-2512-22396 — "syntactic and semantic variations while preserving its original meaning"
[^c3]: arxiv-2512-22396 — "A similarity score between the generated response and the factual answer"
[^c4]: arxiv-2512-22396 — "showing the groups where hallucination levels"
[^c5]: arxiv-2512-22396 — "A higher PHCS score suggests that the LLM struggles"
[^c6]: arxiv-2512-22396 — "Currently, PHCS relies on BERT-based embeddings to"
[^c7]: arxiv-2512-22396 — "that generates responses at scale with LLaMA-2 models"
