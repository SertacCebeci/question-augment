---
description: "Answers to semantically linked questions about one image can disagree, polarity against category for instance; the clearer the depicted emotion, the more consistent the answers."
aliases: ["cross-question consistency", "within-item answer consistency"]
sources: ["arxiv-2511-22929"]
---
# Cross-question answer consistency

Some questions about one item are linked by entailment: if the answer to one is fixed, the answer to the other should follow. Such a pair can be checked for agreement without any reference answer. The case study of vision-language models on artworks uses this check. Its example pairs the emotion's polarity with the named emotion: "model, the answers to Q 4 (emotion polarity) and Q 5 (specific emotion) would always match."[^c1] A model that calls an image's emotion negative and then names a joyful emotion has answered two linked questions against each other.

The paper reports that this happens. "We observe inconsistency both within answers and across answers."[^c2] Within an answer, the justification to a yes/no question already names the emotion and its form, so it overlaps with the answers to the later questions about the specific emotion and its expression.[^c3] Across answers, the same image gets different verdicts depending on which question is asked.

The paper's account of the cause is structural and is the authors' own: "they are unable to reflect on the consistency of their output".[^c4] The model produces each answer as text without a separate check on whether the answers cohere. This is the mechanism the paper points to, not one it isolates.

The rate of disagreement depends on the item. "the clearer and more intense the emotion depicted, the more consistently the models answer" — the consistency rises with the intensity the authors rate.[^c5] For images with "subjective, weak, or ambivalent emotions, we often see contradictory answers to the various questions."[^c6] Hedging does not repair this: "not all uncertain statements are" marked as uncertain, and attributions the authors consider unambiguous are weakened.[^c7]

The check is different from the two consistency tests already in the wiki. A paraphrase test asks the same question in other words; a round trip asks the inverse task. The check here asks different questions about one item that are linked by what their answers must imply.

## Limits

- The linked pairs are chosen by the authors. In the sections read, only the Q 4 and Q 5 pair is stated as one that should match; the overlap of Q 3 with Q 5 and Q 6 is described, not scored (my reading).[^c3]
- The disagreement is reported from hand evaluation of 38 images and three models. The sections read give no rate of contradictory pairs, so the size of the inconsistency is not measured here.[^c8]
- The intensity correlation is observed, and the paper relates it to human behaviour through a citation. It is not tested against human agreement in this text.
- Whether a separate consistency check, or a reasoning pass, would reduce the disagreement is not tested; the authors' point is that the models lack such a pass, not that adding one helps.

## Related

- [[bidirectional-reasoning-consistency]] — checks a reasoning chain by running it backward; a consistency test on the direction of one chain, where this note checks different linked questions.
- [[paraphrase-group-hallucination-dispersion]] — the same question reworded; this note concerns different questions whose answers must agree.
- [[round-trip-invertibility-consistency]] — the forward task and its inverse; the linked questions here need not be inverses of each other.
- [[concrete-cue-grounding]] — the disagreement is concentrated on images whose cues are weakest, where the answers split by polarity.

[^c1]: arxiv-2511-22929 — "model, the answers to Q 4 (emotion polarity) and"
[^c2]: arxiv-2511-22929 — "We observe inconsistency both within answers and across answers"
[^c3]: arxiv-2511-22929 — "the models often already identify"
[^c4]: arxiv-2511-22929 — "they are unable to reflect on the consistency of their output"
[^c5]: arxiv-2511-22929 — "more intense the emotion depicted, the more consistently the models answer"
[^c6]: arxiv-2511-22929 — "see contradictory answers to the various questions"
[^c7]: arxiv-2511-22929 — "by the models: not all uncertain statements are"
[^c8]: arxiv-2511-22929 — "We select 38 images of artworks"
