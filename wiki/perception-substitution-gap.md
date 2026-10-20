---
description: "Replacing an image with a text rendering of the same algorithmic puzzle, algorithm held fixed, measures how much of a multimodal model's error sits in perception rather than reasoning."
aliases: ["textual rendering ablation", "perception bottleneck by text substitution", "multimodal-minus-text accuracy gap"]
sources: ["arxiv-2601-00215", "arxiv-2512-21329"]
---
# Perception substitution gap

Take a task that needs two things: reading an image, then running an algorithm on what was read. Give the model the same content as a deterministic text string instead of the picture, keep the question and the algorithm unchanged, and compare accuracy. The difference estimates how much of the failure lies in extracting information from the image rather than in what is done with it. The work this note rests on applies the test to nine algorithmic visual puzzles (Clock, Checker Move, Maze, Move Box, N-Queens and four more) with Claude-3.5 and Claude-3.7 in thinking mode. Its text forms are "simple strings where colors are encoded as characters," so the two conditions differ in input format and not in the task.[^c1]

The measured gap is large. Substituting the image "with its textual rendering yields large and consistent gains," averaging 26.7 points for Claude-3.5 and 23.6 for Claude-3.7.[^c2] The gap is widest where perceptual demand is highest. On Clock, Claude-3.7 improves from 7% to 83%, and on N-Queens both models reach near-perfect accuracy.[^c3] Because the question and the algorithm are the same in both conditions, the authors read the change as a change in extraction difficulty alone: "the only factor that has changed is the difficulty of extracting the relevant information from the visual input."[^c4]

The traces point the same way. In the image condition, "errors most often originate at the perception stage and then propagate through reasoning chains that are otherwise internally valid."[^c5] The authors' summary is that "the reasoning components of these models are largely intact for the algorithmic tasks studied here; the bottleneck is in feeding them correct inputs."[^c6]

A second study estimates the same share with a different operation, and reads its result the same way. It runs a two-stage pipeline: a vision-language model turns each image into a natural-language description, one image at a time, and a second model induces and applies the rule from those descriptions. The first stage is built to add no cross-image signal, so the reasoner's input changes in readability and not in what it implies.[^c11] The authors classify each failure by the earliest step that breaks and find that approximately 80 percent of failures are perception errors.[^c12] In the one-stage setting on Mini-ARC the figure is 86.4 percent of all errors.[^c13] Because the pipeline has a separate perception stage, it places a failure at a stage boundary, which is finer than a text substitution gives. It still does not say which computation inside the model fails (my inference, not measured in either study).

The method is a substitution, so it compares two inputs, not a perception stage with a reasoning stage inside the model. The gap says what the model loses when the picture is harder to read than the same content written out. It does not say where inside the model the loss happens.

## Limits

- The authors present the text condition as an upper bound. They concede the text forms are highly structured and may overstate the gap: "overstate the perception gap."[^c7] The bound is "the maximum performance gap attributable to visual perception," in the authors' words.[^c8] A text string can carry cues an image encoder does not expose, so the gap mixes perception with the ease of reading tokens. This is my inference from the text forms, not a measured effect.
- The bottleneck test in the text is run on Claude models only. The Qwen-2.5-VL-7B model that is trained later is not run in the text condition in the sections read.
- The puzzles are synthetic and algorithmic, with 100 visual samples per category in the original set.[^c9] The result does not transfer to photographs, charts or documents, where the image may carry information that no text form captures. That is my reading of the scope, not a tested claim.
- The evaluation is open-ended. The authors chose this because "models often guessed the correct answer from the provided options, even when" their reasoning was wrong.[^c10] The gap would look different under multiple choice, where guessing lifts accuracy in both conditions.
- One category set, two Claude models, one run per condition. No variance across seeds or prompts is reported in the text read.
- The perception stage is itself a model, and its output depends on a prompt that injects generic human perceptual priors. The authors say their descriptions "should not be interpreted as an optimal or canonical intermediate representation for abstract reasoning."[^c15] The share so measured belongs to this description format as much as to the image.
- The attribution is manual. It rests "on manual inspection of model outputs and reasoning traces."[^c14] The pipeline also does not hold reasoning fixed: the authors note the two-stage design "may slightly increase the inductive reasoning difficulty," since the model gets more information to induce from.[^c16]

## Related

- [[functional-perception-gap]] — another "perception gap," measured by whether anatomically trained models can read PET tracer intensity; the same word for a different test
- [[text-modality-dominance]] — the converse direction: corrupting the text channel of omni-modal models, not replacing the image with text
- [[cot-hallucination-trap]] — when visual grounding is weak, fluent reasoning decouples from the image; the puzzle traces show the same inheritance of a misread input
- [[counterfactual-image-grounding-audit]] — tests whether an answer depends on the image by blanking or swapping it, rather than measuring the cost of reading it

[^c1]: arxiv-2601-00215 — "simple strings where colors are encoded as characters"
[^c2]: arxiv-2601-00215 — "with its textual rendering yields large and consistent gains"
[^c3]: arxiv-2601-00215 — "On Clock, Claude-3.7 improves from 7%"
[^c4]: arxiv-2601-00215 — "the only factor that has changed is the difficulty of extracting the relevant information from"
[^c5]: arxiv-2601-00215 — "Errors most often originate at the perception"
[^c6]: arxiv-2601-00215 — "is in feeding them correct inputs."
[^c7]: arxiv-2601-00215 — "overstate the perception gap"
[^c8]: arxiv-2601-00215 — "that quantifies the maximum performance gap attributable to visual perception"
[^c9]: arxiv-2601-00215 — "provides only 100 visual samples per category"
[^c10]: arxiv-2601-00215 — "models often guessed the correct answer from the provided options, even when"
[^c11]: arxiv-2512-21329 — "ensuring that no crossimage inductive signals are leaked during this stage."
[^c12]: arxiv-2512-21329 — "observe that approximately 80% of failure cases"
[^c13]: arxiv-2512-21329 — "On Mini-ARC, perception errors account for 86.4% of all errors in setting 1(a) (standard one-stage)"
[^c14]: arxiv-2512-21329 — "on manual inspection of model outputs and reasoning traces."
[^c15]: arxiv-2512-21329 — "should not be interpreted as an optimal or canonical intermediate representation for abstract reasoning."
[^c16]: arxiv-2512-21329 — "inductive reasoning difficulty since the model must perform"
