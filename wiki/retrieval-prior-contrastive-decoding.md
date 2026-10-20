---
description: "Each document's expert is scored as (1+β) times its logits minus β times a no-context prior, plus γ times the log of its retrieval relevance, so weakly retrieved documents count for less."
aliases: ["retrieval-aware contrastive decoding", "retrieval-gated contrastive decoding", "context-aware decoding with a retrieval prior"]
sources: ["openalex-org-w7124227879"]
---
# Retrieval-prior contrastive decoding

Context-aware decoding (CAD) "improves faithfulness by shifting probability mass" toward tokens the context supports.[^c1] Most CAD formulations "assume a single supportive context that defines the" conditional distribution.[^c10] A multi-document extension, DvD, "extends CAD to multiple documents but collapses" them into one input sequence, which conflicts with a design where each document keeps its own cache.[^c9]

The paper's rule works per document. For each contextual expert k, its logits are calibrated against the logits s0 of an amateur expert, and a retrieval term is added:

ŝk = (1 + β0) sk − β0 s0 + γ log rk

The amateur is "one amateur expert with an empty cache", that is, the model's prior with no document in context.[^c3] The first term is a contrast: the expert's logits are pushed away from what the model would say with no context at all. The last term is a prior on the expert itself, set by its retrieval relevance rk. β0 sets the contrast strength between amateur and expert, and "and γ controls retrieval gating".[^c2] The next token is the highest calibrated candidate across experts.

The relevance score rk is one number per document. The paper obtains it by fusing a first-stage retrieval score and a cross-encoder reranker score, both mapped into [0, 1), and "we fuse them into a single per-document relevance score via the" harmonic mean.[^c4] Because rk lies in [0, 1), log rk is never positive, and it becomes more negative as a document looks less relevant. So the term lowers the influence of weak documents without removing them.

Two settings are fixed by a rule rather than tuned per item. β0 is computed for the first generated token, as in AdaCAD, and then "keep it fixed thereafter".[^c6] The gating weight is a single constant: "We empirically set γ = 2.5 for" all experiments.[^c5]

The paper's ablation removes each term in turn. Dropping the retrieval prior (γ = 0) or the contrast (β = 0) "leads to large accuracy drops" on the reported tasks.[^c7] The paper credits the retrieval term with noise robustness: the rule "downweights irrelevant experts",[^c8] and on NQ under LOFT, the paper says, "this yields strong gains".[^c13]

The amateur here plays the same role as the null pass in [[null-image-logit-subtraction]], where a blank image replaces the empty document cache and the next-token distribution from the blank input is subtracted from the real one. What the text adds is the γ log r term, which has no counterpart in the blank-image method. Whether the subtraction and the retrieval term do different work on the same tasks is not separated in the text beyond the ablation above (my inference).

## Limits

- γ is a constant chosen on the benchmarks. The text gives a sweep in an appendix but no derivation of 2.5 from the mechanism (my inference).
- The size of the retrieval penalty depends on the scale and fusion of rk. The three variants the paper compares "differ only in the relevance signal",[^c11] so the comparison varies the signal's source, not its scale, and only one retriever family is named.
- β0 is fixed after the first token. Whether a contrast strength chosen at the start still fits later tokens is not tested in the text (my inference).
- The retrieval term reweights experts that were retrieved. The paper says the method "cannot recover evidence that is entirely" absent from the candidate set.[^c12]
- The rule needs the logits of every expert and the amateur at each step, so it does not apply to models that expose only sampled tokens (as in the parent method, [[decode-time-expert-aggregation]]).
- The evidence is one paper's benchmarks (LOFT and LongBench, with a fixed top-90 pool). No count of how often the retrieval term changes the chosen token is given here (my inference).

## Related

- [[decode-time-expert-aggregation]] — the expert layout this rule weights; this note is the scoring rule alone
- [[null-image-logit-subtraction]] — the same subtraction against a null-input pass, in vision-language decoding, without a retrieval term
- [[context-fidelity-boosting]] — another decoding-time method that raises tokens the context supports; the mechanism is an additive bias, not a contrast with an empty-context pass

[^c1]: openalex-org-w7124227879 — "improves faithfulness by shifting probability mass"
[^c2]: openalex-org-w7124227879 — "and γ controls retrieval gating"
[^c3]: openalex-org-w7124227879 — "one amateur expert with an empty cache"
[^c4]: openalex-org-w7124227879 — "we fuse them into a single per-document relevance score via the"
[^c5]: openalex-org-w7124227879 — "We empirically set γ = 2.5 for"
[^c6]: openalex-org-w7124227879 — "keep it fixed thereafter"
[^c7]: openalex-org-w7124227879 — "leads to large accuracy drops"
[^c8]: openalex-org-w7124227879 — "which downweights irrelevant experts"
[^c9]: openalex-org-w7124227879 — "extends CAD to multiple documents but collapses"
[^c10]: openalex-org-w7124227879 — "assume a single supportive context that defines the"
[^c11]: openalex-org-w7124227879 — "These variants differ only in the relevance signal"
[^c12]: openalex-org-w7124227879 — "it cannot recover evidence that is entirely"
[^c13]: openalex-org-w7124227879 — "this yields strong gains on NQ under LOFT"
