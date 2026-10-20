---
description: "A spread of annotator labels can come from one probabilistic belief per annotator or from several categorical readings of the sentence; the aggregate probability means different things in each."
aliases: ["probabilistic versus categorical disagreement", "two sources of label distributions", "belief or reading distribution"]
sources: ["doi-10-48550-arxiv-2209-03392"]
---
# Label distribution readings

A label distribution over annotators is a vector of votes, such as 82 Entailment, 17 Neutral and 1 Contradiction. The same vector can come from two different processes, and the paper argues that the difference changes what the aggregate probability means. Jiang and de Marneffe write that disagreement in the categorical labels "arise in at least two ways: (1) a single probabilistic inference, or (2) multiple potentially categorical inferences."[^r1]

In the first reading, each annotator holds a graded judgment and reports it as a label. In the paper's "Sir James" example, "each annotator may have an underlying probabilistic judgment of how likely it is that Sir James thinks it's absurd."[^r9] The vote share then estimates that graded judgment, which is my reading of the paper's example. The paper says that in this case "the probability associated with the Entailment label can be taken as the probabilistic belief (Kyburg, 1968) of an individual annotator for the truth of the hypothesis."[^r2] The aggregate is a probability over one judgment, repeated across annotators.

In the second reading, each annotator is categorical, but each picks a different reading of the sentence. The paper's example is a hypothesis whose truth depends on whether it is evaluated before or after a product release. Each reading yields a clean categorical judgment, and the spread mixes them. So "the probability associated with the Entailment label does not represent the judgment of an individual."[^r3] The paper puts the contrast as "One is uncertainty in the state of the world. One is in how to interpret the sentences."[^r4]

The distinction matters for what is inferred from a spread. Under the first reading a high-spread item tells you about the strength of one belief, so the vote share is a natural target (my inference). Under the second, the spread is a set of interpretations, and a single probability averages over readings that no single annotator held (my inference). This links to the sources of disagreement: the second reading covers the items whose sources are coreference, temporal reference and similar specification gaps, and the paper says that "discourse context is needed for resolving many of the uncertainty" of that kind.[^r5]

## Limits

- The distinction is drawn from worked examples in the paper's taxonomy, not measured on annotators. The paper says so: "Pursuing this line of research is left for future work."[^r6] It proposes that one could "collect empirical evidence for this distinction", for instance with "multilabel or sliding bar annotations, or free-text explanations".[^r7]
- A vote vector alone cannot tell the two readings apart. The paper sorts items by reading the sentences, not by asking the annotators which reading they took. My inference is that the two would look alike in the counts and differ only in the annotators' stated grounds.
- Some items carry both. The paper says of one example that "[7] involves categorical and probabilistic inferences." So the two readings are not exclusive, and the note does not give a rule for splitting a spread between them.[^r8]
- The modelling in the same paper is trained on vote counts and does not separate the two readings. Whether a model that does separate them outperforms one that does not was not tested.
- The sentences were judged in isolation, without discourse. The paper names that setup as a possible cause of the second reading, and it is not tested whether context reduces it.

## Related

- [[annotation-disagreement-sources]] — the three components that can each supply the uncertainty; the second reading here is the case where the uncertainty is in how to interpret the text.
- [[annotator-distribution-target]] — trains on the vote spread as a target; this note asks what that spread is a spread of.
- [[set-valued-disagreement-label]] — outputs the readings as a set of labels, which fits the second reading better than a single probability does.
- [[uncertainty-dependent-label-noise]] — label noise there rises with ambiguity even for accurate labelers, a relation to the spread on the labelers' side that this note separates into two readings.

[^r1]: doi-10-48550-arxiv-2209-03392 — "arise in at least two ways: (1) a single probabilistic inference, or (2) multiple potentially categorical inferences"
[^r2]: doi-10-48550-arxiv-2209-03392 — "can be taken as the probabilistic belief (Kyburg, 1968) of an individual annotator for the truth of the hypothesis."
[^r3]: doi-10-48550-arxiv-2209-03392 — "the probability associated with the Entailment label does not represent the judgment of an individual"
[^r4]: doi-10-48550-arxiv-2209-03392 — "One is uncertainty in the state of the world. One is in how to interpret the sentences."
[^r5]: doi-10-48550-arxiv-2209-03392 — "discourse context is needed for resolving many of the uncertainty"
[^r6]: doi-10-48550-arxiv-2209-03392 — "Pursuing this line of research is left for future work."
[^r7]: doi-10-48550-arxiv-2209-03392 — "We could design experiments to collect empirical evidence for this distinction, such as collecting multilabel or sliding bar annotations, or free-text explanations"
[^r8]: doi-10-48550-arxiv-2209-03392 — "[7] involves categorical and probabilistic inferences"
[^r9]: doi-10-48550-arxiv-2209-03392 — "each annotator may have an underlying probabilistic judgment of how likely it is that Sir James thinks"
