---
description: "A label-free reward for a question-proposing agent that peaks when the Solver's majority-vote agreement is 50%, minus a density penalty, so proposals track the Solver's capability frontier."
aliases: ["challenge reward", "R_chal", "frontier-targeting question reward", "50% agreement reward"]
sources: ["arxiv-2602-11241", "arxiv-2512-02472", "arxiv-2511-16043"]
---
# Uncertainty-peaked challenge reward

> Score a proposed question by how undecided the Solver is about it:
> zero reward for questions it always or never answers consistently,
> maximal reward at an even split.

## Mechanism

In Active-Zero, a Searcher (finds images), a Questioner (writes questions) and a Solver are all initialised from one base vision-language model and trained with GRPO. For a probe question x on image I, the Solver is run m times and its empirical accuracy is the fraction of passes that equal the majority-voted answer.[^c1] The challenge reward is R_chal = 1 − |2·Acc − 1|, which is 0 at Acc = 0 or 1 and 1 at Acc = 0.5.[^c2] Maximising it pushes the proposer toward contexts "just beyond its deterministic grasp yet within its latent reasoning potential".[^c3] No labels are needed: "accuracy" is agreement with the Solver's own consensus.

Uncertainty alone invites collapse onto a few ambiguous query types, so the reward is R = max(0, R_chal − P_rep). The penalty P_rep counts a sample's neighbours among batch samples, clustered in text space (1 − BLEU) and image space (1 − cosine of a frozen encoder).[^c4] For the Questioner the same form is used with a linguistic repetition penalty, so questions avoid "both trivial consensus and complete randomness".[^c5]

Advantages are normalised within a semantic domain (group-relative against domain peers), so the proposer cannot drift toward domains with higher absolute reward.[^c6]

The Solver itself is then trained only on items whose consensus accuracy lies inside a window (τ_low = 0.3, τ_high = 0.8 in the paper), with the majority answer as a silver label, so it sees neither trivially solved nor out-of-reach items.[^c7] The pairing is a curriculum with two ends: the proposers aim at the frontier, and the filter on the Solver side keeps only the band.

The same pairing reappears in R-Few, where the Challenger's reward is again built to peak at mid-range Solver success, and the band is applied to one pool in which human-labelled items sit beside the synthetic ones: the paper sorts "all questions (both synthetic and human) by success rate" and keeps the mid-range items.[^c8] The human items are not exempt from the band; they are upweighted "to prevent forgetting" through a separate term.[^c9] Whether a human item that falls outside the band is still useful is not addressed in the text I read. The band thus governs human and synthetic data by one rule, a design choice the note's Solver-side filter does not require.[^c8]

Agent0 uses the same two halves with a code-executing solver. Its curriculum agent is paid through a reward designed to peak when the solver is most divided, and it is trained toward tasks that the executor finds confusing or uncertain.[^c10][^c11] The executor is then trained only on tasks kept by a band on the same score, retaining tasks with a self-consistency between 0.3 and 0.8.[^c12] That band is not symmetric about one half, although the paper states its threshold as δ = 0.25 around 0.5, which would give 0.25 to 0.75. The text does not say which was run; I read this as a discrepancy in the paper's own description, not a tested effect. Agent0 also pays the proposer for the solver's tool calls, which is a separate reward, see [[tool-demanding-question-reward]].

## Limits

- The reward is peaked at 50% agreement, which cannot tell "hard but learnable" from "ambiguous or ill-posed", since both yield split votes. Nothing here separates the two; this is my inference, not a result tested in the paper.
- The silver label is the Solver's own majority vote, so a systematically wrong consensus is reinforced. I did not read an experiment isolating this.
- The 50% peak and the 0.3 to 0.8 window are fixed design choices; I did not find a sweep justifying them.
- Training was on a local pre-indexed image pool of 1.6M images, not on live web search.

## Related

- [[self-consistency-difficulty-score]] — the same majority-vote agreement fraction used as a difficulty measure
- [[temporal-perturbation-questioner-reward]] — another label-free Questioner reward built from Solver confidence
- [[self-evolving-visual-questioner]] — a different closed loop for visual question proposing
- [[learnability-posterior-curriculum]] — curriculum aimed at learnable difficulty
- [[anchor-conditioned-question-generation]] — the same kind of challenger, conditioned on a few sampled human-labelled examples, with a zero-example setting that reverts to ungrounded self-play
- [[tool-demanding-question-reward]] — the tool-call term that Agent0 adds to a proposer reward of this shape

[^c1]: arxiv-2602-11241 — "where ŷ denotes the majority-voted consensus. The challenge reward peaks at maximum uncertainty:"
[^c2]: arxiv-2602-11241 — "Maximizing Rchal compels the Searcher to identify visual"
[^c3]: arxiv-2602-11241 — "potential."
[^c4]: arxiv-2602-11241 — "The final reward is RS = max(0, Rchal − Prep ), encouraging the agent to explore diverse coordinates across the"
[^c5]: arxiv-2602-11241 — "By maximizing Rchal , the Questioner generates tasks that"
[^c6]: arxiv-2602-11241 — "the advantage Â is"
[^c7]: arxiv-2602-11241 — "This ensures the Solver optimize trajectories that are neither"
[^c8]: arxiv-2512-02472 — "sort all questions (both synthetic and human) by success rate"
[^c9]: arxiv-2512-02472 — "upweights the scarce human anchors"
[^c10]: arxiv-2511-16043 — "The reward function is designed to"
[^c11]: arxiv-2511-16043 — "tasks that the Executor finds confusing or uncertain"
[^c12]: arxiv-2511-16043 — "retaining tasks with a self-consistency"
