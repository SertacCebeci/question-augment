---
description: "Questions tied to a named research scenario inside a project score models differently from decontextualized quiz items; the same models scored lower on the tied set than on GPQA-style Q&A."
aliases: ["scenario-grounded evaluation", "decontextualized Q&A gap", "scenario-tied questions", "SDE scenario gap"]
sources: ["arxiv-2512-15567"]
---
# Scenario-tied question gap

A question can be drawn from a research scenario, a modular unit inside a project, instead of from a general subject area. The Scientific Discovery Evaluation (SDE) builds its items this way: "This design ties every question to a research scenario, ensuring that its correctness reflects progress on a practical scientific discovery project rather than decontextualized trivia."[^s1] Domain experts first define about ten scenarios per domain where an LLM could help their own projects; questions are then sampled and vetted within each scenario, and 1,125 questions were kept after panel review.[^s2]

The measured consequence is a gap in score. State-of-the-art models reached 0.71 in biology, 0.60 in chemistry, 0.75 in materials and 0.60 in physics on SDE, while "the same class of models attains 0.84 on MMMU-Pro and 0.86 on GPQA-Diamond".[^s3] The authors read this as evidence that "proficiency in standard examinations does not guarantee mastery of the nuanced, context-dependent reasoning required for scientific discovery."[^s4]

The scenario is also where the score spreads. For gpt-5, accuracy was 0.85 on retrosynthesis planning but 0.23 on NMR structure elucidation.[^s5] Because of this spread, a domain-level score hides the weak scenario, and the authors argue that "scientific discovery is often blocked by misinformation and incorrect decisions rooted in the weakest scenario."[^s6] For someone asking, the practical reading is that a question keeps its meaning only when the context that gives it a correct answer is kept with it; a general-subject question can be answered well and still not show whether the answerer will work on the project.

A second layer is the project itself. Models there must propose testable hypotheses, get feedback from simulations or experiments, and refine. The paper reports that "question-level patterns only partially predict discovery performance", so a tied question is not a proxy for the whole loop.[^s7]

## Limits

- The two score sets are not paired. SDE and GPQA-Diamond are different items, and the comparison of 0.60–0.75 against 0.84–0.86 mixes item difficulty, answer format (multiple choice or exact match) and domain. The gap is shown across benchmarks, not by rewording the same question in and out of its scenario.
- The paper does not run a manipulation that removes scenario context from the same question and measures the change. Whether context is the cause, or whether the SDE items are simply harder, is not separated here.
- The benchmark was built by a finite expert panel. The authors say that "the benchmark inherently reflects the specific research interests" of its contributors, and that earth sciences, social sciences and engineering are not covered.[^s8]
- Scores from commercial APIs drift with provider-side changes, so the absolute numbers are a snapshot.
- Project-level method details (how hypotheses are scored) were not read in full here; the claim above rests on the authors' summary.

## Related

- [[real-query-distribution-transfer-failure]] — a benchmark drawn from academic questions misses how practitioners actually ask; the same source-mismatch concern, measured by retrieval recall
- [[context-dominates-model-choice]] — business context changes which text-to-SQL model scores well; context, not model, carries the accuracy
- [[clarification-benchmarks]] — benchmarks where the question itself is the object being judged

[^s1]: arxiv-2512-15567 — "This design ties every question to a research scenario, ensuring that its correctness reflects progress on a practical scientific discovery project rather than"
[^s2]: arxiv-2512-15567 — "In each domain, a multi-member expert panel defined roughly ten common research scenarios"
[^s3]: arxiv-2512-15567 — "the same class of models attains 0.84 on MMMU-Pro and 0.86 on GPQA-Diamond"
[^s4]: arxiv-2512-15567 — "proficiency in standard examinations does not guarantee mastery of the nuanced"
[^s5]: arxiv-2512-15567 — "NMR structure elucidation (score of 0.23)"
[^s6]: arxiv-2512-15567 — "decisions rooted in the weakest scenario"
[^s7]: arxiv-2512-15567 — "patterns only partially predict discovery performance"
[^s8]: arxiv-2512-15567 — "the benchmark inherently reflects the specific research interests"
