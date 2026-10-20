---
description: "A VLM first writes a JSON-style list of the question's relevant objects, with boxes, sizes and attributes, then reasons over that list instead of scattered coordinates or crops."
aliases: ["thinking with blueprints", "object-file blueprint", "structured object representation", "JSON blueprint for spatial reasoning"]
sources: ["arxiv-2601-01984"]
---
# Object-centric blueprint

The mechanism is a two-stage trace. Before any analysis, the model writes out a structured inventory of the objects that bear on the question. Each entry is an object: a short thought on how it was identified, an entity name, a bounding box, and a natural-language attribute.[^c1] Only after the inventory is written does the trace analyse it and emit an answer. The observation (building the list) and the reflection (reading the list) therefore occupy separate parts of the output, which the paper presents as the feature that distinguishes it from prior methods: "it separates the observation (constructing the blueprint)" from the reflection.[^c2]

The motivation is borrowed from cognitive science. Visual signals are first bound into individuated object files, which together form an object-centric layout; reasoning then scans that layout to answer spatial questions.[^c3] The paper reads the two prevailing VLM alternatives against this picture. Local-patch methods are credited with "improving fine-grained perception but weakening global spatial awareness".[^c4] Coordinate-marking methods are effective for locating objects but "rely on scattered and isolated coordinates rather than organized entities".[^c5] The blueprint is meant to supply the missing global layer: it "provides a global and coherent spatial context for reasoning", so the model does not depend on fragmented cues.[^c16]

Producing such traces is itself a construction problem. The paper notes that "typical spatial reasoning datasets contain only image" question and answer triplets, with no blueprint-guided trace to learn from,[^c15] and that "existing VLMs cannot directly produce such" traces.[^c6] The authors prompt a strong teacher VLM for atomic steps (add an object, analyse the blueprint, answer), assemble them with Monte Carlo Tree Search, and keep "the traces that lead to correct answers" along with traces that backtrack to a correct answer.[^c7] The base model, Qwen2.5-VL, is then supervised on these traces and further trained with reinforcement learning under blueprint-aware rewards (see [[object-cardinality-reward]] and [[answer-reasoning-consistency-reward]]).

On the reported benchmarks the pipeline gives "a 35.9% improvement over the base Qwen2.5-VL" on the SAT subset used for training, and "further yields gains of 4.3%, 3.5%, and 1.2%" on out-of-distribution sets.[^c8] The abstract states that "Experiments show that our method consistently" outperforms the compared VLMs and specialised spatial models.[^c9] The ablation supports the RL stage: removing it "also yields performance degradation across all benchmarks".[^c10]

The authors also apply the same blueprint to video by selecting frames with a CLIP-based module, without retraining. The evidence for this is a single example: "Figure 5 provides an example", and the paper says "we find that it can be applied" to videos.[^c11]

## Limits

- Training uses only synthetic scene images: "Our training relies on SAT, which contains synthetic scene images". The out-of-distribution gains on real-image sets are a few points, and the paper names more diverse data as the first limitation.[^c12]
- Only the 7B model is tested. "Larger VLMs (e.g., 32B) have not been explored due" to compute.[^c12]
- The blueprint records "the rough positions, sizes" of objects.[^c13] The text I read reports no measure of box accuracy, so it does not show that the blueprint geometry is correct, only that the answers improve.
- The ablation row (D) removes SFT, the blueprint and the blueprint techniques together. The paper's result therefore shows that the whole recipe beats vanilla GRPO, not that the blueprint alone accounts for the gain. This separation is my reading of the table, not a claim the authors make.
- Blueprint size matters. With too few objects the analysis rests on incomplete information, and with too many, irrelevant objects can mislead it.[^c14] The paper's answer to this is a reward, which is itself a fixed heuristic.
- The video result rests on one example and no reported metric in the text I read.
- The comparison claims are on the paper's own benchmarks and against the baselines it chose. Nothing here tests whether the structure helps on tasks that need no spatial layout.

## Related

- [[object-cardinality-reward]] — the reward that sizes the blueprint's object list
- [[answer-reasoning-consistency-reward]] — the reward that ties the final answer to the blueprint-guided reasoning
- [[sufficiency-gated-imagination]] — another SAT-trained spatial method; it decides whether to gather more evidence rather than structuring what is already seen
- [[cedi-graph-guided-examiner]] — walks a scene-graph state space; a structured object representation used for probing rather than answering
- [[referent-match-set-ambiguity]] — a scene made queryable step by step, the same move as building the object list before reasoning over it

[^c1]: arxiv-2601-01984 — "Each object oi comprises a thought si describing how the object is identified"
[^c2]: arxiv-2601-01984 — "it separates the observation (constructing the blueprint)"
[^c3]: arxiv-2601-01984 — "visual signals are first bound into individuated object files"
[^c4]: arxiv-2601-01984 — "improving fine-grained perception but weakening global spatial awareness"
[^c5]: arxiv-2601-01984 — "rely on scattered and isolated coordinates rather than organized entities"
[^c6]: arxiv-2601-01984 — "existing VLMs cannot directly produce such"
[^c7]: arxiv-2601-01984 — "We retain both the traces that lead to correct answers"
[^c8]: arxiv-2601-01984 — "our method achieves a 35.9% improvement over the base Qwen2.5-VL on this benchmark"
[^c9]: arxiv-2601-01984 — "Experiments show that our method consistently"
[^c10]: arxiv-2601-01984 — "also yields performance degradation across all benchmarks"
[^c11]: arxiv-2601-01984 — "Figure 5 provides an example"
[^c12]: arxiv-2601-01984 — "Our training relies on SAT, which contains synthetic scene images"
[^c13]: arxiv-2601-01984 — "records the rough positions, sizes, and"
[^c14]: arxiv-2601-01984 — "if the blueprint includes too few objects, the"
[^c15]: arxiv-2601-01984 — "typical spatial reasoning datasets contain only image"
[^c16]: arxiv-2601-01984 — "blueprint provides a global and coherent spatial context for reasoning"
