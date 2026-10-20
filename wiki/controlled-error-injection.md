---
description: "A correct answer edited at a chosen point yields a wrong answer whose error and location are known by construction, so the label is only as sound as the checks applied to the edit."
aliases: ["hallucination injection", "controlled fact fabrication", "error injection into correct responses"]
sources: ["arxiv-2601-09734", "arxiv-2512-05145"]
---
# Controlled error injection

Start from a response taken as correct and edit it at a chosen point. The edited response is wrong in a way the editor chose, and the edit marks where the error is. Nobody has to inspect the output to find the error: the location is a by-product of the construction.

The paper's pipeline does this in three ways. Direct injection "creates factual errors by replacing key entities," the example being a "red rose" changed to a "pink rose."[^e1] The paper says it "directly introduces errors into" responses that were correct.[^e2] Reasoning-chain injection, used for logic and maths, "generates logical hallucinations by perturbing a key step in a correct" chain.[^e3] A third edit replaces a precise value with a vague one, which yields "outputs that are semantically plausible but not strictly faithful to the source."[^e4] The authors apply this last edit only to summarization, "as such ambiguity is unacceptable" in reasoning and mathematics.[^e5]

Context deletion is a related edit with the opposite direction. "information deletion removes details pertinent to the original answer," which creates a controlled case of factual inconsistency with the source.[^e6]

A second use puts the same move under training rather than testing. In arxiv-2512-05145 a VLM judge is trained on preference pairs whose direction is fixed by the edit. For open-ended tasks such as captions, the model writes an original response and a second generation is altered "by prompting the model to introduce specific" inaccuracies, the edited version being the less preferred one.[^e12] The authors state the premise openly: "while we cannot verify absolute accuracy, systematically introducing errors creates" a reliable ranking, with the original preferred over the degraded version.[^e13] Here the injected label is a direction, not a located fact, and the pair feeds a gate on the judge's own reasoning, described in [[verdict-gated-reasoning-trace]].

## How the location becomes a label

The metadata stage carries the location forward. "Sentence-Level Annotation, which marks the specific location of hallucinations," is listed as one of the core labels, and it is what trains the localization part of the diagnosis task.[^e7] The label is therefore produced from the edit rather than from a reader's judgment. My inference: this is what lets the construction scale, and it is also what ties the label's correctness to the edit.

## What checks the label

Two checks run before a sample is kept. An LLM scores each query-answer pair for "clarity, fluency, and coherence (while ignoring correctness)."[^e8] That check is blind by design to the property the edit changes, so it guards fluency and not the label. The label itself is checked with "an ensemble-based approach to enhance labeling accuracy."[^e9] The ensemble is "An ensemble of top-tier classifiers (e.g., Lynx) and LLM-as-a-Judge" methods, combined by confidence.[^e10]

The same construction shows up in another work the wiki holds: [[cot-judge-detection-localization-gap]] inserts one inconsistent step into a human-verified chain, so the error position is known in advance. The two works use the construction for different purposes, one as a test and one as training data.

## Limits

- The known location is the location of the edit. Whether the edited answer is wrong in the labelled way depends on the ensemble, and that ensemble is made of LLM judges. I found no agreement rate or error rate for the label check in the text; this is my reading, not a figure from the paper.
- The text I read has no ablation separating the injection strategies from the unedited seed samples. So the paper does not show that injected samples teach localization better than natural errors would, or than no augmentation at all.
- Edited errors are of the kinds the editor writes: a swapped entity, a perturbed step, a vaguer number. My inference: naturally occurring hallucinations may differ in kind, and a model trained on the edits may learn the edit's signature. The paper does not test this.
- The source corpus is Wikipedia only, "solely on Wikipedia as its source corpus."[^e11] Whether the construction transfers to other domains is untested.
- The training-side edit carries no located label. In arxiv-2512-05145 the edit sets only which of two responses is preferred, and the authors concede that absolute accuracy is not verified. A pair can be "correct" by construction and still be a poor preference if the degraded response is not in fact worse. The paper's open-ended results are on its own benchmarks, and the text does not separate the edit's contribution from the rest of the pipeline.

## Related

- [[hallucination-diagnosis-task]] — the task whose localization targets this construction supplies.
- [[cot-judge-detection-localization-gap]] — the same one-step injection used as a test, to measure whether judges can name the broken step.
- [[verdict-gated-reasoning-trace]] — the training use of the same edit: the injected direction is the known preference a judge's own traces are checked against.

[^e1]: arxiv-2601-09734 — "creates factual errors by replacing key entities"
[^e2]: arxiv-2601-09734 — "This strategy directly introduces errors into"
[^e3]: arxiv-2601-09734 — "generates logical hallucinations by perturbing a key step in a correct"
[^e4]: arxiv-2601-09734 — "outputs that are semantically plausible but not strictly faithful to the source"
[^e5]: arxiv-2601-09734 — "as such ambiguity is unacceptable"
[^e6]: arxiv-2601-09734 — "information deletion removes details pertinent to the original answer"
[^e7]: arxiv-2601-09734 — "Sentence-Level Annotation, which marks the specific location of hallucinations"
[^e8]: arxiv-2601-09734 — "pair for clarity, fluency, and coherence (while ignoring correctness)"
[^e9]: arxiv-2601-09734 — "an ensemble-based approach to enhance labeling accuracy"
[^e10]: arxiv-2601-09734 — "An ensemble of top-tier classifiers (e.g., Lynx) and LLM-as-a-Judge"
[^e11]: arxiv-2601-09734 — "solely on Wikipedia as its source corpus"
[^e12]: arxiv-2512-05145 — "by prompting the model to introduce specific"
[^e13]: arxiv-2512-05145 — "while we cannot verify absolute accuracy, systematically introducing errors creates"
