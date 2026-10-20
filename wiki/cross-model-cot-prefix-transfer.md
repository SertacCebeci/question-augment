---
description: "A reasoning trace passed to another model helps by different routes: answer leakage (AIME), receiver competence (MMLU-Pro), partial structured answers (ZebraLogic), or scaffolding."
aliases: ["provider-receiver CoT transfer", "prefix-based reasoning transfer", "answer leakage in chain-of-thought"]
sources: ["doi-10-48550-arxiv-2605-28913"]
---
# Cross-model CoT prefix transfer

Cheng et al. pass a reasoning trace from a provider model to a receiver model that solves the same problem. They do not stop at the finished trace. They feed the receiver cumulative prefixes of it, so they can see when transfer begins.[^c1] Two modes are compared. In force-answer mode the receiver must answer straight from the prefix, which isolates what can be extracted from the text. In free-generation mode it may keep reasoning first, which tests whether a partial prefix scaffolds the receiver's own reasoning.[^c2]

## What was measured

- Answer leakage is defined as the earliest prefix step at which the provider trace explicitly states the correct final answer.[^c3]
- AIME, force-answer: among runs where the receiver becomes correct, 94.5% of first-correct steps fall at or after leakage. Transfer here is mostly answer extraction.[^c4]
- AIME, free-generation: 88.11% of first-correct steps come before leakage. So continued reasoning from a partial trace succeeds without the answer being shown.[^c5]
- MMLU-Pro: 64.4% of force-answer first-correct steps come before the answer is explicit. The authors read this as a larger role for receiver knowledge and task priors.[^c6]
- ZebraLogic: complete-answer leakage is too coarse because answers have several fields. Receivers first become correct after 82.8% of gold answer components have appeared. Transfer depends on dense partial-answer information.[^c7]
- The authors' summary is that full-trace success can hide different mechanisms, and that scoring only complete-trace reuse can overstate what was transferred.[^c8]

## Receiver agreement as a stopping signal

Without gold answers, the provider can be stopped when a group of receivers agrees. The one-step rule stops at the first prefix where all receivers give the same answer. The two-step rule requires the same answer on two consecutive prefixes. If no agreement occurs, the full-trace prediction is used.[^c9] On AIME with four receivers, only 66.89% of one-step agreements occur after leakage. The two-step rule raises this to 91.67%, so persistence filters out unstable early agreement.[^c10] The authors treat this as a simulated signal over fixed traces, not a deployment strategy.

## Limits

- The study uses fixed provider traces and a simulated stopping rule. No live provider was stopped.
- Leakage on MMLU-Pro and ZebraLogic is detected with an LLM, so those splits carry detector error that I did not check.
- Most figures use one provider (Qwen-4B) for the leakage analysis. Whether the splits hold for other providers is not established from what I read.
- Free-generation agreement stops earlier, but the authors note this moves computation to the receiver side.
- The tasks are math, multiple-choice knowledge and logic puzzles. Nothing here tests open-ended questions or clarification.
- That a trace need not reflect the generator's internal computation is cited by the paper as prior work. It is not tested here.

## Related

- [[reasoning-trace-behavioral-transfer]] — a different channel: traces as a training signal that shifts later behavior, not as inference-time context
- [[information-utilization-rate]] — how much of supplied information a model actually uses
- [[cross-model-epistemic-divergence]] — receivers differ in what they bring to the same input
- [[model-family-continuation-compatibility]] — the same handoff with log-probability cut points, asking whether the provider-receiver family pairing keeps a chain correct; receiver strength tracks the same ordering

[^c1]: doi-10-48550-arxiv-2605-28913 — "problem from increasingly longer trace prefixes."
[^c2]: doi-10-48550-arxiv-2605-28913 — "We compare force-answer, where the receiver"
[^c3]: doi-10-48550-arxiv-2605-28913 — "We define answer leakage as the earliest prefix step"
[^c4]: doi-10-48550-arxiv-2605-28913 — "94.5% of force-answer first-correct steps occur at"
[^c5]: doi-10-48550-arxiv-2605-28913 — "88.11% of free-generation first-correct steps"
[^c6]: doi-10-48550-arxiv-2605-28913 — "On MMLU-Pro, 64.4% of force-answer first-correct"
[^c7]: doi-10-48550-arxiv-2605-28913 — "receivers first become correct after 82.8% of gold"
[^c8]: doi-10-48550-arxiv-2605-28913 — "has been transferred and obscure how reasoning traces"
[^c9]: doi-10-48550-arxiv-2605-28913 — "back to the complete-trace prediction."
[^c10]: doi-10-48550-arxiv-2605-28913 — "only 66.89% of one-step agreements occur after"
