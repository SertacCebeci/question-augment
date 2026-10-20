---
description: "Pruning low-attention tokens during decoding can delete visually critical ones; a medical LVLM study reports that vision-agnostic pruning worsens hallucination."
aliases: ["visual token pruning", "token sparsification in LVLM decoding", "vision-aware token selection", "VATS"]
sources: ["arxiv-2512-01922"]
---
# Visual token sparsification and hallucination

A vision-language decoder generates each token against a cache of earlier keys and values, and the image contributes a large share of them. Sparsifying the decoder keeps some of these tokens and masks the rest, with the aim that attention over the kept tokens stays close to attention over all of them. The Med-VCD paper states this as a constrained choice: "a constrained optimization framework designed to simultaneously reduce the approximation error" between sparse and full attention scores, while keeping the number of retained tokens fixed.[^v1]

The mechanism the paper builds on is that the choice of what to prune has a visual cost. Its central empirical claim is that sparsification which ignores the image worsens hallucination: "ened by vision-agnostic token sparsification" is the paper's own wording for that effect.[^v2] The reason it offers is that tokens with low attention can still matter for what the picture shows. Pruning them "may exacerbate visual hallucination phenomena".[^v3]

The remedy is a per-token score. Each token's score adds an attention-relevance term to a visual saliency term, and the top-S tokens by that score are retained. The saliency term is computed from attention, not from a separate model: "The visual saliency scores originate from the attention" weights of produced and image tokens.[^v4] The retention rule is therefore a way of keeping the tokens that both the decoder attends to and that carry the image.

The ablation points the same way. Removing the whole sparsification module "reduces both model accuracy and decoding speed", and the authors read the partial sparsification as useful because it "can alleviate linguistic bias in Med-LVLMs by reducing the influence of specific tokens during attention operation".[^v5][^v6] The lesson is not that sparsity is good in itself. Sparsity that keeps the visually salient tokens reduces the language bias; sparsity that does not keep them, on the paper's account, increases hallucination.

The reported setting uses a sparsity rate tied to the sequence length: "The sparsity rate is established as 0.8 times the sequence" length, with a separate masking rate for image tokens.[^v7]

## Limits

- The "worsened" claim rests on attention analysis of one model, LLaVA-Med-1.5, run on a random subset of one benchmark's images: "Evaluations were conducted on a randomly selected subset comprising 20% of the benchmark images."[^v8] The text read here gives no before-and-after number for vision-agnostic sparsification alone, so the size of the effect is not established by this note.
- The sparsity rate (0.8 of the sequence) and the masking rate were set for these experiments. The text read here does not show how they were chosen or how the results move with them (my reading).
- A saliency score built from attention inherits attention's own biases. The same method penalises over-attended tokens in a separate step, which is a different mechanism; see [[attention-sink]]. Whether the two steps interact is not tested in the text read here (my inference).
- The headline gains, "raises factual accuracy by an average of 13%", are averages over the paper's own medical benchmarks and its chosen backbone.[^v9] They are not checked here.
- The finding is about decoding-time pruning in one architecture family. Transfer to other vision-language architectures is untested in this text (my inference).

## Related

- [[null-image-logit-subtraction]] — the contrast this method builds on; here the contrasting input is the image with visual tokens masked, not a blank image
- [[attention-sink]] — over-attended tokens, penalised in the same method by a second, calibration step
- [[initial-token-saliency]] — another attention bias that weights tokens by salience; here the weight is a visual saliency score rather than position relative to the first token

[^v1]: arxiv-2512-01922 — "a constrained optimization framework designed to simultaneously reduce the approximation error"
[^v2]: arxiv-2512-01922 — "ened by vision-agnostic token sparsification"
[^v3]: arxiv-2512-01922 — "may exacerbate visual hallucination phenomena"
[^v4]: arxiv-2512-01922 — "The visual saliency scores originate from the attention"
[^v5]: arxiv-2512-01922 — "Eliminating the VATS mechanism reduces both model accuracy and decoding speed"
[^v6]: arxiv-2512-01922 — "partially sparsifying the decoding sequence can alleviate linguistic bias in Med-LVLMs"
[^v7]: arxiv-2512-01922 — "The sparsity rate is established as 0.8 times the sequence"
[^v8]: arxiv-2512-01922 — "Evaluations were conducted on a randomly selected subset comprising 20% of the benchmark images"
[^v9]: arxiv-2512-01922 — "raises factual accuracy by an average of 13%"
