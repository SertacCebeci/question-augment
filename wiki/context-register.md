---
description: "Laser keeps a small slot-based register of refined intent, discarded plans and current plan state, updated each step, so the raw search trace does not fill the context window."
aliases: ["slot-based reasoning state", "compact reasoning-state register", "structured context register"]
sources: ["arxiv-2512-20458"]
---
# Context register

A search agent that works over many steps accumulates its own raw trace: retrieved pages, intermediate prose, dead-end attempts. The Laser authors name the cost plainly: "the context window will be filled up quickly as the number of reasoning steps increases, which are prone to redundancy, hallucination, and context drift."[^c1] Their response is a separate store with a fixed shape rather than a longer window. The context register is "a structured, slot-based storage module that persistently records essential reasoning state throughout the reasoning lifecycle."[^c2]

The register has three slots at step t. The first holds the refined intent: "It stores the refined user intent output by the agentic searcher."[^c3] The second is the planning history, the archive of discarded decomposition plans. The third is the current plan state: the active plan, a record of re-executed sub-tasks with their discarded answers, and a tool-call log. Tool outputs do not enter the register raw. A separate document-extraction action condenses them first: "By condensing retrieved information, this action mitigates uncontrolled context growth from long retrieved documents."[^c4]

Two design features matter for the mechanism. The register is initialised from the output of the planning stage and then rewritten after each action, and the paper says that "updating the context register requires no additional LLM inference".[^c5] Because the actions are a parsable format, the update is done by code, not by another model call. The state passed to the next step therefore has named, bounded content instead of whatever prose the last step happened to produce. The planning history slot also has a job of its own: it records plans already ruled out, which is what lets the agent avoid "re-entering previously invalid planning states" (see [[plan-level-retrospection]]).

What was measured is an ablation. Removing the register entirely (the "w/o Register" variant) gave, in the authors' words, "the substantial degradation in the last row of Figure 3 confirms its importance."[^c6] The register is credited with the effect because it "filters noise, preserves only essential state variables, and prevents the context window from being overwhelmed."[^c6] The paper also reports "the significant reduction in context-token usage achieved by Laser."[^c7] The experiments are on Qwen2.5 and Qwen3 models over "challenging multi-hop QA datasets".[^c8] The figure values behind the drops are not in the text read for this note, so the size of the effect is not given here.

The register sits alongside the retrieve-and-reason loop described in [[retrieval-reasoning-procedure]]: that note asks which choices (plan, index, next step, stop) a system makes over time, and the register is one concrete place where those choices are stored. It also gives a concrete form to the idea of writing the intent down before acting, which [[latent-intent-before-answer]] treats as a latent variable.

## Limits

- The only test of the register is removing it. There is no comparison with a raw trace under the same token budget, nor with an LLM-written summary as the memory. Those comparisons would show whether the gain comes from the typed slots or from merely keeping less text.
- The slots are specified by hand for this action protocol. Whether the same slots suit other tasks, such as open-ended questions with no checkable sub-answers, is not tested. (My inference: a slot like "discarded answers" presupposes that a sub-answer can be judged wrong.)
- A fixed store can drop a fact that was not classed as essential when it was written. The paper's claim that the register "filters noise" is an assertion supported only by the aggregate ablation, not by a measure of what was lost.
- The result is on search QA with small open models. It says nothing about human askers keeping their own notes.
- Compare [[compressed-memory-versus-raw-retrieval]], where raw records beat an agentic memory that compresses them into facts about a user. That is a different kind of compression (facts about a person, not typed reasoning state), so the two results do not decide each other. (My inference.)

## Related

- [[plan-level-retrospection]] — the planning-history slot exists so that the retrospection actions can discard a plan and not return to it
- [[retrieval-reasoning-procedure]] — the retrieve-reason loop whose state this register holds
- [[latent-intent-before-answer]] — the refined-intent slot is an instance of writing the intent out before the answer
- [[compressed-memory-versus-raw-retrieval]] — the opposing result for personal behaviour logs, where compression lost to raw records
- [[verified-lemma-memory]] — a math agent's bounded memory of verified sub-results rather than typed search state (my inference: both answer the same context-window limit, by different stores)

[^c1]: arxiv-2512-20458 — "the context window will be filled up quickly as the number of reasoning steps increases, which are prone to redundancy, hallucination, and context drift."
[^c2]: arxiv-2512-20458 — "a structured, slot-based storage module that persistently records essential reasoning state throughout the reasoning lifecycle."
[^c3]: arxiv-2512-20458 — "It stores the refined user intent output by the agentic searcher."
[^c4]: arxiv-2512-20458 — "By condensing retrieved information, this action mitigates uncontrolled context growth from long retrieved documents."
[^c5]: arxiv-2512-20458 — "updating the context register requires no additional LLM inference"
[^c6]: arxiv-2512-20458 — "The context register filters noise, preserves only essential state variables, and prevents the context window from being overwhelmed"
[^c7]: arxiv-2512-20458 — "the significant reduction in context-token usage achieved by Laser"
[^c8]: arxiv-2512-20458 — "Experiments on Qwen2.5/3-series models across challenging multi-hop QA datasets"
