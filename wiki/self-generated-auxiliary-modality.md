---
description: "A unified multimodal model can be trained to generate depth and segmentation maps as pixel images and reason over them; training only that generation lifted distance estimation 7.92%."
aliases: ["auxiliary modality generation", "auxiliary visual modalities", "internalized generative capabilities"]
sources: ["arxiv-2512-04563"]
---
# Self-generated auxiliary modality

A model that answers a spatial question from RGB pixels alone must infer depth and object boundaries implicitly. One way to supply them is to have the model produce those signals itself, as images, and then read its own output. The COOPER work does this with a unified multimodal model. Depth maps and segmentation masks are converted into RGB pseudo-images, so that the same generator used for photographs can also produce them.[^c1] The authors name the problem this addresses: "unified MLLMs are optimized to produce photorealistic RGB images, and are not equipped to generate structured non-RGB auxiliary modalities."[^c2]

The mechanism has two stages. In the first, the model learns depth and segmentation in one shared RGB space, "the model jointly learns depth and segmentation, while a designated control token during inference dynamically selects the appropriate decoder" for the map it needs.[^c3] The capability is added without a new architecture or a new objective: the map is trained with the same flow-matching loss as any image.[^c4] In the second stage the model learns to interleave these maps with text. The reasoning trace is a sequence of text segments and visual segments, "the interleaved CoT takes the form" of alternating pieces, and the answer follows.[^c5] The visual segments are not supervised: the authors "do not optimize the visual outputs," reasoning that the model's own generated content would add "noise and target drift."[^c6]

What generation training does on its own is the part most relevant to answering. A variant trained only for auxiliary generation, with no reasoning supervision, reaches "a 7.92% gain on distance and size estimation" according to the abstract.[^c7] The authors read this as evidence that "learning to generate auxiliary modalities helps internalize spatial knowledge and strengthen spatial understanding."[^c8] In the ablation, the same effect is stated as "Internalizing generative capabilities significantly improves" understanding-oriented tasks, and that variant comes "close to the final SFT+RL model" on distance and size estimation.[^c9][^c10]

The choice of map is also task-dependent. The model "tends to generate depth maps" for relative-distance questions and more often highlights target objects in segmentation for situational questions. For geometric reasoning it relies on text, since "additional auxiliary modalities provide almost no benefit in this setting."[^c11]

What this changes for asking and answering, as my inference and not the paper's claim: the medium of an intermediate step is a choice. An answerer can construct a depth map or an object mask before judging a distance, and whether that construction pays depends on the question type. The paper's evidence that training on the construction changes the answer is the stage-one variant, not a test of whether the constructed map is used at inference.

## Limits

- One base model. "We implement COOPER on top" of BAGEL, and the auxiliary-modality claims rest on that backbone.[^c12]
- Two modalities only. "We focus on two widely used signals" (depth and segmentation); the text read does not test other auxiliary signals.[^c13]
- The depth training uses synthetic data, "the synthetic indoor dataset Hypersim" and a synthetic outdoor set, so the depth quality on real scenes is not measured in the parts read.[^c14]
- The quality of generated maps is asserted, not measured against specialist models in the text read: "auxiliary modality generation is comparable to specialized models" is the authors' claim.[^c15]
- The 7.92% figure is on one benchmark: "7.92% gain on Q-SpatialBench, which focuses on distance." The general-benchmark gain is smaller, "a modest overall gain of 4.47%."[^c16][^c17]
- No arm in the read sections corrupts, swaps or randomizes the generated map. So whether the answers depend on the map's content, rather than on the generation training, is not established here (my inference from the tables read).
- The task-dependent choice of map is a reported pattern over benchmark categories. The text does not give per-item rates or variance for it.

## Related

- [[latent-visual-thought]] — visual thoughts kept in hidden states and pinned to a sketch encoder's features; here the intermediate is a decodable pixel map trained with the image loss.
- [[sufficiency-gated-imagination]] — evidence rendered by an external world model and gated per query; here the generator is the answerer itself.
- [[suitability-gated-visual-reward]] — the reward side of when to draw; COOPER's reward uses a label measured from the model's own accuracy rather than a prior label.
- [[staged-perception-decomposition]] — also orders perception inside one model's output, but over text stages, not generated images.

[^c1]: arxiv-2512-04563 — "convert depth maps and segmentation masks into RGB pseudo-images"
[^c2]: arxiv-2512-04563 — "unified MLLMs are optimized to produce photorealistic RGB images"
[^c3]: arxiv-2512-04563 — "the model jointly learns depth and segmentation, while a designated control token during inference dynamically selects the appropriate decoder"
[^c4]: arxiv-2512-04563 — "without changing its architecture or"
[^c5]: arxiv-2512-04563 — "the interleaved CoT takes the form"
[^c6]: arxiv-2512-04563 — "the visual content is generated by the model itself, optimizing it would introduce additional noise and target drift"
[^c7]: arxiv-2512-04563 — "7.92% gain on distance and size estimation"
[^c8]: arxiv-2512-04563 — "learning to generate auxiliary modalities helps internalize spatial knowledge and strengthen spatial understanding"
[^c9]: arxiv-2512-04563 — "Internalizing generative capabilities significantly improves"
[^c10]: arxiv-2512-04563 — "reaching performance close to the final SFT+RL model"
[^c11]: arxiv-2512-04563 — "additional auxiliary modalities provide almost no benefit in this setting"
[^c12]: arxiv-2512-04563 — "We implement COOPER on top"
[^c13]: arxiv-2512-04563 — "We focus on two widely used signals"
[^c14]: arxiv-2512-04563 — "use the synthetic indoor dataset Hypersim"
[^c15]: arxiv-2512-04563 — "auxiliary modality generation is comparable to specialized models"
[^c16]: arxiv-2512-04563 — "7.92% gain on Q-SpatialBench, which focuses on distance"
[^c17]: arxiv-2512-04563 — "it also yields a modest overall gain of 4.47%"
