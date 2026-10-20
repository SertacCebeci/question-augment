---
description: "Routing is credited only if it beats random choice of the same number of items; the route-count-matched control separates which questions get retrieval from how many do."
aliases: ["route-count-matched random control", "count-matched random allocation", "matched random routing", "random verifier baseline", "random-scoring control"]
sources: ["doi-10-48550-arxiv-2607-25600", "arxiv-2512-05809"]
---
# Route-count-matched random control

A router that sends some questions to retrieval can look better than a baseline for two different reasons: it picks the right questions, or it sends a different number of them. The route-count-matched control separates the two. Within one dataset–model cell it counts how many questions the router sent to retrieval, then selects exactly that many by a fixed pseudo-random ordering: "a stable SHA-256 ordering selects exactly the same number of questions for retrieval".[^c1] Selected questions take their always-retrieval output and the rest take their no-retrieval output. The control therefore needs no new model calls; it recombines outputs already produced by the static policies.[^c2]

What the control isolates is the choice, holding the count fixed. The paper states its purpose as testing "whether confidence selects more useful questions than random routing at the same route count".[^c3] On that test, the confidence router beat the random control in 17 of 18 dataset–model cells, with an average gain of 0.024 F1.[^c4] The same logic appears in the paper's conclusion, where the advantage over matched random routing is read as showing that "verbalized confidence provides useful question-level allocation signals".[^c9] The point is that a score can be poorly calibrated as a probability and still order questions usefully; the matched control is the test that can tell ordering value from simply retrieving less or more.

The mechanism is simple. A random arm with the same count spends the same retrieval budget and the same number of always-retrieval answers, so any difference in F1 comes from which questions were assigned to retrieval. If the router's ordering carries no information about retrieval benefit, the two arms should match on average. The control does not need a model of why the ordering works; it only needs the count and the two static outputs.

My inference, not the paper's: the design transfers beyond retrieval to any rule that spends a fixed number of expensive actions across items. Any such rule can be audited by a count-matched random arm, and the same audit can show when a score's gain is just a shift in how often the action fires.

The same matched-random arm has been run on a different kind of choice: which imagined world-model views a VLM should use. The paper compares MindJourney's VLM helpfulness score with a random scorer at the same top-k. On the entropy of the answer distribution, "random selection surprisingly produces lower entropy, and hence better calibration than MJ’s helpfulness scoring."[^c11] On SAT-Real at beam depth 1, "the random verifier remains surprisingly competitive".[^c10] The paper's reading is that the heuristic score "is fundamentally misaligned with reasoning quality".[^c12] Here the random arm is the test that shows a verifier's signal is no better than chance on the chosen measure, which is the same role the count-matched arm plays for routing.

## Limits

- The entropy comparison rests on "over the answers of 50 randomly" drawn SAT-Real questions and one backbone, InternVL3-14B.[^c13] My inference: lower entropy is a confidence measure, so a random scorer can lower it without any gain in correctness; the matched arm tests the verifier against chance on that measure, not against the right answer.
- Equal route counts do not mean equal evidence. Some retrieval calls return fewer than five passages, so "equal route counts do" not imply identical returned-passage counts.[^c5] The control matches decisions, not retrieval volume.
- The control does not run the router's own path. It "evaluates allocation rather than a fully execution-matched causal effect".[^c6] The random arm also omits the router's probe: the paper says its token counts "exclude an independently executed routing probe".[^c7] Token comparisons between the arms are therefore not like-for-like.
- The gain is an average over heterogeneous cells. The paper reads its aggregate result as "rather than evidence of universal dominance".[^c8] Beating random in 17 of 18 cells is a count of cells, not a test of each one.
- My inference: one fixed ordering is one draw. The paper reports a single deterministic hash, so the spread of the random arm over other draws is not shown here.
- My inference: the control holds the count fixed and compares only the choice. It says nothing about whether a router with a different count would do better, which is a separate question.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the retrieve-or-not gate whose allocation this control audits
- [[matched-budget-evidence-comparison]] — a matched-budget control on a different axis: matched words of context, not matched routed items
- [[calibration]] — the property the control does not test; ordering value and calibrated probability can come apart
- [[test-time-scaling]] — the world-model verifier case, where a random scorer at matched top-k is the competitive baseline

[^c1]: doi-10-48550-arxiv-2607-25600 — "a stable SHA-256 ordering selects exactly the same number of questions for retrieval"
[^c2]: doi-10-48550-arxiv-2607-25600 — "Both controls are deterministic and post hoc and require no additional model calls"
[^c3]: doi-10-48550-arxiv-2607-25600 — "whether confidence selects more useful questions than random routing at the same route count"
[^c4]: doi-10-48550-arxiv-2607-25600 — "allocation in 17 of 18 settings, with an average gain of 0.024"
[^c5]: doi-10-48550-arxiv-2607-25600 — "calls return fewer than five passages, equal route counts do"
[^c6]: doi-10-48550-arxiv-2607-25600 — "it therefore evaluates allocation rather than a fully execution-matched causal effect"
[^c7]: doi-10-48550-arxiv-2607-25600 — "exclude an independently executed routing probe"
[^c8]: doi-10-48550-arxiv-2607-25600 — "rather than evidence of universal dominance"
[^c9]: doi-10-48550-arxiv-2607-25600 — "verbalized confidence provides useful question-level allocation signals"
[^c10]: arxiv-2512-05809 — "the random verifier remains surprisingly competitive"
[^c11]: arxiv-2512-05809 — "random selection surprisingly produces lower entropy, and hence better calibration than MJ’s helpfulness scoring"
[^c12]: arxiv-2512-05809 — "is fundamentally misaligned with reasoning quality"
[^c13]: arxiv-2512-05809 — "over the answers of 50 randomly"
