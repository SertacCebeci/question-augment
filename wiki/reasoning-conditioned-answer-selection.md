---
description: "A second pass chooses the closed-set answer from the model's reasoning trace rather than its stated answer; removing that pass dropped one disaster-VQA system from 77% to 59% accuracy."
aliases: ["reasoning-guided answer selection", "answer selection from reasoning trace", "trace-based answer mapping", "reasoning-based answer selection"]
sources: ["arxiv-2511-19557"]
---
# Reasoning-conditioned answer selection

A chain-of-thought model emits two things: a reasoning trace and a final answer. When the task has a fixed list of allowed answers, the stated answer and the trace do not always agree. The trace can contain the right evidence while the last sentence drifts. The paper names this as a problem, saying that "these intermediate reasoning steps can sometimes be inconsistent with the final answer".[^c8]

The mechanism it proposes is a second stage that treats the trace as the input and an allowed option as the output. The model's reasoning is generated first. A separate query then asks the language model to pick one of the candidate answers "based solely on the intermediate reasoning".[^c1] The stated answer is not the output of this stage. The stage is applied to multiple-choice questions, where the prompt carries a candidate list. Counting questions have no list, so the model's free-form number is kept.[^c10] The authors say the purpose is to "reduce model hallucination and improve the overall reliability of the framework".[^c2]

The effect is measured by removing the stage. "Removing the answer selection mechanism causes a substantial drop in accuracy", from 77% to 59% in the paper's ablation table.[^c3] Removing chain-of-thought prompting instead gave 74%, so in that table the selection stage mattered more than the reasoning prompt.[^c4] A worked example shows the same effect on a single counting question: the model first estimates 8 buildings although its reasoning is correct, and "the reasoning-guided answer selection module corrects this error" to 6.[^c5]

Where it sits. The wiki already holds several neighbours. In [[trigger-gated-constrained-decoding]] the reasoning trace is shared and only the answer extraction differs, which changes accuracy by itself. In [[reasoning-formatting-decoupling]] a second call reformats an answer into a schema. What is new here is the closed candidate list: the second stage chooses among options, so it can override the model's own stated answer. It addresses the trace-versus-output mismatch that [[final-output-gap]] describes as a diagnostic. [[process-outcome-consistency-verification]] addresses the same concern of answers that a derivation does not support, but through a reward, not by building the answer from the derivation.

## Limits

- The ablation is a single table with one accuracy per condition. The passage read reports no variance, run count or significance test, so a 18-point gap is one measurement.
- The selector's prompt includes the generated answer: "The answer that has been generated for the question" appears in it.[^c6] So the decoupling is by instruction, not by withholding the stated answer. Whether the selector is pulled toward that answer was not measured (my reading).
- No alternative extraction method is run on the same traces. The paper says prior work "relies on post-hoc similarity matching",[^c7] but the comparison is not in what was read. The 77% versus 59% contrast is with no selection stage at all, not with another way of selecting.
- Hallucination is inferred from accuracy. No hallucination rate is reported for the stage, so the mechanism is credited from the accuracy effect (my inference).
- Counting remains weak: "Simple Counting and Complex Counting remain the most challenging tasks".[^c9] The stage does not apply to them, so the gain is confined to the multiple-choice share of the benchmark.
- The evidence is one disaster-imagery VQA setting, two UAV datasets and one multimodal backbone family. Whether a trace-based selector helps text-only tasks, or any task with a different candidate structure, is not tested here.

## Related

- [[trigger-gated-constrained-decoding]] — the same trace-then-extract split, measured as a pure extraction effect on free-text answers
- [[reasoning-formatting-decoupling]] — a second call reformats an answer into a schema; here the second call chooses among options
- [[final-output-gap]] — the trace-versus-output mismatch this stage is built to close
- [[process-outcome-consistency-verification]] — the same lucky-answer concern, handled by a reward rather than by construction
- [[demonstration-label-consistency]] — the exemplar side of the same framework

[^c1]: arxiv-2511-19557 — "based solely on the intermediate reasoning"
[^c2]: arxiv-2511-19557 — "This approach helps reduce model hallucination and improves the overall reliability of the framework"
[^c3]: arxiv-2511-19557 — "Removing the answer selection mechanism causes a substantial drop in accuracy"
[^c4]: arxiv-2511-19557 — "disabling CoT prompting results in a decrease in accuracy to 74%"
[^c5]: arxiv-2511-19557 — "the reasoning-guided answer selection module corrects this error"
[^c6]: arxiv-2511-19557 — "The answer that has been generated for the question"
[^c7]: arxiv-2511-19557 — "which relies on post-hoc similarity matching"
[^c8]: arxiv-2511-19557 — "these intermediate reasoning steps can sometimes be inconsistent with the final answer"
[^c9]: arxiv-2511-19557 — "Simple Counting and Complex Counting remain the most challenging tasks"
[^c10]: arxiv-2511-19557 — "For counting-type questions, the prompt differs from the multiple-choice format by omitting the list of candidate answers"
