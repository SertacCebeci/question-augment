---
description: "An inference-time LLM-tutoring framework that selects one of five Berlyne-derived curiosity operators per turn from the learner's interaction state, raising exploratory questioning and turn count."
aliases: ["CURIOBOT"]
sources: ["ganganath-2026"]
---
# CURIOBOT

> A closed-loop policy for *which linguistic intervention to apply next* in a
> tutoring dialogue — not which axis of $W$ to query, but which framing of
> the current turn is most likely to make the learner ask one.

## Definition / Mechanism

At each tutor turn, CURIOBOT reads the interaction state (response depth,
exploratory questioning, confidence cues, conversational initiative) and
selects one of five discrete operators — NOVELTY, COMPLEXITY, CONFLICT,
UNCERTAINTY, or NEUTRAL — each a distinct way of reframing the same
underlying content to introduce epistemic tension; the tutor's response is
then generated conditioned on that choice, so operator selection is
separated from response generation and can be analysed on its own. At each
tutor turn, the framework selects one of five operators, NOVELTY,
COMPLEXITY, CONFLICT, UNCERTAINTY, or NEUTRAL, that modulates how the tutor
frames information while preserving the same underlying learning objective.
Both stages are implemented using prompted black-box LLMs without
fine-tuning or parameter updates, allowing curiosity modulation to operate
entirely as inference-time linguistic intervention.[^c1]

## Why it matters

In a controlled 3×3×3 factorial study (three LLM families, three academic
domains, three topic-complexity levels; 270 tutoring conversations, 45
participants), curiosity-modulated interactions produced roughly 2.4× more
conversational turns than Baseline under a fixed time budget, with gains
holding across domains and complexity levels. This is a measured effect on
*how much* a human is prompted to ask, produced purely by changing how the
tutor frames its turn, not by changing what it explains.[^c2]

The five operators are not interchangeable: CONFLICT reached the highest
downstream success rate (79.03%, the share of applications followed by a
stable or increased curiosity score) despite being selected only 72 times,
while NOVELTY was selected most often (258 appearances) but achieved a
substantially lower success rate (61.42%) — a difference the paper reads as
consistent with Berlyne's own claim that cognitive conflict produces
stronger epistemic tension than novelty or complexity alone, so an operator
that surfaces a contradiction in the learner's reasoning outperforms one
that merely reframes information as new.[^c3]

## Transfer

| | |
|---|---|
| **Home field** | Psychology of curiosity (Berlyne, 1960, 1962): collative variables — novelty, complexity, conflict, surprise/uncertainty — as the stimulus properties that raise epistemic arousal and information-seeking |
| **Here** | A discrete, per-turn control signal selected by an LLM policy conditioned on the learner's live interaction state, then used to condition a second LLM's response generation |
| **What survives** | The four-way taxonomy as operationally distinguishable prompting strategies, and the qualitative ranking that conflict-based tension outperforms novelty-based tension for sustaining exploration |
| **What does not** | Berlyne's original dose-response claim — an inverted-U relating arousal magnitude to preference — is not tested here; the paper reports categorical operator selection and turn-count/success-rate effects, not an arousal curve, so no quantitative form of the underlying psychological theory is verified by this result |

## Limits

- One population size and composition: 45 participants across 270
  conversations: the 2.4× figure and the operator success-rate ordering are
  this study's numbers, not a cross-study replication.
- The outcome proxies (conversational turns, a "curiosity score" from
  learner interaction signals) stand in for exploratory questioning and
  are not validated against an independent report of felt curiosity at
  scale.
- Operator content and selection policy are confounded: the study does not
  isolate whether the gain comes from *which* operator is chosen or from
  the linguistic content each operator injects regardless of timing.
- `ganganath-2026` is drawn from a single archived preprint text extract,
  not yet independently verified.

## Related

[[constraint-seeking]] · [[clarification-benchmarks]] · [[five-whys]]

[^c1]: ganganath-2026 — "At each tutor turn, the framework selects one of five operators, N OVELTY, C OMPLEXITY, C ONFLICT, U NCERTAINTY, or N EUTRAL, that modulates how the tutor frames information while preserving the same underlying learning objective."
[^c2]: ganganath-2026 — "2.4× more conversational turns than Baseline."
[^c3]: ganganath-2026 — "C ONFLICT achieves the highest success rate"
