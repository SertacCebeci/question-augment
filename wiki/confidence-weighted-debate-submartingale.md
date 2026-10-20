---
description: "In a Dirichlet-categorical debate model, unweighted updates keep expected correctness flat (martingale); calibrated confidence-weighted updates make it drift upward, and diverse seeding helps."
aliases: ["confidence-modulated debate", "martingale limit of multi-agent debate", "diversity-aware initialisation for debate"]
sources: ["arxiv-2601-19921", "arxiv-2511-22854"]
---
# Confidence-weighted debate as a submartingale

In the Dirichlet-categorical model of multi-agent debate (MAD), each agent holds a Dirichlet vector over answers, samples its answer from it, and updates by adding one count per answer seen in the previous round. With homogeneous, fully connected agents, the expected belief in the correct option equals the current belief, so beliefs form a martingale: debate neither helps nor hurts in expectation.[^c1] This is why vanilla debate often fails to beat majority vote despite its cost.[^c2]

## Two separate levers

The paper splits the failure into two stages and treats each with its own mechanism.

**What is debated (diversity).** Because the martingale preserves whatever the start offers, the chance that the initial pool contains a correct hypothesis matters. The proposed initialiser samples a larger candidate pool and greedily picks the N answers with largest marginal diversity, leaving the debate protocol untouched.[^c3] Proposition 1: if success probability is nondecreasing in the number of distinct hypotheses and the diverse initialiser's count stochastically dominates random sampling, then success under diverse initialisation is at least as high.[^c4] Measured: both the number of unique answers and initial Pass@5 rose under diverse initialisation across models.[^c5] In unmodified vanilla MAD, initial diversity correlated significantly but weakly with final accuracy, and MAD helped more on harder datasets where diversity arises naturally.[^c6]

**How it aggregates (confidence).** Agents emit an answer plus a 0–10 verbal confidence, and Dirichlet counts are weighted by it. Theorem 1: if confidence is positively correlated with correctness, the belief process becomes a strict submartingale, E[p_t | F_{t-1}] ≥ p_{t-1}, strict on a positive-probability set.[^c7] Two practical obstacles are named: verbal confidence is miscalibrated, and agents may ignore others' confidence. The authors therefore train with reinforcement learning, using a log-score (binary cross-entropy style) calibration reward plus a correctness reward on the debate-update step, so the policy learns to condition on others' confidence.[^c8] Against an ablation that trains aggregation without the confidence reward, the confidence-modulated debate won on all datasets, including two out-of-distribution ones; starting from identical round-one outputs, it corrected more initially wrong answers and kept more correct ones.[^c9]

The two levers are complementary: one acts on the initial belief distribution, the other on the update dynamics.[^c10]

## Limits

- The theory lives inside the Dirichlet-categorical abstraction of an earlier paper: belief updates are counting, agents are homogeneous and fully connected; position bias and self-reflection are abstracted away.[^c11]
- Theorem 1 assumes confidence is positively correlated with correctness; where calibration fails, the drift guarantee does not apply.[^c12]
- The diversity selector is a heuristic, not claimed optimal; it costs extra sampling (N_cand rather than N answers).[^c3]
- Experiments use homogeneous agents; heterogeneous models and other topologies were not tested.
- Agents may respond to the stated number rather than to the argument behind it. In a debate between two reasoning models on CLadder, the authors find that "both models tend to be more persuaded by more confident arguments," and they cannot say whether this is argument quality "or if models are responding directly to the confidence score."[^c13][^c14] If so, the confidence weighting of Theorem 1 is weighting a signal the agents already use, and its correctness depends on calibration, not on persuasion. This is a single debate study, not a test of the submartingale result.
- The confidence arm requires RL training, so gains are not attributable to a prompt-only change; I did not read the per-dataset numbers closely, so the size of gains is not stated here.
- Proposition 1 is a stochastic-dominance statement; it does not say how large the gain is.

## Related

- [[disagreement-retention-in-debate]] — another way to keep disagreement alive in debate, by filtering messages rather than seeding
- [[verification-weighted-voting]] — weighting votes by a reliability signal, as confidence weights counts here
- [[surprisingly-popular-algorithm]] — aggregation beyond plain majority
- [[conformal-test-martingale]] — martingale vocabulary in a different field (testing); only the term is shared

[^c1]: arxiv-2601-19921 — "This means during the debate, the expected belief at the next round always"
[^c2]: arxiv-2601-19921 — "In practice, vanilla MAD"
[^c3]: arxiv-2601-19921 — "We apply a simple, training-free greedy approximation that iteratively selects the candidate with the"
[^c4]: arxiv-2601-19921 — "Proposition 1 (Diversity-aware initialization improves prior success)."
[^c5]: arxiv-2601-19921 — "demonstrating that our intervention raises the prior probability of MAD success by ensuring more debates"
[^c6]: arxiv-2601-19921 — "MAD tends to be more beneficial on more challenging tasks."
[^c7]: arxiv-2601-19921 — "Theorem 1 (Confidence-weighted debate yields"
[^c8]: arxiv-2601-19921 — "we directly train the"
[^c9]: arxiv-2601-19921 — "confidence modulation increases correction of initially incorrect"
[^c10]: arxiv-2601-19921 — "diversity initialisation affects the initial belief distribution (i.e., what hypotheses are"
[^c11]: arxiv-2601-19921 — "simple counting, ignoring that agents may receive"
[^c12]: arxiv-2601-19921 — "our confidence-modulated debate assumes that expressed confidence is positively correlated with correctness after calibration."
[^c13]: arxiv-2511-22854 — "both models tend to be more persuaded by more confident arguments"
[^c14]: arxiv-2511-22854 — "or if models are responding directly to the confidence score"
