---
description: "A dual-branch LoRA probe that reads an LLM's hidden states, with and without retrieved context, to predict whether retrieval will help before any answer is generated."
aliases: ["Internal Prober", "RAG gain prediction", "selective RAG"]
sources: ["arxiv-2604-07985"]
---
# Internal probing for RAG gain

> "By estimating the expected gain in advance, a system can adopt a
> selective RAG strategy, invoking retrieval only when it is likely to be
> beneficial." Amiraz et al. (2026)[^c1]

## Definition / Mechanism

Retrieval-augmented generation does not help every question: on the
paper's test sets over 30% of questions get zero or negative gain from
retrieval, defined as the log-ratio of answer quality with and without
the retrieved context. Deciding whether to retrieve at all is therefore a
source-routing decision, made per question, before any passage is used.

Internal Prober answers it without generating an answer with either
branch. "We introduce Internal Prober, a novel gain predictor that
directly estimates RAG gain from the internal representations of the
LLM, without requiring full auto-regressive generation." A single
frozen LLM backbone is run as two parallel streams — the question alone,
and the question concatenated with the top retrieved passages — each
adapted by its own LoRA module: "It operates over a single frozen LLM
with two parallel input streams: the question augmented with retrieved
passages (q; p1 . . . p5), and the question alone (q). To avoid
duplicating the full model, we train two independent Low-Rank Adaptation
(LoRA) modules, one per branch."[^c3]

Unlike a probe trained on a fixed representation, the LoRA adapters are
free to move the representation itself toward the task: "Internal Prober
actively adapts the LLM by training LoRA adapters, allowing the model's
internal hidden states to be reshaped in accordance with the target
task." Each branch's final hidden state feeds a linear regression
head predicting an answer-quality score; the two branches' scores are
combined into a log-ratio gain estimate Ĝ, trained end to end against
the true gain with MSE loss.

Routing is a threshold on the sign of Ĝ: "Accordingly, when Ĝ > 0, we
generate the answer using RAG; otherwise, we invoke the LLM without
retrieval to produce a no-RAG response." Because each branch needs
only one forward pass, the source-routing decision costs two parallel
passes instead of the two full generations a generation-based gain
predictor needs: "At inference time, Internal Prober replaces the
standard auto-regressive generation process ... with only two parallel
forward passes."[^c6]

## Why it matters

A practitioner deciding when to route a question to retrieval, rather
than answering closed-book, would use hidden-state probing instead of
either a cheap pre-retrieval query statistic (shown ineffective for this
task) or a full second generation: "Internal Prober helps to ameliorate
the huge performance gap between post-retrieval and post-generation
predictors" — most of the accuracy of comparing two full generations, at
the latency of one. In a selective-RAG evaluation, thresholding its
score consistently beat always retrieving, on both answer quality and
routing accuracy.

## Limits

- White-box access to hidden states is required: "Internal Prober
  requires white-box access to the LLM's internal representations and
  therefore cannot be applied to proprietary black-box models;
  post-retrieval and generation-based predictors remain applicable in
  such settings."[^c8]
- Evaluated only on mid-sized (8–10B parameter) instruction-tuned LLMs;
  whether the reshaped hidden states still carry a usable gain signal at
  much larger or much smaller scale is unverified.
- The gain target itself is a single scalar quality metric trained
  against one retriever and one backbone at a time — the routing
  decision is not shown to transfer across retrievers or LLMs without
  retraining the adapters.

## Related

[[calibrated-retrieval-budget-allocation]] · [[groundedness-gated-tool-routing]] · [[value-of-information]] · [[abstention]]

[^c1]: arxiv-2604-07985 — "By estimating the expected gain in advance, a system can adopt a selective RAG strategy, invoking retrieval only when it is likely to be beneficial."
[^c3]: arxiv-2604-07985 — "It operates over a single frozen LLM with two parallel input streams: the question augmented with retrieved passages (q; p1 . . . p5 ), and the question alone (q). To avoid duplicating the full model, we train two independent Low-Rank Adaptation (LoRA) modules [45], one per branch."
[^c6]: arxiv-2604-07985 — "At inference time, Internal Prober replaces the standard auto-regressive generation process which require |Ano-rag | + |Arag | sequential forward passes by Bert-Gen-2A, with only two parallel forward passes."
[^c8]: arxiv-2604-07985
