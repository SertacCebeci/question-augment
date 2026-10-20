---
description: "Sampling many proofs helps only if one can be picked: a verifier-scored archive refined by PATCH and REWRITE moves, then a pairwise tournament, turns best@K into a single pass@1 answer."
aliases: ["MaxProof", "population-level test-time scaling", "best@K to pass@1 conversion", "verifier-guided evolutionary proof search"]
sources: ["doi-10-48550-arxiv-2606-13473"]
---
# Population search under a noisy verifier

A model that solves a problem in some of its samples has a best@K score that a single answer does not reach, because nothing tells the user which sample is the right one. The MaxProof framing is that the gap is a search problem: "a base model may fail on a single sample, but its best candidate among many" independent samples can be much stronger.[^c1] The framework's stated aim is to turn that into a single-answer system, "pass@1 by searching over a population of candidate proofs, amortizing verifier noise across many" candidates.[^c2]

The loop has three parts. First, N candidates are sampled from the generator and each is verified several times; the fitness of a candidate is the minimum verifier score over those samples (see [[pessimistic-min-judge-aggregation]]), and the archive keeps each proof with its critique and a short summary. Second, for a fixed number of rounds, the top parents are chosen by fitness with a diversity filter, and each parent yields two offspring. PATCH "is the exploitation move: it asks the refiner to" address the verifier's concrete errors while keeping the correct parts; REWRITE "is the exploration move: it asks the refiner to take the high-level idea" and try another route.[^c3] Offspring are verified and added to the archive, and both refinement modes see compact summaries of sibling candidates, so a failure shared by several candidates can be avoided. Third, the loop stops early once two archive candidates reach the maximum score, and a pairwise tournament over the top candidates picks the answer; each match asks the ranker "which of two candidates is the more correct proof" "rather than to assign an absolute score."[^c4]

The paper's reading is that this is an evolutionary search, with the archive as population and the verifier as fitness.[^c5] The reported effect on the M3 model is 35/42 on IMO 2025 and 36/42 on USAMO 2026, above the gold threshold on both.[^c6] The authors argue that the gap to one-shot, of 8 and 10 points, is larger than a plain sampling baseline would give: such a baseline "would, in expectation, lift the score by far less" than that.[^c7] The three components are each motivated by verifier noise: parents are chosen to avoid near-duplicates, the early stop requires two maximum-score candidates, and the final choice is made by comparison rather than by the noisy absolute score. The tournament is the same kind of pairwise comparison that [[prompt-tournament-evaluation]] uses for human ranking, but here the judge is the model itself.

## Limits

- The reported scores come from one model, one configuration (population 32, four verifier samples, ten rounds) and two contests. The parts I read give no run-to-run variance and no cost in tokens or time for a full search. (my reading)
- Search cannot exceed the best candidate it ever generates. On IMO 2025 P6 the population never reaches a viable approach, which the authors call "a base-model capability ceiling, not a search failure."[^c8]
- The final selection can lose the best candidate. On USAMO 2026 P2 a 6/7 candidate sits in the archive but "the self-pick tournament does not select, and the selection loss is 4 points."[^c9] The authors call this a known weakness of the tournament, which arises when verifier scores cluster and the ranker's preferences diverge from the absolute score.[^c10]
- The early stop is a redundancy argument: the chance that two candidates are both false positives is lower than for one. It is not a measured false-positive rate for the stop rule. (my inference)
- Diversity is a lexical rule, not a semantic one: "not both selected if they share a long common prefix."[^c11] Two different wordings of the same wrong idea can both be selected. (my inference)
- The framework is described as model-agnostic, but in the reported experiments "all four roles" are played by the same merged model under different prompts.[^c12] Separate verifiers, rankers or refiners are not tested.
- The sampling-baseline comparison is an argument, not a run reported in the parts I read.

## Related

- [[pessimistic-min-judge-aggregation]] — the min-over-judges reward used as the fitness function here
- [[evolutionary-prompt-search]] — the same population-and-mutation loop applied to prompts, scored on a dev set
- [[tree-search-methods]] — the other way of spending extra inference compute on a search over partial solutions
- [[oracle-best-of-strategies-batch-selection]] — an oracle best-of-candidates whose gap to the real selector is kept as a diagnostic, like the population ceiling versus the self-pick here
- [[verification-weighted-voting]] — aggregating verified answers by weight rather than by a comparison tournament
- [[agentic-iteration-gap-under-localized-verifier-feedback]] — localized verifier feedback driving iterative correction, the mechanism PATCH relies on

[^c1]: doi-10-48550-arxiv-2606-13473 — "a base model may fail on a single sample, but its best candidate among many"
[^c2]: doi-10-48550-arxiv-2606-13473 — "pass@1 by searching over a population of candidate proofs, amortizing verifier noise across many"
[^c3]: doi-10-48550-arxiv-2606-13473 — "PATCH is the exploitation move: it asks the refiner to"
[^c4]: doi-10-48550-arxiv-2606-13473 — "rather than to assign an absolute score."
[^c5]: doi-10-48550-arxiv-2606-13473 — "This loop is naturally read as an evolution-inspired search process"
[^c6]: doi-10-48550-arxiv-2606-13473 — "reaches 35/42 on IMO 2025 and 36/42 on USAMO 2026, exceeding the human gold-medal threshold on both."
[^c7]: doi-10-48550-arxiv-2606-13473 — "lift the score by far less"
[^c8]: doi-10-48550-arxiv-2606-13473 — "this is a base-model capability ceiling, not a search failure."
[^c9]: doi-10-48550-arxiv-2606-13473 — "self-pick tournament does not select, and the selection loss is 4 points."
[^c10]: doi-10-48550-arxiv-2606-13473 — "weakness of the tournament self-pick: in a population where the verifier"
[^c11]: doi-10-48550-arxiv-2606-13473 — "not both selected if they share a long common prefix."
[^c12]: doi-10-48550-arxiv-2606-13473 — "In the M3 release setting used in Section 6, all four roles"
