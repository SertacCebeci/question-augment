---
description: "Reasoning is cut into self-contained propositions, each verified by its own on-demand look at the source before the next begins; the unit of re-consultation is the proposition, not the step."
aliases: ["Reason Chunking", "critical reasoning units", "information chunking"]
sources: ["arxiv-2512-14654"]
---
# Reason chunking

Reason chunking is a way of structuring a multi-step answer around propositions rather than around single steps. The paper that names it (ViRC) starts from Miller's capacity figure, "short-term memory is limited to approximately seven (±2) chunks of information", and takes a chunk to be a grouping of items into one unit.[^c1] Applied to multimodal math, the solution becomes a sequence of Critical Reasoning Units (CRUs): the method "structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs)".[^c2] Each unit has a visual context and a set of textual steps, and the steps "jointly verify a semantically complete proposition".[^c3]

The point of the unit is where visual information is re-consulted. The paper objects to visual chain-of-thought because "it indiscriminately injects visual signals regardless of necessity", that is, a fresh visual look before every step.[^c4] In its place, the image is consulted "through on-demand visual grounding", once per proposition.[^c5] Within a unit the text stays coherent and checks one intermediate claim; across units the visual context is refreshed so the next proposition can be formed.

The formalism places the two familiar schemes at the ends of one family. Text-only CoT is "a degenerate case with a single" CRU that uses the full image once.[^c6] Visual CoT is the opposite extreme, in which "each reasoning step forms its own CRU".[^c7] Reason chunking lies between them, and the transfer from the cognitive claim to the machine is by analogy: the paper states that the decomposition "conforms to Miller's Law" but does not measure chunk capacity in the model.

The units are produced by a pipeline. Sampled reasoning paths are split into fine steps, and "steps associated with the same proposition are grouped into a semantically coherent CRU".[^c8] Each unit is then attached to an image region and a guiding question for the next unit. Four cognitive patterns (planning, reflecting, verifying, backtracking) are realised as crop, scale and display calls over these units. The verifying pattern, for example, makes the model "re-examine relevant visual evidence before advancing to the next proposition".[^c9]

What was measured is a comparison of the full method against a variant without the CRU structure, which the paper reads as the step-wise visual CoT process. The caption states the CRU structure is "substantially outperforming the step-wise Visual CoT process" on the math and high-resolution benchmarks.[^c10] The reasoning-pattern ablation adds a further detail: the patterns help in combination, and "augmentation underperforms the planning-only configuration" in some single-pattern cases, so no one pattern carries the gain.[^c11]

## Limits

- The Miller link is an analogy. The paper cites the seven-chunk figure but does not test whether the unit size tracks any capacity; the boundary of a unit is set by the annotation ("a semantically complete proposition"), not by a measured limit.
- The units are labels made by a generation pipeline ("a three-stage annotation pipeline for reasoning path generation of mathematical problems").[^c12] Whether the grouping of steps into propositions is stable across different annotators, generators or problem types is not tested in the sections read.
- The evaluation is one 7B backbone (the ablation uses Qwen2.5-VL-7B as its baseline) and math plus high-resolution benchmarks. Nothing read here shows the unit beyond mathematical diagrams.
- The control "w/o CRU" is read here as the step-wise visual CoT condition. The sections read do not say whether that control was trained on the same CRUX annotations, so the gain may mix the data with the structure. This is my reading of the table, not a figure the paper states.
- The claim that chunking improves "cognitive efficiency" alongside accuracy is stated as a benefit of the design.[^c13] Token or latency cost of the chunked versus per-step schemes is not reported in the sections read; the efficiency case rests on the redundancy argument.
- A proposition boundary is not a visual boundary. A unit whose propositions need evidence from two regions would still refresh the view once; the paper does not test that case.

## Related

- [[on-demand-resolution-zoom]] — the same move, looking again on request mid-reasoning, but for a single request in video; reason chunking places the request at proposition boundaries.
- [[confidence-triggered-visual-reattention]] — one crop-and-zoom re-query gated by answer confidence; there the trigger is the model's own uncertainty, here it is the end of a unit.
- [[latent-visual-thought]] — interleaving visual and textual reasoning without tools; a different medium for the same question of when the image is consulted.
- [[backward-chaining-subgoal-decomposition]] — decomposing a problem into the intermediate conditions it needs; the propositions of a CRU are of that kind, though the paper does not frame them that way.

[^c1]: arxiv-2512-14654 — "short-term memory is limited to approximately seven (±2) chunks of information"
[^c2]: arxiv-2512-14654 — "structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs)"
[^c3]: arxiv-2512-14654 — "consists of mi ≥ 1 coherent textual steps that jointly verify a semantically complete proposition"
[^c4]: arxiv-2512-14654 — "Although VCoT enhances step-wise visual grounding, it indiscriminately injects visual signals regardless of necessity"
[^c5]: arxiv-2512-14654 — "validated through on-demand visual grounding"
[^c6]: arxiv-2512-14654 — "CoT corresponds to a degenerate case with a single"
[^c7]: arxiv-2512-14654 — "each reasoning step forms its own CRU"
[^c8]: arxiv-2512-14654 — "Steps associated with the same proposition are grouped into"
[^c9]: arxiv-2512-14654 — "re-examine relevant visual evidence before advancing to the next proposition"
[^c10]: arxiv-2512-14654 — "substantially outperforming the step-wise Visual CoT process"
[^c11]: arxiv-2512-14654 — "augmentation underperforms the planning-only configuration"
[^c12]: arxiv-2512-14654 — "We employ a three-stage annotation pipeline for reasoning path generation of mathematical problems"
[^c13]: arxiv-2512-14654 — "improving both accuracy and cognitive efficiency"
