---
description: "When a judge rejects a short plan, discarding only that plan and sampling a new one, with rejected plans kept as a failure history, costs a short prefix rather than a full wrong answer."
aliases: ["Rewind-and-Repeat", "R&R", "iterative plan rejection sampling", "plan rewind"]
sources: ["arxiv-2512-03176"]
---
# Plan-prefix rewind

A model that writes its plan before reasoning produces a cheap thing to check. The inference-time procedure in the paper uses that check. The model proposes one plan. A judge accepts or rejects it. If it is rejected, the process is "rewound such that the rejected plan is appended to a history of failures, and the model is re-prompted" to produce a new, distinct plan.[^c1] The loop "continu[es] until an acceptable plan is found or a retry budget is exhausted."[^c2]

The mechanism is the cost. Only the plan is regenerated, so the rejected work is a short prefix and not a full response. The paper states this as: "only short plan prefixes are resampled rather than full generations."[^c3] After a rejection the next thinking block is short, because "the model only needs to adjust the plan rather than regenerate full reasoning."[^c4] The failure history does the work of a memory: the model is not sent back to a plan it already saw fail.

The contrast in the paper is with Best-of-N on plans. There the model samples several plans in parallel at high temperature and the judge picks one. In rewind-and-repeat, "the model proposes one plan at a time, which user can accept or reject."[^c5] The two differ in when the check happens: rewind checks each plan before the next is drawn, so the judge's decisions shape the sequence of samples. The paper's accounting is that rewind is sequential but the overhead is small: "the short length of each thought block results in negligible overhead relative to" the full rollout.[^c6]

## What is measured

Table 4 of the paper reports how often a rewind happens. "On average, only 22% of plans require a rewind," and "Across all benchmarks, only 20–25%" of plans do.[^c7] Of those, "the majority of those are corrected on the first retry (60–65%)."[^c8] The paper also reports that over 80% of corrections succeed, which is the approval rate of the same autorater, not of a person.

The accuracy effect is reported at the plan stage against the answer stage. For Qwen3-4B, "R&R (Plan) boosts MATH500 accuracy from 84.4" to a higher figure while keeping TTFR near 578 tokens, and the paper calls this "over 7× faster than R&R (Answer)."[^c9] The authors read the mechanism this way: "most initial plans are already well-formed and R&R primarily serves to re-ground" the reasoning early.[^c10] That reading is theirs, and it fits the counts: most plans are not rewound, so the gain comes from a minority of prompts.

The procedure sits in the same wiki line as the trigger designs in [[plan-level-retrospection]]. There the agent decides, from its own judgment, that a trajectory is stuck and rebuilds a decomposition. Here the trigger is external, a judge reading the prompt and the plan, and the repair is a fresh sample of a short prefix. My inference: the two solve different parts of the same problem. Retrospection repairs the structure of the work; rewind repairs its starting point before the work is spent. The failure history plays the role of the planning-history archive described in [[context-register]], and my reading is that it does the same job of keeping a dead plan from returning.

## Limits

- The judge is an LLM autorater standing in for a user. The paper's design choice is "information asymmetry" between the model and the autorater: the judge sees the prompt and plan, not the thoughts.[^c11] That makes the simulation honest about what a user sees, but no user judged a plan. The authors also note that the judge "introduces nontrivial latency and may reflect biases of the" underlying model.[^c12] My inference: a biased judge would change which plans are accepted, and the text does not measure that.
- The 80% correction rate is the autorater's approval rate. It is not a measure of whether a corrected plan led to a correct answer for a person who wanted something else. The paper's own accuracy numbers are pass@1 on checkable tasks.
- Latency is reported on the first plan. The paper says "we compute TTFR based on the first generated plan, even if it is" later rejected.[^c13] The cost of rewinds therefore appears in total tokens, not in the latency figure a user would feel. Rewinds delay the accepted plan, and the reported latency does not show by how much.
- The gain is small and concentrated. Only a fifth to a quarter of plans are rewound, so the accuracy change rests on a minority of prompts. The paper does not report variance across runs in the text read here.
- The procedure needs a checkable plan. On open-ended questions the judge has nothing firm to reject against, and the text does not test that case.

## Related

- [[interleaved-reasoning]] — the trained behavior that makes the first intermediate response a plan, which this procedure needs
- [[plan-level-retrospection]] — a self-triggered rebuild of a decomposition; rewind is judge-triggered and resamples only a short prefix
- [[context-register]] — the planning-history archive that keeps dropped plans from re-entering; the same job as the failure history here

[^c1]: arxiv-2512-03176 — "rewound such that the rejected plan is appended to a history of failures, and the model is re-prompted"
[^c2]: arxiv-2512-03176 — "continuing until an acceptable plan is found or a retry budget is exhausted"
[^c3]: arxiv-2512-03176 — "since only short plan prefixes are resampled rather than full generations"
[^c4]: arxiv-2512-03176 — "the model only needs to adjust the plan rather than regenerate full reasoning"
[^c5]: arxiv-2512-03176 — "the model proposes one plan at a time, which user can accept or reject"
[^c6]: arxiv-2512-03176 — "sequentially, though the short length of each thought block results in negligible overhead relative to"
[^c7]: arxiv-2512-03176 — "On average, only 22% of plans require a rewind"
[^c8]: arxiv-2512-03176 — "the majority of those are corrected on the first retry (60–65%)"
[^c9]: arxiv-2512-03176 — "over 7× faster than R&R (Answer)"
[^c10]: arxiv-2512-03176 — "most initial plans are already well-formed and R&R primarily serves to re-ground"
[^c11]: arxiv-2512-03176 — "introducing information asymmetry"
[^c12]: arxiv-2512-03176 — "introduces nontrivial latency and may reflect biases of the"
[^c13]: arxiv-2512-03176 — "we compute TTFR based on the first generated plan, even if it is"
