---
description: "A reward model that calls tools (crop, page retrieval, constraint checks) and scores only after the observations return, so its judgment follows evidence it fetched, not surface fluency."
aliases: ["ARM-Thinker", "agentic reward model", "agentic reasoning reward model", "think-act-verify reward model", "tool-using generative reward model"]
sources: ["arxiv-2512-05111"]
---
# Agentic reward model

A reward model usually scores a response in one pass: it reads the question and the candidate and emits a number or a verdict, with no way to look anything up. The agentic reward model lets the judge act before it scores. It writes a thought, calls a tool, reads what the tool returns, and only then issues its judgment. The paper states the contrast in one sentence: "Unlike traditional reward models that passively score responses, ARM-Thinker operates as an active agent: it dynamically invokes tools to gather evidence, refine understanding, and verify outputs before producing judgments."[^c1]

The motivation is that the score should follow what the judge can check. The authors put it as "judgments should be conditional on accessible evidence, not just surface fluency."[^c2] The failure they name is "rewarding fluent but unsupported answers, under-rewarding concise evidence-backed responses"[^c3], and they attribute the generative judge's version of it to operating "in a single pass without tools, leading to hallucinated rationales."[^c4]

## Mechanism

The trajectory is a sequence of think–act–observe cycles. Each step is either a tool call or a final answer, and a tool result (text or image) goes back into the context before the next step. The judge also keeps a small indexed memory: a "texts map (e.g., resp 1, resp 2) for candidate responses to compare" and an imgs map for images and crops, so a later step can refer to a specific artifact.[^c5] Three tool families are used: 19 text validators "that verify compliance with linguistic or structural constraints", implemented on the checking schema of MM-IFEngine[^c6][^c7], image crop and zoom-in, and document page retrieval by query or by index.

Training is staged. A supervised cold start is needed because "VLMs typically exhibit limited zero-shot competence in executing novel tool invocations."[^c8] Then comes two-stage GRPO. The first stage rewards format and a bonus for a reasonable attempt at a tool call, to "encourage the model to actively explore tool usage."[^c9] The second stage keeps the correctness reward and adds credit "when tool usage directly contributes to a correct prediction."[^c10] That second-stage credit is gated on the final answer; the text I read does not define what counts as a "successful" tool call. Preference pairs are built from a ground-truth response, with GPT-4o-mini writing "semantically related but flawed responses" as the negatives.[^c11]

The case for the design rests on a gap the authors see in existing judges. Prior multimodal reward models, they say, "have not yet provided RM with the ability to call tools," and they attribute this to tasks that were too easy to need tools: "current tasks are relatively easy and have simple outputs."[^c12][^c13] In the ablation, the Qwen2.5-VL-7B base "rarely invokes tools without explicit supervision"[^c14], while the trained model "is competitive even without tools (comparable to Qwen2.5-VL-7B)" and improves further when tools are on.[^c15]

The reported gains are that the method "improves average accuracy by +16.2%" on reward-modeling benchmarks, with smaller gains on tool-use and general reasoning benchmarks. The 7B model is described as "competitive with, and in some cases superior to, proprietary models like GPT-4o on reward-modeling and tool-use benchmarks."[^c16]

What survives the move to other judging problems, in my reading: the verdict comes after an observation step, so each claim can be tied to a retrieved page or a cropped region rather than to the response's own wording. What does not come for free is the tool inventory. Each tool is a fixed operation someone chose, and the judge's agency is choice among them.

## Limits

- The headline averages mix public benchmarks with one the authors wrote: "we develop ARMBench-VL (Fig. 1(b)), a new benchmark focused on verifiable multi-step reasoning."[^c17] A gain on a benchmark built to reward evidence chains is not an independent measure of judging quality.
- I read the method and the ablations, not the main results tables in the middle of the paper, so the numbers above are the authors' summary sentences and were not checked against tables.
- Faithfulness is asserted, not measured, in the parts I read: the interface is said to "improve faithfulness."[^c18] I found no metric that tests whether a rationale matches its tool output. (my reading)
- The text validators check constraint types from one prior schema.[^c7] A constraint outside those types gets no check, so the judge is agentic only over the checks someone wrote. (my inference)
- The negatives are flawed versions of a reference response, so the training signal rewards agreement with that reference. Whether a tool-verified judge is harder for a policy to exploit is not tested in the parts I read.
- The cost of a multi-turn judge, one rollout per judgment instead of one pass, is not reported in the parts I read.
- One backbone (Qwen2.5-VL-7B) and one pipeline. Extension to a broader set of tools is listed as future work: "In the future, we plan to extend our method to a broader set of tools."[^c19]

## Related

- [[benefit-scaled-tool-reward]] — how a tool call is priced in the reward once a model can call tools; ARM-Thinker's tool term is gated on the final answer, not on a paired with-and-without contrast.
- [[competence-aware-credit-assignment]] — segment-level credit for when a tool call helps; ARM's credit is attached to the final answer.
- [[verifiability-routed-criterion-reward]] — routes checkable criteria to a deterministic verifier and the rest to a judge; ARM's text validators are the deterministic side, placed inside an agent loop.
- [[tool-integrated-reasoning]] — the same call-and-resume pattern, used by an answerer for computation rather than by a judge for evidence.
- [[crop-label-consistency-reward]] — a process reward that scores a zoom-in crop against the model's own label; I did not find an equivalent crop-level term in the parts of ARM-Thinker I read.

[^c1]: arxiv-2512-05111 — "Unlike traditional reward models that passively score responses, ARM-Thinker operates as an active agent: it dynamically invokes tools to gather evidence, refine understanding, and verify outputs before producing judgments."
[^c2]: arxiv-2512-05111 — "judgments should be conditional on accessible evidence, not just surface fluency"
[^c3]: arxiv-2512-05111 — "rewarding fluent but unsupported answers, under-rewarding concise evidence-backed responses"
[^c4]: arxiv-2512-05111 — "Generative reward models typically operate in a single pass without tools, leading to hallucinated rationales"
[^c5]: arxiv-2512-05111 — "texts map (e.g., resp 1, resp 2) for candidate responses to compare"
[^c6]: arxiv-2512-05111 — "A collection of 19 textual validators that verify compliance with linguistic or structural constraints"
[^c7]: arxiv-2512-05111 — "implemented following the checking schema of MM-IFEngine"
[^c8]: arxiv-2512-05111 — "VLMs typically exhibit limited zero-shot competence in executing novel tool invocations"
[^c9]: arxiv-2512-05111 — "In the early phase, the objective is to encourage the model to actively explore tool usage."
[^c10]: arxiv-2512-05111 — "Rsucc assigns additional credit when tool usage directly contributes to a correct prediction"
[^c11]: arxiv-2512-05111 — "we use GPT-4o-mini to generate semantically related but flawed responses"
[^c12]: arxiv-2512-05111 — "these works have not yet provided RM with the ability to call tools"
[^c13]: arxiv-2512-05111 — "current tasks are relatively easy and have simple outputs"
[^c14]: arxiv-2512-05111 — "rarely invokes tools without explicit supervision"
[^c15]: arxiv-2512-05111 — "ARM-Thinker-7B is competitive even without tools (comparable to Qwen2.5-VL-7B)"
[^c16]: arxiv-2512-05111 — "competitive with, and in some cases superior to, proprietary models like GPT-4o on reward-modeling and tool-use benchmarks"
[^c17]: arxiv-2512-05111 — "we develop ARMBench-VL (Fig. 1(b)), a new benchmark focused on verifiable multi-step reasoning"
[^c18]: arxiv-2512-05111 — "and improve faithfulness"
[^c19]: arxiv-2512-05111 — "In the future, we plan to extend our method to a broader set of tools"
