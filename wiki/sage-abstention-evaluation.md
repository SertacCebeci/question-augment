---
description: "SAGE compiles a task-oriented dialogue agent's workflow spec and per-turn state diff into atomic criteria, verifies each by a cost-ordered cascade, and lets any stage abstain instead of guessing."
aliases: ["SAGE", "State-Grounded Abstention-Aware Evaluation", "criterion-cascade evaluation"]
sources: ["khoury-2026"]
---
# SAGE: state-grounded, abstention-aware evaluation

> Judge a dialogue turn by compiling it into many small, independently
> decidable questions instead of one holistic rating — and let each question
> refuse to answer rather than be forced into true or false.

## Definition / Mechanism

Khoury, Lin & Mishra (2026) define a workflow specification
$W=(S,F,\prec,O)$ — a schema, required fields with a legal ordering, and an
outcome predicate — and a per-turn state diff $\Delta_t$. A **compiler**
turns $(W, h_{<t}, u_t, a_t, s_{t-1}, s_t)$ into a list of atomic criteria,
each a (type, arguments, evidence-span) triple checking one of four
workflow-failure classes: ignored user value, wrong next field, premature
confirmation, unsupported value.[^c1]

Each criterion is routed through a three-stage cascade ordered by cost: S1
deterministic rules over the schema and state diff (zero LLM cost, abstains
when the schema underdetermines the check); S2 a pretrained NLI encoder with
a confidence-gated margin that abstains below threshold $\tau$; S3 an
optional focused single-criterion LLM call for the open-class residual.
"Every verifier returns true, false, or abstain, and abstentions propagate
up the cascade rather than being coerced into decisions." The zero-paid-LLM
configuration (compiler + S1 + S2) is named **SAGE-Core**; adding S3 is
**SAGE-LLM**.[^c2]

A turn-level verdict is a simple election over its criteria: failure if any
criterion is true, acceptable only if every compiled criterion is decided
and false, and otherwise — no criterion true but at least one abstain —
**undecided**.[^c3]

Across four benchmark slices (MultiWOZ, Schema-Guided Dialogue, ABCD),
SAGE-Core decides 81–91% of criteria at zero paid LLM cost, and "no
evaluated LLM-as-a-judge baseline...significantly exceeds SAGE-Core on any
slice," including a state-aware GPT-4.1 G-Eval judge costing $4.7–8.0 per
1,000 turns.[^c4]

## Why it matters

It replaces a single holistic acceptability score with many independently
verifiable, typed questions, each cheap enough to answer symbolically most
of the time — and it treats "abstain" as a legitimate output of the
*judge*, not only of the agent being judged, propagating uncertainty
upward instead of forcing a decision that costs an LLM call or a guess.

## Transfer

| | |
|---|---|
| In its home field | selective classification: one predictor $f$, one selector $g$, a single risk–coverage tradeoff over i.i.d. test points ([[abstention]]) |
| Here | many parallel, independently-scoped atomic criteria per turn, each with its own decision stage, aggregated by an election rule rather than a calibrated threshold |
| What survives | abstain as a first-class third output rather than a forced binary; cost-ordered routing (cheapest stage first, escalate only on abstention) |
| What does not | a single risk–coverage curve or a coverage guarantee — SAGE's "undecided" is a majority-style aggregate over many local abstentions, not one calibrated selector with a provable risk bound |

[^c5]

## Limits

- All headline benchmarks use **injected** failures, not naturally occurring
  ones; for three of the four classes the injection operator shares a
  predicate with the S1 symbolic check, so SAGE partly "recovers failures of
  the form it is designed to detect" — the authors call this "partial
  symbolic circularity."[^c6]
- SAGE presupposes a workflow specification with a schema and legal
  ordering; the paper states it "is unsuited to open-ended chat."[^c7]
- Zero-LLM operation (SAGE-Core) is reported as matching or exceeding the
  full cascade (SAGE-LLM) on the tested slices, but this is an ablation
  result on three benchmarks, not a general claim that S3 is never needed.

## Related

[[abstention]] · [[semantic-entropy]] · [[clarification-benchmarks]] · [[calibration]]

[^c1]: khoury-2026
[^c2]: khoury-2026 — "Every verifier returns true, false, or abstain, and abstentions propagate up the cascade rather than being coerced into decisions."
[^c3]: khoury-2026 — "predict failure if any criterion is true; predict acceptable only if every compiled criterion is decided and false; otherwise—no criterion true but at least one abstain— mark the turn undecided."
[^c4]: khoury-2026 — "Its recommended operating point, SAGE-Core, decides 81–91% of criteria with only the compiler, symbolic rules, and on-device encoders—at zero paid LLM cost"
[^c5]: khoury-2026 — "Every verifier returns true, false, or abstain, and abstentions propagate up the cascade rather than being coerced into decisions."
[^c6]: khoury-2026
[^c7]: khoury-2026 — "SAGE requires a workflow specification and is unsuited to open-ended chat."
