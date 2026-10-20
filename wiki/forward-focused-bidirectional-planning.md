---
description: "Plans a dialogue's next-topic path toward a predefined target by decoding forward and backward from opposite ends and merging into one forward path that favors the forward pass."
aliases: ["FF-BPSN", "Forward-Focused Bidirectional Pseudo-Siamese Network", "forward-focused bidirectional planning"]
sources: ["arxiv-2605-20195"]
---
# Forward-focused bidirectional planning

> Plan the path from where the conversation is *and* from where it must
> end, then let the forward pass win the argument.

## Definition / Mechanism

A target-oriented proactive dialogue system must choose a sequence of
subtargets — `[Action, Topic]` pairs — that leads from the current
dialogue state to a predefined final target (e.g. `[Play music, A
Chinese Ghost Story]`), so that a language model can be steered turn by
turn through them. Forward-focused bidirectional planning decodes this
path twice with two structurally identical (pseudo-siamese)
transformer decoders — once forward from the current state toward the
target, once backward from the target toward the current state — and
then fuses the two into a single forward path with a gated module that
weights the forward decoding more heavily: "It conducts bidirectional
planning—from the current state to the target and vice versa—and
merges the results to form the final forward path."[^c1]

The fusion is a learned sigmoid gate over a concatenation of the
forward and backward path representations, plus a weighted blend of
the two before the gate, so the backward pass supplies information the
forward pass alone would miss without ever becoming the primary
signal. An auxiliary loss term pulls the forward and backward
representations toward each other, on the premise that a good forward
and a good backward path describe the same underlying sequence.

## Why it matters

Ablating the two directions shows the effect is asymmetric and both
directions carry real information: dropping either direction (forward
-only or backward-only) hurts, and the fusion is not symmetric —
weighting the fused output toward the *backward* pass instead of the
forward pass gives back less of the gain: "Unidirectional planning (OF
or OB) underperforms bidirectional planning, highlighting the
importance of considering both directions. The forward-focused module
provides the largest gains, whereas the backward-focused module is
less effective."[^c2]

Against a strong same-family baseline (TPC, a prior backward-conditioned
target-driven planner from the same authors' earlier work) the
bidirectional-forward-focused planner also wins on held-out path
accuracy: "Compared with TPC, it improves topic recognition by 1.05%
in Acc. and 0.84% in Bi. Acc. On DuRecDial 2.0, our framework shows
notable gains across all metrics, boosting both action and topic
recognition above 90%."[^c3]

The planned path is then consumed by downstream language models turn
by turn, so a gain in path accuracy here is a gain in *what gets
proposed next* before any response is generated — the planning step is
separated from, and scored independently of, the generation step it
constrains.

## Limits

- Evaluated only on two closely related, English/Chinese-parallel
  recommendation-dialogue datasets (DuRecDial, DuRecDial 2.0) whose
  target and subtarget vocabulary is a fixed, finite `[Action, Topic]`
  catalogue known at training time; nothing in the extract shows the
  method choosing among candidates outside that catalogue.
- The target is given, not discovered: the mechanism plans *the route
  to* a predefined target, not which target to pursue — it is a path
  planner, not a target-selection or stopping mechanism.
- The forward-favoring design is itself a domain assumption
  ("conversations tend to progress forward"); the paper's own ablation
  shows a backward-favoring fusion recovers less of the gain, so the
  asymmetry is tuned to this genre of task-steering dialogue rather
  than derived from a general principle.

## Related

[[next-best-question]] · [[cost-optimal-query-policy]] · [[dual-node-preference-mcts]] · [[intent-elicitation-graph]] · [[curriculum-sequencing-policy]]

[^c1]: arxiv-2605-20195 — "It conducts bidirectional planning—from the current state to the target and vice versa—and merges the results to form the final forward path."
[^c2]: arxiv-2605-20195 — "Unidirectional planning (OF or OB) underperforms bidirectional planning, highlighting the importance of considering both directions. The forward-focused module provides the largest gains, whereas the backward-focused module is less effective."
[^c3]: arxiv-2605-20195 — "Compared with TPC, it improves topic recognition by 1.05% in Acc. and 0.84% in Bi. Acc. On DuRecDial 2.0, our framework shows notable gains across all metrics, boosting both action and topic recognition above 90%."
