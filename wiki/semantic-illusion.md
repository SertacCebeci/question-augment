---
description: "Plausible hallucinations keep the meaning of their evidence, so embedding and NLI scores place them with faithful text; detectors built on those scores fail where a reasoning judge succeeds."
aliases: ["semantic illusion", "entailment-preserving hallucination", "plausible hallucination invisible to similarity"]
sources: ["arxiv-2512-15068"]
---
# Semantic illusion

A fabricated answer can keep the meaning of the evidence it was written from and still get one fact wrong. A detector that scores a response by how close its meaning sits to the context then finds the fabrication about as close as a faithful answer. The paper calls this the "Semantic Illusion", and it measures the gap on one detector family: a RAG response is scored by the cosine distance between its embedding and the closest context sentence (BGE-base-en-v1.5), by the entailment probability of a DeBERTa-v3-large NLI model, and by the share of content tokens with low lexical overlap with the context. The three scores are averaged, or combined by a learned logistic regression.[^s1]

The gap depends on which hallucinations are in the set. On synthetic answer swapping, where a wrong answer is taken from another document, the ensemble separates the classes: "On NQ, we achieve 95.8% coverage with 0% FPR".[^s2] The construction is chosen for this, since answer swapping "guarantees semantic distance".[^s13] On responses that ChatGPT actually generated for HaluEval, "On real data (HaluEval), the FPR degrades to 100%" at the same target.[^s3] The paper reports the same overlap on RAGTruth outputs of Llama-2, Mistral and GPT-4, and reads it as a property of embedding-based detection, not of one model's output: "overlapping distributions persist across all models".[^s5]

The part that matters for the mechanism is the tail. Most hallucinations on HaluEval score low on entailment, but a tail "achieves near-perfect entailment scores",[^s8] and that tail is what sets the conformal threshold; see [[hard-tail-recall-threshold]]. The paper's phrase for these errors is that they are "semantically indistinguishable from faithful responses".[^s4]

The reasoning-based judge is the contrast. GPT-4o-mini, asked to judge the same HaluEval items (n = 200), gets a 7% FPR at the same coverage target, so the signal is in the text.[^s10] The paper's reading is that the semantic features miss it: embeddings "as identical to faithful text, whereas reasoning models can identify the factual divergence".[^s6]

The paper gives a cause for the tail, and the cause is a hypothesis rather than a result. Preference training rewards fluency, and the argument is that "which strongly correlates with fluency, coherence, and plausibility" means the errors that survive training resemble the truth in meaning.[^s7] Nothing here tests that training step; what was measured is the overlap in scores.

The reader-side version of the same gap is in [[plausibility-masks-error]]: there a human checks form before content, and fluent wrong answers pass. Here the scorer is the one that reads the form, through a similarity measure. A related machine-side case is [[cot-hallucination-trap]], where a rationale stays plausible while detached from the evidence. A different route to a missed contradiction, in dense retrieval, is covered in [[decoupled-support-contradiction-retrieval]].

## Limits

- One ensemble, two real-data sets, one coverage target. The claim that semantic features fail in general is a generalization from this ensemble; the paper's own abstract and discussion say so as an implication.
- The abstract says "GPT-4 as a judge achieves 7% FPR",[^s9] but the HaluEval experiment is stated as GPT-4o-mini.[^s10] My inference: the 7% figure belongs to GPT-4o-mini with one prompt template, and the paper admits that "our GPT-4 judge experiments use a single prompt template".[^s11] Prompt sensitivity was not measured, so the reasoning-judge side of the claim is one data point.
- The synthetic benchmark is not a neutral baseline. It is built so that the wrong answer is semantically far, which is why the detector works there; the paper uses this to argue that synthetic benchmarks overstate performance, and that is the reading the NQ result supports.[^s13]
- "Our study relies on established benchmarks rather than live production data".[^s12] The RAGTruth overlap is the paper's evidence of breadth across models, but it is still one archive of outputs.
- The RLHF explanation of the tail is offered, not tested (see above). The claim that "modern" hallucinations are harder than GPT-2 or GPT-3 era errors is likewise not measured in the text read.
- The paper frames cosine similarity as unsafe for guardrails. The evidence shows a failure on one benchmark pair, not a general ranking of similarity measures against each other.

## Related

- [[hard-tail-recall-threshold]] — why the tail of plausible errors sets the threshold and turns a high AUC into 100% FPR
- [[plausibility-masks-error]] — the reader-side version: form passes for content
- [[cot-hallucination-trap]] — a fluent rationale that stays plausible while detached from the evidence
- [[decoupled-support-contradiction-retrieval]] — NLI and negation as a different route to a missed contradiction
- [[llm-judge-validation-gap]] — a reasoning judge needs its own validation before its FPR can be trusted

[^s1]: arxiv-2512-15068 — "We employ an ensemble of three semantic scores"
[^s2]: arxiv-2512-15068 — "On NQ, we achieve 95.8% coverage with 0% FPR"
[^s3]: arxiv-2512-15068 — "On real data (HaluEval), the FPR degrades to 100%"
[^s4]: arxiv-2512-15068 — "are semantically indistinguishable from faithful responses"
[^s5]: arxiv-2512-15068 — "overlapping distributions persist across all models"
[^s6]: arxiv-2512-15068 — "as identical to faithful text, whereas reasoning models can identify the factual divergence"
[^s7]: arxiv-2512-15068 — "which strongly correlates with fluency, coherence, and plausibility"
[^s8]: arxiv-2512-15068 — "achieves near-perfect entailment scores"
[^s9]: arxiv-2512-15068 — "Crucially, GPT-4 as a judge achieves 7% FPR"
[^s10]: arxiv-2512-15068 — "evaluated GPT-4o-mini as a judge on the same HaluEval"
[^s11]: arxiv-2512-15068 — "our GPT-4 judge experiments use a single prompt template"
[^s12]: arxiv-2512-15068 — "Our study relies on established benchmarks rather than live production data"
[^s13]: arxiv-2512-15068 — "This guarantees semantic distance"
