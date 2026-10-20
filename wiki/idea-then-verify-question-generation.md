---
description: "A tutoring agent splits question generation into an idea stage conditioned on the learner's mistake and difficulty history and a verify stage run by a validator with no shared reasoning chain."
aliases: ["Personalized Question Generation", "Hybrid Personalization Engine question pipeline"]
sources: ["arxiv-2604-26962"]
---
# Idea-then-verify question generation

> Decide what to ask from what the learner has gotten wrong before; decide whether the question is any good from a role that never saw how it was written.

## Definition / Mechanism

Zhao et al. (2026) describe DeepTutor's question-generation
component as a two-stage architecture that "separates what to ask from how to
ask and verify" — the split is between the agent that decides the target
concept and the agent that decides whether a specific question is fit to show
the learner, and each stage draws on a different half of the system's memory.
[^c1]

**Stage one, idea generation, is conditioned on the learner's history.** Rather
than generating a question from a bare topic, the idea agent conditions
jointly on retrieved course material and a dynamic learner-memory context
that includes "past mistakes, difficulty trends, and related problems," and
produces a pool of candidate ideas — each specifying a target concept, a
question format (MCQ, written-response, or coding), and a rationale grounded
in the learner's diagnosed gaps — before an evaluator-driven filter prunes the
pool for clarity, relevance and diversity.[^c2]

**Stage two, generation, draws on the same memory for a different purpose:
calibration rather than targeting.** A generator produces a question, answer
and explanation triple for each surviving template, grounding facts in the
retrieved material and setting difficulty from the learner-memory context; "a
structurally separated validator then applies two complementary checks" —
LLM-based verification of template alignment, factual correctness and
pedagogical soundness for every item, plus sandboxed code execution for
computational ones.
[^c3]

**The validator's independence is the stated reason for the split.** The paper
argues the separation is not incidental: "because the validator shares no
reasoning chain with the generator, it must independently verify correctness,
reducing the risk of self-confirming errors that self-evaluation may miss."
[^c4]

A failed question-answer-explanation triple is not silently kept or discarded
but sent back with structured diagnostic feedback and regenerated until both
the pedagogical and factual checks pass.
[^c5]

## Why it matters

The mechanism answers two of the category's axes at once with one design: it
changes **what** an agent asks (the idea stage is a function of the specific
learner's error and difficulty history, not a fixed curriculum) and **whether
a given question is asked at all** (the verify stage can reject and force
regeneration). The load-bearing design choice is architectural, not a prompt
instruction: the validator is a distinct role with no access to the
generator's reasoning trace, which is the paper's own stated defense against
a generator approving its own output. An ablation that removes the dynamic
memory component isolates the idea stage's contribution: "Personalization
and Fitness decline most sharply, showing that the learner profile is central
to gap-aware explanation and difficulty-calibrated practice," while a
separate ablation of the static-grounding component instead degrades
factual/source metrics — the two memory halves feed the two stages
differently and fail differently when removed.
[^c6]

## Limits

- The ablation[^c6] measures the *idea stage's* memory input (removing DPM
  degrades personalization), not the *verify stage* in isolation — no ablation
  in the extract removes only the independent validator to show what a
  self-evaluating generator would produce instead; the self-confirming-error
  claim[^c4] is the paper's design rationale, citing prior work, rather than a
  DeepTutor-specific measurement.
- "Difficulty trends" and "past mistakes" are named inputs to the idea agent,
  but the extract does not specify how difficulty is scored or how a trend is
  computed from the trace forest — the calibration mechanism itself is
  underspecified here.
- The two-stage split is evaluated only inside DeepTutor's full pipeline
  (Table 2 interactive evaluation, §5.4 ablation); there is no baseline in the
  extract that runs the same idea-generation stage with a single-agent
  self-check instead of a structurally separated validator, so the marginal
  effect of separation specifically (versus verification generally) is
  unmeasured.

## Related

[[code-fact-grounded-socratic-assessment]] · [[verification-over-invention]] · [[decision-centric-design]] · [[argument-grounded-socratic-questioning]]

[^c1]: arxiv-2604-26962 — "We propose a two-stage architecture that separates what to ask from how to ask and verify; these stages correspond to ④–⑤ in Appendix Algorithm 1."
[^c2]: arxiv-2604-26962 — "Conditioning jointly on Crag and Cmem , including past mistakes, difficulty trends, and related problems surfaced via the TraceToolkit, the idea agent produces a pool of candidate ideas, each specifying a target concept, question format (MCQ, written-response, or coding), and a personalized rationale grounded in diagnosed gaps."
[^c3]: arxiv-2604-26962
[^c4]: arxiv-2604-26962 — "because the validator shares no reasoning chain with the generator, it must independently verify correctness, reducing the risk of self-confirming errors that self-evaluation may miss"
[^c5]: arxiv-2604-26962 — "Failed pairs receive structured diagnostic feedback and are regenerated until both pedagogical and factual constraints are met."
[^c6]: arxiv-2604-26962 — "Removing DPM mainly weakens adaptation. Personalization and Fitness decline most sharply, showing that the learner profile is central to gap-aware explanation and difficulty-calibrated practice"
