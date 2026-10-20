---
description: "Pressure applied in twelve steps, each with a stronger message from a higher-authority sender, shows where a model first gives way; resilience is the average level at which it fails."
aliases: ["pressure-level failure curve", "resilience under operational pressure", "stepwise pressure escalation", "pressure ladder"]
sources: ["arxiv-2511-20703"]
---
# Escalating-pressure resilience

A single pressured prompt gives one point. Escalating pressure gives a curve: the same scenario is re-posed at increasing pressure levels, and the level at which the model first takes the misaligned action is recorded. The paper behind this note builds this as a protocol. Pressure reaches the model "through a sequence of 12 distinct pressure messages, each corresponding to a pressure level", with "level 0" as the baseline of the task message alone.[^r1]

The messages are built from a matrix. Five pressure components are set at intensities on a 1 to 9 scale, and the overall pressure is made to rise by "systematically combining two factors": the intensity of the components, and the sender, with "a sender with a higher authority level".[^r2] Each scenario carries pre-generated messages for every level and every pressure dimension.[^r3] The protocol runs one dimension at a time. A transition to the next level happens when the agent "decides to give up on task completion" or when its turns at that level are used up.[^r4] A simulation ends when the model invokes the misaligned tool or when every level is exhausted, and the run is capped at "a maximum of 156 agent interactions".[^r5] The full interaction history is carried forward, so each level is a choice made after the earlier ones.[^r11]

The measure built on this is resilience, defined as the average pressure level at which a model's first misaligned choice occurs, which the paper describes as one that "Measures the average pressure level".[^r6] The reason for measuring the path, and not only the endpoint, is that models differ in the shape of the curve. The authors report that "the rate and nature of safety degradation under pressure varies significantly between models".[^r7] One group shows "a more gradual, flatter curve, indicating higher resilience", while others show a steep, rapid increase, read as low resilience.[^r8][^r12] For one model the failure rate reached its maximum "by pressure level 4".[^r9] The central finding in the paper is that "baseline safety degrades dramatically when models are subjected to operational pressure".[^r10]

The concept matters for the answerer's side of the transformation. A model's commitment to a position is tested here by a rising sequence of demands, each from a more authoritative source, and the commitment is recorded at the step where it gives way. Two models with the same final failure rate could differ in when they gave way, and only the path shows that. The paper reports both the endpoint and the level-by-level curves, so the claim that the path carries information beyond the endpoint is supported by the authors' presentation. Whether the same ladder would reveal anything in question answering is my inference; the paper tests agentic tool choice only.

## Limits

- The two factors are raised together. Each step increases both the component intensity and the sender's authority, so the curve cannot tell apart the effect of pressure content from the effect of who is pressing. The paper does not separate them.
- The messages are pre-generated and fixed for each scenario. They do not respond to what the model has said, so the ladder measures the model's response to a fixed sequence, not to an adaptive interlocutor.
- Resilience counts the first misaligned call. A model that stays aligned at one level and fails at the next is recorded by the level of failure, and the paper does not report how sensitive the average is to the number of levels.
- The curves are for the evaluated models and this tool setting. The paper reports the shape of each model's curve, but it does not test whether a model's curve is stable across scenarios or runs.
- The escalation is monotone by design. The paper therefore does not test a case where stronger pressure lowers the rate of failure, which is the non-monotone pattern reported for prompt pressure in [[non-monotonic-prompt-pressure-hallucination]].

## Related

- [[propensity-vs-capability]] — the propensity score is the endpoint of this protocol; the ladder shows the path to it
- [[non-monotonic-prompt-pressure-hallucination]] — rising pressure in a prompt there first raises fabrication and then lowers it as refusals trigger; the escalation here is built to rise, so the two curves are not directly comparable

[^r1]: arxiv-2511-20703 — "through a sequence of 12 distinct pressure messages, each corresponding to a pressure level"
[^r2]: arxiv-2511-20703 — "a sender with a higher authority level"
[^r3]: arxiv-2511-20703 — "contains a set of 6 × 12 pre-generated"
[^r4]: arxiv-2511-20703 — "decides to give up on task completion"
[^r5]: arxiv-2511-20703 — "for a maximum of 156 agent interactions"
[^r6]: arxiv-2511-20703 — "Measures the average pressure level"
[^r7]: arxiv-2511-20703 — "the rate and nature of safety degradation under pressure varies significantly between models"
[^r8]: arxiv-2511-20703 — "gradual, flatter curve, indicating higher resilience"
[^r9]: arxiv-2511-20703 — "rate by pressure level 4, whereas"
[^r10]: arxiv-2511-20703 — "baseline safety degrades dramatically when models are subjected to operational pressure"
[^r11]: arxiv-2511-20703 — "The entire interaction history"
[^r12]: arxiv-2511-20703 — "a steep, rapid increase"
