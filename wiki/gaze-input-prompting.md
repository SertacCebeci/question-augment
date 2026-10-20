---
description: "Giving a multimodal LLM gaze as text coordinates, an overlay or a salience map did not reliably beat the gaze-free baseline on streaming gaze questions, and the best form varied by task."
aliases: ["gaze prompting", "gaze as visual prompt", "gaze input strategies", "salience-map gaze prompt"]
sources: ["arxiv-2512-01707"]
---
# Gaze input prompting

A video model that is not built for gaze can still be handed gaze as an extra input. The StreamGaze paper tests three ways of doing this on Qwen2.5-VL (7B). In the textual prompt, "fixation coordinates are provided alongside the question for each video clip".[^g0] In the visual prompt, "a green dot indicating the gaze center and a red circular region marking the FOV area are overlaid on each frame".[^g1] In the salience-map prompt, "the entire gaze trajectory is aggregated into a single heatmap", given to the model as one extra image.[^g2]

The mechanism is the model's ability to read the cue. The authors' reading of their results is that spatially aggregated cues suit a model better than raw coordinates or per-frame overlays: the salience map gave "the best performance, particularly on present and proactive" tasks.[^g3] Reading Table 3 as printed, the average accuracy is 0.446 without gaze, 0.429 with text or visual prompts, and 0.454 with the salience map. The salience map raises the present-tense score (0.500 to 0.546) and barely moves the proactive one (0.384 to 0.386), while it lowers the past-tense score (0.423 to 0.394). None of the three forms is a consistent gain: "none of the prompting strategies" "consistently outperform the gaze-free baseline".[^g4] The authors conclude that the model "is not inherently equipped to interpret or reason over raw gaze signals".[^g5]

The same pattern appears for reasoning. With GPT-4o, asking the model first to estimate the gaze point, or to box visible objects, changes the tasks unevenly. Visual cues help Scene Recall, but they "can hinder Non-Fixated Object Identification (NFI)", where "excessive focus on gaze regions may suppress exploration of unseen objects".[^g6] So a gaze cue can pull attention to the fixated region and away from the objects the user never looked at, which is exactly what that task asks about.

Our reading: the gap is not only about the format of the cue. The paper also reports that general models "fail to accumulate gaze" over time because they process sparsely sampled frames rather than the stream.[^g7] A gaze cue given once per clip cannot be integrated across a stream the model does not hold in memory.

## Limits

- The prompt ablation uses one model, Qwen2.5-VL at 7B; the reasoning ablation uses GPT-4o. No other model is compared in the sections read, so the finding is not established across models.
- The differences are small. The salience map's average gain over the gaze-free baseline is about 0.8 points, with a loss on past tasks. The text read gives no significance test or variance across runs.
- The input formats follow the earlier EgoGazeVQA work and the authors' choice of three forms. Other encodings of gaze, for example gaze as a learned token or as a temporal sequence, were not tried here.
- The claim is about these forms on this benchmark. It does not say gaze cannot help a model in general; the paper's own finding is that the tested forms did not reliably help.

## Related

- [[gaze-fixation]] — the fixation coordinates that the textual and visual prompts carry to the model.
- [[gaze-scanpath]] — the ordered object sequence, which none of the three prompt forms supplies as such.
- [[imprecise-multimodal-intent-disambiguation]] — gaze as one cue among voice and pointing in a robot's intent step, fused by an LLM rather than shown to a video model.

[^g0]: arxiv-2512-01707 — "fixation coordinates are provided alongside the question for each video clip"
[^g1]: arxiv-2512-01707 — "a green dot indicating the gaze center and a red circular region marking the FOV area are overlaid on each frame"
[^g2]: arxiv-2512-01707 — "the entire gaze trajectory is aggregated into a single heatmap"
[^g3]: arxiv-2512-01707 — "the best performance, particularly on present and proactive"
[^g4]: arxiv-2512-01707 — "consistently outperform the gaze-free baseline"
[^g5]: arxiv-2512-01707 — "is not inherently equipped to interpret or"
[^g6]: arxiv-2512-01707 — "can hinder Non-Fixated Object Identification (NFI)"
[^g7]: arxiv-2512-01707 — "they fail to accumulate gaze"
