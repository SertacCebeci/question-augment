---
description: "An agentic pipeline that converts its own detected knowledge gaps and logical issues into structured questions, then resolves them by tool-mediated search before generating output."
aliases: ["Questioning-and-Solving", "questioning-and-solving closed-loop", "RS-Gen"]
sources: ["bian-2026"]
---
# Questioning-and-solving

> Selection here is not "which axis to ask a human about" but "which of my
> own gaps must be closed by a tool before I am allowed to act" — the
> asker and the answerer of every question are the same agent.

## Definition / Mechanism

RS-Gen restructures image generation from a single black-box mapping into a
four-stage pipeline: an Image Router Agent resolves coreference and locates
the target image; an Intent Analysis Agent evaluates task complexity and
decides whether the request needs only direct generation or a
"search_reason_generation" detour; when it does, this agent mines the
implicit constraints in the instruction and converts them into a structured
question set $Q_t=\{q_1,\dots,q_k\}$ aimed at downstream modules, rather than
letting the generator proceed on an unstated assumption: "the Intent
Analysis Agent deeply parses ambiguous instructions, accurately mining the
implicit constraints hidden behind natural language and translating them
into an explicit, structured question set."[^c1]

Two rules bound what enters $Q_t$. "Defensive Questioning" forces every
non-universal named entity or long-tail concept into an explicit question
about its objective visual features rather than letting the model answer
from its own prior — "this strategy strictly prohibits the model from
relying on its internal prior knowledge for unconstrained heuristic
generation." "Process Decoupling" restricts each question to the terminal,
renderable visual feature and discards intermediate deduction steps the
downstream image model cannot use directly.[^c2]

A separate Reasoning & Search Agent, patterned on ReAct, then answers $Q_t$
by invoking external search, VQA and logic tools in a "Thought-Action-
Observation" loop until the question set is resolved, factually grounded
and logically self-consistent, only then handing a completed instruction to
the Image Generation Agent.[^c3]

## Why it matters

In an ablation on WISE_Verified with Qwen-Image as the base generator,
adding the question-generating Intent Analysis Agent alone raised the
overall score from 0.5500 to 0.5850 (+0.035); adding the Reasoning & Search
Agent that answers those questions produced the largest single jump in the
whole pipeline, 0.5850 to 0.7940 (+0.209) — "following the integration of
the Reasoning & Search Agent, the system experiences a significant
performance leap."[^c4]

## Limits

- The gain attributed to "questioning-and-solving" is read off an ablation
  table that adds sub-agents cumulatively (IR, then IA, then RS, then IG);
  the +0.209 step credits the Reasoning & Search Agent's tool use together
  with the questions the Intent Analysis Agent feeds it, not the question
  set alone in isolation.
- Evaluated on two benchmarks built to reward exactly this kind of
  knowledge-gap and logical-puzzle content (WISE_Verified, RISEBench); no
  general-purpose text-to-image benchmark is reported.
- The questions are never shown to a human; "solving" means tool-mediated
  self-answering, so the mechanism says nothing about when a self-generated
  question should instead be escalated to a person.[^c5]

## Related

[[knowledge-graph-guided-clarification]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: bian-2026 — "the Intent Analysis Agent deeply parses ambiguous instructions, accurately mining the implicit constraints hidden behind natural language and translating them into an explicit, structured question set"
[^c2]: bian-2026 — "this strategy strictly prohibits the model from relying on its internal prior knowledge for unconstrained heuristic generation"
[^c3]: bian-2026 — "Through multi-step deep reasoning and external information retrieval, this agent effectively bridges knowledge blind spots, supplements factual evidence, and accomplishes complex logical deconstruction."
[^c4]: bian-2026 — "following the integration of the Reasoning & Search Agent, the system experiences a significant performance leap, with the overall score substantially increasing to 0.7940"
[^c5]: bian-2026 — "Acting as the "cognitive hub" of the system, this module draws inspiration from the ReAct [14] pattern, possessing the capability to autonomously invoke external search engines, Visual Question Answering (VQA) tools, and logical reasoning tools."
