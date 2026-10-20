---
description: "A learned router sorts each query into an ordered complexity tier, and the tier selects the reasoning strategy from direct answer to tool use, so compute follows inferred difficulty."
aliases: ["elastic reasoning", "cognitive-inspired elastic reasoning", "CogER", "difficulty-tiered reasoning", "per-query reasoning-mode routing"]
sources: ["arxiv-2512-15089", "arxiv-2512-14048", "arxiv-2511-22850"]
---
# Complexity-tiered strategy routing

A query is first placed on an ordered scale of complexity, and the place on that scale decides how much reasoning it gets. The CogER paper uses four tiers. The lowest, L1, is "Queries with simple, unambiguous structure that require no reasoning" and is answered directly. L2 is a chain of thought on a moderately sized model, L3 is an extended chain of thought on a large reasoning model, and L4 lets the model call external tools inside its chain of thought.[^c1] Each tier is a strategy with its own cost, so the tier is also a price.

The tier is not read off the query by a fixed rule. The authors treat the choice as a sequential decision: "we model the process as a Markov Decision Process", and "train a CogER-Agent using reinforcement learning".[^c2] The motivation is stated as a measurement problem: "The true complexity of an incoming query is often not observable in advance".[^c3] A policy that must act before the difficulty is known has to learn, from outcomes, which tier pays off, and that is what separates this from a difficulty classifier.

The paper's own comparison supports this separation. A flat four-class classifier trained to predict query levels is one of its baselines, and "a four-class classifier underperforms the CogER" on the in-domain and out-of-domain sets.[^c4] The authors explain the gap by saying that "purely supervised routing is insufficient to capture the uncertainty of query difficulty".[^c4b] My reading of why: a supervised label fixes one tier per query, whereas an RL policy is scored on the answer it actually produces after its choice, so it can prefer a tier that is not the nominal difficulty when that tier yields correct answers more cheaply. The paper does not separate these two causes, so this is an interpretation, not a result.

What was measured. Against the test-time-scaling baseline S1-32B the paper reports a relative gain in average exact match, and attributes it to routing: "This is primarily attributed to its ability to route each" query to a strategy.[^c5] On cost, the router reports lower latency than the strongest single model: "CogER achieves SOTA accuracy while reducing latency by 76.58% (over 4 times faster)" than DeepSeek-R1.[^c6] The mapping of tiers onto a cognitive scale is borrowed: the authors say they are "inspired by Bloom's Taxonomy" and "first categorize incoming queries into four complexity" levels.[^c7] That taxonomy is a source of the tier names, not a validated measure of query difficulty.

A prompted router sets the tier in a second way. RoutingGen asks Qwen3-8B to label each code problem Simple or Complex, and "the classifier assigns q to one of two difficulty levels" with a textual rationale; Simple problems get few-shot direct generation and Complex ones a structured intention route.[^c11] The label is a prompt judgement rather than a learned policy, and it is not stable across judges: "the two models produce conflicting difficulty labels for 22.56% of HumanEval" tasks when Qwen3-8B and GPT-4o are compared.[^c12] The motivation is the cost of uniform structure on easy items: "indiscriminate use of complex prompting strategies often leads to overthinking on simple tasks".[^c13] The reported saving is a "46.37% relative reduction in total token usage across settings", with routing tokens counted.[^c14] The structured branch is described in [[intention-abstraction]].

A two-level version sits inside a document-QA pipeline. SLEUTH's difficulty agent reads the query together with the distilled evidence and places it on one of two levels, which the paper uses to adapt the reasoning strategy. The paper ties the choice to "complexity and evidence context, leading to consistent performance improvements across multiple" settings, so the level is set after the evidence is built, not from the bare question.[^c17] The authors call this binary estimate "but coarse, which may not capture intermediate reasoning cases."[^c16] Setting the level after evidence reverses the order of the CogER router above, where the tier is chosen from the query; the paper does not compare the two orders, so that contrast is mine.

## Limits

The tier is whatever the policy outputs during rollout. The paper notes that "the model may infer this level based on the context or internal reasoning".[^c8] So the scale is the model's own judgement, and nothing in the text checks it against an external difficulty measure.

The evaluation is narrow. CogER "has been validated on singleturn, text-only tasks".[^c9] The out-of-domain comparison is on arithmetic word problems and college mathematics: "we conduct experiments on MAWPS and CollegeMath".[^c10] Multi-turn dialogue, retrieval-heavy questions and open-ended answers are not tested in the text I read.

The cost comparison is in latency and generated words, with a parameter count for the mixture. It is not a fixed-budget comparison at matched accuracy, so the claim is about a better accuracy-cost point on these benchmarks, not about equal accuracy at lower cost on every workload.

The tiers are a fixed four-step ladder. Whether the same routing works with a finer or continuous scale, or with tiers whose strategies overlap, is not shown.

The prompted router has the same dependence on its judge, seen from the other side. The label moves with the classifier: GPT-4o, which is "a larger model than Qwen3-8B", "tends to classify a greater proportion of tasks as simple", so the same routing spends tokens differently depending on which model labels the tasks.[^c15] The comparison in the slices I read reports accuracy and tokens under each classifier, not whether either label matches an independent difficulty measure. A disagreement of about a fifth of HumanEval tasks is therefore a measured instability, not a settled difficulty ground truth.

## Related

- [[minimal-sufficient-level-reward]] — the reward that trains this router to prefer the lowest tier that suffices; without it the policy drifts to the most expensive tier.
- [[slo-reward-profile]] — another per-query router whose learned behaviour is set by the cost weights in its reward; the same trade-off seen from the reward side.
- [[intent-aware-response-strategy]] — routes each query to a response strategy by a discrete class; the same routing shape with intent in place of difficulty as the class.
- [[sufficiency-gated-imagination]] — first judges whether current evidence suffices before spending more; a cheapest-first policy without explicit tiers.
- [[tool-integrated-reasoning]] — what the top tier does: the chain of thought pauses for a tool call and resumes on its output.
- [[intention-abstraction]] — the structured branch in RoutingGen: a written specification and algorithm idea, sent to the problems a prompted classifier labels complex.
- [[evidence-dense-context-distillation]] — a two-level difficulty agent in a retrieval pipeline, set after the distilled evidence context is built.

[^c1]: arxiv-2512-15089 — "Queries with simple, unambiguous structure that require no reasoning"
[^c2]: arxiv-2512-15089 — "we model the process as a Markov Decision Process"
[^c3]: arxiv-2512-15089 — "The true complexity of an incoming query is often not observable in advance"
[^c4]: arxiv-2512-15089 — "a four-class classifier underperforms the CogER"
[^c4b]: arxiv-2512-15089 — "purely supervised routing is insufficient to capture the uncertainty of query difficulty"
[^c5]: arxiv-2512-15089 — "This is primarily attributed to its ability to route each"
[^c6]: arxiv-2512-15089 — "CogER achieves SOTA accuracy while reducing latency by 76.58% (over 4 times faster)"
[^c7]: arxiv-2512-15089 — "we first categorize incoming queries into four complexity"
[^c8]: arxiv-2512-15089 — "as the model may infer this level based on the context or internal reasoning"
[^c9]: arxiv-2512-15089 — "CogER has been validated on singleturn, text-only tasks"
[^c10]: arxiv-2512-15089 — "we conduct experiments on MAWPS and CollegeMath"
[^c11]: arxiv-2512-14048 — "the classifier assigns q to one of two difficulty levels"
[^c12]: arxiv-2512-14048 — "the two models produce conflicting difficulty labels for 22.56% of HumanEval"
[^c13]: arxiv-2512-14048 — "indiscriminate use of complex prompting strategies often leads to overthinking on simple tasks"
[^c14]: arxiv-2512-14048 — "46.37% relative reduction in total token usage across settings"
[^c15]: arxiv-2512-14048 — "tends to classify a greater proportion of tasks as simple"
[^c16]: arxiv-2511-22850 — "but coarse, which may not capture intermediate reasoning cases."
[^c17]: arxiv-2511-22850 — "complexity and evidence context, leading to consistent performance improvements across multiple"
