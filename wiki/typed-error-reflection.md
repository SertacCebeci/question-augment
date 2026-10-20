---
description: "A second pass reviews an NER output against four named error types (span, type, spurious, omission) and revises it; removing that stage lowered F1 on three of three datasets tested."
aliases: ["reflective analysis", "structured self-assessment", "reflection and correction stage", "error-category self-review"]
sources: ["arxiv-2511-19083"]
---
# Typed-error reflection

Generic self-correction asks a model to look again at its answer without saying what could be wrong. Typed-error reflection gives the review a list of error kinds to check. In the KDR-Agent paper, the NER prediction is followed by a reflection step. It compares the output with the input and sorts the failures into four categories: a span error (the boundary is too broad or too narrow), a type error (a correct mention given the wrong type), a spurious detection (an entity the input does not justify), and an omission (a valid mention left out).[^c1] The reflection writes a diagnostic report with error labels, supporting justifications and suggested revisions, and a second prediction is made from that report.[^c2]

The authors justify the step by analogy: the reflection "enables the model to revise its output through self-criticism, similar to how human annotators refine labels through multiple passes".[^c3] That analogy is theirs and was not tested as a mechanism.

My reading, not the paper's words: the list fixes what the review looks for. A report that says "this span is too narrow" or "this mention is missing" is a claim the second prediction can act on. A reviewer asked only "is anything wrong?" has no such handle. This is the difference from [[intrinsic-self-correction-convergence]], where the instruction gives only the goal.

What was measured. The Reflection & Correction stage is removed in the GPT-4o ablation.[^c4] The table caption gives the setting: "Ablation study results on the GPT-4o LLM backbone (F1 score)".[^c5] Without the stage, F1 falls from 79.41 to 75.91 on NCBI, from 71.85 to 70.17 on OntoNotes 5.0, and from 60.87 to 57.81 on Twitter NER-7. The authors summarise it as: "Removing the Reflection & Correction stage consistently results in performance drops across all domains".[^c6] A separate error analysis, on the same three datasets, reports per-type error rates with and without the stage, and concludes that "the reflection module consistently reduces all error types".[^c7] The gains are largest on the biomedical and social-media sets. On news, the authors call the improvement "modest, likely due to its syntactic regularity and semantic clarity".[^c8]

## Limits

- The ablation removes the whole two-stage pass, not the typed list. The text does not test a generic self-review prompt as a control, so the typed categories are not separated from the second pass itself. This is the central gap for this mechanism.
- The error analysis is hard to read cell by cell. As extracted from the text, the type and spurious rows do not map cleanly onto the datasets and conditions, so I cannot confirm "consistently reduces all error types" for each cell. That claim is the authors'.
- The same model proposes the errors and makes the correction. No external checker is compared. Intrinsic self-correction work finds that repeated generic rounds converge without outside feedback; that result is about generic instructions and repeated rounds, and it does not test a single typed review on NER.
- The ablation runs on GPT-4o only.[^c9] The backbone-scale analysis uses Qwen models, and no ablation of the reflection stage is reported there, so the effect at smaller scales is not in the text.
- The reported values are single F1 numbers. The text gives no spread across runs.

## Related

- [[intrinsic-self-correction-convergence]] — generic self-correction with no external feedback converges over rounds; a typed review is one round with a named checklist, and its behaviour over repeated rounds is untested here.
- [[specific-actionable-self-feedback]] — feedback that says what is wrong; the four categories here are a fixed vocabulary of that kind of feedback.
- [[failure-mode-taxonomy]] — a taxonomy used to locate agent failures after a run; this one is used inside the run, as the prompt for the review.
- [[contrastive-entity-demonstrations]] — the same four error types appear as perturbations in the demonstrations, so the prompt shows these errors before the review looks for them.

[^c1]: arxiv-2511-19083 — "we categorize common NER prediction errors into the following four types"
[^c2]: arxiv-2511-19083 — "R denotes a structured diagnostic report containing"
[^c3]: arxiv-2511-19083 — "output through self-criticism, similar to how human annotators refine labels through multiple passes"
[^c4]: arxiv-2511-19083 — "Removing the Reflection & Correction stage consistently"
[^c5]: arxiv-2511-19083 — "Ablation study results on the GPT-4o LLM backbone (F1 score)"
[^c6]: arxiv-2511-19083 — "results in performance drops across all domains"
[^c7]: arxiv-2511-19083 — "the reflection module consistently reduces all error types"
[^c8]: arxiv-2511-19083 — "likely due to its syntactic regularity and"
[^c9]: arxiv-2511-19083 — "using GPT-4o as the backbone"
