---
description: "Appending a fixed 'Wait, we need to reconsider' cue to a second pass raised MATH-500 accuracy 32.2% to 40.6%; gains concentrate where first-pass entropy is high."
aliases: ["forced Aha", "triggered reconsideration", "extrinsic shift under high entropy"]
sources: ["doi-10-48550-arxiv-2601-00514"]
---
# Entropy-gated forced reconsideration

Spontaneous mid-trace shifts do not help ([[spontaneous-reasoning-shift-illusion]]), yet reconsideration can be supplied from outside. For each question the model gives a baseline completion (Pass 1), then is re-queried with identical decoding parameters plus an appended cue such as "Wait, we need to reconsider. Let's think this through step by step." (Pass 2).[^c1] Uncertainty is token-level Shannon [[entropy]] averaged over the think and answer segments; instances are split into the top 20% of Pass 1 entropy within domain (high) and the bottom 80% (low).[^c2]

## What was measured

Paired over checkpoints and temperatures, Math rose "(0.322 → 0.406; +8.41pp)", crosswords by +0.45pp, and Rush Hour by +0.01pp, negligible because of its near-zero base rate.[^c3] The gain is not random flipping on Math: "50,574 wrong→right vs. 23,500 right→wrong"; on crosswords wins and losses are near balanced (5,380 vs. 5,004).[^c4] The paper reports the gains are amplified in the high-entropy tail, and that the effect is robust to three lexically different cues.[^c5] The authors' conclusion is that uncertainty can be converted into productive reflection when the trigger is external.[^c6]

Conceptual point: the same act, reconsidering, is useless as an emergent behaviour yet useful as an imposed one; what matters is when and why it is invoked, with entropy as the gate.

## Limits

- Pass 2 is an extra generation, so the comparison is not compute-matched; the paper adds a control for the act of prompting itself (App. B.5) that I did not read in detail.
- Gains are domain-dependent: large on Math, tiny on crosswords, nil on Rush Hour.
- The 20% entropy cut is one choice; the high-entropy amplification figures (Table 29) were not read, so its size is unverified here.
- Small GRPO-tuned models, not frontier reasoners.

## Related

- [[spontaneous-reasoning-shift-illusion]] — the null finding this intervention contrasts with
- [[chain-entropy-abstention-gate]] — another entropy-based gate, abstaining instead of retrying
- [[entropy-threshold-clarification-trigger]] — entropy as a trigger for a second action
- [[placebo-controlled-retry-evaluation]] — how to separate a retry's effect from the act of retrying

[^c1]: doi-10-48550-arxiv-2601-00514 — "Wait, we need to reconsider. Let’s think"
[^c2]: doi-10-48550-arxiv-2601-00514 — "high-entropy (top 20% within domain) and"
[^c3]: doi-10-48550-arxiv-2601-00514 — "(0.322 → 0.406; +8.41pp) and a small gain on"
[^c4]: doi-10-48550-arxiv-2601-00514 — "(50,574 wrong→right vs. 23,500 right→wrong),"
[^c5]: doi-10-48550-arxiv-2601-00514 — "these gains are amplified on high-entropy instances"
[^c6]: doi-10-48550-arxiv-2601-00514 — "we demonstrate that uncertainty can be converted"
