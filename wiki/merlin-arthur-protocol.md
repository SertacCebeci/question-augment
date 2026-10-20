---
description: "A helpful and an adversarial prover each pick features for a verifier; the verifier's completeness and soundness errors lower-bound the mutual information those features carry about the label."
aliases: ["M/A classifier", "Merlin-Arthur classifier", "Merlin-Arthur interactive proof", "M/A protocol"]
sources: ["arxiv-2512-11614"]
---
# Merlin-Arthur protocol

A Merlin-Arthur protocol is a three-agent game. A helpful prover and an adversarial prover each choose which part of an input the verifier sees. The verifier's two measured error rates then bound how much the chosen part tells about the label. The mechanism, concretely:

Merlin "selects a feature subset" to convince the verifier of the correct class. Morgana "attempts feature selection" that makes the verifier miss the class. Arthur, the verifier, outputs a class or abstains.[^c1] Two errors are measured on a test set. The completeness error ε_c is "The probability that Arthur fails to classify correctly given" Merlin's features. The strict soundness error ε_s is "The probability that Arthur fails to defend against Morgana", which means Arthur does not abstain on Morgana's features.[^c2]

These two errors bound the precision of the selected features. The bound is approximately 1 − ε_c − ε_s/(1 − ε_c + ε_s). The mutual information between the features and the label is then at least the label's entropy minus the binary entropy of that precision. Low errors on both sides mean the exchanged features "possess high mutual information with the ground truth class."[^c3]

The numbers are small enough to check by hand. For a balanced binary label, the entropy is about 1 bit. If completeness and soundness are each 90 percent, the bound is 0.28 bits, and the paper reports it as "0.28 bits of mutual-information lower bound of information about the class."[^c4] My arithmetic reproduces this: the precision bound is 0.8, whose binary entropy is about 0.72 bits, leaving about 0.28 bits of the one bit.

To use the protocol on generated text, the paper turns the multi-class answer into a binary test: "we frame the multi-class prediction task as a binary verification problem." The positive class is the ground-truth answer and every other output counts as incorrect.[^c5] In RAG the exchanged features are the retrieved context. Merlin masks the context to support the answer, and Morgana masks it to disrupt the answer.[^c6]

Why a verifier that can abstain matters. Soundness is measured by whether the verifier refrains from the correct class under misleading features, so the abstain output is part of what the protocol tests. The original framework bounds mutual information "via measurable test-set quantities" and does so "without requiring explicit modeling of the data distribution."[^c7] That is the feature of the construction that distinguishes it from a heuristic attribution: the bound is read off error rates, not off a fitted saliency map.

Direct computation is intractable. "Applying the M/A protocol directly is computationally hard," because the optimal masks need Arthur evaluated over exponentially many context subsets.[^c8] The paper replaces the search with a single perturbation probe, ATMAN, which "requires a single isolated probe (linear complexity)." Merlin and Morgana then choose the top-k units by that probe's scores.[^c9]

## Limits

- The bound is on information the chosen features carry about the label. It is not a claim that the answer was reasoned from them. The authors say that "high accuracy does not guarantee entropy flow from context to answer."[^c10]
- The precision bound is an approximation. It is stated with a "≳" and rests on a cited theorem and "common discussion of system parameters as in App. B."[^c11]
- Soundness here is deliberately stricter than in the older literature: the paper proposes "a definition of soundness that is explicitly stricter than those established in literature." Its numbers are not directly comparable to earlier M/A results without that adjustment.[^c12]
- The masks come from an explainer, not an exact search. The paper says that using XAI "introduces an inherent tradeoff between explanation fidelity" and verifier robustness, so a reported bound mixes explainer quality with verifier quality.[^c13]
- The original work is on image classification. The language version adds a binary framing that collapses all wrong answers into one class. Whether that collapse hides useful distinctions among wrong answers is not tested in the text read (my inference).

## Related

- [[mutual-information]] — the quantity the protocol bounds from below
- [[abstention]] — the verifier's abstain output is what the soundness error counts
- [[explained-information-fraction]] — the same bound divided by the model's own predictive information
- [[information-estimation-bias]] — mutual information estimated from counts is biased; this bound avoids counting by using test-set error rates (my reading)

[^c1]: arxiv-2512-11614 — "Merlin (Prover, Me) selects a feature subset"
[^c2]: arxiv-2512-11614 — "The probability that Arthur fails to defend against Morgana"
[^c3]: arxiv-2512-11614 — "possess high mutual information with the ground truth class"
[^c4]: arxiv-2512-11614 — "0.28 bits of mutual-information lower bound of information about the class"
[^c5]: arxiv-2512-11614 — "we frame the multi-class prediction task as a binary verification problem"
[^c6]: arxiv-2512-11614 — "Merlin (Me), the helpful prover, masks the retrieved context c"
[^c7]: arxiv-2512-11614 — "via measurable test-set quantities"
[^c8]: arxiv-2512-11614 — "Applying the M/A protocol directly is computationally hard"
[^c9]: arxiv-2512-11614 — "It requires a single isolated probe (linear complexity)"
[^c10]: arxiv-2512-11614 — "While high accuracy does not guarantee entropy flow from context to answer"
[^c11]: arxiv-2512-11614 — "and common discussion of system parameters as in App. B"
[^c12]: arxiv-2512-11614 — "a definition of soundness that is explicitly stricter than those established in literature"
[^c13]: arxiv-2512-11614 — "introduces an inherent tradeoff between explanation fidelity"
