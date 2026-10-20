---
description: "Given the identical LLM-elicited model, a classical planning algorithm reaches full accuracy with far fewer observations than an LLM asked to plan directly over that same model."
aliases: ["knowledge-planning gap"]
sources: ["perets-2026"]
---
# LLM knowledge-planning gap (active feature acquisition)

> Same elicited knowledge, two planners: handing an LLM its own extracted
> model and asking it to decide what to observe next measurably
> underperforms a classical algorithm run on that same model.

## Definition / Mechanism

Perets et al. (2026) isolate knowledge from planning by
holding an LLM-elicited discriminative MRF fixed and comparing two ways of
acting on it: a classical planning algorithm (CMI-driven or Wald-style
acquisition) against the LLM itself asked to classify directly from the
same elicited parameters (MRF-LLM), or from the same parameters plus
retrieved literature passages (RAG-LLM), since both arms see identical
knowledge and only the [[planner-dynamic-stopping|planner]] differs: "the formal algorithm reaches the
same accuracy with much fewer observations, a gap attributable entirely to
planning".[^c1]

Against a full-observation likelihood target, the classical planner
reaches perfect accuracy while the LLM arms plateau well short of it even
once every feature is observed: "at full observation the LLM baselines
reach only RAG-LLM 0.800 and MRF-LLM 0.700, short of the planner's 1.000
against the likelihood label".[^c2]

The gap holds throughout acquisition, not only at the end: "The LLM
baselines trail the planner at every intermediate checkpoint (RAG-LLM
0.34-0.46, MRF-LLM 0.24-0.38)".[^c3]

## Why it matters

For stall 2, this bounds which agent should hold the pen once a selection
criterion is already formalized: an LLM given the same information a
classical scorer would use is not a substitute for running the scorer,
even in the single most favorable case for the LLM — identical knowledge,
one decision, no confound from elicitation quality.

## Limits

- One domain (IBD diagnosis) and one MRF size; the gap's magnitude is not
  shown to generalize to other elicited models or tasks.
- Holds knowledge fixed but not prompting strategy in general — MRF-LLM and
  RAG-LLM are two specific baseline prompts, not an exhaustive search over
  how an LLM could be asked to plan.
- The paper itself flags parts of its evaluation (the top-k arm) as a
  small, 10-patient pilot; the binary-classification numbers quoted here
  are from the larger cohort but the study overall is early-stage.
- `perets-2026` is an unreviewed arXiv preprint [?] at the time of writing.

## Related

[[zero-shot-active-feature-acquisition]] · [[optimal-decision-tree]] · [[bounded-rationality]]

[^c1]: perets-2026 — "the formal algorithm reaches the same accuracy with much fewer observations, a gap attributable entirely to planning"
[^c2]: perets-2026
[^c3]: perets-2026 — "The LLM baselines trail the planner at every intermediate checkpoint (RAG-LLM 0.34–0.46, MRF-LLM 0.24–0.38)"
