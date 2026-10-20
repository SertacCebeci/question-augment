---
description: "LLM agents cooperating on a shared task spontaneously ask clarifying questions without explicit training, at model-dependent rates that peak early in a session."
aliases: ["clarification behavior (Shaji et al. 2026)", "emergent collaborative clarification"]
sources: ["shaji-2026"]
---
# Emergent clarification behavior

> Embodied LLM agents cooperating on a color-matching task spontaneously ask
> clarifying questions — without being trained to — but how often depends
> sharply on the model, and within a session it peaks early.

## Definition / Mechanism

Shaji et al. (2026) define five behaviors as indicators that a collaborating
agent holds an emergent model of its partner's mental state: perspective-taking,
collaborator-aware planning, introspection, theory of mind, and clarification.
Clarification is "an agent demonstrating uncertainty about the collaborator,
the task, or the environment, and actively seeking clarification or additional
information to reduce [[efe-planning-as-variational-inference|ambiguity]]."[^c1]

Behaviors are detected by an LLM judge reading a sliding window of the
interaction transcript; judge output is scored against a human-annotated
subset with Cohen's κ, and — because no single configuration performs best
for every behavior — "we evaluate multiple judge configurations with
different judge LLMs and window parameters ... and select the configuration
with the highest aggregated kappa score ... for that behavior."[^c2]

Across three foundation models embodied as agents in agent-agent and
human-agent color-matching sessions, clarification behavior appears without
any model having been explicitly trained to produce it, and its rate
differs sharply by model: "The MiniMaxAI/MiniMax-M2 model demonstrates
significantly lower occurrence rates of theory-of-mind, perspective-taking,
collaborator-aware planning, and clarification behaviors compared to other
models," while "The Qwen/Qwen3-Coder-480B-A35B-Instruct model exhibits the
highest occurrence rates of clarification and collaborator-aware planning
behaviors."[^c3]

Clarification is also one of the less frequent of the five behaviors
overall — "Clarification behavior occurs less frequently, typically when
agents recognize uncertainty in their understanding of the task or
collaborator" — and it front-loads within a session: "Clarification shows a
peak at the beginning of tasks. This can be because the agents ask
clarifying questions to understand the task as well as the capabilities of
their collaborators."[^c4]

## Known as

| Field | Name there | Exact/Close |
|---|---|---|
| Human-AI collaboration (Shaji et al. 2026) | clarification behavior | exact |
| This wiki | emergent collaborative clarification | close |

## Why it matters

This is a measurement, not a design: it reports that the disposition to ask
exists unprompted in current models and is unevenly distributed by model and
time-localized within a session, which is a boundary condition for anyone
using an LLM agent's spontaneous [[query-clarification-rate|clarification rate]] as a signal — the rate
says as much about which model and which point in the interaction as about
the ambiguity actually present.

## Limits

The claim rests on one task family (a 2D color-matching game with a fixed
tool set), three foundation models, and one behavior-detection pipeline
whose human-agreement baseline is a single author's manual annotation of a
session subset; the paper selects a different judge configuration per
behavior type to maximize agreement, so the reported clarification rate is
already the best-case detector for that behavior, not a fixed instrument
applied uniformly across behaviors. No causal account is given for why
clarification is rarer than the other four behaviors or why it front-loads
— both are offered as plausible readings, not tested claims.

## Related

[[clarification-request]] · [[clarification-benchmarks]] · [[semantic-entropy]] · [[value-of-information]]

[^c1]: shaji-2026 — "Clarification involves an agent demonstrating uncertainty about the collaborator, the task, or the environment, and actively seeking clarification or additional information to reduce ambiguity."
[^c2]: shaji-2026 — "For each behavior type, we evaluate multiple judge configurations with different judge LLMs and window parameters (in Equation 1), and select the configuration with the highest aggregated kappa score (using Equation 3) for that behavior."
[^c3]: shaji-2026 — "The MiniMaxAI/MiniMax-M2 model demonstrates significantly lower occurrence rates of theory-of-mind, perspective-taking, collaborator-aware planning, and clarification behaviors compared to other models."
[^c4]: shaji-2026 — "Clarification behavior occurs less frequently, typically when agents recognize uncertainty in their understanding of the task or collaborator."
