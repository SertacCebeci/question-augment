---
description: "A two-tier duplex agent design routing each turn between a realtime tier that talks, interrupts and asks follow-ups, and a slower tier that plans and executes tasks."
aliases: ["Cerebellum-Brain architecture", "Cerebellum-Brain collaborative framework", "front cerebellum / back brain", "dual-brain architecture"]
sources: ["orantqing-2026"]
---
# Cerebellum-Brain architecture

> A named decoupled architecture for a spoken interaction agent: a fast
> "Cerebellum" tier owns the turn-taking decision — speak, interrupt, ask a
> follow-up, or delegate — while a slower "Brain" tier plans and executes
> multi-step tasks in the background.

## Definition / Mechanism

Gander splits an interactive agent into a front tier ("Cerebellum") and a
back tier ("Brain"). The front tier is a realtime, full-duplex multimodal
model that "can independently handle routine conversational exchanges,
information seeking interactions, and simple search based tasks," and
additionally decides, turn by turn, "whether a request can be resolved
locally or requires delegation to the back brain," with "complex workflows
involving multi step reasoning, external tool use, or long horizon
execution … delegated to the back brain."[^c1]

The routing decision is exposed through three structured tool operations:
`task_start` creates a background task from the current turn; `task_resolve`
grants or denies control (`cancel`, `allow_once`, `allow_session`, `deny`);
and `task_send` routes a later user turn into an already-running task, with
two modes — `main`, which steers the primary task, and `fork`, which
"instantiates a read only auxiliary inquiry without altering the state or
execution trajectory of the primary task." Fork mode is the mechanism by
which the front tier can ask a clarifying or follow-up question about an
in-flight task without committing to changing it.[^c2]

The paper reports the benchmark's own baseline-comparison caveat directly:
"The benchmark's system prompt instructs baselines to execute tools
immediately rather than ask clarifying questions, but the back brain, being
an external agent, never receives it," so the authors had to add an
equivalent instruction file to the back-brain's working directory to keep
the comparison fair — a sign that "execute now" versus "ask first" is
itself a tunable instruction, not a fixed property of the architecture.[^c3]

## Why it matters

On Full-Duplex-Bench v3 (100 tool-augmented spoken-service scenarios with
natural disfluencies), Gander took the floor at an appropriate moment in
100% of scenarios and began speaking prematurely in only 8.0% of turns,
against 13.5% for the next-best system and 47.9% for the weakest baseline,
while its task-accuracy scores (Pass@1 0.400, ToolSel 0.759, ArgAcc 0.503,
RespQual 0.490) trailed the strongest single-tier baselines. The paper reads
this jointly: "a system can trivially suppress interruptions by waiting
longer, at the cost of missing its turn altogether," and Gander's pairing of
a perfect take-turn rate with a low interrupt rate is attributed to
"predicting the interaction decision before any content is generated" —
i.e., the front tier's asking/interrupting decision is scored separately
from, and before, the content it will produce.[^c4]

For the "which axis first" stall, this is a concrete instance of routing
the decision of *whether to ask now* to a component that is architecturally
separate from the component that plans the eventual answer — the routing
tool interface (`task_start`/`task_send`/`task_resolve`) is the mechanism
that makes that separation explicit and measurable, rather than left
implicit in a single model's context window.

## Limits

The turn-taking numbers come from one benchmark (Full-Duplex-Bench v3, 100
scenarios) scored by an LLM judge (GPT-4o) reading an ASR transcript of
synthesized speech, so the reported take-turn/interrupt/filler rates carry
recognition and synthesis error on top of the architecture's own decisions;
the paper itself flags that the back-brain-only ablation cannot be scored on
these three metrics at all because it lacks an audio timeline. The 100%
take-turn / 8.0% interrupt result is for this one system on this one
release of the benchmark, not a general property of two-tier routing
architectures, and the accompanying task-accuracy metrics (Pass@1 0.400)
are below several single-tier baselines, so the architecture trades some
task correctness for turn-taking responsiveness in this evaluation. [?]
`orantqing-2026` is an arXiv preprint, not independently verified.

## Related

[[mutual-information]] · [[optimal-decision-tree]] · [[bounded-rationality]]

[^c1]: orantqing-2026 — "can independently handle routine conversational exchanges, information seeking interactions, and simple search based tasks"
[^c2]: orantqing-2026 — "fork, which instantiates a read only auxiliary inquiry without altering the state or execution trajectory of the primary task"
[^c3]: orantqing-2026
[^c4]: orantqing-2026 — "It takes the floor at an appropriate moment in all 100 scenarios, matched only by the cascaded pipeline, and begins speaking prematurely in just 8.0% of turns, against 13.5% for GPT-Realtime and 47.9% for the weakest baseline."
