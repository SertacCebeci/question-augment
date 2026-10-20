---
description: "Separate predictors estimate each answering strategy's accuracy and cost on a task; routing picks the strategy by a weighted trade-off, or over a batch by a shared budget."
aliases: ["modular strategy predictors", "accuracy-and-cost routing", "constrained and unconstrained routing", "CONCUR routing"]
sources: ["arxiv-2512-09386"]
---
# Accuracy-cost strategy routing

A router of this kind does not choose a strategy from the task text alone. It first estimates, for every candidate strategy, how likely that strategy is to answer this task correctly and what it will cost, and then chooses on those two estimates. In the CONCUR framework a strategy is a (model, decoding method) pair, and the task is "a task ti as comprising both the question and any related context".[^c1] The paper's set is small: "five LLMs and two decoding methods, for a total of ten strategies".[^c2]

Each strategy gets two predictors, trained separately: "one estimates the accuracy of applying sj to the input task, and the other" estimates cost.[^c3] The accuracy predictor is a binary classifier, its label obtained by "comparing the generated and the target answers", and cost is a regression on "computational cost measured in FLOPs", which the authors chose so that models of different size can be compared.[^c4] [^c5]

Each predictor takes two kinds of input. A general-purpose vector comes from an off-the-shelf text embedding of the task and strategy descriptions. A task-specific vector comes from a learned linear projection of that embedding, and the strategy's model and decoding method are learned embedding lookups. The two are concatenated and passed through an MLP. The authors state that including the strategy representations "improves performance over strong routing baselines".[^c6]

Routing then becomes an optimization over these estimates. Unconstrained routing is "choosing the computation strategy that achieves an optimal trade-off between accuracy and cost", a weighted sum with a weight w on accuracy.[^c7] Constrained routing maximizes predicted accuracy under a budget. The paper's point is that solving the budget per task is not the same as solving it for the batch: "optimizing each task individually may not yield the best overall result".[^c8] Its dynamic program distributes a total budget across the batch rather than splitting it evenly. The paper reports that this global allocation gives a gain over the local one: "Table 4 shows a substantial positive change in both budget settings".[^c9]

The reason the design is modular is continual use. Each strategy has its own predictors, so "New strategies can be incorporated simply by training an additional predictor, without retraining existing ones".[^c10] The measured result is that the routed system "outperforms the best single strategy baseline and existing routing methods", with higher accuracy and lower cost on the reported benchmarks.[^c11]

## Limits

The answers scored are short and checkable: "factual multi-hop question answering with short text answers, general reasoning with multiple-choice answers, and mathematical problems requiring numerical answers".[^c12] Open-ended answers, multi-turn tasks and tasks whose right answer is not known in advance are outside the tested range. Nothing here is about which question to ask; the routed object is an answering strategy.

Cost is FLOPs during inference, a proxy and not wall-clock latency or money. The dynamic program's cost grows with the batch size and with the budget, which is my reading of the complexity the paper states. The authors justify keeping it manageable by saying "Since the budget can be kept relatively small through scaling", so the argument depends on budgets staying small.[^c13]

The accuracy labels are correctness against the target answer, as the method text describes. Whether they are stable under resampling of the model's output, or whether a predictor trained on one benchmark still ranks strategies correctly on another, is not established by what I read. The out-of-distribution results are the paper's test of that, and I did not read the tables that carry them, so the cross-benchmark claim is not checked here.

The continual-training claim is a design property plus a training-cost comparison in the paper's later section, which I did not read in full. What is established in the method text is that adding a strategy trains only its own two predictors; that the saving is smaller or larger in practice is not checked here.

Applying this to asking, rather than answering, is my own transfer; the paper does not make it, and the question-side reading of this note is mine.

## Related

- [[complexity-tiered-strategy-routing]] — a per-query router that learns its tiers by reinforcement learning; this note instead predicts accuracy and cost per strategy and optimizes over the predictions.
- [[model-orchestration]] — routes phases between models by hand and leaves automation open; the per-task automated choice here is the step that note lacks.
- [[routing-ceiling]] — a headroom bound: a router can only gain where the candidate strategies differ in accuracy, which bounds what the gains above can be.
- [[question-budgets]] — budgets on what is asked; here the budget is compute per task, a related but different constraint.

[^c1]: arxiv-2512-09386 — "We define a task ti as comprising both the question and any related context"
[^c2]: arxiv-2512-09386 — "In total, this yields five LLMs and two decoding methods, for a total of ten strategies"
[^c3]: arxiv-2512-09386 — "one estimates the accuracy of applying sj to the input task, and the other"
[^c4]: arxiv-2512-09386 — "by comparing the generated and the target answers"
[^c5]: arxiv-2512-09386 — "computational cost measured in FLOPs"
[^c6]: arxiv-2512-09386 — "including these strategy representations improves performance over strong routing baselines"
[^c7]: arxiv-2512-09386 — "choosing the computation strategy that achieves an optimal trade-off between accuracy and cost"
[^c8]: arxiv-2512-09386 — "optimizing each task individually may not yield the best overall result"
[^c9]: arxiv-2512-09386 — "Table 4 shows a substantial positive change in both budget settings"
[^c10]: arxiv-2512-09386 — "New strategies can be incorporated simply by training an additional predictor, without retraining existing ones"
[^c11]: arxiv-2512-09386 — "Results show that CONCUR consistently outperforms the best single strategy baseline and existing routing methods"
[^c12]: arxiv-2512-09386 — "factual multi-hop question answering with short text answers, general reasoning with multiple-choice answers, and mathematical problems requiring numerical answers"
[^c13]: arxiv-2512-09386 — "Since the budget can be kept relatively small through scaling"
