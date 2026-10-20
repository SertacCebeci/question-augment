---
description: "In controlled corruption of initially congruent video, audio and text, omni-modal models lose most accuracy when text is corrupted and little when audio is, showing a text-heavy reliance."
aliases: ["asymmetric modality reliance", "text bias in omni-modal models"]
sources: ["arxiv-2603-27187"]
---
# Text modality dominance

Natural multimodal data confounds modality reliance with information asymmetry: co-occurring modalities carry correlated but unequal information. OMD-Bench removes this by making all three modalities present the same anchor, then corrupting one at a time, so a drop in accuracy is attributable to the corrupted modality.[^c1]

**Measured asymmetry.** With one modality corrupted, the average drop is only 9 pp, but it is uneven. Text corruption costs about 19.5 pp, vision 6.1 pp, and audio has minimal effect.[^c2] The authors read this as heavy reliance on textual cues even in an omni-modal setting.[^c3] The result is consistent with bimodal findings and is here quantified under controlled intervention in the trimodal case.[^c4]

**Why it matters for asking and answering.** A model that weights text over equally informative video or audio will follow a misleading text prompt or premise, and will not use independent evidence to catch it. That inference is mine; the paper measures accuracy loss, not the premise-following mechanism.

## Limits

- Attribution is cleaner than in natural data but not perfect: corruption methods differ per modality, and a smaller audio effect may reflect how audio is corrupted or how weakly models process it.
- Average over ten models; per-model patterns vary and are in appendix tables not read in full.
- Says nothing about training causes of text bias.

## Related

- [[dissonance-graded-abstention-miscalibration]] — same benchmark, abstention side
- [[calibration]] — reliance without matched confidence is a calibration failure
- [[visual-evidence-scoring]] — scoring how much visual evidence supports an answer

[^c1]: arxiv-2603-27187 — "targets one modality at a time, we can attribute each"
[^c2]: arxiv-2603-27187 — "text corruption causes the steepest decline (mean 19.5 pp), vision a smaller one"
[^c3]: arxiv-2603-27187 — "that current models rely heavily on textual cues"
[^c4]: arxiv-2603-27187 — "et al., 2024b; Zheng et al., 2025) and now quantified through controlled intervention in the trimodal case."
