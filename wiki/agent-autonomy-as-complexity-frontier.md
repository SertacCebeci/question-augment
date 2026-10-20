---
description: "Agent autonomy defined as the highest task complexity, counted in workflow steps, at which success rate stays above a threshold; a too-complex task should be decomposed to fit under it."
aliases: ["autonomy level", "task-complexity capability boundary"]
sources: ["arxiv-2603-01203"]
---
# Agent autonomy as a complexity frontier

A single end-task accuracy hides how performance falls as tasks grow. Wang et al. instead place tasks on a complexity scale and read off a frontier.

**Complexity.** Task complexity is "the number and organization of distinct skills and procedural steps required to complete a task". The measure used corresponds mainly to component complexity (Wood 1986), because coordinative and dynamic complexity are hard to estimate from task text.[^c1] Agent trajectories of low-level actions are induced into hierarchical workflows. A step's complexity is the number of most-granular workflow steps beneath it.[^c2] This avoids human completion time, which entangles difficulty with human ability, and raw action counts, which depend on the action space.[^c3]

**Validation.** An LM judged pairs of adjacent-level tasks; the higher level was judged more complex in 82.6% of comparisons, from 10 sampled pairs.[^c4]

**Autonomy.** With success rate SR(k) at complexity level k and target threshold H, autonomy = max{k : SR(k) >= H}: the most complex class an agent finishes end to end with acceptable reliability.[^c5]

**Findings.** Outside computer, business and office domains, most tasks have complexity no greater than 6. Even in software engineering, success drops sharply as complexity rises. Agents do better on self-contained skills (mental processes, work output) than on information input or interacting with others.[^c6] Framework and LM comparisons (OpenHands over SWE-agent, Claude over GPT) hold mainly at medium complexity and may not hold elsewhere.[^c7]

**Use.** Map a user task to its domains and skills, consult the matching curve, and if the task's complexity exceeds the level meeting H, decompose it into simpler subtasks.[^c8] In effect, the size of the question put to an agent should be chosen from its measured frontier.

## Limits

- Complexity is a count of steps from induced workflows, not a ground-truth property. The 82.6% check rests on 10 pairs judged by an LM.
- The frontier depends on the threshold H and on trajectories that happen to be available; few benchmarks allow fair framework comparisons.
- Decomposition advice is shown by one illustrative example, not tested for whether subtask success composes into task success (my observation).
- Coordinative and dynamic complexity are not measured.

## Related

- [[benchmark-labor-market-misalignment]] — the same paper's finding on which work the benchmarks cover at all
- [[evaluation-choices-encode-error-priorities]] — the choice of threshold and metric sets what counts as failure
- [[judge-coverage-overestimation]] — LM-judged validations can overstate agreement

[^c1]: arxiv-2603-01203 — "The number and organization of distinct skills and procedural steps required to complete a task."
[^c2]: arxiv-2603-01203 — "complexity( 𝑣) = | 𝐺 ∩ Desc( 𝑣) |"
[^c3]: arxiv-2603-01203 — "raw agent action counts depend heavily on the specifics of an agent’s action space and execution strategy"
[^c4]: arxiv-2603-01203 — "find that this relative"
[^c5]: arxiv-2603-01203 — "Autonomy = max { 𝑘 | 𝑆𝑅 ( 𝑘) ≥ 𝐻 }"
[^c6]: arxiv-2603-01203 — "success rates drop sharply as task complexity increases"
[^c7]: arxiv-2603-01203 — "However, these trends may"
[^c8]: arxiv-2603-01203 — "recommends decomposing the task (e.g., using an LM) into simpler"
