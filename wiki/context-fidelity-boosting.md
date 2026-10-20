---
description: "A decoding-time additive logit bias, borrowed from watermarking's green-list trick, raised on tokens the context supports and scaled by the context's effect on the model's next-token guess."
aliases: ["CFB", "watermark-inspired decoding", "context-fidelity boosting"]
sources: ["arxiv-2604-22335"]
---
# Context-Fidelity Boosting

> Watermarking biases logits toward a hidden list so a detector can later prove
> the text was machine-written; point the same additive bias at the tokens the
> *context* already supports, and the bias becomes a faithfulness mechanism
> instead of a provenance one.

## Definition / Mechanism

Zhang, Ye, Gao, Li et al. (2026) give this bias a name,
Context-Fidelity Boosting (CFB). At each decoding step $t$, let $V_S$ be the vocabulary tokens that appear in
the source span extracted from the input context. The logit of every token in
$V_S$ is shifted by an additive term $\Delta_t(w)$ and every other token is
left untouched: "Given a context passage C and a query Q, our goal is to
enhance contextual fidelity by increasing the probability of generating
tokens supported by the source content in C" — the reshaping is
$\tilde l_t(w) = l_t(w) + \Delta_t(w)$ for $w \in V_S$, $l_t(w)$ otherwise.

Three variants set $\Delta_t(w)$ with increasing adaptivity. Static boosting
"assigns a fixed boost $\delta$ to all tokens in the source-supported
vocabulary", independent of the input. Context-aware boosting instead
scales the boost by the Jensen–Shannon divergence $D$ between the model's
next-token distribution with and without the context in the prompt, so
$\Delta_t(w) = \delta_{min} + (\delta_{max} - \delta_{min}) \cdot D$: "larger
divergence indicates that the context substantially changes the model's
next-token preference, and therefore warrants a stronger context-fidelity
bias" Token-aware boosting further redistributes that sample-level
budget across $V_S$ by a per-token relevance score that mixes attention mass
over the token's occurrences in the source with the token's average
embedding-cosine similarity to the rest of the source span (weights
$\lambda_1{=}0.6, \lambda_2{=}0.4$), normalized so the mean relevance is 1
before multiplying the context-aware boost.[^c3]

## Why it matters

On stall 6, this is a third point between the two the wiki already holds.
[[constrained-decoding]] makes membership in an admissible set a hard
guarantee by masking every other token to $-\infty$; [[contradiction-gate]]
lets the answer stand and vetoes it after the fact from a separate verifier
call. CFB does neither: it never forbids a context-contradicting token and
never inspects the finished answer — it continuously tilts the sampling
distribution, every step, toward whatever the source span already supports,
using a signal (JSD between context-conditioned and context-free
next-token distributions) that is read off the same forward pass rather than
computed by a second model call. The result is graded, not binary: a token
the context does not mention is still reachable, just less likely, and the
degree of tilt itself scales with how much the context is actually
disagreeing with the model's own next-token guess.

## Transfer

| | |
|---|---|
| **In its home field** | Text watermarking partitions the vocabulary into a pseudorandomly-seeded "green" list and biases logits toward it at every step, so a detector who knows the seed can later prove statistically that a text is watermarked. |
| **Here** | The list is redefined from a pseudorandom, detection-oriented partition into a content-dependent one — the tokens attested in the input's source span — and the bias is read for faithfulness during generation, not verified afterward. |
| **What survives** | The construction itself: an additive per-step logit bias confined to a chosen token subset, cheap enough to apply at every decoding step. |
| **What does not** | Watermarking's statistical detection guarantee (a false-positive rate over a hypothesis test on the green/red split) has no counterpart here — CFB's split is per-example and is never tested for detectability, only for whether the output stayed faithful. |

## Limits

- Needs model internals. "It requires access to model internals such as
  logits and, for the token-aware variant, signals like attention or token
  embeddings, which makes it difficult to apply in black-box API settings."[^c4]
- Loses to a conflict-specific baseline exactly where stall 6 cares most: on
  inputs with an explicit context/parametric-knowledge conflict, "CFB is
  especially effective when context should be amplified, whereas methods
  explicitly designed to suppress parametric priors remain stronger when
  context and internal knowledge are in direct conflict." The mechanism
  boosts source support; it does not detect or represent a conflict as such,
  so it is not the mechanism to reach for when the task is telling a
  contradiction apart from ordinary underspecification.
- The token-aware variant's gain rides on the quality of its relevance
  estimate: it "depends on the quality of local relevance estimation and is
  not consistently superior in high-conflict settings."[^c6]
- No claim in the source about what the bias does to calibration or to
  answers that should be refused outright — evaluated only on ROUGE/FactKB/
  BERT-P/accuracy against context-supported gold answers, never against an
  abstention target.

## Related

[[constrained-decoding]] · [[contradiction-gate]] · [[abstention]]

[^c3]: arxiv-2604-22335 — "larger divergence indicates that the context substantially changes the model’s next-token preference, and therefore warrants a stronger context-fidelity bias"
[^c4]: arxiv-2604-22335 — "it requires access to model internals such as logits and, for the token-aware variant, signals like attention or token embeddings, which makes it difficult to apply in black-box API settings"
[^c6]: arxiv-2604-22335 — "the token-aware variant depends on the quality of local relevance estimation and is not consistently superior in high-conflict settings"
