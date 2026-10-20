---
description: "Per-layer linear probes on token-pooled hidden states, restricted to middle layers, quantile-normalized and combined by a regression, so one score uses many depths instead of a fixed one."
aliases: ["multi-layer probe fusion", "cross-layer hidden-state aggregation", "layer-ensemble probe"]
sources: ["doi-10-48550-arxiv-2603-05471", "arxiv-2511-19806"]
---
# Cross-layer probe ensemble

A probe on an LLM's hidden states has to choose where to read. The usual choices are one layer, often a middle one, and one token, often the first or last generated. The paper argues that this fixed choice is a weak assumption: "Instead, it proposes leveraging all" token-level states, aggregated across layers, because "relying on fitted token-level uncertainty scores may not be the optimal solution" for generalization.[^c1][^c2]

The mechanism has four steps, each a plain operation.

First, pooling inside a layer. A learnable vector θ scores each token, and the sequence embedding is the softmax-weighted sum of that layer's token states: "We compute a sequence-level embedding using a learnable parameter vector θ for a given sequence."[^c3]

Second, a per-layer verdict. A linear classifier with learnable weights W, passed through a sigmoid, gives each layer its own probability that the claim is true: "we apply a linear classifier with learnable weights W on top of the sequence-level embeddings from each layer."[^c4]

Third, a restricted set of depths. The paper keeps only the middle layers, because the first and last are less effective: "last layers to be less effective, we use only the middle layers."[^c5] Concretely, "We use the layers from the first third to the second third of" the model[^c6], for example "layers 11 to 22 for Llama 3.1-8B-Instruct."[^c7]

Fourth, normalize, then regress. Raw per-layer probabilities are on incomparable scales, and the paper argues that they "are not standardized across layers, which could degrade the performance of the regressor."[^c8] Each layer's probabilities are quantile-normalized, then a linear regression with learnt per-layer weights and a bias gives the final score: the paper "train[s] a regression model on top of" the layer-wise probabilities.[^c9] Training data are split so that the first part fits θ and W and the second part fits the layer weights and bias: "the first is used to fit the parameters θ and W, while"[^c10] the rest fits the combination.

Why combine rather than pick. The best depth moves with the data: "Although the most effective layer varies across datasets"[^c11], and intermediate layers in general do better than the first and last.[^c12] The combined score is reported to do at least as well as the best single layer: "or exceeding that of the best individual layer, highlighting the advantage of integrating information"[^c13] across layers. A single middle layer is worse than a set of them: "using a single middle layer performs significantly worse than training on a"[^c14] set of middle layers. Training on the first or last layers alone "is generally ineffective for claim verification tasks."[^c15]

The transferable part is the principle, not the numbers. A regression over several depths lets the fitted weights choose depth per task, and a normalization step makes depths comparable before they are combined. The paper's reading of its own result is that "middle layers emerge as especially informative, suggesting that training should explicitly focus on these representations."[^c16]

A second rule combines depths by vote instead of regression. In a VLM abstention study each layer gets its own probe, the layers are chosen on a validation set, and the verdicts are merged afterwards. The study selects "the top-K layers with highest abstention accuracy," and at inference "we aggregate predictions through majority voting."[^c18][^c19] The count is set by hand: "In our experiments, we set K = 5."[^c20] The vote needs no learned layer weights and no quantile step, so it drops the two fitted parts that the regression above depends on. It also gives every kept layer the same weight, which is my inference rather than a result the paper reports.

## Limits

- The window is given as a fraction of depth, a third to two thirds of the model, and the only worked example in the sections I read is one 8B model. Whether the same window holds for much deeper or shallower models is not tested in those sections.
- The quantile step is argued, not isolated. The paper says raw probabilities "could degrade" the regressor; I did not see a run that removes the step and measures the loss.
- The method is supervised. It fits θ, W and the layer weights on labelled claims, and the paper's own caution applies: "the performance of supervised methods often degrades in out-of-distribution scenarios."[^c17] The reported robustness is across its nine datasets, not across every claim distribution.
- It reads hidden states, so it needs access to the model's internals. That is my inference from the design, not a limit the paper states.
- The aggregation is across depth only. The inputs are hidden states; token-level likelihoods and attention are not combined in this formulation. Combining depth with signal type is a separate question, and the paper does not test it here.
- The depth profile is not uniform across tasks. In a VLM abstention study, abstention accuracy "exhibits a clear rise-then-fall trend" on three datasets, but on one benchmark "accuracy remains consistently high across most layers after initial rise."[^c21][^c22] A middle-layer peak is a property of the task and model, not a fixed depth window.

## Related

- [[retrieval-free-fact-checking]] — the task these probes were measured on, where the layer ensemble is the strongest reported readout
- [[nonlinear-hidden-state-probe]] — fixes the readout's shape (linear versus nonlinear) where this note fixes the depths it reads
- [[single-pass-internal-signal-detector]] — fuses signal types (likelihood, entropy, a hidden embedding) rather than depths
- [[trajectory-geometry-uncertainty-probe]] — also reads across layers, but from the path of per-layer MLP updates, not from per-layer verdicts
- [[latent-representation-abstention-probe]] — the top-K per-layer vote applied to a VLM's abstention on OCR answers

[^c1]: doi-10-48550-arxiv-2603-05471 — "Instead, it proposes leveraging all"
[^c2]: doi-10-48550-arxiv-2603-05471 — "relying on fitted token-level uncertainty scores may not be the optimal solution"
[^c3]: doi-10-48550-arxiv-2603-05471 — "We compute a sequence-level embedding using a learnable parameter vector θ for a given sequence"
[^c4]: doi-10-48550-arxiv-2603-05471 — "we apply a linear classifier with learnable weights W on top of the sequence-level embeddings from each layer"
[^c5]: doi-10-48550-arxiv-2603-05471 — "last layers to be less effective, we use only the middle layers"
[^c6]: doi-10-48550-arxiv-2603-05471 — "We use the layers from the first third to the second third of"
[^c7]: doi-10-48550-arxiv-2603-05471 — "layers 11 to 22 for Llama 3.1-8B-Instruct"
[^c8]: doi-10-48550-arxiv-2603-05471 — "are not standardized across layers, which could degrade the performance of the regressor"
[^c9]: doi-10-48550-arxiv-2603-05471 — "train a regression model on top of"
[^c10]: doi-10-48550-arxiv-2603-05471 — "the first is used to fit the parameters θ and W, while"
[^c11]: doi-10-48550-arxiv-2603-05471 — "Although the most effective layer varies across datasets"
[^c12]: doi-10-48550-arxiv-2603-05471 — "intermediate layers generally yield better performance"
[^c13]: doi-10-48550-arxiv-2603-05471 — "or exceeding that of the best individual layer, highlighting the advantage of integrating information"
[^c14]: doi-10-48550-arxiv-2603-05471 — "using a single middle layer performs significantly worse than training on a"
[^c15]: doi-10-48550-arxiv-2603-05471 — "training only on the first or last layers is generally ineffective for claim verification tasks"
[^c16]: doi-10-48550-arxiv-2603-05471 — "middle layers emerge as especially informative, suggesting that training should explicitly focus on these representations"
[^c17]: doi-10-48550-arxiv-2603-05471 — "the performance of supervised methods often degrades in out-of-distribution scenarios"
[^c18]: arxiv-2511-19806 — "the top-K layers with highest abstention accuracy"
[^c19]: arxiv-2511-19806 — "At inference, we aggregate predictions through majority voting"
[^c20]: arxiv-2511-19806 — "In our experiments, we set K = 5"
[^c21]: arxiv-2511-19806 — "exhibits a clear rise-then-fall trend"
[^c22]: arxiv-2511-19806 — "accuracy remains consistently high across most layers after initial rise"
