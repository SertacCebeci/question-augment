---
description: "Answering over a pre-built map can random-access the regions a query needs through zoom and viewpoint tools, so where to inspect is decoupled from the path needed to reach it."
aliases: ["active house-scale spatial reasoning", "AHSR", "map-directed exploration", "virtual spatial tool invocation", "random-access map inspection"]
sources: ["arxiv-2512-03284"]
---
# Query-conditioned map access

An answerer that already holds the world as a persistent map does not have to perceive all of it. It can ask for one region, or one viewpoint, that the question points at. The house-scale paper names this Active House-Scale Spatial Reasoning: a model "equipped with spatial tools and a pre-built house-scale 3D map" localizes and inspects only the regions the query needs.[^h1] The premise is that "the region relevant to a given query remains" in one place whatever the scene's size,[^h2a] so that "selectively directing perception toward query-relevant regions is both sufficient and efficient."[^h2] The paper states this as an observation that motivates the design; the text does not measure how often a query's relevant region is small.

The mechanism is a two-level interface. The model first sees only a coarse layer: the paper says it "observes only the coarse multi-floor context" of floor-level bird's-eye views.[^h3] Detail is then bought with tool calls. A zoom tool returns a magnified view of a region on one floor; a render tool returns a first-person view from a ground-plane position and yaw. "detailed regional and first-person observations are selected during inference conditioned on the query and the preceding interaction history."[^h4] Each returned observation is appended to the context, and the process is capped by a tool-call budget.

What transfers is the cost structure, not the vision model. In embodied question answering the evidence is gated by movement: observations are limited by "the navigable transitions required to reach a target region."[^h5] The map-access setting removes that gate. The paper says it "enables random access to the environment via virtual spatial tools," and that this decouples reasoning from "robotic movement," replacing "slow navigation with efficient, query-driven evidence gathering."[^h6] The learned policy is described as "separating the decision of where to inspect from the navigation required to reach that location."[^h7] So the question is no longer how to reach the evidence but which region to ask for, under a budget.

Training is two-stage. Supervised fine-tuning teaches the tool format and "template-based error-and-correction sequences" that show recovery from a bad zoom or view.[^h8] Reinforcement learning then sets the amount of exploration. The paper argues that a fixed reward would fail in one direction or the other: "A fixed exploration bonus may encourage unnecessary tool calls, whereas" "a fixed efficiency penalty may suppress information acquisition before sufficient evidence has been collected."[^h9] Its adaptive reward reads the success rate of the rollout group. When that rate is low it pays for distinct viewpoints; as success rises, the reward "shifts toward penalizing exploration beyond the budget."[^h10] A second term scores whether the views land on annotated reference regions, because the count of views alone "does not assess whether the acquired observations" are relevant.[^h11]

What was measured, on the authors' H2 U3D benchmark, with an 8B backbone: SFT alone reached 56.5%, and reinforcement learning raised it to 64.9% while "increases average tool calls from 1.97 to 3.79."[^h12] Removing error injection gave "57.1% and average tool calls to" 2.01, a 7.8-point drop; removing the exploration reward gave 59.7%, which the paper reports as "a 5.2-point drop."[^h13] Tool access alone is not the gain: "However, tool access alone does not" make the model explore well, and the same backbone with prompted tools scored 47.8%.[^h14]

## Limits

- One benchmark built by the authors, with 797 HM3D scenes. The comparison to the strongest passive baseline ("trails SpatialReasoner by 8.6 percentage points overall (56.3% vs. 64.9%)") is on that benchmark only.[^h15]
- The real-world check is small: "For each reconstructed scene, we manually create 30 questions, resulting in 60 questions in total."[^h16] The text reports it as supporting evidence, not as a generalization test.
- The relevant-region premise is asserted, not measured. Nothing in the text reports how large the query-relevant region is, or how often a coarse layer hides it. The paper's own training reward uses "the spatial annotations retained during dataset construction as soft reference" targets, so the notion of "relevant" is the annotator's, not an independent answer-based one.[^h17]
- The method assumes an accurate, pre-built map. The text does not test a stale, partial or wrong map, which is the case a persistent agent meets in practice.
- The error-injection data is template-generated and the budget is fixed at 8 calls. Whether the policy stops for the right reason, rather than when the budget runs out, is not separated in the text.
- The "first benchmark" claim is made "to the best of our knowledge"; the text describes no search method behind it, so it is a priority claim the wiki cannot verify from the text.

## Related

- [[query-first-selective-perception]] — the same question-first order for a video stream: intervals are chosen before frames are encoded; here the choice is a map region.
- [[coarse-to-fine-evidence-zoom]] — two-pass localize-then-zoom over a video; in map access the coarse layer is a floor-level map and the zoom is one tool call among several.
- [[question-conditioned-evidence-acquisition]] — an agent that calls a targeted perception tool each turn on one image; the same call-to-recover-evidence shape without a persistent map.
- [[benefit-scaled-tool-reward]] — rewards a tool call by its paired accuracy gain; the adaptive reward here is gated by the rollout group's success rate instead.
- [[evidence-localization-gap]] — localizing before reasoning hurt on figures where the located item had to be chosen. My reading, not the paper's: map access assumes the zoomed region can be read directly, which that gap suggests may not hold for every query.

[^h1]: arxiv-2512-03284 — "equipped with spatial tools and a pre-built house-scale 3D"
[^h2a]: arxiv-2512-03284 — "the region relevant to a given query remains"
[^h2]: arxiv-2512-03284 — "selectively directing perception toward query-relevant regions is both sufficient and"
[^h3]: arxiv-2512-03284 — "observes only the coarse multi-floor context"
[^h4]: arxiv-2512-03284 — "detailed regional and first-person observations are selected during inference conditioned on the query and the preceding interaction"
[^h5]: arxiv-2512-03284 — "the navigable transitions required to reach a target region"
[^h6]: arxiv-2512-03284 — "enables random access to the environment via virtual spatial tools"
[^h7]: arxiv-2512-03284 — "separating the decision of where to inspect from the navigation required to reach"
[^h8]: arxiv-2512-03284 — "template-based error-and-correction sequences"
[^h9]: arxiv-2512-03284 — "A fixed exploration bonus may encourage unnecessary tool calls, whereas"
[^h10]: arxiv-2512-03284 — "shifts toward penalizing exploration beyond the budget"
[^h11]: arxiv-2512-03284 — "does not assess whether the acquired observations"
[^h12]: arxiv-2512-03284 — "increases average tool calls from 1.97 to 3.79"
[^h13]: arxiv-2512-03284 — "Removing error injection reduces accuracy to 57.1% and average tool calls to"
[^h14]: arxiv-2512-03284 — "However, tool access alone does not"
[^h15]: arxiv-2512-03284 — "trails SpatialReasoner by 8.6 percentage points overall (56.3% vs. 64.9%)"
[^h16]: arxiv-2512-03284 — "For each reconstructed scene, we manually create 30 questions, resulting in 60 questions in total"
[^h17]: arxiv-2512-03284 — "the spatial annotations retained during dataset construction as soft reference"
