---
description: "At a fixed steering budget, a smooth Gaussian profile over layers outscored random, uniform and box-filter spreads on MASK honesty, so depth shape matters beyond total strength."
aliases: ["Gaussian depth schedule", "depth-wise steering schedule", "layer-wise steering allocation", "steering energy allocation across depth"]
sources: ["arxiv-2512-07667"]
---
# Depth-allocated steering strength

Activation steering adds a vector to the residual stream while the model generates. The vector is usually applied at one layer, and the strength given to each layer is a second choice that the usual method leaves implicit. The paper treats it as the missing axis: "the distribution of steering strength across depth remains an underexplored design degree of freedom."[^c1]

Its answer is a per-layer schedule. For each block ℓ, a direction d_ℓ is taken as the first principal axis of paired honest-versus-dishonest activation differences, and the residual δ_ℓ = α_ℓ d_ℓ is added. The strength α_ℓ follows a normalized Gaussian, exp(−(ℓ−µ)²/2σ²), with a centre µ and width σ. The paper states the design as one that "allocates a fixed steering energy budget across layers according to a smooth distribution."[^c2] Weak intervention lands in early layers, and the profile "peaks in mid-to-late layers where abstract semantic features are better separated."[^c3] Read this way, the schedule changes only where the same total offset is placed; the direction itself is unchanged.

## What was measured

On MASK, which separates honesty from knowledge, the paper steers seven open-weight models from the LLaMA, Qwen and Mistral families. The abstract reports that "Gaussian scheduling improves honesty over no-steering and single-layer baselines" in six of seven models.[^c4] The single-layer comparison is not uniform. On Mistral-7B-Instruct-v0.2 a single layer "reaches a higher peak than Gaussian (40.7" against 32.9.[^c5]

Single-layer edits can also push honesty below the no-steering level. On Qwen-2.5-7B and Qwen-2.5-14B the single-layer scores fall below baseline, and the Gaussian schedule lifts them, to 33.9 and 30.1.[^c6] The paper reads this as the failure mode of a point edit.

The stronger test holds the total steering norm fixed and varies only the allocation. The comparison set is random placement across layers, a uniform split over all layers, and a box filter, which is a band of equal weight centred on the best single layer. On LLaMA-3.1-8B-Instruct and Qwen-2.5-7B-Instruct the Gaussian schedule wins, and the paper concludes that "depth-wise distribution is a decisive factor."[^c7] Its explanation is that smooth spreading avoids both overconcentration and dilution: "point edits and the dilution of flat profiles."[^c8]

Against LoRA fine-tuning on the same honest-versus-dishonest targets, the schedule is not replaced by training. Both improve honesty, and the paper finds that "scheduled steering offers most of the benefit at near-zero deployment cost."[^c9]

## Limits

- The equal-budget ablation covers two models out of seven. Whether the ranking of shapes holds on the other five is not measured.
- The box filter's band is centred "on the best single layer found on MASK," the same benchmark the headline uses.[^c10] Whether that choice favours the baseline less than a fair search would is my reading; the paper does not test a different centre.
- The evaluation depends on an external judge: "our evaluation relies on an external LLM judge with specific prompting."[^c11] The paper says sensitivity to judge and prompt is untested.
- The paper's own limitation is that the study concentrates "on the MASK benchmark, which limits the generalizability of our findings."[^c12]
- The method needs "the ability to inject per-layer steering strengths," so it applies only to open-weight models.[^c13]
- The link to asking and answering is indirect, and this is my inference. The object here is a model's report of a belief under pressure, not question selection or formulation. Nothing in the paper says the depth result transfers to human answerers.

## Related

- [[mean-difference-steering-vector]] — the single-direction offset that this schedule scales layer by layer; that note records the claim that effective control needs "several layers at small coefficients"
- [[redundant-multilayer-knowledge-editing]] — the editing analogue: a single-layer edit fits one depth, and copies across layers trade specificity for reach
- [[cross-layer-probe-ensemble]] — the probe-side counterpart, which weights per-layer verdicts instead of per-layer steering strength

[^c1]: arxiv-2512-07667 — "the distribution of steering strength across depth remains an underexplored design degree of"
[^c2]: arxiv-2512-07667 — "allocates a fixed steering energy budget across layers according to a smooth distribution."
[^c3]: arxiv-2512-07667 — "peaks in mid-to-late layers where abstract semantic features are better"
[^c4]: arxiv-2512-07667 — "Gaussian scheduling improves honesty over no-steering and single-layer baselines"
[^c5]: arxiv-2512-07667 — "steering reaches a higher peak than Gaussian (40.7"
[^c6]: arxiv-2512-07667 — "single-layer steering lowers scores below"
[^c7]: arxiv-2512-07667 — "depth-wise distribution is a decisive factor"
[^c8]: arxiv-2512-07667 — "point edits and the dilution of flat profiles"
[^c9]: arxiv-2512-07667 — "scheduled steering offers most of the benefit at near-zero deployment cost"
[^c10]: arxiv-2512-07667 — "which centers a contiguous band on the best"
[^c11]: arxiv-2512-07667 — "our evaluation relies on an external LLM judge with specific prompting"
[^c12]: arxiv-2512-07667 — "on the MASK benchmark, which limits the generalizability of our findings."
[^c13]: arxiv-2512-07667 — "the ability to inject per-layer steering strengths, which restricts its applicability to"
