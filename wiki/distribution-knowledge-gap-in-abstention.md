---
description: "With hidden adversarial injections, a learner that may abstain pays polylog error if it knows the data distribution but provably sqrt(T) if it must infer it from the stream."
aliases: ["adversarial injection model", "reliable abstention under injections", "distribution-agnostic abstention"]
sources: ["arxiv-2602-20111", "arxiv-2602-17918"]
---
# Distribution knowledge gap in abstention

A learner sees a stream where most items come from an unknown distribution D but some are injected by an adversary, with no flag telling which. It may answer or abstain. Error counts every wrong answer, but counts an abstention only when the item was a genuine i.i.d. one.[^c1] Abstaining is therefore safe against injected items and costly on ordinary ones; answering is the reverse. The learner cannot tell which case it is in.

## What is established

- With oracle access to D, prior work gives combined error O(d^2 log T) for VC dimension d. Without it, only roughly sqrt(T) was known for restricted classes.[^c2]
- The gap is real: even for VC dimension 1 every distribution-agnostic learner suffers expected combined error of order sqrt(T) against some oblivious adversary.[^c3] Knowing D is a genuine advantage, not an artefact of weak algorithms.
- Upper bounds come from "robust witnesses": small subsets of earlier labeled examples whose presence makes the wrong label for a new point cost a guaranteed drop in a score. The learner answers only when both labels would cause a large drop, else abstains.[^c4] Each mistake then triggers a guaranteed potential drop, bounding mistakes in the worst case.
- Abstentions on i.i.d. items are bounded by exchangeability: only a few items in any set can be "attackable" (made to trigger abstention by some adversarial extension), so a given i.i.d. item is rarely among them.[^c5]
- Classes of inference dimension k get combined error of order T^(1-1/k); halfspaces in the plane have certificate dimension 3 and get T^(2/3).[^c6] This is notable because such halfspaces are not robustly learnable under clean-label attacks without abstention; abstention changes the picture because many injected points aimed at one sample cost little if the learner abstains or answers the injected points correctly.[^c7]

- Without the distribution the two errors trade off polynomially rather than both being small. For a VC-1 class, any learner faces either expected misclassification of order T^a or abstention error of order T^(1-a) against some oblivious adversary, for every a in [0,1].[^c9] This extends the sqrt(T)-or-sqrt(T) bound to the whole range.[^c10]
- An upper bound matches in shape: boosting weak learners, each estimating shattering probabilities from a subset of the stream, gives misclassification O(T^(3a)) and abstention of order d^2 T^(1-a) (up to logs) for any VC class against oblivious adversaries.[^c11] The same holds against adaptive adversaries only for classes of finite reduction dimension, such as linear classifiers; for all VC classes it is an open question.[^c12] The exponents leave a polynomial gap between the bounds except for VC-1 classes.[^c13]

Reading for questions and answers (my inference, not the paper's): the value of declining to answer depends on what the answerer knows about the distribution of questions it will face. Calibrated "I don't know" can be cheap when that distribution is known and unavoidably expensive when it must be learned from a stream that may be contaminated.

## Limits

- The lower bound uses an oblivious adversary; whether adaptive injection forces more on other classes is open.[^c8]
- Upper bounds all rest on exchangeability of the i.i.d. rounds; faster rates would need new techniques.
- Halfspaces in dimension 3 or more are unresolved (inference dimension is infinite there).
- The setting is realizable, clean-label, binary classification; no claim is made about open-ended language answering. The transfer in the paragraph above is my own reading.
- The oracle in the known-D regime is very strong (any function of D queryable exactly).

## Related

No existing wiki note covers this concept; nearest in subject are the abstention-oriented notes such as [[temperature-scaled-deferral-gate]] and [[loss-aligned-uncertainty-level]].

[^c1]: arxiv-2602-20111 — "Mistakes are always counted, while abstentions are counted only on i.i.d. rounds"
[^c2]: arxiv-2602-20111 — "In the known-D regime,"
[^c3]: arxiv-2602-20111 — "We prove that even for VC dimension 1, every"
[^c4]: arxiv-2602-20111 — "The learner predicts only when one of the two"
[^c5]: arxiv-2602-20111 — "ensures that only a small number of samples in any set can be attackable"
[^c6]: arxiv-2602-20111 — "Halfspaces in R2 have certificate dimension 3"
[^c7]: arxiv-2602-20111 — "Our result demonstrates that abstention fundamentally changes the"
[^c8]: arxiv-2602-20111 — "Our separation lower bound uses an oblivious adversary."
[^c9]: arxiv-2602-17918 — "which shows that polynomial tradeoffs are necessary even for learning function"
[^c10]: arxiv-2602-17918 — "We complete this result with the following lower bound tradeoff between abstention and misclassification errors, which shows that polynomial tradeoffs are necessary even for learning function"
[^c11]: arxiv-2602-17918 — "We propose a family of algorithms AbstainBoost for α ∈ [0, 1] which guarantee O(T 3α )"
[^c12]: arxiv-2602-17918 — "Open question. Can we achieve poly(d)T 1−Ω(1) misclassification and abstention error for any"
[^c13]: arxiv-2602-17918 — "polynomial gap between the guarantees of AbstainBoost from Theorem 2, for VC-1 classes, this"
