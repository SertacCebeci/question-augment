---
description: "A sparse autoencoder on step-level activations of a reasoning model gives decoder directions that cluster by reflection and backtracking, with no behaviour labels in training."
aliases: ["RISE", "reasoning vectors", "SAE decoder columns as reasoning behaviours", "unsupervised reasoning-behaviour discovery"]
sources: ["arxiv-2512-23988"]
---
# SAE reasoning-behaviour vectors

A reasoning trace can be cut into steps, and each step's hidden state at the step boundary can be read as one activation. The mechanism the paper proposes is to train a sparse autoencoder (SAE) on those activations with no labels, and to treat each decoder column as a candidate "reasoning vector." The paper defines fine-grained reasoning behaviours "as linear directions in the activation space, which we refer to as Reasoning Vectors."[^c1] The unit is the step, not the token, because "the same token can play diverse roles across different contexts."[^c2] The paper splits a response "using the delimiter symbol" into steps and takes the representation at that delimiter as the step's activation.[^c3]

The training is an ordinary SAE objective: reconstruction error plus an L0 penalty, so that "only a small number of atomic concepts are used, thereby reducing entanglement across vectors and enhancing interpretability."[^c4] The reported setup is one model, DeepSeek-R1-Distill-Qwen-1.5B, a dictionary of 2048 vectors, and "randomly sampled training examples from the MATH dataset."[^c5] The SAE is trained on a single layer's residual stream.

The structure is then examined after the fact. Decoder columns are projected to two dimensions with UMAP, and an LLM judge labels each step as reflection, backtracking or other. The reflection and backtracking columns form tighter regions than the "other" columns, and silhouette scores "generally" rise with depth: "later layers generally achieve higher Silhouette scores than earlier ones."[^c6] The paper also says that "the comparison between reflection and backtracking reveals only modest differences."[^c7] So the separation the method yields is mainly between a labelled behaviour and the residual, not between the two named behaviours.

What the mechanism gives, and what it does not. The SAE names nothing. It supplies directions; a judge or a researcher supplies the names afterwards. The paper's stated claim is that such directions can be intervened on: "targeted interventions on SAE-derived vectors can controllably amplify or suppress specific reasoning behaviors."[^c8] The intervention results are in the companion note on [[reflection-confidence-coupling]]. (My inference: the method removes the need for a behaviour vocabulary to be fixed in advance, which is the paper's motivation, but the vocabulary still enters when the directions are read.)

## Limits

- The theory is asymptotic. The paper's Theorem 1 says that, "as the number of samples" grows, "any local optimum of the SAE training objective" recovers the ground-truth dictionary up to permutation and scaling, under incoherence, sparsity and separation assumptions.[^c9] The experiments do not check those assumptions on the real activations; the result is a reason to expect the decoder to be meaningful, not a verification that it is.
- The evidence is one small model on one training set. The Qwen3-8B extension is reported in a figure whose values were not in the text I read.
- "Disentangled" is the stated goal, not a measured property. The evidence offered is geometric (UMAP and silhouette) plus judge labels; the paper does not report a disentanglement metric.
- The judge's labels are the only ground truth for behaviour. The agreement analysis is in an appendix I did not read.
- The "other" category is a mixture by construction, so its silhouette is not a behaviour.
- The method discovers directions that cluster; it does not show that a cluster is one reasoning move rather than a surface habit of wording. (My inference: the paper's own frequency analysis of step openers suggests cue words are the visible signal, and whether the directions track more than that is not tested here.)

## Related

- [[reflection-confidence-coupling]] — the intervention results on the reflection and confidence directions found this way
- [[cognitive-heads]] — the same family of question (which activation carries backtracking and verification) answered at attention heads, with keyword labels instead of a judge
- [[sae-uncertainty-correctness-dissociation]] — SAE features for uncertainty are tested there against correctness, which the reasoning-vector paper does not do

[^c1]: arxiv-2512-23988 — "behaviors as linear directions in the activation space, which we refer to as Reasoning Vectors"
[^c2]: arxiv-2512-23988 — "same token can play diverse roles across different contexts"
[^c3]: arxiv-2512-23988 — "reasoning steps using the delimiter symbol"
[^c4]: arxiv-2512-23988 — "reducing entanglement across vectors and enhancing interpretability"
[^c5]: arxiv-2512-23988 — "randomly sampled training examples from the MATH dataset"
[^c6]: arxiv-2512-23988 — "later layers generally achieve higher Silhouette scores than earlier ones"
[^c7]: arxiv-2512-23988 — "the comparison between reflection and backtracking reveals only modest differences"
[^c8]: arxiv-2512-23988 — "targeted interventions on SAE-derived vectors can controllably amplify or suppress specific reasoning behaviors"
[^c9]: arxiv-2512-23988 — "any local optimum of the SAE training objective"
