---
description: "A fixed trust policy toward retrieved context fails one of two user intents: which source should win between context and memory depends on whether the user wants strict grounding or truth."
aliases: ["intent-guided decoding", "context-memory arbitration", "source arbitration in RAG", "intent-aware trust calibration"]
sources: ["doi-10-48550-arxiv-2608-16515"]
---
# Intent-conditioned source arbitration

A retrieval-augmented model can answer from two sources at once: the passage it was handed, and what its weights already hold. The work's claim is that which source should win is not fixed by the retriever or by the model, but by what the user asked for. Its two prompt modes make the point. In strict mode the model is instructed to answer strictly according to the supplied context;[^c1] in truth mode it is told to treat the context as potentially noisy or misleading and to prioritise the correct answer.[^c2]

The argument is that one fixed trust policy cannot serve both intents. Existing RAG systems often apply a fixed trust policy toward retrieved evidence,[^c3] and the cost shows in a measured gap. For Qwen2.5-14B on NQ-Swap, the model answers correctly 91.5% of the time closed-book, but with the misleading context the accuracy falls to 42.0%.[^c4][^c5] A model that always trusts the context is right when the user wants grounding and wrong when the context is corrupted. A model that always discounts the context does the reverse. The paper's framing is that the trust direction has to be a function of the instruction.

## The mechanism

The method, Intent-Guided Decoding, decomposes generation into three conditional branches: the unmodified user branch, a context branch that explicitly follows the retrieved context,[^c6][^c7] and a memory branch that answers closed-book. The user branch is the reference distribution; the other two are the sources it may be pulled toward. Nothing is retrained.

Arbitration runs at two granularities. The coarse stage is an answer-level filter that performs hard replacement only in high-confidence cases: it routes to the memory answer when the memory branch strongly prefers that answer and the user branch does not prefer the context answer. The threshold is a likelihood ratio of three by default, "requiring the memory branch to prefer" the memory candidate.[^c8] The fine stage is token-level correction, applied when the filter does not fire. There the intent sets the direction of the push and branch confidence and source reliability set its size. [[conflict-gated-logit-correction]] describes that stage.

The coarse stage has a measurable role. Removing it, on Qwen2.5-14B, "drops factual world accuracy to 63.0 while leaving faithful accuracy nearly unchanged, suggesting that the filter is conservative".[^c9] The filter is a precision route: it touches stable factual-conflict cases and leaves ordinary context-grounded QA alone.

Intent enters the fine stage as a prior. In the paper's words, "under truth-seeking prompts it can pull decoding toward memory," while under strict prompts it preserves or strengthens context-guided decoding.[^c10]

## What the result says about the concept

The paper's own reading of its results is the part worth keeping. It states that "the key difficulty is not only detecting whether" context or memory is correct, "but also controlling how strongly each source should influence decoding."[^c11] Direction and degree are separate questions. A detector that says which source is right at the answer level does not, by itself, say how far to move the distribution. The reported gain over Direct RAG is large: "score for every model, with gains of 23.0 points for Qwen3-32B," on the intent-aligned average that combines faithful and factual-conflict columns.[^c12]

## Limits

- The evaluation is short-form question answering scored by alias matching. Whether intent-conditioned arbitration holds for long-form generation, where "the answer" is not a short span, is not tested. (My inference from the evaluation design.)
- There are two intent modes, strict and truth, each with a scalar prior. A user who wants partial trust, or a system that must infer intent from the query, is not represented. (My inference.)
- The method shifts probability mass; it does not resolve every conflict. "IGD does not convert all misleading context answers" into correct ones, and some mass moves into an other-answer category.[^c13]
- The factual side is capped by what the closed-book model knows: "correction is naturally limited [39], [40]."[^c14] A model that cannot recover the answer from memory gains nothing from memory-side arbitration.
- The paper names the factual-versus-faithful tension as a limitation of its own framework: "this is a core limitation of the" current setup, since a single aggressive or conservative setting trades one against the other.[^c15]

## Related

- [[conflict-gated-logit-correction]] — the token-level stage that does most of the work in the ablations
- [[context-fidelity-boosting]] — an always-on context-support bias with no memory branch and no intent signal
- [[parametric-suppression]] — why a model can hold the right answer in its layers and lose it at the output, which bears on whether the memory branch is worth trusting (my inference)
- [[evidentiary-basis-of-hallucination]] — the same faithfulness-versus-factuality split, named from the hallucination side
- [[parametric-knowledge-gates-retrieval-noise-damage]] — noise damage gated on the model's own knowledge, measured in another setting

[^c1]: doi-10-48550-arxiv-2608-16515 — "the model is instructed to answer strictly according to the"
[^c2]: doi-10-48550-arxiv-2608-16515 — "to treat the context as potentially noisy or misleading and"
[^c3]: doi-10-48550-arxiv-2608-16515 — "RAG systems often apply a fixed trust policy toward retrieved"
[^c4]: doi-10-48550-arxiv-2608-16515 — "correctly 91.5% of the time in the closed-book setting, but drops"
[^c5]: doi-10-48550-arxiv-2608-16515 — "to 42.0% once the misleading context is provided."
[^c6]: doi-10-48550-arxiv-2608-16515 — "IGD decomposes generation into three conditional"
[^c7]: doi-10-48550-arxiv-2608-16515 — "a context branch that explicitly follows the retrieved context,"
[^c8]: doi-10-48550-arxiv-2608-16515 — "requiring the memory branch to prefer"
[^c9]: doi-10-48550-arxiv-2608-16515 — "drops factual world accuracy to 63.0 while leaving faithful accuracy nearly unchanged, suggesting that the filter is conservative"
[^c10]: doi-10-48550-arxiv-2608-16515 — "under truth-seeking prompts it can pull decoding toward memory,"
[^c11]: doi-10-48550-arxiv-2608-16515 — "suggests that the key difficulty is not only detecting whether"
[^c12]: doi-10-48550-arxiv-2608-16515 — "score for every model, with gains of 23.0 points for Qwen3-32B,"
[^c13]: doi-10-48550-arxiv-2608-16515 — "IGD does not convert all misleading context answers"
[^c14]: doi-10-48550-arxiv-2608-16515 — "correction is naturally limited [39], [40]."
[^c15]: doi-10-48550-arxiv-2608-16515 — "this is a core limitation of the"
