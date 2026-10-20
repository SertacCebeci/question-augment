---
description: "A rubric written at each decision step from the partial trajectory, injected before the next action and checked after it, steers a search agent rather than scoring its finished report."
aliases: ["step-level rubric", "rubric as action guidance", "prescriptive rubric", "inject-verify-retry rubric", "trajectory-conditioned rubric"]
sources: ["doi-10-48550-arxiv-2605-23590"]
---
# Step-level rubric guidance

Rubrics are usually written after an output exists, as a checklist that grades it. The Co-ReAct paper turns them around. Before each tool call a rubric is written for that step and placed in the agent's context, so it constrains what the next action should do rather than how much credit a finished answer earns. The paper's diagnosis is that existing uses are "mostly evaluative rather than action-guiding"[^s1]. Evaluative rubrics answer "how much credit does an output already produced deserve"[^s2], while a search agent during inference needs an answer to "what concrete requirements should the next action satisfy"[^s3].

The paper names three properties the rubric must have. It must be step-level: "it should specify what the next action should cover"[^s4]. It must be conditioned on the trajectory: "it must be conditioned on the current partial trajectory"[^s5]. And it must be discriminative, so that the actions it favours are better than the ones it penalises. The third is the one the authors treat as decisive: untrained rubrics can "actively mislead the search" when injected[^s9].

The mechanism is a loop. "Before each tool call, a trajectory-conditioned" rubric is injected into the agent's context[^s6]. After the action is proposed and before it runs, "an independent verifier checks the proposed action against the rubric"[^s7]. If the check fails, "the verifier returns feedback on which criteria remain" unmet, and the agent regenerates the action[^s8]. The rubric is therefore used twice in one step: first as a target, then as a test of the proposed action.

What was measured. On DeepResearchBench and SQA-CS-V2, with 8B and 14B open-source search agents, "Co-ReAct consistently improves over ReAct and" the test-time compute baselines reported in the paper[^s12]. Replacing the trained rubric generator with an untrained base model "hurts performance below even ReAct"[^s10], which is the ablation that carries the claim that rubric quality, not the mere presence of a rubric, does the work. Verification has a measured effect too: "the verification step catches 21.4% of tool calls that fail rubric" criteria, and removing it lowers the global average[^s11]. With a prompt-only variant on a closed model, "Co-ReAct reaches 37.13 Overall RACE, improving over ReAct by 4.44%"[^s13]. That variant is one where Gemini is "prompted to generate step-level rubrics and verification feedback without GRPO"[^s17].

## Limits

- The gain is measured on a fixed search policy. The paper says it "sits on top of a fixed search policy"[^s14] and does not benchmark against end-to-end trained search agents such as Search-R1[^s15]. Whether the rubric still helps a policy that was itself trained with RL is untested; the paper leaves it to future work[^s16].
- The benchmarks are research-report tasks (DeepResearchBench, SQA-CS-V2). Nothing in the slices I read tests a question-asking agent, a non-search tool setting, or a domain outside these two.
- Cost is not in the parts I read. My inference from the pipeline is that each step adds a rubric call, one evaluator call per candidate, and a verifier call, plus retries; the size of that overhead is not established here.
- The rubric is judged against a consensus of LLM judges, not against human experts or outcomes. A rubric can discriminate well by the consensus and still point the agent the wrong way. (my inference)
- The reading gives point estimates from single runs; I did not see variance across seeds in the slices read.

## Related

- [[listwise-rank-correlation-rubric-reward]] — how the rubric generator is trained, so that its criteria order a slate of candidate actions the way the expert consensus does
- [[rubric-first-planning-scaffold]] — a rubric written once per run at planning, as the structure of the run; here the rubric is rewritten at every step
- [[rubric-aware-on-policy-self-distillation]] — a rubric as a teacher's steering signal during training, not an in-context action guide at inference
- [[preference-consistency-rubric-reward]] — a rubric generator rewarded on report-level preference pairs, the reward that the listwise version replaces
- [[generate-then-verify-candidate-pipeline]] — the same generate, then filter shape, here with a rubric as the filter

[^s1]: doi-10-48550-arxiv-2605-23590 — "mostly evaluative rather than action-guiding"
[^s2]: doi-10-48550-arxiv-2605-23590 — "how much credit does an output already produced deserve"
[^s3]: doi-10-48550-arxiv-2605-23590 — "what concrete requirements should the next action satisfy"
[^s4]: doi-10-48550-arxiv-2605-23590 — "it should specify what the next action should cover"
[^s5]: doi-10-48550-arxiv-2605-23590 — "it must be conditioned on the current partial trajectory"
[^s6]: doi-10-48550-arxiv-2605-23590 — "Before each tool call, a trajectory-conditioned"
[^s7]: doi-10-48550-arxiv-2605-23590 — "an independent verifier checks the proposed action against the rubric"
[^s8]: doi-10-48550-arxiv-2605-23590 — "the verifier returns feedback on which criteria remain"
[^s9]: doi-10-48550-arxiv-2605-23590 — "untrained rubrics can actively mislead the search"
[^s10]: doi-10-48550-arxiv-2605-23590 — "replacing the RL-trained generator with an untrained base model hurts performance below even ReAct"
[^s11]: doi-10-48550-arxiv-2605-23590 — "the verification step catches 21.4% of tool calls that fail rubric"
[^s12]: doi-10-48550-arxiv-2605-23590 — "Co-ReAct consistently improves over ReAct and"
[^s13]: doi-10-48550-arxiv-2605-23590 — "Co-ReAct reaches 37.13 Overall RACE, improving over ReAct by 4.44%"
[^s14]: doi-10-48550-arxiv-2605-23590 — "Co-ReAct is a ReAct-paradigm enhancement: it sits on top of a fixed search policy"
[^s15]: doi-10-48550-arxiv-2605-23590 — "do not benchmark against end-to-end RL-trained search agents such as Search-R1"
[^s16]: doi-10-48550-arxiv-2605-23590 — "stacking our rubric on top of a trained search agent is out of scope here"
[^s17]: doi-10-48550-arxiv-2605-23590 — "is prompted to generate step-level rubrics and verification feedback without GRPO"
