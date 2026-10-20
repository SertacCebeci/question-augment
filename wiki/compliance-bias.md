---
description: "Task-completion scoring, product metrics and RLHF training jointly reward an agent for proceeding under missing or unverified preconditions, so pausing to ask scores worse than guessing."
aliases: ["compliance bias"]
sources: ["ojewale-2026"]
---
# Compliance bias

> Under outcome-only scoring, the expected value of guessing is weakly
> better than asking — so an agent that proceeds without grounding is
> rewarded and one that pauses to ask is not.

## Definition / Mechanism

Ojewale & Venkatasubramanian (2026) name **compliance
bias**: benchmark scoring, product metrics and default deployment
configurations all reward an agent for proceeding even when it lacks the
inputs, evidence or authorization required to do so safely.[^c1]

They trace it to three layers. In evaluation: AgentBench's database
environment hashes only the final table state, so "an agent that guesses a
missing record ID and happens to produce the correct final state receives
the same score as one that verified the correct ID before acting, and the
scoring mechanism cannot distinguish between them."[^c2]

HAL's graders "assign the same score of zero to an agent that abstains and
to one that leaks a user's credit card," and the Agentic Benchmark
Checklist shows "a trivial empty-response agent scores 38% on τ-bench
(exceeding GPT-4o), because the grader accepts ground-truth matches
regardless of whether any reasoning occurred."[^c3]

In training: RLHF sycophancy is the same mechanism one step earlier —
"human raters tend to prefer confident, task-completing responses over
hedged or uncertain ones, and the reward model learns this preference."[^c4]

A 7-model, 144-scenario evaluation (Baseline condition, no abstention
policy) finds the bias is universal but not one behaviour: Llama 3.1 8B
scores the lowest Safety Rate (50.8%) paired with the highest Usability
Rate (91.7%) — proceeds readily, blocks hazards poorly — while Claude
Opus 4.6 inverts this (61.7% SR, 29.2% UR), "blocking authorized actions
roughly seven times out of ten even before any safety instruction is
applied." The authors conclude "proceed-always and refuse-always are both
miscalibrations relative to the ground truth of precondition-aware
action."[^c5]

## Why it matters

This is the answerer-side mirror of the asker's stopping problem: it names
*why* an agent under standard scoring does not pause to ask a clarifying
question or verify a precondition before an irreversible action, even when
[[abstention]] would be the theoretically correct move. It supplies a
measured incentive gradient — not just an observation that agents
sometimes act wrongly — with evidence that the failure sits in the metric,
not only in the model.[^c6]

## Limits

- The evaluation-incentive claim is argued from benchmark design (four
  cited benchmarks) plus one training-level mechanism (sycophancy in
  RLHF); it is not a controlled experiment isolating training from
  scoring as separate causes.
- The two-pole empirical result (Llama vs. Claude) comes from the paper's
  own 144-scenario, seven-model preliminary evaluation — the authors call
  it preliminary, and it is not yet replicated by an independent group.
- "Compliance" is measured here only for tool-using agentic settings with
  irreversible actions; the claim does not establish that the same
  incentive gradient exists in single-turn chatbot evaluation.

## Related

[[abstention]] · [[informed-abstention-framework]] · [[reversibility]] · [[bounded-rationality]]

[^c1]: ojewale-2026 — "Benchmark scoring, product metrics, and default deployment configurations all reward agents for proceeding even when they lack the inputs, evidence, or authorization required to do so safely. We call this phenomenon compliance bias."
[^c2]: ojewale-2026 — "an agent that guesses a missing record ID and happens to produce the correct final state receives the same score as one that verified the correct ID before acting, and the scoring mechanism cannot distinguish between them"
[^c3]: ojewale-2026
[^c4]: ojewale-2026 — "human raters tend to prefer confident, task-completing responses over hedged or uncertain ones, and the reward model learns this preference"
[^c5]: ojewale-2026 — "Llama 3.1 8B has the lowest Baseline SR (50.8%) paired with the highest UR (91.7%)"
[^c6]: ojewale-2026
