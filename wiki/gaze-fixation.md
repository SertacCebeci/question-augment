---
description: "A gaze fixation is a run of gaze that stays in one place long enough and over a visually continuous scene; treating those runs as attention events gives video QA usable query moments."
aliases: ["gaze fixation", "fixation extraction", "stable-gaze interval"]
sources: ["arxiv-2512-01707"]
---
# Gaze fixation

A fixation is an interval in which gaze stops moving across the image. The StreamGaze pipeline extracts them from a raw gaze trajectory and treats each one as an attention event. Each fixation is "characterized by a spatial centroid" and a time span, the centroid being the average of the gaze points inside the interval.[^f1]

Three tests decide whether an interval counts. Spatial stability: gaze points must stay "spatially concentrated within a localized region and persist", each within a bounded radius of the centroid.[^f2] Temporal stability: "by requiring that the interval duration exceeds a minimum" length.[^f3] Scene consistency: the frame-wise hue-saturation histograms must still correlate across the interval, "ensuring that scene-consistent fixations are preserved while" discontinuous segments are dropped, so a cut or a camera jump cannot pass as a fixation.[^f4]

The reason for working with fixations rather than raw gaze is the stated one: raw gaze streams are noisy and "contain fast, unstable fluctuations",[^f9] and the authors argue that fixation intervals "more reliably capture users’ visual attention compared to" rapid saccadic shifts.[^f5] The fixation then becomes a query moment: the pipeline selects "time points that likely correspond to meaningful user attention" and asks questions there.[^f6] Around the centroid, a field-of-view region is taken as the pixels within a radius normalised by frame width, following the foveal and parafoveal model of eye-tracking work; objects inside that region count as in view, those outside as out of view.[^f7]

Mechanically, a fixation is a thresholded summary of a noisy signal. Its meaning depends on three numbers the pipeline sets (dispersion radius, minimum duration, scene-correlation threshold) and on the gaze having been projected onto the frame first. Our reading: the fixation is the unit that makes a gaze stream into discrete, askable events; it does not by itself say what the viewer intended.

## Limits

- The thresholds are the authors'. The sections read report the criteria but no sensitivity analysis showing how the fixation count or the questions change when the radius or duration move.
- Gaze arrives in two forms. Some datasets give world gaze that must be projected with camera parameters; "For datasets that directly provide 2D" coordinates, they are used as given.[^f8] Whether the two routes yield comparable fixations is not tested in the text read.
- The reported quality figure belongs to the verified scanpaths and object sets, not to the fixation detector on its own. The paper gives no agreement check of the detector against an eye-tracker's own fixation labels in the sections read.
- All sources are manipulation-centric egocentric video (cooking, laboratory, assembly). Fixation behaviour in social, navigation or outdoor settings is outside what is shown here.
- The claim that fixations capture attention "more reliably" than raw gaze is the authors' premise, cited from the eye-tracking literature; this text does not test it against an alternative.

## Related

- [[gaze-scanpath]] — the ordered sequence of fixations, each with the objects in and out of view.
- [[implicit-trust-sensing]] — fixations used there as a measure of processing during reading, not as a query moment for video QA.

[^f1]: arxiv-2512-01707 — "Each fixation is characterized by a spatial centroid"
[^f2]: arxiv-2512-01707 — "spatially concentrated within a localized region and persist"
[^f3]: arxiv-2512-01707 — "by requiring that the interval duration exceeds a minimum"
[^f4]: arxiv-2512-01707 — "ensuring that scene-consistent fixations are preserved while"
[^f5]: arxiv-2512-01707 — "more reliably capture users’ visual attention compared to"
[^f6]: arxiv-2512-01707 — "that likely correspond to meaningful user attention"
[^f7]: arxiv-2512-01707 — "and parafoveal regions as circular areas around the gaze"
[^f8]: arxiv-2512-01707 — "For datasets that directly provide 2D"
[^f9]: arxiv-2512-01707 — "and contain fast, unstable fluctuations"
