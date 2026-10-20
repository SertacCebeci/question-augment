---
description: "A coordinator writes its multi-agent plan as natural-language subtasks, worker ids and access lists; reinforcement learning on the final answer trains that text, prompt engineering included."
aliases: ["Conductor output", "natural-language workflow", "language-specified coordination", "RL conductor plan", "subtask-and-access-list plan"]
sources: ["arxiv-2512-04388"]
---
# Natural-language coordination plan

A coordinator can make its output the plan itself. In the Conductor setup a language model emits a sequence of workflow steps. Each step carries a natural-language subtask, the id of the worker assigned to it, and an access list that names which earlier subtask solutions that worker may see; the paper's wording is that each step "specifies a string with a natural-language subtask."[^n1] The three parts are read from the model's response "as three simple Python lists with the same number of entries," and the workers are then prompted in order with their subtask and the context the access list allows.[^n2]

The subtask is free text, so the prompt given to each worker is written by the coordinator, not filled from a template. The authors state the design goal directly: "This design lets the Conductor freely craft tailored subtasks".[^n3] The abstract names the two things this buys: the coordinator learns "to design targeted communication topologies for effective agent-to-agent collaboration, but also to prompt engineer focused instructions to the LLMs to maximally leverage their individual capabilities."[^n4] Prompt engineering and topology design are therefore one output, not two stages.

What trains this text is reinforcement learning on the final answer. The reward "is determined by two progressive conditions": a format condition on whether the three lists parse, and a correctness condition on the final output.[^n5] Nothing in the reward scores the plan separately. The authors report what emerged under that signal: "the emergence of problem breakdowns and prompt-engineered subtasks that match the strengths of each" worker,[^n6] together with "communication strategies that combine independent attempts with final debate rounds."[^n7]

The plan also adapts to difficulty. "As training progresses, the Conductor learns to divide complex LiveCodeBench problems into increasingly granular subtasks" (the authors' Figure 8 contrasts this with MMLU, where workflows stay short).[^n8] Across the controlled comparison the average workflow has "an average of 3 steps, well below the requested limit" of five.[^n9]

The contrast with routing is the point of the construction. Earlier multi-agent methods "essentially train a router classifier to construct agentic workflows by simply selecting models and/or human-designed coordination topologies."[^n10] The Conductor instead uses "natural language as its output medium," which the authors say gives "complete specification freedom."[^n11] In the controlled evaluation it "surpasses all baselines by substantive margins."[^n12]

## Limits

The reward grades only two things, whether the lists parse and whether the final answer is correct, so a plan cannot be judged apart from the workers that carry it out. A plan that a strong worker rescues and a plan that is actually good earn the same credit. The paper's account of why the subtasks are good is a reading of training traces, not a measurement of plan quality. (My inference from the reward definition.)

The headline "unconstrained" table compares against each baseline's "highest recorded performance across our own re-evaluations, private implementation, and online leaderboards, potentially including proprietary, undisclosed prompting and sampling strategies."[^n13] Those numbers are not controlled. The controlled comparison is the one that uses a shared pool: "models with the same set of 7 agents as our Conductor."[^n14]

The 7B-over-3B gain is attributed to prompt engineering. The authors "trace this performance gap to the larger model’s superior prompt engineering skills,"[^n15] from a comparison of two training runs with one recipe. That is one attribution, not an ablation that holds the plan fixed.

The plan is only as strong as its pool. The Conductor "relied on open-source models only in very specific scenarios," given their "inferior performance for most tasks."[^n16] The method works because of "a powerful set of workers";[^n17] with weak workers the same text channel carries weak subtasks, and the paper does not test that regime before its finetuning step.

The plan is also an interface that must parse. A response whose lists cannot be read earns the zero reward, so the output format is a fragile point the method depends on. Whether a different output format would learn as well is not tested here.

The paper measures answer accuracy on reasoning and coding benchmarks. It does not measure whether the subtask text improves the question a user would ask, or whether a plan could be read by a person as a method. Any transfer to question formulation is my inference, not the paper's claim.

## Related

- [[learned-model-coordinator]] — the contrast: that coordinator's own text is discarded because "the job of prompting is delegated to the LLMs in the pool"; here the coordinator's text is the prompt.
- [[model-orchestration]] — a hand-made switch between models at a phase boundary; a natural-language plan is the same boundary, written as subtask instructions chosen per problem.
- [[test-time-scaling]] — the paper's recursive variant lets the coordinator call itself as a further compute axis,[^n18] which is one instance of the general trade of compute for accuracy.
- [[compound-ai-systems]] — the general idea of a system built from several components; a coordination plan is one way of wiring them.

[^n1]: arxiv-2512-04388 — "specifies a string with a natural-language subtask"
[^n2]: arxiv-2512-04388 — "as three simple Python lists with the same number of entries"
[^n3]: arxiv-2512-04388 — "This design lets the Conductor freely craft tailored subtasks"
[^n4]: arxiv-2512-04388 — "to prompt engineer focused instructions to the LLMs to maximally leverage their individual capabilities"
[^n5]: arxiv-2512-04388 — "is determined by two progressive conditions"
[^n6]: arxiv-2512-04388 — "prompt-engineered subtasks that match the strengths of each"
[^n7]: arxiv-2512-04388 — "communication strategies that combine independent attempts with final debate rounds"
[^n8]: arxiv-2512-04388 — "LiveCodeBench problems into increasingly granular subtasks"
[^n9]: arxiv-2512-04388 — "with an average of 3 steps, well below the requested limit"
[^n10]: arxiv-2512-04388 — "essentially train a router classifier to construct agentic workflows"
[^n11]: arxiv-2512-04388 — "by directly using natural language as its output medium"
[^n12]: arxiv-2512-04388 — "The Conductor surpasses all baselines by substantive margins"
[^n13]: arxiv-2512-04388 — "potentially including proprietary, undisclosed prompting and sampling strategies"
[^n14]: arxiv-2512-04388 — "models with the same set of 7 agents as our Conductor"
[^n15]: arxiv-2512-04388 — "we trace this performance gap to the larger model’s superior prompt engineering skills"
[^n16]: arxiv-2512-04388 — "inferior performance for most tasks"
[^n17]: arxiv-2512-04388 — "by relying on a powerful set of workers"
[^n18]: arxiv-2512-04388 — "allowing the Conductor to leverage its own capabilities to complement the"
