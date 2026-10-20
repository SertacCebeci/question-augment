---
description: "Verifying a claim from figure and caption together does no better than from either channel alone for vision-language models, so the two channels are not combined into one judgment."
aliases: ["cross-modal aggregation", "figure-caption fusion gap", "modality combination deficit"]
sources: ["doi-10-48550-arxiv-2506-04585", "arxiv-2512-02231"]
---
# Cross-modal aggregation gap

Scientific evidence is split across two channels, the figure and its caption. The MuSciClaims paper calls the act of combining them cross-modal aggregation, and states the requirement plainly: "Textual reasoning over the caption must be combined with visual reasoning over the figure."[^x1] The test is a three-way comparison. The same claim is judged with figure and caption together, with the caption alone, and with the figure alone. The stated expectation is that "model performance should drop when given either just the figure or the caption."[^x2] If the joint setting does not beat the better single channel, the two channels were not combined into one judgment.

The measured result is that the joint setting does not gain much. Models' performance does not "improve substantially over its performance when using just one modality."[^x3] The paper reads this as a failure of combination: "This indicates that they might not be effectively combining the complementary information present in both modalities."[^x4]

The same three-way test has been run on audio in a speaker benchmark. Each model is scored with vision alone and with vision and audio. Gemini 2.5 Pro "exhibits consistent gains of roughly 10–20 percentage points across all tasks when both modalities are available."[^x8] Qwen3-Omni-30B gains much less, and in some tasks loses accuracy when audio is added, "suggesting that audio input does not reliably improve its reasoning."[^x9] The paper reads the difference between the two models as a difference in fusion rather than in perception. A caveat applies to the vision-only side of the test: the paper observes that "advanced models can occasionally answer certain questions using only visual cues,"[^x10] because speech produces visible signals that "can provide partial evidence about who is speaking or when speech occurs."[^x11] My inference: a vision-only baseline is not a clean absence of audio, so a flat audio gain can come from visual cues that already carry part of the audio's information, not only from a failure to combine the channels.

The reason the combination matters is that the caption holds facts the figure does not show. The paper's example is statistical significance: "information (such as that about statistical significance) in the caption is also important to correctly assess a claim."[^x5] A joint answer has to attach a caption fact, such as a significance threshold, to a figure element, such as a bar, before the verdict. My reading, not the paper's: if the model treats the two channels as separate sources, the joint answer collapses to whichever channel dominates, and that looks like no gain from having both.

## Limits

- The captions are the only text. The paper says that "our dataset is limited to using captions as the textual part of the input to models."[^x6] Context from the methods section, which the paper suggests as a further source, was not tested.
- The claims were filtered to those "clearly and unambiguously supported by the figures."[^x7] For supported claims the figure alone may often suffice, so a flat joint result is partly built into the data. This is my inference; the paper does not test it.
- "Does not improve substantially" is a qualitative reading. The text I read gives no effect size and no significance test for the joint against single-channel comparison. The per-setting table was not read closely enough to report its values here.
- The result is for the vision-language models the paper benchmarks, in zero-shot settings. Whether a model trained to fuse the two channels would show the same flat result is not tested here.

## Related

- [[text-modality-dominance]] — in omni-modal models, corrupting the text hurts far more than corrupting the audio; a joint answer that tracks one channel would look flat in the same way.
- [[aggregation-extraction-gap]] — the cross-document analogue: aggregating facts across sources is answered worse than extracting from one source.
- [[textual-annotation-dependence]] — chart answers rest on printed numerals more than on the plotted marks, another case where one channel carries the answer.

[^x1]: doi-10-48550-arxiv-2506-04585 — "Textual reasoning over the caption must be combined with visual reasoning over the figure"
[^x2]: doi-10-48550-arxiv-2506-04585 — "model performance should drop when given either just the figure or the caption"
[^x3]: doi-10-48550-arxiv-2506-04585 — "improve substantially over its performance when using just one modality"
[^x4]: doi-10-48550-arxiv-2506-04585 — "This indicates that they might not be effectively combining the complementary information present in both modalities"
[^x5]: doi-10-48550-arxiv-2506-04585 — "in the caption is also important to correctly assess a claim"
[^x6]: doi-10-48550-arxiv-2506-04585 — "our dataset is limited to using captions as the textual part of the input to models"
[^x7]: doi-10-48550-arxiv-2506-04585 — "clearly and unambiguously supported by the figures"
[^x8]: arxiv-2512-02231 — "exhibits consistent gains of roughly 10–20 percentage points across all tasks when both modalities are available"
[^x9]: arxiv-2512-02231 — "suggesting that audio input does not reliably improve its reasoning"
[^x10]: arxiv-2512-02231 — "advanced models can occasionally answer certain questions using only visual cues"
[^x11]: arxiv-2512-02231 — "can provide partial evidence about who is speaking or when speech occurs"
