---
description: "Near-tie distractors inflate the softmax denominator and dilute attention on the evidence; holding it needs a logit margin growing like log T, which extra generated tokens do not supply."
aliases: ["attention dilution", "softmax dilution of the needle", "distractor dilution in static attention"]
sources: ["arxiv-2512-13898"]
---
# Score dilution

In a single softmax attention layer with fixed weights, the share of attention a query gives its evidence key shrinks as competing keys accumulate. The mechanism is the denominator. Attention is a normalized exponential of logits, so when many distractor keys sit within a few logits of the evidence key, the normalizing mass is spread over them and the evidence's share falls. The paper calls this score dilution, "a phenomenon inherent to static self-attention."[^c1] Its lemma gives the bound: if at least m distractor keys have logits within Δ of the target's, the target's attention weight is at most 1/(1 + m e^(−Δ)). When m grows with the context length T and Δ is of order one, that bound goes to zero as T grows.[^c2] The paper's gloss is "This lemma formalizes a simple intuition": a constant fraction of tokens near the evidence's logit leaves the attention budget no way to concentrate.[^c2]

The consequence the paper draws is a margin requirement. Fix a target mass 1 − ε against worst-case distractors; the logit gap between target and every distractor must be at least log((T − 1)(1 − ε)/ε), so the gap has to grow as log T.[^c3] A model with fixed weights has no reason to produce such a gap at every length, and the paper's position is that static attention generally does not.[^c3]

Generated tokens do not get around this. The paper proves that any token produced after the evidence, with the same static attention, carries at most its own attention mass on the evidence as evidence signal.[^c4] Under dilution that mass is small, so thinking tokens cannot materially raise the answer's effective margin unless some intermediate token has already attended to the evidence.[^c4] The paper's takeaway is that a successful inference-time strategy has to change the similarity between query and key, "rather than sampling more tokens with unchanged parameters."[^c5]

The empirical side is two synthetic tasks, bug localization in code repositories and anomaly detection in transaction logs. In-context accuracy falls as context length grows, and thinking tokens "show diminishing returns."[^c6] The paper also measures attention mass on the target tokens across layers: for vanilla attention it "goes down drastically" as the number of input tokens rises.[^c7]

What the mechanism says about answering, as my inference and not the paper's claim: when the evidence is buried among near-tie passages, a longer chain of reasoning on the same static attention adds tokens without adding access, so the bottleneck is what the answerer can reach, not how much it writes. This is a reading of the bound, not a tested prescription.

## Limits

- The bounds concern one attention layer with fixed weights, and the worst case: the lemma assumes m distractors within Δ of the target, which is an adversarial configuration. The paper does not measure how often real long-context text reaches it.
- The Ω(log T) requirement is a worst-case necessity for a guaranteed mass. It says nothing about the margins real models actually have, and the paper does not report them.
- The paper attributes long-context failures to score dilution. Its evidence is the synthetic tasks and target attention mass on those tasks; the link to real benchmarks is the authors' reading, which they phrase as "validating the score dilution diagnosis."[^c8] The paper itself treats position sensitivity as a separate effect, the "lost in the middle" pattern, citing it in prior work.[^c9] Whether position bias, rather than dilution, explains a given failure is not separated here.
- The bounds are stated for a single head's softmax; the aggregation across heads is treated in an appendix and is not tested on the benchmarks in the same way.

## Related

- [[query-only-test-time-training]] — the intervention the paper derives from this mechanism: a few updates on the query side, which raise the margin without changing the keys and values.
- [[cot-token-complexity-lower-bound]] — another bound on what generated tokens can do, from communication complexity rather than attention weights.
- [[distractor-similarity-reasoning-inflation]] — the same kind of distractor effect observed in reasoning traces, where incorrect answers put more attention on distractor tokens.

[^c1]: arxiv-2512-13898 — "We attribute these failures to score dilution, a phenomenon inherent to static self-attention."
[^c2]: arxiv-2512-13898 — "This lemma formalizes a simple intuition"
[^c3]: arxiv-2512-13898 — "guaranteeing a fixed target mass against worst-case distractors requires a gap"
[^c4]: arxiv-2512-13898 — "so attending to thinking tokens cannot materially increase the final answer"
[^c5]: arxiv-2512-13898 — "rather than sampling more tokens with unchanged parameters"
[^c6]: arxiv-2512-13898 — "thinking tokens show diminishing returns"
[^c7]: arxiv-2512-13898 — "attention mass for vanilla attention goes down drastically"
[^c8]: arxiv-2512-13898 — "validating the score dilution diagnosis"
[^c9]: arxiv-2512-13898 — "However, these LLMs still exhibit strong position sensitivity"
