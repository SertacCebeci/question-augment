---
description: "Next-token probability splits exactly into additive shares from the embedding, each attention and FFN block and the final LayerNorm, each read by an unembedding probe."
aliases: ["logit-lens decomposition", "residual-stream probability attribution", "probe-difference attribution"]
sources: ["arxiv-2512-07515"]
---
# Residual-stream probability decomposition

A transformer's residual stream is a running sum: the input embedding, plus the output of each attention block and each feed-forward (FFN) block, plus a final LayerNorm adjustment. The decomposition reads an intermediate state through the unembedding matrix to get the probability of the target token, and takes the change in that probe across one block as the block's share. The probe is the logit-lens idea: Φ(h, y) is the softmax probability of token y read from a hidden state h, "the hypothetical probability of the target token y given" that state.[^c1] Each component's share is the change it induces: the embedding's share is the probe on the initial state; a block's share is the probe after the block minus the probe before it; the final LayerNorm's share is the model's actual output probability minus the probe on the last layer's state.[^c2] The paper states that the shares add up to the output: "The final probability for a target token y is exactly" the embedding share, plus the block shares, plus the LayerNorm adjustment.[^c3]

The identity holds for the sum, not for every finer split. Because the probe passes through a softmax, probing each attention head separately does not add up to the attention block's share: "the sum of probability changes calculated by probing individual heads does not equal" the block's contribution.[^c4] The workaround is to work in logit space. Each head's logit contribution to the target is a dot product of its projected output with the target's unembedding vector, and the block's probability change is divided among heads "proportional to its exponential logit contribution."[^c5] The paper's approximation for this step is a first-order one, which it takes for efficiency: "the first-order term for efficiency."[^c6]

Attention is then split by source. For the attention block, the paper "further distribute[s] its contribution to" the query, the retrieved context, earlier generated tokens and the current token, using the attention weights each head puts on each group of positions and summing over heads.[^c7] The result is seven shares per token: query, RAG context, past tokens, self token, FFN, final LayerNorm and initial embedding. Those seven "sum to the token's final probability."[^c8]

This is a different object from the probability itself. A probability says how likely the token is; the decomposition says which part of the residual stream supplied that likelihood. The wiki's [[parametric-suppression]] note records logit-lens readings in which a gold answer peaks in middle layers and then falls; a decomposition of the same kind would name the block that did the falling, which is the step that note's FFN-overwrite account needs and does not measure. The paper's motive for the split is that the common framing is too narrow. Prior approaches attribute hallucinations "to a binary conflict between" FFN-stored knowledge and the retrieved context.[^c9] In the paper's own detector, "Relying solely on the binary conflict between" those two sources "is insufficient for robust detection."[^c10][^c11]

## Limits

- The shares are attributions, not interventions. A logit-lens reading says how the probability was built up along the stream; it does not say what the output would become if a block were removed. This is my inference from the probe's definition, and the paper's own word is "attribution."
- The exact identity is at block level. Head-level and source-level shares depend on a chosen rule, the softmax over head logits and the attention weights. The excerpt I read gives no sensitivity analysis for those rules, and it gives no bound on the first-order error term it drops.
- The method needs white-box access: "it relies on white-box access to model internals, preventing application to closed-source APIs."[^c12]
- It is costly: "the decomposition incurs higher computational overhead than simple scalar probes."[^c13]
- Scope. The paper defines the target phenomenon narrowly: "we define a hallucination as a response" containing content inconsistent with the retrieved context, assuming that context is relevant and correct.[^c14] The shares say nothing about factuality outside that frame.
- The paper claims that its detector "achieves state-of-the-art performance,"[^c15] on five open models. I did not read the results table, so that claim is not checked here, and the usefulness of the shares for detection is the paper's finding, not one this note establishes.

## Related

- [[parametric-suppression]] — the logit-lens reading of a suppressed gold answer; this decomposition would assign the suppression to a named block, a step that note does not measure
- [[single-pass-internal-signal-detector]] — one-pass detectors over internal signals; these shares are another internal signal, read without sampling
- [[null-image-logit-subtraction]] — another route to separating the context's contribution from the prior, by contrasting with a null pass
- [[pos-stratified-source-attribution]] — aggregates these per-token shares by part of speech

[^c1]: arxiv-2512-07515 — "hypothetical probability of the target token y given"
[^c2]: arxiv-2512-07515 — "induces in the probe output"
[^c3]: arxiv-2512-07515 — "The final probability for a target token y is exactly"
[^c4]: arxiv-2512-07515 — "the sum of probability changes calculated by probing individual heads does not equal"
[^c5]: arxiv-2512-07515 — "proportional to its exponential logit contribution"
[^c6]: arxiv-2512-07515 — "the first-order term for efficiency"
[^c7]: arxiv-2512-07515 — "we further distribute its contribution to"
[^c8]: arxiv-2512-07515 — "sum to the token’s final probability"
[^c9]: arxiv-2512-07515 — "Prior approaches attribute hallucinations to a binary conflict between"
[^c10]: arxiv-2512-07515 — "Relying solely on the binary conflict between"
[^c11]: arxiv-2512-07515 — "is insufficient for robust detection"
[^c12]: arxiv-2512-07515 — "it relies on white-box access to model internals"
[^c13]: arxiv-2512-07515 — "the decomposition incurs higher computational overhead than simple scalar probes"
[^c14]: arxiv-2512-07515 — "we define a hallucination as a response"
[^c15]: arxiv-2512-07515 — "TPA achieves state-of-the-art performance"
