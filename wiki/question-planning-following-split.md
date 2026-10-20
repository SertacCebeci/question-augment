---
description: "A question chain can be scored on two separate skills: choosing the next helpful sub-question (planning) and answering a given sub-question (following), which vary differently across models."
aliases: ["planning and following", "Planning vs Following", "question-space vs answer-space exploration", "CoQ planning/following disentanglement"]
sources: ["arxiv-2512-11995"]
---
# Planning and following in a question chain

A multi-step exploration can be written as a chain of sub-questions, each with its answer, that together settle an original question. V-REX calls this a Chain-of-Questions (CoQ) and states the point of the form directly: "CoQ enables us to disentangle the reasoning capabilities into Planning and Following when facing complex tasks".[^c1] The two halves are defined as different abilities: "the proficiency in formulating informative intermediate questions (Planning)", and "the accuracy in addressing these sub-questions (Following)".[^c2]

The split is made by construction. For planning, the human-built ground-truth chain is branched at each node "by adding several uninformative, distracting questions",[^c3] and the model is shown the true answers to earlier steps. It therefore "does not need to solve the sub-questions itself but only needs to decide which question to ask next".[^c4] For following, the same chain is shown with the true question at each step, and the model must pick the correct answer among distractor answers at that step. The authors state the purpose of the design: "This design explicitly isolates the Planning ability from Following."[^c5] Each half is therefore scored while the other is held fixed, which a single end-to-end accuracy cannot do.

## What the split showed

The work measures 702 samples, with 2,504 questions over 2 to 6 steps each, across open-source and proprietary vision-language models. Three findings bear on how the two abilities behave.

- **Variance differs.** Models of the same size vary less on following than on planning: "the same size is smaller in Following than in Planning."[^c6] The authors read this as a sign that exploratory ability, meaning the planning side, is the less settled one.
- **Balance depends on scale.** "Smaller models are better at Following than Planning while larger models have more balanced performance."[^c7] The ratio of following to planning approaches one as size grows.
- **Recovery is asymmetric.** Recovery is defined as reaching "the correct final answer despite making at least one incorrect intermediate step".[^c8] Models recover better from a failed planning step: "VLMs are better at recovering from failed planning steps than from failed following steps."[^c9] The explanation given is that distracting questions "provide fewer clues but do not necessarily derail the final answer", whereas errors in the answer space "are more likely to propagate to an incorrect final answer".[^c10]

Inference (this wiki, not a finding of the paper): the split suggests that asking the next useful question and using an answer are separate competences that a person or model can have to different degrees. A reasoner that answers well may still choose its sub-questions poorly, and the reverse. The paper does not test people, and the claim that the two are separable in human asking is not established here.

## Limits

- **The planning score depends on a chosen answer key.** The ground-truth chains were built by experts: "We rely on human experts to collect high-quality ground-truth QA chains".[^c11] A question counts as helpful because the annotators say so, and a different but also useful sub-question is scored as wrong.
- **The space is closed.** The work evaluates "a series of multiple-choice questions (MCQ) with the CoQ process",[^c12] because free-form exploration cannot be rated reliably. The planning score measures choice among offered options, not the open generation of questions.
- **It is a measurement, not a method.** The paper says so: "CoQ is not a prompting method" but "a way to conduct finegrained evaluation of the exploratory visual reasoning ability of model".[^c13] Nothing here shows that training on planning improves final accuracy.
- **Hints do not always help.** Giving the chain's true steps raises final accuracy for most models and categories: "higher accuracy on final questions when intermediate steps are introduced".[^c14] But "The Retrieval category shows relatively minor improvements in both tasks",[^c15] and for some models the chain "can generate distractive reasoning paths or omit essential reasoning cues in Planning task".[^c16]
- **One domain.** All items are visual reasoning tasks drawn from web images and public benchmarks, in four categories and 15 scenarios. Whether the planning/following gap holds for textual or dialogue asking is not tested.
- The distractors are produced by a language model in a two-stage pipeline and then filtered, so the distractor quality is itself a modelling choice that the measurement inherits.

## Related

- [[chain-of-inquiry-scaffolding-effect]] — an ordered question chain as a scaffold for the answerer; this note separates the chain's asking step from its answering step, and the measured scaffold gains there are the answering side.
- [[self-ask-decomposition]] — the model emits its own sub-question; the planning task here scores which sub-question is chosen among fixed alternatives.
- [[dependency-aware-subquestion-scheduling]] — orders sub-questions by which are ready; the planning task asks which sub-question is helpful, not which is unblocked.

[^c1]: arxiv-2512-11995 — "CoQ enables us to disentangle the reasoning capabilities into Planning and Following when facing complex tasks"
[^c2]: arxiv-2512-11995 — "the proficiency in formulating informative intermediate questions (Planning)"
[^c3]: arxiv-2512-11995 — "by adding several uninformative, distracting questions"
[^c4]: arxiv-2512-11995 — "not need to solve the sub-questions itself but only needs to decide which question"
[^c5]: arxiv-2512-11995 — "This design explicitly isolates the Planning ability from Following."
[^c6]: arxiv-2512-11995 — "the same size is smaller in Following than in Planning"
[^c7]: arxiv-2512-11995 — "Smaller models are better at Following than Planning while larger models"
[^c8]: arxiv-2512-11995 — "reach the correct final answer despite making at least one incorrect intermediate step"
[^c9]: arxiv-2512-11995 — "VLMs are better at recovering from failed planning steps than from failed"
[^c10]: arxiv-2512-11995 — "are more likely to propagate to an incorrect final answer"
[^c11]: arxiv-2512-11995 — "We rely on human experts to collect high-quality ground-truth QA chains"
[^c12]: arxiv-2512-11995 — "a series of multiple-choice questions (MCQ) with the CoQ process"
[^c13]: arxiv-2512-11995 — "a way to conduct finegrained evaluation of the exploratory visual reasoning ability of model"
[^c14]: arxiv-2512-11995 — "higher accuracy on final questions when intermediate steps are introduced"
[^c15]: arxiv-2512-11995 — "The Retrieval category shows relatively minor improvements in both tasks"
[^c16]: arxiv-2512-11995 — "distractive reasoning paths or omit essential reasoning cues in Planning task"
