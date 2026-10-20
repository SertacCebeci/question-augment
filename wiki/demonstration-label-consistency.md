---
description: "In-context accuracy rises with the share of demonstrations that carry the query's label; top-K similarity retrieval does not guarantee that share, and a label-aware selection raised it."
aliases: ["demonstration label consistency", "label agreement of demonstrations", "same-label demonstration ratio", "label-consistent demonstrations"]
sources: ["arxiv-2512-12175", "arxiv-2511-19557"]
---
# Demonstration label consistency

In-context learning (ICL) puts a few labeled demonstrations in the prompt before the query. The usual rule for choosing them is top-K retrieval: take the K candidates nearest to the query in embedding space. The label-consistency view asks a different question about the same set. What share of the chosen demonstrations carry the same label as the query? The paper quantifies it that way: "label consistency is therefore quantified by the ratio of demonstrations with the same label."[^c1]

The mechanism the authors give is that similarity and label agreement are separate ingredients. Similar demonstrations are meant to steer the model toward the concept that governs the query. A demonstration whose label differs from the query's label supplies evidence about a different mapping. The authors' claim is that ordinary top-K retrieval leaves this unchecked: "the label consistency is not guaranteed during demonstration selection."[^c2]

The measured link runs in one direction across their settings. "As label consistency increases, the accuracy of ICL also improves."[^c3] When no demonstration shares the query's label, "the accuracy significantly decreases."[^c4] The effect is largest when few demonstrations are shown: "label consistency is crucial with limited demonstrations."[^c5] With three or fewer demonstrations, their label-aware selection beat plain top-K.

Raising the share is possible without giving up similarity. The paper's method (TopK-SD) pulls each candidate's embedding toward the centroid of its own class before top-K sampling, with a mixing weight λ. On TREC, the synthetic embeddings improved consistency of KNN sampling: "consistency has essentially improved by more than 10%."[^c6] The gain is not monotone in λ. "Label consistency peaks at λ = 0.6," and the authors conclude that "Our findings underscore the criticality of dataset-specific λ optimization."[^c7]

The point for the wiki is the second axis. A retrieval rule judged only by similarity says nothing about whether the demonstrations agree with each other on the label, and that agreement is what the paper measures as predictive.

A different retrieval rule appears in a disaster visual-QA framework whose answers come from a fixed list. There the exemplars are chosen per answer: "For each candidate answer, the most visually similar exemplar is retrieved", so that "the final set of exemplars represents all possible answers."[^c10] The target is coverage of the candidate list, not the share that matches the query's label. Because the query's label is unknown at selection time, the two rules aim at different quantities. The paper does not compare them, and whether per-answer coverage helps or hurts label agreement is not shown (my inference).

## Limits

- The quantity is a ratio over demonstrations. The paper's own theory names a propagation coefficient that it calls "hard to characterize," so the measured ratio stands in for the quantity the theory is about.[^c8]
- The accuracy relation is correlational across settings (Figure 2). The TopK-SD ablation changes similarity and label agreement together, so it does not separate the two effects on its own. Whether a random draw with the same ratio gives the same accuracy was not shown here (my inference from the design).
- At selection time the query's label is unknown: "no substantial prior knowledge is available for the labels of input queries." The method therefore raises consistency for an unknown target, using a reference vector averaged over classes. How often that estimate points to the right label is not reported in the passage read.[^c9]
- λ is tuned per dataset and the paper gives no rule for choosing it without labelled tuning data (my inference).
- The evidence is classification with LLM prompting on five text benchmarks named in the paper. Generation, multi-label, or open-ended tasks are not tested here.

## Related

- [[similarity-selected-exemplars]] — similarity-only retrieval gives mixed results against random choice; label agreement is a second property that similarity does not control.
- [[in-context-learning-as-label-propagation]] — the theory that makes label agreement a term in the error bound, and the reason it matters for selection.
- [[reasoning-conditioned-answer-selection]] — the same disaster-VQA framework's answer stage; its exemplar rule covers each candidate answer instead of matching the query's label.

[^c1]: arxiv-2512-12175 — "label consistency is therefore quantified by the ratio of demonstrations with the same label"
[^c2]: arxiv-2512-12175 — "the label consistency is not guaranteed during demonstration selection"
[^c3]: arxiv-2512-12175 — "as label consistency increases, the accuracy of ICL also improves"
[^c4]: arxiv-2512-12175 — "the accuracy significantly decreases"
[^c5]: arxiv-2512-12175 — "label consistency is crucial with limited demonstrations"
[^c6]: arxiv-2512-12175 — "consistency has essentially improved by more than 10%"
[^c7]: arxiv-2512-12175 — "Label consistency peaks at λ = 0.6"
[^c8]: arxiv-2512-12175 — "hard to characterize"
[^c9]: arxiv-2512-12175 — "no substantial prior knowledge is available for the labels of input queries"
[^c10]: arxiv-2511-19557 — "the final set of exemplars represents all possible answers"
