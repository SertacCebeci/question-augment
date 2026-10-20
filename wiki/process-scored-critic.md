---
description: "In multi-agent debate, a critic scoring each debater's reasoning on fixed weighted criteria, not the vote, cut false rejections of safe household tasks in one embodied-safety paper."
aliases: ["critical agent", "critical evaluator", "reasoning-scoring critic", "critic model in multi-agent debate"]
sources: ["arxiv-2511-21460"]
---
# Process-scored critic

In a multi-agent debate, a critic is a separate model that does not vote on the answer. It reads each debater's assessment and scores the reasoning behind it on fixed, weighted dimensions, then sends the scores and its own chain of thought back into the next round. In the MADRA paper the four dimensions are logical soundness, risk identification, evidence quality and clarity, and the authors "established four dimensions and their weights" from failure modes they had seen.[^c1] The design choice is stated directly: "the Critical Agent solely scores the reasoning process."[^c2] The debaters, not the critic, decide. If the agents agree within three rounds the consensus stands; otherwise "the decision will be made by majority" vote among the debaters.[^c3]

The mechanism targets one error of single-model safety judgment. The authors' premise is that "Even safe instructions are prone to be overinterpreted as dangerous."[^c4] The logical-soundness score penalises that over-interpretation, and the evidence score penalises a model that builds a hypothetical hazard around a benign task, since "LLMs often imagine virtual scenarios related" to a task.[^c5] A debater that wants a higher score has to justify a refusal from the instruction's evidence rather than from an imagined setting. The stated purpose is to reduce herd effects: the critic is there so that "This constrains bias by forcing evaluation on" reasoning rather than on output preference.[^c6] The paper says critical agents "reduce the herd mentality of LLMs."[^c7]

What was measured. In the ablation, the paper reports that without the critic "the rejection rate curve is more" convoluted across debate rounds, and that with it the effect "improves by at least 5%."[^c8][^c9] The headline comparison is against single-agent safety prompting. Safety-CoT flags "20%–42% of inherently safe instructions as harmful," while MADRA keeps "the safe task false alarm rate below 30% for seven out of eight" models, and the authors call "reduction in over-rejection is statistically significant."[^c10][^c11][^c12] The same pipeline reaches "MADRA reaches reject 90% unsafe tasks in all models" on the unsafe side.[^c13] Note that this compares the whole pipeline, debate plus critic, with a single-agent prompt. The critic's own share is what the ablation isolates.

For asking and answering, the relevant point is that the critic changes what a debate rewards. A standard applied to the debaters decides where the exchange converges, which is the pattern in [[adjudication-standard-sets-debate-outcome]]. Here the standard is a process score rather than a logic or ethics rule, and a standard that rewards grounded reasoning is aimed at the over-refusal error described in [[skepticism-trap]]. My reading is that the critic is a way to make a safety judgment answer the question "is this instruction dangerous?" rather than "does this instruction look dangerous?". The passages read do not test whether the critic also catches missed unsafe tasks beyond the 90% headline.

## Limits

- The critic is load-bearing. The paper reports that using a weaker critic model "as the Critical Agent leads to a significant increase in the overrejection of safe tasks."[^c14] The gain is therefore a property of the critic's capability, not of the scoring scheme alone.
- The critic is an LLM, and the authors say it "is not designed to be unbiased."[^c15] The claim is that its rubric is consistent, not that its scores track whether a task is dangerous. Nothing read shows that the score predicts correctness.
- The weights (0.3, 0.3, 0.3, 0.1) were set from failure modes observed in the same experiments on the same benchmarks.[^c16] No sensitivity analysis to the weights appears in the passages read.
- The "statistically significant" claim comes with no test or p-value in the passages read. The "at least 5%" figure comes from a figure whose values were not read as a table.
- Both benchmarks are household, and one (SafeAware-VH, 800 instructions) was built by the same authors. Nothing here tests other domains, and the critic was not compared with other critics or with a debate of matched cost.

## Related

- [[skepticism-trap]] — the over-refusal error direction that a reasoning critic is meant to reduce
- [[adjudication-standard-sets-debate-outcome]] — the same point for a different standard: whoever scores a debate sets where it converges
- [[disagreement-retention-in-debate]] — controls which responses are broadcast; the critic controls which reasoning is rewarded
- [[safety-oriented-prompting]] — the single-agent safety prompt this critic is offered as an alternative to

[^c1]: arxiv-2511-21460 — "We established four dimensions and their weights"
[^c2]: arxiv-2511-21460 — "the Critical Agent solely scores the reasoning process"
[^c3]: arxiv-2511-21460 — "If no consensus is reached, the decision will be made by majority"
[^c4]: arxiv-2511-21460 — "Even safe instructions are prone to be overinterpreted as dangerous"
[^c5]: arxiv-2511-21460 — "LLMs often imagine virtual scenarios related"
[^c6]: arxiv-2511-21460 — "This constrains bias by forcing evaluation on"
[^c7]: arxiv-2511-21460 — "reduce the herd mentality of LLMs"
[^c8]: arxiv-2511-21460 — "that without the Critical Agent, the rejection rate curve is more"
[^c9]: arxiv-2511-21460 — "effect improves by at least 5%"
[^c10]: arxiv-2511-21460 — "20%–42% of inherently safe instructions as harmful"
[^c11]: arxiv-2511-21460 — "the safe task false alarm rate below 30% for seven out of eight"
[^c12]: arxiv-2511-21460 — "reduction in over-rejection is statistically significant"
[^c13]: arxiv-2511-21460 — "MADRA reaches reject 90% unsafe tasks in all models"
[^c14]: arxiv-2511-21460 — "as the Critical Agent leads to a significant increase in the overrejection of safe tasks"
[^c15]: arxiv-2511-21460 — "is not designed to be unbiased"
[^c16]: arxiv-2511-21460 — "based on the frequency of specific failure modes observed in our experiments"
