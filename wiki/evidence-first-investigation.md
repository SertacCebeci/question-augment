---
description: "An interactive diagnostic agent tracks a normalized probability over competing causes, sizes its question budget to estimated ambiguity, and stops once one cause clears a fixed confidence threshold."
aliases: ["Solution Investigator Agent", "SIA", "LLM-as-an-Investigator"]
sources: ["marozzo-2026"]
---
# Evidence-first investigation

> Turn a diagnostic assistant from a one-shot answerer into a hypothesis
> tracker: keep several candidate causes alive as a probability vector,
> spend a [[question-budgets|question budget]] sized to how ambiguous the case looks, and commit
> only when one candidate is far enough ahead.

## Definition / Mechanism

Marozzo & Liò (2026)'s Solution Investigator Agent (SIA)
separates semantic reasoning (the LLM) from deterministic control (state
management, stopping). Before asking anything, it estimates an [[efe-planning-as-variational-inference|ambiguity]]
score $a$ for the initial problem and sets a question budget $B = \min(B_{max},
B_{min}+a)$ — "the budget is dynamically adapted to the expected difficulty
of the case, allowing the agent to ask more questions when the problem is
ambiguous and fewer questions when the evidence is already sufficiently
clear."[^c1]

It then generates a set of candidate causes with a normalized probability
vector $\pi$, and after every user answer recomputes $\pi^{(t+1)}$ from the
full interaction history, keeping candidate names fixed so only their
plausibility moves. Each question is chosen to separate the currently most
competitive candidates rather than asked generically.[^c2]

Stopping is a fixed threshold on the tracked belief, not a question count:
"The investigation stops when the collected evidence makes one candidate
solution sufficiently stronger than the alternatives or when the question
budget is exhausted," formally $\max_i \pi_i \ge \tau$ — a rule the authors
say "prevents the agent from producing a final answer too early while also
avoiding endless questioning."[^c3]

Evaluated against direct-prompting and reasoning-only baselines across LLM
backbones on solved technical-forum threads, "the proposed approach
identifies the underlying problem more accurately than direct prompting and
reasoning-only baselines, while its evidence-first protocol provides a
practical mechanism for reducing user-induced conversational bias" — the
mechanism that produces the low [[user-driven-sycophancy]] rate measured for
the same system.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| dialogue-systems (Marozzo & Liò 2026) | Solution Investigator Agent, SIA | exact — the implemented system |
| dialogue-systems (Marozzo & Liò 2026) | LLM-as-an-Investigator | exact — the paper's name for the same methodology |

## Why it matters

For stall 7 (is $|W|$ small enough to stop), this is a concrete instance of
a **posterior-threshold stopping rule** applied to open-ended natural-
language dialogue rather than to a fixed hypothesis test: candidates are
LLM-generated text, not a closed enumerated set, and the "likelihood
update" is an LLM call rather than a computed [[likelihood-ratio|likelihood ratio]]. It couples
that stopping rule to a **budget that scales with estimated ambiguity**
before any evidence is collected — a stall-1/stall-7 coupling (how uncertain
the case looks sets how much stall-7 budget is available) that this wiki's
existing stopping notes do not address.

## Transfer

| | |
|---|---|
| **Home field** | sequential [[hypothesis-testing|hypothesis testing]] / decision theory: stop when accumulated evidence crosses a fixed confidence threshold on the leading hypothesis (the shape shared with [[sprt]] and posterior-threshold [[stopping-rules|stopping rules]] generally) — this wiki's structural reading, not a transfer the paper itself claims |
| **Here** | $\tau$ is applied to an LLM-maintained probability vector over free-text candidate causes, updated by an LLM call each turn rather than a calibrated likelihood ratio |
| **What survives** | the qualitative shape — stop early when one candidate pulls ahead, keep going while candidates are close, cap the budget so the loop always terminates |
| **What does not** | any error-rate guarantee. SPRT's threshold is set from declared false-accept/false-reject rates via a proven bound; $\tau$ here is a hyperparameter with no stated relation to a diagnostic accuracy or false-diagnosis rate, and the "probability" vector is an LLM's self-reported plausibility, not a quantity with a proven [[calibration]] property |

## Limits

- The claim that this reduces sycophancy rests on the same 30-case,
  two-model robustness test reported for [[user-driven-sycophancy]]; SIA
  itself is not run through that specific spontaneous-vs-prompted probe in
  the paper, only through the separate diagnostic-accuracy benchmark, so the
  causal link between the architecture and the low sycophancy rate is the
  paper's design argument, not a controlled ablation isolating the stopping
  rule from the budget or from the question-generation step.
- $\tau$, $B_{min}$, $B_{max}$ and the ambiguity score $a$ are hyperparameters
  the paper does not report tuning or sensitivity results for.
- The probability vector is produced by prompting an LLM to update
  plausibility scores; nothing here establishes that these scores are
  calibrated probabilities rather than a bounded-range self-report.
- `[?]` This is a June 2026 arXiv preprint, not yet confirmed at a
  peer-reviewed venue.

## Related

[[user-driven-sycophancy]] · [[sprt]] · [[question-budgets]] ·
[[value-of-information]] · [[clarification-benchmarks]]

[^c1]: marozzo-2026 — "the budget is dynamically adapted to the expected difficulty of the case, allowing the agent to ask more questions when the problem is ambiguous and fewer questions when the evidence is already sufficiently clear"
[^c2]: marozzo-2026 — "The agent is instructed to preserve the same candidate names and update only their probabilities."
[^c3]: marozzo-2026 — "The investigation stops when the collected evidence makes one candidate solution sufficiently stronger than the alternatives or when the question budget is exhausted."
[^c4]: marozzo-2026 — "The results show that the proposed approach identifies the underlying problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol provides a practical mechanism for reducing user-induced conversational bias."
