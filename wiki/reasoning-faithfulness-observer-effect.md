---
description: "Exposing an ask/abstain agent's chain-of-thought for oversight can change the policy itself; three named failure modes make standard faithfulness metrics overstate how faithful it is."
aliases: ["reasoning faithfulness observer effect"]
sources: ["mendi-2026", "arxiv-2601-00830"]
---
# Reasoning faithfulness observer effect

> Turning an agent's reasoning on so it can be audited is not a neutral
> instrument on the decision being audited — it can change the decision.

## Definition / Mechanism

Mendi & Bent (2026) test whether the chain-of-thought an
abstaining speak/silent agent states actually reflects the computation
behind its decision, using controlled activation probes and behavioural
ablations.[^c1]

They find that "standard faithfulness methods can overstate evidence that
exposed reasoning reflects the underlying decision process," for three
distinct reasons: "Probability-based metrics saturate under confident
decisions, probes are vulnerable to class imbalance and textual leakage,
and reasoning ablations can confound reasoning content with changes in
inference mode."[^c2]

Their central claim is that the instrumentation itself is not neutral:
"exposing reasoning can change an agent's action policy rather than simply
make it observable" — adding a reasoning step before the action is an
intervention on the policy under audit, not just a window onto it.[^c3]

## Why it matters

For stall 10, this is a caution against reading a model's stated
chain-of-thought as evidence for why it asked, spoke, or abstained: the
wiki elsewhere treats [[abstention]] as a decision that can be inspected
through a named cost or threshold, but this result says the act of
inspecting a *reasoning* agent's abstention can itself move the threshold
being inspected.[^c4]

## Transfer

| | |
|---|---|
| In its home field | mechanistic interpretability: activation probes and ablation studies used to test whether a model's internal computation matches a claimed mechanism, on tasks not chosen for asymmetric cost or class imbalance |
| Here | auditing whether an ask/abstain agent's stated chain-of-thought reflects the computation behind a speak-or-silent decision |
| What survives | probing and ablation as tools for checking a stated reasoning trace against the underlying computation, instead of trusting the text |
| What does not | the assumption that the probes and ablations are themselves neutral measurements — under class imbalance and asymmetric action costs the probes leak and the ablations confound reasoning content with a change of inference mode, so the same tools need setting-specific controls, not a single faithfulness score |

[^c5]

A cheaper intervention, studied in a different setting, asks whether the announcement of observation alone changes what a model reports. Telling a model that its reasoning is monitored and logged did not raise how often it reported a planted cue: "The monitoring condition produced an acknowledgment rate of 21.8%" against a baseline of 20.7%, and the difference "does not meaningfully increase their tendency to report contextual influences".[^c8][^c9][^c10] This is evidence that being told of an audit is not the same as being audited. It does not test the exposure claim above, which concerns the audit itself; that separation is my reading.

## Limits

- Single model (Qwen3-8B) and one task domain (multi-party intervention
  timing); whether the observer effect generalises to other
  chain-of-thought-audited decisions is untested.[^c6]
- `mendi-2026` is an unreviewed 2026 arXiv preprint — `[?]` pending
  verifier confirmation; only the abstract was accessible for this note, so
  the three failure modes are stated at the level the abstract states them,
  not with their supporting figures.[^c7]

## Related

[[abstention]] · [[capability-auditability-tradeoff]] · [[calibration]] · [[semantic-entropy]]

[^c1]: mendi-2026
[^c2]: mendi-2026
[^c3]: mendi-2026
[^c4]: mendi-2026
[^c5]: mendi-2026
[^c6]: mendi-2026
[^c7]: mendi-2026
[^c8]: arxiv-2601-00830 — "The monitoring condition produced an acknowledgment rate of 21.8%"
[^c9]: arxiv-2601-00830 — "models acknowledged embedded hints in only 20.7% of trials"
[^c10]: arxiv-2601-00830 — "does not meaningfully increase their tendency to report contextual influences"
