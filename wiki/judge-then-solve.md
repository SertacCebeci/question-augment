---
description: "A trajectory-level reasoning-control method that judges answerability before solving, then trains the commitment with a consistency-and-length RL reward."
aliases: ["Judge-Then-Solve", "JTS"]
sources: ["gu-2026", "arxiv-2512-16883"]
---
# Judge-Then-Solve (JTS)

> Instead of letting a reasoning model decide whether to abstain somewhere
> inside an open-ended chain of thought, make the commitment the first move
> and reward the rest of the trace for being consistent with it.

## Definition / Mechanism

Gu et al. (2026) restructure inference so answerability is a
gate, not an emergent property of the final token: "the model is required to
first examine whether the provided context contains sufficient information
to support a uniquely grounded answer," expressed in a fixed
`<answerability_judge>` block — Contextual Audit, Integrity Check, binary
Conclusion — before any solution-oriented reasoning; formally $z =
f_{\theta_{judge}}(x) \in \{\mathrm{ANSWERABLE}, \mathrm{UNANSWERABLE}\}$,
and $y = \bot$ if $z=\mathrm{UNANSWERABLE}$, else $y=f_{\theta_{solve}}(x)$.[^c1]

The judgment is trained in two stages: supervised warm-up on
judgment-formatted trajectories, then GRPO with a structured reward
$R = R_{format} + R_{consistency} + R_{task} + R_{length}$, where
$R_{consistency}$ penalizes any mismatch between the stated judgment $z$ and
an external judge's read of the final behaviour, and $R_{length}$ — bounded
to $[-0.1, 0.1]$ — rewards shorter trajectories only among the cases that
failed to abstain after detecting insufficiency, and longer ones only among
answerable cases the model got wrong.[^c2]

Against a base model and a plain-RL baseline trained on the same
missing-premise reward alone, JTS raises [[abstention|Abstention]]-at-Detection from 41.1%
(base) / 81.4% (plain RL) to 99.8% on DeepSeek-R1-Distill-Qwen-14B, and from
40.0% / 90.4% to 99.3% on Qwen3-30B-A3B-Thinking, while cutting average
response length on insufficient-information questions from ~2600–2800 tokens
to ~340–350.[^c3]

On well-defined (answerable) questions this is not free: JTS's answer rate
and correctness are slightly below the base model's (e.g. DeepSeek
correctness 92.4% vs. 99.4% for plain RL), though correctness-per-1000-tokens
improves (0.544→1.028 on DeepSeek) because responses are far shorter.[^c4]

## Why it matters

JTS is a concrete, trained mechanism for closing the
[[detection-to-abstention-gap]]: it targets exactly the translation step
between recognising a missing constraint and acting on that recognition,
rather than trying to improve detection itself. For the answerer's side of
the wiki (stall 10) it is a worked example of turning "commit or hedge" into
an explicit, separately-rewarded control decision made before generation
rather than an implicit property of it.

The same ordering, a decision placed before solving, appears in search agents, with a different target. AdaSearch (Lin et al., 2026) has the agent state explicitly whether its own knowledge suffices, then solve under a parametric prompt or a search prompt. The two are trained separately: problem solving first, under both prompts, and then the decision, on labels from the stage-1 policy's solve rate. The paper reports that joint optimisation "consistently underperforms" the staged version, "suggesting that" the two-stage approach is more effective.[^c5] Here the "no" branch is a search, not a refusal, so the gate decides which tool path to take rather than whether to answer at all (my inference). The score for such a gate is discussed in [[search-decision-f1]].

## Limits

- Evaluated on two reasoning models (14B dense, 30B MoE) and math/QA
  missing-premise data; the consistency reward depends on an external
  LLM-as-judge to score whether output text counts as "abstain," so JTS's
  reported gains are bounded by that judge's own accuracy.
- The conservativeness trade-off on well-defined questions (lower raw answer
  rate and correctness) is real, not merely a length artifact — the paper
  reports it as a genuine cost, not fully absorbed by the Corr./1K
  normalization.
- JTS treats abstention as a single terminal action (`⊥`) chosen once,
  before solving; it is not evaluated as, and does not by itself specify,
  the further behaviour of turning an UNANSWERABLE judgment into a
  clarifying question back to the user rather than a bare refusal.

## Related

[[detection-to-abstention-gap]] · [[recognition-refusal-dissociation]] · [[abstention]] · Commitment

[^c1]: gu-2026 — "the model is required to first examine whether the provided context contains sufficient information to support a uniquely grounded answer"
[^c2]: gu-2026 — "the shaping term is bounded by Rlength ∈ [−0.1, 0.1]"
[^c3]: gu-2026 — "On DeepSeek, JTS increases OAR to 88.5% and A@D to 99.8%. On Qwen, JTS reaches an OAR of 72.4% and an A@D of 99.3%."
[^c4]: gu-2026 — "although JTS slightly lowers raw answer rate and correctness, it produces more concise answers and improves correctness per generated token"
[^c5]: arxiv-2512-16883 — "AdaSearch-E2E consistently underperforms AdaSearch, suggesting that"
