---
description: "The per-turn decision a proactive LLM agent makes between free-text and structured-UI channels to recover information missing from an underspecified task."
aliases: ["Communication Policy", "channel-selection policy", "π_comm"]
sources: ["ma-2026-communication"]
---
# Communication Policy

> A proactive LLM agent facing a vague task specification must decide not only *what* to ask but *through which channel* — free-form text or a generated structured UI — and neither channel dominates the other.

## Definition / Mechanism

Ma et al. (2026) formalize channel selection as a **Communication Policy**: the agent is equipped with two primitives, `ask_question` (free-form natural-language interaction) and `generate_ui` (LLM-generated HTML forms rendered to the user). Three interaction modes follow — text-only ($M_{text}$), UI-only ($M_{ui}$), and hybrid ($M_{hybrid}$), where the agent dynamically chooses between the two primitives at each turn. "In this paper, we formalize the channel-selection decision as Communication Policy. We equip agents with two communication primitives: ask_question for free-form language interaction and generate_ui for HTML-based forms."[^c1]

Across four benchmarks (SWE-bench, TravelGym, τ²-bench, WebArena) and simulated user personas, the two channels trade off rather than one dominating: "text and UI have complementary strengths: text drives task completion, while UI improves response quality and persona compliance." $M_{hybrid}$ wins productivity in 8 of 14 agent–user pairs but not universally — the win is consistent on SWE-bench (4/4) and absent on WebArena (0/2).[^c2]

An oracle ablation isolates the source of the gap: injecting the complete task specification into the prompt (removing any need to ask) raises productivity 2.3×–10.6× over $M_{text}$, and `ask_question` usage drops correspondingly. "Full information improves productivity by 2.3×–10.6× over Mtext, confirming that missing information, rather than execution ability, is the primary bottleneck."[^c3]

## Why it matters

Most work on proactive asking (clarification dialogues, EIG-based selection) treats "what to ask" as the whole problem. This formalizes a second, independent decision — *how* the question is delivered — as a distinct meta-decision with its own trade-off (task completion vs. persona-compliant, low-[[efe-planning-as-variational-inference|ambiguity]] responses), separate from axis selection or question content.

## Limits

The finding rests on simulated users: personas are LLM-parameterized, not human, so persona-compliance and disclosure-uncertainty effects may not transfer to real interlocutors. Results are averaged over four specific benchmarks and model combinations; the hybrid advantage is explicitly task-dependent (absent on WebArena) and the paper does not claim a channel-selection rule that generalizes beyond these settings. [?] — verifier to confirm ma-2026-communication.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[communication-policy-evolution]]

[^c1]: ma-2026-communication — "In this paper, we formalize the channel-selection decision as Communication Policy. We equip agents with two communication primitives: ask_question for free-form language interaction and generate_ui for HTML-based forms."
[^c2]: ma-2026-communication — "text and UI have complementary strengths: text drives task completion, while UI improves response quality and persona compliance."
[^c3]: ma-2026-communication
