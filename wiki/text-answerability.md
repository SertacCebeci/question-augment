---
description: "An item is text-answerable when a language model gets it right without the image; text-only LLMs matching vision models on remote-sensing reasoning show wording alone can carry many answers."
aliases: ["language-prior solvability", "text-only solvability", "blind solvability", "language-prior answerability"]
sources: ["arxiv-2512-17319", "arxiv-2512-05277", "arxiv-2512-03479", "arxiv-2512-01045", "arxiv-2511-21025"]
---
# Text-answerability

Text-answerability is a property of a question–answer item, not of a model: how often a model that never sees the image gets the item right. It matters because a multiple-choice or templated item can carry its answer in its wording, its options, or common-sense priors. A model then reads the answer off the text, and the picture does no work. The remote-sensing paper that introduces RSHR-Bench reports that "text-only LLMs can perform competitively with multimodal VLMs on RS reasoning tasks without seeing the" images, and reads this as "a serious mismatch between current benchmarks and the intended evaluation of visual understanding."[^c1] On XLRS-Bench, a text-only Qwen3-8B "attains 51.6% accuracy, surpassing the GPT-4o at 45.2% (multimodal setting)."[^c2] The mechanism it names is the answer format: multiple-choice formats are "allowing models to exploit textonly priors and inflate scores."[^c3]

The measure is applied to items before release. The authors have text-only LLMs answer each item without the image, and "if their accuracy in this setting is high (typically above 30%), we treat the item as overly solvable from language alone and revise it."[^c4] Revision targets the wording: "Descriptive cues can leak labels," so a cue such as "forest → green" can let a reader eliminate options by common sense rather than visual evidence.[^c5] The loop runs "until correct solutions require genuine visual grounding and all options are free of suggestive cues."[^c6]

The same probe can be read the other way. On LRS-VQA, text-only models "perform substantially worse" than the multimodal ones, which the authors take as evidence that items there need the imagery: "models perform substantially worse: GPT-4 (text-only)".[^c7] So text-answerability is a property of a benchmark's items, and it varies across benchmarks; a benchmark can be low on it without being high on visual understanding.

The probe also appears at the level of a whole benchmark. In the driving video benchmark TAD, the authors run a Blind configuration, in which the model gets only the question, beside frames-only and frames-plus-map configurations. Their comparison of Blind with frames-only is read as a validity check: it "confirms that the benchmark questions cannot be answered without visual input."[^c10] The passages read give no per-item removal rule for TAD, so the check is a reported comparison, not a filter on items (my inference from the reported tables).

ProcObject-10K applies the same probe as a construction filter, before release. The authors have a text-only LLM answer each generated question, and a question the text alone answers well is discarded, since the step targets "questions answerable without video grounding" and such questions "would artificially inflate benchmark performance."[^c11][^c12] The step removes "out approximately 30%" of the initial samples.[^c13] The probe also appears at the level of the benchmark. A language-only model, GPT-5.4-Mini in its blind setting, reaches an "Answering Judge score of 3.14 despite having no video input", against 3.42 for its multimodal counterpart.[^c14] The authors read the closeness of the two as "The reliance on commonsense reasoning is further" validated by language-only models.[^c15]

Med-CRAFT, a construction system for medical instructional-video QA, treats the image dependence of an item as a generation setting rather than only a filter. Its traversal configuration is described as yielding reasoning chains with "visual-dependency levels," so the share of items that need the image is requested before generation, not only removed after.[^c16] Its downstream table then splits accuracy by evidence modality. The text-only baseline, DeepSeek-R1, scores lower on visual items than on textual ones, "(0.60) than on visual (0.20) and cross-modal questions (0.25)."[^c17] That is the same probe as above, read per item category rather than per benchmark. The text read does not define the visual-dependency levels, so how they map onto text-answerability is not known from it (my inference).

CaptionQA applies the same probe as a construction filter for a caption benchmark, where the retained questions are later answered from captions rather than from the image. Each question is put to a text-only model, Qwen2.5-72B, with the image hidden, ten times with shuffled options. The item is removed when the text-only accuracy exceeds a threshold that depends on the option count, the bar being "exceeds an option-dependent" rather than one fixed share, set just above chance.[^c19] In the paper's words, "we treat the question as text-answerable and discard it" when that happens.[^c20] The caption-side measure that this benchmark builds on is [[caption-utility-gap]].

## Limits

- The 30 % threshold is the authors' choice; the passages read give no sensitivity analysis for it.
- The filter is a particular text-only model with its own biases. The authors note that "Qwen3-8B tends to prefer" one orientation and changed the answer key to correct for it.[^c8] An item pushed below the threshold for Qwen3-8B and Llama3-8B may still be answerable by another model (my inference; not tested here).
- Low text-only accuracy does not show that the image is used. It shows only that these models do not solve the item from text. Whether a model uses the image is a separate question, tested by removing the image from that model (see [[counterfactual-image-grounding-audit]]).
- The text-only and multimodal numbers come from different model sets: "text-only (Llama3-8B and Qwen3-8B) and multimodal (image+text; GPT-4o and GPT-4o mini)".[^c9] A gap between the two groups mixes item difficulty with model quality, so it is a diagnostic, not a clean estimate.
- The paper's remedies are human post-editing and iterated rewriting. The passages read do not show that the revised items are harder for multimodal models in a controlled way.
- The video filter in ProcObject-10K uses one text-only LLM and a judge threshold. Whether the roughly 30 % share removed would change with another text model is not reported in the text read (my inference).
- The Med-CRAFT split is a single paper's diagnostic. Its visual rows include a model that took part in building the dataset, and the authors warn that "the possibility of data bias cannot be ruled out."[^c18]

## Related

- [[counterfactual-image-grounding-audit]] — the model-side version: the image is removed from one model; text-answerability is the item-side version, the image is removed from a text-only model
- [[text-modality-dominance]] — reliance on text over vision, measured by corrupting one modality
- [[option-matching-shortcut]] — option-level cues in multiple-choice items, one route by which an item becomes text-answerable

[^c1]: arxiv-2512-17319 — "text-only LLMs can perform competitively with multimodal VLMs on RS reasoning tasks without seeing the"
[^c2]: arxiv-2512-17319 — "a text-only LLM (Qwen3-8B) attains 51.6% accuracy, surpassing the GPT-4o at 45.2% (multimodal setting)"
[^c3]: arxiv-2512-17319 — "allowing models to exploit textonly priors and inflate scores"
[^c4]: arxiv-2512-17319 — "we treat the item as overly solvable from language alone"
[^c5]: arxiv-2512-17319 — "Descriptive cues can leak labels"
[^c6]: arxiv-2512-17319 — "We iterate rewriting until correct solutions require genuine visual grounding"
[^c7]: arxiv-2512-17319 — "models perform substantially worse: GPT-4 (text-only)"
[^c8]: arxiv-2512-17319 — "Qwen3-8B tends to prefer"
[^c9]: arxiv-2512-17319 — "text-only (Llama3-8B and Qwen3-8B) and multimodal (image+text; GPT-4o and GPT-4o mini)"
[^c10]: arxiv-2512-05277 — "the benchmark questions cannot be answered without visual input"
[^c11]: arxiv-2512-03479 — "questions answerable without video grounding"
[^c12]: arxiv-2512-03479 — "would artificially inflate benchmark performance"
[^c13]: arxiv-2512-03479 — "out approximately 30%"
[^c14]: arxiv-2512-03479 — "Answering Judge score of 3.14 despite having no video input"
[^c15]: arxiv-2512-03479 — "The reliance on commonsense reasoning is further"
[^c16]: arxiv-2512-01045 — "visual-dependency levels. These reasoning chains are subsequently"
[^c17]: arxiv-2512-01045 — "(0.60) than on visual (0.20) and cross-modal questions (0.25)"
[^c18]: arxiv-2512-01045 — "the possibility of data bias cannot be ruled out"
[^c19]: arxiv-2511-21025 — "exceeds an option-dependent"
[^c20]: arxiv-2511-21025 — "we treat the question as text-answerable and discard it"
