---
description: "A GRPO reward that pays partial credit for an explicit abstention format and full credit only when a verifier judges the post-refusal clarification content correct against a reference."
aliases: ["clarification-aware RLVR reward", "refusal-with-clarification reward", "Abstain-R1 reward"]
sources: ["arxiv-2604-17073"]
---
# Post-refusal clarification reward

> Reward the refusal, then reward — separately, and only conditionally —
> whether what follows the refusal actually names the missing piece.

## Definition / Mechanism

Zhai, Liang & Kang (2026) train Abstain-R1, a 3B model,
with a GRPO reward that treats "abstain" and "abstain usefully" as two
gated stages rather than one blended score. For unanswerable queries —
questions that are semantically clear but lack a uniquely resolvable
answer from the given information (missing conditions, false premises,
known-unknowns) — the reward is built as: "we define a clarification-aware
RLVR reward that assigns a base reward for following a strict abstention
format, verified by rule-based checks, and an additional reward when the
clarification is semantically aligned with the reference clarification."[^c1]

The abstention format is checked mechanically (the response must box "I
don't know"); the clarification content is not — checking that a free-text
explanation names the actual missing information has no rule-based test,
so a separate model does the checking: "We employ a lightweight verifier
language model V that is trained to judge whether the model's clarification
matches a reference clarification." The verifier compares the model's
extracted clarification span against a reference clarification for the same
query and returns Correct/Incorrect; a strict 3B verifier (xVerify-3B-Ia) is
used during training to resist reward hacking, and a stronger model (o4-mini)
is used only for offline evaluation.

The two checks gate sequentially, not additively: 0.3 reward for the format
alone, rising to 1.0 only when the verifier also passes the content, and 0
if the format check fails outright. "This design ensures that for
unanswerable queries, the model receives non-zero reward only when it
abstains explicitly, and it receives the full reward only when its
post-refusal clarification aligns with the expected missing information."[^c3]
A separate, answerable-side term penalizes abstaining on questions that are
in fact solvable, so the two rewards jointly discourage both hallucinating
on unanswerable queries and habitually refusing answerable ones.

## Why it matters

Prior RL-based abstention training rewards the refusal act itself (a
generic "I don't know") or asks for a follow-up question without checking
whether it identifies anything, so a model can learn to always refuse, or
to refuse and then emit a plausible-sounding but uninformative follow-up,
and still collect reward. Gating the second, larger reward increment on a
verifier's judgment of the clarification's content forces the two failure
modes apart in training. Against the Qwen2.5 3B Instruct base, the trained
model raises refusal on unanswerable queries from 9.4% to 68.1% and
correct-clarification-given-refusal from 6.4% to 80.9%, while answerable
accuracy improves rather than degrades (48.8% → 57.2%): "Its gains are
reflected not only in refusal correctness, but also in clarification
quality and consistency, indicating that the model learns to abstain more
reliably and to provide more useful post-refusal clarifications." The
gains transfer to two unseen benchmarks (Abstain-QA, SelfAware), and a 3B
model trained this way matches or exceeds 671B systems (DeepSeek-V3,
DeepSeek-R1) on the refusal and clarification metrics, which the authors
read as evidence that calibrated abstention with useful content is a
trainable objective, not an emergent property of scale.

## Limits

- An ablation isolates the components: "The w/o Uans variant shows that
  unanswerable training data is essential for abstention: removing it
  increases answerable accuracy but largely eliminates the model's ability
  to refuse and clarify unanswerable queries. Removing the clarification
  reward, by contrast, mainly reduces clarification quality while leaving
  refusal relatively strong." — the two reward terms are not
  redundant, but this also means the clarification term alone does not
  induce abstention; both unanswerable data and the refusal-format reward
  are load-bearing.
- The trade-off is non-monotonic and hand-tuned, not solved: "As the
  clarification reward changes, performance does not improve
  monotonically. Instead, the best balance appears at an intermediate
  value." The reported weighting (0.3 / 0.7) is the point the authors
  found best on this setup; nothing in the mechanism derives it, and it
  would need re-sweeping for another domain or model scale.
- Single 3B backbone (Qwen2.5 3B Instruct), single domain mix (math and
  QA-style unanswerable/answerable pairs); whether the verifier's
  semantic-alignment judgment generalizes to open-ended, non-factual
  clarifications is untested here.
- The training-time verifier (xVerify-3B-Ia) and the evaluation-time judge
  (o4-mini) disagree in principle — no cross-check reports how often the
  weaker training verifier's Correct/Incorrect calls would flip under the
  stronger judge, so some fraction of the reward signal is unverified
  against the metric the paper reports results in.

## Related

[[savor-calibration-abstention-reward]] · [[rlvr-answering-bias]] ·
[[calibration-aware-policy-optimization]] ·
[[decoupled-claim-calibration-training]] · [[abstention]]

[^c1]: arxiv-2604-17073 — "Specifically, we define a clarification-aware RLVR reward that assigns a base reward for following a strict abstention format, verified by rule-based checks, and an additional reward when the clarification is semantically aligned with the reference clarification."
[^c3]: arxiv-2604-17073 — "This design ensures that for unanswerable queries, the model receives non-zero reward only when it abstains explicitly, and it receives the full reward only when its post-refusal clarification aligns with the expected missing information."
