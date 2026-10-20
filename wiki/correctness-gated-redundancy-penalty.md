---
description: "A tool-call penalty applied only to answers already correct, measured against the fewest calls earlier correct answers to that query used, so wrong answers are not charged for calls."
aliases: ["adaptive tool reward", "correct-answer-gated tool penalty", "minimal-call baseline reward"]
sources: ["arxiv-2512-06653", "doi-10-48550-arxiv-2607-10463", "arxiv-2512-02361"]
---
# Correctness-gated redundancy penalty

A model rewarded for answer accuracy alone learns to search more. The paper states the problem as "primary objective, causing models to increase retrieval frequency," since extra retrieval is the cheapest way to raise accuracy.[^c1] Simple efficiency penalties were the obvious fix, and the paper says "such approaches often result in performance" loss, because a scalar reward cannot balance the two goals.[^c2]

The proposed fix makes the efficiency term conditional on correctness and sets its reference per query. For each query the training run "we record the minimal tool usage number" of calls among trajectories that answered correctly.[^c3] A later trajectory on the same query is scored by its excess calls over that reference. If its F1 reaches a threshold, the tool term is an exponential decay in the excess, "exponential decay based on tool usage that exceeds the established" baseline. If F1 falls short, the tool term is zero.[^c4] The gate is the stated purpose of the design, which the paper describes as "avoiding efficiency sacrifices when accuracy is not yet achieved."[^c5]

The same gate turns up in a turn-count reward for a multi-hop retrieval agent. There the efficiency term is paid "only when the answer reward exceeds" 0.5, with the stated purpose of "preventing the agent from receiving efficiency" credit for answers reached by guessing.[^c13] The term is linear in the turns left unused rather than measured against a per-query minimum, so the gate is the part the two designs share. My reading: a fixed threshold on answer F1 is a cruder reference than the cheapest correct run, but it needs no record of earlier trajectories.

A visual tool-use model applies a gate of the same shape to its call term. In the VACoT paper the call reward is zero unless the answer reward reaches 0.5. It is one for up to two calls and then decays as the count rises toward a maximum K.[^c15] The authors say the term "would only be awarded" when the model both makes valid calls and answers correctly, and that without it the model "exhaustively" tries augmentations.[^c16][^c17] The reference here is a fixed allowance of two calls, not the policy's own cheapest correct run. My reading: the correctness gate is the shared element, and this reference is the cruder of the two.

The tool term enters a total reward. The paper's overall form is a weighted sum of an accuracy term and the tool term, with a format check that returns −1 for malformed output: "The overall reward function in our lightSearcher is defined as" that weighted sum.[^c6] Read literally, the tool term is 1 when the call count is at or below the reference and falls below 1 as calls exceed it. It is 0 for an incorrect answer. So a wrong answer is not penalized for its calls; it simply earns no tool term. That reading is mine, from the formula.

The ablation isolates the whole mechanism. Removing the adaptive reward gives "in a surprisingly marginal improvement in model accuracy metrics, yet induces a substantial escalation in search tool invocations," rising "to 2.06 (a 27% rise relative to LightSearcher)."[^c7][^c8] The abstract reports the full method as "reducing search tool invocations by 39.6%" while it "maintains accuracy comparable to SOTA baseline ReSearch."[^c9][^c10]

## What transfers

The transferable part is the reference. The baseline is the cheapest correct run the policy has already produced on the same item, taken online during training. No reference model and no separate counterfactual run is needed. The penalty tightens as the policy finds cheaper successes, and it asks only whether a call was needed for a correct answer, not whether the item could be answered without the tool.

This is a different measure from the paired-benefit reward in [[benefit-scaled-tool-reward]], which scores each call by the accuracy gap between the same question answered with and without the tool, computed offline by a reference model. It is also different from [[self-answer-driven-search-depth]], which looks inside the trajectory for the earliest search step whose intermediate answer is already right. Here the reference is a count over complete trajectories, and the content of the calls is not inspected.

What does not transfer cleanly is the count itself. The formula counts calls, not their usefulness. Two correct runs with the same number of calls score the same whether one call was decisive or the others were idle. The paper's measure of efficiency is therefore a measure of call frequency under a correctness gate, not of retrieval quality.

## Limits

- The reference n is a running minimum over the policy's own trajectories. My reading of the formula: a correct answer reached with no search sets n to zero, and every later correct answer that uses any call is then discounted. The text I read does not say whether such runs are excluded or treated specially.
- The threshold on F1 and the penalty strength are named in the formula without values. The places where the weights are named give no numbers, and I found no values for them in the passages I searched.
- The gate needs a correctness signal during training, since F1 is computed against gold answers. The method is therefore a training-time reward. The paper's evaluation does not test a setting without gold answers, and nothing here claims it would work there.
- The ablation removes the whole adaptive reward at once, so the gate and the exponential shape are not separated. It is not shown that the gate alone accounts for the efficiency gain.
- Evidence is one base model and one dataset in the ablation: "HotpotQA dataset using Qwen2.5-7B-Instruct as the base model."[^c11] The authors' claims for the rest rest on "while validated on multi-hop QA."[^c12]
- A correctness gate does not by itself stop premature answers. The GRASP paper reports that its policy, which has the same gate, still answers early: "the policy still occasionally commits to an answer before the required" evidence is retrieved, and it lists reward shaping against that as future work.[^c14]

## Related

- [[benefit-scaled-tool-reward]] — rewards a call by its paired benefit from a reference model; this note uses the policy's own cheapest correct run as the reference and gates on correctness.
- [[self-answer-driven-search-depth]] — also trains toward the earliest sufficient search step, using intermediate answers rather than call counts.
- [[contrastive-experiential-memory]] — the same paper's memory half; that note shapes what the policy is told, this note shapes what it is paid for.
- [[post-hoc-visual-augmentation]] — the visual-tool case: image transforms rather than searches, with the call reward gated on correctness and a fixed two-call allowance.

[^c1]: arxiv-2512-06653 — "primary objective, causing models to increase retrieval frequency"
[^c2]: arxiv-2512-06653 — "such approaches often result in performance"
[^c3]: arxiv-2512-06653 — "we record the minimal tool usage number"
[^c4]: arxiv-2512-06653 — "exponential decay based on tool usage that exceeds the established"
[^c5]: arxiv-2512-06653 — "avoiding efficiency sacrifices when accuracy is not yet achieved"
[^c6]: arxiv-2512-06653 — "The overall reward function in our lightSearcher is defined as"
[^c7]: arxiv-2512-06653 — "in a surprisingly marginal improvement in model accuracy metrics, yet induces a substantial escalation in search tool invocations"
[^c8]: arxiv-2512-06653 — "to 2.06 (a 27% rise relative to LightSearcher)"
[^c9]: arxiv-2512-06653 — "reducing search tool invocations by 39.6%"
[^c10]: arxiv-2512-06653 — "maintains accuracy comparable to SOTA baseline ReSearch"
[^c11]: arxiv-2512-06653 — "HotpotQA dataset using Qwen2.5-7B-Instruct as the base model"
[^c12]: arxiv-2512-06653 — "while validated on multi-hop QA"
[^c13]: doi-10-48550-arxiv-2607-10463 — "preventing the agent from receiving efficiency"
[^c14]: doi-10-48550-arxiv-2607-10463 — "the policy still occasionally commits to an answer before the required"
[^c15]: arxiv-2512-02361 — "This reward is re-weighted by"
[^c16]: arxiv-2512-02361 — "be awarded when the model both invokes valid API calls"
[^c17]: arxiv-2512-02361 — "vanilla training manner leads the model to exhaustively try"
