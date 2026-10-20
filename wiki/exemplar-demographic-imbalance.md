---
description: "Demographic skew in the in-context exemplars carries into a model's between-group disparity; the paper reports R = 0.67 across selection methods and attributes, and reads it as causal."
aliases: ["demonstration demographic imbalance", "demographic skew in demonstrations", "sensitive-attribute imbalance of exemplars", "exemplar composition bias", "demonstration MaxDiff"]
sources: ["arxiv-2511-15986"]
---
# Exemplar demographic imbalance

A model that learns from examples in its prompt is shaped by which examples it sees. Each example carries a label, and it may also carry a sensitive attribute such as gender, race or ethnicity. The composition of the chosen set on that attribute is a separate property from its label agreement or its similarity to the query. A selection rule does not have to control it, so it can drift.

The measure the paper uses is the gap between the largest and the smallest group share in the selected set: the difference "defined as the difference between the maximum and minimum" proportional representation among the sensitive groups.[^e1] A male–female split gives "MaxDiff = 0.50, whereas perfect parity corresponds to MaxDiff = 0."[^e2] The measure is blind to how many groups there are and to the order between them; it reads one number off the set.

The mechanism the authors propose is that the skew moves from the exemplars into the answers. Their summary finding is that "Unfairness arises from demographic imbalance in selected demonstrations."[^e3] Across methods and attributes, the imbalance and the disparity move together: "correlation (R = 0.67) emerges" between the two.[^e4] The sharpest case is ethnicity, where "Random-Ethnicity (MaxDiff=86.3%)" gave the largest disparities in the table.[^e5] The authors read the relation as direct: "biased exemplar composition directly drives fairness degradation."[^e6] They also state the point as a general one about the paper's setting: "data imbalance in selected demonstrations is the primary source of fairness degradation."[^e7]

What the selection rule does with this matters. The paper compares random, similarity and clustering selection, and finds that none of them is consistently fair: "Existing DS methods cannot bring consistent fairness improvement for medical image analysis."[^e8] Their remedy is to choose the set so that sensitive subgroups are close to equal in share, while keeping the chosen examples relevant to the query. They report that this "effectively mitigates both datadriven and model-induced bias, providing a stable fairness–performance trade-off."[^e9] The remedy is a selection criterion, not a change to the model, which is why the paper frames it as tuning-free.

The transferable part is the measurement. Exemplar composition on a group attribute is a quantity that a prompt-builder can read off the set before the model runs, and the paper treats it as a predictor of disparity. What does not transfer on its face is the setting. The paper works with medical images, a fixed label set and sensitive tags attached to each image. In a text-only task the attribute may not exist, or may be inferred, and nothing here shows the same relation there.

## Limits

- The link is a correlation over a small number of points. Figure 3 plots one point per attribute under a selection method, and the authors do not report a sample of settings wide enough to test the relation as a rule. The phrase "directly drives" is the authors' reading of that correlation, not something the design isolates (my inference).
- Two datasets (Glaucoma and CheXpert Plus subsets) and three vision-language models were tested, with "Each method constructs 8–16 demonstrations per query without fine-tuning."[^e10] Demonstration counts outside that range and text-only tasks were not tested.
- One attribute is balanced at a time. The authors name the gap themselves: "we plan to extend FADS to handle multiple sensitive attributes and more complex intersectional fairness settings."[^e11] Whether balancing one attribute leaves another skewed was not measured, and the paper's own tables show the attributes moving in different directions under the baseline rules.
- The measure is a two-group summary (largest minus smallest share). It does not say whether skew comes from one small group or from a shifted majority, and two sets with the same MaxDiff can differ in what they teach the model (my inference).
- Balance is not shown to be sufficient for fairness. The paper reports reduced disparities under its own method, not a proof that a balanced set yields a balanced answer under every query distribution. The fairness–performance trade-off is reported as "stable," but the accuracy cost is a measured trade-off, not zero.
- The paper's "model-induced bias" is a second source beyond exemplar skew. It is distinguished from data-driven bias by the authors' argument, and this note does not verify that split.

## Related

- [[demonstration-label-consistency]] — the same kind of composition measure on the label axis: the share of exemplars that agree with the query's label. This note is the sensitive-attribute axis.
- [[similarity-selected-exemplars]] — similarity retrieval is the baseline here that can concentrate one group in the set; that note is about whether similarity helps accuracy at all.
- [[in-context-learning-as-label-propagation]] — the transductive view that makes the exemplars' composition a term in the prediction error; the sensitive attribute is a candidate for a similar term (my inference).
- [[qa-benchmark-demographic-skew]] — skew in the source material the exemplars are drawn from; the upstream form of the same imbalance.

[^e1]: arxiv-2511-15986 — "defined as the difference between the maximum and minimum"
[^e2]: arxiv-2511-15986 — "parity corresponds to MaxDiff = 0."
[^e3]: arxiv-2511-15986 — "Unfairness arises from demographic imbalance in selected demonstrations."
[^e4]: arxiv-2511-15986 — "correlation (R = 0.67) emerges"
[^e5]: arxiv-2511-15986 — "Random-Ethnicity (MaxDiff=86.3%)"
[^e6]: arxiv-2511-15986 — "composition directly drives fairness degradation"
[^e7]: arxiv-2511-15986 — "data imbalance in selected demonstrations is the primary source of fairness degradation"
[^e8]: arxiv-2511-15986 — "Existing DS methods cannot bring consistent fairness improvement for medical image analysis."
[^e9]: arxiv-2511-15986 — "providing a stable fairness–performance trade-off"
[^e10]: arxiv-2511-15986 — "Each method constructs 8–16 demonstrations per query without fine-tuning"
[^e11]: arxiv-2511-15986 — "we plan to extend FADS to handle multiple sensitive attributes and more complex intersectional fairness settings"
