---
description: "Externalizing evidence into a queryable structure lets a model fetch only the cues each step needs, instead of reading one entangled input; in zero-shot 3D grounding this raised accuracy."
aliases: ["active graph traversal", "VLM ⊗ SI", "queryable scene graph reasoning"]
sources: ["arxiv-2512-09215"]
---
# Incremental structure retrieval

When the evidence for a question is spread over a large, cluttered store, one way to answer is to hand the reasoner the whole store at once. The alternative examined here keeps the store outside the reasoner and lets the reasoner ask for part of it at a time. The reasoner becomes an agent that moves through the structure and opens only the cues the current step requires. The authors state the principle by analogy to search: "we retrieve relevant information step-by-step, progressively," and the design aims at letting the model operate "as an active agent that selectively" accesses cues.[^c1]

The mechanism appears in View-on-Graph (VoG), a method for zero-shot 3D visual grounding, where a text query names one object in a 3D scene. The authors contrast a "VLM ⊕ SI" input, in which the model "passively consumes" the whole spatial information as composite renderings,[^c2] with a "VLM ⊗ SI" design. The scene is organized as a multi-layer graph: view nodes hold multi-view images, object nodes hold detected objects, inter-layer edges connect each view to the objects visible in it, and intra-layer edges link adjacent viewpoints. Each step alternates exploration, which moves along graph edges, and reasoning, which checks candidate objects from the views already visited. Earlier and current views are kept in view by "placing previously explored views in the topleft and current candidate views in the remaining slots," and a growing pool of objects seen so far serves as the candidate set.[^c3] The loop ends when an object is selected or the depth limit is reached; in the latter case "a forced global reasoning step is performed over the accumulated multi-view and" multi-object evidence.[^c4]

The measured claim is accuracy against variants of the same system. In the ablation, run "on ScanRefer" with an open 2B vision-language model, the authors report that "absence of all structure (S7) causing the largest drop."[^c5][^c6] Multi-round reasoning beats giving all information at once, "as it allows incremental retrieval and reasoning at each step."[^c7] The authors credit the gain on small models to "applying incremental retrieval, only the most relevant" cues being passed at each step, which they describe as reducing cognitive load.[^c8] Graph traversal is a second ingredient: it filters candidates each round, and "graph traversal prevents VoG from overexploring irrelevant regions."[^c9] Without it, the paper says, "causing most reasoning paths to fail even reaching Dmax."[^c10] Depth helps only up to a point: "depth, but the gain saturates beyond 4 since most questions" need no more.[^c11]

The transfer is loose. What carries over is a division of labour: the structure holds the whole store, the reasoner holds a small working set and decides what to open next, and the sequence of those decisions is itself an inspectable trace. What does not carry over is the object of search. Here the target is a fixed object, the edges encode spatial adjacency and visibility, and success is grounding accuracy. In a question-answering setting the analogue of a view would be an evidence unit with its own links, and this paper does not test that. My reading is that the design choice being examined is the interface between store and reasoner, not the graph as such.

## Limits

- The explanation of why incremental access helps is the authors'. The ablations show that traversal and context integration each matter, but the multi-round comparison is against a variant that randomly selects view nodes each round, so it isolates the scheduling of views, not the reasoning's reliance on the graph.
- The authors flag one of their own conditions: the variant that annotates each image with a global object ID is a form of view-object relation, and its conclusions "should be considered with reservation."[^c12]
- The method fails in fully axis-symmetric scenes, where it selects a visually similar view on the opposite side.[^c13]
- The starting view matters. Letting the model choose the start directly hurts, because "searches stop at step 1 because the chosen view already contains most query-related information, discouraging further" exploration.[^c14]
- Graph size is a dial too: beyond 32 view nodes, "candidates per round make selection harder and slightly degrade performance."[^c15]
- The claim that the structure lowers the model's reasoning difficulty is argued from the design. I did not find an experiment that measures reasoning difficulty directly; the evidence is accuracy and step counts.
- The tests read here are on 3D grounding benchmarks with open 2D vision-language models. Whether the gain holds when the store is text, or when the model is a large closed one, is not shown in the parts of the paper I read.

## Related

- [[sequential-window-reading]] — the same stop-when-sufficient loop over a ranked list of text windows; there the window order is the dial, here the graph's edges decide what is reachable.
- [[structural-neighborhood-expansion]] — widening retrieval along a structure from seeds under a budget; close to the traversal half, but without a reasoner choosing each step.
- [[attention-bottleneck-under-cheap-access]] — the other side of the same economy: when access to inputs is cheap, the limit moves to processing them.

[^c1]: arxiv-2512-09215 — "enabling the VLM to operate as an active agent that selectively"
[^c2]: arxiv-2512-09215 — "where the VLM passively consumes"
[^c3]: arxiv-2512-09215 — "placing previously explored views in the topleft and current candidate views in the remaining slots"
[^c4]: arxiv-2512-09215 — "a forced global reasoning step is performed over the accumulated multi-view and"
[^c5]: arxiv-2512-09215 — "We conduct our ablation studies on ScanRefer, use the open-source Qwen2VL-2B as the VLM"
[^c6]: arxiv-2512-09215 — "absence of all structure (S7) causing the largest drop"
[^c7]: arxiv-2512-09215 — "as it allows incremental retrieval and reasoning at each step"
[^c8]: arxiv-2512-09215 — "applying incremental retrieval, only the most relevant"
[^c9]: arxiv-2512-09215 — "graph traversal prevents VoG from overexploring irrelevant regions"
[^c10]: arxiv-2512-09215 — "causing most reasoning paths to fail even reaching Dmax"
[^c11]: arxiv-2512-09215 — "depth, but the gain saturates beyond 4 since most questions"
[^c12]: arxiv-2512-09215 — "should be considered with reservation."
[^c13]: arxiv-2512-09215 — "VoG struggles in fully axis-symmetric scenes."
[^c14]: arxiv-2512-09215 — "searches stop at step 1 because the chosen view already contains most query-related information, discouraging further"
[^c15]: arxiv-2512-09215 — "candidates per round make selection harder and slightly degrade performance."
