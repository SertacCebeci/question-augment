---
description: "Clustering annotators by pairwise label agreement, then modelling each cluster, is reported to beat majority vote and per-annotator models across 40 subjective-task datasets."
aliases: ["agreement-based clustering of annotators", "annotator clustering by agreement"]
sources: ["openalex-org-w7161091356"]
---
# Agreement-based annotator clustering

When several annotators label the same items, the usual move is to take the majority label and discard the rest. The other common move, training one model per annotator, keeps every perspective but costs a model per person, and annotator counts and annotation volumes are often very uneven. The method in this work sits between the two.[^c1]

The mechanism has four steps. First, each pair of annotators gets a similarity computed on the items both labelled: Cohen's kappa for multiclass tasks, Jaccard similarity over label sets for multi-label tasks. The distance is one minus that similarity. Second, the annotators are partitioned by a clustering algorithm such as k-means into C clusters, where C is set to the smallest number of annotations any instance received, so that every instance keeps at least one cluster label.[^c2] Third, within each cluster the labels for an item are majority-voted; a tie is broken by a further adjudicator, or, for multi-label tasks, all labels are kept.[^c3] Fourth, the clusters, not the individuals, become the units a classifier is trained on, through ensemble, multi-label or multitask aggregation.

The premise is that two annotators who independently assign the same label show a shared perspective on that item, and that this justifies placing them in one cluster.[^c4] The paper keeps C odd, because "an odd number of clusters eliminates the possibility of ties" at the cluster level.[^c5]

What was measured: the experiments cover "40 datasets in 18 typologically diverse" languages, with sentiment, emotion and hate-speech labels.[^c6] Against majority vote and against individual-annotator ensembles, the clustered approach is reported to win across the datasets: "the proposed clustering approach outperforms the majority vote".[^c7] Among aggregation strategies, "multi-label and multitask aggregation achieve better performance" than an ensemble on clusters.[^c8] The per-annotator gap is partly put down to skew: annotators with few labels get weak individual models, "annotators with fewer annotations yield weaker models".[^c9]

For asking and answering, the point is this (my inference, not the paper's claim): in a subjective task the label a question is scored against is itself the output of an aggregation choice. Grouping annotators by agreement is one way to keep minority readings in that label without training a model per person.

## Limits

- The evaluation is circular in one respect. The paper says the clustered results are "evaluated against the majority-voted gold labels".[^c10] The gain over majority vote is therefore measured against the very label the method argues is too coarse.
- The number of clusters is fixed by the annotation design, not chosen from the data. The paper notes that the count "can be determined based on the availability of computational" resources and data factors.[^c11] Nothing in the text I read tests how sensitive the result is to C.
- Ties need an extra annotator. The method falls back on "find a third or fifth annotator (adjudicator) for the specific tied instance" when a cluster splits evenly.[^c3] That is a cost the method pushes onto the data collection.
- Gains follow class frequency. "Performance correlates with class distribution" at the class level, so rare classes stay poorly modelled.[^c12]
- Scope: the method is "designed for already annotated datasets where only the anonymous annotator IDs are available".[^c13] It needs repeated labels per item and some overlap between annotators. Whether agreement-based clusters line up with any sociodemographic groups is not checked in the text I read (my reading).

## Related

- [[structured-annotator-disagreement-on-harm]] — also treats annotator disagreement as signal rather than noise, but models annotator traits and prompt effects directly rather than grouping annotators
- [[rater-effects-latent-score-model]] — estimates a parameter per rater; here the per-rater parameter is replaced by a shared cluster label
- [[surprisingly-popular-algorithm]] — another aggregation that beats majority vote, by asking answerers what others will say
- [[disagreement-retention-in-debate]] — keeps the most disagreeing views in a multi-agent exchange, a parallel retention of minority readings

[^c1]: openalex-org-w7161091356 — "the full spectrum of annotator perspectives"
[^c2]: openalex-org-w7161091356 — "ensuring each instance is represented by at least"
[^c3]: openalex-org-w7161091356 — "find a third or fifth annotator (adjudicator) for the specific tied instance"
[^c4]: openalex-org-w7161091356 — "if two annotators independently assign the same label"
[^c5]: openalex-org-w7161091356 — "an odd number of clusters eliminates the possibility of ties"
[^c6]: openalex-org-w7161091356 — "40 datasets in 18 typologically diverse"
[^c7]: openalex-org-w7161091356 — "the proposed clustering approach outperforms the majority vote"
[^c8]: openalex-org-w7161091356 — "multi-label and multitask aggregation achieve better performance"
[^c9]: openalex-org-w7161091356 — "annotators with fewer annotations yield weaker models"
[^c10]: openalex-org-w7161091356 — "evaluated against the majority-voted gold labels"
[^c11]: openalex-org-w7161091356 — "the number of clusters can be determined based on the availability of computational"
[^c12]: openalex-org-w7161091356 — "Performance correlates with class distribution"
[^c13]: openalex-org-w7161091356 — "annotated datasets where only the anonymous annotator IDs are available"
