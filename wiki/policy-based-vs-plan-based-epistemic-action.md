---
description: "Under stochastic transitions, policy-based selection that conditions on future observations visits an information cue more reliably than plan-based selection fixed in advance."
aliases: ["policy-based active inference outperforms plan-based", "reactivity advantage in active inference"]
sources: ["nuijten-2026"]
---
# Policy-based beats plan-based epistemic action under stochastic transitions

> Deciding whether to seek information by scoring a fixed sequence of
> future actions in advance systematically undervalues that information,
> once the environment can react to what the agent does next.

## Definition / Mechanism

Nuijten, van de Laar & de Vries (2026) compare, on a
stochastic "Reactivity Maze" (a latent context parameter is revealed only
by visiting an information cue, and the environment's later dynamics react
to the agent's behavior), a **policy-based** variant of their expected-free-energy
objective — `Factive`, which maintains a joint posterior over states and
actions and can therefore condition its later choices on what it will
observe — against a **plan-based** variant — Standard EFE planning, which
scores one fixed action sequence before observing anything. Policy-based
methods that maintain a joint posterior over states and actions (`Factive`,
Sophisticated Inference) outperform plan-based methods (Standard EFE
planning) in stochastic environments, because they can anticipate their own
future reactivity, making information-gathering consistently valuable and
leading to reliable cue visits.[^c1]

The gap is quantitative: only Factive and Sophisticated Inference
consistently seek information (100% cue visit rate); Standard EFE planning
visits the cue in only 66% of episodes, illustrating the limitation of
plan-based methods — because plan-based evaluation cannot anticipate that
the agent will get to react to the cue observation, it undervalues
information-gathering and prefers the safe option in roughly a third of
cases.[^c2]

## Why it matters

For stall 2, this is a mechanism-level reason to prefer an *adaptive*
selection rule over a *precomputed* one specifically when the environment
(or the answerer) can respond to the asker's next move: a rule that
evaluates "ask now, then react to whatever comes back" is undervalued by
any scheme that must commit to the whole future sequence before seeing an
answer. It is the active-inference-specific instance of the same
structural point [[causal-control-advantage]] makes for multihypothesis
sensing: adaptivity's advantage over a fixed schedule appears once the
environment carries more structure than the simplest two-branch case, not
automatically.

## Transfer

| | |
|---|---|
| **Home field** | Active inference: Bayesian planning over a generative model of future states and observations, compared as fixed plans vs. policies |
| **Here** | An asking agent choosing whether to gather information, where "plan-based" means committing to a question sequence before any answer and "policy-based" means conditioning the next question on the answer just received |
| **What survives** | The qualitative mechanism — evaluating a fixed sequence in advance cannot credit information the agent has not yet received, so it undervalues information-seeking whenever the environment reacts to the agent's actions |
| **What does not** | The specific 66%-vs-100% cue-visit numbers, tied to one maze's stochastic transition structure; and the claim itself, which the paper's own DoorKey environment shows can vanish (equal 89% success for both) when the task has no reactive latent cue to discover |

## Limits

- Established on one stochastic environment (the Reactivity Maze, 200
  episodes) plus a corroborating deterministic T-maze; the paper's own
  MiniGrid DoorKey result shows the advantage disappears when the task is
  spatial navigation without a reactive cue, so "stochastic transitions"
  alone is not sufficient — the environment must also reward anticipating
  its own reaction to the agent.
- "Sophisticated Inference" (a policy-based baseline using recursive
  belief modeling) matches Factive's qualitative advantage but not its
  success rate (94% vs 100%), so the advantage is not unique to one
  implementation of policy-based inference, but its size is
  implementation-dependent.

## Related

[[efe-planning-as-variational-inference]] · [[causal-control-advantage]] · [[active-inference-context-acquisition]] · [[optimal-decision-tree]]

[^c1]: nuijten-2026 — "policy-based methods that maintain a joint posterior over states and actions (Factive , Sophisticated Inference) outperform plan-based methods (Standard EFE planning) in stochastic environments, because they can anticipate their own future reactivity, making information-gathering consistently valuable and leading to reliable cue visits."
[^c2]: nuijten-2026 — "Only Factive and Sophisticated Inference consistently seek information (100% cue visit rate) and achieve near-optimal reward."
