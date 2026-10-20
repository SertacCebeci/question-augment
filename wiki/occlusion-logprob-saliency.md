---
description: "Occlusion saliency slides a black patch over the image and records how far the chosen answer's log-probability falls; the map shows where an answer leans, and chain-of-thought spreads that lean."
aliases: ["occlusion-based saliency analysis", "occlusion sensitivity map", "sliding-window occlusion", "occlusion impact", "log-probability occlusion map"]
sources: ["arxiv-2512-14989"]
---
# Occlusion log-probability saliency

Occlusion saliency is a localized version of the image-removal test. Instead of blanking the whole picture, one hides a small square of it and asks how much the model's confidence in its chosen answer falls. The procedure, as the chemistry-olympiad study applies it, takes an image I, a question Q with its answer options, and the model's predicted distribution over the options. It targets the chosen option a\*, then slides a k × k mask over the image, filling the masked area with black.[^o1] For each position (i, j) the saliency is the drop in log-probability of a\*: S(i, j) = log f(I, Q)[a\*] − log f(Ĩ(i, j), Q)[a\*], where Ĩ(i, j) is the occluded image. A positive S means the region supports the answer, since hiding it lowers confidence; a negative S means the region suppresses it.[^o5] The study uses patch size k = 56 on a sliding grid with stride 28.[^o3] As one number per question, it reports the occlusion impact, the largest |S| over positions.[^o10]

The method needs only option log-probabilities or logits, not gradients or internal states, so the authors call it model-agnostic and black-box.[^o2] That is what carries it across models. The formal idea is older than this paper: a region is treated as important if removing it changes the output. What survives the transfer from image classifiers is the localization. What does not survive automatically is the reading of the map as an explanation. A high-impact region shows that the answer's probability depends on that patch under a black fill; it does not show that the patch is the evidence a chemist would use.

Applied to chain-of-thought (CoT), the map changes shape. The paper's worked stereochemistry item shows the baseline attention "narrowly confined to a" single superficial cue, one methyl group, and ignoring the stereogenic centre.[^o6] Across items, the authors report that baseline models give large, sharply peaked occlusion impacts, and that CoT spreads reliance over more regions, most clearly on the harder national set.[^o7] The authors' summary is that "higher performance with CoT does not result from simply sharpening attention but from fundamentally" changing how the visual evidence is processed.[^o8] The same study also finds CoT raises confidence on most items: "CoT consistently yields higher confidence than the baseline model, showing the benefit" of step-by-step reasoning.[^o9] Confidence and saliency are two readings of one comparison, not independent confirmations.

So the concept gives a way to ask a different question of a visual answer. Accuracy says whether the answer was right; a whole-image removal says whether the image mattered; an occlusion map says which part of the image the answer leans on and whether that lean is narrow or spread. Narrow and sharp is not a sign of a mistake by itself, and the authors concede that the sharper baseline maps "may appear visually cleaner."[^o11]

## Limits

- One benchmark: 473 four-option chemistry items, one study, multiple-choice only. The saliency comparison is between one baseline and one CoT template, on models the text names; the statistics are not reported as tests in the text read.
- The occluder is a black square, so the masked image can be out of distribution. A drop may come from the artifact rather than from the content removed. The text read does not test other fills.
- One patch size (k = 56, stride 28) is reported. How the maps change with k was not read in the text, so the spread of reliance may partly be a property of the chosen window.
- The map is correlational with the answer's log-probability. "Diffuse" is the authors' word for integrative comparison; that reading is not measured against expert reasoning, though the authors compare it to expert elimination strategies in prose.
- The method targets the chosen option. Reliance on the rejected options, which the authors mention as spillover, is only partly visible in this single-option score.
- Log-probability access is required. For models that expose only final answers, the method does not run.

## Related

- [[counterfactual-image-grounding-audit]] — whole-image blanking tests whether the answer depends on the image at all; occlusion asks which part it depends on
- [[evidence-gain-hallucination-score]] — a whole-image log-probability contrast; a localized version of the same measurement is this note
- [[input-ablation-probability-scoring]] — re-runs the model with inputs removed and reads answer probabilities; occlusion keeps the rest of the input and varies the region
- [[cot-hallucination-trap]] — CoT's visual reliance can be shallow when grounding is weak; a spread-out saliency map is one way to see whether the reasoning engaged the image

[^o1]: arxiv-2512-14989 — "The method estimates the importance of an image region"
[^o2]: arxiv-2512-14989 — "option log-probabilities or logits"
[^o3]: arxiv-2512-14989 — "Saliency maps are computed on a sliding grid with patch size k=56"
[^o5]: arxiv-2512-14989 — "indicates a supportive region"
[^o6]: arxiv-2512-14989 — "attention is narrowly confined to a"
[^o7]: arxiv-2512-14989 — "reliance on a few dominant cues. In contrast, CoT models"
[^o8]: arxiv-2512-14989 — "higher performance with CoT does not result from simply sharpening attention but from fundamentally"
[^o9]: arxiv-2512-14989 — "CoT consistently yields higher confidence than the baseline model, showing the benefit"
[^o10]: arxiv-2512-14989 — "we report the occlusion impact"
[^o11]: arxiv-2512-14989 — "Although baseline heatmaps may appear"
