---
description: "Hallucination diagnosis replaces a binary faithfulness label with four scored parts (detection, span localization, explanation, correction), which can be evaluated separately."
aliases: ["hallucination diagnosis", "diagnosis over detection", "Hallucination Diagnosis Task"]
sources: ["arxiv-2601-09734"]
---
# Hallucination diagnosis task

A binary hallucination detector returns one verdict: the output agrees with its source or it does not. The paper's objection is that this verdict, though it is "capable of identifying hallucinations," does not say where the error is or how to repair it: such approaches "fail to provide interpretable and actionable feedback for model improvement, thus limiting practical utility."[^h1]

The proposed task asks for more. A diagnosing model must "not only detect hallucinations, but also perform error localization, causal explanation, and content correction."[^h2] The authors split this into four capabilities: detection, localization, explainability, and mitigation.[^h3] Mitigation means proposing a correction, or generating a revised text that agrees with the source, based on the localization and the explanation.

The mechanism is a structured report. The model is trained to write a JSON object with four fields, "report as a JSON object containing four key fields: conclusion, diagnosis, hallucinations, and corrected answer."[^h4] Each field is scored separately, and a malformed report scores zero. The format is what makes the other parts checkable: a location can only be scored if it can be parsed out of the output. The paper's localization reward is a hit-rate style signal, and their evaluation adds a validity check that each localized span is a verbatim substring of the answer.

## What was measured

No public benchmark exists for the full composite, so the evaluation takes it apart: "deconstructing it into three core sub-tasks: detection, localization, and mitigation."[^h5] Detection is accuracy, and it is measured "given that this evaluation exclusively involves samples containing hallucinations."[^h6] Localization is a hit rate plus span validity, "to ensure localized spans are verbatim substrings of the original answer."[^h7] The corrected text is scored by AlignScore, "a reference-based" factual-consistency metric.[^h8]

Two prompting baselines are compared with the trained 4B model. A single pass writes the whole report; a pipeline makes three sequential calls. The pipeline does better on the fine-grained parts: it "achieves superior performance on fine-grained tasks" such as localization and mitigation. It also "incurs high latency due to multiple LLM calls."[^h9] The text gives the cost: "32B pipeline demands 4.9×" the runtime of the single-pass baseline.[^h10]

The headline detection claim is a different measurement. The 2.4% F1 advantage over Lynx-8B is reported under "Table 3: Hallucination Detection Results."[^h11] It shows the 4B model is a good detector. It does not show that diagnosis is good, because the diagnosis result is the separate Table 5 breakdown.

My inference: once the four parts are scored apart, a failure can be assigned to a part. A report can detect an error correctly and still localize the wrong span, which a single yes-or-no label cannot show.

## Limits

- The composite is conceptualized, not benchmarked: "Lacking established public benchmarks for the full diagnosis task."[^h12] The authors' own diagnosis set is small, with "a diagnosis dataset of 285 samples."[^h13]
- Explainability is part of the definition but is not among the three scored sub-tasks, so the explanation itself is not measured in the reported results.
- Detection is measured only on hallucinated samples. A false alarm on a clean output therefore cannot appear in the reported numbers. My inference: this is the same blind spot that makes detection look better than it is when judges flag clean chains (see [[cot-judge-detection-localization-gap]]).
- The corpus is narrow: the pipeline "relies solely on Wikipedia as its source corpus."[^h14] The model is a single size: "experiments were confined to a 4B-parameter model."[^h15]
- The scope is faithfulness against a source, where "a model's output contradicts or lacks support from the provided source documents."[^h16] Other kinds of error, such as errors with no source to check against, are outside what was tested.

## Related

- [[detection-correction-gap]] — a model can name a flaw and still not act on it; diagnosis scores the naming and the correction as separate parts, but this paper does not measure the gap between them.
- [[cot-judge-detection-localization-gap]] — the measured gap between detecting an error and locating it in a chain; the diagnosis task asks the answerer for the location that judges failed to name.
- [[controlled-error-injection]] — the data construction that supplies the localization targets this task needs.

[^h1]: arxiv-2601-09734 — "fail to provide interpretable and actionable feedback for model improvement, thus limiting practical utility."
[^h2]: arxiv-2601-09734 — "models to not only detect hallucinations, but also perform error localization, causal explanation, and content correction"
[^h3]: arxiv-2601-09734 — "Detection: Accurately identifying if the generated content aligns with the source context."
[^h4]: arxiv-2601-09734 — "report as a JSON object containing four key fields: conclusion, diagnosis, hallucinations, and corrected answer"
[^h5]: arxiv-2601-09734 — "deconstructing it into three core sub-tasks: detection, localization, and mitigation"
[^h6]: arxiv-2601-09734 — "given that this evaluation exclusively involves samples containing hallucinations"
[^h7]: arxiv-2601-09734 — "to ensure localized spans are verbatim substrings of the original answer"
[^h8]: arxiv-2601-09734 — "using AlignScore (Zha et al. 2023) (AS), a reference-based"
[^h9]: arxiv-2601-09734 — "pipeline achieves superior performance on fine-grained tasks"
[^h10]: arxiv-2601-09734 — "32B pipeline demands 4.9×"
[^h11]: arxiv-2601-09734 — "Table 3: Hallucination Detection Results"
[^h12]: arxiv-2601-09734 — "Lacking established public benchmarks for the full diagnosis task"
[^h13]: arxiv-2601-09734 — "This process resulted in a diagnosis dataset of 285 samples"
[^h14]: arxiv-2601-09734 — "solely on Wikipedia as its source corpus"
[^h15]: arxiv-2601-09734 — "experiments were confined to a 4B-parameter model"
[^h16]: arxiv-2601-09734 — "contradicts or lacks support from the provided source documents"
