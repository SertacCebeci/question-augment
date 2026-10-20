---
description: "A disclosure can arise from combining fragments that each reveal nothing alone: an agent that correlates several tool returns can infer a sensitive conclusion no single return supports."
aliases: ["TOP-R", "Tools Orchestration Privacy Risk", "mosaic effect", "compositional privacy leakage"]
sources: ["arxiv-2512-16310"]
---
# Compositional inference leakage

Leakage here is not a fragment that carries the secret. It is a secret that appears only when fragments are put together. The paper formalizes this for a single agent with several tools. The user's instruction is benign. Each tool returns something needed for the task plus a piece of a privacy fragment, and the agent combines the pieces in one reasoning trajectory. "A benign user request may lead the agent to correlate fragments from different tool returns within a single reasoning trajectory and infer a sensitive conclusion that no individual tool return directly reveals."[^c1]

The formal test has three conditions. The conclusion S must be sensitive (C1). No single observation supports S (C2). Some subset of at least two observations supports S (C3). The paper notes that "Conditions C2 and C3 imply that a valid TOP-R instance requires at least two observations to support the sensitive conclusion."[^c2] The number of essential returns is the compositional depth, CTD, which is "the minimum compositional depth."[^c3] The authors describe the mechanism as a contemporary form of the mosaic effect: "individually unclassified pieces can be aggregated to reconstruct classified information."[^c4]

The mechanism needs no attacker. "No prompt injection, tool compromise, or data poisoning is involved, and no party is acting adversarially." The paper's position is that "The risk arises from normal task execution."[^c5] So the leak comes from the answerer doing what it was asked, which is to combine what it has. Whether a combination is task-necessary is the judgement the agent has to make; the paper says the system "must decide whether an inference drawn from several individually non-revealing returns is still necessary for the task."[^c6]

What the measurement shows. On a 1,000-instance benchmark with six agents, "Across six LLM agents, average task completion, leakage, and H-score are 98.0 percent, 88.6 percent," and the H-score averages 20.4.[^c12] The H-score is a harmonic mean of completion and non-disclosure, so it is high only when both are high.[^c8] Leakage rose with depth: "LR rises from 78.7% at CTD 2 to 93.4% at" CTD 5 in the paper's table by assigned depth.[^c11] Completion and disclosure are separate capabilities: "High task completion does not imply low privacy leakage." A model can finish the requested task correctly and still disclose the conclusion, which is why a completion metric alone cannot show the risk.[^c7]

The transfer to questions and answers is my inference, not the paper's claim. An answer can be correct on every line and still carry a conclusion that was never asked for, once it is assembled from parts that each look harmless. An asker who wants to bound what an answer discloses would then have to measure the answer's conclusions, not only its fragments. (my inference)

## Limits

- The benchmark is built with LLM generators and LLM judges. A 30% human audit found "94% for the combined C1–C3 validation assessment," but the reported labels are post-audit labels of a judge model.[^c9]
- Tool returns are frozen and replayed. The paper says the benchmark "uses frozen tool-return records rather than live calls." Live tool failure, multi-turn memory, and downstream propagation are not measured; the paper lists "Hidden internal states, tool-call logs, memory, and downstream propagation" as outside its measurement scope.[^c10]
- The sensitive conclusions are drawn from the benchmark's own privacy domains. Whether the same compositional pattern holds for conclusions outside them is not tested here. (my reading)
- The paper's result on defenses is that "These results show that TOP-R requires defenses beyond prompting alone." It reports that prompt-only mitigation gave a small average gain. Whether a different defense closes the gap is not established here.[^c13]
- The H-score weights completion and non-disclosure equally in its harmonic form. A deployment that prices one above the other would need a different weighting; this is my inference from the formula, not something the paper tests.

## Related

- [[exploitable-information-leakage]] — scores a reply by what a blind opponent can recover from it, against task utility; this note adds that the recovered conclusion may never be stated in any single part of the reply.
- [[personalization-privacy-tradeoff]] — more personalized answers disclose more personal information; compositional inference is a second route to the same disclosure that a per-answer check can miss.
- [[personal-representation-leakage]] — attribute inference from a stored profile is one case of inferring a private attribute from fragments; the profile is the aggregator.
- [[manipulative-information-uptake]] — a set of individually supported claims can mislead together, which a per-claim check does not catch; the same structural gap, applied to decisions rather than disclosures.

[^c1]: arxiv-2512-16310 — "A benign user request may lead the agent to correlate fragments from different tool returns within a single reasoning trajectory and infer a sensitive conclusion that no individual tool return directly reveals."
[^c2]: arxiv-2512-16310 — "Conditions C2 and C3 imply that a valid TOP-R instance requires at least two observations to support the sensitive conclusion."
[^c3]: arxiv-2512-16310 — "Thus, CTD is the minimum compositional depth"
[^c4]: arxiv-2512-16310 — "individually unclassified pieces can be aggregated to reconstruct classified information."
[^c5]: arxiv-2512-16310 — "The risk arises from normal task execution"
[^c6]: arxiv-2512-16310 — "The system must decide whether an inference drawn from several individually non-revealing returns is still necessary for the task"
[^c7]: arxiv-2512-16310 — "High task completion does not imply low privacy leakage."
[^c8]: arxiv-2512-16310 — "A high H-score requires both task completion and non-disclosure."
[^c9]: arxiv-2512-16310 — "Agreement between the manual review and the LLM judge was"
[^c10]: arxiv-2512-16310 — "uses frozen tool-return records rather than live calls."
[^c11]: arxiv-2512-16310 — "LR rises from 78.7% at CTD 2 to 93.4% at"
[^c12]: arxiv-2512-16310 — "Across six LLM agents, average task completion, leakage, and H-score are 98.0 percent, 88.6 percent,"
[^c13]: arxiv-2512-16310 — "These results show that TOP-R requires defenses beyond prompting alone."
