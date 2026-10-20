---
description: "Some decoder tokens in vision-language models absorb attention far beyond their visual content; a medical LVLM method measures this cumulative attention and down-weights it."
aliases: ["attention sinking", "sinking attention calibration", "over-activated tokens", "attention sink calibration"]
sources: ["arxiv-2512-01922"]
---
# Attention sink

In a vision-language decoder, some tokens draw attention far out of proportion to what they contribute to the picture. The attention they take is not spent on the image, and the decoder's next choice can rest on it anyway. The Med-VCD paper calls this attention sinking and places it in LVLMs, citing earlier work for its existence: it refers to a "sinking phenomenon in LVLMs".[^a1]

The paper measures severity per token. It takes "each token's cumulative attention score" by aggregating the attention each token receives across sequential queries, then normalises those sums with a softmax into penalty weights.[^a2] The quantity is therefore a running total of attention received, turned into a relative weight over the sequence. A token that many later queries attend to, whatever its visual content, gets a large weight.

The correction is a reweighting of the attention scores, not a change to the model. The penalised attention is written as (1+β) times the raw query-key score minus β times the weighted score, so a heavily weighted token loses attention in proportion to β. The paper says this "dynamically suppresses over-activation" of tokens that absorb attention without visual content, while keeping attention to visually salient patterns.[^a3] The mechanism is a rescaling per key, so it changes the distribution the decoder uses to pick the next token.

For someone asking or answering with these models, the concept says where a model's attention can go without the picture. An answer can be produced with most of the attention on tokens that carry no image content. That is an inference from the mechanism; the text read here does not test answer quality against sink severity.

## Limits

- The existence of the phenomenon is taken from earlier work in the paper's motivation. The paper's own evidence is the severity measure. The text read here gives no distribution of sink severity across layers, models or decoding steps, so the frequency of the phenomenon is not established by this note.
- The penalty has a hyperparameter β, and the paper fixes it at a single value for its experiments: "The hyperparameters β, α, and λ are configured to 0.1".[^a4] The ablation tables for these hyperparameters exist in the paper, but their values were not read here, so no sensitivity claim is made.
- The paper's ablation includes a version without the calibration step. Its effect is not reported in this note, because the numbers were not read; the claim that calibration helps therefore rests on a table this note has not checked.
- The method is tested on one backbone, LLaVA-Med-1.5 with a 7B decoder, and on medical VQA and report generation. Whether the same penalty helps other architectures or natural-image tasks is untested here.
- The paper treats over-activation on these tokens as harmful. The text read here does not test the alternative that the high-attention tokens carry some useful summary of the context (my reading).

## Related

- [[visual-token-sparsification-hallucination]] — the same method's other step; pruning by attention and reweighting attention both act on the attention weights, and the first decides which tokens remain
- [[null-image-logit-subtraction]] — the other inference-time correction in the same paper's family of methods, acting on the output logits rather than on attention

[^a1]: arxiv-2512-01922 — "sinking phenomenon in LVLMs"
[^a2]: arxiv-2512-01922 — "To quantify the severity of attention sinking, we compute"
[^a3]: arxiv-2512-01922 — "This formulation dynamically suppresses over-activation"
[^a4]: arxiv-2512-01922 — "The hyperparameters β, α, and λ are configured to 0.1"
