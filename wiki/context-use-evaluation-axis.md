---
description: "Parametric-only medical QA scores barely separate similar models, while the same questions with a document added split them widely; the two measure different capacities."
aliases: ["context-conditioned evaluation", "parametric versus contextual evaluation axis"]
sources: ["arxiv-2512-02299"]
---
# Context-use evaluation axis

A question-answering benchmark that asks a model to answer from memory measures one capacity: what the model already stores. A model can score well or badly on it without its use of supplied evidence being tested at all. Zhang et al. argue that this is why the standard medical QA benchmarks fail to separate models: they are "weak at comprehending difference among models' capabilities because they primarily assess a model's parametric knowledge."[^d1] In their comparison on MedMCQA, MedQA and PubMedQA, the larger models sit close together: "the difference among larger language models (7-8B) is minor."[^d2]

The same questions, once a document is attached, spread the models apart. HealthContradict gives each yes/no health question either no context, a correct document, an incorrect one, or both in two orders. For the pair Meditron3-8B and its general-domain base Llama-3.1-8B-Instruct, the gap is 4.5 points with no context, 21.1 points with the correct document and 23.0 points with the incorrect one.[^d3] The same models that look alike from memory differ by about five times as much once context is part of the question. The authors' conclusion is that the benchmark "better captures the difference of models' performance" than the existing medical QA sets.[^d4]

The axis is therefore the condition under which the answer is produced, not the question alone. A parametric benchmark holds the context fixed at nothing and so cannot show how a model handles a document that is right, wrong or contradictory. A context-conditioned benchmark shows that, and it also exposes the failure modes split by [[parametric-context-failure-rates]]. The two evaluations do not replace each other. What a parametric score measures, stored knowledge, is not something a context condition can test; the claim is that a model's usefulness with evidence in hand is a separate quantity that a parametric score does not reveal.

This is a claim about what a benchmark can separate, and that is my reading of the paper's comparison. It does not say the parametric benchmarks are invalid for their own purpose. Nor does it say that a larger spread under context is a better measurement by itself: a spread can also come from prompt format.

## Limits

- The discrimination claim is the authors' own comparison, made on one benchmark against three parametric ones. No formal test of which benchmark separates models better is reported, and the spread between models is not converted into an effect size.
- The spread under context could partly reflect the prompt format, which the authors themselves flag: "variables exist between the Prompt NC (using only parametric" memory and the context prompts.[^d5]
- The benchmark is small and drawn from one source: "the benchmark is constrained by the scope of the TREC resources and may not fully capture evolving public health issues."[^d6] The 81 questions and 920 pairs do not show that the spread holds for other domains, or for free-form answers.
- The reported gaps are at 7–8B. The paper says the difference among the larger parametric models is minor, and it does not show a context-conditioned spread at larger scale.
- Context-use was measured with a single document pair per question. The effect of many documents, or of a retrieval pipeline that chooses them, is not in this work.

## Related

- [[parametric-context-failure-rates]] — the two conditional rates that read the same context conditions instance by instance
- [[parametric-knowledge-gates-retrieval-noise-damage]] — retrieved noise hurts where the model's own knowledge is weak, so a parametric score alone would not predict how context changes an answer
- [[conflicting-evidence-order-effect]] — the order variants of the same context conditions, a finer cut on the same axis

[^d1]: arxiv-2512-02299 — "they primarily assess a model’s parametric knowledge"
[^d2]: arxiv-2512-02299 — "the difference among larger language models (7-8B) is minor"
[^d3]: arxiv-2512-02299
[^d4]: arxiv-2512-02299 — "better captures the difference of models’ performance"
[^d5]: arxiv-2512-02299 — "variables exist between the Prompt NC (using only parametric"
[^d6]: arxiv-2512-02299 — "the benchmark is constrained by the scope of the TREC resources"
