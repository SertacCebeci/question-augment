---
description: "In RAG knowledge conflicts, the model's self-answerability score predicts whether it abandons memory for retrieved context: flip rate falls from 41% (low) to under 5% (high)."
aliases: ["self-answerability gating", "memory-vs-context trust threshold", "TCR conflict signals"]
sources: ["arxiv-2601-06842"]
---
# Self-Answerability Flip Threshold

When retrieved context contradicts what a model memorized, whether the model switches to the context depends on how confident it already is in answering without it. Ye et al. (2026) feed three scalars to a generator: semantic similarity of query and context, factual consistency of query and context (kept apart by two contrastive encoders), and a self-answerability estimate of the query alone.[^c1] The third scalar is the one that arbitrates between memory and context.

## Separating "about" from "true"

In an exploratory probe on 5k Wikidata triples (paraphrase, negated contradiction, unrelated), off-the-shelf sentence embeddings (MiniLM, E5-large) did not separate meaning from truth; but one linear projection to a 2D plane did: "off-the-shelf embeddings intertwine meaning and truth, yet a single linear projection cleanly separates them".[^c2] A conflict is then a context that matches the topic but clashes in fact: high semantic similarity, low factual consistency. Successfully corrected cases cluster in that quadrant.[^c3]

## The threshold

The authors bucket self-answerability s and measure the flip rate, the rate at which the model overrides its parametric answer with context. "for s < 0.3 the flip rate is ∼ 42%, whereas for s > 0.7 it drops to 4%", with the same threshold across Llama-3-8B, Llama-3-13B and Qwen3-8B, yielding the rule "if self-answerability > 0.7, trust memory; otherwise examine context."[^c4] Cases where the model fixed a wrong belief or resisted misinformation showed higher answerability than failures.[^c5]

## Signal weighting and ablation

Each signal is weighted in training by its signal-to-noise ratio (variance of the prediction from that signal over variance of the residual), softmax-normalized. Soft-prompt tokens carrying an MLP encoding of the three scalars are prepended to the input.[^c6] Ablation: removing self-answerability lowers the two headline metrics (MCOR/KGRR) by about 18/26 pp; fixed instead of SNR weights costs 17/20 pp; removing signal integration costs 55/53 pp.[^c7] During decoding, "factual > self-ans before step 10 predicts success in 70% of cases", suggested as a trigger for early stop or re-prompt.[^c8]

## Limits

- The 0.3/0.7 bins are descriptive, reported by the authors on their own conflict benchmark and three backbones; the "rule" is not shown to be optimal or to transfer to other answerability estimators. My inference: the estimator (following Slobodkin et al. 2023) shapes any such threshold.
- Flip rate is correlational; low answerability may co-occur with weak memory rather than cause trust in context.
- The conflict dataset is synthetic (Wikidata triples expanded with GPT-4o), so detection results may overstate real retrieval noise.
- Backbones differ: Llama distributions were tighter than Qwen.[^c9]
- Ablation numbers were read from prose only, not tables.

## Related

- [[parametric-suppression]] — a layer-level account of the same failure, where memory overwrites evidence
- [[context-fidelity-boosting]] — output-level bias toward context over memory
- [[dual-path-knowledge-boundary-probing]] — probing what the model internally knows
- [[gated-answerability-rule]] — answerability used as a gate on behavior

[^c1]: arxiv-2601-06842 — "model-inferred answerability (σans )"
[^c2]: arxiv-2601-06842 — "off-the-shelf embeddings intertwine meaning and truth, yet a single linear projection cleanly separates them"
[^c3]: arxiv-2601-06842 — "indicating ‘topic match but fact clash” is where reevaluation is triggered"
[^c4]: arxiv-2601-06842 — "for s < 0.3 the flip rate is ∼ 42%, whereas for s > 0.7 it drops to 4%"
[^c5]: arxiv-2601-06842 — "SC/SD exhibit higher answerability than still-wrong (SW) or misled"
[^c6]: arxiv-2601-06842 — "we dynamically weight their training contributions according to"
[^c7]: arxiv-2601-06842 — "removing signal integration(SI) collapses 55/53 pp"
[^c8]: arxiv-2601-06842 — "factual > self-ans before step 10 predicts success in 70% of"
[^c9]: arxiv-2601-06842 — "Llama shows"
