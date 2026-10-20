---
description: "Crossing one minimal image edit with one minimal question edit gives four cells per item; fixed XOR gold labels show whether a model's answer tracks the evidence, the wording, or both."
aliases: ["2x2 minimal-edit family", "XOR family construction", "minimal-edit flip rate (MEFR)"]
sources: ["arxiv-2603-06680"]
---
# Crossed image-text edit families

A single correct answer on a visibility question cannot tell a model that reads the pixels from one that guesses a plausible reply. VB (Tripathi, 2026) therefore builds each item as a family of four cells, (image a, question b) for a, b in {0, 1}: a base photo and a photo changed by one atomic scene change, crossed with a base question and a question edited to flip the claim.[^c1]

## Mechanism

The atomic image edit targets one visibility factor (occlusion, distance, framing) and nothing else. The families were physically re-shot rather than digitally edited, for instance by moving an occluder or stepping closer to a screen.[^c2] For the headline subset the gold labels follow an XOR pattern: the base cell is false, either single edit makes the claim true, and applying both makes it false again.[^c3] The first three cells are scored; the fourth (double flip) is a diagnostic for unintended interactions between the two edits.[^c4]

The metric that exploits the design is the minimal-edit flip rate. I_MEFR is the share of families where the base cell and the image-flip cell are both correct, given the base is correct; T_MEFR is the same for the text flip; MEFR is their mean. Abstention counts as incorrect here, and because the denominator is the number of families with a correct base, it shrinks for models that abstain often, so VB reports the denominators.[^c5]

## What it measured

Nine models were scored on 300 headline items each. For six of nine, T_MEFR exceeded I_MEFR: text-flipped questions were handled more reliably than minimal image edits. The gap was largest for GPT-4o (0.893 vs 0.800) and Gemini 2.5 Pro (0.892 vs 0.743).[^c6] Three models reversed it, among them InternVL3-8B (I_MEFR 0.610 vs T_MEFR 0.373), and the lowest-scoring model had a T_MEFR of 0.180, which the authors link to difficulty with negated questions.[^c7] My reading: a text flip can be solved partly by language alone, while an image flip requires the answer to move because the evidence moved, so a model with high T_MEFR and low I_MEFR is tracking wording more than pixels. The paper states the asymmetry, not this reading.

## Limits

- Only 100 families, 300 scored items per model, all photographed by the authors around one campus; no confidence intervals are given for MEFR.
- The XOR pattern fixes the base cell as false, so the headline subset has no true-base cases and no ABSTAIN gold labels; the authors themselves recommend reporting abstention separately.
- The text edit is a negation or claim flip, so T_MEFR may partly measure negation handling rather than evidence tracking.
- Conditioning on a correct base makes MEFR incomparable across models with very different abstention rates.
- Visibility claims only; the transfer to other question types is untested.

## Related

- [[minimal-edit-belief-revision-benchmark]] — the same before/after logic applied to premise edits in text reasoning
- [[frame-level-answerability-labels]] — builds answerability into the input evidence rather than crossing it with the wording
- [[adversarial-unanswerable-questions]] — edits the question to make it unanswerable, where VB edits the evidence
- [[selective-answer-finalization]] — abstaining as an answer option, which VB scores with partial credit

[^c1]: arxiv-2603-06680 — "This yields four evaluated cells (I a , q b ) for a, b ∈ {0, 1}:"
[^c2]: arxiv-2603-06680 — "In practice, families were re-shot rather than digitally edited, and the atomic change"
[^c3]: arxiv-2603-06680 — "Intuitively, the base cell is designed to be confidently refuted by the photo, while either a text edit"
[^c4]: arxiv-2603-06680 — "The DOUBLE_FLIP cell (Section 4.5) provides a diagnostic for unintended interactions, since"
[^c5]: arxiv-2603-06680 — "For correctness checks, ABSTAIN counts as incorrect."
[^c6]: arxiv-2603-06680 — "T_MEFR exceeds I_MEFR for six of nine models, indicating that text-flipped questions are generally"
[^c7]: arxiv-2603-06680 — "the pattern: InternVL3-8B (I_MEFR 0.610 vs. T_MEFR 0.373), Qwen3-VL-8B (0.307 vs. 0.180),"
