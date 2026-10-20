---
description: "Reading in-context learning as transductive label propagation makes demonstration similarity and label agreement two terms of one propagation error, so selection should weigh both."
aliases: ["ICL as transductive learning", "label propagation view of in-context learning", "Bayesian transduction view of ICL", "transductive ICL"]
sources: ["arxiv-2512-12175"]
---
# In-context learning as label propagation

The common Bayesian reading of in-context learning (ICL) says the demonstrations "activate the latent concepts learned during pretraining," so that the model can answer the query from those concepts.[^c1] The transductive reading keeps that picture and changes the learning paradigm. The paper argues that ICL "should be considered transductive learning, rather than inductive learning."[^c2] Transductive learning "focuses on local optimization rather than generalization," so it infers labels for a fixed unlabeled set instead of a general rule.[^c3]

Once ICL is transductive, the paper gives it the shape of semi-supervised label propagation. Transductive label propagation "uses the labels of labeled data to infer the labels of unlabeled data."[^c4] The demonstrations are the labeled data and the query is the unlabeled point. The model's concept for the query is updated from the demonstrations' concepts, weighted by a coefficient s_i that depends on semantic similarity and on the position of each demonstration in the context. An error term ε is added for the propagation error inside the language model.[^c5]

The argument then needs a smoothness assumption, which the paper states as "similar data tend to have the same label."[^c6] Under it, two things make the propagated label trustworthy: the demonstrations should be similar to the query, and they should share its label. The paper's bound puts the propagation error between these terms: "label consistency as a lower bound for evaluating propagation error."[^c7] The noise term "is determined by both semantic similarity and label consistency."[^c8] Similarity is then read as the lever that reduces error, and label agreement as the term that estimates it. Selection that looks only at similarity is therefore incomplete under this view. The paper's stated conclusion: "ICL should focus more on demonstrations, which should have a high semantic similarity to the query and share the same label."[^c9]

What the reframing buys is a reason to measure label agreement at all. The measured version of that agreement is described in [[demonstration-label-consistency]].

## Limits

- The bound is one-sided. It lower-bounds a noise term that involves the propagation error ε, and ε is never measured. The bound says what would be small if the error were small, not how large the error is for a given prompt.
- The derivation assumes the mapping from input to label is smooth. The paper states that the mapping "is smooth and satisfies the L-Lipschitz constraint," and that assumption carries the bound.[^c10] No test of Lipschitz smoothness for an LLM is reported. Whether a discrete label mapping over text meets it is not shown.
- The Bayesian step follows a published framework (Xie et al. 2021), with its assumptions taken over. The transductive relabelling is an interpretation of that framework. It is not a separate experiment.
- Ordering enters the coefficient s_i through the position term, but the paper does not test ordering effects against the theory.
- The evidence for the theory is a correlation between label agreement and accuracy, plus an ablation of one selection method. The theory predicts that both similarity and agreement matter; it does not predict a threshold or a functional form, and none is tested.
- The paper frames the view as explanatory. It does not show that the propagation picture is the mechanism rather than one of several readings that fit the same correlations (my inference).

## Related

- [[demonstration-label-consistency]] — the measured quantity the propagation framing says should matter, and the selection result that follows from it.
- [[similarity-selected-exemplars]] — the similarity side of the same coefficient; there, similarity alone gives mixed results against random choice.
- [[active-in-context-learning]] — a frozen in-context predictor used to choose which labels to query; the same ICL setting, asked about labelling rather than demonstration selection.

[^c1]: arxiv-2512-12175 — "to activate the latent concepts learned during pretraining"
[^c2]: arxiv-2512-12175 — "should be considered transductive learning, rather than inductive learning"
[^c3]: arxiv-2512-12175 — "focuses on local optimization rather than generalization"
[^c4]: arxiv-2512-12175 — "uses the labels of labeled data to infer the labels of unlabeled data"
[^c5]: arxiv-2512-12175 — "denotes the propagation error within the LM in ICL"
[^c6]: arxiv-2512-12175 — "similar data tend to have the same"
[^c7]: arxiv-2512-12175 — "use label consistency as a lower bound for evaluating propagation error"
[^c8]: arxiv-2512-12175 — "is determined by both semantic similarity and label consistency"
[^c9]: arxiv-2512-12175 — "which should have a high semantic similarity to the query and share the same label"
[^c10]: arxiv-2512-12175 — "is smooth and satisfies the L-Lipschitz constraint"
