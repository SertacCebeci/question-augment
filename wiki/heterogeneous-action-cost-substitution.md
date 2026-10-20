---
description: "A single scalar reward that sums the costs of different kinds of action (movement, asking, memory lookup) lets a learned policy substitute cheap internal recall for expensive physical search."
aliases: ["heterogeneous cost substitution", "cost-aware action substitution", "memory-for-movement substitution"]
sources: ["arxiv-2512-18571"]
---
# Heterogeneous action cost and substitution

An embodied agent has actions that differ in kind of cost. Moving through a room spends time and energy, asking a person spends attention, and looking something up in its own memory costs almost nothing. ESearch-R1 places these in one action space (Navigate, Ask, GetMemory, Found) and assigns each a price. The ordering is explicit: "internal recall is cheap while physical movement is expensive."[^c1] Navigation is charged by the distance travelled, dialogue by a base price that rises with each question (see [[question-fatigue-cost]]), and memory retrieval by a small fixed price. The trajectory return is task reward minus a weighted sum over all these costs, so an action of any kind is judged on one scale.

The mechanism is substitution. Because the sum treats a memory lookup and a stretch of movement as the same currency, a trajectory that finds the target by checking memory first ends with a higher return than one that walks to each candidate. A policy trained on such returns, with the group-relative update described in [[group-relative-advantage]], shifts probability toward the cheap action. The paper states the aim as a policy that can "substitute expensive physical exploration with low-cost cognitive retrieval,"[^c2] and reports the measured shift: compared with its supervised starting point, the trained policy uses GetMemory more and does so while "reducing its reliance on high-cost Navigate actions."[^c3]

The evidence that the substitution carries the performance is an ablation. Removing the memory action drops the success rate from 61.5% to 52.0%, and the authors read the loss as the agent being "forced into redundant physical exploration to reverify information it has already seen."[^c4] Removing dialogue is worse: the ablation "causes the SR to plummet to just 10.5%".[^c5] So the two cheap-to-moderate channels do different work. Memory replaces exploration that has already been done; dialogue narrows a candidate set that memory cannot narrow. The sensitivity analysis varies navigation price, dialogue price and the fatigue factor, and reports that the framework "adapts its strategy and consistently identifies more cost-efficient solutions than the baselines."[^c6]

The pattern is not specific to robots. Any agent that can either consult a store it already holds or take an expensive external step faces the same pricing question. A single reward that sums both is the simplest way to let one learned policy choose between them. Whether that choice is the right one depends on the prices, and here the authors set them.

## Limits

- The prices are the authors' choice. Navigation is 1.0, the dialogue base is 0.5 and memory is "cmem = 0.01 (memory retrieval)".[^c7] The memory price is the one that makes substitution pay, and by my reading of the text the list of parameters varied in the sensitivity analysis is navigation, dialogue and the fatigue factor, not memory. The result is least tested where it matters most.
- A cheap action is a substitute only when it is right. In the simulator the memory is written from the agent's own observations of the scene, so the lookup is reliable by construction. Stale or misleading memory is not modelled, so the paper does not show that a cheap lookup stays worth its price when it is wrong. This is my inference from the setup.
- Everything runs in AI2-THOR with a simulated user. The human cost of asking is a modelled number, not a measured one, and the reported costs are simulator units.
- The headline gain is smaller than the abstract suggests. The roughly 50% cost reduction is measured against Qwen2.5-VL-32B, whose average Total Task Cost is 3.3 in Table I. Against ReAct with Gemini-2.5-Pro, whose average is 2.5, the reduction is about 36% by my arithmetic. The success-rate margin over the 32B baseline is 61.5 ± 1.6 against 60.0 ± 2.3 averaged over distractor counts, which lies well inside the reported spreads.
- One exchange rate between success and cost (λ = 1.0) is used throughout. The paper varies the ratios of the cost terms, not the trade-off weight, so it does not show the substitution under a different valuation of success against cost.

## Related

- [[cost-priced-joint-selection-and-stopping]] — prices each candidate question by expected entropy reduction minus cost; the same pricing idea applied to one action type rather than across kinds
- [[voi-per-cost-modality-selection]] — picks among modalities by gain per unit cost, a per-action rule where this note's policy learns the choice
- [[cost-ordered-perception-pyramid]] — a fixed cheap-first order; the substitution here is learned rather than imposed
- [[value-of-information]] — the decision-theoretic yardstick for whether a cheap look is worth its price
- [[question-fatigue-cost]] — the one price in this action space that rises with use
- [[group-relative-advantage]] — the critic-free update that ranks trajectories by summed cost within a group

[^c1]: arxiv-2512-18571 — "internal recall is cheap while physical movement is expensive"
[^c2]: arxiv-2512-18571 — "substitute expensive physical exploration with low-cost cognitive retrieval"
[^c3]: arxiv-2512-18571 — "reducing its reliance on high-cost Navigate actions"
[^c4]: arxiv-2512-18571 — "agent is forced into redundant physical exploration to reverify information it has already seen"
[^c5]: arxiv-2512-18571 — "action causes the SR to plummet to just 10.5%"
[^c6]: arxiv-2512-18571 — "framework adapts its strategy and consistently identifies more"
[^c7]: arxiv-2512-18571 — "cmem = 0.01 (memory retrieval)"
