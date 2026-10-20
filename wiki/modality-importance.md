---
description: "Modality importance reads which input decides a label from unimodal predictions: an input that alone recovers the label while the combined input misses it marks the other as misleading."
aliases: ["emotion-dominant modality", "modality importance label", "MI"]
sources: ["arxiv-2512-02699"]
---
# Modality importance

A multimodal input is not a sum of equal channels, and a model can be right on one channel and wrong once the channels are combined. Modality importance (MI) is a per-item label that reads this from the model's own predictions. The model is run on each channel alone and on the combination, and the predicted emotion of each run is compared with the ground truth. In the emotion paper that defines it, a model that is accurate on audio alone but fails on vision alone or on audio and vision together gives the reading that "this suggests that the visual modality may be irrelevant or even misleading", so audio is the emotion-dominant modality.[^c1]

Read off that rule (my reading of the paper's definition), the label sorts items by the pattern of unimodal results. A channel that is right alone and is lost when the other channel is added marks the other channel as misleading. A channel that is right alone and keeps the answer when combined is informative. Where the two channels are equally informative, the label does not pick one: "For samples where audio and video are equally informative, we include both" orderings.[^c2]

The label is used to order generated reasoning. When audio is dominant, the audio-based segment is placed first, and when video is dominant the video-based segment comes first.[^c3] The paper's aim is to keep the reasoning from starting on the less informative channel, the early-anchoring problem described for emotion reasoning in [[visual-forgetting-during-reasoning]]. The reordering is a training-data device; the label itself is the part that transfers. It needs only the target label and the model's own runs on each channel, not an attribution method over gradients or attention.

## Limits

- The label is a property of the model-input pair, not of the world. Where the model is wrong on every single channel, the rule gives no dominant modality. The text read does not say how such items are labelled (my inference from the rule).
- The label is defined by predictions. The text read does not check it against human judgment of which channel carries the emotion, so a "misleading" channel may only be one the model reads poorly.
- The datasets are DFEW and MAFW, which are "large-scale benchmarks covering diverse facial expressions",[^c4] and the backbone is Qwen2.5-7B with HumanOmni initialisation.[^c5] Transfer to other label spaces, other tasks, or non-emotion targets is not tested.
- The downstream effect is small in the paper's own ablation. Reading its Table 5 (my reading), the reordering step moves the consistency metrics by about a point and one metric drops, so the gain is modest.
- The ablation compares reordering against no reordering, not against a random or fixed alternative order. The gain is therefore not attributed to the modality choice in particular (my inference).

## Related

- [[text-modality-dominance]] — reliance measured by corrupting one modality in aggregate; MI is a per-item contrast of unimodal and combined predictions
- [[weak-channel-addition-penalty]] — adding a channel can lower accuracy in aggregate; MI names, item by item, which channel is the misleading one
- [[visual-forgetting-during-reasoning]] — reasoning drifting toward its own generated text, which the MI-based reordering tries to pre-empt

[^c1]: arxiv-2512-02699 — "this suggests that the visual modality may be irrelevant or even misleading"
[^c2]: arxiv-2512-02699 — "For samples where audio and video are equally informative, we include both"
[^c3]: arxiv-2512-02699 — "If audio is the emotion-dominant modality, the audio-based reasoning"
[^c4]: arxiv-2512-02699 — "DFEW [7] and MAFW [6] are large-scale benchmarks covering diverse facial expressions"
[^c5]: arxiv-2512-02699 — "The LLM backbone is Qwen2.5-7B"
