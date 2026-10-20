---
description: "When a model's checker copy shares weights and answer format with the judge, boosting verdict tokens also boosts checker tokens; a free-standing scalar readout breaks that shortcut."
aliases: ["interface decoupling", "token-copying shortcut in self-evaluation"]
sources: ["doi-10-48550-arxiv-2608-24231", "arxiv-2511-23092"]
---
# Self-reward interface decoupling

In RecurSE a trainable judge gives per-rule YES/NO verdicts (Pass 1) and a synchronized copy of the policy audits that reasoning (Pass 2) to give the only reward. If both passes use the same YES/NO format, the two passes are coupled at the surface: "policy updates that boost YES tokens on judge verdicts simultaneously alter emission probabilities in the synchronized checker, creating a degenerative token shortcut."[^c1] Since the weights are shared, any gradient update that reinforces YES in Pass 1 raises the chance Pass 2 emits YES too, so inflating YES across criteria directly maximizes the self-assigned reward.[^c2]

**The fix.** The checker emits a free-standing five-tier scalar score from 0 to 4 instead of indexed YES/NO tokens, "severing direct token copying while preserving positive capability transfer."[^c3] Empirically, identical YES/NO checking inflates the YES rate and the reward without accuracy gains, whereas the differentiated Final Score keeps the YES rate calibrated and turns reward growth into validation accuracy gains.[^c4]

The mechanism is a property of the reward interface, not of the rubric content. My inference: the general lesson is that a self-evaluator's output channel must not share tokens with the output it grades.

## Limits

- The authors do not claim zero bias, nor that scalar readouts preclude all coupling; the bias term is reduced, not removed.[^c5]
- Tested on rubric judging with one family of base models plus a Gemma replication; other formats are untested.
- Decoupling makes learning viable but does not say when to stop; see the stopping note.

## Related

- [[pairwise-advantage-validity-stopping]] — the companion monitor that bounds the loop
- [[judge-master-key-false-positives]] — judges accepting shallow cues
- [[reasoning-judge-adversarial-policy]] — policies gaming judge rewards
- [[llm-judge-biases]] — verdict-token bias as a judge bias
- [[wireheading]] — the coarser version of the same coupling: when the grade is the reward itself, inflation appears, and separating grade from reward mitigates it, though not fully.[^c6]

[^c1]: doi-10-48550-arxiv-2608-24231 — "policy updates that boost YES tokens on judge verdicts simultaneously alter emission probabilities in the synchronized checker"
[^c2]: doi-10-48550-arxiv-2608-24231 — "inflating YES tokens across criteria directly maximizes self-assigned rewards"
[^c3]: doi-10-48550-arxiv-2608-24231 — "severing direct token"
[^c4]: doi-10-48550-arxiv-2608-24231 — "Identical checking inflates YES rate."
[^c5]: doi-10-48550-arxiv-2608-24231 — "We do not claim b = 0"
[^c6]: arxiv-2511-23092 — "decoupling self-grades from the reward signal mitigates this inflation, models may still display lesser"
