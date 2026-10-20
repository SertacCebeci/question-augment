---
description: "Breadth (entropy of a generator's messages) and decipherability (mutual information with audience readings) trade off along one generation knob; capacity is the best decipherability reachable."
aliases: ["semiotic capacity", "breadth-decipherability trade-off", "semiotic breadth and decipherability"]
sources: ["arxiv-2511-19550"]
---
# Semiotic channel capacity

Picca treats a language model as a "stochastic semiotic engine" whose outputs a human must interpret, and proposes to measure how much meaning such an output can carry to a given audience. The framework has two quantities. Breadth is the entropy of the message source: "semiotic breadth is quantified as the source entropy"[^c1], written $S = H_{A,Ctx}(M)$ for a given audience and context. Decipherability is the mutual information between a message and the interpretation an audience gives it, $D = I(M;\mathrm{Int}) = H(\mathrm{Int}) - H(\mathrm{Int}\mid M)$. The paper's definition is that "decipherability is measured by the mutual information between messages"[^c2], and "It quantifies the reduction in uncertainty about an interpretation that results from" observing the message.[^c3] So breadth is a [[entropy|source entropy]], while decipherability is a [[mutual-information]] whose second variable is a human reading, not the source's own symbols.

A generation knob ties the two together. The paper introduces "a control parameter λ representing the generative complexity of the source (e.g., LLM" sampling temperature, which tunes the message distribution.[^c4] Because the distribution moves with λ, both S and D become functions of λ. The shapes are postulated, not derived: "We postulate two hypotheses about these functions." S(λ) is monotonically increasing, and D(λ) is "unimodal as a function of the generative complexity", peaking at an optimum λ_opt for a given channel.[^c5][^c6] The trade-off follows from this shape: raising λ buys breadth, but "rising λ beyond λopt causes decipherability (D) to decrease."[^c7]

The capacity of the semiotic channel, for a fixed audience and context, is defined as the peak of this curve, "the maximum decipherability achievable by optimizing λ"[^c8]: $C_{A,Ctx} = \max_\lambda D_{A,Ctx}(\lambda)$. The name comes from communication theory, where the channel has a capacity limit ([[channel-capacity]]). Here the audience and context play the part of the channel, and the generated message distribution plays the part of the input. The paper also asserts that the constraint $D(\lambda) \le S(\lambda)$ "holds for all values of λ."[^c9] Read through the two definitions, this is $I(M;\mathrm{Int}) \le H(M)$, which holds for any joint distribution. That step is my inference; the paper gives the inequality without a derivation.

For prompting, the framework reads the prompt as a control on the message distribution. A vague prompt "leaves high openness, resulting in high S and" potentially low D. A specific prompt "narrows the interpretive space, increasing D."[^c10][^c11] The residual ambiguity is the conditional entropy H(Int|M), which the paper names "the effective polysemy of a text for a given audience and context."[^c12] Decipherability is not truth: "A message can be highly decipherable yet factually incorrect, and vice-versa."[^c13]

## Limits

- Nothing here is measured. The paper proposes estimating S by entropy and D from interpretation distributions, but the "Poet" and "Technician" profiles and the prompt examples are illustrations. Human interpretation "is inherently subjective, context-dependent, and difficult to quantify."[^c14] Breadth "necessarily relies on proxies."[^c15]
- Unimodality of D(λ) is a postulate. The framework does not say what happens when D is monotone in λ on some channel, in which case the optimum sits at a boundary of the λ range.
- λ is a single scalar. Prompt persona cues and negative instructions are named as things to measure "by measuring changes in D and S as a function of prompt specificity, persona cues, or negative"[^c16] but the paper tests none of them.
- The optimisation is not always the goal. The paper concedes that "this assumption does not hold in domains where ambiguity, multiplicity, or interpretive" openness are valued, such as art or poetry, where low decipherability may be intended.[^c17]
- The model is static: "The present model does not capture this diachronic evolution."[^c18] The paper also presents itself as "not as a universal theory of artificial communication, but as a targeted and powerful tool."[^c19]
- Shannon capacity is defined for a fixed, known channel law. Here the audience's interpretation distribution is estimated, not known. My inference: the paper's C maximises over one temperature family of input laws, so it is at most the best over all input laws, and therefore a lower bound on the channel's capacity in Shannon's sense. The paper does not make this comparison.

## Related

- [[channel-capacity]] — the analogy's source; the paper's C is a maximum over one family of input distributions, not over all of them (my inference, see Limits)
- [[mutual-information]] — D is this quantity with human interpretations as the second variable
- [[entropy]] — S is the ordinary Shannon entropy of the message source, with no new definition
- [[interpretation-breadth-depth-asymmetry]] — a different breadth: that note counts how many readings an answer addresses, while S here is the entropy of the messages themselves
- [[interpretive-gap]] — the gap between observable behaviour and the reason a user has for it; the same interpretive side of communication, measured differently

[^c1]: arxiv-2511-19550 — "semiotic breadth is quantified as the source entropy"
[^c2]: arxiv-2511-19550 — "decipherability is measured by the mutual information between messages"
[^c3]: arxiv-2511-19550 — "It quantifies the reduction in uncertainty about an interpretation that results from"
[^c4]: arxiv-2511-19550 — "We introduce a control parameter λ representing the generative complexity of the source (e.g., LLM"
[^c5]: arxiv-2511-19550 — "We postulate two hypotheses about these functions"
[^c6]: arxiv-2511-19550 — "which is unimodal as a function of the generative complexity"
[^c7]: arxiv-2511-19550 — "rising λ beyond λopt causes decipherability (D) to decrease."
[^c8]: arxiv-2511-19550 — "the maximum decipherability achievable by optimizing λ"
[^c9]: arxiv-2511-19550 — "holds for all values of λ"
[^c10]: arxiv-2511-19550 — "leaves high openness, resulting in high S and"
[^c11]: arxiv-2511-19550 — "narrows the interpretive space, increasing D."
[^c12]: arxiv-2511-19550 — "the effective polysemy of a text for a given audience and context"
[^c13]: arxiv-2511-19550 — "A message can be highly decipherable yet factually incorrect, and vice-versa"
[^c14]: arxiv-2511-19550 — "human interpretation is inherently subjective, context-dependent, and difficult to quantify"
[^c15]: arxiv-2511-19550 — "semiotic breadth necessarily relies on proxies"
[^c16]: arxiv-2511-19550 — "by measuring changes in D and S as a function of prompt specificity, persona cues, or negative"
[^c17]: arxiv-2511-19550 — "this assumption does not hold in domains where ambiguity, multiplicity, or interpretive"
[^c18]: arxiv-2511-19550 — "The present model does not capture this diachronic evolution."
[^c19]: arxiv-2511-19550 — "not as a universal theory of artificial communication"
