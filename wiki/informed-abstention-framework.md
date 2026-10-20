---
description: "A precondition-aware pause that blocks an agent's next tool call, names the unmet specification, verification or authority gap, and routes to a bounded recovery action."
aliases: ["Informed Abstention Framework", "precondition-aware pause"]
sources: ["ojewale-2026", "arxiv-2601-00588"]
---
# Informed abstention framework

> Abstention is not the endpoint: a good pause is traceable to one of
> three named gaps and routes to a bounded [[recovery-postulate|recovery]] action, not a stop.

## Definition / Mechanism

Ojewale & Venkatasubramanian (2026) define informed
abstention as a structured pause inside an agent's tool-calling loop with
three properties: "It is precondition-aware: the pause is triggered by a
specific identifiable condition such as a missing required input, an
unverifiable state, or an absent authorization." "It is functional: the
pause blocks the next tool call but does not terminate the task... it
routes the interaction to one of three concrete recovery actions, covering
clarification, bounded verification, or handoff." "It is traceable: the
pause generates a structured record explaining what condition was unmet,
what recovery action was taken, and what the outcome was."[^c1]

Three gap types trigger it: a **specification gap** — "the agent is about
to invoke an operation without the minimum information needed for a well
formed and safe call"; a **verification gap** — "the agent cannot confirm
something it needs to know before taking the next step"; and an
**authority gap** — "the next step would create a real commitment or make
a high impact change, but the user has not clearly approved that exact
step." Each routes respectively to targeted clarification, bounded
re-query, or a commitment pause requesting explicit approval.[^c2]

Evaluation needs three metrics reported jointly: Safety Rate (fraction of
hazardous scenarios blocked), Usability Rate (fraction of safe scenarios
executed without friction) and Informed Refusal Rate (fraction of blocks
that named the specific unmet precondition) — "SR, UR, and IRR must be
reported as a joint triple since SR misses over-refusal, UR misses
under-refusal, and both miss the quality of the stop."[^c3]

The same measurement point appears in chat-level safety. CSSBench reports unsafe compliance on malicious prompts beside over-refusal on borderline ones, and folds both into one composite error rate that "micro-averages errors" across the two query sets.[^c8] Its authors warn that a low attack success can be "aggressive rejection even on malicious queries."[^c9] The sections read do not compare the composite against the two rates reported separately, so the point rests on the authors' warning and is not a measured failure of the composite.

Implemented as a pre-execution hook outside the model's context window
(not a system-prompt instruction), the framework achieves "87.5–91%
hazardous-action blocking and 75–92% usability on authorized scenarios"
across 144 scenarios and seven model families, and "the safety–usability
tradeoff is tunable rather than fixed."[^c4]

Prompt-only instruction is measured as insufficient on its own: "GPT-4o
drops from 79.2% to 4.2% UR (−75pp); Claude Sonnet 4.6 falls from 25.0% to
4.2% and Opus 4.6 to 8.3%, declining to execute nearly every safe scenario
despite explicit user authorization... Prompt-Only therefore cannot be
solely relied upon as a deployment strategy."[^c5]

The authority-gap check is run by a guard model kept architecturally
separate from the planning agent: "if the guard runs inside the planning
agent's context, it can be manipulated by the same adversarial inputs that
compromise the planning agent."[^c6]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Agent-safety (Ojewale & Venkatasubramanian) | precondition-aware pause | exact — the abstract's own gloss for the same mechanism |

## Why it matters

This gives stall 2's "pause vs. proceed" decision a taxonomy instead of a
single confidence threshold: the reason to stop and ask is one of three
named, checkable gaps (what is missing, what cannot be confirmed, what is
not authorized), each with its own bounded recovery, rather than a
scalar uncertainty score. It also names where the check must live —
outside the model's context, as a runtime hook — which a prompt-level
"ask when unsure" instruction cannot guarantee.[^c7]

## Transfer

| | |
|---|---|
| In its home field | selective prediction ([[abstention]]): a single-step classifier $(f,g)$ pair over i.i.d. inputs, abstaining when confidence falls below a threshold set by a named cost |
| Here | a multi-step, tool-calling agent where uncertainty compounds across steps and an abstention decision at step $k$ must account for actions already taken |
| What survives | the decomposition of "answer" from "whether to answer"; the requirement that the trigger be named, not just a confidence number; treating the pause as a structured, auditable decision rather than a silent default |
| What does not | selective risk and the risk–coverage curve (no per-instance ground truth or i.i.d. validation sample in a live agent run); Chow's threshold optimality; the paper is explicit that selective prediction's framing "does not transfer directly to agentic settings" |

## Limits

- The claim rests on the paper's own preliminary evaluation: 144
  scenarios (120 hazardous, 24 safe) built from 24 human-authored seeds
  adapted from four prior benchmarks and augmented by GPT-4o-mini —
  a synthetic scenario suite, not observed production traffic.
- The authority-gap guard's semantic-intent judgment is calibrated per
  deployment; the paper reports no universal threshold, only that the
  operating point is tunable.
- IRR under the Checkpoint condition is reported as a structural
  guarantee by construction (every block routes through a named check),
  not measured against an independent judge, unlike the Baseline and
  Prompt-Only IRR figures which are LLM-judge estimated.

## Related

[[abstention]] · [[compliance-bias]] · [[reversibility]] · [[value-of-information]] · [[stopping-rules]]

[^c1]: ojewale-2026 — "It is precondition-aware: the pause is triggered by a specific identifiable condition such as a missing required input, an unverifiable state, or an absent authorization."
[^c2]: ojewale-2026 — "A specification gap occurs when the agent is about to invoke an operation without the minimum information needed for a well formed and safe call."
[^c3]: ojewale-2026 — "SR, UR, and IRR must be reported as a joint triple since SR misses over-refusal, UR misses under-refusal, and both miss the quality of the stop."
[^c4]: ojewale-2026 — "runtime enforcement achieves 87.5–91% hazardous-action blocking and 75–92% usability on authorized scenarios, that compliance bias takes two structurally opposite forms across model families, and that the safety–usability tradeoff is tunable rather than fixed"
[^c5]: ojewale-2026 — "GPT-4o drops from 79.2% to 4.2% UR (−75pp); Claude Sonnet 4.6 falls from 25.0% to 4.2% and Opus 4.6 to 8.3%, declining to execute nearly every safe scenario despite explicit user authorization"
[^c6]: ojewale-2026
[^c7]: ojewale-2026
[^c8]: arxiv-2601-00588 — "a model on CSSBench: it micro-averages errors"
[^c9]: arxiv-2601-00588 — "aggressive rejection even on malicious queries."
