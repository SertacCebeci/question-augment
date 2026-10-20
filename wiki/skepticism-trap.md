---
description: "Aggregate accuracy cannot tell discernment from blanket skepticism: a model can reach high Safety by rejecting valid claims too, visible only when Utility and Safety are scored separately."
aliases: ["over-refusal trap", "over-conservatism on valid claims"]
sources: ["arxiv-2602-08939", "arxiv-2511-21460"]
---
# Skepticism Trap

CausalT5k builds matched Sheep cases (valid causal designs) and Wolf cases (inferential traps). Utility is the acceptance rate of valid claims; Safety is the rejection rate of invalid ones.[^c1] Scored on accuracy alone, a model that says "no" to everything looks merely mediocre. Split into the two axes, it shows high Safety and low Utility.

The measured case: Claude Haiku 3.5 reaches 96% Safety but only 40% Utility on a 100-case seed set, so it rejects many valid causal claims.[^c2] The authors' reading: "a model that says 'no' too often can look safe while failing to recognize legitimate causal evidence."[^c3] The trap is that the refusal metric rewards the very behaviour that hides the failure.

The same error direction shows up in embodied household safety, where the unit is a task instruction rather than a causal claim. A safety-prompted model reaches high rejection of unsafe tasks but also flags safe ones: "20%–42% of inherently safe instructions as harmful."[^c4] The paper reads this as a cost of the prompt itself: "naive safety prompting tightens the" model's boundary "indiscriminately."[^c5] One debate-with-critic pipeline is reported to cut the safe-side error without giving up the unsafe side, as described in [[process-scored-critic]]; that is a single paper's measurement, not a second Utility/Safety split.

For asking and answering, the mechanism is that answer quality has two error directions, and a single score averages them. Over-refusal is a distinct failure from sycophancy; both are invisible to one number, and the paired Sheep/Wolf design is what separates them.

## Limits

One model, N = 100 seed set; the paper presents it as the counter-intuitive instance, not a population rate. The seed sets are balanced diagnostic samples, explicitly not estimates of full-benchmark accuracy. Whether the pattern generalizes beyond causal-claim classification is untested here.

## Related

- [[wise-refusal]] — refusal that is correct because it is grounded in a diagnosed trap
- [[sycophantic-capitulation]] — the opposite error direction, measured with paired pressure variants
- [[calibration]] — Utility/Safety is a two-sided calibration check
- [[expected-utility]] — the two error costs a single accuracy figure averages away
- [[process-scored-critic]] — a debate critic that scores reasoning, reported to reduce the safe-side error of a single-agent safety prompt

[^c1]: arxiv-2602-08939 — "Utility measures acceptance of valid claims, while Safety"
[^c2]: arxiv-2602-08939 — "it achieves 96% Safety, meaning it rejects most invalid causal"
[^c3]: arxiv-2602-08939 — "a model that says “no” too often can look safe"
[^c4]: arxiv-2511-21460 — "20%–42% of inherently safe instructions as harmful"
[^c5]: arxiv-2511-21460 — "naive safety prompting tightens the"
