---
description: "Without external reward anchors, self-reward training saturates; a human-verified holdout index of judge accuracy plus checker fidelity localizes when to stop."
aliases: ["PAV", "Pairwise Advantage Validity", "holdout-monitored early stopping for self-reward"]
sources: ["doi-10-48550-arxiv-2608-24231"]
---
# Pairwise Advantage Validity stopping

In a closed loop where a model's own evaluation supplies the RL reward, nothing external says when the reward stopped being informative. RecurSE argues that such recursion is bounded: "recursive optimization cannot continue indefinitely once selfgenerated rewards or ranking fidelities saturate."[^c1]

**Why checker error matters pairwise.** Group-relative advantages depend only on the ordering of n scores within a prompt, so what must stay faithful is the score difference, not the absolute score. By the triangle inequality the error of a score difference is at most the sum of the two individual normalized errors, so the expected pairwise ranking error is bounded by twice the checker error.[^c2]

**The index.** PAV combines judge rule accuracy A_t and normalized checker error e_C,t on a compact human-verified holdout: V_t = 1 − ((1 − A_t) + 2e_C,t)/3. The weight 2 follows the bound and is fixed in advance. Sample means make the estimate unbiased at each checkpoint, and 95% prompt-bootstrap intervals are reported.[^c3] A fall in checker fidelity signals uncalibrated pairwise rewards, and a high value marks an effective checkpoint region, which guards against "validation deception" where same-style accuracy rises while cross-style transfer drops.[^c4]

**Why not a cheaper signal.** Checker parse rate used as a stopping heuristic (first drop above 5% from peak) would select step 160, long after transfer metrics began to deteriorate. It lags the fidelity signal PAV captures.[^c5]

**What happens after the window.** Late checkers inflate scores to a uniform 3 or 4, which collapses within-group advantage variance and starves the policy of relative gradients. They also fabricate quotes to justify high meta-scores.[^c6]

## Limits

- The holdout needs a one-time human verification cost. Its labels never enter training rewards, so the loop is anchored only in monitoring, not in learning.[^c7]
- Shown for rubric judges on Qwen3.5-9B, Gemma-4-E4B-it and Qwen3.6-27B; whether the weights or the bound carry to non-rubric or open-ended self-modification is not tested (the paper fixes task spec, optimizer and checking protocol).
- The 2:1 weight is derived from a worst-case triangle bound; the paper does not show it is optimal. This is my reading.

## Related

- [[llm-judge-biases]] — judge biases are what an unanchored loop can amplify
- [[judge-master-key-false-positives]] — a related way judge reward is gamed
- [[reasoning-judge-adversarial-policy]] — policies exploiting judge rewards
- [[multi-turn-conformal-stopping]] — another principled stopping rule

[^c1]: doi-10-48550-arxiv-2608-24231 — "recursive optimization cannot continue indefinitely once selfgenerated rewards or ranking fidelities saturate"
[^c2]: doi-10-48550-arxiv-2608-24231 — "the expected pairwise ranking error is bounded"
[^c3]: doi-10-48550-arxiv-2608-24231 — "The relative weight of 2 on checker error directly reflects the bound in Eq. 4 and is fixed a priori."
[^c4]: doi-10-48550-arxiv-2608-24231 — "preventing validation deception where same-style accuracy rises while cross-style transfer degrades"
[^c5]: doi-10-48550-arxiv-2608-24231 — "Parse rate is not a substitute for PAV."
[^c6]: doi-10-48550-arxiv-2608-24231 — "This collapses within-group advantage variance"
[^c7]: doi-10-48550-arxiv-2608-24231 — "Constructing this holdout"
