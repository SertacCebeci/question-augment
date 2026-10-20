---
description: "Organizing a long-horizon research agent around an evolving information state, rather than around the candidate solution, so probing without changing the solution becomes a first-class move."
aliases: ["information paradigm"]
sources: ["fu-2026"]
---
# Information paradigm

> Two ways to organize an agent's research loop: refine the candidate and
> let information pile up as exhaust, or revise the information and let the
> candidate follow.

## Definition / Mechanism

Fu et al. (2026) contrast two ways to organize a long-horizon autonomous
research process. Solution-centric search treats the candidate solution
$x_t$ as the evolving state that a tree, graph or chain protocol refines;
information produced along the way accumulates only as a by-product. Against
this, the information paradigm makes the evolving information state
$I_t$ — a continually revised representation of what the system has learned
about the task — itself the state the system tracks and updates, with
changes in $I_t$ guiding subsequent revision of the retained solution
$x_t$.[^c1]

Two limitations of the solution-centric alternative motivate the framework:
its predefined action structures (tree, graph, chain) constrain how the
next action is chosen from the current search state, giving "limited
support for probing a decision-critical unknown without producing another
candidate"; and its memory mechanisms preserve experiment records or
validated successes without maintaining cross-experiment findings as
revisable, provenance-tracked claims.[^c2]

## Why it matters

For stall 2 — which axis to act on next — the paradigm choice decides what
selection can even see. Under solution-centric search, only actions that
modify or evaluate a candidate are available moves, so a probe that would
gather evidence without changing anything is not a first-class option;
under the information paradigm, [[epistemic-actions|epistemic actions]]
that update the information state without touching the solution sit
alongside interventional ones as an equally available choice. This reading
is the wiki's own gloss on the framework's stated motivation, not a claim
the paper states in these terms.

Instantiated as Iris, the paradigm produced the paper's largest reported
system-level effect: on MLE-Bench, Iris attains a 64.9% overall any-medal
rate and 39.1% gold-medal rate under a 12-hour budget, the highest among
compared systems, and against the same [[backbone-of-a-formula|backbone]] (AIBuildAI, Claude-Opus-4.6)
raises the any-medal rate from 63.1% to 64.9% and the gold-medal rate from
25.8% to 39.1% while cutting the research budget from 24 to 12 hours.[^c3]

## Limits

- This is the paper's own framing of its contribution, not an externally
  validated dichotomy: no experiment isolates "information-centric" from
  "solution-centric" organization while holding every other agent component
  fixed — the reported gains are for the whole Iris system, which also adds
  [[epistemic-actions]] and a knowledge-revision mechanism this note does not
  cover.
- Demonstrated only for autonomous ML engineering (MLE-Bench, 75 Kaggle
  tasks) plus four cross-domain tasks in agentic tool use and model
  post-training; nothing here shows the distinction holds for question-asking
  outside an agent that also produces and evaluates artifacts.
- "Information state" is Iris's specific data structure (raw evidence,
  structured summaries, revisable claim records); the broader claim that
  centering asking on the state of knowledge beats centering it on the
  current best answer is wider than what is tested here.

## Related

[[epistemic-actions]] · [[value-of-information]] · [[adaptive-submodularity]] · [[bounded-rationality]]

[^c1]: fu-2026
[^c2]: fu-2026 — "Predefined tree, graph, or chain structures constrain how the next action is selected from the current research state. Existing actions still serve to modify and evaluate candidate solutions and thus provide limited support for probing a decision-critical unknown without producing another candidate."
[^c3]: fu-2026 — "Under a 12-hour budget, Iris attains a 64.9% overall any-medal rate and a 39.1% gold-medal rate, both the highest among the compared systems (Table 1)."
