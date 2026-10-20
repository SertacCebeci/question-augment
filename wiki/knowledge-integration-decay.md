---
description: "In search-augmented reasoning, the longer the reasoning before a search, the worse the model uses retrieved evidence, because earlier reasoning tokens dominate attention while the document is encoded."
aliases: ["KID", "utilization bottleneck", "reasoning-induced knowledge interference"]
sources: ["arxiv-2602-09517"]
---
# Knowledge Integration Decay

Knowledge Integration Decay (KID) is the finding that a model which interleaves reasoning and search stops using retrieved evidence well as the reasoning written before the search grows longer. The setup was 2WikiMultihopQA under an idealized search, where the model reasons, searches once, and answers from the retrieved evidence. Accuracy under the Search-o1 prompting framework declined as pre-search reasoning lengthened, even though the evidence was sufficient.[^c1]

## Mechanism

The authors define an interference strength: how much attention the tokens of the retrieved document place on the pre-search reasoning, relative to the document's own content. It is averaged over all heads and layers, and measured on Qwen3-4B-Thinking. Under Search-o1 it rose sharply with reasoning length.[^c2] Their reading is that earlier reasoning dominates attention while the document is encoded, so the representation of the new evidence is distorted or weakened and then underused in the final answer.[^c3] This is a correlational attention analysis plus an intervention, not a causal proof by ablation of heads.

## Consequences for answering

- Search-o1 sometimes underperforms plain one-shot RAG, which the authors attribute to KID.[^c4]
- Improving retrieval (an "Easy Search" setting with a small set of highly relevant documents) gave only marginal gains for the baseline. The authors call this a "utilization bottleneck": even with perfect information retrieved, the model struggles to use it.[^c5]

## The mitigation as evidence

Self-Anchored Knowledge Encoding (SAKE) places retrieved documents twice: in a cumulative knowledge stack at the start of the context, as a semantic anchor, and again after the reasoning step.[^c6] Under SAKE, performance stayed stable as pre-search reasoning grew, and interference grew much more slowly.[^c7] Two controls separate this from trivial explanations. Duplicating the document right after the reasoning ("Repeat") gave little or no gain, so repetition alone does not explain it. A "Stack Only" variant beat Search-o1 but fell short of full SAKE, so clean encoding without contextualization in the reasoning is not enough.[^c8]

## Limits

- Evidence comes mainly from 2WikiMultihopQA with a single idealized search and one small model for the attention analysis; the generality across models and multi-search runs is supported only by benchmark gains (HotpotQA, MuSiQue, FRAMES), not by the interference metric.
- The attention metric is a proxy for encoding distortion; the paper does not show that lowering attention to reasoning is the only route to the gain.
- Placing the document early may help for reasons other than shielding (for example, position effects); the Repeat control addresses only duplication.
- Reasoning length is manipulated by the experimenter; whether naturally long reasoning is harmful in the same way is my inference, not tested here.

## Related

- [[contextual-inertia]] — a model's earlier output in context biases later answers, a close cousin in multi-turn dialogue
- [[fact-attenuation]] — facts found upstream are lost downstream; here the loss happens inside one context
- [[plan-before-search-anchoring]] — another way of keeping retrieval from being bent by earlier context
- [[retrieval-state-drift]] — search-agent failure after retrieval is correct

[^c1]: arxiv-2602-09517 — "we observe that as the length"
[^c2]: arxiv-2602-09517 — "Under the Search-o1"
[^c3]: arxiv-2602-09517 — "As the pre-search"
[^c4]: arxiv-2602-09517 — "It is worth noting that the Search-o1"
[^c5]: arxiv-2602-09517 — "utilization bottleneck"
[^c6]: arxiv-2602-09517 — "a cumulative knowledge stack that serves"
[^c7]: arxiv-2602-09517 — "SAKE maintains remarkable stability"
[^c8]: arxiv-2602-09517 — "the effectiveness of SAKE cannot be attributed to simple repetition"
