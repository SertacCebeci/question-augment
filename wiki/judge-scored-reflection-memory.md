---
description: "A reflection written after a judged attempt is scored by the judge, only the best accepted one is kept as memory, and the same weights are trained on the scores as an auxiliary RL signal."
aliases: ["reflection meta-policy", "rubric bank", "judged-experience reflection", "reflection as memory and RL signal"]
sources: ["doi-10-48550-arxiv-2605-10899"]
---
# Judge-scored reflection memory

Learning from a finished attempt usually takes one of two routes. The outcome updates the weights, or a note is kept for the next attempt. The work joins the two in one loop. After a task rollout is judged, the same backbone that acts is prompted to write several reflection candidates for the query and the trajectory, with the trajectory held fixed: the update runs "treating the trajectory as fixed context and backpropagating only through reflection tokens."[^c1] A separate judge scores every candidate. "A privileged LLM judge scores every candidate using the original question" together with the raw trajectory, the stagewise rubric scores and the justifications the task judging produced.[^c2]

Two things follow from the scores. All candidate scores are reward for the reflection tokens, so the shared parameters change. And only the highest-scored accepted reflection is written, as natural-language text, into a rubric bank.[^c3] The bank items are not the planning rubrics of the task policy. They are retrospective: "the prospective rubrics generated during planning, bank items encode outcome-aware lessons."[^c4] The method section puts the pair this way: the agent gets "both parametric RL updates and textual memory updates."[^c5]

Retrieval from the bank has two modes. Within-episode refinement retrieves a query's own earlier reflection when the same question is tried again. Cross-episode transfer "retrieves reflections from related past questions."[^c6] The reflection branch runs one RL step behind the task rollouts: "We instead allow the reflection branch to lag by one RL step."[^c11] The point is that the reflection work does not block the next rollout.

The measured effects are two. In the 600-step ablation, the Meta-Policy arm, which keeps answer-only GRPO and adds reflection training and bank retrieval, improves over the baseline.[^c7] In the caption of the inference-time figure, "the learned meta-policy" enables cross-episode transfer and within-episode refinement, "while Baseline-RL does not benefit from the same reuse."[^c8] The second result is the one that separates memory from training: the same bank does not help the baseline.

## Limits

- The two effects are not separated in the ablation. The Meta-Policy arm bundles "reflection meta-policy training and rubric-bank retrieval" in one arm.[^c9] The reading I did does not say whether the gain comes from the weight update on reflection tokens, from the retrieved text, or from both. My inference is that the bank effect and the auxiliary-gradient effect need separate arms to be told apart.
- The reflection branch is judged by the same kind of judge that scores the task, and the judge sees the trajectory and its justifications. The reflections are therefore optimized toward that judge's view of what mattered. Whether a reflection helps an agent that cannot see the judge is the claim of cross-episode transfer, and in the sections I read it rests on one caption, not on reported numbers.
- The acceptance rule that decides which candidate may enter the bank is not described in the parts I read. That rule sets what the memory can contain.
- Each bank item comes from one trial. A reflection that credits a lucky outcome, or blames a judged-wrong one, is stored with the same standing as the rest. The work does not test this failure.
- The asynchronous branch can fall further behind than one step when training is interrupted; the paper says so for its own run.[^c10]

## Related

- [[stagewise-judged-credit]] — the stage judge whose scores supply the training signal for the attempt that gets reflected on
- [[mistake-distillation-to-single-shot-probe]] — also turns judged failures into reusable items, but into benchmark probes rather than the agent's own memory
- [[reflection-shaped-tree-backup]] — reflection entering training as a reward-shaping device in tree search, a different place where a reflective signal is used

[^c1]: doi-10-48550-arxiv-2605-10899 — "treating the trajectory as fixed context and backpropagating only through reflection tokens"
[^c2]: doi-10-48550-arxiv-2605-10899 — "A privileged LLM judge scores every candidate using the original question"
[^c3]: doi-10-48550-arxiv-2605-10899 — "the highest-scored accepted reflection is also written into an agent rubric bank as natural-language"
[^c4]: doi-10-48550-arxiv-2605-10899 — "the prospective rubrics generated during planning, bank items encode outcome-aware lessons"
[^c5]: doi-10-48550-arxiv-2605-10899 — "giving the agent both parametric RL updates and textual memory updates"
[^c6]: doi-10-48550-arxiv-2605-10899 — "retrieves reflections from related past questions"
[^c7]: doi-10-48550-arxiv-2605-10899 — "both SS-GRPO and Meta-Policy improve over Baseline-RL"
[^c8]: doi-10-48550-arxiv-2605-10899 — "while Baseline-RL does not benefit from the same reuse"
[^c9]: doi-10-48550-arxiv-2605-10899 — "adds reflection meta-policy training and rubric-bank retrieval"
[^c10]: doi-10-48550-arxiv-2605-10899 — "can introduce additional staleness in the asynchronous reflection branch"
[^c11]: doi-10-48550-arxiv-2605-10899 — "We instead allow the reflection branch to lag by one RL step"
