---
description: "In agentic software tasks, success tracked separating assumptions from verified facts and checking them against system state; open-loop 'code written means done' caused 52% of failures."
aliases: ["epistemic discipline", "open-loop execution failure", "closed-loop verification in agents"]
sources: ["arxiv-2601-08806"]
---
# Epistemic discipline in agent execution

APEX-SWE (Integration and Observability tasks for frontier coding agents) defines epistemic discipline as "an agent's ability to distinguish between assumptions and facts, and its willingness to verify the former before acting."[^c1] It is the authors' qualitative explanation of why some models score higher, not a manipulated variable.

## What was observed

Reviewing successful Integration runs, the authors say success "is not determined by raw coding capability" and that high performers often show a three-phase workflow: "systematic exploration, explicit specification extraction, and closed-loop verification."[^c2] Exploration came before action: "In 70.5% of passing trajectories, models explicitly read environment configuration files before attempting implementation, and 95.0% queried external APIs to discover available operations."[^c3]

The failure side is coded across all models. Insufficient Verification is the largest category: "Insufficient Verification accounts for 52% of failures, followed by Bad Environment Understanding (22%), Specification Non-Compliance (14%), and Execution Failure (12%)."[^c4] The dominant mode is open-loop execution, "where models assume code generation equals task completion."[^c5] Within it, 20% of signals are models that never run test scripts and 16% skip final verification. In one case a script reported three low-stock products when the true count was six; the model never compared its output with the required state.

Verification is also separate from asking the environment: failures included agents bypassing provided tools for raw HTTP calls and spending most of a trajectory on authentication errors, which is a failure to understand what the environment already offered (Bad Environment Understanding).

Efficiency pattern: successful runs used fewer episodes than unsuccessful ones (44.9 vs 59.6).[^c6] Fewer turns alone is not the signal, since the model with the fewest turns scored low (18.3%).

## Limits

- The link is qualitative and correlational: failure categories were assigned by reviewing trajectories, and no experiment forces verification on or off to test causation.
- "Epistemic discipline" is a label applied after the fact; no operational measure of it is given beyond failure-mode coding.
- Only coding and operations agents on 200 tasks and eleven models; the finding is for tool-using execution, not for question asking or answer calibration in dialogue.
- Mixing in other factors (model capability, thinking setting, tool-call malformation) is not controlled; the 12% execution failures are a separate cause.

## Related

- [[verification-aware-stopping]] — a retrieval agent stops only when evidence covers each needed claim; the same verify-before-finish idea in search
- [[verification-over-invention]] — verifying rather than generating content
- [[same-model-self-verification-conditional-confidence]] — self-verification by the same model, its limits
- [[solve-verify-detection-gap]] — gap between solving and detecting errors

[^c1]: arxiv-2601-08806 — "ability to distinguish between assumptions and facts, and its willingness to verify the former before acting"
[^c2]: arxiv-2601-08806 — "systematic exploration, explicit specification extraction, and closed-loop verification"
[^c3]: arxiv-2601-08806 — "In 70.5% of passing trajectories, models explicitly read environment configuration files before attempting implementation"
[^c4]: arxiv-2601-08806 — "Insufficient Verification"
[^c5]: arxiv-2601-08806 — "where models assume code generation equals task completion"
[^c6]: arxiv-2601-08806 — "Models typically use fewer episodes on successful tasks compared with unsuccessful tasks (44.9"
