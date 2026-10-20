---
description: "Diffuse (high-entropy) attention heads are gradient-unstable; their mean over heads predicts an LLM answer is wrong without training, about 0.74 AUROC across 5 models and 5 datasets."
aliases: ["HeadEntropy", "softmax-Jacobian trace correctness score", "attention-spread correctness estimate"]
sources: ["arxiv-2602-13699"]
---
# Head entropy as a gradient-stability signal of answer correctness

An answerer can estimate whether its own answer is right from the spread of its attention heads, read in the same forward pass that produces the answer, with no judge model and no trained probe.

## Mechanism

For one attention row with softmax weights p, the Jacobian is diag(p) − pp⊤. Its trace equals 1 − exp(−H2), where H2 is the 2-Rényi entropy of the attention distribution.[^c1] So a head's sensitivity to gradient updates is fixed by how spread its attention is: sharp heads receive small gradients and stay put, diffuse heads remain movable by training.[^c1]

The hypothesis built on this: a correct answer rests on associations training has reinforced, carried by attention patterns training has settled; a pattern that continued training would still reshape marks a generation less grounded in the training distribution.[^c2] HeadEntropy represents each generation by its per-head attention entropies. The direction is fixed in advance: higher entropy, higher chance of an incorrect answer.[^c3]

Evidence that training does settle attention: on five OLMo-2-1B pretraining checkpoints, over 1000 TriviaQA examples, examples whose gold-answer log-probability rose most had trace fall below control at every transition (pooled −0.0035, Wilcoxon p = 1.8e-12), while unlearned examples tracked control.[^c4]

Performance: the plain mean over heads outperforms every competing training-free score by +8.9% to +75.6% relative ROC-AUC in paired comparisons across 5 models and 5 datasets, averaging 0.74 AUROC; out-of-domain it is statistically as good as a trained hidden-state probe (+0.2%).[^c5] Taking the probe away costs hidden states more than twice as much as it costs HeadEntropy: out-of-domain the probe gives up 0.131 AUROC against 0.299 for hidden states.[^c6]

## Why it matters for asking and answering

It is a answerer-side confidence channel that is neither verbalized nor sampled, and whose failure case is named: confident, fluent answers that are wrong because the relevant association was never settled (the aspirin-for-a-child example).[^c7] It separates "computes correctly" from "is grounded".

## Limits

- The training-settles-attention link is shown on one small model (OLMo-2-1B) and one dataset; the causal story from "diffuse" to "ungrounded" is the authors' hypothesis, not proved.
- The signal weakens on the non-thinking Llama-3.1-8B, which the authors leave open; it is strongest on thinking models (0.80 to 0.82 AUROC).[^c8]
- About 0.74 AUROC is modest for a high-stakes deployment; medicine is evaluated as a dataset, not as a clinical safeguard.
- White-box only: needs access to attention weights.
- My own inference: the "ungrounded" reading cannot distinguish a novel-but-correct answer from a wrong one.

## Related

- [[attention-entropy-ambiguity-signature]] — also reads attention diffusion, but as a symptom of prompt ambiguity rather than of ungrounded answers
- [[verbal-confidence-cached-retrieval]] — a verbalized-confidence channel this internal signal is an alternative to
- [[procedural-hallucination-readout-routing]] — another internal-readout route to hallucination detection

[^c1]: arxiv-2602-13699 — "The trace of the softmax Jacobian equals 1 −"
[^c2]: arxiv-2602-13699 — "A correct answer rests on associations that training has reinforced."
[^c3]: arxiv-2602-13699 — "higher entropy means a higher chance of an incorrect answer."
[^c4]: arxiv-2602-13699 — "On learned examples tr(J) falls below"
[^c5]: arxiv-2602-13699 — "Out-of-domain, the untrained"
[^c6]: arxiv-2602-13699 — "Hidden states match H EAD E NTROPY"
[^c7]: arxiv-2602-13699 — "The dose calculation is correct, and the model"
[^c8]: arxiv-2602-13699 — "On thinking models the signal is"
