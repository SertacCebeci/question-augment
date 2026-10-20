---
description: "A debate answerer can be weighted by its binary agreement with specialist-tool outputs, averaged over the tools invoked; the weight is a trust signal, not a proven accuracy measure."
aliases: ["tool-aligned agreement score", "expert-agreement score", "agreement with expert tools", "tool agreement score"]
sources: ["arxiv-2512-07132"]
---
# Tool-agreement weighting

A debate or vote over several answering agents needs a way to decide whose answer to trust. One option is to score each agent against an outside reference. In the DART system the reference is the output of specialist vision tools (grounding, object detection, OCR, spatial reasoning). For each answering agent i and each tool output E_j, an agreement scorer LLM produces a binary judgement: "an agreement scorer LLM produces a binary agreement" between the agent's answer and reasoning and that output.[^t1] The agent's score is the mean of these judgements over the tools invoked for the question, so it lies in [0, 1]. The score is then attached to the agent and carried into the discussion and the final aggregation, where the paper says the steps "provide agreement scores such that more trust is placed on agents" that match the tools.[^t2]

The justification is a comparison of perceptual skill. The authors note that specialist models are "stronger than VLMs within their specific skill set," and they state as a hypothesis that "we hypothesize that VLMs whose outputs agree more" with specialist outputs are more likely to be accurate.[^t3][^t4] The step from agreement to accuracy is therefore an assumption the paper makes, not a measured quantity.

The score has an ablation behind it. Keeping the diverse VLM answerers but removing the expert-based agreement "yields a 1.1% performance drop" on A-OKVQA, which the authors read as the experts' calibrated confidence improving the discussion beyond self-reported confidence.[^t5] The score therefore plays a role that stated confidence does not: it is an external check on an answer, not the agent's own report. The authors frame it as "an indicator for whether or not to trust a VLM output."[^t6]

The reference is kept apart from the debaters on purpose: the paper uses "a separate VLM from the debate agents to avoid" bias, since a shared model could push the tool output toward that model's own habits.[^t7]

What the weight is not is a measure of correctness. It says how far an answer matches a reference, and the reference is only as good as its domain. The paper's own substitution test shows this: replacing the specialist tools with one general VLM lowers accuracy by 2.9 points, and the authors comment that "their generality may come at the cost of reliability" on fine-grained visual tasks.[^t8] A weight built on a weaker reference is a weaker weight. That reading is mine; the paper measures the substitution only as a whole-system accuracy change.

## Limits

- The benefit of the weighting rests on one ablation with one number, on one benchmark. The sections read give no per-agent check that a high score predicts a correct answer; the step from agreement to accuracy is the authors' hypothesis.
- Each score is built from binary judgements by an LLM. The paper names its scorer, "We use Qwen2.5 (7B) as the recruitment agent and agreement scorer."[^t9] The sections read do not report how well that scorer agrees with human judgements of agreement.
- The score is averaged over the tools the recruiter chose for that question. Different questions can therefore be scored against different reference sets, so a 0.5 on one question and a 0.5 on another may rest on different evidence. This is my reading of the formula; the authors do not discuss it.
- The medical test (M3D, with one added medical tool) reports an overall gain, but the sections read do not report an ablation of the score on that dataset. Transfer of the weighting to domains without specialist models is untested.

## Related

- [[calibration]] — the property that stated confidence is meant to have; the score is an outside signal to compare with it, not a replacement for it.
- [[tool-type-confidence-dichotomy]] — tools shift stated confidence in opposite directions by type; the agreement score does not use stated confidence, so that mechanism does not directly apply (my inference).
- [[ambiguity-driven-execution-probing]] — the same kind of tool output used as evidence about which candidate holds; here it weights an agent instead of choosing an answer.
- debate-without-new-information — the tool outputs the score is computed from are also the new information the discussion otherwise lacks.

[^t1]: arxiv-2512-07132 — "an agreement scorer LLM produces a binary agreement"
[^t2]: arxiv-2512-07132 — "agreement scores such that more trust is placed on agents"
[^t3]: arxiv-2512-07132 — "stronger than VLMs within their specific skill set"
[^t4]: arxiv-2512-07132 — "we hypothesize that VLMs whose outputs agree more"
[^t5]: arxiv-2512-07132 — "without expert confidence yields a 1.1% performance drop"
[^t6]: arxiv-2512-07132 — "indicator for whether or not to trust a VLM output."
[^t7]: arxiv-2512-07132 — "use a separate VLM from the debate agents to avoid"
[^t8]: arxiv-2512-07132 — "their generality may come at the cost of reliability"
[^t9]: arxiv-2512-07132 — "We use Qwen2.5 (7B) as the recruitment agent and agreement scorer"
