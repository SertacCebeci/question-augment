---
description: "A token draws attention in proportion to its weight relative to the initial token; this initial saliency, besides position, shapes the U-shaped attention curve over long prompts."
aliases: ["initial saliency", "initial token weight", "attention saliency relative to the first token", "initial-token attention bias"]
sources: ["arxiv-2512-13109"]
---
# Initial-token saliency

When a language model predicts the next token, the attention each earlier token receives depends on two things: how relevant it is to the last token, and a bias that depends on where it sits. The positional part of that bias is the familiar one. The U-shaped attention curve "is often attributed" to position encoding, which favours tokens close to the last position.[^c1] Qiang et al. add a second term. Initial saliency is the tendency of a token to receive more attention when its attention weight relative to the initial token is higher: the authors say tokens are favoured through their "attention weights relative to the initial token".[^c2]

The two terms are written as a bias at position i, pos(i) + sal(i). The position term pos(i) increases monotonically with position; the saliency term sal(i) decreases monotonically. Their opposing trends "produce a U-shaped attention pattern."[^c3] The authors' complaint about existing fixes is that they "overlook sal(i)": scaling relative positions does not reach a term that, unlike pos(i), is tied to absolute position.[^c16]

Why sal(i) falls with position has a simple arithmetic part. Attention over a prefix sums to one, and as "input text length increases and l becomes larger," the weight on the initial token tends to decrease.[^c4] Tokens near the start then have relatively higher weight against it, which is the "sequence have relatively higher attention weights" pattern the authors describe.[^c5] The cause of the initial token's own weight is less settled. One candidate, in the authors' words, "is that the initial token often acts as an attention" sink: it draws high attention despite carrying little content.[^c6][^c7]

The direct test is an intervention. On 200 MDQA question-answer pairs, the authors lowered the attention between the initial token and tokens in the first two documents, raised it for tokens in the fifth and sixth, and observed the top-30% attention distribution in Llama-7B, Vicuna-7B and Tulu-7B. Lowering the initial-token weight reduced attention to early positions, and raising it increased attention to middle ones. The authors read this as "direct evidence for the existence of initial saliency."[^c8]

The same reasoning is then used as a calibration: rescale the initial-token attention by a location-dependent factor, reducing it where attention is dense and raising it where attention is sparse, on selected layers only. The reported gains are improvements of 1.2% to 9.2% for key information in middle positions, and at most 3.6% on MDQA and KV-Retrieval.[^c9][^c10] Combined with an existing position-scaling method, the authors report a maximum of "3.4% in KV-Retrieval tasks."[^c11]

## Limits

- The authors do not claim to exhaust the causes: their study does not "conclusively rule out the possibility that factors" beyond initial saliency and position encoding.[^c12]
- The origin of initial saliency is incomplete in the paper. The attention-sink account is offered as "one possible cause", not tested as the cause.
- The evidence is a handful of 7B-class open models (the text lists "LLaMA-2-7B" among them) and two benchmarks, MDQA and KV-Retrieval. Scaling is applied at chosen layers, and the authors note that scaling "is not necessary at every layer."[^c13][^c14]
- The authors also suggest that U-shaped attention "may have an inherent rationale", since critical information in real text often sits at the start and end of a sequence, and training may make that pattern optimal.[^c15] The calibration is therefore shown to help on these benchmarks, not to be the correct attention pattern in general.
- The scaling factor is a hyperparameter per location and layer. In the parts I read, the text gives no rule that carries it to a new model or task; that transfer is not established here.

## Related

- [[reader-slot-zero-primacy]] — a behavioural slot-0 effect whose mechanism its authors leave open; initial saliency is one candidate for the positional side of that effect.
- [[embedding-retriever-position-bias]] — position bias measured in dense retrievers, a different model class with a different locus.

[^c1]: arxiv-2512-13109 — "The U-shaped attention curve is often attributed"
[^c2]: arxiv-2512-13109 — "attention weights relative to the initial token"
[^c3]: arxiv-2512-13109 — "produce a U-shaped attention pattern."
[^c4]: arxiv-2512-13109 — "input text length increases and l becomes larger,"
[^c5]: arxiv-2512-13109 — "sequence have relatively higher attention weights"
[^c6]: arxiv-2512-13109 — "is that the initial token often acts as an attention"
[^c7]: arxiv-2512-13109 — "substantial semantic information, consistently receive high attention"
[^c8]: arxiv-2512-13109 — "The results provides a direct evidence for the existence of initial saliency"
[^c9]: arxiv-2512-13109 — "improvements ranging from 1.2% to 9.2% were"
[^c10]: arxiv-2512-13109 — "achieving a maximum improvement of 3.6% in"
[^c11]: arxiv-2512-13109 — "3.4% in KV-Retrieval tasks."
[^c12]: arxiv-2512-13109 — "conclusively rule out the possibility that factors"
[^c13]: arxiv-2512-13109 — "LLaMA-2-7B (Touvron et al., 2023)"
[^c14]: arxiv-2512-13109 — "is not necessary at every layer."
[^c15]: arxiv-2512-13109 — "U-shaped attention may have an inherent rationale."
[^c16]: arxiv-2512-13109 — "However, both approaches overlook sal(i)."
