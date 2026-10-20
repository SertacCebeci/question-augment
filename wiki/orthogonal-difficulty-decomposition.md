---
description: "Difficulty of a video training item splits into a perception-load axis and a reasoning-depth axis that vary independently; one scalar hides which demand is high, so the paper grids them."
aliases: ["Orthogonal Difficulty Decomposition", "two-axis difficulty grid", "multidimensional difficulty"]
sources: ["arxiv-2601-00887"]
---
# Orthogonal difficulty decomposition

A training item is usually ranked by one number: sequence length, model perplexity, or the solver's accuracy on it. For video the VideoCuRL paper argues this is the wrong shape, because two demands vary independently: how much perception a clip requires, and how much reasoning sits on top of what is perceived. "scalar metrics fail to disentangle two orthogonal challenges in video understanding"[^c1] A clip can impose heavy perceptual load while needing only shallow reasoning, or be "visually simple yet demand deep causal reasoning."[^c3]

Collapsing both demands into one value loses which one is high. The paper's phrasing: "Collapsing these orthogonal challenges into a single scalar obscures the distinction between perceptual and cognitive complexity."[^c2] A learner ranked on the scalar can be fed items that are hard for the wrong reason.

## Mechanism

Each item receives two scores, each mapped to [0, 1] by quantile normalization so that the marginal distribution on each axis is uniform.

- The visual-temporal axis, D_visual, is a weighted mix of two training-free measures. The first is motion intensity from dense optical flow, "to capture pixel-wise displacement between consecutive frames."[^c10] The second is the entropy of the histogram of temporal frame differences, which the authors use instead of spatial frame entropy so that static high-texture scenes are not labelled hard.
- The cognitive axis, D_text, is a calibrated surprisal of the answer given the question (see [[calibrated-surprisal]]).

The two scores are the basis of a K × K grid, with K = 4 in the paper. The authors describe the construction as "orthogonal basis for our curriculum grid G."[^c4] The orthogonality is therefore a design choice made by picking two proxies that measure different things; it is not measured from the data in the sections read. Items are then scheduled across the grid (see [[competence-gated-wavefront-curriculum]]).

The grid also drives replay. "VideoCuRL does not uniformly sample historical data"[^c7] but revisits the corner buckets: a high-visual, low-text bucket to keep tracking skills, and a low-visual, high-text bucket to keep deduction skills.

## What the ablation shows

The single-axis ablation is the paper's test of the decomposition, on Qwen2.5-VL-7B trained on Video-R1-260k. With only the visual axis, reasoning benchmarks drop: 1.5 points on VSI-Bench, and the authors conclude that "perception-based scheduling alone is insufficient."[^c5] With only the cognitive axis, the perception benchmark drops: "Removing the visual dimension leads to a 3.1% decline in MVBench."[^c6] Each axis therefore carries information the other lacks, in the paper's measurements.

## Limits

- The two-axis claim is tested only against single-axis variants. The ablation I read does not compare against one scalar fused from the same two proxies, which is the comparison the paper's title needs. The correlation between D_visual and D_text is not reported in the sections read (appendices not read).
- The proxies are checked against training-set accuracy in a correlation figure. The authors report that single motion features are noisy: "individual motion features are insufficient for predicting model failure."[^c9] The cognitive axis shows only a general downward trend with local fluctuations.
- The grid is coarse by design. The authors concede that "of difficulty into a discrete grid, while essential for" orthogonal separation, boundaries are coarse against a continuous difficulty.[^c8]
- The visual proxies may miss difficulty that is not in motion or frame change: "may under-represent the difficulty of visually subtle yet semantically dense scenes."[^c11]
- One base model and one dataset. Transfer to text, images, or other modalities is untested here.

## Related

- [[calibrated-surprisal]] — the cognitive axis's measure, and why raw perplexity is not used
- [[competence-gated-wavefront-curriculum]] — the schedule that walks this grid
- [[difficulty-evidence-decomposition-data-selection]] — another two-part decomposition of selection value, aleatoric versus epistemic; there the parts are different quantities, not two kinds of hardness
- [[zero-variance-group-waste]] — a single-scalar difficulty signal, the within-question reward variance, used in a one-axis setting

[^c1]: arxiv-2601-00887 — "scalar metrics fail to disentangle two orthogonal challenges in video understanding"
[^c2]: arxiv-2601-00887 — "Collapsing these orthogonal challenges into a single scalar obscures the distinction between perceptual and cognitive complexity"
[^c3]: arxiv-2601-00887 — "visually simple yet demand deep causal reasoning"
[^c4]: arxiv-2601-00887 — "orthogonal basis for our curriculum grid G."
[^c5]: arxiv-2601-00887 — "perception-based scheduling alone is insufficient"
[^c6]: arxiv-2601-00887 — "Removing the visual dimension leads to a 3.1% decline in MVBench"
[^c7]: arxiv-2601-00887 — "VideoCuRL does not uniformly sample historical"
[^c8]: arxiv-2601-00887 — "of difficulty into a discrete grid, while essential for"
[^c9]: arxiv-2601-00887 — "individual motion features are insufficient for predicting model failure"
[^c10]: arxiv-2601-00887 — "dense optical flow to capture pixel-wise displacement between consecutive frames"
[^c11]: arxiv-2601-00887 — "may under-represent the difficulty of visually subtle yet semantically dense scenes"
