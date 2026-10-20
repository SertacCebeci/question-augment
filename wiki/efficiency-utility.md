---
description: "A success-gated metric that discounts an agent trajectory for excess user-facing turns and tool calls beyond task-specific floors, the penalties fit from human pairwise preferences."
aliases: ["Efficiency Utility"]
sources: ["han-2026"]
---
# Efficiency Utility

> A metric that stops scoring a tool-using agent by success alone: a
> completed trajectory is discounted for how much dialogue and backend
> work it took beyond a task-specific floor, with the discount rates
> learned from which of two successful trajectories humans preferred.

## Definition / Mechanism

Han, Fang, Hou & Liu (2026) define, for a task $x$ and a
successful trajectory $\tau$, excess counts against task-specific
reference-effort floors $f_{tool}(x)$ and $f_{turn}(x)$:
$e_{tool}(\tau) = \max\{0, c_{tool}(\tau) - f_{tool}(x)\}$,
$e_{turn}(\tau) = \max\{0, c_{turn}(\tau) - f_{turn}(x)\}$, where
$c_{tool}$ counts backend tool invocations and $c_{turn}$ counts
assistant messages sent to the user.[^c1]

The metric is $U(\tau) = \mathrm{success}(\tau)\,\lambda_{tool}^{\,e_{tool}(\tau)}\,\lambda_{turn}^{\,e_{turn}(\tau)}$:
"success(τ) indicates whether τ passes the 3-LLM panel... A failed
trajectory scores zero; a successful one at both floors scores one;
each additional tool call or turn multiplicatively reduces the score."[^c2]

$\lambda_{tool}$ and $\lambda_{turn}$ are not hand-set. They are fit with
a Bradley–Terry paired-comparison model over same-task pairs of
already-successful trajectories, so annotators judge only relative
efficiency, never task success: "We fit this cost with a
Bradley–Terry paired-comparison model (Bradley and Terry, 1952)."[^c3]

## Why it matters

This gives asking a *priced* alternative to acting inside one scored
trajectory, on a real multi-turn tool-using agent (ridehailing dialogue):
a success-only score cannot separate the agent that finishes directly
from the one that reaches the same outcome after repeated clarification
or avoidable tool use, and Efficiency Utility is built specifically to
recover that difference without assuming the trade-off rate — it is
learned from paired human judgments, not a hand-picked cost.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Success weighted by Path Length (embodied navigation) | Efficiency Utility (tool-using dialogue agents) |
| What survives | success gate; task-relative reference floor; discount applied only to effort beyond that floor | same three, unchanged |
| What does not | a single path-length axis | replaced by two independently penalized axes (turns, tool calls) whose relative weight is not assumed but fit from human pairwise preference data |

"Efficiency Utility inherits its skeleton from Success weighted by Path
Length (Anderson et al., 2018): a success gate, a task-relative
reference floor, and a penalty only for effort beyond that floor."[^c4]

## Limits

- Calibrated on one benchmark and domain — 58 Chinese-language
  ridehailing tasks, 24 models — the fitted $\lambda_{tool}$,
  $\lambda_{turn}$ are this population's revealed trade-off, not a
  domain-independent constant.
- The tool-call axis has weak human agreement: held-out pairwise
  accuracy is only chance-level when two successful trajectories differ
  solely in tool-call count, so $\lambda_{tool}$ rests on a noisier
  signal than $\lambda_{turn}$.
- `han-2026` is `status: queued` in `wiki/meta/sources.json` — provisional,
  not yet verifier-confirmed. `[?]`

## Related

[[clarification-benchmarks]] · [[value-of-information]] · [[bounded-rationality]] · [[turn-tool-penalty-asymmetry]]

[^c1]: han-2026 — "etool (τ ) = max{0, ctool (τ ) − ftool (x)}, eturn (τ ) = max{0, cturn (τ ) − fturn (x)}."
[^c2]: han-2026 — "success(τ ) indicates whether τ passes the 3LLM panel (Section 3). A failed trajectory scores zero; a successful one at both floors scores one; each additional tool call or turn multiplicatively reduces the score."
[^c3]: han-2026 — "We fit this cost with a Bradley–Terry pairedcomparison model (Bradley and Terry, 1952)."
[^c4]: han-2026 — "Efficiency Utility inherits its skeleton from Success weighted by Path Length (Anderson et al., 2018): a success gate, a task-relative reference floor, and a penalty only for effort beyond that floor."
