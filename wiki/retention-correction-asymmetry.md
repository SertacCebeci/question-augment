---
description: "Relevant retrieved evidence keeps initially correct answers far more reliably than it turns wrong ones right, and larger VLMs correct less, so retrieval gains do not grow with model scale."
aliases: ["correctness retention versus correction rate", "retention-correction split", "inertial priors in RAG", "scale-dependent context integration", "retrieval correction asymmetry"]
sources: ["arxiv-2512-05959", "arxiv-2511-22854"]
---
# Retention–correction asymmetry

Retrieved context acts on a supplied answer in two directions, and a benchmark can measure them separately. Correctness retention is "the percentage of initially correct answers that remain correct after RAG context is provided". Correction rate is "the percentage of initially incorrect answers successfully remediated by RAG context".[^c1] The two counts condition on the baseline answer: retention is taken over the cases the model already gets right, correction over the cases it gets wrong. A retrieval setting can therefore look sound on one count and weak on the other, and a single accuracy number hides which.

The M4-RAG paper measures both on culturally grounded visual question answering, with text and multimodal retrieval over several VLM families. Both rise with retrieval quality: "Both metrics show a positive correlation between the average retrieval relevance score with the performance of all tested models."[^c2] The paper's introduction states the limit of that correlation: "retrieval relevance correlates with performance but does not guarantee successful evidence integration".[^c3]

The two counts are not symmetric. Under poor retrieval, retention falls to 40–60% at relevance scores below 2.0, and the authors read this as "irrelevant context actively misleads models into abandoning correct answers."[^c4] As relevance rises, retention converges toward "near-perfect rates (95–100%)" for all models.[^c5] The correction rate does not follow: "the correction rate never saturates to the same degree as retention, and model spread remains wide even at the highest relevance scores."[^c6] The authors' reading is that "leveraging retrieved evidence to overturn a wrong answer is fundamentally harder than preserving a correct one."[^c7]

The same two-sided reading can be applied to a debate, where a peer's argument stands in for retrieved context. In a dual-agent debate between two reasoning models on CLadder, the authors report that, among questions where the models first disagreed, "far more likely for the debate to change an incorrect answer to a correct one" than the reverse.[^c17] This is a net count of flips, not the two retention rates defined above, so the paper does not show the asymmetry in this note's form. It does show the same direction: a change that repairs a wrong baseline outnumbers a change that breaks a right one. My inference: the two-count reading would separate a debate that keeps correct answers from one that fixes wrong ones, and the debate paper does not report both counts.

## Scale

The asymmetry is sharper for larger models. The paper says large models "form the upper boundary of correctness retention" and, on the correction side, "they are less likely to change an incorrect baseline when given high-quality retrieved evidence."[^c8] Their summary of the two sides: larger models are "less prone to be misled by poor retrieval, but at the same time, also less likely to adopt corrective information supplied by good retrieval."[^c9]

The same pattern shows in the accuracy curves. Text-based retrieval "scales poorly with model size", multimodal gains "do not scale consistently", and "For larger models, the baseline eventually matches or surpasses multimodal RAG performance."[^c10] Reasoning models are "more robust to this effect", keeping retrieval gains longer as scale grows.[^c11]

The paper names the mechanism "inertial priors": "model scale increases inertial priors, that is stronger internal beliefs that are less readily updated by external context."[^c12] This is an interpretation offered by the authors, not a variable they manipulate. What it predicts, and what the data show, is that a larger model's gain from retrieval shrinks with size even when its retrieval is good.

For the wiki, the point is about how to read a RAG result. Relevance alone predicts the retained cases and under-predicts the corrected ones. An evaluation that reports only overall accuracy, or only retrieval relevance, will credit a retriever for keeping correct answers that the answerer would have kept anyway. My inference, not the paper's: the question that separates a useful retriever from a harmless one is how many wrong answers it fixes, not how many right ones it keeps.

## Limits

- Relevance is scored by a judge model, not by people: the text was embedded "using VLM-as-a-judge, to see how relevant the retrieved context is".[^c13] The judge's own error is not measured in the main text.
- The main-text plots show only CVQA. The oracle context on CVQA is a caption generated "conditioned on the image, question, and human-annotated ground-truth answer", so the top of the relevance range carries the answer itself.[^c14] High-relevance retention and correction there partly reflect that leak.
- The correction rate is computed over the baseline-wrong set, and larger models tend to have fewer baseline errors. The text does not show whether the lower correction rate survives when the denominator is held fixed (my inference, not tested).
- The scale claim rests on a few sizes per family: "Gemma3 [53] at 4B, 12B," and 27B, Qwen2.5-VL from 3B to 72B, and a single 7B Pangea model.[^c15] Family and size are confounded with training.
- The authors hedge their own cause: the lower correction "may indicate misalignment between retrievers and foundation models."[^c16] Whether the fix is in the retriever or in the answerer is not decided here.
- The paper does not test the mechanistic account in [[parametric-suppression]]; that link is a candidate, not a finding.

## Related

- [[parametric-knowledge-gates-retrieval-noise-damage]] — the same gate seen from the noise side: damage from irrelevant context depends on the model's own knowledge
- [[parametric-suppression]] — a layer-level account of knowledge conflicts where a correct context-supported answer is overwritten late in the network; a candidate mechanism for the low correction rate, untested here
- [[contextual-inertia]] — persistence of earlier answers across turns, another way a model keeps what it already said
- [[retrieval-state-lock-in]] — retrieval that fixes the answer state can also lock in a wrong one
- [[evidence-language-integration-gap]] — the same integration failure, with the evidence's language as the variable

[^c1]: arxiv-2512-05959 — "the percentage of initially correct answers that remain correct after RAG context is provided"
[^c2]: arxiv-2512-05959 — "Both metrics show a positive correlation between the average retrieval relevance score with the performance of all tested models"
[^c3]: arxiv-2512-05959 — "retrieval relevance correlates with performance but does not guarantee successful evidence integration"
[^c4]: arxiv-2512-05959 — "irrelevant context actively misleads models into abandoning correct answers"
[^c5]: arxiv-2512-05959 — "toward near-perfect rates (95–100%)"
[^c6]: arxiv-2512-05959 — "the correction rate never saturates to the same degree as retention, and model spread remains wide even at"
[^c7]: arxiv-2512-05959 — "leveraging retrieved evidence to overturn a wrong answer is fundamentally harder than preserving a correct one"
[^c8]: arxiv-2512-05959 — "they are less likely to change an incorrect baseline when given high-quality retrieved evidence"
[^c9]: arxiv-2512-05959 — "less likely to adopt corrective information supplied by good retrieval"
[^c10]: arxiv-2512-05959 — "For larger models, the baseline eventually matches or surpasses multimodal RAG performance"
[^c11]: arxiv-2512-05959 — "Reasoning models are more robust to this effect"
[^c12]: arxiv-2512-05959 — "model scale increases inertial priors, that is stronger internal beliefs that are less readily updated by external context"
[^c13]: arxiv-2512-05959 — "using VLM-as-a-judge, to see how relevant the retrieved context is"
[^c14]: arxiv-2512-05959 — "conditioned on the image, question, and human-annotated ground-truth answer"
[^c15]: arxiv-2512-05959 — "Gemma3 [53] at 4B, 12B,"
[^c16]: arxiv-2512-05959 — "this may indicate misalignment between retrievers and foundation models"
[^c17]: arxiv-2511-22854 — "far more likely for the debate to change an incorrect answer to a correct one"
