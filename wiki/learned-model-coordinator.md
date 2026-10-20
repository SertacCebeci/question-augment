---
description: "A small trained coordinator reads its own hidden state and, each turn, picks which LLM of a pool answers and in which role (thinker, worker or verifier), stopping when a verifier accepts."
aliases: ["Trinity coordinator", "tri-role coordination", "multi-LLM coordinator", "test-time model composition via coordination", "learned LLM delegation"]
sources: ["arxiv-2512-04695", "arxiv-2512-04388"]
---
# Learned model coordinator

A small language model placed in front of a pool of larger LLMs can decide who answers without answering the question itself. At each turn it reads its own hidden state through a lightweight head, which gives two sets of logits: one selects an LLM from the pool, the other selects one of three roles for that call.[^c1] The coordinator's own generated text is not used, because "the job of prompting is delegated to the LLMs in the pool."[^c2] A message-processing step injects a role-specific prompt before the request goes out, and the selected model receives "the original query with the full transcript" of earlier turns.[^c3][^c4]

The roles are what separate this from plain routing. Each one is a different contract with the chosen model. The thinker "analyzes the current state and returns meta-level guidance, including high-level plans, decompositions, or critiques of partial solutions."[^c5] The worker acts on the task to make concrete progress. The verifier checks the accumulated solution, and only it can end the run: the run halts "when the verifier is selected and accepts current response as the final answer," and a fixed turn budget ends it otherwise.[^c6] So the stopping rule is a verdict from the system's own verifier role, capped by a count of turns. The paper calls this "a simple, verifiable stopping condition while allowing the coordinator to allocate the compute budget adaptively across" planning, execution and quality control.[^c7]

The trainable part is small. The backbone is a compact model of about 0.6B parameters, but the learned parts, the head and singular-value scales of the backbone's weights, keep "the number of learnable parameters below 20K".[^c8] The paper's bet is that the backbone's internal state already carries the signal the head needs: the hypothesis is a "semantic signal for a lightweight head to coordinate multiple LLMs effectively."[^c9] The read point matters. Taking the representation at the last token instead of the penultimate one gave "severe performance collapse, particularly on LiveCodeBench (more than 10 points drop)."[^c10]

Measured effects, all from the paper's own benchmarks (coding, math, reasoning, domain knowledge): the method "consistently outperforms individual models and existing methods in various tasks."[^c11] Removing the thinker role and then the whole tri-role selection causes "substantial degradation on MATH500 (-6.0 points) and RLPR (-4.57 points)."[^c12] Keeping role selection but sending every query to one fixed agent leaves "performance is significantly undermined."[^c13] With the turn cap raised from 2 to 6, the reported score rises "from 0.823 to 0.863", which the authors read as more than naive routing.[^c14]

## Limits

The benchmarks grade answers, and the coordinator never formulates a question; its roles act on answers the models produce. Whatever carries over to asking is the delegation pattern, not any measured gain in question quality. That transfer is my inference, not something the paper tests.

The upper reference is an oracle. The "PerQuestion-Best" bound is "an upper bound achieved by taking the union of all correct answers," which uses hindsight to pick the right model per question. The paper reports results "close to" that bound on some tasks, not above it.

The verifier's ACCEPT is the model's own judgement. The text reports no measure of how often an accepting verifier is wrong, so whether the stop rule is reliable is open here. My inference is that a verifier from the same pool can share the failure it is checking for.

The authors name their own gap: "is the gap between abstract reasoning and grounded execution, as the system can devise" plans that involve tools without being able to act on them.[^c15] The pool is also fixed in this work.

The optimizer is a separate result. Training is "constrained by cost, since each step requires running the coordinated agents for inference,"[^c16] and the paper prefers an evolution strategy over RL and random search on that basis. Random search "often collapses to unipolar choices, over-selecting a single agent or role."[^c17] That comparison is one paper's; the note does not claim the optimizer matters outside it.

## Related

- [[model-orchestration]] — a hand-made switch between two models at a phase boundary; this note is the learned, per-turn version that the earlier note left open.
- [[role-differentiated-parallel-elicitation]] — fixed role personas answering in parallel for a user; here roles are sequential, and a learned head picks them per turn.
- [[verification-aware-stopping]] — a stop rule tied to verification evidence; the verifier verdict here plays the same stopping role inside a multi-model run.
- [[pre-collapse-intention-state]] — the same kind of read point, a hidden state taken before any output token; there it is applied to intention, here to routing.
- [[natural-language-coordination-plan]] — the opposite choice on prompting: a coordinator whose own text is the subtask instruction given to each worker, trained end-to-end on the final answer. The two notes bound the design question of who writes the prompt.[^c18]

[^c1]: arxiv-2512-04695 — "provides two sets of logits: L logits for selecting an LLM and three logits for assigning its role."
[^c2]: arxiv-2512-04695 — "because the job of prompting is delegated to the LLMs in the pool"
[^c3]: arxiv-2512-04695 — "the original query with the full transcript"
[^c4]: arxiv-2512-04695 — "injects a role-specific prompt before the request is sent"
[^c5]: arxiv-2512-04695 — "The thinker analyzes the current state and returns meta-level guidance, including high-level plans, decompositions, or critiques of partial solutions."
[^c6]: arxiv-2512-04695 — "verifier is selected and accepts current response as the final answer"
[^c7]: arxiv-2512-04695 — "allowing the coordinator to allocate the compute budget adaptively across"
[^c8]: arxiv-2512-04695 — "number of learnable parameters below 20K"
[^c9]: arxiv-2512-04695 — "semantic signal for a lightweight head to coordinate multiple LLMs effectively"
[^c10]: arxiv-2512-04695 — "severe performance collapse, particularly on LiveCodeBench (more than 10 points drop)"
[^c11]: arxiv-2512-04695 — "consistently outperforms individual models and existing methods in various tasks"
[^c12]: arxiv-2512-04695 — "causing substantial degradation on MATH500 (-6.0 points) and RLPR (-4.57 points)"
[^c13]: arxiv-2512-04695 — "only role selection, performance is significantly undermined"
[^c14]: arxiv-2512-04695 — "improving from 0.823 to 0.863 as turns increase from 2 to 6"
[^c15]: arxiv-2512-04695 — "is the gap between abstract reasoning and grounded execution, as the system can devise"
[^c16]: arxiv-2512-04695 — "constrained by cost, since each step requires running the coordinated agents for inference"
[^c17]: arxiv-2512-04695 — "unipolar choices, over-selecting a single agent or role"
[^c18]: arxiv-2512-04388 — "Our model is itself an LLM tasked to output a sequence of workflow steps"
