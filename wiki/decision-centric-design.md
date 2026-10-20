---
description: "An LLM system's act-or-ask/act-or-stop choice is made by an explicit, deterministic policy over exposed signals, not fused into one generation call."
aliases: ["decision-centric framework", "explicit decision layer", "decision-centric abstraction"]
sources: ["arxiv-2604-00414"]
---
# Decision-centric design

> Separate the signal from the switch: expose what the system knows as an
> explicit context, and let a deterministic policy — not a fused generation
> call — pick the action.

## Definition / Mechanism

Sun (2026) frames every control choice an LLM system
makes — answer, clarify, retrieve, call a tool, repair, escalate — as a
**decision point**, a tuple $(A, c, \delta)$: a finite action set $A$; a
decision context $c$ (interaction history, retrieved evidence, validation
outcomes, learned or heuristic signals, hard constraints); and a decision
function $\delta$ that maps $c$ to an action in $A$: "given the same exposed
context and constraints, δ selects the same action, even if parts of that
context are noisy, learned, or heuristic." The point is what it removes:
in a prompt-based system, context interpretation, signal estimation, action
selection and generation are entangled in one model call, so a wrong action
cannot be traced to a bad estimate, a bad policy or a bad execution. "We
propose a decision-centric framework that
separates decision-relevant signals from the policy that maps them to
actions, turning control into an explicit and inspectable layer of the
system."[^c2]

Model routing and adaptive inference scaling already instantiate the tuple
with a static context. The paper's extension is **sequential**: a context
$c_t$ that evolves as chosen actions produce new observations. The minimal
case reduces to a single sufficiency signal $\hat p_{\text{suff},t}\in[0,1]$
gating execute vs. [[clarification-request|clarify]]; a richer case pairs it
with a correctness signal $\hat p_{\text{corr},t}$ gating continue, clarify
or backtrack, where "a failed attempt may lower perceived correctness while
simultaneously improving sufficiency by eliminating alternatives" — the
signals are updated jointly, not independently, by the same action.

## Why it matters

Three experiments hold the policy fixed and vary only whether the driving
signal is an explicit scalar or left inside one LLM call. In calendar
scheduling with $k$ missing fields, the decision-centric (DC)
system reaches 100% success at every $k\in\{0,\dots,4\}$ while a
prompt-based clarify baseline degrades, "dropping to 75%, 60%, and 10% at
k =2, 3, 4, respectively," and blind retry fails at every $k\ge1$ by
exhausting its turn budget without ever clarifying. In graph
disambiguation, a setting (S5) where an action's effect on the *other*
signal is not directly observable — a failed traversal also eliminates
candidates sharing its minority attribute value, shrinking the pool without
a new clarification — DC tracks the update and reaches 100%, while stating
the identical policy in the system prompt ("Prompt w/ policy") stays at
35%, *below* blind retry (60%): "the effective candidate set has already
changed during traversal, and that state update is not available to the LLM
at decision time." In retrieval-stopping control, holding the
stop/expand policy fixed and swapping only how the sufficiency signal is
built (LLM judge, dense similarity, or their composite) isolates signal
quality from decision logic: on medium-difficulty questions, "Prompt reaches
12% success, while DC-LLM reaches 86%" with the *same* underlying LLM and
passages. A further benefit of exposure is diagnosis: logging the signal
at every turn lets a failure be attributed after the fact, without
re-running the model — "A benefit of the decision-centric design is that
failures can be attributed directly to the sufficiency signals."[^c6]

## Transfer

| | |
|---|---|
| **Home field** | LLM system architecture — model routing, adaptive inference scaling, agentic pipelines |
| **Here** | Any point where an asking agent chooses whether to ask, what to ask about, or when to stop asking |
| **What survives** | A policy is only as inspectable as the signal it consumes is explicit; restating a threshold rule in a prompt is not a decision layer, since the state the rule needs (e.g. an updated candidate pool) may not be re-derivable from prompt text |
| **What does not** | The specific signals (LLM-judged sufficiency, embedding similarity, structural consistency) are task-built for these experiments, not general estimators |

## Limits

- All three experiments run one small model family per task (Granite 4.0
  Micro, replicated on LLaMA 3 8B for calendar only); whether the
  Prompt-baseline gap narrows with larger models is explicitly flagged as
  untested ("some of the gaps we observe may narrow" as models improve).
- $\delta$ studied is deterministic and mostly threshold-based; the paper
  states the framework also admits learned or optimization-based $\delta$,
  but does not evaluate one.
- The calendar and graph tasks are synthetic (templated requests, a
  synthetic knowledge graph); only retrieval uses a real benchmark (Natural
  Questions over a fixed BM25 corpus).
- Names an architectural pattern, not a new estimator or policy-learning
  method: the contribution is where control is placed, not how well one
  signal or policy performs alone.

## Related

[[clarification-request]] · [[value-of-information]] · [[compound-ai-systems]] · [[controller-class-regime-theory]] · [[belief-state-gating-policy]]

[^c2]: arxiv-2604-00414 — "We propose a decision-centric framework that separates decision-relevant signals from the policy that maps them to actions, turning control into an explicit and inspectable layer of the system."
[^c6]: arxiv-2604-00414 — "A benefit of the decision-centric design is that failures can be attributed directly to the sufficiency signals."
