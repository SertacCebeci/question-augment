---
description: "A reasoning chain is rebuilt backward from its answer to the question, and the token overlap with the forward chain is scored; a 0.6B model at 70%+ accuracy scored 15%."
aliases: ["forward-backward consistency", "forward-backward alignment", "bidirectional reasoning consistency", "bidirectional alignment"]
sources: ["arxiv-2512-00552"]
---
# Bidirectional reasoning consistency

A chain of reasoning can be tested by running it in the other direction. The procedure has two passes over the same problem. The forward pass produces "reasoning chains (question → steps → answer)". The backward pass produces "backward reconstructions (answer → steps → question)", starting from the model's own answer and working back to the question.[^c1] Consistency is then a set overlap between the two sets of steps: "Consistency is measured by Jaccard similarity:"[^c2] — the tokens that appear in both the forward and backward steps, divided by the tokens that appear in either.

The mechanism the test relies on is retracing. A chain that used a real dependency structure, with each step feeding the next, should be recoverable from its end, and its backward reconstruction should use the same intermediate quantities. A chain assembled from surface cues may reach the same answer without that structure, and the backward pass then has nothing to retrace. This link between retraceability and dependence is my inference; the paper states the test but does not isolate that mechanism.

On a small model the measured overlap was low. The paper reports that the model "achieves reasonable answer accuracy (70%+)" while "it demonstrates poor backward consistency (15%)".[^c3] The authors read the gap as "revealing severe bidirectional alignment failures".[^c4] The backward chains were also longer than the forward ones, averaging about 7.7 steps against about 6.4, which the authors read as "verbose but incoherent reverse explanations".[^c5]

## Limits

- One model, one benchmark. The paper says "empirical findings are based on a single 600M-parameter" model, though it calls the framework model-agnostic.[^c6] The sections I read contain no run on a second model.
- The score is lexical. Jaccard counts shared tokens, not shared inferences. Two backward chains that retrace the same dependency in different words score low, and a verbose chain adds tokens to the union and lowers the score even when every step is right. The length asymmetry (7.7 against 6.4 steps) could therefore depress the number by itself; the paper does not test this (my inference).
- No reference point. The text reports 15% but no baseline from a larger model, a human reverse-chain, or a repeated forward pass, so the number shows inconsistency by this measure, not the distance from what is achievable.
- The sections I read report no check of this score against human judgments of consistency.
- A low score says the two directions disagree. It does not say which direction is wrong, and a consistent chain can still be wrong from the start.

## Related

- [[chain-step-transitivity-coverage]] — the paper's second chain-level measure, computed on the same forward and backward structures, and scoring step links rather than token overlap.
- [[accuracy-masks-unstable-reasoning]] — the same concern that a correct final answer hides the route, approached through internal stability instead of a reverse pass.
- [[backward-chaining-subgoal-decomposition]] — backward chaining as a way to solve; this note uses the backward direction only as a probe of a finished chain.
- [[reasoning-path-fidelity]] — scores a chain against an expert's checkpoints; this test needs no reference path, only the model's own answer.

[^c1]: arxiv-2512-00552 — "backward reconstructions (answer → steps → question)"
[^c2]: arxiv-2512-00552 — "Consistency is measured by Jaccard similarity:"
[^c3]: arxiv-2512-00552 — "while the model achieves reasonable answer accuracy (70%+), it demonstrates poor backward consistency (15%)"
[^c4]: arxiv-2512-00552 — "revealing severe bidirectional alignment failures"
[^c5]: arxiv-2512-00552 — "but incoherent reverse explanations"
[^c6]: arxiv-2512-00552 — "empirical findings are based on a single 600M-parameter"
