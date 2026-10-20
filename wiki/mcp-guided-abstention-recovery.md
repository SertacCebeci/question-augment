---
description: "Routes a code model's deferred prediction to one of three tool-based recovery actions chosen by the diagnosed cause of its uncertainty, instead of treating abstention as a terminal state."
aliases: ["MCP-guided abstention recovery", "cause-routed deferral recovery"]
sources: ["rathnasuriya-2026"]
---
# MCP-guided abstention recovery

> [[abstention|Abstention]] stops at "I don't know." This design asks *why*
> the model doesn't know, and picks the next answerer accordingly.

## Definition / Mechanism

Rathnasuriya & Yang (2026) propose a deployment
pipeline for code language models where a calibrated correctness score is
compared to a tunable threshold, and a below-threshold input is abstained
but not dropped: "Once a calibrated correctness score is available, the
system enforces a policy such that, if the score exceeds a tunable
threshold, the prediction is accepted; otherwise, the input is abstained.
However, abstention is not terminal. The system activates [[recovery-postulate|recovery]] modules
based on the nature of the input and task."[^c1]

For generative tasks a model–context–protocol (MCP) layer routes the
abstained case to one of three actions keyed to a diagnosed failure mode.
Missing task information triggers reasoning and decoding diversification:
"the MCP layer augments the input. It may invoke model reasoning
strategies to generate intermediate plans or sketches that clarify
intent... decoding is diversified, and candidates are re-ranked based on
follow-up uncertainty estimation." Missing external knowledge triggers
evidence injection: "the system injects contextual information, such as
documentation snippets or relevant specifications... lightweight
analyzers or compilers may be invoked to validate outputs. These tools
convert knowledge uncertainty into evidence the model can act on." A
capability gap triggers task simplification and, failing that, a final
refusal: "the MCP system enforces simplifications... If uncertainty
remains high after such interventions, the system abstains definitively,
ensuring correctness is never sacrificed for coverage."[^c2]

For classification tasks the recovery route is symbolic rather than
generative: "Static analyzers, program slicing tools, or rule-based
validators are applied to the input... classification decisions are
always supported by either model confidence or symbolic evidence."[^c3]

## Why it matters

On stall 4, this makes the *next* answerer conditional on the cause of the
first answerer's uncertainty rather than fixed in advance: a prompt gap
gets model reasoning, a knowledge gap gets a document or a compiler, a
competence gap gets task decomposition and, only then, a terminal refusal.
On stall 10, it turns "how much to commit, and how to say the rest" into a
branch instead of a single threshold cut: what the answerer says when it
does not commit is itself a dispatch decision, not silence.[^c4]

## Transfer

| | |
|---|---|
| In its home field | MCP tool invocation as a way to give an LLM live external context during generation |
| Here | triggered specifically by a below-threshold abstention decision, and the tool chosen is selected by which of three named failure modes produced the uncertainty |
| What survives | the call structure — converting an unresolved question into a tool query that returns evidence the model can condition on — and the principle that a refusal can carry a cause label that routes it |
| What does not | any guarantee that the routed tool actually resolves the uncertainty; the three-mode taxonomy and its dispatch rule are the paper's proposed design (§2, "Our Envision"), not something the reported experiments (§4) measure |

[^c5]

## Limits

- The recovery mechanism itself is unimplemented and unmeasured in this
  source. The paper's own roadmap places MCP-module construction in future
  work — "we will implement concrete MCP modules for both model types" —
  and the reported numbers (Tables 1–2) test only the [[calibration]] step
  that feeds the threshold, not the routing-and-repair loop this note
  describes. Everything above is a proposed design, not a validated
  method.[^c6]
- Only the calibration inputs to the threshold are measured, and on a
  narrow slice: two models per table (DeepSeek-Coder-7B paired with either
  CodeLlama-7B or Qwen-Coder-7B) on one benchmark each (MBPP+; a defect
  prediction set), with no ablation isolating any one recovery branch's
  effect on final accuracy.
- The three-way failure-mode taxonomy (missing prompt information /
  missing external knowledge / capability gap) is asserted, not derived
  from a diagnostic procedure; the paper does not say how the system
  determines which of the three applies to a given abstained case.

## Related

[[abstention]] · [[learned-deferral]] · [[calibration]] · [[defect-localization]]

[^c1]: rathnasuriya-2026 — "Once a calibrated correctness score is available, the system enforces a policy such that, if the score exceeds a tunable threshold, the prediction is accepted; otherwise, the input is abstained. However, abstention is not terminal. The system activates recovery modules based on the nature of the input and task."
[^c2]: rathnasuriya-2026 — "the MCP layer augments the input. It may invoke model reasoning strategies to generate intermediate plans or sketches that clarify intent"
[^c3]: rathnasuriya-2026
[^c4]: rathnasuriya-2026 — "This work reframes abstention as a principled decision-making mechanism rather than a fixed thresholding heuristic in future code intelligence systems."
[^c5]: rathnasuriya-2026 — "We propose a structured framework for deploying code intelligence systems that unifies model uncertainty, selective abstention, and tool-informed recovery into a single decision process"
[^c6]: rathnasuriya-2026 — "we will integrate constraint-based decoding, prompt augmentation, and lightweight synthesis validators. These milestones are planned for completion within a 12 month timeframe"
