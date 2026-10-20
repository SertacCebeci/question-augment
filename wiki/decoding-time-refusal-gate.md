---
description: "A refusal score is computed before generation and rechecked at every decoding step, with a learned logit mask applied when a token-level score crosses a threshold."
aliases: ["safety-aware controllable decoding", "two-stage safety gate", "controllable safety decoder", "SCD", "rejection-rate decoder"]
sources: ["arxiv-2512-02363"]
---
# Decoding-time refusal gate

A refusal gate is a safety check built into the decoder rather than placed before it. The paper describes its safety signal as having two parts: "We adopt a two-stage safety signal: (i) an utterance-level" check and "pre-decoding check and (ii) a token-level dynamic signal" during generation.[^c1][^c2]

The first stage is a binary head on a pooled representation of the context, P_reject = σ(W_cls · h_pool). It is evaluated before any token is produced: "Rejection is therefore evaluated prior to generation and rechecked" at each step.[^c3] The second stage scores every generated position, p_{j,t} = σ(w_tok · h_t), and applies a logit change when that score exceeds a threshold. The paper writes the adjusted logits as õ_t = o_t − λ_safe·I[P_reject > τ_pre] + I[p_{j,t} > τ_tok]·m. The text says "Decoding logits are dynamically modulated at each generation" step, and that "where m is a learned mask biasing unsafe continuations".[^c4][^c5] The head itself is trained as a binary classifier, "A binary head predicts refusal to suppress unsafe outputs,"[^c6] and the decoder is also trained to emit an explicit token: "Train the decoder to emit" the refusal marker when the score is above threshold.[^c7]

What is measured is a rejection rate. The paper defines it as the fraction of unsafe queries the model refuses, to "recognize and refuse unsafe or out-of-scope queries".[^c8] On the paper's own dataset, the full model's rejection rate is 12.4%, against 6.0% for the variant with fusion and the gate but without the safety decoder, and 2.1% for the baseline LLaMA (Table I).[^c9]

## Limits

- As printed, the pre-check term subtracts the same constant λ_safe from every vocabulary logit. A constant shift across all tokens leaves a softmax unchanged, so the pre-check cannot alter the next-token distribution by itself (my reading of equation 12). Any refusal it causes must come from the trained refusal token or from the learned mask. This may be a typesetting error in the paper, and the text does not resolve it.
- "Unsafe" is not defined in the text. The denominator is given only as "Total Unsafe Queries",[^c10] with no size, labelling procedure or source. The rate cannot be checked.
- The rejection rate counts refusals on unsafe items only. No false-refusal rate on answerable queries is reported. A higher rejection rate therefore cannot tell a safe refusal from over-refusal, which is the failure a service for elderly users would most need to see.
- One proprietary dataset, 3 seeds, and no comparison with other safety decoders. The related-work section mentions controlled decoding with auxiliary constraints, but the experiments do not compare against it.
- The thresholds τ_pre and τ_tok and the weight λ_safe are tuned by grid search on validation data. The text gives no sensitivity analysis, so how far the 12.4% figure depends on those choices is unknown.
- The mechanism needs a trained head, a trained mask and a fine-tuned decoder. What survives the transfer to a prompt-only answerer is the separation of a refusal decision made before an answer from a check during it. The trained logit mask does not transfer to a frozen model.

## Related

- [[abstention]] — "I don't know" as a third output; this note is one way to produce that output from inside the decoder, and the rejection rate here is an abstention rate on a chosen set.
- [[constrained-decoding]] — also changes the next-token choice at each step, but by a grammar that keeps output admissible; here the change is a learned mask triggered by a safety score.
- [[context-fidelity-boosting]] — the same additive logit-bias form, raised on tokens the context supports rather than on refusal.
- [[gated-memory-integration]] — the knowledge-side gate in the same architecture, which decides how much retrieved material enters the hidden state.

[^c1]: arxiv-2512-02363 — "We adopt a two-stage safety signal: (i) an utterance-level"
[^c2]: arxiv-2512-02363 — "pre-decoding check and (ii) a token-level dynamic signal"
[^c3]: arxiv-2512-02363 — "Rejection is therefore evaluated prior to generation and rechecked"
[^c4]: arxiv-2512-02363 — "Decoding logits are dynamically modulated at each generation"
[^c5]: arxiv-2512-02363 — "where m is a learned mask biasing unsafe continuations"
[^c6]: arxiv-2512-02363 — "A binary head predicts refusal to suppress unsafe outputs"
[^c7]: arxiv-2512-02363 — "Train the decoder to emit"
[^c8]: arxiv-2512-02363 — "recognize and refuse unsafe or out-of-scope queries"
[^c9]: arxiv-2512-02363
[^c10]: arxiv-2512-02363 — "Total Unsafe Queries"
