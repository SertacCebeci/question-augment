---
description: "A gaze scanpath is the time-ordered sequence of objects a viewer's fixations land on, with in-view and out-of-view objects kept apart; the order is what the question can refer to."
aliases: ["fixated-object sequence", "gaze scanpath", "object-level scanpath"]
sources: ["arxiv-2512-01707"]
---
# Gaze scanpath

A scanpath is the time-ordered record of where a viewer's gaze settled. In the StreamGaze pipeline it is built at the object level: each fixation contributes the objects inside and outside the field of view during that fixation, and the fixations are kept in the order they occurred. The authors build one per video: "we construct a scanpath S that represents the temporal evolution of gaze-guided object observations".[^s1] The ordering is the content: the scanpath "preserves the temporal order of fixations, thereby capturing how attention shifts across different spatial regions and semantic contexts in the video".[^s2]

The construct matters for how questions are made. From one scanpath the same video yields a question about the next object looked at ("What object does the user gaze at next") and a question about an object that was never looked at ("which did the user never gaze at?").[^s3] The first is answered by a step in the sequence; the distractors of the second are objects the sequence never visits. Without the sequence, neither question has a grounded answer. The authors keep only checked sequences: "Only human-verified scanpaths and object sets" are used for the benchmark.[^s6]

What survives the transfer from eye-tracking is the ordering and the split between visited and unvisited items. Eye-tracking scanpaths are usually sequences of locations, with the saccades between them. The object-level version here keeps the objects at those locations and drops the spatial path between them. This reading is mine, not the paper's; the paper does not discuss the saccades.

## Limits

- The object sets are not raw detector output. Annotators correct "any mislabeled or missing objects and captions" in each fixation episode, and the paper reports an "average correctness rate of approximately 83%".[^s4] The text read does not separate detector error from annotator correction, so the error rate of the sequence itself is not known from it.
- The sequences come from three egocentric sources, cooking, laboratory and assembly. The authors say the benchmark is "in manipulation-centric egocentric environments, leaving" social, navigation and outdoor settings unexplored.[^s5]
- The text reports accuracy by task. It does not report an ablation that shuffles or removes the scanpath order, so whether a model needs the order, or only the set of visited objects, is not tested here.
- A scanpath depends on the fixations under it; its limits are those of [[gaze-fixation]].

## Related

- [[gaze-fixation]] — the fixation is the unit a scanpath orders; the scanpath adds the objects and the order.
- [[implicit-trust-sensing]] — gaze fixations used as an implicit processing measure in a reading study, without any ordered object sequence.

[^s1]: arxiv-2512-01707 — "we construct a scanpath S that represents the temporal evolution of gaze-guided object observations"
[^s2]: arxiv-2512-01707 — "fixations, thereby capturing how attention shifts across different spatial regions and semantic contexts in the video"
[^s3]: arxiv-2512-01707 — "which did the user never gaze at?"
[^s4]: arxiv-2512-01707 — "average correctness rate of approximately 83%"
[^s5]: arxiv-2512-01707 — "in manipulation-centric egocentric environments, leaving"
[^s6]: arxiv-2512-01707 — "Only human-verified scanpaths and object sets"
