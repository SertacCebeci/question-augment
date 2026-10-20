---
description: "With surface style matched by judge paraphrasing, self-recognition and self-preference rise: the judge then favours the answer whose opinion it already holds."
aliases: ["belief-driven self-preference", "semantic self-recognition", "agreement-based self-preference", "shared-belief bias"]
sources: ["arxiv-2512-05379"]
---
# Shared-belief self-preference

If the stylistic cue behind [[judge-self-recognition]] is removed, the preference does not disappear. The paper tests the obvious next step: the judge paraphrases the competitor's answer so that both candidates read as if the judge wrote them, which should neutralise the superficial cues. The expected result was a further drop in self-preference. The observed result is the opposite: "it increases self-recognition (Figure 11), and increases harmful self-preference (Figure 12)."[^c1]

The authors' reading is that once style no longer separates the two answers, the judge chooses by content: "when the stylistic differences are removed, the judge is relying on semantic differences between the two answers to judge which one was written by itself and which one to favor."[^c2] The concept, then, is that self-recognition and self-preference operate at more than one level. A judge may prefer an answer "because its style resembles the judge's own, or because it expresses an opinion that the judge agrees with."[^c3] The paper's summary is that "when superficial self-recognition is removed, shared belief takes over as the driving force behind self-preference."[^c4]

The two levels were separated with a cross-reasoning design. The judge's chosen label is paired with the competitor's reasoning, and the reverse, so that style and belief pull in opposite directions. For the weaker models the shared belief reinforces their original, wrong answer: "For the weaker models, we observe a negative effect of shared belief."[^c5] The three stronger models do the opposite, and the paper reports that "all three stronger models exhibit a positive self-recognition effect", choosing their own reasoning even against their original selection.[^c6] So the same mechanism that makes a strong judge trust its own errors also makes it switch to its own style when the content is equal.

The paper draws a conclusion about the whole mitigation programme. "This observation reveals the impossibility" of a complete elimination of self-preference, since removing it "would require" decoupling the judge's decisions from what it believes is correct; the authors reframe the research question as "preventing the judge from overly relying on its prior belief."[^c7][^c8] The point for asking and answering is that an evaluator's agreement with a candidate can come from the evaluator's own view of the content, which no change of style will remove. My inference from the design: a judge that is strong enough to know the answer is also strong enough to favour its own answer on content grounds, so a reduction in surface cues cannot be read as a reduction in the judge's stake.

## Limits

- The paraphrase is done by the judge itself, so the competitor's answer is changed in ways the judge chooses. The parts read here show examples (Figure 10) and no numerical check on the paraphrases' fidelity.
- The cross-reasoning result is reported as a trend across models in a figure; the parts read give no per-model numbers and no variance.
- The effect is shown on QuALITY, where correctness is labelled. Whether shared belief drives preference on tasks without a ground truth is not tested, and the paper's own definition of harm depends on that label.
- The paper does not show that belief-level preference can be reduced by any method. It states a reframing, and the experiments only establish that the stylistic route is insufficient.
- Belief and ability are not separated by design: a judge that agrees with a correct opinion and one that agrees with a wrong opinion both fall under the same mechanism, and the paper tells them apart only through the labelled correctness of each answer.

## Related

- [[harmful-self-preference]] — the bias itself, measured against ground-truth labels; this note says where it survives once style is removed
- [[judge-self-recognition]] — the surface half of the same mechanism, and the perturbation that removes it
- [[llm-judge-biases]] — the broad family of judge biases, into which a belief-agreement effect is a further entry

[^c1]: arxiv-2512-05379 — "it increases self-recognition (Figure 11), and increases harmful self-preference (Figure 12)"
[^c2]: arxiv-2512-05379 — "when the stylistic differences are removed, the judge"
[^c3]: arxiv-2512-05379 — "or because it expresses an opinion that the"
[^c4]: arxiv-2512-05379 — "when superficial self-recognition is removed, shared belief takes over as"
[^c5]: arxiv-2512-05379 — "For the weaker models, we observe a negative effect of shared belief"
[^c6]: arxiv-2512-05379 — "all three stronger models exhibit a positive self-recognition effect"
[^c7]: arxiv-2512-05379 — "of a complete elimination of self-preference, which would"
[^c8]: arxiv-2512-05379 — "the judge from overly relying on its prior belief"
