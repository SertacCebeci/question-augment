---
description: "A one-line map that pins each tagged lesion to its extracted anatomy raised GPT-family lesion-level classification, significantly for GPT-4o, in a prompt-only test."
aliases: ["anatomy-aware prompting", "explicit anatomical grounding", "tag-to-attribute pinning"]
sources: ["arxiv-2512-05537"]
---
# Attribute pinning in the prompt

A model that reads several tagged findings in one text can attach a finding to the wrong attribute, for instance the wrong organ. The incidentaloma study tests a cheap remedy: keep the tagged report as it is, and add a single line that states each tag's attribute, taken from an earlier extraction. The authors call this "a concise mapping that pins each tag to previously extracted anatomy information."[^c1] Its stated purpose is that "This pinning removes residual ambiguity about anatomy assignment while keeping all evidence in situ."[^c2]

Mechanism, in my reading: the pin adds no evidence the report lacks. It states an association the model would otherwise rebuild from the text, and the rebuilding is where errors enter. The pipeline that produced the anatomy labels existed for this reason: its inference "was sometimes limited when relevant anatomy mentions appeared outside the immediate sentence."[^c3] A finding named in one sentence and located in an earlier one is the case the pin is meant to settle.

The comparison is controlled. Both prompts "use the same instruction described in Figure 1 and the same report content,"[^c4] so the pinned line is the only change.

What was measured. The abstract reports that "grounding yielded statistically significant performance gains across GPT-based models" at p < 0.05.[^c5] In the results, "adding anatomical context further improved performance," by up to 0.08 in incidentaloma macro-F1.[^c6] For GPT-4o the gain was tested directly: "GPT-4o (Anatomy) significantly outperformed its base version (p = 0.012)," and GPT-OSS with anatomy also improved over its base.[^c7] On the follow-up cases the counts moved in the same direction: "GPT-4o (Base) missed 10 of 29 (34.5%) such cases," against 7 of 29 with the pin.[^c8] The authors read this as "anatomy-aware prompting improves focus on lesion-specific information."[^c9]

## Limits

- The significance tests resample lesions, "a lesion-level bootstrap analysis restricted to lesions annotated as incidentalomas."[^c10] Lesions cluster within reports, so this may understate uncertainty; that is my inference, not a figure in the paper.
- The pinned value came from a checked pipeline: "we implemented a double-verification process for anatomy extraction."[^c11] The gain is therefore measured with clean anatomy labels. What a noisy extraction would do to the prompt is not tested.
- One attribute (organ, with six or seven categories) on one task, on a test set of "80 double-annotated reports."[^c12] Whether pinning helps for attributes the model must infer, or for free-valued ones, is not shown.
- No arm pins the attribute without tags, so the pin's effect apart from the tags is not measured. Every anatomy prompt was layered on the tagged report.
- Generation used "settings intended to minimize stochastic variation,"[^c13] which fixes sampling but not the prompt wording. Variance across prompt wordings is not reported.
- The Llama results are described as showing "the consistent benefit of anatomy-aware prompting," but the Llama rows of the extracted table are hard to align with their labels, so I do not rely on them here.

## Related

- [[candidate-span-tagging]] — the tags this pin is layered on; the tag says which span is meant, the pin says which organ it belongs to.
- [[medium-context-sweet-spot-for-numeric-prediction]] — another measurement of how much added context helps; there the gain had a sweet spot rather than rising monotonically, and here a single targeted line was added.

[^c1]: arxiv-2512-05537 — "a concise mapping that pins each tag to previously extracted anatomy information"
[^c2]: arxiv-2512-05537 — "This pinning removes residual ambiguity about anatomy assignment while keeping all"
[^c3]: arxiv-2512-05537 — "when relevant anatomy mentions appeared outside the immediate sentence"
[^c4]: arxiv-2512-05537 — "use the same instruction described in Figure 1 and the same report content"
[^c5]: arxiv-2512-05537 — "grounding yielded statistically significant performance gains across GPT-based models"
[^c6]: arxiv-2512-05537 — "adding anatomical context further improved performance"
[^c7]: arxiv-2512-05537 — "GPT-4o (Anatomy) significantly outperformed its base version (p = 0.012)"
[^c8]: arxiv-2512-05537 — "GPT-4o (Base) missed 10 of 29 (34.5%) such cases"
[^c9]: arxiv-2512-05537 — "These trends indicate that anatomy-aware prompting improves focus on lesion-specific information"
[^c10]: arxiv-2512-05537 — "a lesion-level bootstrap analysis restricted to lesions annotated as incidentalomas"
[^c11]: arxiv-2512-05537 — "we implemented a double-verification process for anatomy extraction"
[^c12]: arxiv-2512-05537 — "The held-out test set contains 80 double-annotated reports"
[^c13]: arxiv-2512-05537 — "Generation was performed with settings intended to minimize stochastic variation"

