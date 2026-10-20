---
description: "Clarification value decays with trajectory position at a rate set by which information dimension is missing — goal value collapses by 10% of execution, input value persists to roughly 50%."
aliases: ["VOI decay curve", "forced-injection framework", "trajectory commitment model"]
sources: ["gulati-2026"]
---
# Clarification timing decay

> When an agent can ask, the value of asking is not constant over its trajectory: it decays with how much of the trajectory has already committed to a wrong assumption, and the decay's shape is set by which of four information dimensions (goal, input, constraint, context) is missing — so "which axis first" cannot be answered without also answering "by when."

## Definition / Mechanism
Gulati et al. (2026) inject ground-truth clarifications at controlled points (10/30/50/70/90% of an oracle-calibrated action budget) into 84 underspecified tasks across three agent benchmarks (MCP-Atlas, TheAgentCompany, SWE-Bench Pro) and four frontier models (GPT-5.2, Claude Sonnet 4.5, Gemini 3 Flash, DeepSeek V3.2), disabling the agent's own ask capability so the timing effect is isolated from the agent's decision to ask. They define commitment $C_d(t)\in[0,1]$, the fraction of actions up to time $t$ that causally depend on dimension $d$, and bound clarification value by the uncommitted remainder: "The value of clarification at time t is bounded by the recoverable portion: VOI_d(t) ≤ VOI_d(0) · (1 − C_d(t)), since committed actions cannot be undone."[^c1]

The measured decay is dimension-dependent, not simply "earlier is always better": "goal clarification loses nearly all value after 10% of execution (pass@3 drops from 0.78 to baseline), while input clarification retains value through roughly 50%." On MCP-Atlas, goal injection at 10% recovers near-oracle performance (pass@3 0.78 vs. oracle 0.80, no-clarification 0.40) and falls to the no-clarification baseline by 70%; input injection declines more gradually (0.46 at 10% to 0.25 at 90%, no-clarification 0.33, oracle 0.57).[^c2]

Cross-model Kendall's τ on which task variants benefit from early clarification is 0.78–0.87 among models sharing identical task coverage and exceeds 0.34 (p<0.01) across the full four-model panel, "support[ing] the interpretation that timing effects are predominantly task-intrinsic: the same variants benefit from early injection regardless of which model executes them."[^c3]

## Why it matters
It converts "when should an agent ask" from a single policy question into a per-dimension schedule: the optimal moment to query goal-level information is not the optimal moment to query input-level information, and a selection criterion (stall 2) that scores axes without a timing term will misrank a goal question that must be asked in the first 10% against an input question with a much longer window.

## Limits
The decay curves are an upper bound on information value, not a measured VOI: "forced injection disables ask_user while natural-ask enables it, so agents may plan differently when they know they cannot ask; the forced-injection VOI curves should be interpreted as upper bounds on information value." The strongest signal comes from one benchmark (MCP-Atlas, n=5–28 per dimension); TheAgentCompany shows floor effects that attenuate the goal and constraint signals, and the context dimension's combined sample (n=17) is stated by the authors as too small for a reliable timing conclusion. The study measures the demand side only — how much performance a correctly-timed answer buys — not whether or how an agent should detect that it needs to ask. The source is a 2026 arXiv preprint, not yet peer reviewed.[^c4]

## Related
[[value-of-information]] · [[expected-information-gain]] · [[bounded-rationality]] · [[reversibility]]

[^c1]: gulati-2026
[^c2]: gulati-2026 — "goal clarification loses nearly all value after 10% of execution (pass@3 drops from 0.78 to baseline), while input clarification retains value through roughly 50%"
[^c3]: gulati-2026 — "These results support the interpretation that timing effects are predominantly task-intrinsic: the same variants benefit from early injection regardless of which model executes them."
[^c4]: gulati-2026 — "A behavioral confound exists between protocols: forced injection disables ask_user while natural-ask enables it, so agents may plan differently when they know they cannot ask; the forced-injection VOI curves should be interpreted as upper bounds on information value."
