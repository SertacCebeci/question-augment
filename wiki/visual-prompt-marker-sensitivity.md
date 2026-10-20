---
description: "Visually prompted benchmarks score the same model differently when only the marker drawn on the image changes in colour, shape, size, label or position, which can reorder a leaderboard."
aliases: ["visually prompted tasks", "visual prompting sensitivity", "visual marker variance"]
sources: ["arxiv-2512-17875"]
---
# Visual-prompt marker sensitivity

A visually prompted task marks regions of an image and asks about them: which of two marked points is closer to the camera, or which marked point corresponds to a reference point.[^c1] The marker is part of the input the benchmark author chose, and the question does not ask about it. A fixed marker convention is therefore easy to overlook. Shu et al. treat it as a variable. The default BLINK marker, a small red circle with a numeric label placed above, was compared with 16 alternative styles spanning colour, shape, marker size, text size, label form and label position. The alternatives were drawn from the visual prompting literature.[^c2]

The effect on accuracy is large. Marker style "can cause accuracy swings of up to 21% on the same image-question pairs"[^c3], and the swings are "often causing ranking reversals among state-of-the-art models."[^c4]

The test is paired. Each alternative marker is compared with the default on the same resampled items, so the difference is attributed to the marker and not to which items were drawn: "because both conditions use the same sampled items."[^c5] The authors also set the variance produced by changing the marker against the variance produced by resampling the dataset, as a ratio R. Values "R ≥ 1 indicate that changing marker style perturbs accuracy at least as much as resampling the test set itself."[^c6] Most markers show significant differences for at least one model, which the authors read as showing that "marker style is not cosmetic."[^c7]

The clearest case in the paper is a reversal on one task. "Llama 4 Scout outperforms Gemini 2.5 Flash under the default red marker for relative depth", and under the blue marker the ranks change.[^c8]

The authors report that the effect is specific to these tasks: "applying the same intervention to more traditional VLM benchmarks does not significantly change the results."[^c9]

What survives the transfer to other settings is the design. Hold the items fixed, vary only the presentation the model reads, and compare that variance with the variance from redrawing items. The number 21% does not transfer. It belongs to four datasets and these marker families.

## Limits

- The study covers nine VLMs and four datasets: BLINK's relative depth and correspondence tasks, plus two larger sets that the authors built by repurposing DA-2K for depth and SPair-71K for correspondence. The 16 styles are the authors' selection, not an exhaustive family.[^c2]
- The scope of the numbers differs between the figure and the introduction. Figure 1 reports "accuracy swings up to 13%"[^c10] for one model on one BLINK task. The 21% figure is the largest swing over all markers and datasets. They are not the same measurement.
- The paper shows that the ranking is unstable under marker changes. It does not show which presentation reflects a model's ability. Any claim that the default marker is the correct one would be mine, not the paper's.
- Implementation effects are part of the same claim. The introduction says that details "imperceptible to humans such as JPEG compression further perturb" results.[^c11] I read the main text through its experiments and the figure captions, not the JPEG section or the appendix, so I make no claim about the size of that effect.
- The authors read the marker effect as a sign that models are "over-reliant on specific visual cues."[^c12] That is their suggestion. The study measures the instability; the mechanism is not isolated in the text I read.

## Related

- benchmark-subset-rank-instability — the other source of leaderboard change in the same paper: redrawing the items, not the marker. The ratio R sets the two against each other.
- [[answer-format-dependent-bias-measurement]] — the same pattern on text: changing only the answer format reverses model orders in a bias measurement.
- [[minimal-edit-prompt-attack]] — a related sensitivity on the text side. There a wording edit moves accuracy; here an edit to the marker on the image does.

[^c1]: arxiv-2512-17875 — "image and asks about relationships within or between images"
[^c2]: arxiv-2512-17875 — "We then create 16 alternative styles (commonly seen in visual prompting literature) spanning 6 categories"
[^c3]: arxiv-2512-17875 — "marker style can cause accuracy swings of up to 21% on"
[^c4]: arxiv-2512-17875 — "often causing ranking reversals among state-of-the-art models"
[^c5]: arxiv-2512-17875 — "because both conditions use the same sampled items."
[^c6]: arxiv-2512-17875 — "least as much as resampling the test set itself."
[^c7]: arxiv-2512-17875 — "marker style is not cosmetic"
[^c8]: arxiv-2512-17875 — "Llama 4 Scout outperforms Gemini 2.5 Flash under the default red marker for relative depth"
[^c9]: arxiv-2512-17875 — "applying the same intervention to more traditional VLM benchmarks does not significantly change the results."
[^c10]: arxiv-2512-17875 — "accuracy swings up to 13%"
[^c11]: arxiv-2512-17875 — "imperceptible to humans such as JPEG compression further perturb"
[^c12]: arxiv-2512-17875 — "over-reliant on specific visual cues."
