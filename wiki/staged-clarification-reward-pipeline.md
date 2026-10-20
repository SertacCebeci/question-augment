---
description: "A four-stage RL reward — redundancy, diversity, answerability, relevance — gates each as a hard rejection before the next, matching GPT-5's success with 41% fewer questions."
aliases: ["CLARITI"]
sources: ["arxiv-2604-14624", "arxiv-2512-07478"]
---
# Staged clarification reward pipeline

> Four cheap, decomposed reward checks, applied as sequential gates instead
> of one blended score, substitute for a task-success reward too expensive
> to compute at training scale.

## Definition / Mechanism

Vijayvargiya, Viswanathan & Neubig (2026) train CLARITI,
an 8B clarification module (Qwen3 8B, SFT then GRPO), to ask single-turn
clarifying questions on underspecified SWE issues. Running full agent
trajectories (up to 30 steps) as a reward signal is computationally
intractable per training step and gives no decomposable signal for *why* a
clarification helped or failed, so the reward is built from four intrinsic,
cheaply-judged properties instead, applied as sequential rejection gates:
"Generated clarification sets flow through four sequential stages: (1)
Non-Redundancy filters generations with high number of questions answerable
from the underspecified issue (threshold r ≥ 0.5), (2) Diversity filters
generations with generic questions similar across different issues
(threshold r ≥ 0.5), (3) Answerability scores whether users can answer
questions in the generation from the full issue, and (4) Task Relevance
classifies questions in the generation into information categories weighted
by empirical impact (RQ1)."[^c1]

The ordering is load-bearing, not incidental: "candidates failing a stage
receive zero reward and are not evaluated in subsequent stages. This
progressive structure prioritizes simpler constraints before refining
higher-level behavior and critically prevents each reward component from
being gamed in isolation by earlier, easier-to-satisfy objectives."[^c2]
Non-redundancy must precede answerability because a redundant question
(already answered in the issue) trivially scores as answerable without any
genuine information-seeking; diversity must precede answerability because a
generic, reusable question template can be "answerable" across many issues
without being issue-specific. Answerability in turn precedes task
relevance, keyed to the impact hierarchy in
[[information-need-impact-hierarchy]] and phrased per the strategies in
[[answerable-clarification-strategies]]. The four scores are then weighted
equally: $r_\text{final} = 0.25(r_\text{redundancy} + r_\text{diversity} +
r_\text{answerability} + r_\text{relevance})$, judged by Qwen3 32B during
training and by GPT-5 at evaluation to avoid the model judging its own
training signal.

Trained on 1,000 RL instances built from SWE-Gym Raw underspecified
variants, the model reaches "36.8% task success while generating only 3.0
questions on average — 41% fewer than GPT-5 (5.1 questions) — recovering
88% of the fully specified performance." A stage-ablation confirms each
gate carries independent weight: "Removing Stage 3 (answerability) drops
performance to 24.4%, nearly identical to no clarification, confirming that
unanswerable questions actively degrade performance through context
pollution rather than being merely neutral. Removing Stage 4 (task
relevance) drops performance to 32.0%, validating the SHAP-weighted reward
as a meaningful driver of task success." SFT alone (no RL) reaches only
24.2% with the fewest questions (1.5), close to the no-clarification
baseline — the staged rewards, not supervised imitation, drive the gain.

## Why it matters

The pipeline is a general answer to a recurring problem in RL reward
design for compound behavior: when the true objective (task success) is
too expensive to evaluate per step, and a single blended proxy reward is
gameable component-by-component, ordering the proxies as sequential hard
gates — cheapest and most exploitable constraint first — removes the
incentive to satisfy a later stage by degenerately over-satisfying an
earlier one. A side effect reported qualitatively: on issues where every
candidate question would fail a gate, the trained model asks nothing,
which the authors read as abstention emerging from the reward structure
rather than an explicit taught policy.

## Limits

- Ablations remove one stage at a time; the paper does not report the
  interaction of removing two or more stages together, so the claim that
  "each stage is a necessary precondition for the next" is supported
  stage-by-stage, not jointly.
- The reward judge (Qwen3 32B) differs from the evaluation judge (GPT-5) to
  reduce bias, but the training reward's own accuracy against a human
  judgment of redundancy/diversity/answerability/relevance is not
  separately measured — the four scores are trusted as judged, not
  verified.
- "The model struggles when underspecification requires deep code
  comprehension to detect — it can identify surface-level gaps but cannot
  bridge from issue symptoms to underlying implementation concepts as
  reliably as GPT-5." — unverified beyond this qualitative comparison.
- Single domain (SWE-Bench-style issues), single base model (Qwen3 8B);
  the pipeline's four stages are specific to this task's information
  taxonomy and would need re-deriving (a new RQ1/RQ2 pass) for another
  domain.

- A close relative is progressive reward shaping in agentic tool-use QA (Su et al.). It also orders its stages, from parseable tool calls to answer correctness, and states the aim as "with simple, fundamental rewards and progressively transition into more challenging criteria."[^c3] Where this pipeline zeroes every later stage on a failure, the PRS equations add stage terms under threshold indicators, so partial credit survives; this is my reading, since the text extraction garbles those equations. The two are therefore not the same gate: one a hard rejection, the other a cumulative dense score.

## Related

[[information-need-impact-hierarchy]] · [[answerable-clarification-strategies]]
· [[ask-f1-selective-escalation-metric]] · [[two-tiered-reward-architecture]]
· [[question-budgets]]

[^c1]: arxiv-2604-14624 — "Generated clarification sets flow through four sequential stages: (1) Non-Redundancy filters generations with high number of questions answerable from the underspecified issue (threshold r ≥ 0.5), (2) Diversity filters generations with generic questions similar across different issues (threshold r ≥ 0.5), (3) Answerability scores whether users can answer questions in the generation from the full issue, and (4) Task Relevance classifies questions in the generation into information categories weighted by empirical impact (RQ1)."
[^c3]: arxiv-2512-07478 — "with simple, fundamental rewards and progressively transition into more challenging criteria."
[^c2]: arxiv-2604-14624 — "candidates failing a stage receive zero reward and are not evaluated in subsequent stages. This progressive structure prioritizes simpler constraints before refining higher-level behavior and critically prevents each reward component from being gamed in isolation by earlier, easier-to-satisfy objectives."
