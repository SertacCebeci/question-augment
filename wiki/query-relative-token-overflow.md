---
description: "A compressed context token can be adequate for one question and overflowed for another; overflow is query-relative, so detecting it needs query-context joint features, not token statistics alone."
aliases: ["token overflow", "compression overflow", "compressed-token overflow detection"]
sources: ["arxiv-2602-12235"]
---
# Query-relative token overflow

In soft context compression (here xRAG, which maps a retrieved passage to a single dense token fed to a frozen LLM), a compressed token can reach a regime where it no longer holds what a given question needs. The source work calls this token overflow and define it as instance-level and behavioural: the uncompressed reference answer is right and the compressed one is wrong.[^c1] The label depends on the pair (context, question), not on the context alone.

## What separates detectors

Four feature families were compared for predicting overflow.

- Token saturation statistics (Hoyer sparsity, spectral entropy, kurtosis of the compressed vector) separate compressed from uncompressed tokens almost perfectly (above 0.95 AUC-ROC with linear classifiers).[^c2] The same statistics are near-random at predicting overflow; even when query-conditioned they reach only 0.55-0.63.[^c3]
- Context complexity (perplexity, length, gzip compressibility) is also near-random, though the authors suggest it may matter for longer contexts or harsher compression.[^c4]
- Attention patterns during generation give moderate signal (0.62 AUC-ROC on average) and need LLM forward passes.[^c5]
- Linear probes on joint query-and-context representations reach 0.70-0.73 and beat context-only models (0.64-0.69).[^c6]

The authors read this as: overflow is not an intrinsic property of the compressed vector but arises from the mismatch between what the token holds and what the query requires.[^c7] A token can look structurally "compressed" and still be fine for the question asked.

## Where the signal appears

The probe works right after the projection step, before the LLM runs, with 0.72 AUC-ROC on average. Middle-layer hidden states after inference give identical performance, so the loss is fixed at compression time and merely propagates.[^c8] This makes a cheap pre-LLM gate possible, for example to resize chunks or fall back to the full passage. Linear probes sufficed; MLPs added little, which the authors take to mean the structure is roughly linearly separable.[^c9]

## For asking and answering

For anyone deciding whether a compressed or summarized context can answer a question, the point is that sufficiency is a property of the pair. A context judged adequate in the abstract (low saturation, simple text) says little about a particular question. My own inference: the same holds for any lossy intermediate, so the question must enter the adequacy check.

## Limits

- One architecture (xRAG), short passages compressed into a single token, and three QA datasets (HotpotQA, SQuADv2, TriviaQA); the authors state generalization to other compressors, longer contexts and other tasks is untested.[^c10] The claim that the method transfers is an expectation, not a result.
- 0.72 AUC-ROC is modest; a gate built on it would still pass many overflowed cases.
- Overflow is defined by task failure against a reference that is itself correct, so cases where both fail, or fail differently, are not counted.
- Whether "behaves like noise" holds mechanistically was not isolated; the saturation hypothesis was disconfirmed for detection.

## Related

- [[sufficient-statistic]] — adequacy of a compressed summary is relative to the question asked of it
- [[rate-distortion-theory]] — the formal frame for how much a fixed-size code can retain; this paper gives no bound, only empirical detection
- [[retrieval-cue-disruption]] — another case where whether information is usable depends on the query-side cue
- [[decoded-answer-rank-compression]] — a different compression of model output with measured costs
- [[nonlinear-hidden-state-probe]] — the contrast on the probe's shape: an MLP beat a linear probe for token-level entity hallucination, while linear sufficed here; different targets, so the two results do not conflict as stated

[^c1]: arxiv-2602-12235 — "Oi = 1 Tiref = 1 ∧ Ti (Ci ) = 0 ."
[^c2]: arxiv-2602-12235 — "Linear classifiers achieve"
[^c3]: arxiv-2602-12235 — "performance remains limited (0.55–0.63 AUCROC)."
[^c4]: arxiv-2602-12235 — "Context-level features (shown in Table 1) also"
[^c5]: arxiv-2602-12235 — "patterns (0.62 AUC-ROC on average) and saturation statistics (even when query-conditioned) provide no meaningful improvement over projectionstage features."
[^c6]: arxiv-2602-12235 — "outperforming context-only models (0.64–0.69"
[^c7]: arxiv-2602-12235 — "This reveals that overflow is not an intrinsic property of compressed representations but emerges"
[^c8]: arxiv-2602-12235 — "Post-inference detection using middle-layer hidden states achieves identical performance"
[^c9]: arxiv-2602-12235 — "Similar to tokentype classification (RQ1), linear classifiers prove"
[^c10]: arxiv-2602-12235 — "This work focuses on the xRAG architecture as"
