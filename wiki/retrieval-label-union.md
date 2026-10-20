---
description: "Predicting a query's labels as the union of its k nearest stored examples, with no model, gains recall but loses precision and subset accuracy as k grows."
aliases: ["retrieval-based labeling", "k-NN label union", "neighbour label transfer", "label transfer via retrieval"]
sources: ["arxiv-2512-04106"]
---
# Retrieval label union

Take a query, retrieve the k stored examples nearest to it by embedding, and output the union of their labels. No language model reads the query or the examples; the labels of the neighbours are copied. This is the model-free arm of retrieval-augmented prompting. It is a baseline for a specific question: how much of a retrieved set's value is already in its labels, before any inference.[^c7]

In a multi-label code vulnerability task, the union rule behaves in a way that the model-in-the-loop arms do not. At one neighbour it is competitive: "Retrieval-Based Labeling performs well at k = 1" and its subset accuracy is 41.80% at that setting.[^c2] As k rises the union grows, and the scores move in opposite directions. Precision falls: "Retrieval-Based Labeling deteriorates rapidly from 64.19% at" one shot to 43.06% at ten.[^c3] Recall rises to 98.24% at ten shots, and the authors attribute this to over-prediction: the rule "tends to include a superset of correct labels".[^c4] Subset accuracy, which needs the exact label set, drops to 4.60% at ten shots.[^c1]

The mechanism the authors give is the accumulation of wrong labels. Each added neighbour contributes its own labels, and "the accumulation of incorrect labels from" unrelated samples is what the union cannot filter.[^c5] The authors read the strong k=1 result as "likely due to high similarity" between the query and its single neighbour.[^c6] The shape is therefore a trade-off set by k: one neighbour gives a close but narrow label set, and each further neighbour widens the set faster than it adds correct labels. Because "it bypasses model inference and aggregates labels directly," nothing in the rule can drop a wrong label once it enters the union.[^c8]

## Limits

- One dataset, four CWE categories after excluding non-vulnerable functions, one embedding model, one LLM elsewhere in the study. The k-curve is from that setting only.
- The union rule was tested only in its unweighted form. A per-label vote, a threshold on neighbour agreement, or a distance weighting would change the precision and recall trade-off; none is in the paper, so whether a filtered union escapes the over-prediction is untested (my inference).
- The figures are single values per cell, with no interval. The step from strong at k=1 to weak at ten is large enough to read directionally, but the exact cross-over point is not established.
- The decline is a property of label union under multi-label scoring. For single-label classification, where a union cannot grow beyond one label, the same curve would not appear, so the number does not carry over (my inference).
- The paper's reason for the k=1 result is the authors' conjecture about similarity and was not isolated.

## Related

- [[similarity-selected-exemplars]] — the same retrieved neighbours, with a model reading them; there the selection rule is the variable, here the labels are the output
- [[in-context-learning-as-label-propagation]] — the transductive frame in which copying neighbour labels is the operation; this note is its measured model-free arm
- [[demonstration-label-consistency]] — how often the neighbours share the query's label, the quantity whose absence the union rule turns into over-prediction

[^c1]: arxiv-2512-04106 — "Retrieval-Based Labeling (4.60%)"
[^c2]: arxiv-2512-04106 — "Retrieval-Based Labeling performs well at k = 1"
[^c3]: arxiv-2512-04106 — "Retrieval-Based Labeling deteriorates rapidly from 64.19% at"
[^c4]: arxiv-2512-04106 — "due to overprediction; it tends to include a superset of correct labels"
[^c5]: arxiv-2512-04106 — "the accumulation of incorrect labels from"
[^c6]: arxiv-2512-04106 — "likely due to high similarity"
[^c7]: arxiv-2512-04106 — "value of model inference over simple label propagation"
[^c8]: arxiv-2512-04106 — "it bypasses model inference and aggregates labels directly"
