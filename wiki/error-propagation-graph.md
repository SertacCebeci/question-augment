---
description: "Errors in a reasoning chain form a graph of which step's error comes from which earlier step; a Jaccard loss on its edges, added to SFT, raised step-identification accuracy in one ablation."
aliases: ["error propagation graph", "error trajectory graph", "root-cause error graph"]
sources: ["doi-10-48550-arxiv-2512-01424"]
---
# Error propagation graph

A wrong step in a reasoning chain is often not the only wrong step. Later steps inherit the mistake and build on it, so the useful record of an error is which step it came from, not only which steps are wrong. ViRectify stores this as a graph over the steps, encoded as an adjacency list in which each entry "indicates that the error in a given step originates from" an earlier step.[^c1] The erroneous solutions in the benchmark carry several errors each, so the structure to recover is more than one label per chain.[^c2]

The graph is also a training target. The first SFT stage adds to the cross-entropy loss a graph term, defined so that "the graph loss is computed as one minus the" Jaccard similarity between the predicted and the ground-truth edge sets.[^c3] The paper states the purpose of the term: it "encourages the model to capture the structural dependencies among reasoning steps" by "promoting consistency between predicted and true error propagation relations."[^c4][^c5]

The ablation is the measured part. "Removing the graph loss consistently degrades performance across all metrics,"[^c6] and step-identification accuracy (Acci, the average step-wise accuracy of identifying erroneous steps)[^c8] drops from 82.41 to 72.17 when the term is removed.[^c7] My reading of the mechanism: a predicted edge that disagrees with the annotated one costs something even when the step label is right, so the model is pushed to say which earlier error each later error depends on. The paper does not separate the label term from the edge term, so this is an interpretation of why the term helps, not a result.

## Limits

The edges are an annotation. They were produced with GPT-o4-mini from the question, the timestamped captions, a verified correct solution and the step labels, and only "a subset of the corrections is further verified by human" experts.[^c9] The graph therefore records an annotator model's account of how a chain went wrong, not a measured failure process.

The ablation I read removes one term from one training recipe. The text does not compare the graph against another structural loss, or against the same step labels with the edges dropped in a different way, so the gain could come from the extra supervision rather than from the graph's structure.

The Jaccard score is a set overlap over edges. A predicted edge to a neighbouring step scores the same as a missing edge, and the loss has no notion of a dependency being nearly right. This is a reading of the formula as written, not something the paper tests.

## Related

- [[detection-correction-gap]] — the split between naming an error and fixing it; the graph makes the naming step finer, at the level of which step depends on which
- [[dag-aware-evaluation-protocol]] — orders checks by a prerequisite graph so feedback names root causes rather than downstream symptoms; the same root-versus-symptom distinction, in an evaluator
- [[error-enumeration-verdict-format]] — requires localized errors before a verdict, a neighbouring way to force an error's location into the output

[^c1]: doi-10-48550-arxiv-2512-01424 — "indicates that the error in a given step originates from"
[^c2]: doi-10-48550-arxiv-2512-01424 — "Erroneous solutions in our benchmark contain an average of 4.78 incorrect steps"
[^c3]: doi-10-48550-arxiv-2512-01424 — "the graph loss is computed as one minus the"
[^c4]: doi-10-48550-arxiv-2512-01424 — "encourages the model to capture the structural dependencies among reasoning steps"
[^c5]: doi-10-48550-arxiv-2512-01424 — "by promoting consistency between predicted and true error propagation relations"
[^c6]: doi-10-48550-arxiv-2512-01424 — "Removing the graph loss consistently degrades performance across all metrics"
[^c7]: doi-10-48550-arxiv-2512-01424 — "dropping from 82.41 to 72.17"
[^c8]: doi-10-48550-arxiv-2512-01424 — "measures the average step-wise accuracy of identifying erroneous reasoning steps"
[^c9]: doi-10-48550-arxiv-2512-01424 — "a subset of the corrections is further verified by human"
