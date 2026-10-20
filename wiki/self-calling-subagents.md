---
description: "A main agent splits a hard visual question into atomic subtasks run by weight-sharing copies of itself in isolated contexts, so its trace stays language-only and only returned text reaches it."
aliases: ["self-calling chain-of-thought", "sCoT", "virtual replica subagents", "parameter-sharing subagents", "self-invoked atomic subtasks"]
sources: ["arxiv-2512-08511"]
---
# Self-calling subagents

A model can answer a hard question by calling copies of itself. The main agent reads the question, splits it into atomic subtasks such as grounding, captioning or OCR, and sends each one to a subagent. The subagent is not a second model. The paper says subagents "are designed as virtual replicas, which shares exactly the same weights with the main agent."[^s1] A call is an ordinary forward pass: "invoking/calling a subagent simply issues another forward call to the LLM server that runs the main agent."[^s2] Each subagent "processes one cropped image at a time" and returns "a concise textual response to the main agent."[^s3]

The subagent works in a closed context. "each subtask is processed in an isolated context, independent of the main reasoning chain."[^s4] "Subagents operate independently across tool calls, without access to global information or communication with other agents."[^s5] The main chain never sees the subagent's internal reasoning, only its text answer, and aggregates those answers into the final answer. The paper calls the main agent's accumulated trace, its own tokens together with the returned texts, a Self-Calling Chain-of-Thought (sCoT). The point of the name is that the trace is language-only. The image is read only inside a subagent call, and the planner reasons over words: "the reasoning itself is language-only."[^s6]

The authors' stated reason for this design is trainability. Compared with interleaved multimodal chains of thought (iMCoT), the sCoT paradigm "does not require interleaved multimodal reasoning capabilities from the agents," which makes it "much easier to optimize than iMCoT."[^s7]

Training uses GRPO on the main agent's trajectory. The subagent outputs are masked out of the update, "while masking out the textual outputs returned by subagents to avoid reward leakage."[^s8] The authors say this lets the model learn "when to call subagents and how to structure subtasks," without fitting the subagent answers themselves.[^s9]

The reported result: on V* and HR-Bench 4K, the trained model (SubagentVL, built on Qwen2.5-VL-7B) beats the interleaved baseline DeepEyes "by 1.2% and 1.9% on V* benchmark and HR-Bench 4K respectively," and "sCoT achieves better results than Deepeyes with only" about a quarter of its GPU hours.[^s10]

What this may mean for asking and answering is my inference, not a measured result. A question broken into sub-questions, each answered in a narrow context and then aggregated, is a formulation in which the planner needs to hold only short answers. The mechanism concerns how the answer is produced, not what is asked.

## Limits

- Two benchmarks and one base model. The gains are on V* and HR-Bench 4K with Qwen2.5-VL-7B. The paper also says the model is "competitive on 8K" but does not beat the baselines there, "while remaining competitive on 8K." Other base models and tasks are not tested in the text read.[^l1]
- The efficiency comparison is not controlled. The sCoT run used "more constrained training resources" than DeepEyes, but the two systems also differ in batch size, rollouts and data. The "easier to optimize" claim is the authors' attribution across two systems, not a test of language-only against interleaved traces on the same setup.[^l2]
- The gain is attributed to strategy, not perception. Gains on general grounding and OCR are small: "SubagentVL demonstrates only marginal gains in grounding and OCR." The authors read this as "this suggests that the enhanced ability primarily emerges from learning an appropriate subagent-calling strategy," which is their interpretation.[^l3]
- Calls are sequential. "the main agent invokes subagents in a sequential manner," so parallel subagent calls are not tested.[^l4]
- The protocol is fragile. Early training shows "This suggests that the main agent initially prefers" to solve alone. Relaxing the tool-call constraints collapses calling to repeating the user query. The ablations say "carefully curated training data are essential for stable" learning, and "Reason data leads to degraded performance."[^l5]
- The memory benefit is asserted. The text says the design "facilitates saving memory," but the read text gives no memory figure.[^l6]

## Related

- [[tool-integrated-reasoning]] — the code-execution analogue: the trace pauses for an outside tool and resumes on its output. Self-calling keeps the tool inside the model and the trace in text.
- [[hierarchical-context-isolation]] — the same rule that the planner sees only returned results. That work uses separate worker models and a manager layer; here the subagents are the same weights called as functions.
- [[self-ask-decomposition]] — the same move of splitting a question into sub-questions. My reading is that here each sub-question gets a fresh context rather than the running chain.
- [[tool-output-loss-masking]] — the loss-side treatment of returned text. The reason given here is reward leakage, not memorization of deterministic outputs.

[^s1]: arxiv-2512-08511 — "subagents are designed as virtual replicas, which shares exactly the same weights with the main agent"
[^s2]: arxiv-2512-08511 — "invoking/calling a subagent simply issues another forward call to the LLM server that runs the main agent"
[^s3]: arxiv-2512-08511 — "processes one cropped image at a time, and returns a concise textual response to the main agent"
[^s4]: arxiv-2512-08511 — "each subtask is processed in an isolated context, independent of the main reasoning chain"
[^s5]: arxiv-2512-08511 — "Subagents operate independently across tool calls, without access to global information or communication with other agents"
[^s6]: arxiv-2512-08511 — "the reasoning itself is language-only"
[^s7]: arxiv-2512-08511 — "much easier to optimize than iMCoT"
[^s8]: arxiv-2512-08511 — "while masking out the textual outputs returned by subagents to avoid reward leakage"
[^s9]: arxiv-2512-08511 — "when to call subagents and how to structure subtasks"
[^s10]: arxiv-2512-08511 — "sCoT achieves better results than Deepeyes with only"
[^l1]: arxiv-2512-08511 — "while remaining competitive on 8K"
[^l2]: arxiv-2512-08511 — "despite operating under more constrained training resources"
[^l3]: arxiv-2512-08511 — "SubagentVL demonstrates only marginal gains in grounding and OCR"
[^l4]: arxiv-2512-08511 — "the main agent invokes subagents in a sequential manner"
[^l5]: arxiv-2512-08511 — "Reason data leads to degraded performance"
[^l6]: arxiv-2512-08511 — "This design also facilitates saving memory"
