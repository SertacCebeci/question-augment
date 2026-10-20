---
description: "Scoring an answer as correct AND parseable (output accuracy) exposes a format gap that task accuracy hides: 77-85% task accuracy can coexist with 0% usable replies."
aliases: ["output accuracy", "structured-output reliability gap", "correct but unusable"]
sources: ["doi-10-48550-arxiv-2605-02363", "arxiv-2512-13374", "arxiv-2512-11315"]
---
# Output accuracy and the format gap

Galeone et al. score a reply on two independent things: whether the answer is right (task accuracy, recovered from any signal in the text) and whether the reply parses as JSON with all required fields (json_valid). Their primary metric, output accuracy, is the product of the two.[^c1] The rationale is deployment: a reply that is right but unparseable cannot be consumed downstream, so it is operationally a wrong answer.[^c2]

## What the split reveals

With no system prompt, three 7-9B models reached 77-85% task accuracy on GSM8K and 0% output accuracy on both datasets, so the bottleneck was format, not reasoning.[^c3] A minimal hand-written JSON instruction did not fix this in general. Gemma 2-9B wrapped every JSON reply in markdown fences; the fallback parser recovered 88.4% task accuracy but no output was parseable.[^c4] GPT-4o showed the same fence-wrapping default, so the gap is not confined to small models.[^c5]

Because the fence is a model-specific default that a static prompt does not suppress, the cure the authors tested was iterative: an optimizer model reads the target model's failing traces and rewrites the system prompt. Gemma went from 0% output accuracy at epoch 1 to a breakthrough at epoch 2 once the optimizer found and suppressed the fence.[^c6] The reported result is 84-87% output accuracy on GSM8K and 34-40% on MATH.[^c7]

The quality of the optimizing model mattered: replacing Claude Sonnet 4.5 with Claude 3 Haiku as the meta-agent dropped mean output accuracy to 61.0% and raised run-to-run standard deviation from under 1 pp to 21.8 pp.[^c8]

Grammar-constrained decoding guarantees syntactic validity but cost 3.6x-8.2x latency here and in places degraded task quality, while the optimized prompt ran at near-NAIVE latency.[^c9] Whether a format is achieved by instruction, grammar, or tuning therefore changes the cost of the answer as well as its rate of validity (see [[structured-output]]).

## What it means for asking and answering

The measured quantity depends on who consumes the reply. A question whose answer is read by a parser has a second correctness condition that a content-only grader never sees. This reading is mine, not the paper's: scoring only content overstates how well a question-answer exchange worked whenever the reply shape is part of the request.

A null produced by a failed output structure is also not the same thing as a refusal. In a study of combinatorial-optimization features, the structured decoder records a null in two cases that look alike. One is a calibrated abstention. The other is a reply that never completes its structure, after a reasoning trace has used up the generation budget. The authors state that "The output is identical in form to a calibrated abstention," and that the second case, a structured-output failure, "leaves the pipeline with" non-informative gaps.[^c10][^c11] A format-gated score therefore cannot tell a model that declined from a model that ran out of room, and the reading of a null depends on which of the two produced it (my inference from the paper's three failure modes).

The same split shows up with a different kind of reply. In MultiNet v1.0, a benchmark of generalist models across vision, language and robot control, Magma is asked to answer language questions and "often emits the wrong type of output": spatial coordinates where labels were wanted. The authors say this lowers its exact-match score "despite partially relevant content."[^c12][^c13] Explicit format instructions did not remove the pattern: "Magma still produced coordinates in vision-language tasks" after prompting.[^c14] So a reply can be the wrong type while its content is partly right, and a score that rewards only strict shape reads it as wrong. The separate-scores reading is the paper's; that a content-only grader would miss the type error is my inference.

## Limits

- The testbed is arithmetic and competition math with a fixed JSON contract; the authors choose it because ground truth is unambiguous. Transfer to subjective or open-ended tasks is not measured.
- The Magma case rests on the authors' reading of exact match against semantic similarity and on qualitative examples. The slices read give no count of wrong-type outputs, and the similarity measure's definition was not in those slices.
- Scores are zero-shot with "strict output parsing,"[^c15] so a wrong-type reply counts as wrong by construction. A lenient parser would move the Magma number, and the sections read do not report one.
- Baselines other than AloLab are single deterministic runs; only AloLab has five runs and intervals.
- The 0% figures are partly parser strictness (fences, missing fields); a lenient parser would score differently. That is a property of the metric, not of the models' ability.
- CONSTRAINED and REF+CONSTRAINED were run on GSM8K only, and GPT-4o on GSM8K under three strategies only.
- The meta-agent ablation used one target model (Llama 3.1-8B) and one dataset.

## Related

- [[structured-output]] — the four ways of getting a schema-shaped reply; this note measures the gap among them
- [[constrained-decoding]] — the guarantee-by-construction member, with the latency cost reported here
- [[format-restriction-effect]] — the effect of format on task quality, a separate quantity from format validity
- [[requirement-focused-prompt-training]] — another route to requirement compliance through the prompt
- [[exact-match-versus-weighted-agreement]] — another case where a strict count and a graded measure of the same replies diverge; here the strictness is about shape, there about distance

[^c1]: doi-10-48550-arxiv-2605-02363 — "output accuracy: task_accuracy × json_valid. This is the primary metric throughout."
[^c2]: doi-10-48550-arxiv-2605-02363 — "a response that is mathematically correct but structurally invalid cannot be consumed by a downstream system, making it operationally"
[^c3]: doi-10-48550-arxiv-2605-02363 — "confirming that the bottleneck is format, not reasoning."
[^c4]: doi-10-48550-arxiv-2605-02363 — "task accuracy recovered by the fallback parser is 88.4%, but all outputs are unparseable."
[^c5]: doi-10-48550-arxiv-2605-02363 — "the same markdown-fence wrapping observed in Gemma"
[^c6]: doi-10-48550-arxiv-2605-02363 — "followed by a single-epoch breakthrough at epoch 2 as the"
[^c7]: doi-10-48550-arxiv-2605-02363 — "it reaches 84–87% output accuracy on GSM8K and 34–40%"
[^c8]: doi-10-48550-arxiv-2605-02363 — "reduces mean output accuracy to 61.0% and increases"
[^c9]: doi-10-48550-arxiv-2605-02363 — "decoding enforces syntactic validity but incurs 3.6×–8.2× latency overhead"
[^c10]: arxiv-2512-13374 — "The output is identical in form to a calibrated abstention"
[^c11]: arxiv-2512-13374 — "structured-output failure leaves the pipeline with"
[^c12]: arxiv-2512-11315 — "often emits the wrong type of output"
[^c13]: arxiv-2512-11315 — "depressing exact-match despite partially relevant content"
[^c14]: arxiv-2512-11315 — "Magma still produced coordinates in vision-language tasks"
[^c15]: arxiv-2512-11315 — "strict output parsing"
