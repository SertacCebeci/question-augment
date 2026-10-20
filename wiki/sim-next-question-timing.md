---
description: "A planning layer picks and times each question by forward-simulating its expected one-step posterior collapse under a per-game question budget, not by a generic ask-policy or a prompt claim."
aliases: ["sim.next", "hypothetical-transition evaluation", "question timing under budget"]
sources: ["arxiv-2604-07236"]
---
# Sim.next question timing

> Each question is selected and timed by forward simulation under a declared budget, not issued by a generic question policy.

## Definition / Mechanism

In a four-layer externalization of a planning harness for noisy
Collaborative Battleship ([[arxiv-2604-07236|How Much Heavy Lifting Can an
Agent Harness Do? (2026)]]), the planning layer (L2) chooses, at every
turn, between asking an information-gathering question and taking a
scoring shot by rolling each candidate forward through a belief-update
simulator rather than scoring it analytically or asking an LLM to judge
it: "Hypothetical-transition evaluation is exposed as a sim.next
primitive that scores a candidate action by its expected one-step
posterior collapse rather than by a prompt-returned claim." "+ Planning.
Evaluates shoot and question actions via sim.next with a two-bucket
question budget." sim.next runs on the harness's own 500-particle
Metropolis–Hastings posterior over hidden ship placements — the same
backend the belief-only baseline uses — so the only thing that changes
between the two harnesses is this evaluate-then-choose step, never the
belief model itself.

Question *timing*, not just question *selection*, is what the budget
buys: candidate questions are drawn from a region-DSL action set and
placed into one of two per-game buckets rather than spent at a uniform
rate, so that questions cluster where they carry the most information
about the posterior: "the action set includes region-DSL questions drawn
under a two-bucket budget so that questions are timed — early-game ROI
narrowing and late-game cluster closeout — rather than uniformly
rate-limited." Against the objection that the layer simply asks more:
"each question is selected and timed by sim.next under declared budget
constraints, not issued by a generic question policy."[^c2]

## Why it matters

Against a belief-only harness that fires at the highest-probability cell
and asks no questions, adding this layer — zero LLM calls in either
harness — is the single largest jump the paper's four-layer ablation
finds on any layer, primary or secondary: "Across 54 games, declarative
planning carries the heavy lifting (+24.1pp win rate over a belief-only
harness, zero LLM calls)." The gain is asymmetric across metrics
(+0.017 F1 vs. +24.1pp win rate), because the mechanism changes how
often the agent escapes a flat, uninformative posterior rather than
sharpening its aim once there. The budget also shows up directly as
an asking rate: the planning layer's win rate is bought at "asking about
11.9 questions per game," against about 8 for the harnesses one layer up
(symbolic and LLM-backed reflection), where reflection competes with the
same finite per-game turn supply for the questions the budget would
otherwise spend.[^c4]

## Limits

- Single domain (Battleship), which the paper itself flags as
  unusually favorable to a simulate-and-score planner: "Battleship is
  also a probabilistic-search problem in which MCMC posteriors and
  sim.next-evaluated planning are a particularly natural fit, so the
  planning layer's +24.1pp lift may overstate what declarative planning
  recovers in less search-friendly domains."[^c5]
- 54 games; the confidence intervals are wide enough to show the
  L1→L2 jump clearly but not to bound its size tightly.
- The two-bucket budget is hand-set (early-game ROI narrowing,
  late-game cluster closeout), not learned; when the next layer changes
  the bucket count (two to three plus an exploit threshold), the paper
  names this a confound it does not control for.
- The question pool is a fixed region-DSL, not LLM-generated: the
  paper contrasts this with a richer, LLM-emitted Python-program
  question pool from prior Battleship work and leaves that axis
  unexplored here — **unverified** whether sim.next timing still
  dominates once the question pool itself is LLM-authored.

## Related

[[expected-information-gain]] · [[question-budgets]] · [[value-of-information]] · [[decision-centric-design]] · [[uncertainty-gated-lm-fallback]]

[^c2]: arxiv-2604-07236 — "each question is selected and timed by sim.next under declared budget constraints, not issued by a generic question policy."
[^c4]: arxiv-2604-07236 — "+Planning achieves its high win rate while asking about 11.9 questions per game; both symbolic and LLM-backed reflective variants ask about 8"
[^c5]: arxiv-2604-07236 — "Battleship is also a probabilistic-search problem in which MCMC posteriors and sim.next-evaluated planning are a particularly natural fit, so the planning layer’s +24.1pp lift may overstate what declarative planning recovers in less search-friendly domains."
