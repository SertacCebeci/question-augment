---
description: "Scoring a visual reasoning trace by matching each object it names to a ground-truth mask gives two numbers, mention coverage and spatial precision, which a correct final answer does not reveal."
aliases: ["Logical Quality and Visual Quality", "LQ and VQ", "mask-matched trace score", "visual trace fidelity"]
sources: ["arxiv-2512-05091"]
---
# Object-grounded trace scoring

A visual reasoning trace can be checked against the image, not only against its final answer. In the Visual Reasoning Tracer setup, each reasoning step is paired with the object it names: the trace is a sequence of pairs in which each step t_i is "a natural language reasoning step that usually corresponds to a visual region in the image, and m_i is a segmentation mask corresponding to the visual object(s) mentioned in t_i".[^c1] Because every mentioned object carries a mask, the trace can be compared with ground-truth masks directly. The authors present this as a deliberate alternative to judging with another model: "Our design avoids reliance on problematic approaches like artificial formats and LLM-based evaluators."[^c2]

The comparison is a bipartite matching. Predicted and ground-truth masks are paired by maximising total IoU, solved with the Hungarian algorithm, and a predicted object counts as identified when its matched IoU exceeds a threshold.[^c3] In the paper that threshold is τ = 0.5.[^c4] Two scores follow from the matching. Logical Quality (LQ) is the fraction of ground-truth visual objects that the trace mentions, |V_pred ∩ V_GT| / |V_GT|. It asks whether the reasoning attends to the parts of the image the question needs and names them in a recognisable way.[^c5] Visual Quality (VQ) is computed only over the identified traces and is their mean mask IoU. It asks how spatially precise those references are.[^c6]

The reason to keep these apart from the answer is that they can diverge. The final answer is scored separately, as mask IoU on the output (the "A" column). In the benchmark, grounding and segmentation baselines keep some answer accuracy while producing no valid trace: they "completely fail to generate valid reasoning outputs (scoring zero on R-LQ and R-VQ)".[^c7] The same divergence appears inside one model family. Reinforcement learning raised answer mIoU from 59.5 to 62.1 while the trace did not improve. The authors read the answer gain as chain-of-thought that "guides the model to the correct final answer more effectively even without finer-grained segmentation in the reasoning steps".[^c8] A single accuracy number records only the answer; the two trace scores record whether the answer was reached through named, located objects.

## Limits

- The score is only as good as its ground truth. A correct object whose predicted mask falls below τ counts as unidentified, and the paper reports no sensitivity analysis over τ. This is my inference from the definition, not a tested result.
- LQ measures mention, not use. A trace can name the needed object and still reason from something else, and the metric does not test whether the named object carried the inference. The phrase "logical quality" is the authors' label for coverage.
- VQ is averaged only over identified traces, so a model that identifies few objects can post a high VQ on a small, easy subset. Reporting LQ beside VQ partly guards against this. This too is my reading.
- The formalism needs objects with segmentable extents. Text-only reasoning has no mask to match. Any analogue, such as matching spans to gold passages, is my analogy and is not tested here.
- The training data are machine-generated and the evaluation set was filtered by people, because "synthetically generated data can contain noise or error samples".[^c9] The numbers come from one benchmark and one model family, so the size of the answer-trace gap is not established across settings.

## Related

- [[grounding-answer-dual-axis-audit]] — the same split between answer correctness and evidence localization, in a crop-overlap setting rather than mask matching
- [[perception-step-faithfulness]] — also scores intermediate visual claims against the image, rather than the final answer alone
- [[final-output-gap]] — the reverse case: a correct trace overridden by a wrong output

[^c1]: arxiv-2512-05091 — "a segmentation mask corresponding to the visual object(s)"
[^c2]: arxiv-2512-05091 — "Our design avoids reliance on problematic approaches like artificial formats and LLM-based evaluators."
[^c3]: arxiv-2512-05091 — "We establish this correspondence using bipartite matching"
[^c4]: arxiv-2512-05091 — "j and their IoU score Wij exceeds a predefined threshold τ (e.g., τ = 0.5)."
[^c5]: arxiv-2512-05091 — "The LQ focuses on whether the model pays attention to the visual parts that are relevant to"
[^c6]: arxiv-2512-05091 — "VQ focuses on how accurately this visual trace is grounded"
[^c7]: arxiv-2512-05091 — "they completely fail to generate valid reasoning outputs (scoring zero on R-LQ and R-VQ)"
[^c8]: arxiv-2512-05091 — "guides the model to the correct final answer more effectively even without finer-grained segmentation in the reasoning steps"
[^c9]: arxiv-2512-05091 — "synthetically generated data can contain noise or error samples"
