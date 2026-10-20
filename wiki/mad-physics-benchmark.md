---
description: "LLM agents choosing what, when and how precisely to measure under a shared cost budget in altered-physics environments still make poorly-informed, sometimes out-of-bounds predictions."
aliases: ["MaD Physics", "Measuring and Discovering Physics"]
sources: ["jain-2026-physics"]
---
# MaD Physics benchmark

> A benchmark that forces an LLM agent to spend a single shared budget across
> **what** to measure, **when**, and **at what fidelity**, before it must
> infer an altered physical law from the resulting noisy data — isolating
> axis-selection-under-budget from static knowledge recall.

## Definition / Mechanism

Each trial places the agent in one of three physics environments (classical,
fluid, quantum mechanics), each with the standard law optionally "altered"
(e.g. anisotropic inertial mass, a modified gravity exponent) so the agent
cannot answer from memorized physics. The agent chooses a sequence of
observations $(t_k, o_k, \sigma_k)$ — measurement time, observation function,
noise scale (inverse fidelity) — each corrupted by Gaussian noise and each
charged a cost $C(o_k,\sigma_k)$ strictly increasing in fidelity, under a
total budget $B$: $\sum_k C(o_k,\sigma_k) \le B$. Once $B$ is exhausted or a
time limit $T_\text{max}$ is reached, the agent must predict the system's
state at a future query time from its collected observations alone.[^c1]

Four Gemini models (2.5 Flash Lite, 2.5 Flash, 2.5 Pro, 3 Flash) were run
with a minimal code-execution scaffold under two system prompts: a bare
*Base* prompt, and a *Strategy* prompt giving a structured procedure for
data collection explicitly inspired by [[bayesian-experimental-design|Bayesian experimental design]]. Larger
models did better, but even the strongest model (Gemini 3 Flash) produced
inaccurate predictions on unaltered physics, and the 2.5-generation models
produced predictions numerically out of the plausible range entirely — a
failure at planning-under-budget, not at physics knowledge, since the same
models are given the observations they themselves chose. The Strategy
prompt improved performance on many tasks over Base.[^c2]

## Why it matters

It gives stall 2 (which axis first) an instrument for measuring, rather than
assuming, whether an LLM agent's sequential choice of what-to-observe under
an explicit resource budget approaches informative selection: the benchmark's
headline result is that current frontier agents' structured exploration and
data-collection is the identified shortcoming, not model capacity alone,
and that supplying an explicit selection procedure (rather than better
knowledge) is what moved the number.

## Transfer

| | Bayesian experimental design (home field: statistics) | Here |
|---|---|---|
| What survives | the myopic loop of proposing a measurement, weighing cost against expected informativeness, updating on the result | the *Strategy* system prompt instructs the agent to follow exactly this loop in place of unstructured tool use |
| What does not | a guarantee the prompted procedure is executed as a probabilistic update, or a posterior over the altered law's form | the benchmark measures only prediction error after the fact, so it cannot certify the *Strategy*-prompted model is computing anything like an [[expected-information-gain]] score |

[^c3.1][^c3.2][^c3]

## Limits

The claim that agents fail specifically at *selection* under budget, rather
than at inference from data, rests on the paper's own framing (observations
are the agent's own choices, so any prediction error is at least partly a
selection failure) — the benchmark does not decompose error into a
selection component and an inference component, so the "shortcoming in
structured exploration" reading is the paper's interpretation of an
aggregate prediction-error number, not a directly measured selection metric.
Results are reported for Gemini models only; the authors note future work
should test other frontier models.

## Related

[[bayesian-experimental-design]] · [[expected-information-gain]] · [[value-of-information]] · [[clarification-benchmarks]]

[^c1]: jain-2026-physics — "In MaD Physics, the agent operates in a loop of measurement and prediction. It is allocated a fixed budget and must choose what to measure (e.g., which particle, which location), when to measure it, and with what fidelity (trading off cost for precision). Once the budget is exhausted, the agent must leverage its collected observations to infer the underlying dynamics and predict the future state of the system."
[^c2]: jain-2026-physics
[^c3.1]: jain-2026-physics — "Strategy provides a structured strategy inspired by Bayesian experimental design (Rainforth et al., 2024)."
[^c3.2]: jain-2026-physics — "In contrast to measuring the exact symbolic accuracy, which is standard in symbolic regression, MaD Physics focuses on measuring the prediction accuracy."
[^c3]: jain-2026-physics
