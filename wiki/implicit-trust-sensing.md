---
description: "Gaze and autonomic signals (fixations, pupil size, heart rate variability) differed by label and predicted self-reported trust, but they are indirect measures of trust."
aliases: ["physiological trust measures", "implicit trust measures", "psychophysiological trust sensing", "behavioral and physiological trust signals"]
sources: ["arxiv-2512-12348"]
---
# Implicit trust sensing

Trust is usually read from what people say about it. Implicit trust sensing reads it from the eyes and the body while people process the same content: gaze, pupil size and autonomic activity recorded during reading. The claim is that these signals show processing states a self-report can miss. In this lab study they did vary with how health information was labelled.

The mechanism the paper proposes pairs each signal with a reading of attention or arousal. "Saccades, characterized by the frequency and length of eye movements between fixations, often signal" information verification.[^p3] Pupil size is read through load and arousal: "increased pupil dilation, linked to higher cognitive" load may mean deeper processing when a reader is weighing credibility.[^p4] Heart rate variability (HRV) is read in one direction: "with higher HRV indicating lower physiological arousal which is associated with relaxation, comfort,".[^p2] Skin conductance and skin temperature are read the same way, as comfort and engagement. These are the paper's assumptions from prior work, not measurements of trust.

Measured results. In the lab study (N=40, fully within-subjects) "fixation duration and pupil diameter of fixation showed significant differences by information sources and labels" in the label area of the stimulus.[^p5] RMSSD heart rate variability and skin temperature "differed when participants engaged with information with different labels".[^p6] Models trained on these features predicted self-reported binary trust (high vs low) with 73% accuracy, and the source of the information with 65%.[^p9] The models were user-independent, evaluated by leave-one-subject-out, "to ensure that any predictions generalize across all participants".[^p10] The aim was to find where implicit and explicit responses part: "helping to identify discrepancies between the explicit (i.e., self-reported) and implicit trust-related".[^p11]

Combining channels did not help in this data: "combining gaze and physiological features did not improve performance across all models".[^p7]

My inference: a trust measure can carry a sensed channel independent of the self-report, and a mismatch between the two is itself informative. The paper does not test this; it names the mismatch as the goal.

## Limits

- Not a trust measure by itself. "we caution against overinterpreting them as direct indicators of trust, a complex and subjective construct".[^p8]
- Confounds. "Such signals can be influenced by unrelated factors like attention, physical arousal, or contextual noise".[^p12] A fixation or a pupil change may reflect the stimulus layout or fatigue as easily as trust.
- Observation. The authors note that "as being observed might heighten scrutiny of AI-labeled information", so the lab setting may have amplified the label effect itself.[^p13]
- Small and narrow. Forty participants, one lab, and a sample "not representative of the general population".[^p14]
- Single time point, self-report as the anchor. The signals were not checked against any decision or action.
- Prediction numbers are on one split of one design. The paper reports R² 0.35 for trust scores, but the sections read give no majority-class baseline for the 73% binary accuracy, so it cannot be placed against chance here (my inference).

## Related

- [[disclosed-label-trust-effect]] — the self-reported label effect that these signals were recorded beside; the sensing adds an implicit channel to that finding

[^p2]: arxiv-2512-12348 — "with higher HRV indicating lower physiological arousal which is associated with relaxation, comfort,"
[^p3]: arxiv-2512-12348 — "Saccades, characterized by the frequency and length of eye movements between fixations, often signal"
[^p4]: arxiv-2512-12348 — "increased pupil dilation, linked to higher cognitive"
[^p5]: arxiv-2512-12348 — "fixation duration and pupil diameter of fixation showed significant differences by information sources and labels"
[^p6]: arxiv-2512-12348 — "differed when participants engaged with information with different labels"
[^p7]: arxiv-2512-12348 — "combining gaze and physiological features did not improve performance across all models"
[^p8]: arxiv-2512-12348 — "we caution against overinterpreting them as direct indicators of trust, a complex and subjective construct"
[^p9]: arxiv-2512-12348 — "in classifying binary trust levels (high vs. low)"
[^p10]: arxiv-2512-12348 — "to ensure that any predictions generalize across all participants"
[^p11]: arxiv-2512-12348 — "helping to identify discrepancies between the explicit (i.e., self-reported) and implicit trust-related"
[^p12]: arxiv-2512-12348 — "Such signals can be influenced by unrelated factors like attention, physical arousal, or contextual noise"
[^p13]: arxiv-2512-12348 — "as being observed might heighten scrutiny of AI-labeled information"
[^p14]: arxiv-2512-12348 — "was not representative of the general population"
