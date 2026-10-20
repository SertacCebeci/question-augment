---
description: "Referential ambiguity can be typed by the size of the scene's match set: empty (absence), several (multiplicity), empty only from one robot's view (observation-level), or ungrounded wording."
aliases: ["environment-induced ambiguity", "absence and multiplicity ambiguity", "SG-CoT ambiguity types"]
sources: ["arxiv-2603-18271"]
---
# Referent match-set ambiguity

A robot planner can tell what kind of question to ask by counting. The instruction names a target by attributes; the scene is searched for objects carrying them; the size of that match set types the ambiguity. This is the formalisation in the SG-CoT planning framework.[^c1]

## The types

Let A(I) be the attributes the instruction ascribes to its target and A(o) those of an object o. The match set is every scene object whose attributes include A(I).[^c2]

- Absence: the match set is empty. The thing asked for is not there.
- Multiplicity: the match set has more than one member. The instruction fits several objects.[^c3]
- Observation-level: a robot sees only a subset of the scene. The match set from its own view is empty while the global match set has at least one member. Someone else, or somewhere else, holds the answer, so the useful question may go to another robot instead of the user.[^c4]
- Underspecification (instruction-level): the reference is ungrounded, for example "place something over the green bowl" in place of "place the red block over the green bowl".[^c5]

The first, second and fourth are called environment-induced: they cannot be seen from the instruction text alone. The authors list classifying them formally as a contribution, noting they are largely unexplored by prior approaches.[^c6] Their measurement supports the point: instruction-level ambiguity was the most manageable for earlier methods, while environment-level ambiguity was harder because it is not explicitly visible from the instruction alone.[^c7]

## Why the typing matters for asking

The agent must not only notice ambiguity but name its source. In the benchmark, the ask action carries a question and an ambiguity tag. If the tag matches the ground truth the agent is given the missing target. If it does not, the trial ends at once with a success rate of 0, because the agent could not identify the source of the ambiguity.[^c8] The question is therefore scored by whether it targets the right cause, not by whether the agent merely hesitated. This separates two things: detecting that something is wrong (the ADA metric) and asking so that the answer resolves it (success rate).[^c9]

The typed setup was run in a tabletop simulator with 400 trials: 100 randomised configurations for each of three single-agent categories plus 100 clear scenarios.[^c10] Making the scene queryable (a scene graph the model retrieves from step by step) beat giving it the whole graph at once; the drop was 0.34 ADA and 0.38 SR for the small model.[^c11]

## Limits

- All types are defined over closed sets of attribute-matched objects. Ambiguity about intent, preference or vague predicates is only covered by the underspecification case and is not typed further.
- The tag-matching rule is a benchmark device. It rewards the correct label but does not measure whether a human would find the question natural or cheap to answer.
- Results are simulated tabletop scenes with a high-level pick and place plus ask action space, and two models; whether the counts transfer to cluttered real scenes is not tested here.
- Which counts should trigger asking versus acting is not derived. That multiplicity should prompt a question is assumed by the benchmark design (my reading).

## Related

- [[embodied-ambiguity-sources]] — splits embodied ambiguity by where the missing information lives; absence and observation-level here are the "in the world" side
- [[ambiguity-taxonomy]] — general catalogue of ambiguity sources
- [[task-ambiguity]] — ambiguity over which task is meant, a different axis from which object
- [[ambiguity-detection-localization-gap]] — detecting ambiguity versus pinpointing its source

[^c1]: arxiv-2603-18271 — "ambiguous scenarios are"
[^c2]: arxiv-2603-18271 — "be the set of attributes describing a target object"
[^c3]: arxiv-2603-18271 — "Absence is defined as the"
[^c4]: arxiv-2603-18271 — "Multi-agent systems are also"
[^c5]: arxiv-2603-18271 — "Instruction-level ambiguity,"
[^c6]: arxiv-2603-18271 — "formally classified into three distinct types, including environment-induced ambiguities, which are"
[^c7]: arxiv-2603-18271 — "the environment-level as they are not explicitly visible from the instruction alone."
[^c8]: arxiv-2603-18271 — "resulting in an SR of 0 for the trial, as the LLM"
[^c9]: arxiv-2603-18271 — "inherently evaluates the correctness of the clarification question"
[^c10]: arxiv-2603-18271 — "with 100 randomized configurations per ambiguity category, and 100 clear scenarios."
[^c11]: arxiv-2603-18271 — "This results in an overall drop of"
