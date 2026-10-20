---
description: "A GRPO reward term that adds a retrieval-time bonus only to answers already correct, centred on the batch's mean retrieval time, so cheaper correct paths score higher."
aliases: ["accuracy-efficiency reward", "batch-centred retrieval-time reward", "efficiency reward in RouteRAG"]
sources: ["arxiv-2512-09487"]
---
# Correctness-gated retrieval-cost reward

A multi-turn search agent trained only on answer correctness is paid the same for a correct answer reached after one lookup as after six (my reading of the stage-one reward, which is exact match alone). The RL systems that train such agents on outcome reward alone, the paper says, "effectively improves correctness" but "does not explicitly address retrieval cost or efficiency."[^c1] RouteRAG's sharpest point is that retrieval is not one price: graph evidence "is substantially more expensive to retrieve" than text,[^c2] so a policy that can choose between them needs a signal about what it spent.

The mechanism has two stages. In the first, the reward is exact match alone, "solely for answer correctness, allowing it to acquire" a base capability.[^c3] In the second, a correct trajectory also receives an efficiency term built from its total retrieval time, "from the total retrieval time across all reasoning" steps. The term is the batch mean retrieval time minus the trajectory's own time, divided by a normalizer.[^c4] A trajectory faster than the batch average gets a positive bonus, and a slower one a penalty.[^c5] A wrong answer gets no efficiency term at all, whatever its cost. The reward is then fed into GRPO, which scores each trajectory against the mean of its sampled group.[^c6]

Two choices in the design are argued for in the text. The reference is taken over the whole batch, not the group, because a group of about five trajectories gives a noisy mean: "Each GRPO group may contain only a few trajectories," and batch averaging "reduces the impact of noisy" timing.[^c7] The cost is the time spent retrieving, not a count of calls. My reading of the appendix's decomposition is that, for correct trajectories, the efficiency term enters the group-relative advantage as a deviation from the group's own mean, so a path cheaper than its peers is favoured and a costlier one penalised. The paper's words for the effect are that the term works by "discouraging unnecessary retrieval."[^c8]

What was measured: the paper reports that the trained 7B model "consistently reduce[s] the average retrieval turns across all datasets" relative to the variant trained without the term.[^c9] In the Table 4 averages the 7B row goes from "2.70 (+20%)" turns without the term to a lower count with it, while average F1 moves from "59.5 (-1.1)" without the term to a higher value with it.[^c10] For the 3B model the turn gap is smaller, "2.51 (+3.3%)" without the term, and F1 is "55.2 (-0.5)" without it.[^c11] The authors read the result as accuracy kept, "maintains comparable or even higher" than the outcome-only model, so that efficiency gains "do not come" at the cost of answer quality.[^c12]

## Limits

- The cost is wall-clock retrieval time (equation 4 uses total retrieval time), not number of calls or tokens. The turn count is reported separately, and the two can diverge: a single slow call and two fast ones cost differently under this reward. The slices read give no breakdown.
- The batch reference makes the reward depend on what else is in the batch. The appendix concedes that "a simple question requiring little retrieval could yield a disproportionately large" positive reward, and that "This is indeed a potential" drawback. Its answer is the group-relative step, which is argued, not isolated by an experiment in the slices read.[^c13]
- Gating on correctness means an agent that is wrong on a hard question receives no pressure to stop searching on it. Whether the term reduces wasted retrieval on questions the model cannot answer was not measured here (my inference).
- Only 3B and 7B models were trained: "and evaluation only on 3B and 7B LLMs."[^c14] The graph side is one retriever: "this choice limits our evaluation of how RouteRAG" interacts with other graph systems.[^c15]
- The differences in Table 4 are half an F1 point for 3B and about one point for 7B, reported as single averages. The slices read give no variance estimate, so the size of the accuracy effect is not established (my inference).
- The stage-two ablation, training with stage one only, is in Table 2; I did not extract its numbers, so the benefit of the two-stage schedule over a single mixed reward is not checked in this note.

## Related

- [[group-relative-advantage]] — the advantage that the efficiency term is centred within
- [[information-utility-retrieval-control]] — a dense per-step retrieval signal that is annealed away; the cost term here is added after a correctness-only stage and is not annealed
- [[heterogeneous-action-cost-substitution]] — a single scalar that sums action costs; here the cost is measured retrieval time, which makes graph retrieval dearer by construction
- [[knowledge-boundary-aware-reward]] — another reward term deferred by a two-stage curriculum
- [[self-answer-driven-search-depth]] — a reward that also targets the earliest sufficient search step, from the intermediate answers rather than from elapsed time
- [[syntactic-complexity-routing-between-retrieval-paths]] — a fixed external router between retrieval paths, where RouteRAG's mode choice is inside the policy

[^c1]: arxiv-2512-09487 — "While this reward design effectively improves correctness, it does not explicitly address retrieval cost"
[^c2]: arxiv-2512-09487 — "is substantially more expensive to retrieve."
[^c3]: arxiv-2512-09487 — "solely for answer correctness, allowing it to acquire"
[^c4]: arxiv-2512-09487 — "from the total retrieval time across all reasoning"
[^c5]: arxiv-2512-09487 — "This design provides positive reward for trajectories that"
[^c6]: arxiv-2512-09487 — "The policy model πθ is optimized by maximizing"
[^c7]: arxiv-2512-09487 — "Each GRPO group may contain only a few trajectories"
[^c8]: arxiv-2512-09487 — "discouraging unnecessary retrieval."
[^c9]: arxiv-2512-09487 — "consistently reduce the average retrieval turns across all datasets"
[^c10]: arxiv-2512-09487 — "2.70 (+20%)"
[^c11]: arxiv-2512-09487 — "2.51 (+3.3%)"
[^c12]: arxiv-2512-09487 — "maintains comparable or even higher"
[^c13]: arxiv-2512-09487 — "little retrieval could yield a disproportionately large"
[^c14]: arxiv-2512-09487 — "and evaluation only on 3B and 7B LLMs."
[^c15]: arxiv-2512-09487 — "this choice limits our evaluation of how RouteRAG"
