---
description: "From street imagery, multimodal models rate conventional, well-kept scenes as attractive and miss safety and function the picture does not show, so agreement with residents splits by place type."
aliases: ["design-centric bias", "visual-cue substitution", "image-evident judgment bias", "aesthetic overweighting from images"]
sources: ["arxiv-2512-11827"]
---
# Visible-cue judgment bias

When a model judges a place from a picture of it, the judgment tends to follow what the picture shows. Malekzadeh and colleagues built the setup to test this. Google Street View images were collected around greenspaces that residents of Łódź had mapped; up to ten images per site went to three multimodal models (GPT-4o, Claude 3.5 Haiku, Gemini 2.0 Flash), which gave a binary attractive or unattractive call and up to three free-text reasons. Each model's reasons were then sorted into twelve shared categories and compared with the residents' reasons.[^c1]

The pattern of agreement is uneven. "Agreement is consistently high for attractive formal greenspaces, with Claude (92.4%) showing" the strongest alignment.[^c2] For attractive informal sites, agreement "drops sharply for attractive informal greenspaces, ranging from 16.7% to" 36.1%.[^c3] For unattractive formal sites, agreement stays at 13.6% to 25.0%, which the authors read as models that "tend to default to a positive assessment of parks."[^c4] The reasons show the same shape. Safety is the largest gap: residents mention it often, "but which AI models almost entirely overlook."[^c5] The authors summarize the models as having "overemphasized aesthetic cues and underrepresented functional infrastructure, especially in" informal spaces.[^c6]

The mechanism the authors give starts from the input. "AI models require a visual proxy to process" the environment, and the qualities that make a place attractive to residents are, in their account, ones "that are not readily discernible in visual imagery alone."[^c7][^c8] My inference from this: a model that equates the visible with the valuable would score a neat park well and a rough informal site badly, whatever residents experienced there. The authors' word for the tendency is "design-centric" bias: the models "equate what is visually orderly or well-maintained" with quality.[^c9] This is the authors' interpretation of their results. Nothing in the study varied the image's visibility to isolate it as a cause.

The same paper finds that adding the respondent's socio-demographic profile barely moves these judgments. Their reading is that the output is driven by the image, not by who is asking.[^c10] That is a second route by which the answer ignores the asker: the profile is present in the prompt and does not change what the model sees.

## Limits

- Single city, one survey (N = 407, collected 2019 to 2020), and one image source. The authors note that their approach "restricts evaluations to street- or route-visible perspectives, which may obscure" key qualities of informal or enclosed sites.[^c11]
- The image analysis is exploratory. The authors "conducted an exploratory image analysis focusing on the visual features" and tie the segmentation results to the model's reasons only by association.[^c12]
- The image budget was ten per site, and for large parks the images were chosen by hand. Many areas of big parks went unseen, so part of the gap may come from what was shown to the model, not from the model's judgment.[^c13]
- Whether the bias lies in the models or in the image set is not separated. A model shown a more complete view of an informal site was not tested (my inference from the design).
- The categories were built inductively by the research team, and the agreement figures depend on that coding. A different coding could move the safety gap (my inference; the paper does not test it).

## Related

- [[demographic-conditioning-insensitivity]] — the same paper's persona null: conditioning on a profile does not move the answer, which fits the reading that the image carries the judgment
- [[functional-perception-gap]] — a vision-language model that reads structural images well fails on functional ones; a different domain with the same shape of gap between what the training data shows and what the task needs
- [[perception-substitution-gap]] — a way to tell perception error from reasoning error by replacing the image with text, which would separate the image channel from the model's judgment here

[^c1]: arxiv-2512-11827 — "Each reason provided by participants and AI models was reviewed and assigned to one of twelve"
[^c2]: arxiv-2512-11827 — "Agreement is consistently high for attractive formal greenspaces, with Claude (92.4%) showing"
[^c3]: arxiv-2512-11827 — "agreement drops sharply for attractive informal greenspaces, ranging from 16.7% to"
[^c4]: arxiv-2512-11827 — "positive assessment of parks, potentially overlooking contextual issues less apparent in imagery."
[^c5]: arxiv-2512-11827 — "but which AI models almost entirely overlook."
[^c6]: arxiv-2512-11827 — "overemphasized aesthetic cues and underrepresented functional infrastructure, especially in"
[^c7]: arxiv-2512-11827 — "AI models require a visual proxy to process"
[^c8]: arxiv-2512-11827 — "that are not readily discernible in visual imagery alone."
[^c9]: arxiv-2512-11827 — "they equate what is visually orderly or well-maintained"
[^c10]: arxiv-2512-11827 — "suggesting that adding sociodemographic context to the prompts does not meaningfully influence the models' evaluations."
[^c11]: arxiv-2512-11827 — "Our use of SVI restricts evaluations to street- or route-visible perspectives, which may obscure"
[^c12]: arxiv-2512-11827 — "we conducted an exploratory image analysis focusing on the visual features"
[^c13]: arxiv-2512-11827 — "many areas inevitably remained undocumented, potentially affecting the"
